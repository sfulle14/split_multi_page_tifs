import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Import ttk for Progressbar
from PIL import Image
import os  # Import os for path operations

def split_tif(input_files, output_folder, progress_bar):
    total_pages = sum(Image.open(file).n_frames for file in input_files)
    progress_bar['maximum'] = total_pages  # Set the maximum value of the progress bar

    for input_file in input_files:
        with Image.open(input_file) as img:
            base_name = os.path.splitext(os.path.basename(input_file))[0]  # Get the base name without extension
            for i in range(img.n_frames):
                img.seek(i)
                output_path = os.path.join(output_folder, f'{base_name}_page_{i + 1}.tif')  # Use base name
                img.save(output_path)  # Save to the specified output folder
                progress_bar['value'] += 1  # Update progress bar
                root.update_idletasks()  # Update the UI

def select_files():
    file_paths = filedialog.askopenfilenames(filetypes=[("TIFF files", "*.tif;*.tiff")])
    if file_paths:
        output_folder = filedialog.askdirectory(title="Select Output Folder")  # Select output folder
        if output_folder:  # Check if an output folder was selected
            try:
                split_tif(file_paths, output_folder, progress_bar)  # Pass output folder to the function
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
