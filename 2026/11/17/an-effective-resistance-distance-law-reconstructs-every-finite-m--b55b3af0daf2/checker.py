"""Standalone arithmetic and quadrature checks for the resistance-law inverse theorem.
No external dependencies. Run: python checker.py
"""
from fractions import Fraction
from math import factorial, exp, isclose
from random import Random


def cp(k):
    assert k>=1
    return 2*factorial(2*k-2)//factorial(k-1)


def power_sums(lens, top):
    return [sum((Fraction(1, x)**k for x in lens), Fraction(0)) for k in range(top+1)]


def coefficients(lens, top):
    L=sum(lens)
    H=power_sums(lens,top)
    # dimensionful coefficients of the full Laplace transform
    return {k: (cp(k)*H[k-2] + sum((cp(p)*cp(k-p)*(H[p-1]*H[k-p-1]-H[k-2]) for p in range(1,k)),0))/L**2 if k>=2 else 2/L for k in range(1,top+1)}


def recover_from_coefficients(A, L, m):
    H={0:Fraction(m)}
    for k in range(3,m+3):
        middle=range(2,k-1)
        den=cp(k)+2*cp(1)*cp(k-1)*(m-1)-sum(cp(p)*cp(k-p) for p in middle)
        assert den>0
        correction=sum(cp(p)*cp(k-p)*H[p-1]*H[k-p-1] for p in middle)
        H[k-2]=(L**2*A[k]-correction)/den
    # Newton identities reconstruct polynomial whose zeros are reciprocals of lengths.
    e=[Fraction(1)]
    for k in range(1,m+1):
        e.append(sum(((-1)**(i-1)*e[k-i]*H[i] for i in range(1,k+1)),Fraction(0))/k)
    return e


def true_elementary(lens):
    e=[Fraction(1)]
    for length in lens:
        z=Fraction(1,length)
        e=[e[0]]+[e[k]+z*e[k-1] if k<len(e) else z*e[k-1] for k in range(1,len(e)+1)]
    return e


def phi(t,n=2000):
    assert n%2==0
    h=1/n
    return h/3*(1+1+sum((4 if j%2 else 2)*exp(-t*(j*h)*(1-j*h)) for j in range(1,n)))


def integrated_laplace(lens,s):
    L=sum(lens)
    vals=[phi(s*float(x)) for x in lens]
    acc=sum((float(x)**2)*vals[i] for i,x in enumerate(lens))
    acc+=sum((float(x*y))*vals[i]*vals[j] for i,x in enumerate(lens) for j,y in enumerate(lens) if i!=j)
    return acc/float(L)**2


def direct_mesh_laplace(lens,s,n=64):
    # Independently compute resistance as current through two circle arcs;
    # use midpoint rule over ordered endpoint pairs on every loop.
    L=float(sum(lens));acc=0.0
    for i,ell_i in enumerate(lens):
        a=float(ell_i)
        for j,ell_j in enumerate(lens):
            b=float(ell_j)
            total=0.
            for k in range(n):
                x=(k+.5)*a/n
                for h in range(n):
                    y=(h+.5)*b/n
                    if i==j:
                        q=abs(x-y)
                        res=q*(a-q)/a
                    else:
                        res=x*(a-x)/a+y*(b-y)/b
                    total+=exp(-s*res)
            acc+=a*b*total/(n*n)
    return acc/L**2


def simulation_mean(lens,N=140000,seed=32179):
    rng=Random(seed)
    w=[float(x) for x in lens];L=sum(w)
    means=0.0;means2=0.
    for it in range(N):
        def sample():
            u=rng.random()*L
            for i,t in enumerate(w):
                if u<t:return i,u
                u-=t
            return len(w)-1,w[-1]
        i,x=sample();j,y=sample()
        if i==j:
            q=abs(x-y);r=q*(w[i]-q)/w[i]
        else:
            r=x*(w[i]-x)/w[i]+y*(w[j]-y)/w[j]
        means+=r;means2+=r*r
    mu=means/N; sd=((means2/N-mu*mu)/N)**.5
    exact=(2*L*sum(x*x for x in w)-sum(x**3 for x in w))/(6*L*L)
    assert abs(mu-exact)<6*sd, (mu,exact,sd)
    return mu, exact, sd


def main():
    configs=[[1],[1,1],[1,2,3],[1,1,2],[2,2,3,5],[1,3,3,3,7], [1,1,1,1,1,1]]
    rng=Random(543)
    for m in range(2,9):
        for _ in range(42):configs.append([rng.randint(1,19) for __ in range(m)])
    for ls in configs:
        lens=list(map(Fraction,ls));m=len(lens);L=sum(lens)
        A=coefficients(lens,m+2)
        assert A[1]==2/L
        assert A[2]==Fraction(4*m*m,L*L)
        recovered=recover_from_coefficients(A,L,m)
        target=true_elementary(lens)
        assert recovered==target,(ls,recovered,target)
    # Laplace quadrature compared with independent pairwise network calculation.
    for ls in ([1],[1,2,3],[1,1,2],[1,3,3,7]):
        for s in (0.13,0.91,3.7):
            a=integrated_laplace(ls,s)
            b=direct_mesh_laplace(ls,s,n=96)
            assert abs(a-b)<0.0004,(ls,s,a,b)
    for ls in ([1,2,3],[1,1,2],[1,3,3,7]):
        simulation_mean(ls)
    # Verify all factorial inequalities used for the analytic positive-coefficient proof.
    for k in range(4,90):
        subtotal=sum(cp(p)*cp(k-p) for p in range(2,k-1))
        assert subtotal <= 4*(k-3)*factorial(2*k-4)//factorial(k-2)
        for m in (1,2,3,100):
            assert cp(k)+2*cp(1)*cp(k-1)*(m-1)-subtotal>0
    print('RESISTANCE_BOUQUET_INVERSE_CHECKS_OK',len(configs),'coefficients,',4*3,'quadrature comparisons')


if __name__=='__main__':main()
