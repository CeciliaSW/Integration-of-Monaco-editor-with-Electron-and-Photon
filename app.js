const {app, Menu, BrowserWindow}  =  require('electron');
const url = require('url');
const path  = require('path');
const {ipcMain} = require('electron');
const {dialog} = require('electron');
const fs = require('fs');

app.on('before-quit',  ()=> {
    console.log('Saliendo...');
});

let win;

createWindow = function(){

    win =  new BrowserWindow({
        width: 800, 
        height: 700, 
        title: '...',
        center: true, 
        frame:false,
        maximizable: false, 
        webPreferences:{
            nodeIntegration:true, 
            contextIsolation: false,
            enableRemoteModule:true
        }
    }); 

    win.loadURL(
        url.format({
            pathname: path.join(__dirname, 'index.html'),
            protocol:'file',
            slashes:true
        })
    );
}

app.on('browser-window-created', (e,window) => {
    window.setMenu(null);
});

    ipcMain.on('maximize', () => {
    BrowserWindow.getFocusedWindow()?.maximize();
    });

    ipcMain.on('unmaximize', () => {
    BrowserWindow.getFocusedWindow()?.unmaximize();
    });

    ipcMain.on('isMaximized', (event) => {
    if(!BrowserWindow.getFocusedWindow()?.isMaximized()){
        BrowserWindow.getFocusedWindow()?.maximize();
    }else{
        BrowserWindow.getFocusedWindow()?.unmaximize();
    }
    event.returnValue = BrowserWindow.getFocusedWindow()?.isMaximized();
    });

    ipcMain.on('minimize', () => {
    BrowserWindow.getFocusedWindow()?.minimize();
    });

    ipcMain.on('close', () => {
    BrowserWindow.getFocusedWindow()?.close();
    });

    ipcMain.on('show-context-menu', (event) => {
        const template = [
            {
                label: 'Developer tools',
                role: 'toggledevtools'
            }
        ];
    
        const menu =  Menu.buildFromTemplate(template);
        menu.popup(BrowserWindow.fromWebContents(event.sender));
    });

    ipcMain.on('openFile', async (event, args)=> {
    
    const  chosenFolders =  await dialog.showOpenDialog(win,{properties:['openFile']});
    var pathFile  =  chosenFolders.filePaths[0];

    fs.readFile(pathFile,'utf8',(err, data)=> {
        if(err) {
            dialog.showMessageBox(win, {
                message:'Error al leer el archivo seleccionado.',
                buttons: ['Aceptar']
            });
            return;
        }
        event.sender.send('datosarchivo',data); 
    });

});

ipcMain.on('saveFile',async (event, args)=> {

    var path  =  await dialog.showSaveDialog(win,{properties:[]});

    fs.writeFile(path.filePath, args, (err)=> {
        if(err){
            console.log(err);
        }
    });

});

app.on('ready', createWindow);