#!/bin/python

import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
import sys, random, os

class RES:
    def __init__(self):
        file_path = self.openDialogWindow()
        csv_file = self.openCSVFile(file_path)
        emails = self.formatFile(csv_file)
        csv_file.close()
        winner_cap = simpledialog.askinteger("Input", "How many winner selections?", parent=self.root, minvalue=1)
        winners_dispaly = ""
        winners_write = ""
        for winner in range(0, winner_cap):
            winner_temp = str(self.selectWinners(emails))
            winners_dispaly += (winner_temp + "\t\tOut of: " + str(len(emails) + 1) + "\n").rjust(50)
            winners_write += (winner_temp + ", " + str(len(emails) + 1) + "\n")

        messagebox.showinfo("Winners", "The winners are:\n\n" + winners_dispaly)
        self.saveWinners(file_path, winners_write)

    def openDialogWindow(self):
        self.root = tk.Tk()
        self.root.withdraw()
        return filedialog.askopenfilename()

    def openCSVFile(self, filename):
        csv_file = open(filename, "r", errors='ignore')
        return csv_file

    def formatFile(self, file):
        data = []
        next(file)
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

    def saveWinners(self, file_path, winners):
        winners_csv_file = open(os.path.basename(file_path)[:-4] + " Winners.csv", "w+")
        winners_csv_file.write("Email, Pool Size\n")
        winners_csv_file.write(winners)
        winners_csv_file.close()


if __name__ == "__main__":
    main_thread = RES()