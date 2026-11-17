"""Build oriented barycentric quotient cellular chain complex of Petersen matching complex / A5."""
from itertools import combinations,permutations
from collections import defaultdict
from math import comb
from functools import lru_cache
from time import monotonic

def parity(p):
    return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2
V=list(combinations(range(5),2)); vi={v:i for i,v in enumerate(V)}
E=list((i,j) for i,j in combinations(range(10),2) if not set(V[i]).intersection(V[j]))
assert len(E)==15
E0={e:i for i,e in enumerate(E)}
groups=[]
for p in permutations(range(5)):
    if parity(p):continue
    mapv=[vi[tuple(sorted((p[a],p[b])))] for a,b in V]
    mape=[E0[tuple(sorted((mapv[i],mapv[j])))] for i,j in E]
    groups.append(tuple(mape))
assert len(groups)==60
faces_by_size=defaultdict(list)
for k in range(1,6):
    for combE in combinations(range(15),k):
        vertices=set()
        for ei in combE:vertices.update(E[ei])
        if len(vertices)==2*k:
            faces_by_size[k].append(sum(1<<e for e in combE))
faces=[f for layer in faces_by_size.values() for f in layer]
faceSet=set(faces)
print('faces count:',[len(faces_by_size[i]) for i in range(1,6)],'total',len(faces),flush=True)
# chains enumerated using all upward inclusions. Each face is an original barycentric vertex.
upper={a:[b for b in faces if (a!=b and a&b==a)] for a in faces}
chains=[[] for _ in range(5)]
def build(prefix):
    chains[len(prefix)-1].append(tuple(prefix))
    if len(prefix)==5: return
    for b in upper[prefix[-1]]:
        build(prefix+[b])
for a in faces:build([a])
print('barycentric chains:',[len(c) for c in chains],flush=True)

@lru_cache(maxsize=None)
def maskmap(f,grp):
    return sum((1<<grp[i]) for i in range(15) if f>>i &1)

def canon(chain):
    return min(tuple(maskmap(f,gid) for f in chain) for gid in groups)

orbit_index=[]; orbit_reps=[]
for dimension,cs in enumerate(chains):
    reps={canon(c) for c in cs}
    reps=sorted(reps)
    orbit_reps.append(reps)
    orbit_index.append({v:i for i,v in enumerate(reps)})
print('quotient cells:',[len(c) for c in orbit_reps],flush=True)

def differential(d):
    if d==0:return []
    ind=orbit_index[d-1]
    columns=[]
    for c in orbit_reps[d]:
        v=defaultdict(int)
        for j in range(len(c)):
            smaller=c[:j]+c[j+1:]
            key=canon(smaller)
            v[ind[key]]+=(-1)**j
        columns.append({k:n for k,n in v.items() if n})
    return columns
bounds=[[]]+[differential(d) for d in range(1,5)]

def rank_mod(columns,p):
    piv={}
    for col in columns:
        c={i:v%p for i,v in col.items() if v%p}
        while c:
            a=min(c)
            if a not in piv:
                div=pow(c[a],-1,p)
                piv[a]={j:(v*div)%p for j,v in c.items() if (v*div)%p}
                break
            f=c[a]
            for j,v in piv[a].items():
                w=(c.get(j,0)-f*v)%p
                if w:c[j]=w
                elif j in c:del c[j]
    return len(piv)

for d in range(2,5):
    for col in bounds[d]:
        check=defaultdict(int)
        for j,c in col.items():
            for k,v in bounds[d-1][j].items():check[k]+=c*v
        assert all(v==0 for v in check.values())
print('boundary-square-zero: PASS',flush=True)
for p in (2,3,5,7,1009):
    ranks=[0]+[rank_mod(bounds[d],p) for d in range(1,5)]+[0]
    betti=[len(orbit_reps[d])-ranks[d]-ranks[d+1] for d in range(5)]
    print('mod',p,'ranks',ranks,'betti',betti,flush=True)
