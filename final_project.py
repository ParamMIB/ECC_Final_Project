from nicegui import ui
import random
import time

@ui.page('/')
def homepage():
    ui.query('body').style('background-color: lightblue')
    ui.chat_message("Hello! This is your (ECC-101) Python Course Assistant").style('font-size: 21px; font-weight: bold; margin-top: 15px;')
    ui.chat_message("Click a Topic Below to Revise Method/Code Logic or to Explore it").style('font-size: 20px; font-weight: bold;')

    with ui.row().style('gap: 20px; width: 100%; margin-top: 30px'):
        ui.button('Sorting Methods', on_click=lambda: ui.navigate.to('/sorting')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
        ui.button('Graphs using Matplotlib', on_click=lambda: ui.navigate.to('/graphs')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
        ui.button('Turtle', on_click=lambda: ui.navigate.to('/turtle')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')

    with ui.row().style('gap: 20px; width: 100%;'):
        ui.button('Searching', on_click=lambda: ui.navigate.to('/search')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
        ui.button('Text Files', on_click=lambda: ui.navigate.to('/text')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
        ui.button('SQL', on_click=lambda: ui.navigate.to('/sql')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
    
    with ui.row().style('gap: 20px; width: 100%; margin-top: 30px'):
            ui.button('BST', on_click=lambda: ui.navigate.to('/bst')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
    

@ui.page('/sorting')
def sortingpage():
    ui.query('body').style('background-color: lightblue')
    ui.chat_message("Topic: Sorting Methods").style('font-size: 24px; font-weight: bold; margin-top: 15px;')
    ui.label("Sorting is the process of orgainising an unorganised dataset like list or arrays.")
    ui.label("Many different types of sorting techniques with different time complexities are available.")
    ui.label("You can click on a sorting method given below to know more about it.")
    with ui.row().style('gap: 20px; width: 100%; margin-top: 30px'):
            ui.button('Bubble Sort', on_click=lambda: ui.navigate.to('/bubble')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
            ui.button('Insertion Sort', on_click=lambda: ui.navigate.to('/insertion')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
            ui.button('Merge Sort', on_click=lambda: ui.navigate.to('/merge')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
    with ui.row().style('gap: 20px; width: 100%;'):
                ui.button('Quick Sort', on_click=lambda: ui.navigate.to('/quick')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
                ui.button('Heap Sort', on_click=lambda: ui.navigate.to('/heap')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
                ui.button('BST Sort', on_click=lambda: ui.navigate.to('/bst')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')

    ui.label("Time and Space Complexity Summary").style('font-size: 20px; font-weight: bold; color: purple; margin-top: 20px;' )
    columns = [
         {"name": "method", "label": "Sorting Method", "field": "method", "align": "left", "sortable": True},
         {"name": "best", "label": "Best Case", "field":"best", "align":"centre"},
         {"name": "average", "label": "Average Case", "field": "average", "align": "centre"},
         {"name": "worst", "label": "Worst Case", "field": "worst", "align": "centre"},
         {"name": "space", "label": "Space Complexity", "field": "space", "align": "centre"}
    ]
    rows = [
         {"method": "Bubble Sort", "best": "O(n)", "average": "O(n²)", "worst": "O(n²)", "space": "O(1)"},
         {"method": "Insertion Sort", "best": "O(n)", "average": "O(n²)", "worst": "O(n²)", "space": "O(1)"},
         {"method": "Merge Sort", "best": "O(n log n)", "average": "O(n log n)", "worst": "O(n log n)", "space": "O(n)"},
         {"method": "Quick Sort", "best": "O(n log n)", "average": "O(n log n)", "worst": "O(n²)", "space": "O(log n)"},
         {"method": "Heap Sort", "best": "O(n log n)", "average": "O(n log n)", "worst": "O(n log n)", "space": "O(1)"},
         {"method": "BST Sort", "best": "O(n log n)", "average": "O(n log n)", "worst": "O(n²)", "space": "O(n)"},
    ]
    ui.table(columns = columns, rows = rows, row_key = "method")
    ui.button("Homepage", on_click=lambda: ui.navigate.to('/'))

def bubble_sort(L):
     for i in range(len(L)-1):
          for j in range(len(L)-1):
               if L[j] > L[j+1]:
                    L[j],L[j+1] = L[j+1],L[j]
@ui.page('/bubble')
def bubblepage():
     ui.query('body').style('background-color: lightblue')
     ui.chat_message("Bubble Sort").style('font-size: 24px; font-weight: bold; margin-top: 15px;')
     ui.label("Try Sorting A List Using Bubble Sort.")
     ui.label("Give appropriate parameters to generate a random list to be sorted using this method.")
     with ui.row().style('gap: 20px; margin-top: 10px;'):
        n = ui.number('Number of elements: ', value=10, min=1, step=1)
        input_min = ui.number('Lower Limit: ', value=1, step=1)
        input_max = ui.number('Upper Limit: ', value=100, step=1)
     o_label = ui.label().style('font-size: 16px; font-weight: bold;')
     s_label = ui.label().style('font-size: 16px; font-weight: bold;')
     t_label = ui.label().style('font-size: 16px; font-weight: bold;')

     def run_bubble_sort():
        num = int(n.value)
        low = int(input_min.value)
        high = int(input_max.value)
        L = random.choices(range(low,high),k=num)
        o_label.set_text(f"Original list: {L}")
        t1 = time.time()
        bubble_sort(L)
        t2 = time.time()
        s_label.set_text(f"Sorted list: {L}")
        t_label.set_text(f"Time took to bubble sort this list: {t2-t1} seconds")
     ui.button("Generate List and Sort", on_click = run_bubble_sort).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')
     ui.label("How it works (Logic)").style('font-size: 20px; font-weight: bold;')
     ui.markdown("""
     * **Bubble Sort** is a simple comparison-based algorithm.
     * It works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order.
     * It uses a nested for loop to make (n-1)^2 comparisions possible so that any list (even the one sorted in totally opposite way descending) can be sorted
     * The largest element "bubbles up" to its correct position at the end of each pass.
        """)
     ui.label("Python Code").style('font-size: 20px; font-weight: bold;')
     ui.markdown("""
     ```python
     def bubble_sort(L):
     for i in range(len(L)-1):
          for j in range(len(L)-1):
               if L[j] > L[j+1]:
                    L[j],L[j+1] = L[j+1],L[j]
        ```
     """)
     ui.button("Sorting Page", on_click=lambda: ui.navigate.to('/sorting'))


def insertion_sort(L):
    for i in range(1,len(L)):
        key = L[i]
        j = i - 1
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j+1] = key

@ui.page('/insertion')
def insertionpage():
     ui.query('body').style('background-color: lightblue')
     ui.chat_message("Insertion Sort").style('font-size: 24px; font-weight: bold; margin-top: 15px;')
     ui.label("Try Sorting A List Using Insertion Sort.")
     ui.label("Give appropriate parameters to generate a random list to be sorted using this method.")
     with ui.row().style('gap: 20px; margin-top: 10px;'):
        n = ui.number('Number of elements: ', value=10, min=1, step=1)
        input_min = ui.number('Lower Limit: ', value=1, step=1)
        input_max = ui.number('Upper Limit: ', value=100, step=1)
     o_label = ui.label().style('font-size: 16px; font-weight: bold;')
     s_label = ui.label().style('font-size: 16px; font-weight: bold;')
     t_label = ui.label().style('font-size: 16px; font-weight: bold;')

     def run_insertion_sort():
        num = int(n.value)
        low = int(input_min.value)
        high = int(input_max.value)
        L = random.choices(range(low,high),k=num)
        o_label.set_text(f"Original list: {L}")
        t1 = time.time()
        insertion_sort(L)
        t2 = time.time()
        s_label.set_text(f"Sorted list: {L}")
        t_label.set_text(f"Time took to insertion sort this list: {t2-t1} seconds")
     ui.button("Generate List and Sort", on_click = run_insertion_sort).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')
     ui.label("How it works (Logic)").style('font-size: 20px; font-weight: bold;')
     ui.markdown("""
     * **Insertion Sort** splits the list into two invisible sections: a sorted part on the left and an unsorted part on the right.
     * The algorithm starts at the second element (index 1) and assumes the very first element is already a "sorted list" of size one.
     * It picks up the first element from the unsorted side (we call this the key) and compares it with the elements on the sorted side moving backwards from right to left.
     * If elements in the sorted section are greater than the key, the algorithm shifts them one position to the right to create an empty pocket.
     * As soon as it finds an element smaller than the key (or reaches the beginning of the list), it drops the key into that empty pocket.
     * This process repeats for every single element until the unsorted section becomes empty.
        """)
     ui.label("Python Code").style('font-size: 20px; font-weight: bold;')
     ui.markdown("""
     ```python
     def insertion_sort(L):
     for i in range(1,len(L)):
        key = L[i]
        j = i - 1
        while j >= 0 and L[j] > key:
            L[j + 1] = L[j]
            j -= 1
        L[j+1] = key

        ```
     """)
     ui.button("Sorting Page", on_click=lambda: ui.navigate.to('/sorting'))

def merge_sort(L):
    if len(L) <= 1:
        return L

    mid = len(L) // 2

    left = merge_sort(L[:mid])
    right = merge_sort(L[mid:])

    return merge(left,right)


def merge(left,right):
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

@ui.page('/merge')
def mergepage():
     ui.query('body').style('background-color: lightblue')
     ui.chat_message("Merge Sort").style('font-size: 24px; font-weight: bold; margin-top: 15px;')
     ui.label("Try Sorting A List Using Merge Sort.")
     ui.label("Give appropriate parameters to generate a random list to be sorted using this method.")
     with ui.row().style('gap: 20px; margin-top: 10px;'):
        n = ui.number('Number of elements: ', value=10, min=1, step=1)
        input_min = ui.number('Lower Limit: ', value=1, step=1)
        input_max = ui.number('Upper Limit: ', value=100, step=1)
     o_label = ui.label().style('font-size: 16px; font-weight: bold;')
     s_label = ui.label().style('font-size: 16px; font-weight: bold;')
     t_label = ui.label().style('font-size: 16px; font-weight: bold;')

     def run_merge_sort():
        num = int(n.value)
        low = int(input_min.value)
        high = int(input_max.value)
        L = random.choices(range(low,high),k=num)
        o_label.set_text(f"Original list: {L}")
        t1 = time.time()
        merge_sort(L)
        t2 = time.time()
        s_label.set_text(f"Sorted list: {L}")
        t_label.set_text(f"Time took to merge sort this list: {t2-t1} seconds")
     ui.button("Generate List and Sort", on_click = run_merge_sort).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')
     ui.label("How it works (Logic)").style('font-size: 20px; font-weight: bold;')
     ui.markdown("""
     * In **Merge Sort** mid variable declared with value length of L floor divided by 2. L divided into two parts left and right (from first element until mid and from mid until last one respectively) and each recursed to be sorted by again calling merge_sort on them.
     * The sorted list returned via merge function to be defined below that uses the left and right sorted lists to merge them into 1. 
     * The merge function with parameters left and right (two sorted lists) is defined. An empty sorted list made to be returned later, two iterable variables i and j with initial values 0 defined. While loop used to loop until either i or j reaches the end of their respective lists (left and right). 
     * Conditonal statement if used to check if ith element of left sorted list was less than or equal to right j the element, in that case the smaller element ith of left is appended to sorted_list and index i moved 1 unit ahead to (or equal) check for next value in left list. Else condition by default means jth of right is less than ith of left hence that element is appended this time and j incremented instead of i.
     * Now that looping is finished, we add the remaining elements from the left or right list via the extend function and list slicing from the latest iterated value of i and j respectively. Finally, sorted_list is returned. 
        """)
     ui.label("Python Code").style('font-size: 20px; font-weight: bold;')
     ui.markdown("""
     ```python
     def merge_sort(L):
        if len(L) <= 1:
        return L

        mid = len(L) // 2

        left = merge_sort(L[:mid])
        right = merge_sort(L[mid:])

        return merge(left,right)

     def merge(left,right):
        sorted_list = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1

        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])

        return sorted_list

        ```
     """)
     ui.button("Sorting Page", on_click=lambda: ui.navigate.to('/sorting'))

def quick_sort(L,start=0,end=None):
    if end == None:
        end = len(L) - 1
    if end - start < 1:
        return
    else:
        x = partition(L,start,end)
        if start < x:
            quick_sort(L,start,x-1)
        if end > x:
            quick_sort(L,x+1,end)

def partition(L,start,end):
    p = L[start]
    i = start + 1
    j = end
    while i<j:
        if L[i]<p and L[j]>=p:
            i += 1
            j -= 1
        elif L[i]>=p and L[j]<p:
            L[i],L[j] = L[j],L[i]
            i += 1
            j -= 1
        elif L[i]<p and L[j]<p:
            i += 1
        elif L[i]>=p and L[j]>=p:
            j -= 1
    
    if j == i - 1:
        L[start],L[j] = L[j],L[start]
        return j
    elif i==j and L[i] < p:
        L[start],L[i] = L[i],L[start]
        return i
    elif i==j and L[i] >= p:
        L[start],L[i-1] = L[i-1],L[start]
        return i-1

@ui.page('/quick')
def quickpage():
     ui.query('body').style('background-color: lightblue')
     ui.chat_message("Quick Sort").style('font-size: 24px; font-weight: bold; margin-top: 15px;')
     ui.label("Try Sorting A List Using Quick Sort.")
     ui.label("Give appropriate parameters to generate a random list to be sorted using this method.")
     with ui.row().style('gap: 20px; margin-top: 10px;'):
        n = ui.number('Number of elements: ', value=10, min=1, step=1)
        input_min = ui.number('Lower Limit: ', value=1, step=1)
        input_max = ui.number('Upper Limit: ', value=100, step=1)
     o_label = ui.label().style('font-size: 16px; font-weight: bold;')
     s_label = ui.label().style('font-size: 16px; font-weight: bold;')
     t_label = ui.label().style('font-size: 16px; font-weight: bold;')

     def run_quick_sort():
        num = int(n.value)
        low = int(input_min.value)
        high = int(input_max.value)
        L = random.choices(range(low,high),k=num)
        o_label.set_text(f"Original list: {L}")
        t1 = time.time()
        quick_sort(L)
        t2 = time.time()
        s_label.set_text(f"Sorted list: {L}")
        t_label.set_text(f"Time took to quick sort this list: {t2-t1} seconds")
     ui.button("Generate List and Sort", on_click = run_quick_sort).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')
     ui.label("How it works (Logic)").style('font-size: 20px; font-weight: bold;')
     ui.markdown("""
     * In **Quick Sort** we use the partition function to be described below that basically takes the first element from L and puts it in its correct index position (according to sorted list), shifts all elements smaller than the first element to the left half of it and all bigger ones to right half and finally returns the index of the correct position of that element.
     * Next, we recurse quicksort to now sort the left half and right halves left unsorted by using the returned index.
     * In partition function the pivot is defined as p which is taken as the very first element of the list. Next, we define i variable as start value + 1 and j as end value. Using while looping with condition to run until i is less than j we use conditional statements to do some tasks of the partition function.
     * If the ith element is less than p and jth is bigger this is the ideal case where smaller element is leftward and bigger rightward, so we don’t make any changes to L and just bring i and j closer by increasing I by 1 and decreasing j by 1.
     * Using elif condition we cover the unideal case where both ith and jth elements are not in a position where they should be (i.e. ith is greater and jth is less than p), in this case we switch both the elements in the list and again bring i and j closer. We use another elif condition where both ith and jth are less than p in this case only ith elements position is correct but jth is wrong so we increment just i by one keeping j same and make no changes to our list (we wait for the case where i becomes greater than p so we can use the second condition).
     * Similar elif case is defined next where both are now greater, so we just decrement j without any changes in L. After the while loop is iterated, we have a partially covered all the tasks of partition function, now we just need to place pivot in its correct position and return its index. 
     * We again use conditional statements for it. If statement covers the case where j is less than i by one this could have happened when both were in correct place yet adjacent and i incremented and j decremented, so now j holds the smaller number and i the bigger one than p so we just need to swap pivot and jth number to get the result needed and return j to return index of p. 
     * We use elif to cover case where i and j are same and element corresponding to them is less than p. In this case we can just swap out that element with p to get the needed result and return i or j for correct index.
     * Lastly, we cover the case where i and j are equal and element corresponding is greater. We switch out the element just before the ith element with p to get the correct result (this works because this could have been the case when jth element was in its correct place but i was bigger than p but also both these were adjacent to each other so j decremented by one and landed on i but it is confirmed that element before it is smaller than p as otherwise, I would not have moved ahead from it).
        """)
     ui.label("Python Code").style('font-size: 20px; font-weight: bold;')
     ui.markdown("""
     ```python
def quicksort(L,start=0,end=None):
    if end == None:
        end = len(L) - 1
    if end - start < 1:
        return
    else:
        x = partition(L,start,end)
        if start < x:
            quicksort(L,start,x-1)
        if end > x:
            quicksort(L,x+1,end)

def partition(L,start,end):
    p = L[start]
    i = start + 1
    j = end
    while i<j:
        if L[i]<p and L[j]>=p:
            i += 1
            j -= 1
        elif L[i]>=p and L[j]<p:
            L[i],L[j] = L[j],L[i]
            i += 1
            j -= 1
        elif L[i]<p and L[j]<p:
            i += 1
        elif L[i]>=p and L[j]>=p:
            j -= 1
    
    if j == i - 1:
        L[start],L[j] = L[j],L[start]
        return j
    elif i==j and L[i] < p:
        L[start],L[i] = L[i],L[start]
        return i
    elif i==j and L[i] >= p:
        L[start],L[i-1] = L[i-1],L[start]
        return i-1

        ```
     """)
     ui.button("Sorting Page", on_click=lambda: ui.navigate.to('/sorting'))

class CBT():
    def __init__(self,a,l):
        self.arr = a
        self.last = l
    def li(self,i):
        index = 2*i + 1
        if index <= self.last:
            return index
        else:
            return None
    def ri(self,i):
        index = 2*i + 2
        if index <= self.last:
            return index
        else:
            return None
    def pi(self,i):
        if i == 0:
            return None
        else:
            return (i-1)//2

def heapify(tree,i=0):
    left = tree.li(i)
    right = tree.ri(i)
    if left is not None and tree.arr[left] > tree.arr[i] and (right is None or tree.arr[left] > tree.arr[right]):
        tree.arr[left],tree.arr[i] = tree.arr[i],tree.arr[left]
        heapify(tree,left)
    elif right is not None and tree.arr[right] > tree.arr[i] and (left is None or tree.arr[right] > tree.arr[left]):
        tree.arr[right],tree.arr[i] = tree.arr[i],tree.arr[right]
        heapify(tree,right)
    else:
        return
    
def heap_sort(L):
    tree = CBT(L,len(L)-1)
    sorted_list = []
    for i in range((len(L) // 2) - 1, -1, -1):
        heapify(tree, i)
    while tree.last >= 0:
        heapify(tree)
        sorted_list.append(tree.arr[0])
        last_val = tree.arr.pop()
        if tree.arr:
            tree.arr[0] = last_val
        tree.last -= 1
    L[:] = sorted_list[::-1]

@ui.page('/heap')
def heappage():
     ui.query('body').style('background-color: lightblue')
     ui.chat_message("Heap Sort").style('font-size: 24px; font-weight: bold; margin-top: 15px;')
     ui.label("Try Sorting A List Using Heap Sort.")
     ui.label("Give appropriate parameters to generate a random list to be sorted using this method.")
     with ui.row().style('gap: 20px; margin-top: 10px;'):
        n = ui.number('Number of elements: ', value=10, min=1, step=1)
        input_min = ui.number('Lower Limit: ', value=1, step=1)
        input_max = ui.number('Upper Limit: ', value=100, step=1)
     o_label = ui.label().style('font-size: 16px; font-weight: bold;')
     s_label = ui.label().style('font-size: 16px; font-weight: bold;')
     t_label = ui.label().style('font-size: 16px; font-weight: bold;')

     def run_heap_sort():
        num = int(n.value)
        low = int(input_min.value)
        high = int(input_max.value)
        L = random.choices(range(low,high),k=num)
        o_label.set_text(f"Original list: {L}")
        t1 = time.time()
        heap_sort(L)
        t2 = time.time()
        s_label.set_text(f"Sorted list: {L}")
        t_label.set_text(f"Time took to quick sort this list: {t2-t1} seconds")
     ui.button("Generate List and Sort", on_click = run_heap_sort).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')
     ui.label("How it works (Logic)").style('font-size: 20px; font-weight: bold;')
     ui.markdown("""
     * In **Heap Sort** a class CBT (Complete Binary Tree) is first defined which maps a binary tree directly onto a flat Python list (self.arr). Array and the last node (basically max valid index of the active heap) is defined within init definition as a and l. 
     * Further functions to access left and right child are defined using the formula 2xi + 1 and 2xi + 2 for left and right child respectively (i is index of parent node). Then, function to access parent node usinf (i-1) floor divided by 2 is used (i is child's index in this case). 
     * Then we define the heapify function (parameters are the tree and index from where we want to heapify) where the rule is that every parent node must be greater than child node or equal. We define the left and right child of given index (as left and right).
     * We use conditional statements, but before making any comparisons the function evaluates whether child indices are valid (left is not None). First the condition where left is bigger than other two is taken and then in elif condition when right is biggest is taken. 
     * Conditions are followed by switching of values (of bigger child and the parent node) and recursively calling heapify on the child node whose value just changed because it may cause disturbance in the tree below it.
     * Function heapsort with parameter the list is defined. List is converted to CBT class and stored in variable tree. Empty sorted list is made to store values in descending order gradually. Firstly, a bottom-up heap construction is done using a for loop which optimizes performance by skipping leaf nodes which by default hold heap criteria.
     * As any node after (len(L) floor divided by 2) won’t have any child nodes there is no point in heapyfing them. In a valid Max-Heap absolute max always rests at index 0. We define a while loop to run till we don't pop out all the elements from our tree, this loop captures the root value (max) and appends it to the sorted list. 
     * To remove the extracted element pop() is used and placed back at index 0. Tree.last tracking is decremented by 1 as now there is one less element in the tree. In the next iteration heapify again forces the new root value down to it’s proper position and biggest element emerges on the root again. 
     * The sorted list is inverted and stored in L. (To prevent python from generating disconnected variable array, slice assignment is utilized L[:] and to reverse sorted-list[::-1])
        """)
     ui.label("Python Code").style('font-size: 20px; font-weight: bold;')
     ui.markdown("""
     ```python
class CBT():
    def __init__(self,a,l):
        self.arr = a
        self.last = l
    def li(self,i):
        index = 2*i + 1
        if index <= self.last:
            return index
        else:
            return None
    def ri(self,i):
        index = 2*i + 2
        if index <= self.last:
            return index
        else:
            return None
    def pi(self,i):
        if i == 0:
            return None
        else:
            return (i-1)//2

def heapify(tree,i=0):
    left = tree.li(i)
    right = tree.ri(i)
    if left is not None and tree.arr[left] > tree.arr[i] and (right is None or tree.arr[left] > tree.arr[right]):
        tree.arr[left],tree.arr[i] = tree.arr[i],tree.arr[left]
        heapify(tree,left)
    elif right is not None and tree.arr[right] > tree.arr[i] and (left is None or tree.arr[right] > tree.arr[left]):
        tree.arr[right],tree.arr[i] = tree.arr[i],tree.arr[right]
        heapify(tree,right)
    else:
        return
def heapsort(L):
    tree = CBT(L,len(L)-1)
    sorted_list = []
    for i in range((len(L) // 2) - 1, -1, -1):
        heapify(tree, i)
    while tree.last >= 0:
        heapify(tree)
        sorted_list.append(tree.arr[0])
        last_val = tree.arr.pop()
        if tree.arr:
            tree.arr[0] = last_val
        tree.last -= 1
    L[:] = sorted_list[::-1]

        ```
     """)
     ui.button("Sorting Page", on_click=lambda: ui.navigate.to('/sorting'))

class BST:
    def __init__(self,key):
        self.root = key
        self.left = None
        self.right = None

    def insert(self,key):
        if self.root == key:
            return
        elif self.root > key:
            if self.left == None:
                self.left = BST(key)
            else:
                self.left.insert(key)
        else:
            if self.right == None:
                self.right = BST(key)
            else:
                self.right.insert(key)
    
    def min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    def delete(self,key):
        if key < self.root:
            if self.left is not None:
                self.left = self.left.delete(key)
        elif key > self.root:
            if self.right is not None:
                self.right = self.right.delete(key)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                successor = self.right.min()
                self.root = successor.root
                self.right = self.right.delete(successor.root)
        return self
    def balance(self): 
        sorted_elements = self.inorder()
        def build(sarr, start, end):
            if start>end:
                return None
            mid = (start+end)//2
            b= BST(sarr[mid])
            b.left = build(sarr, start, mid-1)
            b.right = build(sarr, mid+1, end)
            return b
        b=build(sorted_elements, 0, len(sorted_elements)-1)
        self.root = b.root
        self.left = b.left
        self.right = b.right

    def inorder(self):
        elements = []
        if self.left != None:
            elements.extend(self.left.inorder())
        elements.append(self.root)
        if self.right != None:
            elements.extend(self.right.inorder())
        return elements 

    def search(self,key):
        if self.root == key:
            return True
        elif self.root > key:
            if self.left != None:
                return self.left.search(key)
            else:
                return False
        else:
            if self.right != None:
                return self.right.search(key)
            else:
                return False


@ui.page('/bst')
def bstpage():
     ui.query('body').style('background-color: lightblue;')
     ui.chat_message("BST Sorting and implementation").style('font-size: 24px; font-weight: bold; margin-top: 15px;')
     ui.label("Try Sorting A List Using BST Sort.").style('font-size: 18px; font-weight: bold; margin-top: 15px;')
     ui.label("Give appropriate parameters to generate a random list to be sorted using this method.")
     with ui.row().style('gap: 20px; margin-top: 10px;'):
        n = ui.number('Number of elements: ', value=10, min=1, step=1)
        input_min = ui.number('Lower Limit: ', value=1, step=1)
        input_max = ui.number('Upper Limit: ', value=100, step=1)
        
     o_label = ui.label().style('font-size: 16px; font-weight: bold;')
     s_label = ui.label().style('font-size: 16px; font-weight: bold; color: green;')
     t_label = ui.label().style('font-size: 16px; font-weight: bold; color: purple;')

     def run_bst_sort():
        global t, L
        num = int(n.value)
        low = int(input_min.value)
        high = int(input_max.value)
        L = random.choices(range(low, high), k=num)
        o_label.set_text(f"Original list for BST: {L}")
        
        t1 = time.time()
        t = BST(L[0])
        for i in L[1:]:
            t.insert(i)
        L = t.inorder()
        t2 = time.time()
        
        s_label.set_text(f"Sorted list for BST: {L}")
        t_label.set_text(f"Time took to BST sort this list: {t2-t1:.6f} seconds")
        
     ui.button("Generate List and Sort", on_click=run_bst_sort).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')

     ui.label("Try Inserting into BST.").style('font-size: 18px; font-weight: bold; margin-top: 15px;')
     ui.label("Give a number to be inserted using this method.")
     with ui.row().style('gap: 20px; margin-top: 10px;'):
        in_num = ui.number("Enter a number to be inserted into the BST: ", value=100, min=1, step=1)

     s_label2 = ui.label().style('font-size: 16px; font-weight: bold; color: green;')
     
     def run_bst_in():
        global t, L
        if 't' not in globals() or t is None:
            ui.notify("Please generate a list and sort to build the base tree first!", type='warning')
            return
            
        val = int(in_num.value)
        t.insert(val)
        s_label2.set_text(f"Updated list with the new element: {t.inorder()}")
        
     ui.button("INSERT", on_click=run_bst_in).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')

     ui.label("Try Deleting from the BST.").style('font-size: 18px; font-weight: bold; margin-top: 15px;')
     ui.label("Give the value to be deleted using this method.")
     with ui.row().style('gap: 20px; margin-top: 10px;'):
         del_num = ui.number("Enter the number to be deleted: ", value=100, min=1, step=1)

     s_label3 = ui.label().style('font-size: 16px; font-weight: bold; color: red;')
     
     def run_bst_del():
         global t
         if 't' not in globals() or t is None:
             ui.notify("Please generate a base tree first!", type='warning')
             return
             
         val = int(del_num.value)
         t = t.delete(val)
         
         if t is None:
             s_label3.set_text("Updated list: Tree is now empty!")
         else:
             s_label3.set_text(f"Updated list with the element deleted: {t.inorder()}")
             
     ui.button("DELETE", on_click=run_bst_del).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')

     ui.label("Try Balancing the BST.").style('font-size: 18px; font-weight: bold; margin-top: 15px;')
     s_label4 = ui.label().style('font-size: 16px; font-weight: bold; color: blue;')
     
     def run_bst_bal():
         global t
         if 't' not in globals() or t is None:
             ui.notify("Please generate a base tree first!", type='warning')
             return
             
         a = t.root 
         t.balance()
         b = t.root 
         s_label4.set_text(f"Updated tree balancing sequence complete! Root node changed from {a} to {b}")
         
     ui.button("BALANCE", on_click=run_bst_bal).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')

     ui.label("Try Searching a value in the BST.").style('font-size: 18px; font-weight: bold; margin-top: 15px;')
     ui.label("Give the value to search for using this method.")
     with ui.row().style('gap: 20px; margin-top: 10px;'):
         search_num = ui.number("Enter the number to search for inside binary tree: ", value=100, min=1, step=1)

     s_label5 = ui.label().style('font-size: 16px; font-weight: bold;')
     
     def run_bst_search():
         global t
         if 't' not in globals() or t is None:
             ui.notify("Please generate a base tree first!", type='warning')
             return
             
         val = int(search_num.value) 
         res = t.search(val)
         if res:
             s_label5.set_text(f"Number {val} is present in the BST!")
             s_label5.style('color: green;')
         else:
             s_label5.set_text(f"Number {val} is completely absent from the BST.")
             s_label5.style('color: red;')
             
     ui.button("SEARCH", on_click=run_bst_search).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')

     ui.label("How it works (Logic)").style('font-size: 20px; font-weight: bold;')
     ui.markdown("""
     * Class **BST** is defined where each instance represents a structural node containing three primary attributes a data payload value (self.root), pointer to a smaller left sub-tree (self.left) and slly, pointer to right (self.right).
     * **Insertion**
     * Function insert defined to insert elements into a BST after defining it, function checks if incoming value matches self.root, if yes then execution is terminated to prevent duplicates.  
     * If value is smaller the algorithm looks at the left child node, if empty it creates a whole new BST child node, but if a child already exists it calls insert recursively down that branch. For larger value similar thing happens but with right child node.
     * **Deletion**
     * Functions  min and del are defined to get the minimum value from a BST and to delete a node. The min function just looks for the leftmost node of the tree as that is the node which holds the minimum value. In deletion there are 3 subcases.
     * If the node is a leaf child we can directlt strip if off from the tree by setting the connection of parent node to None. If there is just one child node it is obvious that that node will directly take the position of the current node so we change the connection of parent of our current node directly to the child node.
     * Function heapsort with parameter the list is defined. List is converted to CBT class and stored in variable tree. Empty sorted list is made to store values in descending order gradually. Firstly, a bottom-up heap construction is done using a for loop which optimizes performance by skipping leaf nodes which by default hold heap criteria.
     * The last case where we have both child present is tricky because we don’t know which child should take the position of current node or even a node below child node may be able to take the position, so we find a value (replacement) to copy into that spot instead. 
     * For example, if current node is 45 and left child is 20 and right is 60 which has further 2 children 50 and 70, we go to the right node and then apply min function which gives us 50 a perfect substitute value. Then we recursively call delete on 50 again and delete the original 50 sitting at leaf (as it falls in case 1).
     * **Balancing**
     * We define a function balance to balance the number of node / height on left and right halves (w.r.t root node). The method calls self.inorder() to extract all entries in the tree.
     * An internal recursive function build computes the middle index of the array segments, picks the median value to serve as the balanced tree root node, then builds left and right sub-trees out of remaining split halves.
     * Main tree overrides its original pointers to root left and right.
     * **Sorting (Inorder)**
     * Function inorder defined to give a sorted list of all the elements in the tree. It checks the left branch first appends the current root value and then appends right branches last. 
     * As by the definition of BST the leftmost elements are least and rightmost are biggest. This guarantees a sorted list in ascending order.
        """)
     ui.label("Python Code").style('font-size: 20px; font-weight: bold;')
     ui.markdown("""
     ```python
class BST:
    def __init__(self,key):
        self.root = key
        self.left = None
        self.right = None

    def insert(self,key):
        if self.root == key:
            return
        elif self.root > key:
            if self.left == None:
                self.left = BST(key)
            else:
                self.left.insert(key)
        else:
            if self.right == None:
                self.right = BST(key)
            else:
                self.right.insert(key)
    
    def min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current
    def delete(self,key):
        if key < self.root:
            if self.left is not None:
                self.left = self.left.delete(key)
        elif key > self.root:
            if self.right is not None:
                self.right = self.right.delete(key)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                successor = self.right.min()
                self.root = successor.root
                self.right = self.right.delete(successor.root)
        return self
    def balance(self): 
        sorted_elements = self.inorder()
        def build(sarr, start, end):
            if start>end:
                return None
            mid = (start+end)//2
            b= BST(sarr[mid])
            b.left = build(sarr, start, mid-1)
            b.right = build(sarr, mid+1, end)
            return b
        b=build(sorted_elements, 0, len(sorted_elements)-1)
        self.root = b.root
        self.left = b.left
        self.right = b.right

    def inorder(self):
        elements = []
        if self.left != None:
            elements.extend(self.left.inorder())
        elements.append(self.root)
        if self.right != None:
            elements.extend(self.right.inorder())
        return elements

        ```
     """)
     ui.button("Sorting Page", on_click=lambda: ui.navigate.to('/sorting'))

import matplotlib.pyplot as plt
@ui.page('/graphs')
def graphspage():
    ui.query('body').style('background-color: lightblue')
    ui.chat_message("Topic: Graphs Using Matplotlib Library").style('font-size: 24px; font-weight: bold; margin-top: 15px;')

    branches = ['EE', 'ECE', 'DSA', 'CSE', 'MnC', 'EP']
    students = [160, 110, 60, 120, 100, 30]
    with ui.row().style('align-items: center; gap: 15 px; margin-top: 15px;'):
        ui.label("Choose Graph Type: ").style('font-size: 16px; font-weight: bold;')
        graph_selector = ui.select(
            options=['Line Graph', 'Bar Graph', 'Pie Chart'],
            value='Line Graph',
            on_change=lambda: render_selected_graph.refresh()
        ).style('width: 200px; background-color: white;')
    @ui.refreshable
    def render_selected_graph():
        selected = graph_selector.value
        with ui.pyplot(figsize=(6, 3.8)):
            if selected == 'Line Graph':
                plt.plot(branches,students, color='blue', marker= '*', linestyle='-')
                plt.title("Student Count (Line)")
                plt.xlabel("Branches")
                plt.ylabel("Number of Students")
            elif selected =='Bar Graph':
                plt.bar(branches, students, color='darkblue')
                plt.title("Student Count (Bar)")
                plt.xlabel("Branches")
                plt.ylabel("Number of Students")
            elif selected == 'Pie Chart':
                plt.pie(students, labels=branches, startangle=90, colors=['yellow','orange','red','purple','violet','blue'])
                plt.title("Student Count (Pie)")
    render_selected_graph()
    ui.label("Few Codes Implementation").style('font-size: 20px; font-wight: bold; margin-top: 15px;')
    ui.markdown("""
    ```python
#PART 1
#f(x) = x^3 - 5x
#g(x) = x^2 + x - 2
import matplotlib.pyplot as plt
def f(x):
    return x**3 - 5*x
def g(x):
    return x**2 + x - 2
x_list = []
y1 = []
y2 = []

for i in range(10001):
    x_list.append(-5 + 0.001*i)
    y1.append(f(x_list[i]))
    y2.append(g(x_list[i]))

plt.plot(x_list,y1)
plt.plot(x_list,y2)
plt.show()
    
    ```
    """)
    ui.image('graph_output.png').style('width: 300px; border-radius: 4px; margin-bottom: 10px;')

    ui.label("Logic Breakdown").style('font-size: 20px; font-wight: bold; margin-top: 15px;')
    ui.markdown("""
    * matplotlib module imported as plt
    * functions f(x) and g(x) defined using the given formulas
    * 3 lists: x_list for common x axis, y1 for y axis plot of f(x) and y2 for g(x) defined
    * for loop ran 10001 times to get a clean smooth looking curve, x list appended starting from -5 and increased by 0.001 so as to reach +5 at the last iteration
    * y1 and y2 appended using appropriate functional call with corresdponding x_list values
    * plt.plot(x_list,y1/y2) used 2 times to get a plot
    * plt.show() to finally show the graphs
    """)

    ui.button("Homepage", on_click=lambda: ui.navigate.to('/'))

@ui.page('/turtle')
def turtlepage():
    ui.query('body').style('background-color: lightblue')
    ui.chat_message("Topic: Logo/Design Using Turtle")
    ui.label("Reviewing essential Turtle graphic commands, logic, and syntax.").style('font-size: 16px; margin-bottom: 15px;')
    ui.label("1. Core Built-In Commands Reference").style('font-size: 20px; font-weight: bold; margin-top: 15px;')
    with ui.column().style('gap: 5px; margin-left: 15px; margin-bottom: 20px;'):
        ui.label("* forward(distance) / fd() : Moves the turtle forward by the specified number of steps.").style('font-size: 15px;')
        ui.label("* backward(distance) / bk() : Moves the turtle backward by the specified number of steps.").style('font-size: 15px;')
        ui.label("* left(angle) / lt() : Turns the turtle counter-clockwise by a specified number of degrees.").style('font-size: 15px;')
        ui.label("* right(angle) / rt() : Turns the turtle clockwise by a specified number of degrees.").style('font-size: 15px;')
        ui.label("* circle(radius) : Draws a complete circle with a given radius parameter anticlockwise with tangent direction that turtle is currently facing.").style('font-size: 15px;')
        ui.label("* penup() / pu() : Lifts the pen up so moving the turtle won't draw any lines.").style('font-size: 15px;')
        ui.label("* pendown() / pd() : Puts the pen down so moving the turtle draws lines again.").style('font-size: 15px;')
        ui.label("* teleport(x, y) : Instantly moves the turtle to position (x, y) without drawing a line.").style('font-size: 15px;')
        ui.label("* pos() : Returns the turtle's current position coordinate tuple (x, y).").style('font-size: 15px;')
        ui.label("* distance(x, y) : Returns the absolute distance from the turtle to the point (x, y).").style('font-size: 15px;')

    ui.label("2. Code Examples & Logic").style('font-size: 20px; font-weight: bold; margin-top: 15px;')
    ui.label("Example A: N-Sided Regular Polygon & Circle Touching just 1 Side of it.").style('font-size: 20px; font-weight: bold; color: darkblue; margin-top: 10px;')
    ui.markdown("""
```python
from turtle import *

s = int(input("Enter number of sides: "))
speed(10)

for i in range(s):
    forward(100)
    left(360/s)

forward(50)
circle(100)
input("Press enter to exit...")
```
    """)
    ui.label("Logic Breakdown").style('font-size: 18px; font-weight: bold; margin-top: 15px;')
    ui.markdown("""
    * Every turtle method in the module imported using '*' (imports everything)
    * User asked for the closed polygon's number of sides
    * turtles speed increased to max 10
    * for loop used to make the n sided poylgon by running n times
    * 100 units forward moved followed by turtle turning angle leftwards by 360/s degrees as For any regular polygon, the sum of all exterior angles is always **360°**. Dividing 360 by the number of sides `s` calculates the precise angle the turtle must turn at each vertex.
    * `circle(100)`: Draws a circle with a radius of 100 units from the turtle's current landing spot.
    """)
    ui.image('polygon_output.png').style('width: 300px; border-radius: 4px; margin-bottom: 10px;')

    ui.label("Example B: Centered 5-Pointed Star").style('font-size: 20px; font-weight: bold; color: darkblue; margin-top: 15px;')
    ui.markdown("""
```python
from turtle import *

teleport(0, 95.10)
right(72)
forward(200)

for i in range(4):
    right(144)
    forward(200)

input("Press Enter to exit")
```
    """)
    ui.label("Logic Breakdown").style('font-size: 18px; font-weight: bold; margin-top: 15px;')
    ui.markdown("""
    * All turtle methods imported
    * `teleport(0, 95.10)`: Offsets the starting position to keep it centered
    * first side of the star drawn outside the for loop as the first angle that had to be turned was half of that to be turned otherwise
    * for loop ran 4 times to complete the rest 4 sides of the star
    * `right(144)`: A standard star layout requires an interior point angle of **36°**. The required exterior turning angle for the turtle is 180° - 36° = 144°.
    * `forward(200)`: Moves the turle forward by 200 units
    """)
    ui.image('star_output.png').style('width: 300px; border-radius: 4px; margin-bottom: 10px;')

    ui.button("Homepage", on_click=lambda: ui.navigate.to('/'))

@ui.page('/search')
def searchpage():
    ui.query('body').style('background-color: lightblue')
    ui.chat_message("Topic: Searching Methods").style('font-size: 24px; font-weight: bold; margin-top: 15px;')
    ui.label("Searching is the process of finding if the element is present inside a dataset or even finding it's position inside the dataset.")
    ui.label("Searching can be implemented using many different algorithms")
    ui.label("Given below are a few searching algorithms you can try, they have different space and time complexities")
    with ui.row().style('gap: 20px; width: 100%; margin-top: 30px'):
            ui.button('Linear Search', on_click=lambda: ui.navigate.to('/linear')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
            ui.button('Binary Search', on_click=lambda: ui.navigate.to('/binary')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
            ui.button('BST Search', on_click=lambda: ui.navigate.to('/bst')).style('padding: 16px; font-size: 16px; flex-grow: 1; background-color: darkblue;')
    ui.label("Searching Complexity Summary").style('font-size: 20px; font-weight: bold; color: purple; margin-top: 20px;')

    columns = [
        {"name": "method", "label": "Searching Method", "field": "method", "align": "left", "sortable": True},
        {"name": "best", "label": "Best Case Time", "field": "best", "align": "center"},
        {"name": "average", "label": "Average Case Time", "field": "average", "align": "center"},
        {"name": "worst", "label": "Worst Case Time", "field": "worst", "align": "center"},
        {"name": "space", "label": "Space Complexity", "field": "space", "align": "center"}
    ]

    rows = [
        {"method": "Linear Search", "best": "O(1)", "average": "O(n)", "worst": "O(n)", "space": "O(1)"},
        {"method": "Binary Search", "best": "O(1)", "average": "O(log n)", "worst": "O(log n)", "space": "O(1)"},
        {"method": "BST Search", "best": "O(1)", "average": "O(log n)", "worst": "O(n)", "space": "O(1)"},
    ]

    ui.table(columns=columns, rows=rows, row_key="method").style('width: 100%; background-color: white;')
    ui.button("Homepage", on_click=lambda: ui.navigate.to('/'))

def linear(key,L):
    for i in range(len(L)):
        if L[i] == key:
            return i
    return False

@ui.page('/linear')
def linearpage():
    ui.query('body').style('background-color: lightblue')
    ui.chat_message("Linear Search").style('font-size: 24px; font-weight: bold; margin-top: 15px;')
    ui.label("In Linear search we iterate throught the list one element at a time until we find the element we were looking for")
    ui.label("Can be used on unsorted list but time complexity is high")
    ui.label("Element index can be returned easily")

    def run_gen_list():
        global L1
        num = int(n.value)
        low = int(input_min.value)
        high = int(input_max.value)
        L1 = random.choices(range(low,high),k=num)
        o_label.set_text(f"List: {L1}")


    with ui.row().style('gap: 20px; margin-top: 10px;'):
        n = ui.number('Number of elements: ', value=10, min=1, step=1)
        input_min = ui.number('Lower Limit: ', value=1, step=1)
        input_max = ui.number('Upper Limit: ', value=100, step=1)
    o_label = ui.label().style('font-size: 16px; font-weight: bold;')

    ui.button("Generate List", on_click=run_gen_list).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')

    with ui.row().style('gap: 20px; margin-top: 10px;'):
        no = ui.number('Enter number to be searched: ', value=100)
    s_label = ui.label().style('font-size: 16px; font-weight: bold;')


    def run_linear_search():
        global L1
        val = float(no.value)
        a = linear(val,L1)
        if a == False:
            s_label.set_text(f"Number {val} not present in list...")
        else:
            s_label.set_text(f"Number {val} found at index {a} in the list...")
    ui.button("SEARCH", on_click=run_linear_search).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')
    ui.label("How it works (Logic)").style('font-size: 20px; font-weight: bold;')
    ui.markdown("""
        * In *Linear Search* we use a for loop that runs the length of the given list unless it finds the element to be found.
        * If condition used to check if it finds the element and the return the index (the iterative variable i).
        * If even after iterating through the entire list it finds nothing False boolean value is returned
    """)
    ui.label("Python Code").style('font-size: 20px; font-weight: bold;')
    ui.markdown("""
    ```python
    def linear(key,L):
    for i in range(len(L)):
        if L[i] == key:
            return i
    return False
    ```
    """)

    ui.button("Searching Methods", on_click=lambda: ui.navigate.to('/search')).style('background-color: darkblue; padding: 10px 20px; margin-top: 80px;')

def binary(a,L):
    start = 0
    end = len(L) - 1
    mid = (start + end)//2
    while end >= start:
        mid = (start + end)//2
        if L[mid] == a:
            return True
        elif L[mid] > a:
            end = mid - 1
        else:
            start = mid + 1
    return False

@ui.page('/binary')
def binarypage():
    ui.query('body').style('background-color: lightblue')
    ui.chat_message("Binary Search").style('font-size: 24px; font-weight: bold; margin-top: 15px;')
    ui.label("Binary Search is a quicker alternative to linear search it basically divides the list in two halves each time.")
    ui.label("Much less time complexity but doesn't work on unsorted list")

    def run_gen_list():
        global L2
        num = int(n.value)
        low = int(input_min.value)
        high = int(input_max.value)
        L2 = random.choices(range(low,high),k=num)
        L2.sort()
        o_label.set_text(f"List: {L2}")

    with ui.row().style('gap: 20px; margin-top: 10px;'):
        n = ui.number('Number of elements: ', value=10, min=1, step=1)
        input_min = ui.number('Lower Limit: ', value=1, step=1)
        input_max = ui.number('Upper Limit: ', value=100, step=1)
    o_label = ui.label().style('font-size: 16px; font-weight: bold;')

    ui.button("Generate List", on_click=run_gen_list).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')

    with ui.row().style('gap: 20px; margin-top: 10px;'):
        no = ui.number('Enter number to be searched: ', value=100)
    s_label = ui.label().style('font-size: 16px; font-weight: bold;')


    def run_bin_search():
        global L2
        val = float(no.value)
        a = binary(val,L2)
        if a == False:
            s_label.set_text(f"Number {val} not present in list...")
        else:
            s_label.set_text(f"Number {val} found in the list...")
    ui.button("SEARCH", on_click=run_bin_search).style('background-color: darkblue; padding: 10px 20px; margin-top: 10px;')
    ui.label("How it works (Logic)").style('font-size: 20px; font-weight: bold;')
    ui.markdown("""
        * In *Bianry Search* we first define three variables start end and mid ( mid is inside while) with initial values 0, lenght of list a list -1 and mid floor value between them respectively.
        * While loop is ran with contidition to run until end becomes smaller than start
        * Conditional statements used to compare mid index value in list and the value to be found
        * If they match Boolean True returned otherise the half list is eliminated by changing the value of start or end to change the mid in the next pass of while
    """)
    ui.label("Python Code").style('font-size: 20px; font-weight: bold;')
    ui.markdown("""
    ```python
def binary(a,L):
    start = 0
    end = len(L) - 1
    mid = (start + end)//2
    while end >= start:
        mid = (start + end)//2
        if L[mid] == a:
            return True
        elif L[mid] > a:
            end = mid - 1
        else:
            start = mid + 1
    return False
    ```
    """)

    ui.button("Searching Methods", on_click=lambda: ui.navigate.to('/search')).style('background-color: darkblue; padding: 10px 20px; margin-top: 80px;')

        

    
@ui.page('/text')
def textpage():
    ui.query('body').style('background-color: lightblue;')
    ui.chat_message("Topic: Text Files Handling in Python").style('font-size: 24px; font-weight: bold; margin-top: 15px;')
    ui.label("Here Python interacts with your computer storage system to permanently write and extract text datasets.")
    ui.label("Here your progress is saved permanently inside ROM and not just temporarily inside RAM (like in terminal).")

    ui.label("1. Live File System").style('font-size: 20px; font-weight: bold; margin-top: 15px;')
    ui.label("Enter a filename and content below to physically create and read a text file on your laptop/PC.")

    with ui.row().style('gap: 20px; margin-top: 10px; width: 100%; max-width: 500px;'):
        # Input fields for tracking structural state targets
        filename_input = ui.input(label='Filename', value='trial.txt', placeholder='Enter name with .txt').style('flex-grow: 1;')
    
    content_input = ui.textarea(label='File Content', placeholder='Type lines of text here...', value='Line 1: Hello World!\nLine 2: I am Param Agarwal from IITR ECE!').style('width: 100%; max-width: 600px;')

    status_msg = ui.label("").style('font-size: 15px; font-weight: bold; color: green;')
    read_output = ui.label("").style('font-size: 15px; font-family: monospace; background-color: #f3f4f6; padding: 10px; border-radius: 4px; display: none; width: 100%; max-width: 600px;')

    def run_create_file():
        name = filename_input.value.strip()
        text_data = content_input.value
        
        if not name.endswith('.txt'):
            name += '.txt'
            filename_input.value = name
            
        try:
            f = open(name, 'w')
            f.write(text_data)
            f.close()
            
            status_msg.set_text(f"File with name: '{name}' has been made on your laptop with its content.")
            status_msg.style('color: green;')
            read_output.style('display: none;')
            ui.notify(f"Created file: {name}", type='positive')
        except Exception as e:
            status_msg.set_text("Error writing file")
            status_msg.style('color: red;')

    def run_read_file():
        name = filename_input.value.strip()
        if not name.endswith('.txt'):
            name += '.txt'
            
        try:
            f = open(name, 'r')
            lines = f.readlines()
            f.close()
            
            c_lines = []
            for line in lines:
                c_lines.append(line.strip())
            display_text = "\n".join(c_lines)
            
            status_msg.set_text(f" Successfully read '{name}' from storage")
            status_msg.style('color: darkblue;')
            read_output.set_text(display_text)
            read_output.style('display: block;')
        except FileNotFoundError:
            status_msg.set_text(f"File '{name}' not found! Please generate it first.")
            status_msg.style('color: red;')
            read_output.style('display: none;')
        except Exception as e:
            status_msg.set_text("Error reading file")
            status_msg.style('color: red;')

    with ui.row().style('gap: 15px; margin-top: 15px;'):
        ui.button("WRITE FILE", on_click=run_create_file).style('background-color: darkblue; padding: 10px 20px;')
        ui.button("READ FILE", on_click=run_read_file).style('background-color: darkblue; padding: 10px 20px;')

    ui.separator().style('margin-top: 25px;')

    ui.label("2. How it works (Logic Breakdown)").style('font-size: 20px; font-weight: bold; margin-top: 15px;')
    ui.markdown("""
* **File Access Modes (`'w'` and `'r'`)**: The second parameter dictates target directory actions. Passing `'w'` opens the structure for writing, **overwriting** any older file sharing that name. Mode `'r'` strictly grants read access permissions.
* **Resource Cleanup (`.close()`)**: You must always apply `.close()` at the final execution sequence line to securely commit cached changes to your hard drive and release system hooks.
* **Line Sanitation (`.strip()`)**: When reading line strings sequentially via loops, Python preserves raw tracking linebreaks (`\\n`). Invoking `.strip()` sanitizes formatting noise by trimming trailing white spaces and control tabs cleanly.
    """)

    ui.label("3.Code Syntax Example").style('font-size: 20px; font-weight: bold; margin-top: 15px;')
    ui.markdown("""
```python
# Part A: Writing numeric lines sequentially
f = open('ab.txt', 'w')
for i in range(50):
    f.write(str(i) + '\\n')
f.close()

# Part B: Iterating and reading with string sanitation
f = open('ab.txt', 'r')
for i in f:
    print(i.strip())
f.close()
```
    """)

    ui.button("Homepage", on_click=lambda: ui.navigate.to('/')).style('margin-top: 25px; background-color: #4b5563;')

@ui.page('/sql')
def sqlpage():
    ui.query('body').style('background-color: lightblue')
    ui.chat_message("Topic: SQL Integrated With Python")


    ui.button("Homepage", on_click=lambda: ui.navigate.to('/'))

ui.run(title="Python Topics Assistant")
