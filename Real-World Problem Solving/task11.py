def process_log_file(filename,keyword="ERROR"):
    """
    Processes a log file and counts how many times a specified keyword appears.
    
    Parameters:
    - filename (str): The name of the log file to read.
    - keyword (str): The keyword to search for in each line (default is "ERROR").
    """
    try :
        count = 0 #Initialize a counter
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines: #iterate over each line and count keyword occurrences
                if keyword in line:
                    count += 1
        print(f"Total occurrences of '{keyword}': {count}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

process_log_file("sample_log.txt","ERROR")
process_log_file("sample_log.txt","WARNING")