def reduce_integer_complex(boundaries,counts):
    # Mutable sparse columns, cell IDs unchanged; eliminate integer unit pivot pairs
    B=[None]+[[dict(col) for col in bd] for bd in boundaries]
    alive=[set(range(a)) for a in counts]
    pivots=[]
    while True:
        best=None
        for d in range(1,len(counts)):
            row_cofaces=defaultdict(list)
            for j in alive[d]:
                for i,a in B[d][j].items():
                    if abs(a)==1 and i in alive[d-1]: row_cofaces[i].append(j)
            for i,js in row_cofaces.items():
                for j in js:
                    col=B[d][j]
                    nnz_row=sum(1 for k in alive[d] if i in B[d][k])
                    score=(len(col)-1)*(nnz_row-1)
                    key=(score,len(col)+nnz_row,d,i,j)
                    if best is None or key<best[0]:best=(key,d,i,j)
        if best is None:break
        _,d,i,j=best
        pivot=B[d][j][i]
        col_pivot=dict(B[d][j])
        for k in alive[d]:
            if k==j:continue
            a=B[d][k].get(i,0)
            if a:
                for row,val in col_pivot.items():
                    w=B[d][k].get(row,0)-a*val//pivot
                    if w:B[d][k][row]=w
                    else:B[d][k].pop(row,None)
        B[d][j]={}
        if d>1:B[d-1][i]={}
        if d<len(counts)-1:
            for col in B[d+1]:col.pop(j,None)
        alive[d].remove(j);alive[d-1].remove(i)
        pivots.append((d,i,j))
    print('integer unit cancellations',len(pivots),'remaining cells',[len(x) for x in alive],flush=True)
    remaining={str(d):{str(j):{str(i):a for i,a in B[d][j].items()} for j in sorted(alive[d]) if B[d][j]} for d in range(1,len(counts))}
    print('residual matrices',remaining,flush=True)
    return pivots,alive,remaining



def check_original_simple_connectivity():
    # Triangular presentation of pi_1 of the matching complex, after a spanning tree.
    es={tuple(i for i in range(15) if f & (1<<i)) for f in faces_by_size[2]}
    ts={tuple(i for i in range(15) if f & (1<<i)) for f in faces_by_size[3]}
    parent=list(range(15)); tree=set()
    def root(x):
        while parent[x]!=x:x=parent[x]
        return x
    for i,j in sorted(es):
        a,b=root(i),root(j)
        if a!=b:parent[a]=b;tree.add((i,j))
    assert len(tree)==14
    ids={e:i+1 for i,e in enumerate(sorted(es-tree))}
    assert len(ids)==61
    def letter(i,j):
        return (1 if i<j else -1)*ids.get(tuple(sorted((i,j))),0)
    def reduced(word):
        acc=[]
        for x in word:
            if not x:continue
            if acc and acc[-1]==-x:acc.pop()
            else:acc.append(x)
        return tuple(acc)
    def inverse(word):return tuple(-x for x in reversed(word))
    rels=[reduced((letter(a,b),letter(b,c),letter(c,a))) for a,b,c in sorted(ts)]
    assert len(rels)==145
    live=set(ids.values())
    eliminations=0
    while live:
        best=None
        for ri,r in enumerate(rels):
            for pos,c in enumerate(r):
                if sum(abs(x)==abs(c) for x in r)!=1:continue
                rest=r[pos+1:]+r[:pos]
                replacement=inverse(rest) if c>0 else rest
                key=(len(r),abs(c),ri)
                if best is None or key<best[0]:best=(key,ri,c,replacement)
        assert best is not None,'Uneliminated nontrivial fundamental-group presentation'
        _,ri,c,replacement=best
        g=abs(c)
        for k,R in enumerate(rels):
            if k==ri:continue
            new=[]
            for x in R:
                if abs(x)==g:new.extend(replacement if x*c>0 else inverse(replacement))
                else:new.append(x)
            rels[k]=reduced(new)
        rels.pop(ri)
        live.remove(g)
        eliminations+=1
    assert all(not r for r in rels)
    print('original pi_1: trivial by',eliminations,'exact generator eliminations')
    return eliminations

def check_fixed_3cycle():
    sigma=(1,2,0,3,4)
    vmap=[vi[tuple(sorted(sigma[a] for a in v))] for v in V]
    emap=tuple(E0[tuple(sorted((vmap[i],vmap[j])))] for i,j in E)
    fixed=[f for f in faces if maskmap(f,emap)==f]
    assert len(fixed)==4
    witness=(1<<0)|(1<<3)|(1<<6)
    assert witness in fixed and witness in faceSet
    print('fixed 3-cycle: four invariant matching simplices; witness edges',
          [[V[z] for z in E[i]] for i in range(15) if witness & (1<<i)])

if __name__=='__main__':
    counts=[len(x) for x in orbit_reps]
    assert len(groups)==60 and counts==[14,58,94,60,12]
    assert [len(faces_by_size[i]) for i in range(1,6)]==[15,75,145,90,6]
    assert [len(chains[i]) for i in range(5)]==[331,2460,5010,3600,720]
    pivots,alive,remaining=reduce_integer_complex(bounds[1:],counts)
    assert len(pivots)==118
    assert [len(x) for x in alive]==[1,0,1,0,0]
    assert all(not d for d in remaining.values())
    assert sum((-1)**i*n for i,n in enumerate(counts))==2
    check_original_simple_connectivity()
    check_fixed_3cycle()
    print('verified: quotient integral H_0=Z, H_2=Z, all other H_i=0')
    print('verified: quotient pi_1=1 by normal generation of A_5 by fixed 3-cycles')
    print('therefore the geometric quotient is homotopy equivalent to S^2')
