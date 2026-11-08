"""Exact arithmetic verifier for two-leader placement on a single-edge-deleted biclique.
Only the Python standard library is needed. Run: python verify.py
"""
from fractions import Fraction as Q
from itertools import combinations
import json
from pathlib import Path

class Poly:
    def __init__(self, terms=0):
        if isinstance(terms,int): terms={(0,0):terms}
        self.t={k:int(v) for k,v in terms.items() if v}
    def __add__(self,b):
        b=aspoly(b); v=dict(self.t)
        for k,c in b.t.items():v[k]=v.get(k,0)+c
        return Poly(v)
    __radd__=__add__
    def __neg__(self):return Poly({k:-v for k,v in self.t.items()})
    def __sub__(self,b):return self+(-aspoly(b))
    def __rsub__(self,b):return aspoly(b)-self
    def __mul__(self,b):
        b=aspoly(b);v={}
        for (i,j),a in self.t.items():
            for (k,l),c in b.t.items():v[i+k,j+l]=v.get((i+k,j+l),0)+a*c
        return Poly(v)
    __rmul__=__mul__
    def __pow__(self,n):
        assert isinstance(n,int) and n>=0
        y=Poly(1);b=self
        while n:
            if n&1:y=y*b
            b=b*b;n//=2
        return y
    def __eq__(self,b):return self.t==aspoly(b).t
    def substitute(self,p,q):
        return sum((c*(p**i)*(q**j) for (i,j),c in self.t.items()),Poly())
    def evaluate(self,p,q):return sum(v*p**i*q**j for (i,j),v in self.t.items())

def aspoly(v):return v if isinstance(v,Poly) else Poly(v)
P=Poly({(1,0):1});R=Poly({(0,1):1});X=P;Y=R

def ratnum(obj):return Poly({(a,b):c for a,b,c in obj})
F={c:(ratnum(v['numerator']),ratnum(v['denominator'])) for c,v in json.loads((Path(__file__).parent/'formulas.json').read_text()).items()}
classes=list(F)
assert len(classes)==8 and set(classes)=={'A* B*','A* A','A A','B* B','B B','A* B','A B*','A B'}
checks=0

class Rat:
    def __init__(self,n,d=1):
        self.n=aspoly(n);self.d=aspoly(d)
    def __add__(self,other):
        other=asrat(other);return Rat(self.n*other.d+other.n*self.d,self.d*other.d)
    __radd__=__add__
    def __neg__(self):return Rat(-self.n,self.d)
    def __sub__(self,other):return self+(-asrat(other))
    def __rsub__(self,other):return asrat(other)-self
    def __mul__(self,other):
        other=asrat(other);return Rat(self.n*other.n,self.d*other.d)
    __rmul__=__mul__
    def __truediv__(self,other):
        other=asrat(other);return Rat(self.n*other.d,self.d*other.n)
    def __rtruediv__(self,other):return asrat(other)/self
    def __pow__(self,i):
        assert i>=0
        return Rat(self.n**i,self.d**i)
    def same(self,other):
        other=asrat(other);return self.n*other.d==other.n*self.d

def asrat(x):return x if isinstance(x,Rat) else Rat(x)

def source_objective(label):
    kind=label.split()
    a=sum(z.startswith('A') for z in kind);b=2-a
    p,q=Rat(P),Rat(R)
    s,t=p-a,q-b
    delta=a*q+b*p-a*b
    U=t/(q*delta);V=s/(p*delta);W=1/delta
    alpha,beta=1/q,1/p
    base=s/q+t/p+s*U+t*V
    # The removed cross-edge contributes a negative rank-one update
    # on the follower coordinates; trace correction from Sherman-Morrison.
    if 'A*' in kind and 'B*' in kind:return base
    if 'A*' in kind:
        num=s*W**2+beta**2+2*beta*V+t*V**2
        den=1-beta-V
    elif 'B*' in kind:
        num=t*W**2+alpha**2+2*alpha*U+s*U**2
        den=1-alpha-U
    else:
        num=(alpha+U-W)**2+(s-1)*(U-W)**2+(W-beta-V)**2+(t-1)*(W-V)**2
        den=1-alpha-U-beta-V+2*W
    return base+num/den

