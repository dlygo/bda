import time, concurrent.futures, multiprocessing
arange=20000

def sum_square(number):
    sum = 0
    for i in range(number):
        sum += i*i
    return sum
    
def serial_runner(arange):
    start = time.perf_counter()
    for i in range(arange): 
        sum_square(i)
    end = time.perf_counter()
    print(f'Serial: {round(end-start,2)} second(s)')

def parallel_runner(arange):
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(sum_square, range(arange))
    end = time.perf_counter()
    print(f'Parallel process poolmap: {round(end-start,2)} second(s)')

def parallel_runner_limit_workers(arange):
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(sum_square, range(arange))
    end = time.perf_counter()
    print(f'Parallel process poolmap 4 workers: {round(end-start,2)} second(s)')

def parallel_map(arange):
    start = time.perf_counter()
    with multiprocessing.Pool() as p:
        p.map(sum_square, range(arange))
    end = time.perf_counter()
    print(f'Parallel multiprocessing: {round(end-start,2)} second(s)')


if __name__ == "__main__":
        arange = 20000
        serial_runner(arange)
        parallel_runner(arange)
        parallel_runner_limit_workers(arange)
        parallel_map(arange)
