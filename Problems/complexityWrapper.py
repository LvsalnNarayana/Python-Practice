import time
import psutil
import os

def complexity_wrapper(func):
    def wrapper(*args, **kwargs):
        # Measure initial memory usage
        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss
        
        # Measure start time
        start_time = time.time()
        
        # Execute the function
        result = func(*args, **kwargs)
        
        # Measure end time
        end_time = time.time()
        
        # Measure final memory usage
        final_memory = process.memory_info().rss
        
        # Calculate time and space complexity
        time_taken = end_time - start_time
        memory_used = final_memory - initial_memory
        
        print(f"Time Complexity: {time_taken:.6f} seconds")
        print(f"Space Complexity: {memory_used / 1024:.2f} KB")
        
        return result
    return wrapper
