"""Stand-alone exact enumeration of linear isometries of a fused-lasso norm.
Only finite-dimensional test instances; the general classification needs the proof.
"""
from itertools import permutations, product


def count_isometries(n, a, b):
    assert n >= 1 and a > 0 and b > 0
    forms = []
    for i in range(n):
        row = [0] * n
        row[i] = a
        forms.append(tuple(row))
    for i in range(n - 1):
        row = [0] * n
        row[i] = b
        row[i + 1] = -b
        forms.append(tuple(row))
    allowed = {tuple(v) for v in forms} | {tuple(-x for x in v) for v in forms}
    ans = set()
    for image_ids in permutations(range(len(forms)), n):
        if n > 1:
            for signs in product((-1, 1), repeat=n):
                rows_scaled = [tuple(signs[i] * t for t in forms[j]) for i, j in enumerate(image_ids)]
                # A^T(a e_i) are rows_scaled[i]. Check images of b(e_i-e_{i+1})
                # in integers by multiplying both sides by a.
                used = set(image_ids)
                valid = True
                for i in range(n - 1):
                    difference = tuple(b*(rows_scaled[i][k]-rows_scaled[i+1][k]) for k in range(n))
                    choices = [j for j, w in enumerate(forms) if difference == tuple(a*t for t in w) or difference == tuple(-a*t for t in w)]
                    if len(choices) != 1 or choices[0] in used:
                        valid = False
                        break
                    used.add(choices[0])
                if valid and len(used) == len(forms):
                    ans.add(tuple(rows_scaled))
        else:
            for s in (-1,1):
                ans.add((tuple(s*t for t in forms[image_ids[0]]),))
    return len(ans)


def main():
    for n in (1, 2, 3, 4):
        for (a, b) in ((1, 1), (1, 2), (2, 1)):
            actual = count_isometries(n, a, b)
            predicted = 2 if n == 1 else (12 if n == 2 else 16) if a == b else 4
            assert actual == predicted, (n, a, b, actual, predicted)
            print(f'n={n} a={a} b={b}: {actual} isometries, predicted {predicted}')
    # Verifies one larger balanced path (9 potential kink terms).
    actual = count_isometries(5, 1, 1)
    assert actual == 16, actual
    print(f'n=5 a=1 b=1: {actual} isometries, predicted 16')
    print('PASS: 13 exact enumeration cases')


if __name__ == '__main__':
    main()
