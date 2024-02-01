# Data-Structures

My solution for the "Data Structures" course on Coursera:
https://www.coursera.org/learn/data-structures/

Here are my notes from the course:

## Arrays
* Contiguous area of memory consisting of equal sized elements indexed by contiguous integers.
* **Random access:** Constant time read or write an element in the array. <br> Address = array_addr + element_size*(i-first_index)
<br>Supported operations:

|          | Add      | Remove  |
| -------- | -------- | ------- |
| Beginning| $O(n)$   | $O(n)$  |
| Middle   | $O(n)$   | $O(n)$  |
| End      | $O(1)$   | $O(1)$  |

* Dynamic arrays (resizable): Start the array with capacity = 1 and:
    * While doing PushBack, resize the array by 2 times every time the array becomes full. Amortised cost: $O(1)$
    * While doing PopBack, resize the array by half every time the size of array filled becomes half of the array capacity.
<br> We can use any constant growth factor to get the same amortised cost. However, if we increase the array by a constant number of spaces, the amortised cost becomes $O(n)$.

## Linked Lists
List elements need not be stored in contiguous areas of memory.
* **Singly Linked Lists:** Node contains a key and a pointer to the next node.
* **Doubly Linked Lists:** We have a head pointer, a tail pointer and each node contains a key and a pointer to the next node and one to the previous node.
<br>Supported operations:

| Operation            | Singly Linked List | Doubly Linked List | LL with tail | 
| -------------------- | -------- | ------- | ------- |
| PushFront(key)       | $O(1)$   |   |   |
| TopFront()           | $O(1)$   |   |   |
| PopFront()           | $O(1)$   |   |   |
| PushBack(key)        | $O(n)$   |   | $O(1)$ |
| TopBack()            | $O(n)$   |   | $O(1)$ |
| PopBack()            | $O(n)$   | $O(1)$ |   |
| Find(key)            | $O(n)$   |   |   |
| Erase(key)           | $O(n)$   |   |   |
| Empty()              | $O(1)$   |   |   |
| AddBefore(Node, key) | $O(n)$   | $O(1)$ |   |
| AddAfter(Node, key)  | $O(1)$   |   |   |

## Stacks
Stacks or LIFO queues are abstract data type with the operations:
* Push(key)
* Top()
* Pop()
* IsEmpty()

Each operation is $O(1)$ and can be implemented with arrays or linked lists. If implemented using arrays, some part of the array which is not used is wasted. If we implement using linked lists, there is some extra overhead for each element being pushed because there is a pointer for each.

## Queues
FIFO: Abstract datatype with operations:
* Enqueue(key)
* Dequeue()
* IsEmpty()

Each operation is $O(1)$ and can be implemented using arrays (will need to have a circular array) or linked lists (with a tail pointer).

## Trees
* A Tree is:
    * empty, or
    * a node with
        * a key, and 
        * a list of child trees (for binary tree - left and right instead)
        * (optional) parent

* Some terminologies: root, parent, child, ancestor, descendant, sibling, leaf, interior node, level, height, forest.
* A lot of the times, recursion is useful for tree based problems.
* Tree Traversal: 2 main ways:
    * Depth first traversal: Eg. Recursive implementations of:
        * InOrderTraversal (Defined only for binary trees),
        * PreOrderTraversal
        * PostOrderTraversal
    * Breadth First Traversal:
        * LevelTraversal


## Priority Queue
* A generalisation of a queue where each element is assigned a priority and elements come out in order by priority. Supported operations:
    * Insert(p) to insert an element with priority p.
    * ExtractMax()
