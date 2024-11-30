import time

def format_time(seconds):
    """Format time in hours:minutes:seconds.hundredths."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    seconds = seconds % 60
    hundredths = int((seconds - int(seconds)) * 100)
    
    return f"{hours:02}:{minutes:02}:{int(seconds):02}.{hundredths:02}"

def stopwatch():
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    
    input("Press Enter to stop the stopwatch...")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    formatted_time = format_time(elapsed_time)
    
    print(f"Elapsed time: {formatted_time}")

if __name__ == "__main__":
    stopwatch()
