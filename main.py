import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Import ttk for Progressbar
from PIL import Image

def split_tif(input_files, progress_bar):
    total_pages = sum(Image.open(file).n_frames for file in input_files)
    progress_bar['maximum'] = total_pages  # Set the maximum value of the progress bar

    for input_file in input_files:
        with Image.open(input_file) as img:
            for i in range(img.n_frames):
                img.seek(i)
                img.save(f'{input_file}_page_{i + 1}.tif')
                progress_bar['value'] += 1  # Update progress bar
                root.update_idletasks()  # Update the UI

def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("TIFF files", "*.tif;*.tiff")])
    if file_paths:
        try:
            split_tif(file_paths, progress_bar)  # Pass progress bar to the function
            messagebox.showinfo("Success", "TIF files split successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("TIF Splitter")

# Create a button to select the TIF files
btn_select = tk.Button(root, text="Select TIF Files", command=select_files)
btn_select.pack(pady=20)

# Create a progress bar
progress_bar = ttk.Progressbar(root, length=300)
progress_bar.pack(pady=20)

# Run the application
root.mainloop()
