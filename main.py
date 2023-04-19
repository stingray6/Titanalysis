# Importing libraries
import pandas as pd
import seaborn as sns
import os
import matplotlib.pyplot as plt

# Importing data file
path = os.getcwd() + r"\files\train.csv"
titanic_data = pd.read_csv(path)

# Style
sns.set_style('darkgrid')


class Plot:
    def __init__(self, data_frame):
        self.data_frame = data_frame

    def show(self):
        pass


# Option 1
class Histogram(Plot):
    def __init__(self, data_frame, column_name, bins=10):
        super().__init__(data_frame)
        self.column_name = column_name
        self.bins = bins

    def show_column(self, column_name):
        self.data_frame[column_name].hist(bins=self.bins)
        plt.show()

    def show(self):
        self.show_column(self.column_name)


# Option 2
class Scatter(Plot):
    def __init__(self, data_frame, x="Age", y="Fare"):
        super().__init__(data_frame)
        self.x = x
        self.y = y

    def show_column(self, x, y):
        self.data_frame.plot.scatter(x, y)
        plt.show()

    def show(self):
        self.show_column(self.x, self.y)


# Option 3
class Line(Plot):
    def __init__(self, data_frame, x="Age", y="Fare"):
        super().__init__(data_frame)
        self.x = x
        self.y = y

    def show_column(self, x, y):
        self.data_frame.plot.line(x, y)
        plt.show()

    def show(self):
        self.show_column(self.x, self.y)


def create_histogram(data_frame):
    print("Available fields: ")
    for element in data_frame.columns:
        print(element)

    print("Specify column name: ")
    column_name = input("> ")

    if column_name not in data_frame:
        column_name = 'Age'
    print("Specify number of bins: ")
    bins = int(input("> "))
    age_histogram: Plot = Histogram(data_frame, column_name, bins)

    return age_histogram


def create_scatter_plot(data_frame):
    print("Available fields: ")
    for element in data_frame.columns:
        print(element)

    print("Specify x axis: ")
    x = input("> ")
    if x not in data_frame:
        x = 'Age'

    print("Specify y axis: ")
    y = input("> ")
    if y not in data_frame:
        y = 'Fare'

    age_fare_scat: Plot = Scatter(data_frame, x, y)

    return age_fare_scat


def create_line_plot(data_frame):
    print("Available fields: ")
    for element in data_frame.columns:
        print(element)

    print("Specify x axis: ")
    x = input("> ")
    if x not in data_frame:
        x = 'Age'

    print("Specify y axis: ")
    y = input("> ")
    if y not in data_frame:
        y = 'Fare'

    line_plot: Plot = Line(data_frame, x, y)

    return line_plot


class PlotMenu:
    def __init__(self, data_frame):
        self.current_plot: Plot = None
        self.option = None
        self.data_frame = data_frame

    def show(self):
        print("1 - Create histogram\n"
              "2 - Create scatter plot\n"
              "3 - Create line plot\n")
        self.option = input("> ")
        if self.option == "1":
            self.current_plot = create_histogram(self.data_frame)
        elif self.option == "2":
            self.current_plot = create_scatter_plot(self.data_frame)
        elif self.option == "3":
            self.current_plot = create_line_plot(self.data_frame)
        elif self.option == "4":
            self.current_plot = create_bar_plot(self.data_frame)
        else:
            self.current_plot = None
            print("Error: invalid option. Please try again: ")
            self.show()
        if self.current_plot is not None:
            self.current_plot.show()


# Printing options screen
def show_start_screen():
    options = {1: "Show data as a table",
               2: "Show a plot",
               0: "Exit"}

    print("### - TITANIC ANALYSIS - ###\n"
          "This program can be used to explore data related to Titanic ship catastrophe.\n")
    for element in options:
        print(f"{element} - {options[element]}\n")
    print("Enter a number to proceed:")


# Option 1
def show_table():
    print(titanic_data.to_string())


# Menu
def menu_loop():
    menu = 1
    plot_menu = PlotMenu(titanic_data)

    while menu != 0:
        show_start_screen()
        menu = int(input("> "))
        if menu == 0:
            print("Closing...")
        elif menu == 1:
            show_table()
        elif menu == 2:
            plot_menu.show()
        else:
            print("Error: invalid number provided. Please try again: ")


# Main function
if __name__ == '__main__':
    menu_loop()
