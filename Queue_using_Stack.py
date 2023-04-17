def enqueue(ar, elem):
    ar.append(elem)


def peak(ar):
    print(ar[0])


def dequeue(ar, temp):
    if len(ar) == 0:
        print("Queue Empty")
        return
    if not temp:
        for x in range(len(ar) - 1, -1, -1):
            temp.append(ar[x])
    popped = temp.pop(-1)
    ar.remove(popped)
    return popped


arr = []
t = []
enqueue(arr, 1)
enqueue(arr, 2)
peak(arr)
print(arr)
dequeue(arr, t)
enqueue(arr, 3)
print(arr)
dequeue(arr, t)
print(arr)
