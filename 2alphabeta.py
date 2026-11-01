def alpha_beta(depth, index, maximizing, values, alpha, beta):
    if depth == 3:
        return values[index]

    if maximizing:
        best = -999

        for i in range(2):
            value = alpha_beta(depth + 1, index * 2 + i,
                               False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 999

        for i in range(2):
            value = alpha_beta(depth + 1, index * 2 + i,
                               True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = [3, 5, 6, 9, 1, 2, 0, -1]

result = alpha_beta(0, 0, True, values, -999, 999)

print("Optimal value:", result)