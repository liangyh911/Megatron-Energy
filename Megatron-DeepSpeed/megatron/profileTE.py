import time
from zeus.monitor import ZeusMonitor

import torch
from torch import distributed

init_time = 0
start_time = 0
end_time = 0
monitor = ZeusMonitor()

def start_timer():
    global start_time
    start_time = time.time()

def get_elapsed_time():
    global start_time
    if start_time == 0:
        return 0
    return time.time() - start_time

def monitor_init():
    global monitor, init_time
    monitor = ZeusMonitor(gpu_indices=[0,1,2,3], approx_instant_energy = True)
    init_time = time.time()

    # device_rank = torch.distributed.get_rank()
    # f = open("./output/init_time.txt", "w")
    # f.write(str(init_time))
    # f.close()

def monitor_begin(key):
    global monitor
    monitor.begin_window(key)
    # start_time = time.time()


def monitor_end(key, dir, label):
    global monitor
    measurement = monitor.end_window(key)

    device_rank = torch.distributed.get_rank()
    f = open("./output/" + dir + "/" + str(device_rank)+".txt", 'a')
    f.write(key + " " + label + ": " + str(measurement.total_energy) + "\n")
    f.close()
    
    return 0