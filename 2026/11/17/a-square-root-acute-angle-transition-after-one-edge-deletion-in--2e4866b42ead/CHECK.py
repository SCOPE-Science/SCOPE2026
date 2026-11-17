"""Exact verification for the one-edge-defect Laplacian-simplex angle theorem.

Requires Python 3 and SymPy. No numerical tolerance enters the certificates.
"""
import sympy as sp

p, q = sp.symbols('p q', integer=True, positive=True)
n = p + q
c = p*q/((p-1)*(q-1))
Da = (p-1)/(p*q**2) + q/(p*n**3)
Oa = -1/(p*q**2) + q/(p*n**3)
Db = (q-1)/(q*p**2) + p/(q*n**3)
Ob = -1/(q*p**2) + p/(q*n**3)
X = -1/n**3
u = [(n-1)/(n*q), -1/(n*q), -(n-1)/(n*p), 1/(n*p)]
v = [Da-X, Oa-X, X-Db, X-Ob]
s = sp.factor(Da+Db-2*X)

def entry(g,h, same=False):
    if g<2 and h<2:
        initial = Da if g==h==0 else Oa
    elif g>=2 and h>=2:
        initial = Db if g==h==2 else Ob
    else:
        initial = X
    if same:
        initial = Oa if g==1 else Ob
    return sp.factor(initial+c*(u[g]*v[h]+v[g]*u[h])+c**2*s*u[g]*u[h])

P,Q=sp.symbols('P Q', integer=True, nonnegative=True)
D=(p-1)**2*(q-1)**2*n**3
F=(n-1)*(n-2)**2+(3*n-4)*p*q-(p*q)**2
assert sp.cancel(entry(0,3)-F/D)==0
assert sp.cancel(entry(1,2)-F/D)==0

sign_cases=[('defect-within',entry(0,1),D,{p:P+2,q:Q+2}),
            ('both-defects',entry(0,2),D,{p:P+2,q:Q+2}),
            ('ordinary-cross',entry(1,3),D,{p:P+2,q:Q+2}),
            ('ordinary-within',entry(1,1,True),q*q*D,{p:P+3,q:Q+2})]
for name,k,den,shift in sign_cases:
    cert=sp.factor(-k*den)
    poly=sp.Poly(sp.expand(cert.subs(shift)),P,Q)
    assert all(z>0 for z in poly.coeffs()),(name,poly)
    print('POSITIVE_POLYNOMIAL_CERT',name,'monomials',len(poly.terms()))

num_cases=0
for a in range(2,8):
 for b in range(2,8):
    m=a+b
    lap=sp.zeros(m)
    for i in range(a):
     for j in range(a,m):
      if i==0 and j==a:continue
      lap[i,i]+=1;lap[j,j]+=1;lap[i,j]-=1;lap[j,i]-=1
    J=sp.ones(m)/m
    inverse=(lap+J).inv()-J
    k_matrix=inverse*inverse
    groups=[0]+[1]*(a-1)+[2]+[3]*(b-1)
    for i in range(m):
     for j in range(i+1,m):
      x=entry(groups[i],groups[j],groups[i]==groups[j])
      assert sp.simplify(k_matrix[i,j]-x.subs({p:a,q:b}))==0,(a,b,i,j)
    num_cases+=1

first_nonobtuse=None
for N in range(4,401):
    for a in range(2,N//2+1):
        b=N-a;t=a*b
        signal=(N-1)*(N-2)**2+(3*N-4)*t-t*t
        if signal<=0:
            if first_nonobtuse is None:first_nonobtuse=(N,a,b,signal)
            break
assert first_nonobtuse == (25,11,14,-86)
print('ONE_EDGE_DEFECT_ANGLE_PASS exact_matrix_profiles=',num_cases,
      'first_nonobtuse=',first_nonobtuse,'symbolic_sign_classes=',len(sign_cases))