# Formal rational-function identities, for arbitrary p,q, not finite samples.
for name,(num,den) in F.items():
    assert source_objective(name).same(Rat(num,den)),name


def positive_coeff(p,nonzero=True):
    global checks
    assert all(z>=0 for z in p.t.values()),p.t
    if nonzero:assert p.t and any(z>0 for z in p.t.values())
    checks+=len(p.t)

# Every rational objective denominator is positive for p,q>=3.
for label,(numer,denom) in F.items():
    z=denom.substitute(3+X,3+Y)
    positive_coeff(z)
    assert z.evaluate(0,0)>0

# All candidate differences J_class-J_AA are nonnegative for p>=6, q>=p;
# strict except the symmetric opposite-side pair B B when q=p.
for name,(n,d) in F.items():
    if name=='A A':continue
    an,ad=F['A A']
    diff=n*ad-an*d
    z=diff.substitute(6+X,6+X+Y)
    positive_coeff(z)
    if name=='B B':
        assert all(j>0 for (i,j) in z.t) # equal only at Y=0
    else:
        assert z.evaluate(0,0)>0 # strictly positive for all X,Y>=0

# Remaining unbounded strips: p=3,4,5 with indicated starting q.
for p0,q0 in [(3,7),(4,5),(5,6)]:
    for name,(n,d) in F.items():
        if name=='A A':continue
        an,ad=F['A A']
        z=(n*ad-an*d).substitute(Poly(p0),q0+Y)
        positive_coeff(z)
        assert z.evaluate(0,0)>0

# Six finite low-size cases have unique optimum {a0,b0}.
for p0,q_hi in [(3,6),(4,4),(5,5)]:
    for q0 in range(p0,q_hi+1):
        exact={label:Q(n.evaluate(p0,q0),d.evaluate(p0,q0)) for label,(n,d) in F.items()}
        assert all(v>exact['A* B*'] for key,v in exact.items() if key!='A* B*')
        checks+=len(exact)-1

# Independent grounded-Laplacian matrix inverse by exact Gauss-Jordan elimination.
def inverse_trace(M):
    n=len(M); A=[[Q(x) for x in row]+[Q(i==j) for j in range(n)] for i,row in enumerate(M)]
    for k in range(n):
        pivot=next(i for i in range(k,n) if A[i][k]);A[k],A[pivot]=A[pivot],A[k]
        z=A[k][k];A[k]=[x/z for x in A[k]]
        for i in range(n):
            if i!=k:
                z=A[i][k]
                if z:A[i]=[x-z*y for x,y in zip(A[i],A[k])]
    return sum(A[i][n+i] for i in range(n))

def graph(p,q):
    L=[[0 for _ in range(p+q)] for _ in range(p+q)]
    for a in range(p):
        for b in range(p,p+q):
            if a==0 and b==p:continue
            L[a][a]+=1;L[b][b]+=1;L[a][b]-=1;L[b][a]-=1
    return L

def kind(i,j,p):
    def lab(x):return 'A*' if x==0 else 'B*' if x==p else 'A' if x<p else 'B'
    return ' '.join(sorted((lab(i),lab(j)),key=lambda z:('A' not in z, '*' not in z)))

matrix_checks=0
for p0 in range(3,9):
    for q0 in range(p0,13):
        L=graph(p0,q0); size=p0+q0
        for i,j in combinations(range(size),2):
            key=kind(i,j,p0)
            ns,ds=F[key]
            formula=Q(ns.evaluate(p0,q0),ds.evaluate(p0,q0))
            free=[z for z in range(size) if z not in (i,j)]
            M=[[L[a][b] for b in free] for a in free]
            assert inverse_trace(M)==formula,(p0,q0,i,j,key)
            matrix_checks+=1

print('VERIFY_OK: symbolic coefficient checks',checks,'exact grounded-matrix comparisons',matrix_checks)
