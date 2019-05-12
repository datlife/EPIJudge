import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot, A):
    # TODO - you fill in here.
	if not A:
		return

	# Runtime: O(N)
	# Space: O(N)
	# L, P, R = [], [], []
	# for i in range(len(A)):
	#	if A[i] < A[pivot]: L.append(A[i])
	#	elif A[i] > A[pivot]: R.append(A[i])
	#	else: P.append(A[i])	
	# A[:] = L + P + R
	pivot = A[pivot]
	smaller, unclassified, larger = 0, 0, len(A)
	while unclassified < larger:
		if A[unclassified] < pivot:
			A[smaller], A[unclassified] = A[unclassified], A[smaller]
			smaller += 1
			unclassified += 1
		elif A[unclassified] == pivot:
			unclassified += 1
		else: # A[unclassified] > pivot:
			larger -= 1
			A[larger], A[unclassified] = A[unclassified], A[larger]


@enable_executor_hook
def dutch_flag_partition_wrapper(executor, A, pivot_idx):
    count = [0, 0, 0]
    for x in A:
        count[x] += 1
    pivot = A[pivot_idx]

    executor.run(functools.partial(dutch_flag_partition, pivot_idx, A))

    i = 0
    while i < len(A) and A[i] < pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] == pivot:
        count[A[i]] -= 1
        i += 1
    while i < len(A) and A[i] > pivot:
        count[A[i]] -= 1
        i += 1

    if i != len(A):
        raise TestFailure('Not partitioned after {}th element'.format(i))
    elif any(count):
        raise TestFailure("Some elements are missing from original array")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("dutch_national_flag.py",
                                       'dutch_national_flag.tsv',
                                       dutch_flag_partition_wrapper))
