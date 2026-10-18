from itertools import permutations

def transitive_closure(leq):
    n = len(leq)
    for k in range(n):
        for i in range(n):
            if leq[i][k]:
                for j in range(n):
                    if leq[k][j]:
                        leq[i][j] = True
    return leq

def chain(n):
    return [[i <= j for j in range(n)] for i in range(n)]

def covers(leq, x, y):
    if x == y or not leq[x][y]:
        return False
    n = len(leq)
    return not any(k not in (x, y) and leq[x][k] and leq[k][y] for k in range(n))

def bottom(leq):
    return next(i for i in range(len(leq)) if all(leq[i][j] for j in range(len(leq))))

def top(leq):
    return next(i for i in range(len(leq)) if all(leq[j][i] for j in range(len(leq))))

def atoms(leq):
    b = bottom(leq)
    return [j for j in range(len(leq)) if covers(leq, b, j)]

def expand(leq, generating_atom):
    n = len(leq)
    N = n + 2
    out = [[False] * N for _ in range(N)]
    for i in range(N):
        out[i][i] = True
    for i in range(n):
        for j in range(n):
            if leq[i][j]:
                out[i + 2][j + 2] = True
    old_bottom = bottom(leq) + 2
    old_atom = generating_atom + 2
    out[0][old_bottom] = True
    out[0][1] = True
    out[1][old_atom] = True
    transitive_closure(out)
    return out, old_bottom

def operations(leq):
    n = len(leq)
    meet = [[None] * n for _ in range(n)]
    join = [[None] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            lows = [z for z in range(n) if leq[z][a] and leq[z][b]]
            maxs = [z for z in lows if not any(z != w and leq[z][w] for w in lows)]
            ups = [z for z in range(n) if leq[a][z] and leq[b][z]]
            mins = [z for z in ups if not any(z != w and leq[w][z] for w in ups)]
            assert len(maxs) == 1 and len(mins) == 1
            meet[a][b] = maxs[0]
            join[a][b] = mins[0]
    imp = [[None] * n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            cand = [z for z in range(n) if leq[meet[a][z]][b]]
            maxs = [z for z in cand if not any(z != w and leq[z][w] for w in cand)]
            assert len(maxs) == 1
            imp[a][b] = maxs[0]
    return meet, join, imp

def generated_by(g, leq, meet, join, imp):
    S = {bottom(leq), top(leq), g}
    changed = True
    while changed:
        changed = False
        for a in tuple(S):
            for b in tuple(S):
                for c in (meet[a][b], join[a][b], imp[a][b]):
                    if c not in S:
                        S.add(c)
                        changed = True
    return S

def automorphisms(leq):
    n = len(leq)
    lo, hi = bottom(leq), top(leq)
    ans = []
    for p in permutations(range(n)):
        if p[lo] != lo or p[hi] != hi:
            continue
        if all(leq[i][j] == leq[p[i]][p[j]] for i in range(n) for j in range(n)):
            ans.append(p)
    return ans

Z = {2: chain(2), 3: chain(3)}
canonical_generator = {2: 0, 3: 1}

for n in range(4, 21):
    base = Z[n - 2]
    if n - 2 == 2:
        generating_atom = 1
    else:
        generating_atom = canonical_generator[n - 2]
    Z[n], canonical_generator[n] = expand(base, generating_atom)

checks = 0
for n in range(2, 21):
    leq = Z[n]
    assert len(leq) == n
    checks += 1
    meet, join, imp = operations(leq)
    gens = [g for g in range(n) if len(generated_by(g, leq, meet, join, imp)) == n]
    expected_count = 2 if n in (2, 4, 5) else 1
    assert len(gens) == expected_count
    checks += 1
    assert canonical_generator[n] in gens
    checks += 1

for n in range(2, 9):
    leq = Z[n]
    meet, join, imp = operations(leq)
    gens = [g for g in range(n) if len(generated_by(g, leq, meet, join, imp)) == n]
    autos = automorphisms(leq)
    unseen = set(gens)
    orbits = []
    while unseen:
        g = next(iter(unseen))
        orb = {p[g] for p in autos}
        orbits.append(orb)
        unseen -= orb
    expected_orbits = 2 if n == 2 else 1
    assert len(orbits) == expected_orbits
    checks += 1

print(f"VERIFY_OK {checks} exact assertions")
