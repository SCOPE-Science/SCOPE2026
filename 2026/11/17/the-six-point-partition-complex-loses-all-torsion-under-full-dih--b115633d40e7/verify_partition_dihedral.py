"""Exact integral chain contraction for the six-point dihedral partition quotient.

Run: python verify_partition_dihedral.py
Only Python's standard library is required.
"""
from itertools import combinations
from collections import defaultdict

N=6

def set_partitions(elements):
    if not elements:
        yield ()
        return
    first,*rest=elements
    for p in set_partitions(rest):
        yield (frozenset((first,)),)+p
        for i in range(len(p)):
            yield p[:i]+(p[i]|{first},)+p[i+1:]

def canon(p):
    return tuple(sorted(tuple(sorted(b)) for b in p))

def refines(a,b):
    return all(any(set(x).issubset(y) for y in b) for x in a)

P=sorted({canon(p) for p in set_partitions(list(range(N))) if 1<len(p)<N},key=lambda x:(-len(x),x))
D=sorted(set(tuple((s*i+j)%N for i in range(N)) for s in (1,-1) for j in range(N)))

def transform(part,perm):
    return canon(tuple(tuple(perm[v] for v in block) for block in part))

def act(chain,perm):
    return tuple(transform(part,perm) for part in chain)

def orbit(chain):
    return min(act(chain,perm) for perm in D)

chains_by_dim={0: [(p,) for p in P]}
for d in range(1,N-2):
    chains_by_dim[d]=[c+(q,) for c in chains_by_dim[d-1] for q in P
                 if 1<len(q)<len(c[-1]) and refines(c[-1],q)]
C={d: sorted({orbit(chain) for chain in chains}) for d,chains in chains_by_dim.items()}
index={d:{chain:i for i,chain in enumerate(C[d])} for d in C}
# An independent orbit-count audit via Burnside's lemma.
for d,chains in chains_by_dim.items():
    fixed=sum(sum(act(chain,g)==chain for chain in chains) for g in D)
    assert fixed == len(D)*len(C[d]),(d,fixed)
B={}
for d in range(1,N-2):
    cols={}
    for j,c in enumerate(C[d]):
        out={}
        for i in range(len(c)):
            f=orbit(c[:i]+c[i+1:])
            r=index[d-1][f]
            out[r]=out.get(r,0)+(-1)**i
        cols[j]={r:v for r,v in out.items() if v}
    B[d]=cols

# Chain identity on original matrices, with integer coefficients.
for d in range(2,N-2):
    for col in B[d].values():
        ans=defaultdict(int)
        for i,a in col.items():
            for j,b in B[d-1][i].items():ans[j]+=a*b
        assert all(v==0 for v in ans.values())

original_counts=tuple(len(C[d]) for d in range(N-2))
assert original_counts==(35,215,419,250)

# Active generators in each degree. Each cancellation is an integral basis
# change followed by deletion of a contractible two-generator summand.
active={d:set(range(len(C[d]))) for d in C}


def eliminate(d):
    M=B[d]
    steps=0
    while True:
        row_entries=defaultdict(set)
        for j,col in M.items():
            for i,v in col.items():
                if v: row_entries[i].add(j)
        # Pick an exact unit pivot, minimizing potential fill-in.
        best=None
        for j,col in M.items():
            for i,v in col.items():
                if abs(v)==1:
                    score=((len(row_entries[i])-1)*(len(col)-1),len(col)+len(row_entries[i]),i,j)
                    if best is None or score<best[0]:best=(score,i,j,v)
        if best is None:break
        _,r,c,u=best
        pivot=M[c].copy()
        for j in list(row_entries[r]):
            if j==c:continue
            col=M[j]
            a=col.get(r,0)//u
            for i,v in pivot.items():
                q=col.get(i,0)-a*v
                if q:col[i]=q
                else:col.pop(i,None)
        del M[c]
        assert r in active[d-1] and c in active[d]
        active[d-1].remove(r)
        active[d].remove(c)
        if d-1 in B:
            B[d-1].pop(r,None)
        if d+1 in B:
            for col in B[d+1].values():col.pop(c,None)
        steps+=1
    return steps

steps={d:eliminate(d) for d in range(1,N-2)}
remaining={d:len(v) for d,v in active.items()}
nonzero={d:sum(len(c) for c in mat.values()) for d,mat in B.items()}
print('partitions:',len(P),'dihedral order:',len(D))
print('cell counts degrees 0..3:',original_counts)
print('Burnside orbit counts: verified')
print('initial boundary-square identities: zero')
print('integral unit cancellations by boundary degree:',steps)
print('remaining chain group ranks:',remaining)
print('remaining nonzero boundary entries:',nonzero)
assert steps=={1:34,2:181,3:238},steps
assert remaining=={0:1,1:0,2:0,3:12}
assert all(v==0 for v in nonzero.values())
print('integral homology: H0=Z, H1=H2=0, H3=Z^12')
