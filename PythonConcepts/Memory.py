import sys
import tracemalloc

tracemalloc.start()

# Code that may have memory issues
x = [i for i in range(10000)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("\n")
for stat in top_stats:
    print(stat)
