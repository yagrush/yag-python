import sys
import memory_profiler
from line_profiler import LineProfiler


def get_set_generator():
    arrays_generator = ([tuple((x, y)) for y in range(100)] for x in range(100))
    for v in arrays_generator:
        yield v


def get_set():
    return [[tuple((x, y)) for y in range(100)] for x in range(100)]


# @memory_profiler.profile
def main(args):
    print(args)
    # for v in get_set():
    for v in get_set_generator():
        print(v)


if __name__ == "__main__":
    # main(sys.argv[1:])
    prof = LineProfiler()
    prof.add_function(main)
    prof.runcall(main, sys.argv[1:])
    prof.print_stats(output_unit=1e-6)  # μs
