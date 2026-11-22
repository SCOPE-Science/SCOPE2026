#!/usr/bin/env python3
"""Independent direct word-level checks of four-one unbordered rotations."""
from collections import Counter
from itertools import combinations, product

N_MAX = 20

def direct(w):
    n = len(w)
    unbordered = 0
    for i in range(n):
        v = w[i:] + w[:i]
        if all(v[:k] != v[n-k:] for k in range(1,n)):
            unbordered += 1
    return unbordered

def gaps_at_a_one(w, i):
    n = len(w)
    assert w[i] == '1'
    g = []
    p = (i+1) % n
    for _ in range(4):
        zeros = 0
        while w[p] == '0':
            zeros += 1
            p = (p+1) % n
        g.append(zeros)
        p = (p+1) % n
    assert p == (i+1)%n
    return tuple(g)

def gap_law(g):
    a,b,c,d = g
    nearby = sum(g[i] != g[(i+1)%4] for i in range(4))
    return (nearby - 2*(a==c and a<min(b,d))
                   - 2*(b==d and b<min(a,c))
                   - 2*(a==c and b==d and a!=b))

def signed_num(g):
    ans=0
    for i in range(4):
        a,b,c,d=(g[(i+j)%4] for j in range(4))
        ans += int(a<d and not (a==c and b>=d))
        ans += int(a>d and not (b==d and c>=a))
    return ans

def coeffs():
    P={0:(1,-1,1,-2,1,-1,1),2:(0,4,4,0,-8,-8,8),
       3:(0,0,0,8,8,8,-24),4:(0,0,0,0,4,4,16)}
    # D = product_{j=1}^4(1-z^j), hence G_j=P_j/D.
    gf={}
    for j,p in P.items():
        arr=list(p)+[0]*max(0,N_MAX-3-len(p))
        arr=arr[:N_MAX-3]
        for k in (1,2,3,4):
            for t in range(k,len(arr)):
                arr[t] += arr[t-k]
        gf[j]=arr
    return gf

def run():
    spectra=coeffs()
    for n in range(4,N_MAX+1):
        counts=Counter()
        for ones in combinations(range(n),4):
            w=['0']*n
            for i in ones: w[i]='1'
            w=''.join(w)
            u=direct(w)
            g=gaps_at_a_one(w,ones[0])
            assert u==gap_law(g)==signed_num(g), (n,w,g,u)
            counts[u]+=1
        assert sum(counts.values())==len(list(combinations(range(n),4)))
        for label in (0,2,3,4):
            assert counts[label] == n * spectra[label][n-4] // 4
            assert 4 * counts[label] == n * spectra[label][n-4]
        assert not (set(counts)-{0,2,3,4})
        print(n,dict(sorted(counts.items())))
    # Additional large-gap probes, independent of the finite-n enumerations.
    for a,b,c,d in product((0,1,2,5,9,17,31),repeat=4):
        g=(a,b,c,d)
        w=''.join('1'+'0'*x for x in g)
        assert direct(w)==gap_law(g)==signed_num(g),g
    print('direct word, gap law, exact generating coefficients PASS')

if __name__=='__main__':run()
