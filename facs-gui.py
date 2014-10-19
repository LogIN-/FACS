#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: login
# @Date:   2014-10-19 18:11:22
# @Last Modified by:   login
# @Last Modified time: 2014-10-19 18:58:00
from ttk import Frame, Button, Label, Style
from Tkinter import Tk, BOTH
import tkFileDialog
import tkMessageBox as box



class FACSMainWindow(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)         
        self.parent = parent        
        self.initUIConstants()
        self.initUI()

        self.inputDirectory = ""
        self.outputDirectory = ""

    def initUIConstants(self):
        # defining options for opening a directory
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = self
        options['title'] = 'Select directory for FACS:'


    def initUI(self):
      
        self.parent.title("FACS machine output analyzer")
        self.style = Style()
        self.style.theme_use("default")        
        self.pack()

        inputDir = Button(self, text='Select input directory', command=self.askInputDirectory)
        inputDir.grid(row=0, column=1)

        outputDir = Button(self, text="Select output directory", command=self.askOutputDirectory)
        outputDir.grid(row=1)

        processFiles = Button(self, text="Process", command=self.processData)
        processFiles.grid(row=2)


    def onError(self):
        box.showerror("Error", "Could not open file")
        
    def onWarn(self):
        box.showwarning("Warning", "Deprecated function call")
        
    def onQuest(self):
        box.askquestion("Question", "Are you sure to quit?")
        
    def onProcessingEnd(self):
        box.showinfo("Information", "Processing complete!\n\nOutput location" + self.outputDirectory)
         
    def askInputDirectory(self):
        """Returns a selected directoryname."""
        self.inputDirectory = tkFileDialog.askdirectory(**self.dir_opt)    

    def askOutputDirectory(self):
        """Returns a selected directoryname."""
        self.outputDirectory = tkFileDialog.askdirectory(**self.dir_opt)

    def processData (self):
        self.onProcessingEnd(); 

def main():
  
    root = Tk()
    ex = FACSMainWindow(root)
    root.geometry("300x150+300+300")
    root.mainloop()  


if __name__ == '__main__':
    main()  