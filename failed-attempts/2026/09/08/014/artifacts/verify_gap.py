#!/usr/bin/env python3
"""Pure-Python (stdlib only) certificate for the p^4 commuting-probability gap.

Part A: exact rational arithmetic for the gap formulas (top/second-max/width).
Part B: brute-force conjugacy-class computation for explicit witnesses:
  - H3 x C3   (order 81, |Z|=9 stratum; attains top 33/81 = 11/27)
  - H3        (order 27 nonabelian, exponent 3)
  - C9 rtimes C3 (order 27 nonabelian, exponent 9)
  - Sylow3(S9) as explicit permutation group (order 81, |Z|=3 stratum)
  - D8 x C2   (order 16, p=2 analogue: top 10/16 = 5/8)
Only generic group operations (mult/identity/inverse search, class partition,
commutator-subgroup closure) are used; assertions check the theorem's instance data.
"""
import json
from fractions import Fraction
from itertools import product

LOG = []

def log(msg):
    LOG.append(msg)
    print(msg, flush=True)

# ---------------------------------------------------------------- Part A
def part_a():
    log("=== Part A: exact rational gap arithmetic ===")
    for p in [3, 5, 7, 11, 13]:
        top_num = p**3 + p**2 - p
        sec_num = p**3 + p - 1
        den = p**4
        top, sec = Fraction(top_num, den), Fraction(sec_num, den)
        width = top - sec
        assert width == Fraction((p - 1) ** 2, p**4), p
        assert Fraction(0) < sec < top < Fraction(1), p
        # character-sum identity for the top stratum: p^3 linears + (p^2-p) degree-p
        assert p**3 * 1 + (p**2 - p) * p**2 == p**4, p
        # realizability range for b from a = p^3-1-b*p >= 0
        bmax = (p**3 - 1) // p
        assert bmax == p**2 - 1, p
        log(f"p={p}: top={top} second={sec} width={width} b in [0,{bmax}] OK")
    # the p=3 forbidden numerators strictly between 29 and 33
    assert [k for k in range(0, 82) if Fraction(29, 81) < Fraction(k, 81) < Fraction(33, 81)] == [30, 31, 32]
    log("p=3: values strictly between 29/81 and 33/81 are exactly {30,31,32}/81 OK")

