import wx,time,string
import os
class main(wx.Frame):
    def __init__(self,parent,title):
        #Creating frame
        wx.Frame.__init__(self,parent, title = title,size = (300,100))
        panel = wx.Panel(self)

        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        b1 = wx.Button(panel,1,"Add the text")
        b2 = wx.Button(panel,2,"About this app")
        b3 = wx.Button(panel,3,"Go home !")

        hsizer.Add(b1,1,wx.EXPAND|wx.ALL,2)
        hsizer.Add(b2,2,wx.EXPAND|wx.ALL,2)
        hsizer.Add(b3,3,wx.EXPAND|wx.ALL,2)
        panel.SetSizer(hsizer)
    
        self.Bind(wx.EVT_BUTTON,self.newdlg,b1)
        self.Bind(wx.EVT_BUTTON,self.info,b2)
        self.Bind(wx.EVT_BUTTON,self.gohome,b3)        

        self.Centre()
        self.Show()
        
    def info(self,e):
        dlg = wx.MessageDialog(self,'This software will definitely help you improve your reading speed and concentration\n Use It regularly for best results','About this software',wx.OK|wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def gohome(self,event):
        #add dialog confirmation
        self.Close(True)

    def newdlg(self,event):
        z = sub(None,-1,'TYPE and READ')

class sub(wx.Frame):
     
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500,400))
        panel1 = wx.Panel(self)

        menubar = wx.MenuBar()
        menu1 = wx.Menu()
        menu2 = wx.Menu()

        menu1.Append(101,"Copy \tCtrl+C",'Copies the text in the box')
        menu1.Append(102,"Cut \tCtrl+X",'Cuts the text in the box')
        menu1.Append(103,"Paste \tCtrl+V",'Pastes the text in the box')
        menu1.AppendSeparator()
        menu1.Append(103,"SelectAll \tCtrl+A",'Selects the entire text in the box')

        wx.EVT_MENU(self,101,self.oncopy)
        wx.EVT_MENU(self,102,self.oncut)
        wx.EVT_MENU(self,103,self.onpaste)
        wx.EVT_MENU(self,103,self.onselectall)
        
        menu2.Append(201,"Help",'How to use this software')
        #wx.EVT_MENU(self,201,self.onhelp)

        menubar.Append(menu1,'Edit')
        menubar.Append(menu2,'About')

        self.t1 = wx.StaticText(panel1,-1,"Enter your text below",style = wx.ALIGN_CENTER |wx.TE_PROCESS_ENTER)
        self.f1 = wx.Font(10,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.t1.SetFont(self.f1)

        self.textb1 = wx.TextCtrl(panel1,-1,pos = (0,19),style = wx.TE_MULTILINE,size = (500,100))

        self.splb1 = wx.Button(panel1,-1,label = "Browse...",pos = (200,120),size = (100,25))
        self.splb1.Bind(wx.EVT_BUTTON,self.browse)
        
        self.t21 = wx.StaticText(panel1,-1,"Browse a text file to read",pos=(0,120),style = wx.ALIGN_CENTER)
        self.f21 = wx.Font(10,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.t21.SetFont(self.f21)
        
        self.t2 = wx.StaticText(panel1,-1,"Read your text here",pos=(0,150),style = wx.ALIGN_CENTER)
        self.f2 = wx.Font(10,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.t2.SetFont(self.f2)

        wx.StaticLine(panel1,-1,(0,167),(500,1))
        self.t3 = wx.StaticText(panel1,-1,"READ HERE",pos=(200,278),style = wx.ALIGN_CENTER)
        self.f3 = wx.Font(15,wx.DEFAULT,wx.NORMAL,wx.BOLD)
        self.t3.SetFont(self.f2)

        #self.t3 = wx.TextCtrl(panel1,-1,pos = (200,278),size = (100,50))
        
        self.t4 = wx.StaticText(panel1,-1,"Words per second:",pos=(100,228),style = wx.ALIGN_CENTER)
        
        self.spinner = wx.SpinCtrl(panel1,-1,'',pos = (200,228),size = (100,20))
        self.spinner.SetRange(float(0.1),10)
        self.spinner.SetValue(1)

        self.button1 = wx.Button(panel1,id = wx.ID_ANY,label = 'Play',pos = (150,168),size = (100,50))
        self.button1.Bind(wx.EVT_BUTTON,self.read)

        self.button2 = wx.Button(panel1,id = wx.ID_ANY,label = 'Pause',pos = (50,168),size = (100,50))
        self.button2.Bind(wx.EVT_BUTTON,self.pause)

        self.button3 = wx.Button(panel1,id = wx.ID_ANY,label = 'Stop',pos = (250,168),size = (100,50))
        self.button3.Bind(wx.EVT_BUTTON,self.stop)

        self.button4 = wx.Button(panel1,id = wx.ID_ANY,label = 'Restart',pos = (350,168),size = (100,50))
        self.button4.Bind(wx.EVT_BUTTON,self.restart)


        self.i = 0

        self.SetMenuBar(menubar)
        self.Show()
    def oncopy(self,e):
        self.textb1.Copy()
    def oncut(self,e):
        self.textb1.Cut()
    def onpaste(self,e):
        self.textb1.Paste()
    def onselectall(self,e):
        pass;
        
    def browse(self,e):
            wildcard = "Text Files (*.txt)|*.txt|" "Word Documents (*.docx)|*.docx|"  "All files (*.*)|*.*"
            dialog = wx.FileDialog(None, "Choose a file", os.getcwd(), "", wildcard, wx.OPEN)
            if dialog.ShowModal() == wx.ID_OK:
                self.openit(dialog.GetPath()) 
                self.read(e)
            dialog.Destroy()

    def openit(self,k):
        f = open(k,"r+")
        l = f.read()
        self.textb1.SetValue(str(l))
        
    def pause(self,e):
        self.timer.Stop()
    
    def restart(self,e):
        self.i = 0
        self.read(wx.EVT_BUTTON)

    def stop(self,event):
        self.i = 0
        self.timer.Stop()

    def typed(self,e):
        l = self.textb1.GetValue()
        word = l.split()
        l = len(word)
        if self.i == l:
            self.timer.Stop()
        else:
            self.t3.SetLabel(word[self.i])
            self.i+=1
            
    def read(self,event):
        self.timer = wx.Timer(self, -1)
        self.Bind(wx.EVT_TIMER, self.typed)
        x = self.spinner.GetValue()
        self.timer.Start(1000/x)
        

app = wx.App()
a = main(None,"DJ")
app.MainLoop()
