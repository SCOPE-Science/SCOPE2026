"""Exact rank-shell Parseval identities and small-prime-field enumeration."""
from fractions import Fraction
from itertools import product
import sympy as S

q,N=S.symbols('q N',positive=True)
mu=2-1/N
b=q+1-q/N
var=(N-1)**2*(q-1)/N**2
w2=S.factor((mu-1)*(b-q)/((q*q-1)*(q*q-q)))
w1=S.factor((mu-1)*(q*q-b)/((q-1)*(q*q-q)))
w0=S.factor(1-w1-w2)
assert S.simplify(w0+w1+w2-1)==0
assert S.simplify(w0+q*w1+q*q*w2-mu)==0
second=q+3-2*(q+1)/N+q/N**2
assert S.simplify(w0+q*q*w1+q**4*w2-second)==0
assert S.simplify((second-mu*mu)-var)==0
assert S.simplify(mu+var/(mu-1)-b)==0
print('SYMBOLIC_MOMENTS_AND_TWO_SHELL_OBSTRUCTION_PASS')

def rank_mod(a,n,p):
    a=[list(row) for row in a];r=0
    for col in range(n):
        k=next((j for j in range(r,n) if a[j][col]%p),None)
        if k is None: continue
        a[r],a[k]=a[k],a[r]
        z=pow(a[r][col],-1,p)
        a[r]=[(z*x)%p for x in a[r]]
        for j in range(r+1,n):
            fac=a[j][col]
            a[j]=[(a[j][c]-fac*a[r][c])%p for c in range(n)]
        r+=1
    return r

def verify(p,n):
    z=p**n
    weights=[Fraction(int(S.cancel(v.subs({q:p,N:z})).p),int(S.cancel(v.subs({q:p,N:z})).q)) for v in (w0,w1,w2)]
    assert all(x>0 for x in weights)
    ct={n-t:0 for t in (0,1,2)}
    vals={n-t:[0,0] for t in (0,1,2)}
    # The two characters have frequency matrices E_11 and E_11+E_22.
    # Over prime fields, summing powers of primitive roots can be done by
    # counting zero versus nonzero trace residues: require uniform residues.
    residues={n-t:[[0]*p for _ in range(2)] for t in (0,1,2)}
    for entries in product(range(p),repeat=n*n):
        rank=rank_mod([entries[i*n:(i+1)*n] for i in range(n)],n,p)
        if rank not in ct:continue
        ct[rank]+=1
        residues[rank][0][entries[0]%p]+=1
        residues[rank][1][(entries[0]+entries[n+1])%p]+=1
    for a in (0,1):
        probs=[sum(weights[t]*Fraction(residues[n-t][a][r],ct[n-t]) for t in (0,1,2)) for r in range(p)]
        assert probs==[Fraction(1,p)]*p,(p,n,a,probs)
    print(f'EXHAUSTIVE_RANK_SHELL_CHARACTER_ORTHOGONALITY_PASS q={p} n={n} matrix_count={p**(n*n)} weights={weights}')
for p,n in [(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)]:verify(p,n)
