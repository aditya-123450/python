def read_file(filename): 
    file = None 
    try: 
        print("Opening file...") 
        file = open(filename, 'r') 
        content = file.read() 
        print(f"File content: {content}") 
        return content 
    except FileNotFoundError: 
        print(f"Error: File '{filename}' not found") 
        return None 
    except PermissionError: 
        print("Error: Permission denied") 
        return None 
    finally: 
        # This always executes 
        if file: file.close()
        print("File closed successfully") 
        print("Cleanup completed")