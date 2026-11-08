"""Exact finite-field census of reparametrization orbits of non-thin subalgebras.
Run with Python 3: python verify.py. No third-party packages.
"""
from itertools import product
from collections import Counter, deque

N = 14
EXPECTED = {
    2: {1: {8: 6, 16: 1}, 2: {4: 4}},
    4: {1: {384: 14, 768: 1, 1536: 4}, 2: {48: 4, 96: 6}},
}

class Field:
    def __init__(self, q):
        assert q in (2, 4)
        self.q = q
        self.tab = [[0] * q for _ in range(q)]
        for a in range(q):
            for b in range(q):
                z = 0
                for i in range(q.bit_length()-1):
                    if (b >> i) & 1:
                        z ^= a << i
                if q == 4:
                    if z & 8:
                        z ^= 0b1100
                    if z & 4:
                        z ^= 0b111
                self.tab[a][b] = z
        self.inv = [0] + [next(b for b in range(1,q) if self.tab[a][b] == 1)
                              for a in range(1,q)]
        self.monom = [tuple(1 if j == i else 0 for j in range(N)) for i in range(N)]
        for a in range(1,q):
            assert self.tab[a][self.inv[a]] == 1

    def times(self, a, b):
        r = [0] * N
        for i, ai in enumerate(a):
            if ai:
                mult = self.tab[ai]
                for j in range(N-i):
                    bj = b[j]
                    if bj:
                        r[i+j] ^= mult[bj]
        return tuple(r)

    def basis(self, vectors):
        pivots = {}
        for v0 in vectors:
            v = list(v0)
            for j in sorted(pivots):
                if v[j]:
                    mult = self.tab[v[j]]
                    v = [a ^ mult[b] for a,b in zip(v,pivots[j])]
            if any(v):
                j = next(i for i, x in enumerate(v) if x)
                mult = self.tab[self.inv[v[j]]]
                v = [mult[a] for a in v]
                for h, old in list(pivots.items()):
                    mult = self.tab[old[j]]
                    if old[j]:
                        pivots[h] = tuple(a ^ mult[b] for a,b in zip(old,v))
                pivots[j] = tuple(v)
        return tuple(pivots[i] for i in sorted(pivots))

    def normal_form(self, k, z):
        a, b, c, d, e = z[:5]
        x = list(self.monom[4]); x[5]=a; x[7]=b; x[9]=d
        y = list(self.monom[6]); y[7]=c; y[9]=e
        if k==1:
            f,g = z[5:7]; x[11]=f; y[11]=g
            v = [self.monom[0],tuple(x),tuple(y),self.monom[13]]
        else:
            v = [self.monom[0],tuple(x),tuple(y),self.monom[11],self.monom[13]]
        v.extend([self.times(x,x),self.times(x,y),self.times(x,self.times(x,x))])
        return self.basis(v)

    def powers(self, m, c):
        x = list(self.monom[1]); x[m] = c
        ans = [self.monom[0]]
        for _ in range(1,N):
            ans.append(self.times(ans[-1],x))
        return ans

    def scaling(self, c):
        x = list(self.monom[1]); x[1]=c
        ans=[self.monom[0]]
        for _ in range(1,N):
            ans.append(self.times(ans[-1],x))
        return ans

    def substitute(self, vector, powers):
        ans=[0]*N
        for i,c in enumerate(vector):
            if c:
                mult=self.tab[c]
                for j,v in enumerate(powers[i]):
                    if v:
                        ans[j] ^= mult[v]
        return tuple(ans)


def run(q):
    F=Field(q)
    full={}; split={1:0,2:0}
    piv={1:(0,4,6,8,10,12,13),2:(0,4,6,8,10,11,12,13)}
    for kind in (1,2):
        length=7 if kind==1 else 5
        for params in product(range(q),repeat=length):
            # In characteristic 2, the published non-thin criterion 3a != 2c reduces to a != 0.
            if not params[0]:
                continue
            B=F.normal_form(kind,params)
            assert tuple(next(i for i,a in enumerate(v) if a) for v in B)==piv[kind]
            assert B not in full, 'Nonunique parameterization'
            full[B]=(kind,params)
            split[kind]+=1
            # Check closure under products and independent verification of the embedding dimension.
            allproducts=[F.times(v,w) for v in B for w in B]
            assert len(F.basis(B+tuple(allproducts)))==len(B), 'Not a subalgebra'
            radical=B[1:]
            radical_products=[F.times(v,w) for v in radical for w in radical]
            dimsq=len(F.basis(radical_products))
            assert len(radical)-dimsq == (2 if kind==1 else 3)
    assert split[1]==q**7-q**6 and split[2]==q**5-q**4

    # Every automorphism t -> u*t + c2*t^2 + ... + c13*t^13 factors
    # successively into scalar dilation and elementary substitutions.
    # Additive bases: {1} for F2 and {1,alpha} for F4 (alpha=2).
    gens=[F.powers(m,c) for m in range(2,N) for c in ([1] if q==2 else [1,2])]
    if q==4:
        gens.append(F.scaling(2))
    unseen=set(full); hist={1:Counter(),2:Counter()}
    while unseen:
        root=unseen.pop()
        Q=deque([root]);size=1
        kind=full[root][0]
        while Q:
            B=Q.popleft()
            for powers in gens:
                C=F.basis([F.substitute(v,powers) for v in B])
                assert C in full and full[C][0]==kind, 'Automorphism failed to preserve stratum'
                if C in unseen:
                    unseen.remove(C);Q.append(C);size+=1
        hist[kind][size]+=1
    for kind in (1,2):
        assert dict(hist[kind]) == EXPECTED[q][kind], (q,kind,hist[kind])
        assert sum(size*multiplicity for size,multiplicity in hist[kind].items())==split[kind]
    print('q=',q,'sizes=',split,'orbits=',dict((i,dict(hist[i])) for i in (1,2)))

if __name__=='__main__':
    run(2)
    run(4)
    print('VERIFY_OK')
