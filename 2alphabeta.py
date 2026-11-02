

def alpha_beta(node, depth, alpha, beta, maximizing_player):

    # Base condition
    if depth == 0 or isinstance(node, int):
        return node

    if maximizing_player:

        best_value = float('-inf')

        print("\nMAX Node")
        print("Alpha =", alpha, "Beta =", beta)

        for child in node:

            value = alpha_beta(
                child,
                depth - 1,
                alpha,
                beta,
                False
            )

            best_value = max(best_value, value)
            alpha = max(alpha, best_value)

            print(
                "MAX updated:",
                "Value =", best_value,
                "Alpha =", alpha,
                "Beta =", beta
            )

            if alpha >= beta:
                print(">>> BETA CUTOFF: Branch pruned")
                break

        return best_value

    else:

        best_value = float('inf')

        print("\nMIN Node")
        print("Alpha =", alpha, "Beta =", beta)

        for child in node:

            value = alpha_beta(
                child,
                depth - 1,
                alpha,
                beta,
                True
            )

            best_value = min(best_value, value)
            beta = min(beta, best_value)

            print(
                "MIN updated:",
                "Value =", best_value,
                "Alpha =", alpha,
                "Beta =", beta
            )

            if alpha >= beta:
                print(">>> ALPHA CUTOFF: Branch pruned")
                break

        return best_value


# Game Tree
game_tree = [
    [
        [3, 5],
        [6, 9]
    ],
    [
        [1, 2],
        [0, 4]
    ]
]


# Main Program
result = alpha_beta(
    game_tree,
    depth=3,
    alpha=float('-inf'),
    beta=float('inf'),
    maximizing_player=True
)

print("\n================================")
print("Optimal Game Value:", result)
print("================================")