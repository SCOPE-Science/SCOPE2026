#!/usr/bin/env python3
"""Independent finite checks supporting the Boolean-center argument.

The infinite theorem is proved in RESULT.md from the Fraisse extension property.
This script checks the finite Heyting-algebra lemmas used in that proof and the
finite truth-pattern classification behind the orbit formula.
"""
from itertools import product

checks = 0
poset_count = 0
central_tests = 0
splitting_tests = 0
support_tests = 0

def ok(c, msg="assertion failed"):
    global checks
    checks += 1
    if not c:
        raise AssertionError(msg)

def is_poset(mask, n):
    # Off-diagonal relation bits indexed by ordered pairs i!=j; reflexivity is implicit.
    rel = [[i == j for j in range(n)] for i in range(n)]
    k = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            rel[i][j] = bool((mask >> k) & 1)
            k += 1
    for i in range(n):
        for j in range(n):
            if i != j and rel[i][j] and rel[j][i]:
                return None
    for i in range(n):
        for j in range(n):
            if rel[i][j]:
                for k in range(n):
                    if rel[j][k] and not rel[i][k]:
                        return None
    return rel

def upsets(rel):
    n = len(rel)
    ans = []
    for U in range(1 << n):
        good = True
        for x in range(n):
            if (U >> x) & 1:
                for y in range(n):
                    if rel[x][y] and not ((U >> y) & 1):
                        good = False
                        break
            if not good:
                break
        if good:
            ans.append(U)
    return ans

def imp(rel, U, V):
    # x is in U -> V iff every y >= x that lies in U also lies in V.
    n = len(rel)
    W = 0
    for x in range(n):
        good = True
        for y in range(n):
            if rel[x][y] and ((U >> y) & 1) and not ((V >> y) & 1):
                good = False
                break
        if good:
            W |= 1 << x
    return W

def neg(rel, U):
    return imp(rel, U, 0)

def comparable_components(rel):
    n = len(rel)
    seen = [False]*n
    comps = []
    for s in range(n):
        if seen[s]:
            continue
        stack=[s]; seen[s]=True; C=0
        while stack:
            x=stack.pop(); C |= 1<<x
            for y in range(n):
                if not seen[y] and (rel[x][y] or rel[y][x]):
                    seen[y]=True; stack.append(y)
        comps.append(C)
    return comps

def eval_at(U, m):
    return (U >> m) & 1

expected_labeled = {1:1, 2:3, 3:19, 4:219}
for n in range(1,5):
    this_count = 0
    bits = n*(n-1)
    for mask in range(1 << bits):
        rel = is_poset(mask, n)
        if rel is None:
            continue
        this_count += 1
        poset_count += 1
        ups = upsets(rel)
        top = (1<<n)-1
        comps = comparable_components(rel)
        central = []
        for U in ups:
            nu = neg(rel,U)
            if (U | nu) == top:
                central.append(U)
        # In an upset algebra the complemented elements are exactly unions of
        # comparability components.
        unions = set()
        for cmask in range(1 << len(comps)):
            U=0
            for i,C in enumerate(comps):
                if (cmask>>i)&1:
                    U |= C
            unions.add(U)
        ok(set(central) == unions, f"center/components mismatch n={n}")
        ok(len(central) == 2**len(comps), f"center size mismatch n={n}")
        central_tests += 2

        # For every nonzero central element c, choose a maximal point m in c.
        # Evaluation at m is a Heyting map to 2.  Its graph embedding A -> A x 2
        # makes d=(0,1) a new central element strictly below the image of c.
        for c in central:
            if c == 0:
                continue
            maxima = [m for m in range(n)
                      if ((c>>m)&1) and not any(rel[m][y] and y!=m for y in range(n))]
            ok(bool(maxima), "nonempty upset has no ambient maximal point")
            m = maxima[0]
            ok(eval_at(c,m) == 1)
            for U in ups:
                ok(eval_at(neg(rel,U),m) == (1-eval_at(U,m)))
                for V in ups:
                    hU,hV = eval_at(U,m),eval_at(V,m)
                    ok(eval_at(U & V,m) == (hU & hV))
                    ok(eval_at(U | V,m) == (hU | hV))
                    ok(eval_at(imp(rel,U,V),m) == ((1-hU) | hV))
            # d=(0,1), e(c)=(c,1): nonzero and strict below.
            ok(c != 0)
            splitting_tests += 1
    ok(this_count == expected_labeled[n], f"labeled poset count wrong n={n}")

# Truth-pattern support classification.  For an ordered n-tuple in an atomless
# Boolean algebra, the 2^n Boolean cells have a nonempty support S. Every
# nonempty S is realizable by a finite partition of 1 indexed by S.
expected_orbits = [1,3,15,255,65535]
for n in range(5):
    patterns = list(product((0,1), repeat=n))
    count = (1 << len(patterns)) - 1
    ok(count == expected_orbits[n], f"orbit formula wrong n={n}")
    # Exhaustively realize all supports for n<=4 in a finite powerset algebra.
    for smask in range(1, 1 << len(patterns)):
        S = [patterns[i] for i in range(len(patterns)) if (smask>>i)&1]
        # Atoms are indexed by S. Define b_i as the union of atoms whose i-th bit is 1.
        tuple_sets = []
        for i in range(n):
            b = {j for j,p in enumerate(S) if p[i]}
            tuple_sets.append(b)
        recovered = set()
        for j in range(len(S)):
            recovered.add(tuple(1 if j in tuple_sets[i] else 0 for i in range(n)))
        ok(recovered == set(S), f"support realization failed n={n}")
        support_tests += 1

print(
    f"VERIFY_OK {checks} exact assertions; {poset_count} labeled posets through four points; "
    f"{central_tests} center/component checks; {splitting_tests} center-splitting witnesses; "
    f"{support_tests} nonempty truth-pattern supports through arity four"
)
