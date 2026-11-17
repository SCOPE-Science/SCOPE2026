from itertools import combinations
from math import gcd
from collections import Counter
from sympy import Matrix,ZZ
from sympy.matrices.normalforms import smith_normal_form

def crosses(a,b,c,d):
    if len({a,b,c,d})<4:return False
    if a>b:a,b=b,a
    if c>d:c,d=d,c
    return ((a<c<b)!=(a<d<b)) and ((c<a<d)!=(c<b<d))

def faces(p):
    diag=[(a,b) for a in range(p) for b in range(a+1,p) if ((b-a)!=1 and (a,b)!=(0,p-1))]
    compatibility={(i,j):not crosses(*diag[i],*diag[j]) for i in range(len(diag)) for j in range(i+1,len(diag))}
    out=[[] for i in range(p-2)]
    for k in range(1,p-2):
        out[k]=[c for c in combinations(range(len(diag)),k) if all(compatibility[i,j] for i,j in combinations(c,2))]
    maps=[]
    for t in range(p):
        maps.append([diag.index(tuple(sorted(((a+t)%p,(b+t)%p)))) for a,b in diag])
    def canonical(face):
        tuples=[tuple(sorted(maps[t][u] for u in face)) for t in range(p)]
        i=min(range(p),key=lambda t:tuples[t])
        raw=[maps[i][u] for u in face]
        inversions=sum(raw[a]>raw[b] for a in range(len(raw)) for b in range(a+1,len(raw)))
        return tuples[i],(-1)**inversions
    orbits=[]; idxs=[]
    for k in range(1,p-2):
        reps=sorted({canonical(f)[0] for f in out[k]})
        orbits.append(reps)
        idxs.append({r:i for i,r in enumerate(reps)})
        assert len(out[k])==p*len(reps)
    # matrices d_k for simplex of size k+1 to size k. d1 edges to vertices.
    matrices=[]
    for k in range(2,p-2):
        matr=Matrix.zeros(len(orbits[k-2]),len(orbits[k-1]))
        for j,sigma in enumerate(orbits[k-1]):
            for i in range(len(sigma)):
                tau=sigma[:i]+sigma[i+1:]
                canon,sg=canonical(tau)
                matr[idxs[k-2][canon],j]+=(-1)**i*sg
        matrices.append(matr)
    for j in range(len(matrices)-1):
        assert matrices[j]*matrices[j+1]==Matrix.zeros(matrices[j].rows,matrices[j+1].cols)
    print('p',p,'original face counts',[len(f) for f in out[1:]],'quotient face counts',list(map(len,orbits)))
    if p==7:
        d1,d2,d3=matrices
        print('d1=',d1)
        # choose spanning edge with boundary +e1-e0, then remaining edges form cycle coordinates.
        col=next(j for j in range(d1.cols) if d1[:,j]!=Matrix.zeros(d1.rows,1))
        tree=d1[:,col]; assert set(tree)=={1,-1}
        others=[j for j in range(d1.cols) if j!=col]
        assert d1.rank()==1
        # project boundary d2 to non-tree edge coordinates
        rel=d2[others,:]
        snf=smith_normal_form(rel,domain=ZZ)
        diagonal=[abs(int(snf[i,i])) for i in range(min(snf.rows,snf.cols)) if snf[i,i]!=0]
        print('H1 nonzero Smith invariants',diagonal,'H1 free rank',len(others)-len(diagonal))
        assert diagonal==[1]* (len(others)-1)+[7],diagonal
        assert d2.rank()==len(others) and d3.rank()==d2.cols-len(others)
        assert d3.cols-d3.rank()==1
        d3snf=smith_normal_form(d3,domain=ZZ)
        d3factors=[abs(int(d3snf[i,i])) for i in range(min(d3snf.rows,d3snf.cols)) if d3snf[i,i]!=0]
        print('H2 image primitive factors',d3factors)
        assert d3factors==[1]*5
        print('p=7 H_1=Z/7, H_2=0, H_3=Z, H_0=Z')
    elif p==5:
        assert len(orbits)==2 and len(orbits[0])==1 and len(orbits[1])==1
        print('p=5 quotient is a circle')

for p in [5,7]:faces(p)
print('ASSOCIAHEDRON_PRIME_LENS_QUOTIENT_PASS')
