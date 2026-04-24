
import random
import time
import sys

sys.setrecursionlimit(50000)

SEED = 42
random.seed(SEED)


def insertion_sort(arr):
    """
    Insertion Sort – O(n^2) average/worst, O(n) best (already sorted).
    Stable: Yes | In-place: Yes
    """
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr):
    """
    Merge Sort – O(n log n) all cases.
    Stable: Yes | In-place: No (uses O(n) extra space)
    """
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:    
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr, low=None, high=None):
    """
    Quick Sort – O(n log n) average, O(n^2) worst (sorted input + last pivot).
    Stable: No | In-place: Yes (sorts in-place, returns sorted list)
    Pivot strategy: last element (Lomuto partition scheme)
    """
    a = arr[:] if low is None else arr  
    if low is None:
        low, high = 0, len(a) - 1
    if low < high:
        pi = _partition(a, low, high)
        quick_sort(a, low, pi - 1)
        quick_sort(a, pi + 1, high)
    return a


def _partition(arr, low, high):
    pivot = arr[high]        
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1




def measure_time(sort_func, arr):
    """
    Times sort_func on a COPY of arr.
    Returns (sorted_result, time_in_ms).
    """
    data = arr[:]                         
    start = time.perf_counter()
    result = sort_func(data)
    end   = time.perf_counter()
    ms = (end - start) * 1000
    return result, ms



def generate_datasets(sizes=(1000, 5000, 10000)):
    datasets = {}
    for n in sizes:
        random.seed(SEED)
        rand_list    = [random.randint(1, 100000) for _ in range(n)]
        sorted_list  = list(range(1, n + 1))
        reverse_list = list(range(n, 0, -1))
        datasets[n] = {
            "random":  rand_list,
            "sorted":  sorted_list,
            "reverse": reverse_list,
        }
    return datasets




ALGORITHMS = [
    ("Insertion Sort", insertion_sort),
    ("Merge Sort",     merge_sort),
    ("Quick Sort",     quick_sort),
]

INPUT_TYPES = ["random", "sorted", "reverse"]
SIZES       = [1000, 5000, 10000]


def separator(title):
    print("\n" + "=" * 65)
    print(f"  {title}")
    print("=" * 65)




def run_correctness_check():
    separator("CORRECTNESS CHECK")
    test = [5, 2, 9, 1, 5, 6]
    expected = [1, 2, 5, 5, 6, 9]
    print(f"\n  Input:    {test}")
    print(f"  Expected: {expected}\n")
    all_pass = True
    for name, func in ALGORITHMS:
        result = func(test[:])
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_pass = False
        print(f"  {name:<20} → {result}  [{status}]")
    print(f"\n  Overall: {'ALL PASS ✓' if all_pass else 'SOME FAILED ✗'}")




def run_experiments(datasets):
    separator("PERFORMANCE MEASUREMENT (times in milliseconds)")

    # results[size][input_type][algo_name] = ms
    results = {n: {t: {} for t in INPUT_TYPES} for n in SIZES}

    for itype in INPUT_TYPES:
        print(f"\n  ── Input type: {itype.upper()} ──")
        print(f"  {'Algorithm':<22} {'n=1000':>10} {'n=5000':>10} {'n=10000':>12}")
        print(f"  {'-'*56}")
        for name, func in ALGORITHMS:
            row = f"  {name:<22}"
            for n in SIZES:
                arr = datasets[n][itype]
                _, ms = measure_time(func, arr)
                results[n][itype][name] = ms
                row += f"  {ms:>8.2f} ms"
            print(row)

    return results




def print_full_table(results):
    separator("FULL RESULTS TABLE (27 experiments)")
    header = f"\n  {'Size':>7}  {'Input Type':>12}  {'Insertion Sort':>16}  {'Merge Sort':>12}  {'Quick Sort':>12}"
    print(header)
    print("  " + "-" * 68)
    for n in SIZES:
        for itype in INPUT_TYPES:
            r = results[n][itype]
            ins = r["Insertion Sort"]
            mrg = r["Merge Sort"]
            qck = r["Quick Sort"]
            print(f"  {n:>7}  {itype:>12}  {ins:>14.2f} ms  {mrg:>10.2f} ms  {qck:>10.2f} ms")
    print()



if __name__ == "__main__":
    print("╔═══════════════════════════════════════════════════════════════╗")
    print("║   Sorting Performance Analyzer (SPA)                         ║")
    print("║   ETCCDS202 | Unit 3 Assignment                              ║")
    print("║   Roll No: 2501730189                                         ║")
    print("╚═══════════════════════════════════════════════════════════════╝")

    run_correctness_check()

    datasets = generate_datasets()
    results  = run_experiments(datasets)
    print_full_table(results)

    separator("ALGORITHM PROPERTIES SUMMARY")
    props = [
        ("Insertion Sort", "O(n^2)",      "O(n)",       "Stable",   "In-place"),
        ("Merge Sort",     "O(n log n)",  "O(n log n)", "Stable",   "Out-of-place"),
        ("Quick Sort",     "O(n log n)*", "O(n^2)**",   "Unstable", "In-place"),
    ]
    print(f"\n  {'Algorithm':<18} {'Average':>12} {'Worst':>12} {'Stable':>10} {'Memory':>14}")
    print("  " + "-" * 70)
    for row in props:
        print(f"  {row[0]:<18} {row[1]:>12} {row[2]:>12} {row[3]:>10} {row[4]:>14}")
    print("\n  * Quick Sort average O(n log n) on random data")
    print("  ** Quick Sort degrades to O(n^2) on sorted/reverse-sorted with last-element pivot")

    print("\n" + "=" * 65)
    print("  All experiments completed.")
    print("=" * 65)
