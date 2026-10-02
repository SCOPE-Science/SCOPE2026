from itertools import product


def check_equal_window_probability():
    cases = 0
    for q in (2, 3, 4):
        for k in range(1, 5):
            for shift in range(1, k + 2):
                length = k + shift
                total = q ** length
                equal = 0
                for word in product(range(q), repeat=length):
                    if word[:k] == word[shift:shift+k]:
                        equal += 1
                assert equal * (q ** k) == total
                cases += 1
    return cases


def check_qary_bubble_endpoint_contradiction():
    cases = 0
    comparisons = 0
    for q in (3, 4):
        for L in range(3, 7):
            for rho in range(1, L):
                flank = L - rho
                for d in range(q):
                    for A in product(range(q), repeat=flank):
                        if A[-1] == d:
                            continue
                        for B in product(range(q), repeat=flank):
                            if B[0] == d:
                                continue
                            P = A + (d,) * rho + B
                            Pp = A + (d,) * (rho - 1) + B
                            long_vertices = [P[a:a+L-1] for a in range(len(P)-L+2)]
                            short_vertices = [Pp[b:b+L-1] for b in range(len(Pp)-L+2)]
                            for a, u in enumerate(long_vertices):
                                for b, v in enumerate(short_vertices):
                                    if a - b not in (0, 1):
                                        continue
                                    comparisons += 1
                                    if u == v:
                                        assert (a, b) in {
                                            (0, 0),
                                            (L-rho+1, L-rho),
                                        }
                            cases += 1
    return cases, comparisons


if __name__ == '__main__':
    c1 = check_equal_window_probability()
    c2, cmp_count = check_qary_bubble_endpoint_contradiction()
    print(f'equal-window probability cases: {c1}')
    print(f'q-ary local bubble cases: {c2}')
    print(f'offset comparisons checked: {cmp_count}')
    print('PASS')
