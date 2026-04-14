import psutil

cpu_threshold = 10       
mem_threshold = 70        
root_disk_threshold = 80 
home_disk_threshold = 90 
check_interval = 5

def check_cpu():
    cpu_usage = psutil.cpu_percent(interval=5)
    if cpu_usage > cpu_threshold:
        print(f"[Alert] CPU usage : {cpu_usage}% (Threshold: {cpu_threshold}%)" )


            