# ---------------------------------------------------------------- generic finite-group machinery
def build_group(elements, mult):
    """elements: list of hashables; mult: associative binary op. Returns dict of data."""
    G = list(elements)
    n = len(G)
    # identity search
    e = next(x for x in G if all(mult(x, y) == y and mult(y, x) == y for y in G))
    inv = {}
    for x in G:
        inv[x] = next(y for y in G if mult(x, y) == e and mult(y, x) == e)
    # conjugacy classes
    seen = set()
    classes = []
    for g in G:
        if g in seen:
            continue
        cl = set()
        for h in G:
            c = mult(mult(h, g), inv[h])
            cl.add(c)
        cl = frozenset(cl)
        classes.append(cl)
        seen |= set(cl)
    assert sum(len(c) for c in classes) == n
    k = len(classes)
    center = [g for g in G if any(g in c and len(c) == 1 for c in classes)]
    # commutator subgroup via closure
    comms = set()
    for g in G:
        for h in G:
            # [g,h] = g^{-1} h^{-1} g h
            comms.add(mult(mult(mult(inv[g], inv[h]), g), h))
    # closure of comms
    sub = {e}
    frontier = [e]
    while frontier:
        x = frontier.pop()
        for c in comms:
            for y in (mult(x, c), mult(c, x)):
                if y not in sub:
                    sub.add(y)
                    frontier.append(y)
    Gprime_order = len(sub)
    assert n % Gprime_order == 0
    return {
        "order": n, "k": k, "cp": Fraction(k, n),
        "center_order": len(center),
        "class_sizes": sorted(len(c) for c in classes),
        "centralizer_sizes": sorted(n // len(c) for c in classes),
        "Gprime_order": Gprime_order,
        "linears": n // Gprime_order,
    }

def report(name, d):
    log(f"{name}: |G|={d['order']} k={d['k']} cp={d['cp']} |Z|={d['center_order']} "
        f"|G'|={d['Gprime_order']} linears={d['linears']}")
    log(f"   class sizes: {d['class_sizes']}")
    return d

# ---------------------------------------------------------------- witnesses
def heis3xC3():
    E = [(a, b, c, d) for a in range(3) for b in range(3) for c in range(3) for d in range(3)]
    def mult(g, h):
        a, b, c, d = g
        x, y, z, w = h
        return ((a + x) % 3, (b + y) % 3, (c + z + a * y) % 3, (d + w) % 3)
    return E, mult

def heis3():
    E = [(a, b, c) for a in range(3) for b in range(3) for c in range(3)]
    def mult(g, h):
        a, b, c = g
        x, y, z = h
        return ((a + x) % 3, (b + y) % 3, (c + z + a * y) % 3)
    return E, mult

def C9_semi_C3():
    # C9 rtimes C3 via u -> u^4 (4 has order 3 mod 9)
    E = [(i, j) for i in range(9) for j in range(3)]
    p4 = [1, 4, 7]
    def mult(g, h):
        i, j = g
        ip, jp = h
        return ((i + p4[j] * ip) % 9, (j + jp) % 3)
    return E, mult

def sylow3_S9():
    # permutations of 0..8 as tuples; mult(p,q)[i] = p[q[i]]
    def mult(p, q):
        return tuple(p[q[i]] for i in range(9))
    a1 = (1, 2, 0, 3, 4, 5, 6, 7, 8)
    a2 = (0, 1, 2, 4, 5, 3, 6, 7, 8)
    a3 = (0, 1, 2, 3, 4, 5, 7, 8, 6)
    t = (3, 4, 5, 6, 7, 8, 0, 1, 2)
    e = tuple(range(9))
    seen = {e}
    stack = [e]
    while stack:
        x = stack.pop()
        for g in (a1, a2, a3, t):
            for y in (mult(x, g), mult(g, x)):
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
    return list(seen), mult

def D8xC2():
    def mult(p, q):
        return (tuple(p[0][q[0][i]] for i in range(4)), (p[1] + q[1]) % 2)
    r = (1, 2, 3, 0)
    s = (0, 3, 2, 1)
    e = (0, 1, 2, 3)
    perms = {e}
    stack = [e]
    pm = lambda p, q: tuple(p[q[i]] for i in range(4))
    while stack:
        x = stack.pop()
        for g in (r, s):
            for y in (pm(x, g), pm(g, x)):
                if y not in perms:
                    perms.add(y)
                    stack.append(y)
    assert len(perms) == 8, len(perms)
    E = [(p, c) for p in perms for c in (0, 1)]
    return E, mult

def part_b():
    log("=== Part B: brute-force witness groups ===")
    out = {}
    E, m = heis3xC3()
    d = report("H3xC3 (ord81)", build_group(E, m))
    assert d["order"] == 81 and d["center_order"] == 9 and d["k"] == 33
    assert d["cp"] == Fraction(33, 81) == Fraction(11, 27)
    assert all(s == 3 for s in d["class_sizes"] if s > 1)
    assert d["Gprime_order"] == 3 and d["linears"] == 27
    out["H3xC3"] = {k: str(v) if isinstance(v, Fraction) else v for k, v in d.items() if k != "class_sizes"}

    E, m = heis3()
    d = report("H3 (ord27, exp3)", build_group(E, m))
    assert d["order"] == 27 and d["center_order"] == 3 and d["k"] == 11
    out["H3"] = {k: str(v) if isinstance(v, Fraction) else v for k, v in d.items() if k != "class_sizes"}

    E, m = C9_semi_C3()
    d = report("C9rtC3 (ord27, exp9)", build_group(E, m))
    assert d["order"] == 27 and d["center_order"] == 3 and d["k"] == 11
    out["C9rtC3"] = {k: str(v) if isinstance(v, Fraction) else v for k, v in d.items() if k != "class_sizes"}

    E, m = sylow3_S9()
    d = report("Sylow3(S9) (ord81)", build_group(E, m))
    assert d["order"] == 81 and d["center_order"] == 3, d
    assert d["k"] <= 29 and d["k"] not in (30, 31, 32), d
    assert d["cp"] <= Fraction(29, 81), d
    assert (d["k"] - 29) % 2 == 0, d  # k = 29 - 2b form
    assert d["linears"] <= 9, d       # |Z|=p stratum: at most p^2 linears
    out["Sylow3S9"] = {k: str(v) if isinstance(v, Fraction) else v for k, v in d.items() if k != "class_sizes"}
    out["Sylow3S9"]["class_sizes"] = d["class_sizes"]
    log(f"   Sylow3(S9) full class-size multiset: {d['class_sizes']}")

    E, m = D8xC2()
    d = report("D8xC2 (ord16, p=2 analogue)", build_group(E, m))
    assert d["order"] == 16 and d["center_order"] == 4 and d["k"] == 10
    assert d["cp"] == Fraction(10, 16) == Fraction(5, 8)
    out["D8xC2"] = {k: str(v) if isinstance(v, Fraction) else v for k, v in d.items() if k != "class_sizes"}
    log("All brute-force assertions passed.")
    return out

if __name__ == "__main__":
    part_a()
    out = part_b()
    with open("verify_results.json", "w") as f:
        json.dump(out, f, indent=2)
    with open("verify_log.txt", "w") as f:
        f.write("\n".join(LOG) + "\n")
    log("Wrote verify_results.json and verify_log.txt")
