"""Independent angular-moment Gram computation for quadratic-harmonic lune gradient concentration.
Requires numpy; all source/observation measures are uniform-sphere probability measures.
"""
import math
import numpy as np


def traceless_basis(d):
    raw=[]
    for i in range(d):
        for j in range(i+1,d):
            a=np.zeros((d,d));a[i,j]=a[j,i]=1
            raw.append(a)
    for i in range(d-1):
        a=np.zeros((d,d));a[i,i]=1;a[d-1,d-1]=-1
        raw.append(a)
    basis=[]
    for a in raw:
        for b in basis:
            a=a-np.sum(a*b)*b
        t=np.linalg.norm(a)
        assert t>1.e-10
        basis.append(a/t)
    return np.array(basis)*math.sqrt((d+2)/4)


def conditional_grad_product(a,b,phi,d):
    v=np.array([math.cos(phi),math.sin(phi)])
    pa=v@a[:2,:2]@v; pb=v@b[:2,:2]@v
    de=a[2:,2:]; ee=b[2:,2:]
    # Dirichlet Gram = 4(E[x^T AB x] - E[(x^T A x)(x^T B x)]).
    # Conditional moments are derived from r^2~Beta(1,(d-2)/2)
    # and w uniform on S^(d-3), independent of the longitude.
    ab=a@b
    term2=(2*(v@ab[:2,:2]@v)+np.trace(ab[2:,2:]))/d
    term4=(8*pa*pb+np.trace(de)*np.trace(ee)+2*np.trace(de@ee)
           +2*pa*np.trace(ee)+2*pb*np.trace(de)
           +8*(a[2:,:2]@v)@(b[2:,:2]@v))/(d*(d+2))
    return 4*(term2-term4)


def lune_gram(d,L):
    basis=traceless_basis(d)
    m=len(basis)
    # Every angular integrand is a trigonometric polynomial of order <=4;
    # 16 periodic samples identify it without aliasing. Integrate its
    # Fourier coefficients exactly over the symmetric lune angle.
    n=16
    phis=2*np.pi*np.arange(n)/n
    data=np.empty((n,m,m))
    for h,phi in enumerate(phis):
        for i,a in enumerate(basis):
            for j,b in enumerate(basis[:i+1]):
                data[h,i,j]=data[h,j,i]=conditional_grad_product(a,b,phi,d)
    coeff=np.fft.fft(data,axis=0)/n
    out=np.zeros((m,m),dtype=complex)
    for k in range(-4,5):
        factor=L if k==0 else 2*np.sin(k*L/2)/k
        out+=factor*coeff[k%n]
    out=np.real(out)/(2*np.pi)
    assert np.linalg.norm(out-out.T)<1.e-11
    return (out+out.T)/2


def predicted_spectrum(d,L):
    mass=L/(2*np.pi); mu=np.sin(L)/L; nu=mu*np.cos(L)
    b=1/d; rho=np.sqrt((d-2)/d); c=(d-2)/(2*d)
    rad=np.hypot(b*nu,rho*mu)
    vals=[1-b*nu-rad,1-b*nu+rad,1+2*b*nu]
    vals +=[1+c*mu]*(d-2)+[1-c*mu]*(d-2)
    vals +=[1]*((d-2)*(d-1)//2-1)
    return np.sort(mass*np.array(vals))


def test():
    count=0
    for d in (3,4,5,7,9):
        pivot=math.acos(math.sqrt(3/8))
        for L in (.035,.21,.72,pivot,1.12,math.pi/2,1.94,math.pi-pivot,2.95,math.pi-.01):
            observed=np.linalg.eigvalsh(lune_gram(d,L))
            pred=predicted_spectrum(d,L)
            assert len(observed)==len(pred)==d*(d+1)//2-1
            assert max(abs(observed-pred))<3e-12,(d,L,observed,pred)
            assert abs(sum(observed)-(d*(d+1)//2-1)*L/(2*np.pi))<2e-12
            assert observed[0]>-1.e-12 and observed[-1]<1+1.e-12
            count+=3
            b=1/d;rho=math.sqrt((d-2)/d);mu=math.sin(L)/L;nu=mu*math.cos(L)
            lamplus=1-b*nu+math.hypot(b*nu,rho*mu)
            lamminus=1-b*nu-math.hypot(b*nu,rho*mu)
            s=1+2*b*nu
            if d>=4:
                assert lamplus>=s-1.e-13 and lamminus<=s+1.e-13
            else:
                if L<pivot-1.e-8: assert s>lamplus
                if pivot+1.e-8<L: assert lamplus>s
                if L<math.pi-pivot-1.e-8: assert lamminus<s
                if L>math.pi-pivot+1.e-8: assert s<lamminus
            count+=1
    print('LUNE_GRADIENT_SPECTRAL_CHECKS_PASS',count)

if __name__=='__main__':
    test()
