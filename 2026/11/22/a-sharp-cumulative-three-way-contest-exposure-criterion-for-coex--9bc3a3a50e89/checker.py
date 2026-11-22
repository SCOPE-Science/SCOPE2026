"""Exact finite algebra checks for proportional-demography higher-order contest model.
Only the theorem's finite identities are checked; global and periodic dynamics use proof.
"""
from fractions import Fraction as Q
from random import Random


def datum(a,b,c,d,k,alpha,x):
    A=[[Q(0),a,-c],[-a,Q(0),b],[c,-b,Q(0)]]
    H=[[Q(1,2)+A[i][j] for j in range(3)] for i in range(3)]
    B=[[[2*H[i][j]*H[i][m]+H[i][j]*H[j][m]+H[i][m]*H[m][j]
       for m in range(3)] for j in range(3)] for i in range(3)]
    f=[k*z for z in d]
    F=sum((f[i]*x[i] for i in range(3)),Q(0))
    D=sum((d[i]*x[i] for i in range(3)),Q(0))
    y=[f[i]*x[i]/F for i in range(3)]
    s=a+b+c
    ys=[b/s,c/s,a/s]
    z=sum((ys[i]/d[i] for i in range(3)),Q(0))
    xs=[ys[i]/d[i]/z for i in range(3)]
    Ds=sum((d[i]*xs[i] for i in range(3)),Q(0))
    h=[sum((H[i][j]*y[j] for j in range(3)),Q(0)) for i in range(3)]
    hs=[sum((H[i][j]*ys[j] for j in range(3)),Q(0)) for i in range(3)]
    L=[sum((B[i][j][m]*y[j]*y[m] for j in range(3) for m in range(3)),Q(0)) for i in range(3)]
    Ls=[sum((B[i][j][m]*ys[j]*ys[m] for j in range(3) for m in range(3)),Q(0)) for i in range(3)]
    dx=[x[i]*(D/(F*F)*f[i]*sum((2*H[i][j]*f[j]*x[j] for j in range(3)),Q(0))*(1-alpha)
         +D/(F**3)*f[i]*sum((B[i][j][m]*f[j]*x[j]*f[m]*x[m] for j in range(3) for m in range(3)),Q(0))*alpha -d[i]) for i in range(3)]
    deriv=-sum((xs[i]*dx[i]/x[i] for i in range(3)),Q(0))
    diss=-2*alpha*Ds*sum((ys[i]*(h[i]-Q(1,2))**2 for i in range(3)),Q(0))
    assert sum(dx)==0
    assert all(q==Q(1,2) for q in hs)
    assert all(q==Q(1) for q in Ls)
    assert deriv==diss,(deriv,diss)
    assert deriv<=0
    assert (alpha==0 or x==xs or deriv<0)
    return deriv


def main():
    rng=Random(20261119)
    checks=0
    for _ in range(1200):
        a,b,c=[Q(rng.randint(1,9),20) for _ in range(3)]
        d=[Q(rng.randint(1,20),rng.randint(1,5)) for _ in range(3)]
        k=Q(rng.randint(1,15),rng.randint(1,6))
        v=[Q(rng.randint(1,25)) for _ in range(3)]
        x=[q/sum(v) for q in v]
        alpha=rng.choice([Q(0),Q(1,7),Q(2,5),Q(1)])
        datum(a,b,c,d,k,alpha,x)
        checks+=1
    print(f'PASS {checks} exact-rational drift, conservation, equilibrium and strictness tests')
    print('Global LaSalle convergence and neutral periodicity are analytic, not computational claims.')
if __name__=='__main__': main()
