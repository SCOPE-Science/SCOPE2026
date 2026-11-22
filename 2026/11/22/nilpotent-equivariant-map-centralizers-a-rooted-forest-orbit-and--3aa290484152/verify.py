#!/usr/bin/env python3
"""Independent finite checks of nilpotent equivariant-map commutants."""
from itertools import product,permutations
from collections import Counter,defaultdict
from functools import lru_cache
from math import factorial,comb

def isforest(p):
    n=len(p)
    for i in range(1,n+1):
        seen=set(); v=i
        while v:
            if v in seen:return False
            seen.add(v);v=p[v-1]
    return True

def forest_shape(p):
    n=len(p); children=[[] for _ in range(n+1)]
    for v,par in enumerate(p,1):children[par].append(v)
    def code(v):return '('+''.join(sorted(code(x) for x in children[v]))+')'
    return ''.join(sorted(code(v) for v in children[0]))

def centralizer_recursion(p,q):
    n=len(p);children=[[] for _ in range(n+1)]
    for v,par in enumerate(p,1):children[par].append(v)
    roots=children[0]
    @lru_cache(None)
    def h(v,w):
        if w==0:
            result=1
            for c in children[v]:result*=h(c,0)+q*sum(h(c,u) for u in roots)
            return result
        result=1
        for c in children[v]:result*=sum(h(c,u) for u in children[w])
        return result
    total=1
    for v in roots:total*=h(v,0)+q*sum(h(v,w) for w in roots)
    return total

def abelian_group(q):
    return list(range(q)), lambda a,b:(a+b)%q, 0

def s3_group():
    items=list(permutations(range(3)))
    id_of={a:i for i,a in enumerate(items)}
    mul=lambda a,b:id_of[tuple(items[a][items[b][j]] for j in range(3))]
    return list(range(6)),mul,id_of[(0,1,2)]

def brute_centralizer(p,group):
    elements,mul,e=group;n=len(p);q=len(elements)
    def f_of(i,a):return (0,None) if p[i-1]==0 else (p[i-1],a)
    def g_of(i,a,targets,phases):
        j=targets[i-1]
        return (0,None) if j==0 else (j,mul(a,phases[i-1]))
    count=0
    for tg in product(range(n+1),repeat=n):
        nz=[i for i,j in enumerate(tg) if j]
        for phases_nonzero in product(elements,repeat=len(nz)):
            phases=[e]*n
            for idx,g in zip(nz,phases_nonzero):phases[idx]=g
            okay=True
            for i in range(1,n+1):
                j,b=g_of(i,e,tg,phases)
                fg=(0,None) if j==0 else f_of(j,b)
                j,b=f_of(i,e)
                gf=(0,None) if j==0 else g_of(j,b,tg,phases)
                if fg!=gf:okay=False;break
            if okay:count+=1
    return count

def predicted_orbit_size(p,q):
    n=len(p)
    aut=0
    for pi in permutations(range(1,n+1)):
        perm=(0,)+pi
        if all(perm[p[i-1]]==p[perm[i]-1] for i in range(1,n+1)):
            aut+=1
    return factorial(n)*q**(n-p.count(0))//aut

def brute_conjugacy_orbit(p,group):
    elems,mul,e=group;n=len(p)
    inverses={a:next(b for b in elems if mul(a,b)==e and mul(b,a)==e) for a in elems}
    seen=set()
    for pi0 in permutations(range(1,n+1)):
        pi=(0,)+pi0
        inverse_pi=[0]*(n+1)
        for i in range(1,n+1):inverse_pi[pi[i]]=i
        for phases in product(elems,repeat=n):
            targets=[];outphases=[]
            for i in range(1,n+1):
                j=inverse_pi[i]
                k=p[j-1]
                targets.append(pi[k])
                outphases.append(-1 if k==0 else mul(inverses[phases[j-1]],phases[k-1]))
            seen.add((tuple(targets),tuple(outphases)))
    return len(seen)

def direct_nilpotent_count(b,q):
    s=0;by_root=Counter();shapes=defaultdict(int)
    for p in product(range(b+1),repeat=b):
        if isforest(p):
            roots=p.count(0);weight=q**(b-roots);s+=weight;by_root[roots]+=weight
            shapes[forest_shape(p)]+=weight
    return s,by_root,shapes

def main():
    for b in range(1,6):
        for q in (1,2,3,6):
            total,by_root,shapes=direct_nilpotent_count(b,q)
            assert total==(1+b*q)**(b-1),(b,q,total)
            for k in range(1,b+1):
                assert by_root[k]==comb(b-1,k-1)*(b*q)**(b-k)
            print('FOREST_COUNT',b,q,total,len(shapes))
    for group,name,maxn in [(abelian_group(2),'C2',4),(abelian_group(3),'C3',3),(abelian_group(6),'C6',3),(s3_group(),'S3',3)]:
        q=len(group[0])
        for b in range(1,maxn+1):
            reps={}
            for p in product(range(b+1),repeat=b):
                if isforest(p):reps.setdefault(forest_shape(p),p)
            for shape,p in reps.items():
                a=centralizer_recursion(p,q)
                z=brute_centralizer(p,group)
                assert a==z,(name,b,shape,p,a,z)
                if b<=3:
                    orbit=brute_conjugacy_orbit(p,group)
                    assert orbit==predicted_orbit_size(p,q),(name,b,shape,orbit,predicted_orbit_size(p,q))
            print('CENTRALIZER_CHECK',name,b,len(reps))
    print('NILPOTENT_POINTED_GSET_CENTRALIZERS_PASSED')

if __name__=='__main__':main()
