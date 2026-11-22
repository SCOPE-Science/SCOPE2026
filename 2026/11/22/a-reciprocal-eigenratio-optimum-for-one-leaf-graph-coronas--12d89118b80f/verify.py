"""Independent finite tests of the one-leaf corona eigenratio theorem.

Python 3 standard library only. Tests supplement, not replace, the proof.
"""
import math
import random


def eigvals(A):
    n = len(A)
    a = [r[:] for r in A]
    for _ in range(30*n*n):
        p, q = max(((i, j) for i in range(n) for j in range(i+1,n)),
                   key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[p][q]) < 3.e-12:
            break
        tau = (a[q][q]-a[p][p])/(2*a[p][q])
        t = (1 if tau>=0 else -1)/(abs(tau)+math.sqrt(1+tau*tau))
        c = 1/math.sqrt(1+t*t); s=t*c
        app, aqq, apq = a[p][p],a[q][q],a[p][q]
        a[p][p]=app-t*apq
        a[q][q]=aqq+t*apq
        a[p][q]=a[q][p]=0.
        for k in range(n):
            if k not in (p,q):
                akp,akq=a[k][p],a[k][q]
                a[k][p]=a[p][k]=c*akp-s*akq
                a[k][q]=a[q][k]=s*akp+c*akq
    else:
        raise AssertionError('Jacobi did not converge')
    return sorted(a[i][i] for i in range(n))


def laplacian(n, edges):
    a = [[0.]*n for _ in range(n)]
    for i,j,w in edges:
        a[i][i]+=w; a[j][j]+=w
        a[i][j]-=w; a[j][i]-=w
    return a


def cycle(n): return [(i,(i+1)%n) for i in range(n)]
def clique(n): return [(i,j) for i in range(n) for j in range(i+1,n)]
def cube(d): return [(i,i^(1<<k)) for i in range(1<<d) for k in range(d) if i < (i^(1<<k))]

def trial(n, edges, P, Q, B):
    eigen = eigvals(laplacian(n,[(i,j,1.) for i,j in edges]))
    low,high=eigen[1],eigen[-1]
    degree=2*len(edges)/n
    x=2/math.sqrt(low*high)
    a=B/(n*(Q+degree*P*x/2)); b=x*a
    G=2*n
    chosen=[(i,j,b) for i,j in edges]+[(i,i+n,a) for i in range(n)]
    v=eigvals(laplacian(G,chosen))
    R=v[-1]/v[1]
    expected=.5*(1+math.sqrt(high/low)+math.sqrt(1+high/low))**2
    assert abs(R/expected-1)<1.e-8,(n,R,expected)
    assert abs((len(edges)*P*b+n*Q*a)/B-1)<1.e-10
    # Reciprocal scalar identity and global minimum for symmetric designs.
    F=lambda z: (z+2+math.sqrt(z*z+4))/2
    for xx in (x/8,x/2,x,x*2,x*8):
        Rxx=F(low*xx)*F(high*xx)/(low*xx)
        assert Rxx >= expected-1.e-9
    # Check unrestricted independent edge perturbations, normalized to budget.
    rng=random.Random(1000+n*101+int(P*100)+int(Q*10))
    for _ in range(60):
        active=[(i,j,b*math.exp(rng.uniform(-2.,2.))) for i,j in edges]
        active += [(i,i+n,a*math.exp(rng.uniform(-2.,2.))) for i in range(n)]
        cost=sum(w*(P if k<len(edges) else Q) for k,(_,_,w) in enumerate(active))
        active=[(i,j,w*B/cost) for i,j,w in active]
        u=eigvals(laplacian(G,active))
        assert u[1]>0 and u[-1]/u[1]>=expected-1.e-7,(n,u[-1]/u[1],expected)
    return 1+5+60


def main():
    checks=0
    for n in (3,4,5,6,7,8,9,10):
        for P,Q,B in ((1.,1.,1.),(3.,.7,7.)):
            checks+=trial(n,cycle(n),P,Q,B)
    for n in (3,4,5,6,7):
        checks+=trial(n,clique(n),1.3,2.,5.)
    for d in (2,3):
        checks+=trial(1<<d,cube(d),1.,3.,2.)
    # Cycle asymptotic: rim/leaf design ratio differs from spectral-gap design.
    for n in (25,50,100,200):
        s=4*math.sin(math.pi/n)**2
        l=4*math.sin(math.pi*(n//2)/n)**2
        x=2/math.sqrt(s*l)
        gap_x=(2+math.sqrt(s))/(math.sqrt(s)*(1+math.sqrt(s)))
        assert 1<gap_x/x<2.1
        checks+=1
    print(f'PASS {checks} exact-formula, Jacobi-spectrum and asymmetric-perturbation checks')

if __name__=='__main__':main()
