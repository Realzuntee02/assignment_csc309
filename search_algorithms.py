from collections import deque
import heapq


# Sample graph representation:
# Adjacency list with edge weights: {node: [(neighbor, weight), ...]}
# For unweighted searches (BFS, DFS, DLS, IDS), weights can be ignored or treated as 1.
weighted_graph = {
    'S': [('A', 1), ('B', 5)],
    'A': [('C', 2)],
    'B': [('D', 1), ('E', 2)],
    'C': [('F', 3)],
    'D': [('G', 5)],
    'E': [('G', 1)],
    'F': [('G', 1)],
    'G': [],
}

# Unweighted adjacency list for BFS, DFS, DLS, IDS
unweighted_graph = {
    'S': ['A', 'B'],
    'A': ['C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': ['G'],
    'F': ['G'],
    'G': [],
}


# 1. Breadth-First Search (BFS)
def bfs(graph, start, goal):
  queue = deque([[start]])
  visited = set([start])

  while queue:
    path = queue.popleft()
    node = path[-1]

    if node == goal:
      return path

    for neighbor in graph.get(node, []):
      if neighbor not in visited:
        visited.add(neighbor)
        new_path = list(path)
        new_path.append(neighbor)
        queue.append(new_path)
  return None


# 2. Depth-First Search (DFS)
def dfs(graph, start, goal):
  stack = [[start]]
  visited = set()

  while stack:
    path = stack.pop()
    node = path[-1]

    if node == goal:
      return path

    if node not in visited:
      visited.add(node)
      for neighbor in reversed(graph.get(node, [])):
        if neighbor not in visited:
          new_path = list(path)
          new_path.append(neighbor)
          stack.append(new_path)
  return None


# 3. Depth-Limited Search (DLS)
def dls(graph, node, goal, limit, path=None):
  if path is None:
    path = [node]

  if node == goal:
    return path

  if limit <= 0:
    return None

  for neighbor in graph.get(node, []):
    if neighbor not in path:
      result = dls(graph, neighbor, goal, limit - 1, path + [neighbor])
      if result is not None:
        return result
  return None


# 4. Iterative Deepening Search (IDS / IDDFS)
def ids(graph, start, goal, max_depth=10):
  for depth in range(max_depth + 1):
    result = dls(graph, start, goal, depth)
    if result is not None:
      return result
  return None


# 5. Uniform Cost Search (UCS)
def ucs(graph, start, goal):
  # Priority queue stores tuples: (cumulative_cost, path)
  pq = [(0, [start])]
  visited = set()

  while pq:
    cost, path = heapq.heappop(pq)
    node = path[-1]

    if node == goal:
      return path, cost

    if node in visited:
      continue

    visited.add(node)

    for neighbor, weight in graph.get(node, []):
      if neighbor not in visited:
        heapq.heappush(pq, (cost + weight, path + [neighbor]))
  return None, float('inf')


# --- Testing the implementation ---
if __name__ == '__main__':
  start_node = 'S'
  goal_node = 'G'

  print('BFS Path:', bfs(unweighted_graph, start_node, goal_node))
  print('DFS Path:', dfs(unweighted_graph, start_node, goal_node))
  print('DLS Path (limit=2):', dls(unweighted_graph, start_node, goal_node, 2))
  print('IDS Path:', ids(unweighted_graph, start_node, goal_node, max_depth=4))

  path, cost = ucs(weighted_graph, start_node, goal_node)
  print(f'UCS Path: {path} with total cost: {cost}')
