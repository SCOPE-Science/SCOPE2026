"""Finite checks for the mesoscopic bipartite bond-percolation limit.

Only finite arithmetic identities are tested here; the limiting theorem
is established by the separate multinomial characteristic-function proof.
"""
import itertools
import math
from fractions import Fraction

checks=0

def require(cond, msg):
    global checks
    checks+=1
    if not cond:
        raise AssertionError(msg)

def component_from_patterns(patterns,r):
    parent=list(range(r))
    def find(x):
        while parent[x]!=x: x=parent[x]
        return x
    for bit in patterns:
        active=[i for i in range(r) if bit>>i & 1]
        for i in active[1:]:parent[find(i)]=find(active[0])
    comp={i for i in range(r) if find(i)==find(0)}
    q=sum(any((bit>>i)&1 for i in comp) for bit in patterns)
    return len(comp),q

def exact(n,p):
    r=len(p)
    out={}
    pattern_probs=[]
    for pattern in range(1<<r):
        prob=Fraction(1)
        for i in range(r):prob*=p[i] if (pattern>>i)&1 else (1-p[i])
        pattern_probs.append(prob)
    for patterns in itertools.product(range(1<<r),repeat=n):
        pr=math.prod(pattern_probs[t] for t in patterns)
        stat=component_from_patterns(patterns,r)
        out[stat]=out.get(stat,Fraction(0))+pr
    return out

for p in [(Fraction(1,4),)*3,(Fraction(1,3),Fraction(2,5),Fraction(1,2)),(Fraction(1,2),Fraction(1,3),Fraction(1,5))]:
    a,b,c=p
    no_pair=1-a*b-a*c-b*c+2*a*b*c
    for n in range(1,5):
        d=exact(n,p)
        require(sum(d.values())==1,(n,p,'normalization'))
        ps1=sum(pr for (s,q),pr in d.items() if s==1)
        ex1=(1-a*(b+c-b*c))**n
        require(ps1==ex1,(n,p,'isolated hub',ps1,ex1))
        ps2=sum(pr for (s,q),pr in d.items() if s==2)
        ex2=(1-b*(a+c-a*c))**n+(1-c*(a+b-a*b))**n-2*no_pair**n
        require(ps2==ex2,(n,p,'two hubs',ps2,ex2))
        ps3=1-ps1-ps2
        require(ps3==sum(pr for (s,q),pr in d.items() if s==3),(n,p,'three hubs'))
        require(all(0<=q<=n for (s,q) in d), (n,p,'ordinary bounds'))

# Pair-category probability and rare-triple bounds, in exact arithmetic.
for p in [(Fraction(1,3),)*3,(Fraction(1,4),Fraction(2,5),Fraction(1,2))]:
    a,b,c=p
    q12=a*b*(1-c);q13=a*c*(1-b);q23=b*c*(1-a)
    triple=a*b*c
    require(q12+q13+q23+triple == a*b+a*c+b*c-2*a*b*c,'pair decomposition')
    for k in range(2,10):
        n=k*k*k*k
        alpha=[float(x)*k*k for x in p] # same probabilities recomputed n^(1/2) parameters
        require(abs(n*float(q12)-alpha[0]*alpha[1]*(1-float(c)))<1e-8, 'Poisson parameter identity')

# Deterministic convergence of exact cluster probabilities to inhomogeneous ER.
for aa in [(0.7,0.9,1.15),(1.0,1.0,1.0)]:
    for n in (1000,10000,100000):
        a,b,c=[x/math.sqrt(n) for x in aa]
        p1=(1-a*(b+c-b*c))**n
        p2=(1-b*(a+c-a*c))**n+(1-c*(a+b-a*b))**n-2*(1-a*b-a*c-b*c+2*a*b*c)**n
        u=math.exp(-aa[0]*aa[1]);v=math.exp(-aa[0]*aa[2]);w=math.exp(-aa[1]*aa[2])
        limit1=u*v
        limit2=(1-u)*v*w+(1-v)*u*w
        require(abs(p1-limit1)<7/math.sqrt(n),(n,'p1 rate'))
        require(abs(p2-limit2)<7/math.sqrt(n),(n,'p2 rate'))
        require(0<=p1<=1 and 0<=p2<=1+1e-10,(n,'probability range'))

print(f'PASS: {checks} deterministic exact/arithmetic checks')
