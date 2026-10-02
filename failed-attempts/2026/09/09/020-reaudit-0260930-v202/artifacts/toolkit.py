"""Core finite-group machinery: mult tables as numpy int arrays."""
import numpy as np
import itertools

def find_identity(T):
    n = T.shape[0]
    for e in range(n):
        if np.all(T[e, :] == np.arange(n)) and np.all(T[:, e] == np.arange(n)):
            return e
    raise ValueError("no identity")

def inverses(T, e):
    n = T.shape[0]
    inv = np.full(n, -1)
    for a in range(n):
        c = np.where((T[a, :] == e))[0]
        # need also T[:,a]; but in group right inverse = left inverse
        for b in c:
            if T[b, a] == e:
                inv[a] = b
                break
        assert inv[a] >= 0, "not a group"
    return inv

def el_orders(T, e, inv):
    n = T.shape[0]
    ords = np.ones(n, dtype=int)
    for a in range(n):
        x = a
        k = 1
        while x != e:
            x = T[x, a]
            k += 1
            assert k <= n
        ords[a] = k
    return ords

def center(T, e):
    n = T.shape[0]
    z = [a for a in range(n)
         if np.all(T[a, :] == T[:, a][np.argsort(np.arange(n))]) and True]
    # direct check
    out = []
    for a in range(n):
        ok = True
        for b in range(n):
            if T[a, b] != T[b, a]:
                ok = False
                break
        if ok:
            out.append(a)
    return np.array(out, dtype=int)

def subgroup_generated(T, e, inv, gens):
    seen = {e}
    stack = [e] + list(gens)
    seen.update(gens)
    while stack:
        a = stack.pop()
        for b in list(seen):
            for c in (T[a, b], T[b, a], int(inv[a])):
                if c not in seen:
                    seen.add(c)
                    stack.append(c)
    return np.array(sorted(seen), dtype=int)

def commutator_subgroup(T, e, inv):
    n = T.shape[0]
    comms = set()
    for a in range(n):
        for b in range(n):
            ab = T[a, b]; ba = T[b, a]
            # [a,b] = a^-1 b^-1 a b
            v = T[T[T[int(inv[a]), int(inv[b])], a], b]
            comms.add(int(v))
    return subgroup_generated(T, e, inv, list(comms))

def normal_closure(T, e, inv, gens):
    n = T.shape[0]
    S = set(gens) | {e}
    # close under conjugation then subgroup
    changed = True
    cur = set(S)
    while changed:
        changed = False
        for g in range(n):
            gi = int(inv[g])
            for h in list(cur):
                c = int(T[T[g, h], gi])
                if c not in cur:
                    cur.add(c); changed = True
    return subgroup_generated(T, e, inv, list(cur))

def lower_central_series(T, e, inv):
    """Return list of subgroups [G=gamma1 > gamma2 > ... > 1], gamma_{i+1}=[G,gamma_i]."""
    n = T.shape[0]
    G = np.arange(n)
    series = [G]
    while True:
        prev = series[-1]
        if len(prev) == 1:
            break
        comms = set()
        for a in range(n):
            for h in prev:
                v = int(T[T[T[int(inv[a]), int(inv[int(h)])], a], int(h)])
                comms.add(v)
        nxt = subgroup_generated(T, e, inv, list(comms))
        # normal closure in G to be safe (gamma terms are normal)
        nxt = normal_closure(T, e, inv, list(nxt))
        if len(nxt) == len(prev):
            # stabilized above 1 -> not nilpotent (shouldn't happen for 2-groups)
            series.append(nxt)
            break
        series.append(nxt)
        if len(nxt) == 1:
            break
        assert len(series) <= n + 2
    return series

def nilpotency_class(T, e, inv):
    s = lower_central_series(T, e, inv)
    # gamma_{c+1} = 1, gamma_1 = G; class = len(series)-1 for nontrivial
    return len(s) - 1

def derived_order(T, e, inv):
    return len(commutator_subgroup(T, e, inv))

def frattini_rank(T, e, inv):
    """For a 2-group: rank = log2 |G/Phi|, Phi = G^2 [G,G]."""
    n = T.shape[0]
    assert n & (n - 1) == 0
    squares = {int(T[a, a]) for a in range(n)}
    G2 = subgroup_generated(T, e, inv, list(squares))
    D = commutator_subgroup(T, e, inv)
    Phi = subgroup_generated(T, e, inv, list(set(G2) | set(D)))
    q = n // len(Phi)
    return int(round(np.log2(q))), len(Phi)

def order_profile(T, e, inv):
    ords = el_orders(T, e, inv)
    prof = {}
    for o in ords:
        prof[int(o)] = prof.get(int(o), 0) + 1
    return prof

def is_abelian(T):
    n = T.shape[0]
    for a in range(n):
        for b in range(a + 1, n):
            if T[a, b] != T[b, a]:
                return False
    return True