* Implementations:
    * Unsorted Array/List: Insert is $O(1)$, while ExtractMax is $O(n)$.
    * Sorted Array/List: Insert is $O(n)$, while ExtractMax is $O(1)$.
    * Binary Heap: Min heap
        * Insert: Attach the new node to a leaf and then sift up until the heap property is satisfied for all nodes. Time: $O(Tree Height)$
        * ExtractMax: Bring one of the leaves to the root and then sift down until the heap property is satisfied for all nodes. Time: $O(Tree Height)$.
    <br>
    To keep the tree shallow, we need to ensure that it is a complete binary tree. It can then also be stored as an array (space efficient). Easy to implement as well.
* Build Heap: For $i$ from $\lfloor n/2 \rfloor$ down to $1$, call sift down. Running time: $O(n)$.
* Heap Sort: In place and asymptotically optimal.
    ```
    def HeapSort(A):
        BuildHeap(A)
        Repeat n-1 times:
            swap A[1] and A[size]
            size = size-1
            SiftDown(1)
    ```
* Partial Sorting can be solved in $O(n)$ if $k=O(n/logn)$, that is, $k$ is small.

## Disjoint Sets
* Operations:
    * MakeSet(x) to create a singleton set {x}
    * Find(x) returns ID of the set containing x
    * Union(x, y) to merge 2 sets containing x and y
* Implementation:
    * Represent each set as a rooted tree
    * Find(x) returns ID of the set as the root of the tree
    * $parent[i]$ is the parent of $i$th element, or $i$ if it is the root.
    * **Union by rank heuristic:** Store the heights of all nodes using array rank. While doing union, hang the smaller tree on the larger one.
    <br>
    Time complexity for find and union: $O(logn)$
    * **Path Compression heuristic:** Finding the root (ID) for an element involves attaching the root with all the elements on the path from the element to the root.
    <br>
    Amortised time complexity for find and union: $O(log*n)$ where $log*$ represents the iterated logarithm function - up to 5-6 for any practical values of n.
    ```
    def Find(i):
        if i != parent(i):
            parent(i) = Find(parent[i])
        return parent[i]
    ```

## Hashing
Used for sets and dictionaries in Python
* Direct Addressing: Space intensive $O(N)$ where $N$ is the set of all possible values. Practical only if the possible universe is small.
* Objectives of a good hash function:
    * Fast to compute
    * Must be deteministic
    * Minimum collisions - Chaining to handle collisions
    * Direct addressing with $O(m)$ memory, where $m$ is the cardinality of the hash function.

* Complexity analysis:
    * Memory consumption with chaining: $O(n+m)$, where $n$ is the number of elements currently stored in the hash table and $m$ is the cardinality of the hash function.
    * Operations work in time: $O(c+1)$ where c is the length of the chain.
    * So, we want both $m$ and $c$ to be small.
    * Load factor, $\alpha = n/m$, measuring how filled up the array is
    * What if the number of keys is unknown in advance? We can start with a very big hash table, but then we will waste a lot of memory. We thus need dynamic arrays. We can copy the ideas from dynamic arrays.

* Universal Family: define a family of hash functions using randomisation in order to ensure that the function doesn't break for a particular set of inputs.
    * For any 2 keys, the probability of collision $\leq 1/m$ over all hash functions
    * Or the average length of the longest chain is $O(1+\alpha)$
    * **For integers:**
        * Choose a prime number, $p$ just greater than the range of integers and cardinality $m$.
        * ${((a*x+b) mod p) mod m}$ for all $a,b: 1\leq a \leq p-1, 0\leq b \leq p-1$ is a universal family.
        * Convert all possible integers from 0 to $10^L-1$.
        * Choose $a$ and $b$ randomly from the defined ranges.
    * **For strings:**
        * Convert all characters into integers using, for example, ascii encoding.
        * Choose a big prime number $p$.
        * $(\sum_{i=0}^{|S|-1} S[i]x^i) mod p$ with $1 \leq x \leq p-1$
        * Cardinality fix: take modulo with cardinality, $m$.
        * For any 2 strings $s_1$ and $s_2$ of length at most $L+1$, the probability of collision is at most $L/p + 1/m$. For this to be a universal family, we can choose $p$ to be very large.
