def h(state, goal):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != goal[i]:
            count += 1
    return count


def solve(start, goal):
    open_list = [(h(start, goal), start, [])]
    visited = set()

    while open_list:
        open_list.sort()
        f, state, path = open_list.pop(0)

        if state in visited:
            continue
        visited.add(state)

        path = path + [state]

        if state == goal:
            for s in path:
                print(s[0:3])
                print(s[3:6])
                print(s[6:9])
                print()
            return

        zero = state.index(0)

        for move in [-3, 3, -1, 1]:
            new = zero + move

            if 0 <= new < 9:
                if abs(move) == 1 and zero // 3 != new // 3:
                    continue

                temp = list(state)
                temp[zero], temp[new] = temp[new], temp[zero]
                temp = tuple(temp)

                if temp not in visited:
                    g = len(path)
                    f = g + h(temp, goal)
                    open_list.append((f, temp, path))

    print("No solution")


start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solve(start, goal)