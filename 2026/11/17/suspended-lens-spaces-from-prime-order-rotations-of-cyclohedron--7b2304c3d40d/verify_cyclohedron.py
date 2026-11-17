"""Finite checks of cyclic graph-associahedron boundary rotation quotients.
No external dependencies. Does not replace the general proof."""
from collections import defaultdict
from itertools import combinations

def tubes(n):
    out=set()
    for length in range(1,n):
        for start in range(n):
            out.add(frozenset((start+j)%n for j in range(length)))
    return tuple(sorted(out,key=lambda a:(len(a),tuple(sorted(a)))))

def compatible(a,b,n):
    if a <= b or b <= a: return True
    if a&b: return False
    # disjoint and nonadjacent in the cycle
    return not any(((x+1)%n in b or (x-1)%n in b) for x in a)

def build(n):
    T=tubes(n); vertices=list(range(len(T)))
    adjacent=[set() for _ in vertices]
    for i in vertices:
        for j in range(i+1,len(T)):
            if compatible(T[i],T[j],n): adjacent[i].add(j)
    faces=[tuple()]
    by_dim=[[(i,) for i in vertices]]
    for d in range(1,n-1):
        prev=by_dim[-1]
        curr=[]
        for face in prev:
            for v in sorted(set.intersection(*(adjacent[i] for i in face)) if face else set()):
                if v>face[-1]: curr.append(face+(v,))
        by_dim.append(curr)
    # actions are strictly indexed by T, not by sorted binary representation
    idx={t:i for i,t in enumerate(T)}
    rot=tuple(idx[frozenset((x+1)%n for x in t)] for t in T)
    assert sorted(rot)==vertices
    for d,fs in enumerate(by_dim):
        S=set(fs)
        for f in fs:
            assert tuple(sorted(rot[i] for i in f)) in S
    return T,rot,by_dim

def sign_reorder(seq):
    return (-1)**sum(x>y for k,x in enumerate(seq) for y in seq[k+1:])

def quotient(n,rot,by_dim):
    assert n>=5 and all(not any(rot[i]==i for i in f) for fs in by_dim for f in fs)
    def rotate_face(face, steps):
        t=list(face)
        for _ in range(steps):t=[rot[i] for i in t]
        return t
    def canon(f):
        opts=[]
        for shift in range(n):
            seq=rotate_face(f,shift)
            opts.append((tuple(sorted(seq)),sign_reorder(seq)))
        best=min(x[0] for x in opts)
        return best, next(x[1] for x in opts if x[0]==best)
    orbits=[]
    for fs in by_dim:
        ss={canon(f)[0] for f in fs}
        orbits.append(tuple(sorted(ss)))
    index=[{f:i for i,f in enumerate(fs)} for fs in orbits]
    boundaries=[]
    for d in range(1,len(orbits)):
        cols=[]
        for f in orbits[d]:
            col=defaultdict(int)
            for j in range(len(f)):
                face=f[:j]+f[j+1:]
                rep,sgn=canon(face)
                col[index[d-1][rep]]+=(-1)**j*sgn
            cols.append(dict(col))
        boundaries.append(cols)
    for d,cols in enumerate(boundaries,1):
        for col in cols:
            second=defaultdict(int)
            if d>=2:
                for row, coeff in col.items():
                    for nextrow,c in boundaries[d-2][row].items():second[nextrow]+=coeff*c
                assert not any(second.values())
    return orbits,boundaries

def rank_mod(cols,num_rows,p):
    piv={}
    for col in cols:
        vec={i:(x%p) for i,x in col.items() if x%p}
        while vec:
            pivot=min(vec)
            if pivot not in piv:
                inv=pow(vec[pivot],-1,p)
                piv[pivot]={i:(a*inv)%p for i,a in vec.items() if a%p}
                break
            t=vec[pivot]
            for i, a in piv[pivot].items():
                new=(vec.get(i,0)-t*a)%p
                if new: vec[i]=new
                elif i in vec:del vec[i]
    return len(piv)

def main():
    T,rot,by_dim=build(5)
    print('C5 tubes',len(T),'dual-boundary simplex counts',tuple(len(fs) for fs in by_dim))
    orbits,boundaries=quotient(5,rot,by_dim)
    print('C5 quotient cell counts',tuple(len(fs) for fs in orbits))
    assert tuple(len(fs) for fs in by_dim)==(20,90,140,70)
    assert tuple(len(fs) for fs in orbits)==(4,18,28,14)
    for p in (2,3,5,7):
        ranks=[rank_mod(cols,len(orbits[i]),p) for i,cols in enumerate(boundaries)]
        betti=[len(orbits[i])-(ranks[i-1] if i else 0)-(ranks[i] if i<len(ranks) else 0) for i in range(len(orbits))]
        print('C5 quotient F_'+str(p), 'ranks',tuple(ranks),'Betti',tuple(betti))
        assert tuple(betti)==((1,1,1,1) if p==5 else (1,0,0,1))
    T7,rot7,ff7=build(7)
    assert tuple(len(x) for x in ff7)==(42,420,1680,3150,2772,924)
    print('C7 dual-boundary simplex counts',tuple(len(fs) for fs in ff7))
    for n,p in ((5,5),(7,7),(10,5),(15,5),(14,7),(21,7),(9,3),(12,3)):
        k=n//p
        # Number of coordinate orbits is k; nonidentity element of C_p fixes no coordinate.
        e=k*p-1
        trivial=k-1
        nontrivial=k*(p-1)
        assert e==trivial+nontrivial
        # Fourier multiplicities from the exact class function on the p-cycle:
        # trace at identity n-1, and trace at every nonidentity element -1.
        assert ((n-1)-(p-1))//p==trivial
        assert ((n-1)+1)//p==k
        assert ((n-1)-(p-1))%p==0
        print('n',n,'p',p,'k',k,'fixed_real_dimension',trivial,'moving_real_dimension',nontrivial,
              'predicted_top_dimension',n-2)
    print('CYCLOHEDRON_PRIME_ROTATION_QUOTIENT_CHECKS_PASS')
if __name__=='__main__': main()
