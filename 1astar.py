import heapq

# Calculate Manhattan Distance
def get_manhattan_distance(state, goal):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:  # Skip the empty tile
            current_row, current_col = i // 3, i % 3

            goal_idx = goal.index(tile)
            goal_row, goal_col = goal_idx // 3, goal_idx % 3

            distance += abs(current_row - goal_row) + abs(current_col - goal_col)

    return distance


# Generate neighboring states
def get_neighbors(state):
    empty_idx = state.index(0)
    row, col = empty_idx // 3, empty_idx % 3

    neighbors = []

    moves = [
        ("Up", -1, 0),
        ("Down", 1, 0),
        ("Left", 0, -1),
        ("Right", 0, 1)
    ]

    for move, dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_empty_idx = new_row * 3 + new_col

            # Swap blank tile with adjacent tile
            new_state = list(state)

            new_state[empty_idx], new_state[new_empty_idx] = (
                new_state[new_empty_idx],
                new_state[empty_idx]
            )

            neighbors.append((move, tuple(new_state)))

    return neighbors


# A* Search Algorithm
def solve_8_puzzle(start, goal):
    start_h = get_manhattan_distance(start, goal)

    open_list = [(start_h, 0, start, [])]
    visited = set()

    while open_list:
        f, g, state, path = heapq.heappop(open_list)

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for move, new_state in get_neighbors(state):
            if new_state not in visited:
                new_g = g + 1
                new_h = get_manhattan_distance(new_state, goal)
                new_f = new_g + new_h

                heapq.heappush(
                    open_list,
                    (
                        new_f,
                        new_g,
                        new_state,
                        path + [(move, new_state)]
                    )
                )

    return None


# Print the puzzle board
def print_board(state):
    """Prints the board in a 3x3 grid."""

    for i in range(0, 9, 3):
        print(state[i:i + 3])

    print("-" * 12)


# Main program
if __name__ == "__main__":

    start = (
        1, 2, 3,
        0, 4, 6,
        7, 5, 8
    )

    goal = (
        1, 2, 3,
        4, 5, 0,
        7, 8, 6
    )

    print("Initial Board:")
    print_board(start)

    solution = solve_8_puzzle(start, goal)

    if solution:
        print(f"Solved in {len(solution)} moves!\n")

        for step, (move, state) in enumerate(solution, start=1):
            print(f"Step {step}: Move Blank '{move}'")
            print_board(state)

    else:
        print("No solution found.")