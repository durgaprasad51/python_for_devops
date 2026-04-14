import psutil

def get_cpu_threshold():
    user_cpu = int(input("Enter the CPU utilization"))

    current_cpu = psutil.cpu_percent(interval=1)
    print("current_cpu %: ", current_cpu)

    if current_cpu > user_cpu:
        print("CPU Alert email sent....")
    else:
        print("CPU is in safe state")

get_cpu_threshold()