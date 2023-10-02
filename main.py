from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import colorchooser

showStatusbar=True
showToolbar=True
url=""
fontFamily='Arial'
fontSize=12
textChanged=False


class MainMenu(Menu):
    def __init__(self, parent, *args, **kwargs):
        Menu.__init__(self, parent, *args, **kwargs)
        self.parent=parent

        ###File_menu###
        """self.new_icon=PhotoImage(file='icons/new.png')
        self.open_icon=PhotoImage(file='icons/open.png')
        self.save_icon=PhotoImage(file='icons/save.png')"""
        
        self.file=Menu(self, tearoff=0)
        
        """self.file.add_command(label='New', image=self.new_icon, compound=LEFT, accelerator="Ctrl+N")
        self.file.add_command(label='Open', image=self.open_icon, compound=LEFT, accelerator="Ctrl+O")
        self.file.add_command(label='Save', image=self.save_icon, compound=LEFT, accelerator="Ctrl+S")"""
        
        self.file.add_command(label='New', compound=LEFT, accelerator="Ctrl+N", command=self.parent.newFile)
        self.file.add_command(label='Open', compound=LEFT, accelerator="Ctrl+O")
        self.file.add_command(label='Save', compound=LEFT, accelerator="Ctrl+S")
        self.file.add_command(label='Save as', compound=LEFT, accelerator="Ctrl+Alt+S")
        self.file.add_command(label='Exit', compound=LEFT)
        
        ###Edit_menu###
        
        self.edit=Menu(self, tearoff=0)
        self.edit.add_command(label='Copy', compound=LEFT, accelerator="Ctrl+C")
        self.edit.add_command(label='Paste', compound=LEFT, accelerator="Ctrl+V")
        self.edit.add_command(label='Cut', compound=LEFT, accelerator="Ctrl+X")
        self.edit.add_command(label='Clear All', compound=LEFT, accelerator="Ctrl+Alt+C")
        self.edit.add_command(label='Find', compound=LEFT, accelerator="Ctrl+F")
        
        ###view menu###
    
        global showStatusbar
        global showToolbar
            
        self.view=Menu(self, tearoff=0)
        self.view.add_checkbutton(onvalue=True, offvalue=False, label="Tool Bar", variable=showToolbar)
        self.view.add_checkbutton(onvalue=True, offvalue=False, label="Status Bar", variable=showStatusbar)
        
        ###themes menu###
        
        self.themes=Menu(self, tearoff=0)
        self.color_list = {
            
            'Default':      '#000000.#FFFFFF',# first one is a font color, second is the bg color
            'Tomato' :      '#ffff00.#ff6347',
            'LimeGreen' :   '#fffff0.#32cd32',
            'Magenta'  :    '#fffafa.#ff00ff',
            'RoyalBlue' :   '#ffffbb.#4169e1',
            'MediumBlue' :  '#d1e7e0.#0000cd',
            'Dracula' :     '#ffffff.#000000'
                      
        }
        
        self.theme_choise=StringVar()
        for i in sorted(self.color_list):
            self.themes.add_radiobutton(label=i, variable=self.theme_choise)
        
        self.add_cascade(label='File', menu=self.file)
        self.add_cascade(label='Edit', menu=self.edit)
        self.add_cascade(label='View', menu=self.view)
        self.add_cascade(label='Theme', menu=self.themes)
        
        
        
        
        
class TextEditor(Text):
    def __init__(self, parent, *args, **kwargs):
        Text.__init__(self, parent, *args, **kwargs)
        self.parent=parent
        self.config(wrap='word') 
        self.pack(expand=YES, fill=BOTH)   
        self.config(relief=FLAT)
        xscrollbar=Scrollbar(self, orient=HORIZONTAL)
        xscrollbar.pack(side=BOTTOM, fill=X)
        yscrollbar=Scrollbar(self, orient=VERTICAL)
        yscrollbar.pack(side=RIGHT, fill=Y)
        xscrollbar.config(command=self.xview)
        yscrollbar.config(command=self.yview)


