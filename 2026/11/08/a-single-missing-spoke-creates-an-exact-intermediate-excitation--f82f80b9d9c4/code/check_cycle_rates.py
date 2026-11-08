"""Independent cycle-mean checks of the three-phase missing-spoke theorem."""
from itertools import product
from fractions import Fraction

def adj(n):
    G=[set() for _ in range(n+1)]
    for i in range(1,n+1):
        j=1+i%n;G[i].add(j);G[j].add(i)
        if i!=1:G[0].add(i);G[i].add(0)
    return G

def simple_cycles(A):
    cycles=set()
    N=len(A)
    for root in range(N):
        stack=[(root,[root])]
        while stack:
            u,p=stack.pop()
            for v in A[u]:
                if v==root and len(p)>=3:
                    if p[1]<p[-1]:cycles.add(tuple(p))
                elif v>root and v not in p:
                    stack.append((v,p+[v]))
    return sorted(cycles)

def incr(a,b):
    if a==b:return 0
    return 1 if (b-a)%3==1 else -1

def predicted(s,n):
    # source independent of transfer matrix; inspect each triangle and quadrilateral directly
    x=s[0]
    if any(len({x,s[i],s[i+1]})==3 for i in range(2,n)):return Fraction(1)
    four=(0,2,1,n)
    w=sum(incr(s[four[j]],s[four[(j+1)%4]]) for j in range(4))
    return Fraction(3,4) if w else Fraction(0)

for n in range(4,9):
    A=adj(n); cycs=simple_cycles(A);counts={}
    for s in product(range(3),repeat=n+1):
        actual=max([Fraction(abs(sum(incr(s[c[j]],s[c[(j+1)%len(c)]]) for j in range(len(c)))),len(c)) for c in cycs]+[Fraction(0)])
        exp=predicted(s,n)
        assert actual==exp,(n,s,actual,exp)
        counts[actual]=counts.get(actual,0)+1
    print('n',n,'simple_cycles',len(cycs),'activity_populations',dict(sorted(counts.items())))
print('PASS independent directed cycle maxima through n=8')
