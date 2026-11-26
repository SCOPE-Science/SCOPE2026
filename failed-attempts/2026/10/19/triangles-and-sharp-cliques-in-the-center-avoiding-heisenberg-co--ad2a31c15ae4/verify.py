"""Finite checks for a symplectic Lie-generation subgraph.
Uses only the Python standard library and prime finite fields.
Run: python verify.py
"""
from itertools import combinations, product
from math import prod


def rref(basis, q):
    rows = [list(row) for row in basis if any(x % q for x in row)]
    if not rows:
        return ()
    d = len(rows[0]); rank = 0
    for col in range(d):
        pivot = next((i for i in range(rank, len(rows)) if rows[i][col] % q), None)
        if pivot is None: continue
        rows[rank],rows[pivot]=rows[pivot],rows[rank]
        a = pow(rows[rank][col], -1, q)
        rows[rank]=[(a*x)%q for x in rows[rank]]
        for i in range(len(rows)):
            if i != rank:
                t=rows[i][col]
                if t:
                    rows[i]=[(x-t*y)%q for x,y in zip(rows[i],rows[rank])]
        rank += 1
        if rank == len(rows): break
    return tuple(tuple(v) for v in rows[:rank])


def all_k_subspaces(dim,k,q):
    if k==0: return [()]
    ans=[]
    for pivots in combinations(range(dim),k):
        positions=[(r,c) for r in range(k) for c in range(pivots[r]+1,dim) if c not in pivots]
        for vals in product(range(q),repeat=len(positions)):
            rows=[[0]*dim for _ in range(k)]
            for r,c in enumerate(pivots): rows[r][c]=1
            for (r,c),v in zip(positions,vals):rows[r][c]=v
            ans.append(tuple(tuple(row) for row in rows))
    assert len(ans)==len(set(ans))
    return ans


def rank(rows,q): return len(rref(rows,q))


def symplectic(u,v,q):
    n=len(u)//2
    return sum(u[i]*v[n+i]-u[n+i]*v[i] for i in range(n))%q


def isotropic(U,q): return all(symplectic(u,v,q)==0 for u in U for v in U)


def _sym_count(n,q):
    s=[1,q-1]
    for k in range(2,n+1):
        s.append((q-1)*q**(k-1)*s[-1]+(q**(k-1)-1)*q**(k-1)*s[-2])
    return s[n]


def symmetric_direct(n,q):
    places=[(i,j) for i in range(n) for j in range(i,n)]
    tot=0
    for seq in product(range(q),repeat=len(places)):
        mat=[[0]*n for _ in range(n)]
        for (i,j),v in zip(places,seq):mat[i][j]=mat[j][i]=v
        if rank(mat,q)==n:tot+=1
    return tot


def iso_count_formula(n,k,q):
    x=prod(q**(2*n-i)-q**i for i in range(k))
    y=prod(q**k-q**i for i in range(k))
    return x//y


def verify(q,n,check_actual_lie):
    m=2*n
    iso={k:[U for U in all_k_subspaces(m,k,q) if isotropic(U,q)] for k in range(1,n+1)}
    for k,spaces in iso.items():
        assert len(spaces)==iso_count_formula(n,k,q),(n,q,k,len(spaces))
    lags=iso[n]; L=prod(q**i+1 for i in range(1,n+1))
    assert len(lags)==L
    comps=[set() for _ in lags]
    for i in range(len(lags)):
        for j in range(i+1,len(lags)):
            if rank(lags[i]+lags[j],q)==m:
                comps[i].add(j);comps[j].add(i)
    t=q**(n*(n+1)//2)
    assert all(len(N)==t for N in comps)
    tordered=sum(len(comps[i]&comps[j]) for i in range(len(lags)) for j in comps[i]); assert tordered%6==0
    T=tordered//6
    S=_sym_count(n,q)
    assert T == L*t*S//6,(q,n,T,L*t*S//6)
    active=q**n*L
    isolated=sum(q**k*len(iso[k]) for k in range(1,n))
    degree=q**n*t
    triangles=T*q**(3*n)
    edges=L*t*q**(2*n)//2
    assert active*degree//2 ==edges
    # Rank test of the generated Lie algebra: concatenate generators and cross brackets.
    if check_actual_lie:
        atoms=[]
        for k,groups in iso.items():
            for U in groups:
                for func in product(range(q),repeat=k):
                    atoms.append((U,tuple(tuple(list(v)+[func[i]]) for i,v in enumerate(U))))
        assert len(atoms)==active+isolated
        actual_edges=0
        for i in range(len(atoms)):
            ui,ai=atoms[i]
            for j in range(i+1,len(atoms)):
                uj,aj=atoms[j]
                cross=[(0,)*m+(symplectic(x[:m],y[:m],q),) for x in ai for y in aj]
                actual=rank(ai+aj+tuple(cross),q)==m+1
                expected=(len(ui)==n and len(uj)==n and rank(ui+uj,q)==m)
                assert actual==expected,(q,n,i,j,ui,uj)
                actual_edges+=int(actual)
        assert actual_edges==edges
    # Exact matrix enumeration independently verifies symmetric recurrence.
    if n<=3 and q<=3:
        assert symmetric_direct(n,q)==S
    print('verified', 'q=',q,'n=',n,'Lagrangians=',L,'complements=',t,
          'symmetric_nonsingular=',S,'active=',active,'isolated=',isolated,
          'degree=',degree,'edges=',edges,'triangles=',triangles)


def main():
    for q,n,brutal in [(2,1,True),(3,1,True),(2,2,True),(3,2,True),(2,3,False)]:
        verify(q,n,brutal)
    print('VERIFY_OK 5 cases; direct Lie-bracket closure and triple counting')

if __name__=='__main__':main()
