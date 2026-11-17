"""Exact simplicial, quotient-chain and fundamental-group checks for noncrossing matchings.
Python 3 standard library only. Run: python VERIFY.py
"""
import json
from collections import Counter, defaultdict, deque
from itertools import combinations


def reduced(word):
    word = list(word)
    out=[]
    for x in word:
        if out and out[-1] == -x: out.pop()
        else: out.append(x)
    while len(out)>1 and out[0] == -out[-1]: out=out[1:-1]
    return out


def compute(n, reflective):
    chords=list(combinations(range(n),2)); ci={c:i for i,c in enumerate(chords)}
    def crosses(a,b):
        i,j=a;k,l=b
        return i<k<j<l or k<i<l<j
    ok=lambda a,b: not(set(chords[a])&set(chords[b])) and not crosses(chords[a],chords[b])
    faces=[(i,) for i in range(len(chords))]
    for k in range(2,n//2+1):
        more=[]
        for f in faces:
            if len(f)!=k-1:continue
            for i in range(f[-1]+1,len(chords)):
                if all(ok(t,i) for t in f):more.append(f+(i,))
        faces+=more
    all_faces=set(faces)
    perms=[]
    for rot in range(n):
        for sign in ((1,-1) if reflective else (1,)):
            perm=tuple(ci[tuple(sorted(((rot+sign*i)%n,(rot+sign*j)%n)))] for i,j in chords)
            assert len(set(perm))==len(chords)
            perms.append(perm)
    # Include flags of the barycentric subdivision of every nonempty simplex.
    chains={0:[(f,) for f in faces]}
    for d in range(1,n//2):
        chains[d]=[(small,)+chain for chain in chains[d-1]
                   for size in range(1,len(chain[0]))
                   for small in combinations(chain[0],size)]
    flag_orbit={}; repdims={}
    for d in chains:
        for chain in chains[d]:
            if chain in flag_orbit:continue
            orbit={tuple(tuple(sorted(p[i] for i in f)) for f in chain) for p in perms}
            rep=min(orbit)
            for member in orbit:flag_orbit[member]=rep
            repdims[rep]=d
    nmax=max(chains)
    reps={d:sorted(c for c,dim in repdims.items() if dim==d) for d in range(nmax+1)}
    index={d:{c:i for i,c in enumerate(reps[d])} for d in reps}
    B={d:{} for d in range(1,nmax+1)}
    for d in B:
        for j,c in enumerate(reps[d]):
            col=defaultdict(int)
            for k in range(d+1):
                f=c[:k]+c[k+1:]
                col[index[d-1][flag_orbit[f]]]+=(-1)**k
            B[d][j]={i:v for i,v in col.items() if v}
    for d in range(2,nmax+1):
        for col in B[d].values():
            check=defaultdict(int)
            for i,v in col.items():
                for row,u in B[d-1][i].items():check[row]+=v*u
            assert all(z==0 for z in check.values())
    # Unit-pivot integer chain contraction: no division except by units +/-1.
    R={d:{j:dict(v) for j,v in B[d].items()} for d in B}
    active={d:set(range(len(reps[d]))) for d in reps}
    pivot_count=Counter()
    while True:
        pivot=None
        for d in sorted(R):
            for j in sorted(active[d]):
                for i,v in sorted(R[d].get(j,{}).items()):
                    if i in active[d-1] and abs(v)==1:
                        pivot=(d,i,j,v);break
                if pivot:break
            if pivot:break
        if not pivot:break
        d,i,j,v=pivot
        col=R[d][j]
        for k in sorted(active[d]-{j}):
            w=R[d][k].get(i,0)
            if w:
                cur=R[d][k]
                for rr,u in col.items():
                    if rr!=i:
                        z=cur.get(rr,0)-w*v*u
                        if z:cur[rr]=z
                        else:cur.pop(rr,None)
                cur.pop(i,None)
        for k in R[d]:R[d][k].pop(i,None)
        R[d].pop(j,None)
        if d+1 in R:
            for k in R[d+1]:R[d+1][k].pop(j,None)
        active[d].remove(j);active[d-1].remove(i);pivot_count[d]+=1
    remaining={str(d):len(x) for d,x in active.items()}
    boundary={str(d):sorted([abs(v) for j in active[d] for i,v in R[d].get(j,{}).items() if i in active[d-1]]) for d in R}
    # 2-skeleton relator verification of fundamental group presentation.
    fundamental=None
    if n==8:
        edges=[];adj=defaultdict(list)
        for j,chain in enumerate(reps[1]):
            a=index[0][flag_orbit[(chain[0],)]]
            b=index[0][flag_orbit[(chain[1],)]]
            assert B[1][j]==({a:-1,b:1} if a!=b else {}), (j,a,b,B[1][j])
            edges.append((a,b));adj[a].append((b,j));adj[b].append((a,j))
        visited={0};queue=deque([0]);tree=set()
        while queue:
            v=queue.popleft()
            for w,e in adj[v]:
                if w not in visited:
                    visited.add(w);queue.append(w);tree.add(e)
        assert len(visited)==len(reps[0]) and len(tree)==len(reps[0])-1
        others=sorted(set(range(len(edges)))-tree)
        generators={e:i+1 for i,e in enumerate(others)}
        relations=[]
        for ch in reps[2]:
            edge_cycles=[((ch[1],ch[2]),1),((ch[0],ch[2]),-1),((ch[0],ch[1]),1)]
            relations.append(reduced(sgn*generators[index[1][flag_orbit[e]]]
                                     for e,sgn in edge_cycles if index[1][flag_orbit[e]] in generators))
        free=set(generators.values());eliminations=0
        while True:
            options=[]
            for k,r in enumerate(relations):
                for x in set(map(abs,r)):
                    if sum(abs(t)==x for t in r)==1:
                        cost=(len(r)-1)*sum(any(abs(t)==x for t in s) for s in relations)
                        options.append((cost,len(r),k,x))
            if not options:break
            _,_,k,x=min(options)
            r=relations[k];pos=next(h for h,t in enumerate(r) if abs(t)==x)
            pre=r[:pos];post=r[pos+1:]
            rhs=[-a for a in reversed(pre)]+[-a for a in reversed(post)]
            if r[pos]<0:rhs=[-a for a in reversed(rhs)]
            new=[]
            for h,s in enumerate(relations):
                if h==k:continue
                word=[]
                for a in s:
                    if a==x:word+=rhs
                    elif a==-x:word += [-u for u in reversed(rhs)]
                    else:word.append(a)
                new.append(reduced(word))
            relations=new;free.remove(x);eliminations+=1
        nonempty=sorted([r for r in relations if r])
        fundamental={'initial_generators':len(generators), 'eliminations':eliminations,
                     'remaining_generators':len(free),
                     'remaining_relations':nonempty}
        if reflective:
            assert not free and not nonempty
        else:
            assert len(free)==1 and len(nonempty)==3
            assert all(len(r)==2 and r[0]==r[1] and abs(r[0]) in free for r in nonempty)
    out={'n':n,'group':'dihedral' if reflective else 'cyclic',
         'face_counts':dict(sorted(Counter(map(len,faces)).items())),
         'cell_counts':{str(d):len(a) for d,a in reps.items()},
         'unit_cancellations':dict(sorted(pivot_count.items())),
         'reduced_cells':remaining,'reduced_boundary_abs':boundary}
    if fundamental is not None:out['pi1_presentation']=fundamental
    return out


def main():
    data=[compute(n,False) for n in range(4,9)]+[compute(8,True)]
    assert data[4]['cell_counts']=={'0':45,'1':169,'2':168,'3':42}
    assert data[4]['reduced_cells']=={'0':1,'1':1,'2':2,'3':0}
    assert data[4]['reduced_boundary_abs']=={'1':[],'2':[2],'3':[]}
    assert data[5]['cell_counts']=={'0':35,'1':112,'2':105,'3':27}
    assert data[5]['reduced_cells']=={'0':1,'1':0,'2':0,'3':0}
    for x in data[:4]:
        assert all(not v for v in x['reduced_boundary_abs'].values()),x
    print(json.dumps(data,sort_keys=True,separators=(',',':')))
    print('VERIFY_OK')

if __name__=='__main__':main()
