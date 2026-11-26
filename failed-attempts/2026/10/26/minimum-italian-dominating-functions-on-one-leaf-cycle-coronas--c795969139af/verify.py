"""Standalone exact checks for minimum Italian functions on one-leaf coronas.

No external packages.  All tests independently implement the defining
zero-neighbor inequality rather than relying on the proof's 3-state classification.
"""
from itertools import product
from math import ceil


def direct_minima(edges, n):
    nbr = [set() for _ in range(2 * n)]
    for a, b in edges:
        nbr[a].add(b)
        nbr[b].add(a)
    for a in range(n):
        b = n + a
        nbr[a].add(b)
        nbr[b].add(a)
    best, count = 3 * n, 0
    for label in product(range(3), repeat=2 * n):
        w = sum(label)
        if w > best:
            continue
        if any(label[v] == 0 and sum(label[u] for u in nbr[v]) < 2
               for v in range(2 * n)):
            continue
        if w < best:
            best, count = w, 0
        count += 1
    return best, count


def base_gamma_count(edges, n):
    N = [1 << i for i in range(n)]
    for a,b in edges:
        N[a] |= 1<<b
        N[b] |= 1<<a
    msk = (1 << n) - 1
    gam = n
    for B in range(1<<n):
        cover = 0
        for i in range(n):
            if B & (1<<i): cover |= N[i]
        gam = min(gam, B.bit_count() + (msk & ~cover).bit_count())
    cnt=0
    for B in range(1<<n):
        cover = 0
        for i in range(n):
            if B & (1<<i): cover |= N[i]
        if B.bit_count()+(msk&~cover).bit_count()==gam:
            cnt+=2**B.bit_count()
    return n+gam,cnt


def predicted(n):
    m, r = divmod(n, 3)
    cnt=(3*2**m if r==0 else n*(m+3)*2**m if r==1 else n*2**(m+1))
    return n+(n+2)//3, cnt


def cycle(n):
    return sorted(set((i,(i+1)%n) if i<(i+1)%n else ((i+1)%n,i)
                      for i in range(n)))


def run():
    # Fully independent direct definition enumeration, 3^(2n) functions.
    for n in range(3, 7):
        direct=direct_minima(cycle(n),n)
        partial=base_gamma_count(cycle(n),n)
        formula=predicted(n)
        assert direct==partial==formula, (n,direct,partial,formula)
        print(f'direct_cycle_corona_n={n}: minimum={direct[0]}, count={direct[1]}')

    # Exhaust ALL simple base graphs on 2,3,4 vertices against direct 3^(2n) labels.
    for n in range(2,5):
        edges=[(i,j) for i in range(n) for j in range(i+1,n)]
        for mask in range(1<<len(edges)):
            E=[e for k,e in enumerate(edges) if mask>>k & 1]
            assert direct_minima(E,n)==base_gamma_count(E,n),(n,mask)
        print(f'general_base_n={n}: {1<<len(edges)} graphs checked')

    # Independent direct binomial-composition enumeration: min dominating sets.
    for n in range(3,41):
        k=(n+2)//3
        dcount=0
        one_uncovered=0
        for B in range(1<<n) if n<=14 else ():
            if B.bit_count()>k:continue
            covered=0
            for i in range(n):
                if B>>i&1:
                    for j in (i-1,i,i+1):covered |= 1<<(j%n)
            missing=n-covered.bit_count()
            if B.bit_count()+missing==k:
                dcount+=2**B.bit_count()
                if missing==1: one_uncovered+=2**B.bit_count()
        if n<=14:
            assert dcount==predicted(n)[1],(n,dcount,predicted(n))
            if n%3==1: assert one_uncovered==n*(2**(n//3))
            else: assert one_uncovered==0
        print(f'formula_n={n}: minimum={predicted(n)[0]}, count={predicted(n)[1]}')
    print('VERIFY_OK')

if __name__ == '__main__': run()
