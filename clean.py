import os

# Function to delete all files starting with "image" in current directory
def delete_files_starting_with_image():
    current_directory = os.getcwd()

    for filename in os.listdir(current_directory):
        if filename.startswith("image") or filename.startswith("video"):
            file_path = os.path.join(current_directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
                
    print("Finished deleting images and videos")

# Call the function
delete_files_starting_with_image()
