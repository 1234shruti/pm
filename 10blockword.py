from collections import deque

def goal_stack_planning(initial, goal, blocks):
    # Stack contains states and corresponding action plans
    stack = [(set(initial), [])]
    visited = set()

    while stack:
        state, plan = stack.pop()
        state_key = frozenset(state)

        if all(g in state for g in goal):
            return plan

        if state_key in visited:
            continue

        visited.add(state_key)
        actions = []

        for x in blocks:
            if ("ONTABLE", x) in state and ("CLEAR", x) in state and ("ARMEMPTY",) in state:
                actions.append(("PICKUP", x))

            for y in blocks:
                if x != y and ("ON", x, y) in state and ("CLEAR", x) in state and ("ARMEMPTY",) in state:
                    actions.append(("UNSTACK", x, y))

            if ("HOLDING", x) in state:
                actions.append(("PUTDOWN", x))

                for y in blocks:
                    if x != y and ("CLEAR", y) in state:
                        actions.append(("STACK", x, y))

        # Apply operators using their preconditions and effects
        for action in actions:
            new_state = set(state)
            op = action[0]

            if op == "PICKUP":
                x = action[1]
                new_state.remove(("ONTABLE", x))
                new_state.remove(("CLEAR", x))
                new_state.remove(("ARMEMPTY",))
                new_state.add(("HOLDING", x))

            elif op == "UNSTACK":
                x, y = action[1], action[2]
                new_state.remove(("ON", x, y))
                new_state.remove(("CLEAR", x))
                new_state.remove(("ARMEMPTY",))
                new_state.add(("CLEAR", y))
                new_state.add(("HOLDING", x))

            elif op == "STACK":
                x, y = action[1], action[2]
                new_state.remove(("HOLDING", x))
                new_state.remove(("CLEAR", y))
                new_state.add(("ON", x, y))
                new_state.add(("CLEAR", x))
                new_state.add(("ARMEMPTY",))

            elif op == "PUTDOWN":
                x = action[1]
                new_state.remove(("HOLDING", x))
                new_state.add(("ONTABLE", x))
                new_state.add(("CLEAR", x))
                new_state.add(("ARMEMPTY",))

            stack.append((new_state, plan + [action]))

    return None


# Initial configuration
initial = {
    ("ON", "A", "B"),
    ("ONTABLE", "B"),
    ("ONTABLE", "C"),
    ("CLEAR", "A"),
    ("CLEAR", "C"),
    ("ARMEMPTY",)
}

# Desired goal configuration
goal = {
    ("ON", "A", "B"),
    ("ON", "B", "C")
}

blocks = {"A", "B", "C"}

plan = goal_stack_planning(initial, goal, blocks)

print("Initial State: A on B; B and C on table")
print("Goal State: A on B; B on C\n")

if plan:
    print("Actions to achieve the goal:")
    for i, action in enumerate(plan, 1):
        print(i, action)

    print("\nGoal configuration achieved!")
else:
    print("Goal cannot be achieved.")