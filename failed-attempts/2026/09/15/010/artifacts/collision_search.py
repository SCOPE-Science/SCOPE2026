"""Bounded recovery test for the target claim (diagonal-pencil fiber multiplicities).

Target context: for Phi=(f,g) split, P=(a,b), and the pencil of curves x-y=c,
  |O_Phi(P) cap C_c| = multiplicity of c in d_n = f^n(a) - g^n(b).
Unboundedness (the target's existence horn) requires >=k-fold collisions for all k.
This script checks exact integer orbits of disintegrated polynomials for such
collisions and for eventual strict growth (which forces a uniform fiber bound).

Run: python3 collision_search.py  (stdlib only)
"""
from collections import Counter


def orbit(f, a, n):
    xs = [a]
    for _ in range(n):
        xs.append(f(xs[-1]))
    return xs


def fiber_report(name, f, g, a, b, n=12):
    X, Y = orbit(f, a, n), orbit(g, b, n)
    d = [x - y for x, y in zip(X, Y)]
    mc = max(Counter(d).values())
    ad = [abs(v) for v in d]
    tail_strict = all(ad[i + 1] > ad[i] for i in range(5, len(ad) - 1))
    print(f"{name}: maxfiber={mc} tailstrict(5:)={tail_strict} "
          f"max|d| bitlen={ad[-1].bit_length()}")
    return mc


def main():
    print("TEST A: fiber multiplicities (need >=3 in one fiber for unboundedness route)")
    tests = [
        ("f=g=x^2+1,a=0,b=2", lambda x: x * x + 1, lambda x: x * x + 1, 0, 2),
        ("f=g=x^2+1,a=0,b=3", lambda x: x * x + 1, lambda x: x * x + 1, 0, 3),
        ("f=g=x^2-3,a=0,b=1", lambda x: x * x - 3, lambda x: x * x - 3, 0, 1),
        ("f=g=x^2-3,a=0,b=2", lambda x: x * x - 3, lambda x: x * x - 3, 0, 2),
        ("f=g=x^2-7,a=1,b=2", lambda x: x * x - 7, lambda x: x * x - 7, 1, 2),
        ("f=x^2+1,g=x^2+2,a=0,b=0", lambda x: x * x + 1, lambda x: x * x + 2, 0, 0),
        ("f=x^2+1,g=x^2-3,a=1,b=0", lambda x: x * x + 1, lambda x: x * x - 3, 1, 0),
        ("f=g=x^3+x+1,a=0,b=1", lambda x: x**3 + x + 1, lambda x: x**3 + x + 1, 0, 1),
        ("f=g=x^2+x+3,a=0,b=5", lambda x: x * x + x + 3, lambda x: x * x + x + 3, 0, 5),
        ("f=g=2x^2+x,a=1,b=2", lambda x: 2 * x * x + x, lambda x: 2 * x * x + x, 1, 2),
    ]
    for name, f, g, a, b in tests:
        fiber_report(name, f, g, a, b)

    print()
    print("TEST B: growth ratios |d_{n+1}|/|d_n| for f=g=x^2+1,a=0,b=2")
    f = g = lambda x: x * x + 1
    X, Y = orbit(f, 0, 10), orbit(g, 2, 10)
    d = [X[i] - Y[i] for i in range(11)]
    for i in range(1, 11):
        print(i, abs(d[i]) / abs(d[i - 1]) if d[i - 1] != 0 else None)

    print()
    print("TEST C: 62-pair grid over disintegrated quadratics (triple-collision hunt)")
    grid_a = [0, 1, 2, 3, 5]
    grid_b = [0, 1, 2, 4, 7]
    polys = {"x^2+1": lambda x: x * x + 1, "x^2-3": lambda x: x * x - 3,
             "x^2-7": lambda x: x * x - 7, "x^2+x+3": lambda x: x * x + x + 3}
    n = 14
    rows = []
    for pname, f in polys.items():
        for a in grid_a:
            for b in grid_b:
                if a == b:
                    continue
                X, Y = orbit(f, a, n), orbit(f, b, n)
                if len(set(X)) < n + 1 or len(set(Y)) < n + 1:
                    continue  # preperiodic coordinate: outside target hypotheses
                d = [x - y for x, y in zip(X, Y)]
                if d[-1] == 0 and d[-2] == 0:
                    continue  # merged orbits: diagonal fiber infinite, excluded by hypotheses
                mc = max(Counter(d).values())
                ad = [abs(v) for v in d]
                onset = next((i for i in range(len(ad) - 1)
                              if all(ad[j + 1] > ad[j] for j in range(i, len(ad) - 1))), None)
                rows.append((pname, a, b, mc, onset))
    triple = [r for r in rows if r[3] >= 3]
    print(f"pairs tested: {len(rows)}, pairs with >=3-fold collision: {len(triple)}")
    for r in triple:
        print(r)
    print("max maxfiber over grid:", max(r[3] for r in rows))
    print("monotonicity-onset distribution:", Counter(r[4] for r in rows))


if __name__ == "__main__":
    main()
