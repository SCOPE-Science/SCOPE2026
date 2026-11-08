import itertools, math
from collections import defaultdict

# This standalone check constructs the orbit-barycenter fixed triangulation.
def orbits_parts(part_sizes, gens):
    N=sum(part_sizes); parent=list(range(N))
    def root(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]];x=parent[x]
        return x
    def union(a,b):
        a=root(a);b=root(b);parent[a]=b
    for g in gens:
        assert sorted(g)==list(range(N))
        for x,y in enumerate(g):union(x,y)
    groups=defaultdict(list)
    for x in range(N):groups[root(x)].append(x)
    return sorted(map(tuple,groups.values()),key=lambda a:min(a))

def all_faces(part_sizes,orbit_blocks):
    ix=[]
    for i,n in enumerate(part_sizes):ix.extend([i]*n)
    sizes=len(orbit_blocks)
    N=len(ix)
    # Generate closed neighborhoods directly from graph adjacency, independently
    # of the predicted multipartite support criterion.
    closed=[{v}|{w for w in range(N) if ix[v]!=ix[w]} for v in range(N)]
    face={}
    for mask in range(1,1<<sizes):
        totals=[0]*len(part_sizes)
        for j,b in enumerate(orbit_blocks):
            if mask>>j&1:
                for v in b:totals[ix[v]]+=1
        union={v for j,b in enumerate(orbit_blocks) if mask>>j&1 for v in b}
        geometric=any(union<=nv for nv in closed)
        assert geometric==(min(totals)<=1)
        if geometric:
            d=mask.bit_count()-1;face.setdefault(d,[]).append(mask)
    return face

def gf2_rank(cols):
    basis={}
    for x in cols:
        while x:
            k=x.bit_length()-1
            if k in basis:x^=basis[k]
            else:basis[k]=x;break
    return len(basis)

def homology_mod2(faces):
    maxd=max(faces,default=-1)
    rank=[]
    for d in range(1,maxd+1):
        prev={a:i for i,a in enumerate(faces.get(d-1,[]))}
        cols=[]
        for face in faces.get(d,[]):
            col=0;b=face
            while b:
                lsb=b&-b;b-=lsb
                col^=1<<prev[face^lsb]
            cols.append(col)
        rank.append(gf2_rank(cols))
    betti={}
    for d in range(maxd+1):
        value=len(faces[d])-(rank[d-1] if d else 0)-(rank[d] if d<len(rank) else 0)
        if d==0:value-=1
        if value:betti[d]=value
    return betti

def prediction(part_sizes,orbits):
    pos=0; f=[]
    for n in part_sizes:
        f.append(sum(len(b)==1 and pos<=b[0]<pos+n for b in orbits))
        pos+=n
    k=len(f);r=sum(t>0 for t in f)
    if any(t==1 for t in f):return {},f
    return {k+r-2:math.prod(t-1 for t in f if t>0)}, f

def perm_from_cycles(part_sizes, cycles):
    N=sum(part_sizes); p=list(range(N))
    for c in cycles:
        for a,b in zip(c,c[1:]+c[:1]):p[a]=b
    return p

def check_case(ns,generators):
    orbs=orbits_parts(ns,generators); face=all_faces(ns,orbs)
    pred,f=prediction(ns,orbs)
    got=homology_mod2(face)
    if got!=pred:raise AssertionError((ns,generators,orbs,f,pred,got))
    return len(orbs),sum(map(len,face.values())),f,got

def main():
    cases=[]
    for ns in [(2,2),(2,3),(3,3),(2,2,2),(3,2,2),(3,3,2),(2,2,2,2),(3,3,3),(4,3,2),(3,3,3,2)]:
        N=sum(ns)
        cycles=[];pos=0
        for n in ns:
            if n>1:
                cycles.append([pos,pos+1])
                if n>2:cycles.append(list(range(pos,pos+n)))
            pos+=n
        ident=list(range(N))
        per=[perm_from_cycles(ns,[c]) for c in cycles]
        test=[[],[ident]]+[[x] for x in per]+[[x,y] for x,y in itertools.combinations(per,2)]
        if len(per)>=3:test.extend([list(q) for q in itertools.combinations(per,3)])
        for gens in test:
            rec=check_case(ns,gens)
            cases.append((ns,rec))
    print('PARAMETER/SUBGROUP CASES:',len(cases))
    for ns in sorted(set(n for n,_ in cases),key=lambda x:(len(x),x)):
        rows=[r for n,r in cases if n==ns]
        types=set(tuple(sorted(r[-1].items())) for r in rows)
        print('parts',ns,'checks',len(rows),'distinct reduced Betti profiles',len(types),'max faces',max(r[1] for r in rows))
    print('ALL_VERIFY_OK')
if __name__=='__main__':main()
