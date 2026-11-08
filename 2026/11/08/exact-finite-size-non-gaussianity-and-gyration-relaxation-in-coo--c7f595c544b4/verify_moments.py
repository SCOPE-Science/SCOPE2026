"""Exact checks for a finite complete-graph cooperative Brownian averaging model.

For each unordered pair (i,j), at rate nu, both coordinates move to their
midpoint; between events each coordinate has Brownian diffusivity D.
The calculations use centered coordinates y_i=x_i-mean(x).
"""
import sympy as sp
import random

n, D, nu=sp.symbols('n D nu', positive=True)
Q=4*D*(n-1)/(nu*n)
A=16*D**2*(n-1)*(7*n**2+13*n-6)/(nu**2*n**2*(7*n-6))
B=48*D**2*(n-1)*(9*n**2-13*n+6)/(nu**2*n**3*(7*n-6))
assert sp.simplify(2*D*(n-1)-nu*n*Q/2)==0
assert sp.simplify(12*D*(n-1)*Q/n+nu*(3*A-7*n*B)/8)==0
assert sp.simplify(4*D*(n+1)*Q+nu*(-(n-sp.Rational(3,4))*A+n*B/4))==0
assert sp.factor(B/n/(Q/n)**2-3)==6*n*n/((n-1)*(7*n-6))
Q2diff=2*Q/(n-1)
D4diff=2*(n*B+3*A)/(n*(n-1))
assert sp.simplify(D4diff/Q2diff**2-3-3*(n+6)/(7*n-6))==0
assert sp.simplify(A/Q**2-1-2*(13*n-6)/((n-1)*(7*n-6)))==0
assert sp.limit((B/n)/(Q/n)**2-3,n,sp.oo)==sp.Rational(6,7)
assert sp.limit(D4diff/Q2diff**2-3,n,sp.oo)==sp.Rational(3,7)
assert sp.limit(n*(A/Q**2-1),n,sp.oo)==sp.Rational(26,7)
assert sp.simplify(sp.diff(6*n*n/((n-1)*(7*n-6)),n)-6*n*(12-13*n)/((n-1)**2*(7*n-6)**2))==0
assert sp.simplify(sp.diff(3*(n+6)/(7*n-6),n)+144/(7*n-6)**2)==0

rng=random.Random(19091)
checks=0
for N in range(2,11):
    for j in range(13):
        raw=[sp.Rational(rng.randint(-20,20),rng.randint(1,7)) for _ in range(N)]
        center=sum(raw)/N
        y=[v-center for v in raw]
        q=sum(v*v for v in y)
        p4=sum(v**4 for v in y)
        d_q=d_p4=d_q2=sp.Integer(0)
        for i in range(N):
            for k in range(i+1,N):
                a=(y[i]+y[k])/2
                upd=list(y)
                upd[i]=upd[k]=a
                u_q=sum(v*v for v in upd)
                u_p4=sum(v**4 for v in upd)
                d_q+=u_q-q
                d_p4+=u_p4-p4
                d_q2+=u_q**2-q**2
        assert d_q==-sp.Rational(N,2)*q
        assert d_p4==(-7*N*p4+3*q*q)/8
        assert d_q2==(-N+sp.Rational(3,4))*q*q+sp.Rational(N,4)*p4
        assert sum((y[i]-y[k])**2 for i in range(N) for k in range(i+1,N))==N*q
        assert sum((y[i]-y[k])**4 for i in range(N) for k in range(i+1,N))==N*p4+3*q*q
        checks+=5
for N in range(2,11):
    d=sp.Rational(3,5);rate=sp.Rational(7,11)
    qq=Q.subs({n:N,D:d,nu:rate});aa=A.subs({n:N,D:d,nu:rate});bb=B.subs({n:N,D:d,nu:rate})
    assert sp.simplify(2*d*(N-1)-rate*N*qq/2)==0
    assert sp.simplify(12*d*(N-1)*qq/N+rate*(3*aa-7*N*bb)/8)==0
    assert sp.simplify(4*d*(N+1)*qq+rate*(-(N-sp.Rational(3,4))*aa+N*bb/4))==0
    checks+=3
print('PASSED',checks,'exact independent pair updates and moment identities')
print('CHECK_LIMITS',sp.Rational(6,7),sp.Rational(3,7),sp.Rational(26,7))
