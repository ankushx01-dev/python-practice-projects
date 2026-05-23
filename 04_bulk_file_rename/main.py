import os

# Take folder path from the user
folder_path = input("Enter folder path: ")

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"Error: The directory '{folder_path}' does not exist.")
    exit()

# Get all files from the folder
files = os.listdir(folder_path)

# Loop through each file
for index, file_name in enumerate(files):

    # Create full old file path
    old_file = os.path.join(folder_path, file_name)

    # Skip folders
    if os.path.isdir(old_file):
        continue

    # Get file extension
    file_extension = os.path.splitext(file_name)[1]

    # Create new file name
    new_file_name = f"file_{index + 1}{file_extension}"

    # Create full new file path
    new_file = os.path.join(folder_path, new_file_name)

    # Rename file
    os.rename(old_file, new_file)

    # Print renamed file
    print(f"{file_name} renamed to {new_file_name}")

# Final message
print("\nThank you for using the Bulk File Renamer")