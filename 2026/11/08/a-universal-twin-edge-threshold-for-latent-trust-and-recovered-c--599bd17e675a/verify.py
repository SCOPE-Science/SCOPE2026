"""Exact-rational checks for twin-edge activation in adaptive-confidence HK dynamics."""
from fractions import Fraction as F
from itertools import combinations
import random


def update(n, edges, x, cvals, gamma, delta):
    active = {e for e in edges if abs(x[e[0]]-x[e[1]]) < cvals[e]}
    nxt = []
    for i in range(n):
        neighbors = [i]
        neighbors += [v if u == i else u for u,v in active if u == i or v == i]
        nxt.append(sum((x[j] for j in neighbors), F(0)) / len(neighbors))
    cn = {e:(cvals[e]+gamma*(1-cvals[e]) if e in active else delta*cvals[e]) for e in edges}
    return nxt,cn,active


def trial(n, d, extra_edges, epsvec, delta, gamma=F(1,4), c=F(3,5), a=F(2,5)):
    assert d >= 1 and d <= n-2
    S = range(2,2+d)
    H = {tuple(sorted((u,v))) for w in S for u,v in ((0,w),(1,w))}
    H |= {tuple(sorted(e)) for e in extra_edges}
    all_edges = H | {(0,1)}
    X = [F(1,2)+a,F(1,2)-a]+[F(1,2)]*(n-2)
    X = [v+e for v,e in zip(X,epsvec)]
    D = X[0]-X[1]
    rho = F(1,d+1)
    assert D>c and all(abs(X[u]-X[v])<c for u,v in H)
    C={e:c for e in all_edges}
    eps=max(abs(v) for v in epsvec)
    assert 2*eps < min(c-a, gamma,2*a-c)
    first = None
    checks = 3
    for t in range(34):
        active_expected = D*rho**t < c*delta**t if delta>rho else False
        Xnew,Cnew,act = update(n,all_edges,X,C,gamma,delta)
        if first is None:
            assert H <= act, ('lost initially active edge',n,d,t)
            assert ((0,1) in act)==active_expected, ('wrong activation',n,d,t)
            assert X[0]-X[1] == D*rho**t, ('wrong antisym mode',n,d,t)
            checks+=3
            if (0,1) in act:
                first=t
        elif first is not None:
            assert len(act)==len(all_edges), ('failed to stay fully receptive',n,d,t)
            checks+=1
        X,C=Xnew,Cnew
    assert (first is None) == (delta<=rho)
    checks+=1
    if delta>rho:
        predicted=0
        while D*rho**predicted >= c*delta**predicted:
            predicted+=1
        assert first==predicted, ('first-passage mismatch',first,predicted)
        checks+=1
    return checks,first


def main():
    rng = random.Random(16421)
    checks=0
    examples=[]
    for n in range(3,10):
      for d in range(1,n-1):
        # Only extra edges incident to members of S or within the outside part,
        # and every outside vertex is connected to S, keeping both endpoints twins.
        for case in range(5):
          S=list(range(2,2+d))
          outside=list(range(2+d,n))
          E=set()
          for w in outside:
             E.add(tuple(sorted((w,rng.choice(S)))))
          for u,v in combinations(range(2,n),2):
             if rng.random()<0.3: E.add((u,v))
          epsilon=F(1,100)
          eta=[F(rng.randint(-4,4),400) for _ in range(n)]
          rho=F(1,d+1)
          for delta in [F(0),rho/2,rho,(rho+1)/2,F(9,10)]:
             count, first = trial(n,d,E,eta,delta)
             checks+=count
             if n in (3,7) and case==0 and d in (1,n-2):
                examples.append((n,d,str(delta),first))
    # With n=3, D/c=4/3 and delta/rho=4/3, the time-one
    # equality is nonreceptive; activation occurs at time two.
    checks_eq, time_eq=trial(3,1,set(),[F(0)]*3,F(2,3))
    assert time_eq==2
    checks+=checks_eq+1
    # Critical slowing down near the forgetting/mixing boundary.
    checks_close, time_close=trial(3,1,set(),[F(0)]*3,F(101,200))
    assert time_close==29
    checks+=checks_close+1
    print('PASS', checks, 'exact-rational step assertions')
    print('illustrations', examples[:16])


if __name__=='__main__': main()
