"""Independent finite verification of two-matching topology of triangular books."""
from itertools import combinations
from math import comb

def faces_by_subsets(n):
    # Edge indices: u-i: [0,n), v-i: [n,2n), central uv: 2n.
    edges=[(0,i+2) for i in range(n)]+[(1,i+2) for i in range(n)]+[(0,1)]
    out={(): 0}
    for r in range(1,5):
        for s in combinations(range(2*n+1),r):
            degrees=[0]*(n+2)
            for j in s:
                a,b=edges[j]; degrees[a]+=1; degrees[b]+=1
            if max(degrees)<=2:
                out[s]=r-1
    return out

def faces_by_formula(n):
    a=range(n); b=range(n,2*n); c=2*n
    z={()}
    for i in range(3):
        for x in combinations(a,i):
            for j in range(3):
                for y in combinations(b,j):
                    z.add(tuple(sorted(x+y)))
    for i in range(2):
        for x in combinations(a,i):
            for j in range(2):
                for y in combinations(b,j):
                    z.add(tuple(sorted(x+y+(c,))))
    return z

def betti2(faces):
    dims={}
    for s in faces:
        if s:
            dims.setdefault(len(s)-1,[]).append(s)
    for x in dims.values(): x.sort()
    ranks={}
    for dim in range(1,max(dims)+1):
        row_index={f:j for j,f in enumerate(dims[dim-1])}
        basis={}
        for sigma in dims.get(dim,[]):
            v=0
            for i in range(len(sigma)):
                f=sigma[:i]+sigma[i+1:]
                v^=1 << row_index[f]
            while v:
                p=v.bit_length()-1
                if p not in basis:
                    basis[p]=v;break
                v^=basis[p]
        ranks[dim]=len(basis)
    ranks[0]=1 if dims.get(0) else 0
    return {d:len(cells)-ranks.get(d,0)-ranks.get(d+1,0) for d,cells in dims.items()}

def run():
    for n in range(2,11):
        f=faces_by_subsets(n); g=faces_by_formula(n)
        assert set(f)==g,(n,'face difference')
        expected_count=(1+n+comb(n,2))**2+(1+n)**2
        assert len(f)==expected_count,(n,len(f),expected_count)
        beta=betti2(f)
        expected={2:(n-1)**2,3:comb(n-1,2)**2}
        for k in range(1,4):
            assert beta.get(k,0)==expected.get(k,0),(n,k,beta,expected)
        assert beta[0]==0,(n,beta)
        vec=[sum(1 for t in f if len(t)==k) for k in range(5)]
        print(f'n={n:2d} faces={len(f):5d} augmented_f_vector={vec} beta2={beta.get(2,0):3d} beta3={beta.get(3,0):3d}')
    print('PASS: independent graph-incidence faces, cone-join enumeration, mod-two boundary ranks, and formula match for 2<=n<=10.')

if __name__=='__main__':run()
