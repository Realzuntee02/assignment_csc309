from collections import deque
import heapq

# Uniform Branching Factor Binary Tree (Nodes N1 to N15)
# Unweighted adjacency list for BFS, DFS, DLS, IDS
unweighted_graph = {
    'N1': ['N2', 'N3'],
    'N2': ['N4', 'N5'],
    'N3': ['N6', 'N7'],
    'N4': ['N8', 'N9'],
    'N5': ['N10', 'N11'],
    'N6': ['N12', 'N13'],
    'N7': ['N14', 'N15'],
    'N8': [],
    'N9': [],
    'N10': [],
    'N11': [],
    'N12': [],
    'N13': [],
    'N14': [],
    'N15': [],
}

# Weighted graph representation with edge weights for UCS
weighted_graph = {
    'N1': [('N2', 1), ('N3', 4)],
    'N2': [('N4', 2), ('N5', 1)],
    'N3': [('N6', 5), ('N7', 1)],
    'N4': [('N8', 1), ('N9', 3)],
    'N5': [('N10', 2), ('N11', 1)],
    'N6': [('N12', 1), ('N13', 2)],
    'N7': [('N14', 3), ('N15', 1)],
    'N8': [],
    'N9': [],
    'N10': [],
    'N11': [],
    'N12': [],
    'N13': [],
    'N14': [],
    'N15': [],
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
def ids(graph, start, goal, max_depth=5):
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
    start_node = 'N1'
    goal_node = 'N15'

    print('=== Uniform Branching Factor (b=2) Tree Search ===')
    print('BFS Path:', bfs(unweighted_graph, start_node, goal_node))
    print('DFS Path:', dfs(unweighted_graph, start_node, goal_node))
    print('DLS Path (limit=3):', dls(unweighted_graph, start_node, goal_node, 3))
    print('IDS Path:', ids(unweighted_graph, start_node, goal_node, max_depth=4))

    path, cost = ucs(weighted_graph, start_node, goal_node)
    print(f'UCS Path: {path} with total cost: {cost}')