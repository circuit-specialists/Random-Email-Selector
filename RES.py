#!/bin/python

import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
import sys
import random

class RES:
    def __init__(self):
        file_path = self.openDialogWindow()
        csv_file = self.openCSVFile(file_path)
        emails = self.formatFile(csv_file)
        winner_cap = simpledialog.askinteger("Input", "How many winner selections?", parent=self.root, minvalue=1)
        for winner in range(0, winner_cap):
            print("The email: " + str(self.selectWinners(emails)) + " was chosen from " + str(len(emails)) + " emails")
        csv_file.close()

    def openDialogWindow(self):
        self.root = tk.Tk()
        self.root.withdraw()
        return filedialog.askopenfilename()

    def openCSVFile(self, filename):
        csv_file = open(filename, "r", errors='ignore')
        return csv_file

    def formatFile(self, file):
        data = []
        for line in file:
            try:
                data.append(line[:line.index(',')])
            except:
                None
        return data

    def selectWinners(self, emails):
        true_random = random.SystemRandom()
        winner = true_random.choice(emails)
        emails.remove(winner)
        return winner


if __name__ == "__main__":
    main_thread = RES()