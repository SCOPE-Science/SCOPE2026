from fractions import Fraction
import heapq
import math


def stirling2(n, k):
    row = [0] * (k + 1)
    row[0] = 1
    for r in range(1, n + 1):
        nxt = [0] * (k + 1)
        for j in range(1, min(r, k) + 1):
            nxt[j] = row[j - 1] + j * row[j]
        row = nxt
    return row[k]


def bernoulli_number(m):
    a = [Fraction(0) for _ in range(m + 1)]
    for q in range(m + 1):
        a[q] = Fraction(1, q + 1)
        for j in range(q, 0, -1):
            a[j - 1] = j * (a[j - 1] - a[j])
    return -a[0] if m == 1 else a[0]


def universal_cbar(n, k):
    s = stirling2(k + n, n - 1)
    term = Fraction(
        math.factorial(k + 1) * math.factorial(n - 2) * s,
        math.factorial(k + n - 1),
    )
    return Fraction((-1) ** (k + 1), k * (k + 1)) * (
        bernoulli_number(k + 1) - term
    )


def jefferson_statistics(p, samples=200000):
    n = len(p)
    counts = [0] * n
    # Highest averages: the next quotient for bin i is p_i/(m_i+1).
    heap = [(-p[i], i, 1) for i in range(n)]
    heapq.heapify(heap)
    s1 = s2 = s11 = 0.0
    for N in range(1, samples + 1):
        _, i, k = heapq.heappop(heap)
        counts[i] += 1
        heapq.heappush(heap, (-p[i] / (k + 1), i, k + 1))
        t = [counts[j] - N * p[j] for j in range(n)]
        c1 = (1.0 - sum(1.0 / x for x in p)) / 12.0
        c1 -= sum((u * u + u) / (2.0 * x) for u, x in zip(t, p))
        # B_3(y)=y^3-(3/2)y^2+(1/2)y and c_2=(1/6) sum p_i^-2 B_3(t_i+1).
        c2 = sum(
            ((u + 1.0) ** 3 - 1.5 * (u + 1.0) ** 2 + 0.5 * (u + 1.0))
            / (6.0 * x * x)
            for u, x in zip(t, p)
        )
        s1 += c1
        s11 += c1 * c1
        s2 += c2
    mean1 = s1 / samples
    mean2 = s2 / samples
    var1 = s11 / samples - mean1 * mean1
    return mean1, mean2, var1


def c1_variance_formula(p):
    n = len(p)
    H = sum(1.0 / x for x in p)
    return (
        (n - 1) * (n + 4) / 288.0
        + (H - n * n) / 144.0
        + sum((1.0 - x) ** 3 / (x * x) for x in p) / 720.0
    )


if __name__ == "__main__":
    for n in range(2, 6):
        vals = [universal_cbar(n, k) for k in range(1, 5)]
        print(f"n={n} universal cbar k=1..4: {vals}")

    p = [math.sqrt(2.0) / 4.0, math.pi / 12.0]
    p.append(1.0 - sum(p))
    mean1, mean2, var1 = jefferson_statistics(p)
    print("p =", p)
    print("empirical mean c1 =", mean1)
    print("theory mean c1    =", float(universal_cbar(3, 1)))
    print("empirical mean c2 =", mean2)
    print("theory mean c2    =", float(universal_cbar(3, 2)))
    print("empirical var c1  =", var1)
    print("theory var c1     =", c1_variance_formula(p))
