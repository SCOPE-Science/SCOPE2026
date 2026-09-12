"""dim H^2(Q32; F2) via normalized bar resolution over GF(2). Result: 2."""
els = [(i, j) for i in range(16) for j in range(2)]

def mul(x, y):
    i, j = x; k, l = y
    if j == 0:
        return ((i + k) % 16, l)
    else:
        if l == 0:
            return ((i - k) % 16, 1)
        else:
            return ((i - k + 8) % 16, 0)

non1 = [e for e in els if e != (0, 0)]
vidx = {e: i for i, e in enumerate(non1)}
m = len(non1)

def var(g, h):
    if g == (0, 0) or h == (0, 0):
        return None
    return vidx[g] * m + vidx[h]

N = m * m
rows = []
for g in els:
    for h in els:
        for k in els:
            vs = [v for v in (var(g, h), var(mul(g, h), k), var(g, mul(h, k)), var(h, k)) if v is not None]
            s = set()
            for v in vs:
                if v in s:
                    s.remove(v)
                else:
                    s.add(v)
            if s:
                rows.append(s)
print("eqns:", len(rows), "unknowns:", N)
pivot, rank = {}, 0
for s in rows:
    b = 0
    for v in s:
        b |= (1 << v)
    x = b
    while x:
        c = x.bit_length() - 1
        if c in pivot:
            x ^= pivot[c]
        else:
            pivot[c] = x; rank += 1
            break
print("eqn rank:", rank, "=> dim Z^2 =", N - rank)
crows = []
for t_elt in non1:
    s = set()
    for g in non1:
        for h in non1:
            v = (1 if g == t_elt else 0) + (1 if h == t_elt else 0) + (1 if mul(g, h) == t_elt else 0)
            if v % 2 == 1:
                s.add(vidx[g] * m + vidx[h])
    b = 0
    for v in s:
        b |= (1 << v)
    if b:
        crows.append(b)
piv2, crank = {}, 0
for b in crows:
    x = b
    while x:
        c = x.bit_length() - 1
        if c in piv2:
            x ^= piv2[c]
        else:
            piv2[c] = x; crank += 1
            break
print("coboundary rank:", crank)
print("dim H^2(Q32;F2) =", (N - rank) - crank)
