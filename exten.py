import os

def change_file_extension(folder_path, old_extension, new_extension):
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return
    
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    
    # Iterate through each file in the folder
    for file_name in files:
        # Check if the file has the old extension
        if file_name.endswith(old_extension):
            # Construct the old and new file paths
            old_file_path = os.path.join(folder_path, file_name)
            new_file_path = os.path.join(folder_path, os.path.splitext(file_name)[0] + new_extension)
            
            try:
                # Rename the file with the new extension
                os.rename(old_file_path, new_file_path)
                print(f"File '{file_name}' renamed to '{os.path.basename(new_file_path)}'")
            except Exception as e:
                print(f"Error renaming file '{file_name}': {str(e)}")

# User input for folder path, old extension, and new extension
folder_path = input("Enter the folder path: ")
old_extension = input("Enter the old extension (including '.'): ")
new_extension = input("Enter the new extension (including '.'): ")

# Call the function with user input
change_file_extension(folder_path, old_extension, new_extension)
