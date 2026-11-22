#!/usr/bin/env python3
"""Independent finite-field row reduction for delta derivations of sl2.

Only the displayed Lie brackets and action matrices are used; the proof's
weight-block reduction is not used in the computation.
"""

def rank_mod(rows, p):
    a = [[z % p for z in row] for row in rows]
    rank = 0
    for col in range(len(a[0])):
        pivot = next((r for r in range(rank, len(a)) if a[r][col]), None)
        if pivot is None:
            continue
        a[pivot], a[rank] = a[rank], a[pivot]
        t = pow(a[rank][col], -1, p)
        a[rank] = [t * z % p for z in a[rank]]
        for r in range(rank + 1, len(a)):
            t = a[r][col]
            if t:
                a[r] = [(x - t*y) % p for x,y in zip(a[r],a[rank])]
        rank += 1
    return rank


def direct_dimension(p, m, delta):
    d = m + 1
    e = [[0]*d for _ in range(d)]
    f = [[0]*d for _ in range(d)]
    h = [[0]*d for _ in range(d)]
    for i in range(d):
        h[i][i] = m - 2*i
        if i:
            e[i-1][i] = m-i+1
        if i<d-1:
            f[i+1][i] = i+1
    act=[e,f,h]
    # Brackets: [e,f]=h, [h,e]=2e, [h,f]=-2f.
    eq=[]
    for i,j,k,c in [(0,1,2,1),(2,0,0,2),(2,1,1,-2)]:
        for s in range(d):
            row=[0]*(3*d)
            row[k*d+s] += c
            for t in range(d):
                row[j*d+t] -= delta*act[i][s][t]
                row[i*d+t] += delta*act[j][s][t]
            eq.append(row)
    return 3*d-rank_mod(eq,p)


def predicted(p, m, delta):
    if m==0:
        return 0
    if m==p-2:
        return p+1 if delta==1 else 0
    if m==p-1:
        return p if delta==1 else p+2 if delta==2 else 0
    if delta==1:
        return m+1
    if delta==(-2*pow(m,-1,p))%p:
        return m+3
    if m>=2 and delta==(2*pow(m+2,-1,p))%p:
        return m-1
    return 0


def run():
    tests=0
    for p in [3,5,7,11,13,17,19]:
        for m in range(p):
            for delta in range(p):
                expected=predicted(p,m,delta)
                got=direct_dimension(p,m,delta)
                assert got==expected, (p,m,delta,expected,got)
                tests+=1
    # Primes were tested over their prime fields; ranks extend unchanged to F_{p^e}.
    assert direct_dimension(3,2,2)==5
    assert direct_dimension(5,4,2)==7
    assert direct_dimension(7,5,1)==8
    print('MODULAR_SL2_DELTA_SPECTRUM_OK', tests)

if __name__=='__main__':
    run()
