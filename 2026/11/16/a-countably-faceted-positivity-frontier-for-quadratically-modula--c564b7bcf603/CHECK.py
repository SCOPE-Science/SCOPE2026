"""Reproducibility checks for a two-harmonic theta-kernel positivity frontier.
Uses exact rational arithmetic for rational q, with y_n=(q**(-2*n)+q**(2*n))/2.
These finite checks supplement the complete analytic proof; they do not prove it.
"""
from fractions import Fraction as F

def y(q,n):
    return (q**(-2*n)+q**(2*n))/2

def f(q,alpha,beta,n):
    z=y(q,n)
    return 1+alpha*q*z+beta*q**4*(2*z*z-1)

def vertex(q,n):
    yn=y(q,n); ym=y(q,n+1); den=1+2*yn*ym
    return (-2*(yn+ym)/(q*den),1/(q**4*den))

def line(q,beta,n):
    z=y(q,n)
    return -(1+beta*q**4*(2*z*z-1))/(q*z)

count=0
for q in [F(1,2),F(2,3),F(4,5),F(9,10)]:
    for n in range(12):
        a,b=vertex(q,n)
        assert f(q,a,b,n)==0 and f(q,a,b,n+1)==0
        yn=y(q,n); ym=y(q,n+1)
        for k in range(24):
            # Factorization is an exact identity at each tested frequency.
            assert f(q,a,b,k)==2*(y(q,k)-yn)*(y(q,k)-ym)/(1+2*yn*ym)
            assert f(q,a,b,k)>=0
            assert (f(q,a,b,k)==0)==(k in (n,n+1))
            count+=1
        if n:
            _,prev=vertex(q,n-1)
            assert b<prev
            beta=(b+prev)/2
            alpha=line(q,beta,n)
            assert f(q,alpha,beta,n)==0
            assert all(f(q,alpha,beta,k)>0 for k in range(24) if k!=n)
        else:
            beta=2*b
            alpha=line(q,beta,0)
            assert f(q,alpha,beta,0)==0
            assert all(f(q,alpha,beta,k)>0 for k in range(1,24))
    # High-mode obstruction when the quadratic parameter is negative.
    for alpha,beta in [(F(-1,2),F(0)),(F(2),F(-1,7))]:
        assert any(f(q,alpha,beta,k)<0 for k in range(1,50))
print('CHECK_OK exact_vertex_factorizations=%d facet_interior=48 high_mode_obstructions=8' % count)
