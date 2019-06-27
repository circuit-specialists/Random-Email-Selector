#!/bin/python

import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
import sys
import random

class RES:
    def __init__(self):
        file_path = self.openDialogWindow()
        csv_file = self.openCSVFile(file_path)
        emails = self.formatFile(csv_file)
        csv_file.close()
        winner_cap = simpledialog.askinteger("Input", "How many winner selections?", parent=self.root, minvalue=1)
        winners = ""
        for winner in range(0, winner_cap):
            winners += (str(self.selectWinners(emails)) + "\tOut of: " + str(len(emails)) + "\n").rjust(50)

        messagebox.showinfo("Winners", "The winners are:\n\n" + winners)
        self.saveWinners(winners)

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

    def saveWinners(self, winners):
        winners_csv_file = open("winners.csv", "w+")
        winners_csv_file.write(winners)
        winners_csv_file.close()


if __name__ == "__main__":
    main_thread = RES()