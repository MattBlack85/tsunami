import multiprocessing

from .client import Tsunami


def main(url, num_request):
    proc_number = multiprocessing.cpu_count()
    procs = [Tsunami(url, num_request) for _ in range(proc_number)]
    for p in procs:
        p.start()

    for p in procs:
        p.join()
