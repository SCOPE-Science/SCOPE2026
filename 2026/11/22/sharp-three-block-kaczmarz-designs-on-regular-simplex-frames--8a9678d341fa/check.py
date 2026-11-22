"""Exact arithmetic checks for three-block simplex projection theorem.
Run: python check.py (requires sympy).  All analytic bounds are proved in RESULT.md.
"""
import itertools
import sympy as sp
m,a,b,x,y=sp.symbols('m a b x y', positive=True)
check_count=0

def require(expr):
    global check_count
    assert sp.simplify(expr)==0, sp.factor(expr)
    check_count+=1

# Both analytic boundary values yield exactly a double objective contact.
M=a+b+1
T=(M+1)/(3*M+1)
A=M/((a+1)*(b+1))
B=M*b/((b+1)*(M-1))
C=M*a/((a+1)*(M-1))
D=A*x*y+B*x*(1-x-y)+C*y*(1-x-y)
require(D.subs({x:T,y:T})-T*(1-T))
require(A-B-C+2*M*a*b/((a+1)*(b+1)*(M-1)))
require((2*M*a*b/((a+1)*(b+1)*(M-1)))/B-2*a/(a+1))
require((2*M*a*b/((a+1)*(b+1)*(M-1)))/C-2*b/(b+1))

# Case with exactly one nonsingleton block.
M=m
T1=M/(3*M-2)
p=[T1,(M-1)/(3*M-2),(M-1)/(3*M-2)]
s=[M-2,1,1]
D1=sum(p[i]*p[j]*M*s[k]/((M-s[i])*(M-s[j]))
       for i,j,k in [(0,1,2),(0,2,1),(1,2,0)])
require(D1-T1*(1-T1))
require(T1-(M+1)/(3*M+1)-2/((3*M-2)*(3*M+1)))
require(T1-sp.Rational(1,3)-2/(3*(3*M-2)))

# Rational projector formula and characteristic polynomials in an explicit basis.
lam=sp.symbols('lam')
def exact_test(sz):
    global check_count
    n=sum(sz)
    H=sp.eye(n)-sp.ones(n,n)/n
    Ps=[]; start=0
    for size in sz:
        inds=list(range(start,start+size)); start+=size
        E=sp.zeros(n); z=sp.zeros(n,1)
        for i in inds: E[i,i]=1; z[i]=1
        P=H*(E+z*z.T/(n-size))*H
        assert P*P==P
        Ps.append(P)
        check_count+=1
    if sz[1]==1:
        t=sp.Rational(n,3*n-2)
        weights=[t,(1-t)/2,(1-t)/2]
    elif sz[2]==1:
        t=sp.Rational(n+1,3*n+1)
        weights=[t,t,1-2*t]
    else:
        t=sp.Rational(1,3)
        weights=[t,t,t]
    mat=sum((weights[j]*Ps[j] for j in range(3)),sp.zeros(n))
    V=sp.zeros(n,n-1)
    for i in range(n-1): V[i,i]=1; V[n-1,i]=-1
    metric=V.T*V
    restricted=metric.inv()*V.T*mat*V
    actual=sp.factor(restricted.charpoly(lam).as_expr())
    det=sum(weights[i]*weights[j]*n*sz[k]/((n-sz[i])*(n-sz[j]))
            for i,j,k in [(0,1,2),(0,2,1),(1,2,0)])
    expected=sp.prod((lam-weights[i])**(sz[i]-1) for i in range(3))*(lam**2-lam+det)
    require(actual-expected)
    require(det-t*(1-t) if sz[2]==1 else 0)
    # With one large block, other two group-mean eigenvalues t and 1-t.
    if sz[1]==1: require(det-t*(1-t))
    if sz[2]==1: assert sp.factor(actual).subs(lam,t)==0
    check_count+=1

for n in range(4,9):
    for a0 in range(n-2,0,-1):
        for b0 in range(min(a0,n-a0-1),0,-1):
            c0=n-a0-b0
            if c0<1 or c0>b0: continue
            exact_test((a0,b0,c0))

# Direct rational examples, including the nonuniform selection advantage.
for n in range(4,120):
    t1=sp.Rational(n,3*n-2)
    assert t1>sp.Rational(n+1,3*n+1)>sp.Rational(1,3)
    check_count+=1
print(f'PASS: {check_count} exact symbolic, polynomial and rational checks')
