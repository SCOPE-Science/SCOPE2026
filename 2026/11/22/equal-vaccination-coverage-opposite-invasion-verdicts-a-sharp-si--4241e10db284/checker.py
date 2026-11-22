"""Reproducible mathematical checks for equal-coverage polarized SIV invasion.
Requires only Python 3 standard library. Uses physical node variables, not Monte Carlo simulations.
"""
from fractions import Fraction
from itertools import combinations, product
from math import cos, pi, sqrt

def graph(m):
    # Clique K_m: nodes 0..m-1; path P_m: nodes m..2m-1.
    # Single bridge from clique node 0 to path node m+1.
    N=2*m
    adj=[[0]*N for _ in range(N)]
    edges=[(a,b) for a in range(m) for b in range(a+1,m)]
    edges += [(j,j+1) for j in range(m,2*m-1)]
    edges += [(0,m+1)]
    for a,b in edges: adj[a][b]=adj[b][a]=1
    return adj,edges

def consistent(A,s):
    return all(s[i]*sum(A[i][j]*s[j] for j in range(len(s)))>0 for i in range(len(s)))

def stable_saturated_signs(A):
    n=len(A)
    return [s for s in product((-1,1),repeat=n) if consistent(A,s)]

def transition(A,s,I,V,epsilon=0.5,omega=0.8,alpha=0.5,phi=0.5,lam=0.3):
    # source Eqns (1),(2),(3),(6),(8), using current opinion as vaccination decision
    n=len(A)
    o=[]
    for i in range(n):
        nbr=[j for j in range(n) if A[i][j]]
        v=s[i]+epsilon*sum(s[j] for j in nbr)/len(nbr)+omega*sum(I[j] for j in nbr)/len(nbr)
        o.append(max(-1.,min(1.,v)))
    gamma=[(1+x)*0.5 for x in o]
    ni=[];nv=[]
    for i in range(n):
        S=1-I[i]-V[i]
        q=1
        for j in range(n):
            if A[i][j]:q*=1-lam*I[j]
        q=1-q
        ni.append((1-alpha)*I[i]+S*(1-gamma[i])*q)
        nv.append((1-phi)*V[i]+S*gamma[i])
    return o,ni,nv

def check_small_minimality():
    checked=0
    for n in range(2,6):
        pairs=list(combinations(range(n),2))
        for mask in range(1<<len(pairs)):
            adj=[[0]*n for _ in range(n)]
            for k,(i,j) in enumerate(pairs):
                if mask & (1<<k):adj[i][j]=adj[j][i]=1
            visited={0};todo=[0]
            while todo:
                k=todo.pop()
                for j in range(n):
                    if adj[k][j] and j not in visited:
                        visited.add(j);todo.append(j)
            if len(visited)<n:continue
            checked+=1
            assert not any(any(x<0 for x in s) and any(x>0 for x in s)
                       for s in stable_saturated_signs(adj))
    return checked

assert check_small_minimality()>0
A,E=graph(3)
s_c=[-1]*3+[1]*3
s_p=[1]*3+[-1]*3
assert consistent(A,s_c) and consistent(A,s_p)
for m in range(3,51):
    a,e=graph(m)
    assert consistent(a,[-1]*m+[1]*m) and consistent(a,[1]*m+[-1]*m)
    cR=m-1
    pR=2*cos(pi/(m+1))
    assert cR>pR

# Spectral quantities for m=3 via exact rational inequalities:
alpha=Fraction(1,2);lam=Fraction(3,10);phi=Fraction(1,2)
assert Fraction(1,2)+Fraction(3,10)*2>1
assert (alpha - 0)**2 > (lam**2)*2  # (lambda sqrt(2) < alpha)
assert alpha>0 and phi>0 and phi<1

# Both disease-free states have exactly half the nodes pro-vaccine and V=1/(1+phi) there.
V0=[0.,0.,0.,2/3,2/3,2/3]
V1=[2/3,2/3,2/3,0.,0.,0.]
for s,V in [(s_c,V0),(s_p,V1)]:
    O,In,Vn=transition(A,list(map(float,s)),[0.]*6,V)
    assert O==list(map(float,s))
    assert max(abs(vn-v) for vn,v in zip(Vn,V))<1e-14
    assert In==[0.]*6
    assert abs(sum(V)/6-1/3)<1e-14

# Check the exact infection linearization against a small perturbation of the source map.
# Direction supported on the three negative vertices: clique Perron (1,1,1), path Perron (1,sqrt(2),1).
for s,V,dirI,expected in [(s_c,V0,[1.,1.,1.,0.,0.,0.],.5+.3*2),
                             (s_p,V1,[0.,0.,0.,1.,sqrt(2),1.],.5+.3*sqrt(2))]:
    h=1e-7; pert=[h*v for v in dirI]
    O,I2,V2=transition(A,list(map(float,s)),pert,V)
    for k,v in enumerate(dirI):
        if v>0:
            ratio=I2[k]/(h*v)
            assert abs(ratio-expected)<2e-6,(s,k,ratio,expected)
    assert O==list(map(float,s))
print('PASS: complete connected-graph binary strict-polarization census through n=5')
print('PASS: graph family m=3..50 strict signs and ordered spectral thresholds')
print('PASS: two six-node exact DFE and equal vaccine coverage 1/3')
print('PASS: epidemic linearization (clique multiplier 1.1, path multiplier 0.924264...)')
print('PASS: exact inequality 3 sqrt(2)/10 < 1/2 < 3*2/10')