* Searching a pattern $P$ in a text $T$:
    * Running time of naive find pattern function is $O(|T||P|)$
    * Optimised approach - Rabin Karp's Algorithm:
        * For each $i$ denote $H[i]$ to be the hash value of the substring starting at index $i$ having length $|P|$.
        * Then, $ H[i] = xH[i+1] + (T[i] - T[i+|P|]x^{|P|}) mod p $.
        * Time complexity: $O(|T|+(q+1)|P|)$ where $q$ is the number of occurences of $P$ in $T$ - usually small.

* Hash function in python:
    * Works if and only if the input is an immutable object.
        * if input is integer, returns the same integer
        * if float, string, tuple (or any other immutable object) - hashes them
    * While using custom data structures, we can also customise the standard python operators by overriding the __hash()__ method. (Other standard operators which can be useful are listed here: https://docs.python.org/3/library/operator.html) Example:

```
class Emp:
    def __init__(self, emp_name, id):
        self.emp_name = emp_name
        self.id = id
 
    def __eq__(self, other):
        # Equality Comparison between two objects
        return self.emp_name == other.emp_name and self.id == other.id
 
    def __hash__(self):
        # hash(custom_object)
        return hash((self.emp_name, self.id))
```
* Distributed Hash tables:
    * In order to save some space/cost and to do "instant uploads", dropbox/google drive use several hash functions to ascertain when multiple files are the same.
    * Precompute hashes for the files already stored to compare with.
    * For fast search/access on a very large set on trillions of objects - distributed hash tables:
        * **Scaling:** Get many computers $(n)$ and create a hash table on each of them.
        * Determine which computer owns the object O: $h(O) mod n$.
        * **Fault Tolerance:** Computers sometimes break. So:
            * Need to store several copies of the data.
            * When the service grows and new computers are added to the cluster, the formula no longer works.
        * Need **Consistent Hashing**.
            * Choose a hash function with cardinality $m$ and put numbers from $0$ to $m-1$ on a circle clockwise.
            * Each object is stored on the closest computer.
            * When a computer goes off - the neighbours take its data
            * When a computer is added, it takes the data from the neighbours.
            * Overlay Network: In practice, we have something like: node knows information about nodes at $\pm 1, \pm 2, \pm 4, ..., O(logn)$

## Binary Search Trees
A local search datastructure that stores a number of elements each with a key coming from an ordered set. Supported operations: Range Search and Nearest neighbours search.
* Search tree instead of sorted array to enable insert and deletion easily.
* Search Tree property: X's key is larger than the key of any descendant of its left child and smaller than the key of any descendant of its right child.
* Some operations:
    * Find works just like binary search.
    * $Next(N)$ - to get the key with value just next to the value at $N$
        <br> if $N.right$ is not $NULL$, return $LeftDescendant(N.right)$
        <br> otherwise, return $RightAncestor(N)$
    * For $RangeSearch(x, y)$, do $node = Find(x)$ and keep on doing $node = Next(node)$ until node value is less than $y$.
    * $Insert(k)$ works the same as $Find(k)$.
    * $Delete(k)$:
    ```
    def delete(N):
        if N.right is NULL:
            remove N, promote N.left
        else:
            X = Next(N)  # this means X.left is NULL
            Replace N by X, promote X.right
    ```
* Problem: Ensuring that operations don't take too long because of the imbalance in the trees.
    * Solutions: AVL Trees, Red Black Trees, Treaps, Splay Trees etc.
    * **AVL Trees:**
        * AVL property - $ |N.left.height - N.right.height| \leq 1$
        * The height of the tree is $O(logn)$.
        * When inserting, only the nodes on the insertion path are affected in terms of the height. So, we do required left right rotations along the path to ensure that the tree is balanced.
    * **Splay Trees:** Put frequenctly searched items close to the root. Amortised cost is $O(logn)$.
