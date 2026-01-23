

def reading_file(file_path):
    """Reads the content of a file and returns it as a string."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "The specified file was not found."
    except IOError:
        return "An error occurred while reading the file."
    
if __name__ == "__main__":
    file_path = 'myfile.txt' 
    file_content = reading_file(file_path)
    print(file_content)