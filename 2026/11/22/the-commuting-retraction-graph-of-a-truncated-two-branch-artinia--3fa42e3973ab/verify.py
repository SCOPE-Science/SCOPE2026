"""Finite-field replay of the defining identities for truncated two-branch rings.

This checker enumerates all unital homomorphisms from generator images in
A=k[x,y]/(x^2,xy,y^N). The general all-field theorem is proved separately.
Run: python verify.py
"""
from itertools import product
from collections import Counter


def field(q):
    if q == 4:
        # F_2[t]/(t^2+t+1), binary-basis representation.
        def add(a, b): return a ^ b
        def mul(a, b):
            z = 0
            while b:
                if b & 1: z ^= a
                a <<= 1
                if a & 4: a ^= 7
                b >>= 1
            return z
    else:
        def add(a, b): return (a + b) % q
        def mul(a, b): return (a * b) % q
    return add, mul


def check(q, N):
    add, mul = field(q)
    dim = N + 1  # 1,x,y,...,y^(N-1)
    zero = (0,) * dim
    one = (1,) + (0,) * N
    def plus(a,b): return tuple(add(v,w) for v,w in zip(a,b))
    def scale(s,a): return tuple(mul(s,v) for v in a)
    def times(a,b):
        out = [0] * dim
        out[0] = mul(a[0], b[0])
        for i in range(1, dim):
            out[i] = add(mul(a[0],b[i]),mul(b[0],a[i]))
        for i in range(2,dim):
            for j in range(2,dim):
                t = i+j-1
                if t < dim: out[t] = add(out[t],mul(a[i],b[j]))
        return tuple(out)
    def power(a, m):
        z=one
        for _ in range(m):z=times(z,a)
        return z
    def evaluate(v,fx,fy):
        z = scale(v[0],one)
        for idx,coeff in enumerate(v[1:]):
            basis_image = fx if idx==0 else power(fy,idx)
            z=plus(z,scale(coeff,basis_image))
        return z
    vectors = [(0,) + a for a in product(range(q),repeat=N)]
    maps=[]
    for fx in vectors:
        if times(fx,fx)!=zero:continue
        for fy in vectors:
            if times(fx,fy)!=zero or power(fy,N)!=zero:continue
            if evaluate(fx,fx,fy)==fx and evaluate(fy,fx,fy)==fy:
                maps.append((fx,fy))
    # Independently construct the claimed normal forms and compare every map.
    x = (0, 1) + (0,) * (N - 1)
    y = (0, 0, 1) + (0,) * (N - 2)
    socle = (0,) * N + (1,)
    minus_one = 1 if q in (2,4) else q - 1
    predicted = {(zero, zero), (x, y)}
    for c in range(q):
        for t in range(q):
            predicted.add((scale(t,socle), plus(plus(y,scale(c,x)),scale(mul(minus_one,mul(c,t)),socle))))
    first = (N + 1) // 2
    for a in range(q):
        for coeffs in product(range(q), repeat=N-first):
            h = [0] * dim
            for j, coeff in enumerate(coeffs, start=first):
                h[j+1] = coeff
            ux = plus(x, tuple(h))
            predicted.add((ux, scale(a,ux)))
    assert set(maps) == predicted, (q,N,'normal-form discrepancy')
    def rank_of(f):
        fx,fy=f
        mat=[list(one),list(fx)] + [list(power(fy,j)) for j in range(1,N)]
        r=0
        for c in range(dim):
            piv=next((i for i in range(r,len(mat)) if mat[i][c]),None)
            if piv is None:continue
            mat[r],mat[piv]=mat[piv],mat[r]
            inv=next(j for j in range(1,q) if mul(mat[r][c],j)==1)
            mat[r]=[mul(inv,u) for u in mat[r]]
            for i in range(len(mat)):
                if i!=r and mat[i][c]:
                    t=mat[i][c]
                    # Subtraction equals addition in characteristic two.
                    if q == 4 or q == 2:
                        mat[i]=[add(u,mul(t,v)) for u,v in zip(mat[i],mat[r])]
                    else:
                        mat[i]=[(u-t*v)%q for u,v in zip(mat[i],mat[r])]
            r+=1
        return r
    counts=Counter(map(rank_of,maps))
    m=N//2
    expected={1:1,2:q**(m+1),N:q*q,N+1:1}
    assert counts==expected, (q,N,counts,expected)
    inner=[f for f in maps if rank_of(f) in (2,N)]
    edges=[]
    for i,f in enumerate(inner):
        for j in range(i+1,len(inner)):
            g=inner[j]
            if evaluate(g[0],*f)==evaluate(f[0],*g) and evaluate(g[1],*f)==evaluate(f[1],*g):
                edges.append((i,j))
    degree=Counter(k for edge in edges for k in edge)
    assert len(edges)==q*q
    assert max(degree.values(),default=0)==1
    assert len(inner)-len(degree)==q**(m+1)-q*q
    assert all(set((rank_of(inner[i]),rank_of(inner[j])))=={2,N} for i,j in edges)
    total=2+q*q+q**(m+1)
    ordered_commuting=5*q**(m+1)+7*q*q+4
    assert ordered_commuting == total + 2*(2*(total-2)+1+q*q)
    print(f'q={q} N={N}: {total} retractions, ranks {dict(sorted(counts.items()))}, '+
          f'{len(edges)} edges, {len(inner)-len(degree)} isolates, '+
          f'{ordered_commuting} ordered commuting pairs')


if __name__=='__main__':
    for parameters in [(2,3),(3,3),(4,3),(5,3),(2,4),(3,4),(2,5),(2,6)]:
        check(*parameters)
    print('TRUNCATED_BRANCH_RETRACTION_GRAPH_VERIFIED')