class StatusBar(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.parent=parent
        self.pack(side=BOTTOM)
        self.config(text='Status Bar')
        
class ToolBar(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.parent=parent
        self.pack(side=TOP, fill=X)
        
        
#############################ToolBox##############################

        self.cbFont=ttk.Combobox(self)
        self.cbFontSize=ttk.Combobox(self)
        self.cbFont.pack(side=LEFT, padx=(5,10))
        self.cbFontSize.pack(side=LEFT)

        #######################FONT###############################

        #self.boldIcon=PhotoImage(file='icons/bold.png')
        btnBold=Button(self, command=self.parent.changeBold)#,"""image=self.boldIcon""")
        btnBold.pack(side=LEFT,padx=5)
        ##########################################################
        #self.italicIcon=PhotoImage(file='icons/italic.png')
        btnItalic=Button(self, command=self.parent.changeItalic)#,"""image=self.italicIcon""")
        btnItalic.pack(side=LEFT,padx=5)
        ##########################################################
        #self.underlineIcon=PhotoImage(file='icons/underline.png')
        btnUnderline=Button(self, command=self.parent.changeUnderline)#,"""image=self.underlineIcon""")
        btnUnderline.pack(side=LEFT,padx=5)
        ##########################################################
        #self.fontcolorIcon=PhotoImage(file='icons/fontcolor.png')
        btnFontColor=Button(self, command=self.parent.changeFontColor)#,"""image=self.fontcolorIcon""")
        btnFontColor.pack(side=LEFT,padx=5)
        ##########################################################
        #self.alignleftIcon=PhotoImage(file='icons/alignleft.png')
        btnAlignLeft=Button(self, command=self.parent.alignLeft)#,image=self.alignleftIcon)
        btnAlignLeft.pack(side=LEFT,padx=5)
        ##########################################################
        #self.aligncenterIcon=PhotoImage(file='icons/aligncenter.png')
        btnAlignCenter=Button(self, command=self.parent.alignCenter)#,image=self.aligncenterIcon)
        btnAlignCenter.pack(side=LEFT,padx=5)
        ##########################################################
        #self.alignrightIcon=PhotoImage(file='icons/alignright.png')
        btnAlignRight=Button(self, command=self.parent.alignRight)#,image=self.alignrightIcon)
        btnAlignRight.pack(side=LEFT,padx=5)
        
        ###############################################################
        
        fonts=font.families()
        fontList=[]
        fontSizeList=[]
        
        for i in range (8,80):
            fontSizeList.append(i)
        for i in fonts:
            fontList.append(i)
        self.fontVar=StringVar()
        self.cbFont.config(values=fontList, textvariable=self.fontVar)
        self.cbFont.current(0)
        self.cbFontSize.config(values=fontSizeList)
        self.cbFontSize.current(4)
        
        ##########bind-method###########
        
        self.cbFont.bind("<<ComboboxSelected>>", self.parent.getFont)
        self.cbFontSize.bind("<<ComboboxSelected>>", self.parent.getFontSize)
        
        
class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent=parent
        self.pack(fill=BOTH, expand=True)
               
        #widget
        self.main_menu=MainMenu(self)
        self.toolbar=ToolBar(self)
        self.texteditor=TextEditor(self)
        self.statusbar=StatusBar(self)
        
        
        #parent menu configuration
        self.parent.config(menu=self.main_menu)
        
        #setting focus
        self.texteditor.focus()
        self.texteditor.configure(font='arial 12')
        self.texteditor.bind('<<Modified>>', self.changed)
    
    def newFile(self,*args):
        global url
        try:
            url=""
            self.texteditor.delete(1.0, END)
        except:
            pass
    
        
    def changed(self,*args):
        global textChanged
        flag=self.texteditor.edit_modified()
        textChanged = True
        print(flag)
        if flag:
            words=len(self.texteditor.get(1.0, 'end-1c').split())
            letters=len(self.texteditor.get(1.0, 'end-1c'))
            self.statusbar.config(text="Characters " +str(letters)+ "    Words: "+str(words))
        self.texteditor.edit_modified(False)
        
        
        
    def getFont(self,*args):  
        global fontFamily
        fontFamily=self.toolbar.cbFont.get()
        self.texteditor.configure(font=(fontFamily, fontSize))
        
    def getFontSize(self,*args):  
        global fontSize
        fontSize=self.toolbar.cbFontSize.get()
        self.texteditor.configure(font=(fontFamily, fontSize))
        
    def changeBold(self,*args):
        text_pro=font.Font(font=self.texteditor['font'])
        print(text_pro.actual('weight'))
        if text_pro.actual('weight')=='normal':
            self.texteditor.configure(font=(fontFamily,fontSize,'bold'))
        elif text_pro.actual('weight')=='bold':
            self.texteditor.configure(font=(fontFamily,fontSize,'normal')) 
    
    def changeItalic(self,*args):
        text_pro=font.Font(font=self.texteditor['font'])
                
        if text_pro.actual('slant')=='roman':
            self.texteditor.configure(font=(fontFamily,fontSize,'italic'))
        elif text_pro.actual('slant')=='italic':
            self.texteditor.configure(font=(fontFamily,fontSize,'roman')) 
    
    def changeUnderline(self,*args):
        text_pro=font.Font(font=self.texteditor['font'])
        if text_pro.actual('underline')==0:
            self.texteditor.configure(font=(fontFamily,fontSize,'underline'))
            print("1")
        elif text_pro.actual('underline')==1:
            self.texteditor.configure(font=(fontFamily,fontSize,'normal'))
            print("0")
    
    def changeFontColor(self, *args):
        color = colorchooser.askcolor()
        print(color)
        self.texteditor.configure(fg=color[1])
    
    def alignLeft(self):
        content = self.texteditor.get(1.0, 'end')
        self.texteditor.tag_config('left', justify=LEFT)
        self.texteditor.delete(1.0, 'end')
        self.texteditor.insert(INSERT, content, 'left')
        
    def alignCenter(self):
        content = self.texteditor.get(1.0, 'end')
        self.texteditor.tag_config('center', justify=CENTER)
        self.texteditor.delete(1.0, 'end')
        self.texteditor.insert(INSERT, content, 'center')        
        
    def alignRight(self):
        content = self.texteditor.get(1.0, 'end')
        self.texteditor.tag_config('right', justify=RIGHT)
        self.texteditor.delete(1.0, 'end')
        self.texteditor.insert(INSERT, content, 'right') 
    
if __name__=="__main__":
    root=Tk()
    root.title("Text Editor")
    MainApplication(root).pack(side=TOP, fill=BOTH, expand=True)
    root.iconbitmap('icons')
    root.geometry("1000x550")
    root.mainloop()
