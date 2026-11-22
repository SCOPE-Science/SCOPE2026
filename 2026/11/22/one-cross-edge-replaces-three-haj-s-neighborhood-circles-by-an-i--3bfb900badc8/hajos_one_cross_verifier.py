"""Finite cross-checks for the augmented two-clique Hajos graph.

The unbounded homology statement is proved by the simplex attachment
argument in RESULT.md, not inferred from these finite tests.
Run: python3 hajos_one_cross_verifier.py
"""
from collections import defaultdict
from itertools import combinations


def graph(a, b, augmented=False):
    assert a >= 5 and b >= 5
    w, y, alpha, z, beta = 0, 1, 2, a, a+1
    A = list(range(1,a))
    B = list(range(a,a+b-1))
    edges = set()
    def add(u,v):
        assert u != v
        edges.add((min(u,v),max(u,v)))
    for shore in (A, B):
        for u,v in combinations(shore,2):add(u,v)
    for t in A[1:] + B[1:]:add(w,t)
    add(y,z)
    if augmented: add(alpha,beta)
    return a+b-1,edges


def neighborhood_complex(a,b,augmented):
    n,edges=graph(a,b,augmented)
    ngh=[0]*n
    for u,v in edges:
        ngh[u]|=1<<v
        ngh[v]|=1<<u
    faces=defaultdict(set)
    for M in ngh:
        S=M
        while S:
            faces[S.bit_count()-1].add(S)
            S=(S-1)&M
    return faces,ngh


def rank2(cols):
    piv={}
    for c in cols:
        while c:
            k=c.bit_length()-1
            if k in piv:c^=piv[k]
            else:
                piv[k]=c
                break
    return len(piv)


def reduced_betti(faces):
    dims=sorted(faces)
    idx={k:{s:i for i,s in enumerate(sorted(faces[k]))} for k in dims}
    ranks={0:1}  # reduced boundary C_0 -> C_-1
    for k in dims:
        if k==0:continue
        lower=idx[k-1]
        cols=[]
        for s in sorted(faces[k]):
            c=0
            for i in range(s.bit_length()):
                if s>>i&1:c^=1<<lower[s^(1<<i)]
            cols.append(c)
        ranks[k]=rank2(cols)
    return {k:len(faces[k])-ranks[k]-ranks.get(k+1,0) for k in dims}


def pset(vertices):
    M=sum(1<<i for i in vertices)
    S=M;res=set()
    while S:
        res.add(S)
        S=(S-1)&M
    return res


def check_local_attachment(a,b):
    old,old_neigh=neighborhood_complex(a,b,False)
    new,new_neigh=neighborhood_complex(a,b,True)
    old_faces=set.union(set(),*old.values())
    new_faces=set.union(set(),*new.values())
    n=a+b-1; alpha=2;beta=a+1;w=0;y=1;z=a
    A=set(range(2,a));B=set(range(a+1,n))
    # Independent explicit five-family description of the old complex.
    TA=pset(A)
    TB=pset(B)
    for u in A: TA |= pset(({w,y}|A)-{u})
    for u in B: TB |= pset(({w,z}|B)-{u})
    claimed_old=TA|TB|pset(A|B)|pset(A|{z})|pset(B|{y})
    assert claimed_old==old_faces
    A0=set(range(2,a))-{alpha}
    B0=set(range(a+1,n))-{beta}
    EA=pset({w,y,beta}|A0)
    assert EA == pset(i for i in range(n) if (new_neigh[alpha] >> i) & 1)
    EB=pset({w,z,alpha}|B0)
    assert EB == pset(i for i in range(n) if (new_neigh[beta] >> i) & 1)
    assert new_faces == old_faces | EA | EB
    LA=EA & old_faces
    LB=EB & old_faces
    requiredA=pset({w,y}|A0)|pset({beta}|A0)|pset({beta,w})|pset({beta,y})
    requiredB=pset({w,z}|B0)|pset({alpha}|B0)|pset({alpha,w})|pset({alpha,z})
    assert LA==requiredA and LB==requiredB
    assert EA&EB==pset({w})
    return old,new


def main():
    records=0
    for a in range(5,8):
        for b in range(a,9):
            old,new=check_local_attachment(a,b)
            got_old={k:v for k,v in reduced_betti(old).items() if v}
            got_new={k:v for k,v in reduced_betti(new).items() if v}
            old_expected=defaultdict(int)
            old_expected[1]+=3
            old_expected[a-3]+=1;old_expected[b-3]+=1
            new_expected=defaultdict(int)
            new_expected[2]+=1
            new_expected[a-3]+=1;new_expected[b-3]+=1
            assert got_old==dict(old_expected),(a,b,'old',got_old,dict(old_expected))
            assert got_new==dict(new_expected),(a,b,'new',got_new,dict(new_expected))
            print(f'(a,b)=({a},{b}) old={got_old} new={got_new} local-attachment=PASS')
            records+=1
    # Relative attaching map in the basis (gamma_U,gamma_P,gamma_Q).
    matrix=[(1,0,0),(1,0,-1),(1,0,0),(1,-1,0)]
    def det3(v1,v2,v3):
        a,b,c=v1;d,e,f=v2;g,h,i=v3
        return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    minors=[det3(*triple) for triple in combinations(matrix,3)]
    assert any(abs(t)==1 for t in minors)
    print('attaching-map 3x3 unit minor:',minors,'PASS')
    print('finite checks:',records,'PASS')
if __name__=='__main__':main()
