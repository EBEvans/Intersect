import time
import math
import random

# the maximum value of a list element
# to choose a good MAX:
# assume that LENGTH = xey and use MAX = ((2x)^2)e(2y)
MAX = int(36e8)

# the length of the list
LENGTH = int(3e4)

# number of guaranteed common elements in each list
# but the simulation assumes the number of common elements to be found in unknown
NUM_COMMON = 5


# randomly populates the lists list1 and list2
def set_generate():
    (list1, list2) = ([], [])

    # randomly generate two different lists
    # NOTICE: may randomly (unlikely) generate common elements
    # To help avoid this, suggest choosing MAX and LENGTH such that:
    # sqrt(MAX) = 2*LENGTH as rough solution to the Birthday Problem/Birthday Paradox
    for i in range(0, LENGTH):
        list1.append(random.randint(0, MAX))
        list2.append(random.randint(0, MAX))

    # replace NUM_COMMON number of values with the same random number
    # at different random indices in both lists
    for i in range(1, NUM_COMMON + 1):
        temp = random.randint(0, MAX)
        list1[random.randint(0, LENGTH)] = temp
        list2[random.randint(0, LENGTH)] = temp

    return list1, list2


# linear search across unsorted lists
# expected O(n^2) time complexity
# assumes number of potential common elements is unknown
# but if one element exists once in one list and twice in another, will only find the first element in the other list
def brute_force(list1, list2):
    found = []
    for i in range(0, LENGTH):
        for j in range(0, LENGTH):
            if list1[i] == list2[j]:
                found.append(list1[i])
                break
    return found


# The actual binary search method which gets called
# O(log n) time complexity (or O(n log n) to search for every element of list1 in list2).
def binary_search(search_list, seek):
    left_bound = 0
    right_bound = len(search_list) - 1
    while left_bound <= right_bound:
        middle = math.floor((left_bound + right_bound)/2)
        if seek == search_list[middle]:
            return seek
        elif search_list[middle] < seek:
            left_bound = middle + 1
        elif search_list[middle] > seek:
            right_bound = middle - 1
        else:
            raise RuntimeError("?!?!?!?")
    return -1


# searches for each/every element of set1 in set2
# only records found similar elements
def search_similar(list1, list2):
    results = []
    for i in range(0, LENGTH):
        seeking = list1[i]
        found = binary_search(list2, seeking)
        if found != -1:
            results.append(found)
    return results


def main():
    random.seed(time.time())

    temp = set_generate()
    list1 = temp[0]
    list2 = temp[1]

    start_brute = time.time()
    brute_results = brute_force(list1, list2)
    end_brute = time.time()
    brute_time = end_brute - start_brute
    print("time to brute-force search:", brute_time)
    print("found similar elements using brute-force search:", brute_results)

    start_sorted = time.time()
    # Note that Python's default .sort() algorithm, Timsort, is O(n log n)
    list2.sort()
    sorted_results = search_similar(list1, list2)
    end_sorted = time.time()
    sorted_time = end_sorted - start_sorted
    print("time to sort and search:", sorted_time)
    print("found similar elements using sort-and-search:", sorted_results)
    return


main()
