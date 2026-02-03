from collections import deque

def water_jug_bfs(cap1, cap2, target):
    visited = set()
    queue = deque()
    queue.append((0, 0, []))
    visited.add((0, 0))

    while queue:
        j1, j2, path = queue.popleft()

        if j1 == target or j2 == target:
            return path + [(j1, j2)]

        next_states = [
            (cap1, j2),
            (j1, cap2),
            (0, j2),
            (j1, 0),
            (j1 - min(j1, cap2 - j2), j2 + min(j1, cap2 - j2)),
            (j1 + min(j2, cap1 - j1), j2 - min(j2, cap1 - j1))
        ]

        for state in next_states:
            if state not in visited:
                visited.add(state)
                queue.append((state[0], state[1], path + [(j1, j2)]))

    return None


if __name__ == "__main__":
    cap1 = 4
    cap2 = 3
    target = 2

    result = water_jug_bfs(cap1, cap2, target)

    if result:
        print("Steps:")
        for step in result:
            print(step)
    else:
        print("No solution")
