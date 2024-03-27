import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [5, 6, 7, 8, 9],
    'C': [9, 10, 11, 12, 13]
}
df = pd.DataFrame(data)

# Function to create different plots
def create_plot(plot_type):
    if plot_type == 'Scatter Plot':
        plt.figure(figsize=(5, 4))
        sns.scatterplot(data=df, x='A', y='B')
        plt.title('Scatter Plot')
        plt.xlabel('A')
        plt.ylabel('B')
        canvas.draw()
    elif plot_type == 'Histogram':
        plt.figure(figsize=(5, 4))
        sns.histplot(data=df, x='C')
        plt.title('Histogram')
        plt.xlabel('C')
        plt.ylabel('Frequency')
        canvas.draw()

# Create main Tkinter window
root = tk.Tk()
root.title("Plot Selector")

# Dropdown menu for selecting plot type
plot_types = ['Scatter Plot', 'Histogram']
selected_plot = tk.StringVar(value=plot_types[0])
plot_dropdown = ttk.Combobox(root, textvariable=selected_plot, values=plot_types, state='readonly')
plot_dropdown.pack()

# Matplotlib canvas
fig, ax = plt.subplots(figsize=(6, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Initial plot
create_plot(selected_plot.get())

# Function to handle plot selection change
def on_plot_change(event):
    create_plot(plot_dropdown.get())

plot_dropdown.bind("<<ComboboxSelected>>", on_plot_change)

# Run Tkinter event loop
root.mainloop()
