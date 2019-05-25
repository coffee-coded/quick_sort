count =0
def partition(first, last):
    global unsorted_array
    pivot = unsorted_array[first]
    i=first+1
    j=first+1
    while j<=last:
        if unsorted_array[j]<pivot:
            unsorted_array[i],unsorted_array[j]=unsorted_array[j],unsorted_array[i]
            i=i+1
        j=j+1
    unsorted_array[first],unsorted_array[i-1]=unsorted_array[i-1],unsorted_array[first]
    return i-1


def quick_sort(first,last):
    global count
    count=count+(last-first)
    global unsorted_array
    mid = 0
    if first<last:
        mid = partition(first,last)
        quick_sort(first,mid-1)
        quick_sort(mid+1,last)
    return

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
    global unsorted_array

    input_array()

    if len(unsorted_array) == 0:
        print("\n\nNothing to sort")
        print("Goodbye human")
    else:
        print("Unsorted List : ", end="")
        print(unsorted_array)
        print(" Sorted  List : ", end="")
        quick_sort(0, len(unsorted_array) - 1)
        print(unsorted_array)
        print("Count : ",count)
        print("\n\n  Goodbye Human")
