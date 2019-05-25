
def quick_sort(array_unsorted):
    if len(array_unsorted) == 1 or len(array_unsorted) == 0:
        return array_unsorted
    pivot: object = array_unsorted[0]
    left = array_unsorted[1]
    l_k = 1
    right = array_unsorted[-1]
    r_k = len(array_unsorted) - 1
    while l_k != r_k:
        if not right < pivot:
            r_k = r_k - 1
            right = array_unsorted[r_k]
        if not left > pivot and l_k != r_k:
            l_k = l_k + 1
            left = array_unsorted[l_k]

        if l_k != r_k and left > pivot > right:
            array_unsorted[l_k], array_unsorted[r_k] = array_unsorted[r_k], array_unsorted[l_k]
            right = array_unsorted[r_k]
            left = array_unsorted[l_k]
    if l_k == r_k:
        piv_e = 0
        if array_unsorted[l_k] < array_unsorted[0]:
            piv_e = l_k
            array_unsorted[l_k], array_unsorted[0] = array_unsorted[0], array_unsorted[l_k]
        elif array_unsorted[l_k - 1] < array_unsorted[0]:
            piv_e = l_k - 1
            array_unsorted[l_k - 1], array_unsorted[0] = array_unsorted[0], array_unsorted[l_k - 1]
        array_unsorted[piv_e + 1:] = quick_sort(array_unsorted[piv_e + 1:])
        array_unsorted[:piv_e] = quick_sort(array_unsorted[:piv_e])
        return array_unsorted


def input_array():
    global unsorted_array
    print("Press q to quit inserting values\n")
    unsorted_array = []
    i = 0
    while True:
        x = input("Input : ")
        if x == "q" or x == "Q":
            break
        else:
            try:
                unsorted_array.insert(i, int(x))
                print("Your input of ", x, "has been added")
                i += 1
            except:
                print("Couldn't be added")


if __name__ == "__main__":

    input_array()

    if len(unsorted_array) == 0:
        print("\n\nNothing to sort")
        print("Goodbye human")
    else:
        print("Unsorted List : ", end="")
        print(unsorted_array)
        print(" Sorted  List : ", end="")
        print(quick_sort(unsorted_array))
        print("\n\n  Goodbye Human")
