"""Reconstruct the binary rank-four subspace building and the C7 orbit complex.
Uses only Python 3 standard library; optionally SymPy for exact Smith normal form.
"""
from itertools import combinations

def rank(vs):
    bas={}
    for x in vs:
        while x:
            b=x.bit_length()-1
            if b in bas: x^=bas[b]
            else: bas[b]=x;break
    return len(bas)

def span_mask(vs):
    x={0}
    for v in vs: x|={a^v for a in tuple(x)}
    return sum(1<<v for v in x)

def subspaces():
    S={}
    for d in (1,2,3):
        for vs in combinations(range(1,16),d):
            if rank(vs)==d:
                S[span_mask(vs)]=d
    assert [list(S.values()).count(i) for i in (1,2,3)]==[15,35,15]
    return S

def mul(v):
    # Vector V=F2*e0 + F8 with t^3=t+1.
    a,b,c=(v>>1)&1,(v>>2)&1,(v>>3)&1
    return (v&1) | (c<<1) | ((a^c)<<2) | (b<<3)

def act_mask(m):
    return sum(1<<mul(v) for v in range(16) if (m>>v)&1)

def orbit_reps(cells):
    unseen=set(cells); reps={}
    while unseen:
        s=min(unseen); orb=set(); t=s
        for _ in range(7):
            orb.add(t); t=tuple(act_mask(v) for v in t)
        assert t==s
        assert orb <= unseen
        for u in orb: reps[u]=s
        unseen-=orb
    return reps

def main():
    S=subspaces()
    ranks={d:sorted(s for s,r in S.items() if r==d) for d in (1,2,3)}
    lt=lambda a,b: a!=b and (a&b)==a
    C0={(x,) for x in S}
    C1={(a,b) for a,b in combinations(S,2) if (S[a]<S[b] and lt(a,b)) or (S[b]<S[a] and lt(b,a))}
    C1={tuple(sorted(t,key=lambda a:S[a])) for t in C1}
    C2={(a,b,c) for a in ranks[1] for b in ranks[2] if lt(a,b) for c in ranks[3] if lt(b,c)}
    assert (len(C0),len(C1),len(C2))==(65,315,315)
    assert all(act_mask(s) in S and S[act_mask(s)]==d for s,d in S.items())
    maps=[orbit_reps(C) for C in (C0,C1,C2)]
    basis=[sorted(set(m.values())) for m in maps]
    assert tuple(map(len,basis))==(11,45,45),tuple(map(len,basis))
    indexes=[{c:i for i,c in enumerate(B)} for B in basis]
    matrices=[]
    for k in (1,2):
        D=[[0]*len(basis[k]) for _ in basis[k-1]]
        for j,c in enumerate(basis[k]):
            for i in range(len(c)):
                face=c[:i]+c[i+1:]
                r=maps[k-1][face]
                D[indexes[k-1][r]][j]+=(-1)**i
        matrices.append(D)
    D1,D2=matrices
    for i in range(len(basis[0])):
        for j in range(len(basis[2])):
            assert sum(D1[i][k]*D2[k][j] for k in range(len(basis[1])))==0
    # Choose 10 independent edges of the 1-skeleton via spanning tree.
    parent=list(range(len(basis[0])))
    def find(x):
        while parent[x]!=x: x=parent[x]
        return x
    tree=[]
    for j in range(len(basis[1])):
        support=[i for i in range(len(basis[0])) if D1[i][j]]
        assert len(support)==2 and sorted(D1[i][j] for i in support)==[-1,1]
        a,b=map(find,support)
        if a!=b:
            parent[a]=b; tree.append(j)
    assert len(tree)==len(basis[0])-1
    others=[j for j in range(len(basis[1])) if j not in tree]
    # Boundary in C1 / span(tree) is projected by the complement coordinate;
    # every cycle is determined by these coordinates (unimodular graph incidence).
    M=[[D2[j][k] for k in range(len(basis[2]))] for j in others]
    from sympy import Matrix,ZZ
    from sympy.matrices.normalforms import smith_normal_form
    diag=smith_normal_form(Matrix(M),domain=ZZ).diagonal()
    nz=[abs(int(x)) for x in diag if x]
    assert len(nz)==35 and set(nz)=={1},(len(nz),set(nz))
    assert len(basis[2])-len(nz)==10
    assert {a for a in S if act_mask(a)==a}=={span_mask([1]),span_mask([2,4,8])}
    for k in range(1,7):
        fixed=[s for s in S if all(act_mask(s)==s for _ in (0,))]
        # Distinct nontrivial powers are generators because 7 is prime.
        assert len(fixed)==2
    print('BINARY_PARABOLIC_SINGER_PASS original=(65,315,315) quotient=(11,45,45)')
    print('d1rank=10 d2smith_unit_invariants=35 H1=0 H2=Z^10 fixed_nonidentity_vertices=2')
    for q in (2,3,4,5,7,8,9):
        top=1+q**6; scalar=(q-2)*(1+q**3); generic=(q**3-q)*2
        assert (top+scalar+generic)//(q**3-1)==q**3+q+1
        assert (top+scalar+generic)%(q**3-1)==0
    print('BURNSIDE_POLYNOMIAL_PASS q=2,3,4,5,7,8,9')
if __name__=='__main__':main()
