# DataStructuresAlgorithms

## Complexity Theory
#### Types of Complexity
1. Time
    * Many algorithms are affected by the time it takes for them to complete their task.
    So it is important to know how long it may tak to complete a task and what algorithm bout bes suit that requirement.
2. Space
   * Some algorithms require a lot of memory or disk space. This means that  algorithms may sometimes trade space for speed.
3. Other Scarce Resources
    * Network Speed
    * Hardware Capacity such as GPUs or CPUs

#### Why bother with Algorithm complexity?
* The ability to predict an algorithms behaviour saves time in future development when you realise the algorithm takes
too long or uses too much memory for particular use-cases. Knowing what an algorithm will do given different sets of input 
is key to choosing the right algorithm for the job. 
* Comparing algorithms allows us to decide which algorithm would work best for us. Bubble sort works well on sorted data, but terribly
on unsorted data. Knowing such facts allows us to quickly determine the most suitable algorithm for the task.

## Big O Notation
Big O Notation is used to study the performance of algorithms. Looking into the upper bound of an
algorithms performance, or more notably, the worst case performance.
- An algorithm with a good Big O performance means it wont fail you when you use it in a particular use case.
- It also measures **Asymptotic Behaviour**
    - As the size of the problem grows, how does the algorithm continue to perform?
    - Another way of looking at this is; what happens to performance as N grows larger and larger?
    
### Big O Rules:
1. **O(N)**: If an algorithm performs f(N) steps, then it is O(f(N))
2. **O(N+N) = O(2N)**: If an algorithm performs f(N) steps followed by g(N) steps, then it is O(f(N) + g(N))
3. **O(N^2 + N) = O(N^2)**: If f(N) > g(N) for large N, then O(f(N) + g(N) = O(f(N)))
    - if f is greater than g for large numbers, you can simplify by rounding up f and g to just f. Since f will eventually dominate the runtime.
4. **O(N * N) = O(N^2)**: If an algorithm performs g(N) steps for reach of f(N) steps, then O(f(N) * g(N))
5. **O(f(N))**: Ignore constant multiples
    * O(C * f(N) = O(f(N)))
    * O(f(C * N) = O(f(N)))
    
## Typical Runtime Functions

* Big O notation helps to describe some common complexity functions. 

### O(1)
* A few algorithms take a constant amount of time , such as setting a variable to the first item in an array. 
It takes one step. This is described as being an **O(1)** behaviour. 
* If an algorithm performs a defined number of steps, its constant runtime would never change. Even if it is a million steps, the constant runtime never changes.
*as long as the number of steps does not change when N increases*.

### O(n^2)
* Is the order done twice, simply put. As big O rule 2 demonstrates.

### O(n^c)
* C nested loops where c is the constant demonstrates c amount of loops
* Here we know that c is constant and N typically does not increase as c increases

### O(log N)
* These are problems that divide a search space into 2 pieces at each step
* Let us say you want to search for the number 15:
    1. you start at the root node [21]
    2. [21] is more than [15] so we go down the lower node [9]
    3. we have now cut the collection of possible nodes by half\
    4. this will continue until the relevant node is found
```
            [21]
            /  \
           /    \
        [9]      [35]
        / \      /  \
      [7] [15] [24] [45]
```
* With Log N, O Notation is always the same no matter how many Log bases (such as heb, 10 or binary) are used:
    * LogB(N) = LogA(N) / LogA(B)
    
### O(2^n)
* Exponential time where the growth doubles with each addition of the input data set
* This is commonly found in brute force algorithms

### O(N!)
* Factorial means N * (N -1) * (N - 2) * (N - 3) ...
* 6! = 6 * 5 * 4 * 3 * 2 * 1

## Comparing Runtime Functions
Now lets see how different runtime functions may compare to each other.
For example f(n^2) would grow much faster than f(n).

You would find that functions such as N Factorial (N!) have an extremely steep increase in the tme it takes
to execute the task as more data is given to it.
In this respect, we can consider (N) as having a linear line where there is a steady increase in time as more data is given, but not so much so that the
function could be considered slow.
O(Log N) is considered the fastest method of designing a function, since a logarithmic function cuts it's workload in half with every step.

| Runtime   | F(1, 100)   | Time       |
|-----------|-------------|------------|
| O(Log N)  | 10          | 0.00001 sec|
| O(sqrt N) | 32          | 0.00003 sec|
| N         | 1, 000      | 0.001 sec  |
| N^2       | 1, 000, 000 | 1 sec      |
| 2^N       | 1.07x10^301 | 3.40X10^287 years |
| N!        | 4.02X10^2567| 1.28X10^2554 years|

## P and NP
There is a philosophical question out there that asks "does P = NP"

* P - Polynomial Time (being deterministic)
* NP - Non-deterministic Polynomial Time

Consider this, if we want to find the largest value in a list we could:
* Step through each item of the list and keep track of the largest item you have seen so far. If the list contains N numbers, the algorithm will do N steps. This is an example of Polynomial Time.
* In this case our function can make an inspired guess as to which variable is the largest in our list, and then verify if that is indeed the case. THis makes it a Non-deterministic Polynomial Time Algorithm.

# Numerical Algorithms

## Random Numbers
Many algorithms seem to be able to produce random numbers from a group or list of numbers. In practice, true randomness in computing is extremely rare.
This is because computers simply follow a list of definite steps, quantum computing may deliver different solutions in this regard. 

We have different types of number generators:
* (PRNG) Pseudorandom Number Generators
* (CRNG) Cryptographic Random Number Generator
* (TRNG) True Random Number Generator

look at ww.random.org

## Linear Congruential Generators (LCGs)