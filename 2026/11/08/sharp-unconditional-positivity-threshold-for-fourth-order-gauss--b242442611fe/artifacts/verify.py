"""Exact symbolic and rational checks for a fourth-order heat-update threshold."""
import itertools
import sympy as sp

p,q,t,x=sp.symbols('p q t x',positive=True)
n=p+q
a=p*t+q
D=lambda z:z*z+6*z+12
F=lambda z:(z*z-6*z+12)/D(z)

# Spectral projector entries give three off-diagonal classes.
clique=1/n-F(a*x)/p+q*F(n*x)/(p*n)
independent=1/n-F(p*x)/q+p*F(n*x)/(q*n)
cross=(1-F(n*x))/n
clique_expected=12*x*(a*(p+2*q-q*t)*x*x+6*a*x+12*t)/(D(a*x)*D(n*x))
independent_expected=12*x*x*p*(x*(q+2*p)+6)/(D(p*x)*D(n*x))
cross_expected=12*x/D(n*x)
for left,right in [(clique,clique_expected),(independent,independent_expected),(cross,cross_expected)]:
    assert sp.factor(left-right)==0
print('SYMBOLIC_FACTOR_IDENTITIES_OK')

def laplacian(P,Q,T):
    N=P+Q
    mat=sp.zeros(N)
    for i in range(N):
        for j in range(i+1,N):
            w = T if i<P and j<P else (1 if i<P<=j else 0)
            mat[i,j]=mat[j,i]=-w
            mat[i,i]+=w;mat[j,j]+=w
    return mat

def update(L,H):
    Z=H*L
    N=L.rows
    return (Z*Z+6*Z+12*sp.eye(N)).inv()*(Z*Z-6*Z+12*sp.eye(N))

checks=0
for P,Q in itertools.product(range(2,6),range(2,6)):
    limit=sp.Rational(P+2*Q,Q)
    for T in sorted(set((sp.Rational(0),sp.Rational(1),limit/2,limit,limit+sp.Rational(1,3),limit*sp.Rational(2)))):
        L=laplacian(P,Q,T)
        for H in [sp.Rational(1,8),sp.Rational(1),sp.Rational(5),sp.Rational(200)]:
            X=update(L,H)
            assert X==X.T
            assert all(sum(X[i,j] for j in range(P+Q))==1 for i in range(P+Q))
            aa=sp.cancel(clique_expected.subs({p:P,q:Q,t:T,x:H}))
            bb=sp.cancel(independent_expected.subs({p:P,q:Q,x:H}))
            cc=sp.cancel(cross_expected.subs({p:P,q:Q,x:H}))
            assert all(X[i,j]==aa for i in range(P) for j in range(P) if i!=j)
            assert all(X[i,j]==bb for i in range(P,P+Q) for j in range(P,P+Q) if i!=j)
            assert all(X[i,j]==cc for i in range(P) for j in range(P,P+Q))
            assert all(X[i,i]>0 for i in range(P+Q))
            if T<=limit:
                assert all(X[i,j]>0 for i in range(P+Q) for j in range(P+Q))
            checks+=1
print('EXACT_MATRIX_CASES_OK',checks)

for P,Q in itertools.product(range(2,8),range(2,8)):
    threshold=sp.Rational(P+2*Q,Q)
    for T in [threshold+sp.Rational(1,5),threshold+2,threshold*3]:
        A=(P*T+Q)*(P+2*Q-Q*T)
        B=6*(P*T+Q)
        C=12*T
        assert A<0 and B>0 and C>0
        # At x = -2 B/A + sqrt(-2 C/A), the quadratic is strictly negative.
        witness=-2*B/A + sp.sqrt(-2*C/A)
        assert sp.simplify(A*witness**2+B*witness+C)<0
print('SHARP_NEGATIVE_WITNESS_CASES_OK',36*3)
