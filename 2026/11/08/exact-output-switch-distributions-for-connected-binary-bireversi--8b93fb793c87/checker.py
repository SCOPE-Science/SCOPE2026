"""Independent small-state enumeration and exact all-size coefficient recurrence."""
from itertools import permutations
from math import factorial, comb


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i + j] += a * b
    return out


def component_poly(max_n):
    e = [[1]]
    c = [[]]
    for n in range(1, max_n + 1):
        en = [factorial(n) ** 2] * (n + 1)
        cn = en[:]
        for j in range(1, n):
            prod = mul(c[j], e[n - j])
            for k, v in enumerate(prod):
                cn[k] -= comb(n - 1, j - 1) * v
        assert all(v >= 0 for v in cn)
        assert cn == cn[::-1]
        e.append(en)
        c.append(cn)
    return e, c


def brute(n):
    ps = list(permutations(range(n)))
    whole = [0] * (n + 1)
    connected = [0] * (n + 1)
    tested = 0
    for a in ps:
        for b in ps:
            seen = {0}
            frontier = [0]
            while frontier:
                q = frontier.pop()
                for v in (a[q], b[q]):
                    if v not in seen:
                        seen.add(v)
                        frontier.append(v)
            conn = len(seen) == n
            for bits in range(1 << n):
                sw = [(bits >> q) & 1 for q in range(n)]
                # Independently use the defining inverse-output criterion,
                # not the invariant-subset formula used in the proof.
                valid = True
                for output in (0, 1):
                    inverse_targets = [a[q] if (output ^ sw[q]) == 0 else b[q]
                                       for q in range(n)]
                    if len(set(inverse_targets)) != n:
                        valid = False
                        break
                tested += 1
                if valid:
                    k = sum(sw)
                    whole[k] += 1
                    if conn:
                        connected[k] += 1
    return whole, connected, tested


def main():
    e, c = component_poly(9)
    tests = 0
    for n in range(1, 6):
        w, connected, count = brute(n)
        assert w == e[n], (n, w, e[n])
        assert connected == c[n], (n, connected, c[n])
        tests += count
        print(f'n={n}: examined={count}, all={w}, connected={connected}')
    for n in range(6, 10):
        print(f'n={n}: recurrence all={e[n][0]}, connected={c[n]}')
    print(f'PASS; independently checked {tests} complete binary transducer tables')


if __name__ == '__main__':
    main()
