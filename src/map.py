import memory_profiler
from line_profiler import LineProfiler

nums = range(10000)

prof = LineProfiler()

"""
ループ処理
mapの方が
・メモリ消費が少し少ない
・処理速度が圧倒的に速い
"""


@memory_profiler.profile
def f_map(ns):
    """
        Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
         9     21.3 MiB     21.3 MiB           1   @memory_profiler.profile
        10                                         def f_map(ns):
        11     21.8 MiB      0.5 MiB       20001       print(list(map(lambda n: n * 2, ns)))
    """
    print(list(map(lambda n: n * 2, ns)))


# prof.add_function(f_map)
# prof.runcall(f_map, nums)
f_map(nums)


@memory_profiler.profile
def f_loop(ns):
    """
        Line #    Mem usage    Increment  Occurrences   Line Contents
    =============================================================
        19     21.8 MiB     21.8 MiB           1   @memory_profiler.profile
        20                                         def f_loop(ns):
        21     22.1 MiB      0.2 MiB       10001       print([n * 2 for n in ns])
    """
    print([n * 2 for n in ns])


# prof.add_function(f_loop)
# prof.runcall(f_loop, nums)
# prof.print_stats(output_unit=1e-6)
f_loop(nums)

"""
Total time: 0.002744 s
File: /Users/yagrush/work/python-generator/src/map.py
Function: f_map at line 10

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    10                                           def f_map(ns):
    11         1       2744.0   2744.0    100.0      print(list(map(lambda n: n * 2, ns)))

Total time: 0.023921 s
File: /Users/yagrush/work/python-generator/src/map.py
Function: f_loop at line 19

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    19                                           def f_loop(ns):
    20     10001      23921.0      2.4    100.0      print([n * 2 for n in ns])
"""
