from functools import lru_cache
from itertools import product

def partitions(n, low=1):
    if n == 0:
        yield ()
    else:
        for i in range(low,n+1):
            for rest in partitions(n-i,i):
                yield (i,)+rest

def graph(part):
    n=sum(part)
    f=[]; p=0
    for m in part:
        for j in range(m): f.append(p+((j+1)%m))
        p+=m
    return f

def sig(part,k):
    from collections import Counter
    c=Counter(part)
    if k==1:
        return (bool(c[1]),sum(m*a for m,a in c.items() if m>=2)>0)
    if k==2:
        return (min(c[1],2),min(c[2],2),0 if not any(m>=3 for m in c) else (1 if sum(c[m] for m in c if m>=3)==1 and c[3]==1 else 2))
    return tuple(sorted((m,min(a,k)) for m,a in c.items()))

def auto_colors(P,Q,k):
    graphs=[graph(P),graph(Q)]
    states=[]; infos=[]
    offsets=[]
    for b,f in enumerate(graphs):
        offsets.append(len(states))
        for t in product(range(len(f)),repeat=k):
            states.append((b,t))
            infos.append(tuple(int(t[i]==t[j]) for i in range(k) for j in range(k))+tuple(int(f[t[i]]==t[j]) for i in range(k) for j in range(k)))
    indices={st:i for i,st in enumerate(states)}
    M={v:i for i,v in enumerate(sorted(set(infos)))}
    colors=[M[x] for x in infos]
    for turn in range(50):
        new=[]
        for b,t in states:
            new.append((colors[indices[(b,t)]],)+tuple(tuple(sorted(set(colors[indices[(b,t[:j]+(a,)+t[j+1:])]] for a in range(len(graphs[b]))))) for j in range(k)))
        M={v:i for i,v in enumerate(sorted(set(new)))}
        newcolors=[M[x] for x in new]
        if newcolors==colors: break
        colors=newcolors
    a,b=offsets[1],len(states)
    return set(colors[:a])==set(colors[a:b]),turn+1

if __name__=='__main__':
  for k,maxn in [(1,7),(2,8),(3,6)]:
    pp=[p for n in range(1,maxn+1) for p in partitions(n)]
    ct=0; fail=[]; depth=0
    for i,p in enumerate(pp):
      for q in pp[i+1:]:
        got,d=auto_colors(p,q,k)
        exp=sig(p,k)==sig(q,k)
        ct+=1;depth=max(d,depth)
        if got!=exp:
          fail.append((p,q,got,exp));print('FAIL',k,fail[-1]);break
      if fail:break
    print('k',k,'p',len(pp),'comparisons',ct,'max_iteration',depth,'fails',len(fail))
