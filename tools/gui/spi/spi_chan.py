#
# Created on Thu Oct 06 2022 6:53:58 AM
#
# The MIT License (MIT)
# Copyright (c) 2022 Aananth C N
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
import tkinter as tk
from tkinter import ttk

import gui.lib.window as window

import gui.lib.asr_widget as dappa # dappa in Tamil means box



class SpiChannelTab:
    n_spi_chans = 0
    max_spi_chans = 255
    n_spi_chans_str = None

    gui = None
    tab_struct = None # passed from *_view.py file
    configs = [] # all Spi configs tkinter strings are stored here.

    header = ["label", "SpiChannelId", "SpiChannelType", "SpiDataWidth", "SpiDefaultData", "SpiEbMaxLength",
              "SpiIbNBuffers", "SpiTransferStart"]
    header_objs = 12 #Objects / widgets that are part of the header and shouldn't be destroyed
    header_size = 3
    non_header_objs = []
    dappas_per_row = len(header)

    def __init__(self, gui):
        self.gui = gui
        self.n_spi_chans = 0
        self.n_spi_chans_str = tk.StringVar()

        #spi_channel = arxml_spi.parse_arxml(gui.arxml_file)
        spi_channel = None
        if spi_channel == None:
            return 
        for chan in spi_channel:
            if "SpiChannelId" in chan:
                self.init_spi_chan(chan)


    def __del__(self):
        del self.n_spi_chans_str
        del self.non_header_objs[:]


    def create_empty_spi_chan(self):
        spi_chan = {}
        spi_chan["label"] = "Spi Channel #"
        spi_chan["SpiChannelId"] = str(self.n_spi_chans-1)
        spi_chan["SpiChannelType"] = "IB"
        spi_chan["SpiDataWidth"] = "4" # bytes
        spi_chan["SpiDefaultData"] = "0xAA551234"
        spi_chan["SpiEbMaxLength"] = "65535"
        spi_chan["SpiIbNBuffers"] = "65535"
        spi_chan["SpiTransferStart"] = "MSB"
        return spi_chan



    def draw_dappa(self, i):
        dappa.label(self, "Spi Channel #", self.header_size+i, 0, "e")

        # SpiChannelId
        dappa.entry(self, "SpiChannelId", i, self.header_size+i, 1, 10, "readonly")

        # SpiChannelType
        values = ("IB (Internal Buffer)", "EB (External Buffer)")
        dappa.combo(self, "SpiChannelType", i, self.header_size+i, 2, 17, "readonly", values)

        # SpiDataWidth
        dappa.spinb(self, "SpiDataWidth", i,self.header_size+i, 3, 13, "normal", tuple(range(1,33)))

        # SpiDefaultData
        dappa.entry(self, "SpiDefaultData", i, self.header_size+i, 4, 17, "normal")

        # SpiEbMaxLength
        dappa.spinb(self, "SpiEbMaxLength", i, self.header_size+i, 5, 13, "normal", tuple(range(0,65536)))

        # SpiIbNBuffers
        dappa.spinb(self, "SpiIbNBuffers", i, self.header_size+i, 6, 13, "normal", tuple(range(0,65536)))

        # SpiTransferStart
        values = ("MSB", "LSB")
        dappa.combo(self, "SpiTransferStart", i, self.header_size+i, 7, 10, "readonly", values)



    def delete_dappa_row(self):
        objlist = self.non_header_objs[-self.dappas_per_row:]
        for obj in objlist:
            obj.destroy()
        del self.non_header_objs[-self.dappas_per_row:]



    def update(self):
        # destroy most old gui widgets
        self.n_spi_chans = int(self.n_spi_chans_str.get())

        # Tune memory allocations based on number of rows or boxes
        n_dappa_rows = len(self.configs)
        if self.n_spi_chans > n_dappa_rows:
            for i in range(self.n_spi_chans - n_dappa_rows):
                self.configs.insert(len(self.configs), dappa.AsrCfgStr(self.header, self.create_empty_spi_chan()))
                self.draw_dappa(n_dappa_rows+i)
        elif n_dappa_rows > self.n_spi_chans:
            for i in range(n_dappa_rows - self.n_spi_chans):
                self.delete_dappa_row()
                del self.configs[-1]

        # Support scrollable view
        self.scrollw.scroll()



    def draw(self, tab):
        self.tab_struct = tab
        self.scrollw = window.ScrollableWindow(tab.frame, tab.xsize, tab.ysize)
        
        #Number of modes - Label + Spinbox
        label = tk.Label(self.scrollw.mnf, text="No. of Channels:")
        label.grid(row=0, column=0, sticky="w")
        spinb = tk.Spinbox(self.scrollw.mnf, width=10, textvariable=self.n_spi_chans_str, command=lambda : self.update(),
                    values=tuple(range(0,self.max_spi_chans+1)))
        self.n_spi_chans_str.set(self.n_spi_chans)
        spinb.grid(row=0, column=1, sticky="w")

        # Save Button
        genm = tk.Button(self.scrollw.mnf, width=10, text="Save Configs", command=self.save_data, bg="#206020", fg='white')
        genm.grid(row=0, column=2)

        # Update buttons frames idle tasks to let tkinter calculate buttons sizes
        self.scrollw.update()

        # Table heading
        dappa.heading(self, 2)
        
        self.update()



    def save_data(self):
        # self.backup_data()
        self.tab_struct.save_cb(self.gui)
