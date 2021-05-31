# Intersect
Compares efficient and inefficient methods of finding the common elements of two lists, like a set intersection.

Decided to make this on a whim when, in a TV show, the characters need to search through two peoples' private libraries for books contained in both libraries. Of course, this is in more generalized form.
I'm used to splitting my attention between TV and phone/computer, so I figured why not; it's cool knowing how to solve problems.

The brute-force comparison of each element in list1 to each element of list2 should average 1/2 n^2 performance; the sorting of one list and binary-search for each element of the unsorted list to the sorted list should have 2(n log n) performance (n log n performance for each step).
