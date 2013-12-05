#!/usr/bin/env python
4
import pickle
import wx

class MainFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, wx.DefaultPosition, wx.Size(1000, 700))

        panel = wx.Panel(self, -1)

        self.list = wx.ListCtrl(self, -1, style=wx.LC_LIST)

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(wx.ListCtrl(panel, -1, style=wx.LC_LIST), 1)

        self.list.InsertColumn(0, 'Artist')
        self.list.InsertColumn(1, 'Album')
        self.list.InsertColumn(2, 'Title')

        self.list.SetColumnWidth(0, 150)
        self.list.SetColumnWidth(1, 150)
        self.list.SetColumnWidth(2, 150)

        self.SetSizer(box)
        self.Centre()
        self.Show(True)

class MainApp(wx.App):
    def OnInit(self):
        frame = MainFrame(None, -1, 'Juke')

        return 1

app = MainApp(0)
app.MainLoop()
