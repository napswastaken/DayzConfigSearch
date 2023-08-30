import os
import re

#point to the folder you want to scan configs for. path should have double backslash for paths
root_directory = r"Path\\to\\Folder"

#output where you want the text file to go
output_file_path = os.path.join(os.path.expanduser("~"), "Downloads/export/classnames.txt")

# REGEX for class, classname must have scope 2, or it skips it
class_pattern = r"class\s+(\w+)\s*:\s*\w+\s*\{[^}]*scope\s*=\s*2;\s*"

def extract_classnames(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        classnames = re.findall(class_pattern, content)
        return classnames

def process_config_file(file_path):
    classnames = extract_classnames(file_path)
    return classnames

def write_classnames_to_file(classnames):
    with open(output_file_path, "w") as output_file:
        for classname in classnames:
            output_file.write(classname + "\n")

def main():
    if not os.path.exists(root_directory):
        print("Directory does not exist.")
        return

    classnames = []

    for root, _, files in os.walk(root_directory):
        for file in files:
            if file.lower() == "config.cpp":
                file_path = os.path.join(root, file)
                extracted_classnames = process_config_file(file_path)
                classnames.extend(extracted_classnames)
            elif file.lower() == "config.bin":
                print("Found a config.bin file:", os.path.join(root, file))
                
    if classnames:
        write_classnames_to_file(classnames)
        print("Classnames written to", output_file_path)
    else:
        print("No classnames found.")

if __name__ == "__main__":
    main()
