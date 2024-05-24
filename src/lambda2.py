import memory_profiler
from line_profiler import LineProfiler

"""
無名関数の方がすっきりするが無駄が多いか.
"""

nums = range(10000)

prof = LineProfiler()


def fp(v):
    print(v)


# @memory_profiler.profile
def f(ns):
    """
        Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        13     21.4 MiB     21.4 MiB           1   @memory_profiler.profile
        14                                         def f(ns):
        15     21.4 MiB      0.0 MiB       10001       for v in ns:
        16     21.4 MiB      0.0 MiB       10000           fp(v)
    """
    for v in ns:
        fp(v)


# @memory_profiler.profile
def lmd(ns):
    """
        Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        19     21.3 MiB     21.3 MiB           1   @memory_profiler.profile
        20                                         def lmd(ns):
        21     21.5 MiB      0.0 MiB       10001       for v in ns:
        22     21.5 MiB      0.1 MiB       30000           (lambda x: print(x))(v)
    """
    for v in ns:
        (lambda x: print(x))(v)


# f(nums)

# lmd(nums)


# prof.add_function(f)
# prof.runcall(f, nums)
# prof.print_stats(output_unit=1e-6)

"""
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    14                                           def f(ns):
    23     10001       1031.0      0.1      8.1      for v in ns:
    24     10000      11755.0      1.2     91.9          fp(v)
"""


prof.add_function(lmd)
prof.runcall(lmd, nums)
prof.print_stats(output_unit=1e-6)

"""
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    28                                           def lmd(ns):
    37     10001       1050.0      0.1      7.3      for v in ns:
    38     10000      13313.0      1.3     92.7          (lambda x: print(x))(v)
"""
