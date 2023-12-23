import tkinter as tk
from tkinter import scrolledtext
from tkinter import filedialog
from PyPDF2 import PdfMerger 
import os

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")



def choose_files():
    file_paths = filedialog.askopenfilenames(
        filetypes=[("PDF files", "*.pdf")]  # Specify that only PDF files are allowed
    ) # Open a file dialog for multiple file selection
    for idx, path in enumerate(file_paths, start=1):
        tab_content.insert(tk.END, f"{idx}. {path}\n")  # Insert each file path with an index into the Text widget

def merge_files():
    # Get the selected PDF file paths from the Text widget
    file_paths_with_index = tab_content.get("1.0", tk.END).strip().split("\n")
    
    if len(file_paths_with_index) < 2:
        # Ensure at least two PDF files are selected for merging
        return
    
    # Extract the file paths by removing the index numbers
    file_paths = [path.split(' ', 1)[1] for path in file_paths_with_index]
    
    # Ask the user to select a destination file for the merged PDF
    destination_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    if destination_file:
        try:
            # Check if the file already exists and confirm overwrite
            if os.path.exists(destination_file):
                confirm = tk.messagebox.askyesno("File Exists", "The file already exists. Do you want to overwrite it?")
                if not confirm:
                    return

            pdf_merger = PdfMerger()

            # Append each selected PDF to the merger
            for path in file_paths:
                pdf_merger.append(path.strip())  # Remove leading/trailing spaces

            # Write the merged PDF to the destination file
            with open(destination_file, "wb") as output_pdf:
                pdf_merger.write(output_pdf)

            # Clear the Text widget after merging
            tab_content.delete(1.0, tk.END)
        except Exception as e:
            # Handle any errors that may occur during merging
            tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")

def clear_files():
    tab_content.delete(1.0, tk.END)  # Clear the Text widget

def close_window():
    root.destroy()

# Create the main application window
root = tk.Tk()

# Set the title of the window
root.title("PDF-Fusion(By-Akash Kumar)")

# Set the window dimensions
window_width = 600
window_height = 500

# Center the window on the screen
center_window(root, window_width, window_height)

# for changing default icon
iconPath = "D:\Python\PDF-Merged-App\pdf-svgrepo-com.ico"
root.iconbitmap(iconPath)

# for Bold fonts


header_label = tk.Label(root, text="PDF - FUSION", font=("Helvetica", 14), bg="white", fg="#274472")
header_label.pack()

# Create a button instead of the input field
choose_button = tk.Button(root, text="SELECT PDF FILES", font=("Arial", 16),width=30, height=1,fg="white", bg="#12123E",command=choose_files)
choose_button.pack(pady=10)

#Here The All File selected Path will be show

tab_content = scrolledtext.ScrolledText(root, width=70, height=10)
tab_content.pack(pady=10)


button_frame = tk.Frame(root)
button_frame.pack()



merge_button = tk.Button(button_frame, text="MERGE", font=("Arial", 11,"bold"), width=8, height=1,bg='#6AB187',fg="black", command=merge_files)
merge_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="CLEAR", font=("Arial", 11,"bold"), width=8, height=1,bg='#EA6A47',fg="black", command=clear_files)
clear_button.pack(side=tk.LEFT, padx=10)

close_button = tk.Button(button_frame, text="CLOSE", font=("Arial", 11,"bold"), width=8, height=1,bg='red',fg="black", command=close_window)
close_button.pack(side=tk.LEFT, padx=10)





# Run the Tkinter event loop
root.mainloop()
