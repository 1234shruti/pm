visited = set()

def dfs(a, b):
    if (a, b) in visited:
        return False

    visited.add((a, b))
    print((a, b))

    if a == 2:
        print("Goal reached!")
        return True

    # Fill Jug A
    if dfs(4, b):
        return True

    # Fill Jug B
    if dfs(a, 3):
        return True

    # Empty Jug A
    if dfs(0, b):
        return True

    # Empty Jug B
    if dfs(a, 0):
        return True

    # Pour Jug A into Jug B
    amount = min(a, 3 - b)
    if dfs(a - amount, b + amount):
        return True

    # Pour Jug B into Jug A
    amount = min(b, 4 - a)
    if dfs(a + amount, b - amount):
        return True

    return False


print("WATER JUG PROBLEM USING DFS")
print("Jug A = 4 litres")
print("Jug B = 3 litres")
print("Goal = 2 litres in Jug A")
print()

dfs(0, 0)