from itertools import product
from collections import defaultdict,Counter,deque
from math import comb

def graph(sizes):
    d=1+sum(sizes)
    N=2*d
    adj=[0]*N
    def edge(a,b):
        adj[a]|=1<<b;adj[b]|=1<<a
    for j in range(d):edge(j,d+j)
    pos=1;petals=[]
    for r in sizes:
        cells=list(range(pos,pos+r));pos+=r
        petals.append(cells+[d+x for x in cells])
        for layer in (0,d):
            for a in cells:edge(layer,layer+a)
            for ix,a in enumerate(cells):
                for b in cells[ix+1:]:edge(layer+a,layer+b)
    return adj,petals,d

def power(adj,s):
    n=len(adj); full=(1<<n)-1
    blue=s
    for v in range(n):
        if (s>>v)&1:blue|=adj[v]
    while blue!=full:
        old=blue
        for v in range(n):
            if (blue>>v)&1:
                white=adj[v]&~blue
                if white and not white&(white-1):blue|=white
        if old==blue:break
    return blue==full

def predicate(s,petals,d):
    return bool(s&((1<<0)|(1<<d))) or all(any((s>>v)&1 for v in pp) for pp in petals)

def run(sizes,do_tar=True):
    adj,petals,d=graph(sizes);N=len(adj);good=[];scores=Counter()
    for s in range(1<<N):
        p=power(adj,s);q=predicate(s,petals,d)
        assert p==q,('WRONG',sizes,s,p,q)
        if p:
            good.append(s);scores[s.bit_count()]+=1
    k=len(sizes)
    theory=Counter()
    for t in range(N+1):
        a=(2*comb(N-2,t-1) if t>=1 and t-1<=N-2 else 0)+(comb(N-2,t-2) if t>=2 and t-2<=N-2 else 0)
        b=[1]
        for r in sizes:
            p=[comb(2*r,i) for i in range(1,2*r+1)]
            c=[0]*(len(b)+len(p))
            for i,x in enumerate(b):
                for j,y in enumerate(p):c[i+j+1]+=x*y
            b=c
        theory[t]=a+(b[t] if t<len(b) else 0)
    assert all(theory[t]==scores[t] for t in range(N+1)),(sizes,scores,theory)
    goodset=set(good)
    mins=[s for s in good if not any((s^(1<<v)) in goodset for v in range(N) if s>>v&1)]
    expected=Counter({1:2,k:__import__('math').prod(2*r for r in sizes)})
    if k==1:expected=Counter({1:2+2*sizes[0]})
    assert Counter(s.bit_count() for s in mins)==expected,(sizes,Counter(s.bit_count() for s in mins),expected)
    print('TEST_OK',sizes,'n',N,'all',len(good),'minimal',len(mins))
    if do_tar:
        for budget in range(1,min(N,k+2)+1):
            live=set(s for s in good if s.bit_count()<=budget)
            cc=[]
            while live:
                first=live.pop();q=deque([first]);count=1
                while q:
                    s=q.popleft()
                    for v in range(N):
                        t=s^(1<<v)
                        if t in live and t.bit_count()<=budget:
                            live.remove(t);q.append(t);count+=1
                cc.append(count)
            cc.sort(reverse=True)
            if budget==1:target=[1,1] if k>=2 else [1]*(2+2*sizes[0])
            elif 2<=budget<k:target=[len([s for s in good if s.bit_count()<=budget])]
            elif budget==k:target=[len([s for s in good if (s&((1<<0)|(1<<d))) and s.bit_count()<=budget])]+[1]*__import__('math').prod(2*r for r in sizes)
            else:target=[len([s for s in good if s.bit_count()<=budget])]
            target.sort(reverse=True)
            assert cc==target,(sizes,budget,cc[:10],target[:10]);
            print('TAR_OK',sizes,budget,len(cc),cc[:3])
for s in ([2],[3],[2,2],[2,3],[2,2,2],[2,2,3],[2,2,2,2]):run(s)
print('VERIFY_OK')
