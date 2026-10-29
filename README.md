Search Algorithms

Breadth-First Search (BFS)

• Strategy: Explores the graph level by level (FIFO queue).
• Algorithm:
	1. Initialize a queue with the start node and a visited set containing start.
	2. While the queue is not empty:
		• Pop the front node current.
		• If current is the goal, return the path.
		• For each unvisited neighbor of current, mark it as visited, record its parent, and push it to the queue.
	3. If the queue empties without finding the goal, return None.

Depth-First Search (DFS)

• Strategy: Explores as deep as possible along each branch before backtracking (LIFO stack).
• Algorithm:
	1. Initialize a stack with the start node and a visited set.
	2. While the stack is not empty:
		• Pop the top node current.
		• If current is the goal, return the path.
		• If current is not visited, mark it as visited.
		• For each unvisited neighbor of current, push it to the stack.
	3. If the stack empties without finding the goal, return None


Depth-Limited Search (DLS)

• Strategy: DFS with a preset maximum depth limit l to prevent infinite loops.
• Algorithm:
	1. Call recursive_dls(node, goal, limit, visited).
	2. If node == goal, return the path.
	3. If limit == 0, return None (cutoff).
	4. For each neighbor of node:
		• Recursively call dls(neighbor, goal, limit - 1).
		• If a solution is found, return it.
	5. Return None if no path is found within the limit


Iterative Deepening Search (IDS / IDDFS)

• Strategy: Repeatedly runs DLS with increasing depth limits (limit = 0, 1, 2, ...).
**• Algorithm:**
	1. Set depth = 0.
	2. Loop indefinitely:
		• Run DLS(start, goal, limit=depth).
		• If a solution is found, return it.
		• Increment depth by 1.

### Uniform Cost Search (UCS)

• Strategy: Expands the node with the lowest cumulative path cost first (Priority Queue).
• Algorithm:
	1. Initialize a priority queue (min-heap) with (0, start, [start]).
	2. Initialize a visited set.
	3. While the priority queue is not empty:
		• Pop the node with the minimum cumulative cost and its path.
		• If current is the goal, return path and cost.
		• If current is already visited, skip it.
		• Mark current as visited.
		• For each neighbor with weight from current:
			• If neighbor is not visited, push (cost + weight, neighbor, path + [neighbor]) to the priority queue.
	4. Return None if the queue empties.


# Artificial Intelligence: Uninformed Search Algorithms

An implementation and comparative analysis of classic uninformed search algorithms in Python. This project was developed as part of an academic assignment to explore how different state-space search strategies traverse graphs and find paths.

---

## 🚀 Implemented Search Algorithms & Strategies

### 1. Breadth-First Search (BFS)
* **Strategy:** Explores the graph level by level (FIFO queue). Guaranteed to find the shortest path in terms of edge count.
* **Algorithm:**
  1. Initialize a queue with the start node and a visited set containing start.
  2. While the queue is not empty:
     * Pop the front node `current`.
     * If `current` is the goal, return the path.
     * For each unvisited neighbor of `current`, mark it as visited, record its parent, and push it to the queue.
  3. If the queue empties without finding the goal, return `None`.

### 2. Depth-First Search (DFS)
* **Strategy:** Explores as deep as possible along each branch before backtracking (LIFO stack).
* **Algorithm:**
  1. Initialize a stack with the start node and a visited set.
  2. While the stack is not empty:
     * Pop the top node `current`.
     * If `current` is the goal, return the path.
     * If `current` is not visited, mark it as visited.
     * For each unvisited neighbor of `current`, push it to the stack.
  3. If the stack empties without finding the goal, return `None`.

### 3. Depth-Limited Search (DLS)
* **Strategy:** DFS with a preset maximum depth limit $l$ to prevent infinite loops in deep or cyclic graphs.
* **Algorithm:**
  1. Call `recursive_dls(node, goal, limit, visited)`.
  2. If `node == goal`, return the path.
  3. If `limit == 0`, return `None` (cutoff).
  4. For each neighbor of `node`:
     * Recursively call `dls(neighbor, goal, limit - 1)`.
     * If a solution is found, return it.
  5. Return `None` if no path is found within the limit.

### 4. Iterative Deepening Search (IDS )
* **Strategy:** Repeatedly runs DLS with increasing depth limits ($\text{limit} = 0, 1, 2, \dots$). Combines the space efficiency of DFS with the optimality of BFS.
* **Algorithm:**
  1. Set $\text{depth} = 0$.
  2. Loop indefinitely:
     * Run `DLS(start, goal, limit=depth)`.
     * If a solution is found, return it.
     * Increment depth by 1.

### 5. Uniform Cost Search (UCS)
* **Strategy:** Explores nodes with the lowest cumulative path cost first (Priority Queue / Min-Heap). Guaranteed to find the optimal path in weighted graphs.
* **Algorithm:**
  1. Initialize a priority queue (min-heap) with `(0, start, [start])`.
  2. Initialize a visited set.
  3. While the priority queue is not empty:
     * Pop the node with the minimum cumulative cost and its path.
     * If `current` is the goal, return path and cost.
     * If `current` is already visited, skip it.
     * Mark `current` as visited.
     * For each neighbor with weight from `current`:
       * If neighbor is not visited, push `(cost + weight, neighbor, path + [neighbor])` to the priority queue.
  4. Return `None` if the queue empties.