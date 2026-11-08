"""Standard-library independent source-resolved theta census checker."""
from itertools import product
from collections import Counter

def polynomial(Ls):
    ans=Counter()
    for d in range(3):
        pol={(0,0):1}
        for L in Ls:
            all_words=[(-1,)*a+(1,)*(L-a) for a in range(L+1)]
            all_words +=[(-1,)*a+(0,)+(1,)*(L-1-a) for a in range(L)]
            c=sum(sum(w)%3==d for w in all_words)
            p=int(L%3==d);q=int((-L)%3==d)
            term=[((0,0),c-p-q),((1,0),p),((0,1),q)]
            new=Counter()
            for (a,b),v in pol.items():
                for (x,y),w in term:
                    new[(a+x,b+y)]+=v*w
            pol=new
        for (a,b),v in pol.items():
            if a>=1 and b>=1:ans[(a,b)]+=3*v
    return +ans

def adjacency(Ls):
    adj=[set(),set()]
    chains=[]
    for L in Ls:
        path=[0]
        for k in range(L-1):path.append(len(adj));adj.append(set())
        path.append(1)
        for a,b in zip(path,path[1:]):adj[a].add(b);adj[b].add(a)
        chains.append(path)
    return adj,chains

def brute(Ls):
    adj,chains=adjacency(Ls)
    counts=Counter()
    for colors in product(range(3),repeat=len(adj)):
        if not all(any(colors[b]==(colors[a]+1)%3 for b in adj[a]) for a in range(len(adj))):continue
        plus=sum(colors[p[1]]==(colors[p[0]]+1)%3 for p in chains)
        minus=sum(colors[p[-2]]==(colors[p[-1]]+1)%3 for p in chains)
        counts[plus,minus]+=1
    return +counts

if __name__=='__main__':
    cases=0; states=0
    for m in (3,4):
        for Ls in product(range(2,6),repeat=m):
            N=2+sum(L-1 for L in Ls)
            if N>10:continue
            a=polynomial(Ls);b=brute(Ls)
            assert a==b,(Ls,a,b)
            cases+=1;states+=3**N
    print('source_resolved_cases=',cases,'colorings_enumerated=',states)
    for Ls in ((2,4,2),(3,3,3),(3,3,3,3),(2,3,4),(3,4,5),(2,2,2)):
        print(Ls,'coefficients=',sorted(polynomial(Ls).items()))
    for m in range(3,10):
        for h in range(1,8):
            a=2*h+1
            expected=3*(a**m-2*(a-1)**m+(a-2)**m)
            got=sum(polynomial((3*h,)*m).values())
            assert got==expected,(m,h,expected,got)
    print('equilateral_identity_cases=',7*7)
