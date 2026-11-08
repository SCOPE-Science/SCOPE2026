"""Exact finite check for repeated expected-phylogenetic-diversity crossings.

Python 3 standard library only. Trees are unordered rooted full binary shapes;
every edge has unit length and every leaf independently dies with probability q.
"""
from functools import lru_cache
from fractions import Fraction
from math import gcd
from itertools import combinations

@lru_cache(None)
def shapes(n):
    if n == 1:
        return ("a",)
    result = set()
    for i in range(1, n // 2 + 1):
        for left in shapes(i):
            for right in shapes(n - i):
                if i == n - i and left > right:
                    continue
                result.add("(" + left + "," + right + ")")
    return tuple(sorted(result))

def parse(s):
    if s == "a":
        return "a"
    assert s[0] == "(" and s[-1] == ")"
    dep = 0
    for pos in range(1, len(s) - 1):
        char = s[pos]
        if char == "(":
            dep += 1
        elif char == ")":
            dep -= 1
        elif char == "," and dep == 0:
            return parse(s[1:pos]), parse(s[pos + 1:-1])
    raise ValueError(s)

def profile(t):
    """All nonroot clade sizes: index k is the number of k-leaf edges."""
    sizes = []
    def rec(node):
        if node == "a":
            return 1
        a = rec(node[0]); b = rec(node[1])
        sizes.extend((a, b))
        return a + b
    n = rec(t)
    assert len(sizes) == 2 * n - 2
    out = [0] * (n + 1)
    for k in sizes:
        out[k] += 1
    return tuple(out)

def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a

def pval(a, x):
    value = 0
    for c in reversed(a):
        value = value * x + c
    return value

def div_by_xminus1(a):
    assert sum(a) == 0 and len(a) > 1
    out = [0] * (len(a) - 1)
    out[-1] = a[-1]
    for i in range(len(out) - 2, -1, -1):
        out[i] = a[i + 1] + out[i + 1]
    return trim(out)

def remainder(a, b):
    r = trim([Fraction(c) for c in a]); b = trim([Fraction(c) for c in b])
    assert b[-1] != 0
    while len(r) >= len(b) and any(r):
        x = r[-1] / b[-1]
        k = len(r) - len(b)
        for j in range(len(b)):
            r[j + k] -= x * b[j]
        r = trim(r)
        if r == [0]:
            break
    return r

def primitive_positive_scale(a):
    """Clear denominators and common factors by a strictly positive scale."""
    from math import lcm
    den = 1
    for x in a:
        den = lcm(den, Fraction(x).denominator)
    vals = [int(Fraction(x) * den) for x in a]
    d = 0
    for x in vals:
        d = gcd(d, abs(x))
    return trim([v // d for v in vals]) if d else [0]

def count_roots_0_1(p):
    p = trim(p)
    if p == [0]:
        raise ValueError("identical polynomials")
    while len(p) > 1 and p[0] == 0:
        p = trim(p[1:])
    while len(p) > 1 and sum(p) == 0:
        p = div_by_xminus1(p)
    if len(p) < 2:
        return 0
    seq = [p, trim([i * p[i] for i in range(1, len(p))])]
    while seq[-1] != [0]:
        r = remainder(seq[-2], seq[-1])
        if r == [0]:
            break
        seq.append(primitive_positive_scale([-x for x in r]))
    def variations(x):
        values = [pval(a,x) for a in seq]
        signs = [1 if v > 0 else -1 for v in values if v]
        return sum(signs[i] != signs[i - 1] for i in range(1, len(signs)))
    return variations(0) - variations(1)

def expected_direct(s, death):
    tree = parse(s)
    clades = []
    def visit(node, next_index):
        if node == "a":
            return 1 << next_index, next_index + 1
        a, ni = visit(node[0], next_index)
        b, nj = visit(node[1], ni)
        clades.extend((a, b))
        return a | b, nj
    _, n = visit(tree, 0)
    assert n == 11 and len(clades) == 20
    survived = 1 - death
    out = Fraction(0)
    for mask in range(1 << n):
        k = mask.bit_count()
        score = sum(bool(mask & clade) for clade in clades)
        out += score * survived ** k * death ** (n - k)
    return out

TREE_A = "((a,((a,a),(a,a))),((a,a),((a,a),(a,a))))"
TREE_B = "((a,(a,a)),((a,(a,a)),((a,a),(a,(a,a)))))"

if __name__ == "__main__":
    assert profile(parse(TREE_A))[1:11] == (11,5,0,2,1,1,0,0,0,0)
    assert profile(parse(TREE_B))[1:11] == (11,4,3,0,1,0,0,1,0,0)
    expected_shapes = {2:1,3:1,4:2,5:3,6:6,7:11,8:23,9:46,10:98,11:207}
    expected_profiles = {2:1,3:1,4:2,5:3,6:6,7:11,8:23,9:45,10:95,11:194}
    expected_counts = {2:(0,0,0),3:(0,0,0),4:(1,0,0),5:(3,0,0),6:(15,0,0),7:(53,2,0),8:(232,21,0),9:(877,113,0),10:(3787,678,0),11:(15400,3306,15)}
    for n in range(2,12):
        trees=shapes(n)
        ps=sorted(set(profile(parse(s)) for s in trees))
        assert len(trees)==expected_shapes[n], (n,len(trees))
        assert len(ps)==expected_profiles[n], (n,len(ps))
        roots = [0,0,0]
        for i in range(len(ps)):
            for j in range(i):
                diff = [x-y for x,y in zip(ps[i],ps[j])]
                k=count_roots_0_1(diff)
                assert k in (0,1,2), (n,k,diff)
                roots[k]+=1
        assert tuple(roots)==expected_counts[n], (n,roots,expected_counts[n])
        print("n=%d shapes=%d profiles=%d root_counts=%s" % (n,len(trees),len(ps),roots))
    pa=profile(parse(TREE_A));pb=profile(parse(TREE_B))
    difference=[b-a for a,b in zip(pa,pb)] # E_A - E_B
    assert difference[2:9] == [-1,3,-2,0,-1,0,1]
    for q in (Fraction(1,2),Fraction(2,3),Fraction(3,4)):
        pd=expected_direct(TREE_A,q)-expected_direct(TREE_B,q)
        polynomial=pval(difference,q)
        factored= -q*q*(1-q)*(q*q+q-1)*(q**3+q-1)
        assert pd==polynomial==factored, (q,pd,polynomial,factored)
        print("death=%s expectation_gap=%s" % (q,pd))
    print("ALL_EXACT_CHECKS_PASSED")
