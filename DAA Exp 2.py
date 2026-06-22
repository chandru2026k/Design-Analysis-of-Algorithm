import time
import matplotlib.pyplot as plt


# Interpolation Search Function
def interpolation_search(arr, key):
    low = 0
    high = len(arr) - 1
    comparisons = 0

    while (
        low <= high
        and key >= arr[low]
        and key <= arr[high]
    ):

        comparisons += 1

        if low == high:
            if arr[low] == key:
                return low, comparisons
            return -1, comparisons

        pos = low + int(
            ((high - low) * (key - arr[low]))
            / (arr[high] - arr[low])
        )

        if arr[pos] == key:
            return pos, comparisons

        elif arr[pos] < key:
            low = pos + 1

        else:
            high = pos - 1

    return -1, comparisons


# Input
n = int(input("Enter number of elements: "))


# Uniformly distributed sorted array
arr = list(range(1, n + 1))

print("\nArray generated successfully.")

key = int(input("Enter search key: "))


# Execution Time Measurement
start = time.perf_counter()

position, comparisons = interpolation_search(arr, key)

end = time.perf_counter()

execution_time = end - start


# Output
print("\n----- RESULT -----")

if position != -1:
    print(f"Element found at position: {position}")
else:
    print("Element not found")

print(f"Comparisons Performed: {comparisons}")
print(f"Execution Time: {execution_time:.10f} seconds")

print("\nComplexity Analysis")
print("Average Time Complexity : O(log log n)")
print("Worst Case Complexity   : O(n)")
print("Space Complexity        : O(1)")


# Graph for Different Input Sizes
sizes = [1000, 5000, 10000, 50000, 100000]
times = []

for size in sizes:

    test_arr = list(range(1, size + 1))
    test_key = size // 2

    start = time.perf_counter()

    interpolation_search(test_arr, test_key)

    end = time.perf_counter()

    times.append(end - start)


# Plot
plt.figure(figsize=(8, 5))

plt.plot(
    sizes,
    times,
    marker='o'
)

plt.title(
    "Interpolation Search Execution Time"
)

plt.xlabel("Input Size")

plt.ylabel("Execution Time (seconds)")

plt.grid(True)

plt.show()