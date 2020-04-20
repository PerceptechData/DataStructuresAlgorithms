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