import os

def getPdfFiles(path):
    pdf_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.pdf'):
                pdf_files.append(os.path.join(root, file))
    return pdf_files

def deleteContents(folder_path):
    try:
        # Iterate over all the files and subfolders in the specified folder
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            # Check if it's a file and delete it
            if os.path.isfile(file_path):
                os.remove(file_path)

            # Check if it's a subfolder and delete it recursively
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

        print(f"All files and folders in {folder_path} have been deleted.")

    except Exception as e:
        print(f"An error occurred: {e}")