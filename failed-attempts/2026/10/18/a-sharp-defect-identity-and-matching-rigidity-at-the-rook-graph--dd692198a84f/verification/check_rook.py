#!/usr/bin/env python3
"""Self-contained finite checks of the rook-graph PCF theorem.

No external libraries, internet, or previously generated data are required.
The infinite claims are established by the accompanying mathematical proof.
"""
from collections import Counter


def bad_cells(board):
    m, n = len(board), len(board[0])
    assert all(len(row) == n and len(set(row)) == n for row in board)
    assert all(len({board[i][j] for i in range(m)}) == m for j in range(n))
    bad = []
    for i in range(m):
        for j in range(n):
            neighbors = [board[i][b] for b in range(n) if b != j]
            neighbors += [board[a][j] for a in range(m) if a != i]
            if not any(t == 1 for t in Counter(neighbors).values()):
                bad.append((i, j))
            row_symbols = set(board[i])
            col_symbols = {board[a][j] for a in range(m)}
            assert ((i, j) in bad) == (row_symbols == col_symbols)
    return bad


def rectangle(m, n):
    return [[(i + j) % n for j in range(n)] for i in range(m)]


def sharp_defect(n):
    q = n + 1
    return [[(i+j) % q for j in range(1,q)] for i in range(1,q)]


def square(n):
    q = n + 2
    surviving_rows = [i for i in range(q) if i not in (0, 1)]
    surviving_cols = [j for j in range(q) if j not in (0, 2)]
    return [[(i + j) % q for j in surviving_cols] for i in surviving_rows]


def check_constructions():
    rect_count = 0
    for n in range(3, 15):
        for m in range(2, n):
            assert bad_cells(rectangle(m, n)) == []
            rect_count += 1
    for n in range(2, 17):
        assert bad_cells(sharp_defect(n)) == [(i,i) for i in range(n)]
        board = square(n)
        assert bad_cells(board) == []
        assert len({c for row in board for c in row}) == n + 2
    print("rectangular constructions:", rect_count,
          "square constructions:", 15)


def enumerate_square(n, palette_size):
    matrix = [[-1] * n for _ in range(n)]
    rows = [set() for _ in range(n)]
    cols = [set() for _ in range(n)]
    counts = [0, 0, n * n + 1]

    def visit(position):
        if position == n * n:
            counts[0] += 1
            bad = bad_cells(matrix)
            counts[1] += len(bad) == 0
            counts[2] = min(counts[2], len(bad))
            if palette_size == n + 1:
                absent_rows = [set(range(palette_size)) - set(r)
                               for r in matrix]
                absent_cols = [set(range(palette_size)) -
                               {matrix[i][j] for i in range(n)}
                               for j in range(n)]
                a = [sum(s in row for row in absent_rows)
                     for s in range(palette_size)]
                b = [sum(s in col for col in absent_cols)
                     for s in range(palette_size)]
                assert a == b
                assert len(bad) == sum(t * t for t in a)
                if len(bad) == n:
                    assert len({i for i, j in bad}) == n
                    assert len({j for i, j in bad}) == n
            return
        i, j = divmod(position, n)
        for c in range(palette_size):
            if c not in rows[i] and c not in cols[j]:
                matrix[i][j] = c
                rows[i].add(c)
                cols[j].add(c)
                visit(position + 1)
                rows[i].remove(c)
                cols[j].remove(c)
        matrix[i][j] = -1

    visit(0)
    return tuple(counts)


def check_small_exhaustive():
    known = {
        (2, 2): (2, 0, 4),
        (2, 3): (18, 0, 2),
        (2, 4): (84, 24, 0),
        (3, 3): (12, 0, 9),
        (3, 4): (1056, 0, 3),
        (3, 5): (27480, 2160, 0),
    }
    for (n, q), answer in known.items():
        actual = enumerate_square(n, q)
        assert actual == answer, ((n, q), actual, answer)
        print("exhaustive", (n, q), actual)


if __name__ == "__main__":
    check_constructions()
    check_small_exhaustive()
    print("ROOK_VERIFICATION_OK")
