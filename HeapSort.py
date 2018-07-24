## maximum heap

# heapify is used based on all its children are in heapified format.
# therefore, do "heapify" need to follow the bottom-up order.
# time complex for heapify is O(log(n))
def heapify(lArr, iLen, iIndex):
    """
    @param: lArr, original array list
    @param: iLen, array list len
    @param: iIndex, starting index need to be checked for heapify
    """
    # check two children:
    # left child index
    iLeftIndex = iIndex * 2 + 1
    # right child index
    iRightIndex = iIndex * 2 + 2

    # compare with two children/check if "iIndex" is the largest.
    iLargest = iIndex
    if iLeftIndex < iLen and lArr[iLargest] < lArr[iLeftIndex]:
        iLargest = iLeftIndex
    if iRightIndex < iLen and lArr[iLargest] < lArr[iRightIndex]:
        iLargest = iRightIndex

    # if adjust is needed, do the swap!
    if iLargest != iIndex:
        lArr[iIndex],lArr[iLargest] = lArr[iLargest], lArr[iIndex]
        # not only for current level, recurrsively check child of previous largest num;
        heapify(lArr, iLen, iLargest)

# overall time complex is O((2n-1)log(n))  ~~ O(nlog(n))
def heapSort(lArr):
    """
    @param: lArr
    """
    iLen = len(lArr)
    # side note: range(start, end, step)
    # heapify the whole array, from bottom to top [time complex O(nlog(n))]
    for i in range(iLen, -1, -1):
        heapify(lArr, iLen, i)

    # one by one pop out the root (largest)
    # iEnd: dynamically shrink the length/size of the heap [time complex O( (n-1)log(n) )]
    for i in range(iLen, 0, -1):
        # store largest to the end of array
        lArr[0], lArr[i-1] = lArr[i-1], lArr[0]
        # heapify the root
        heapify(lArr, i-1, 0)


## test
ArrTest1 = [10, 5, 15, 8, 10, 100, 150, 1000]
ArrTest2 = []
ArrTest3 = [0,0,0,0,0,0,0,0,0,0,0,0]
ArrTest4 = [5,60,3,6,1000,43,20]

heapSort(ArrTest1)
heapSort(ArrTest2)
heapSort(ArrTest3)
heapSort(ArrTest4)

print (ArrTest1)
print (ArrTest2)
print (ArrTest3)
print (ArrTest4)