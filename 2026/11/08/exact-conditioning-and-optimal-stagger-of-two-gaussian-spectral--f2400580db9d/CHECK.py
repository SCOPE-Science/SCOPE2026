"""Direct numerical verification of exact two-bin Hermitian-lifting spectrum.
Only NumPy is required; this test does not substitute for the proof."""
import math
import numpy as np


def basis():
    bs=[]
    for k in range(3):
        m=np.zeros((3,3),complex)
        m[k,k]=1
        bs.append(m)
    for i,j in [(0,1),(0,2),(1,2)]:
        r=np.zeros((3,3),complex)
        r[i,j]=r[j,i]=1/math.sqrt(2)
        bs.append(r)
        q=np.zeros((3,3),complex)
        q[i,j]=1j/math.sqrt(2)
        q[j,i]=-1j/math.sqrt(2)
        bs.append(q)
    return bs


def direct(a,b,c,eta):
    matrices=basis()
    rows=[]
    for j,weights in enumerate(((a,b,c),(c,b,a))):
        for k in range(4):
            theta=k*math.pi/2+(eta if j else 0.)
            v=np.array(weights,dtype=complex)*np.exp(1j*theta*np.arange(3))
            rows.append([np.vdot(v,H@v).real for H in matrices])
    return np.array(rows)


def theoretical(a,b,c,eta):
    U=2*math.sqrt((a*a+c*c)**2+2*b**4)
    fixed=[U,2*(a*a-c*c),2*b*(a+c),2*b*(a+c),
           2*b*(a-c),2*b*(a-c)]
    z=abs(math.cos(2*eta))
    return np.sort(fixed+[2*math.sqrt(2)*a*c*math.sqrt(1+z),
                          2*math.sqrt(2)*a*c*math.sqrt(max(0,1-z))])


def abc(alpha,delta,omega):
    return (math.exp(-alpha*(delta-omega)**2),
            math.exp(-alpha*omega**2),
            math.exp(-alpha*(delta+omega)**2))


def params(a,b,c):
    return (2*math.sqrt((a*a+c*c)**2+2*b**4),
            2*(a-c)*min(a+c,b),2*math.sqrt(2)*a*c)

checks=0
rng=np.random.default_rng(34567)
for alpha,delta,omega in [(1,1,1),(.4,1,.02),(.4,1,1.2),
                           (3.,.65,.2),(.18,2.,.9),(.8,.9,.45)]:
    a,b,c=abc(alpha,delta,omega)
    assert a>c>0 and b>0
    U,L,T=params(a,b,c)
    for eta in [0,.00037,math.pi/100,math.pi/12,math.pi/8,
                math.pi/4,math.pi/2,math.pi/2-.01]+list(rng.uniform(.02,1.55,22)):
        M=direct(a,b,c,eta)
        sv=np.sort(np.linalg.svd(M,compute_uv=False))
        pred=theoretical(a,b,c,eta)
        assert np.allclose(sv,pred,atol=1.e-12,rtol=1.e-11), (alpha,delta,omega,eta,sv,pred)
        checks+=1
        H=np.diag([b*b,-(a*a+c*c),b*b])
        assert np.linalg.norm(M@np.array([np.trace(B@H).real for B in basis()]))<1.e-10
        checks+=1
        if eta not in (0,math.pi/2):
            lower=min(L,T*math.sqrt(1-abs(math.cos(2*eta))))
            assert abs(sv[0]-lower)<2.e-10
            checks+=1
    for eta in np.linspace(0,math.pi/2,401):
        if eta in (0,math.pi/2):
            continue
        low=min(L,T*math.sqrt(1-abs(math.cos(2*eta))))
        assert low <= min(L,T)+1.e-12
        checks+=1
    if L<T:
        cap=1-(L/T)**2
        for eta in [math.pi/4,math.acos(cap)/2]:
            low=min(L,T*math.sqrt(1-abs(math.cos(2*eta))))
            assert abs(low-L)<1.e-10
            checks+=1
    else:
        assert abs(theoretical(a,b,c,math.pi/4)[0]-T)<1.e-10
        checks+=1

a,b,c=abc(1,1,1)
U,L,T=params(a,b,c)
assert L>T
assert abs(U/min(L,T)-39.32018961405606)<1e-9
checks+=1
for d in [1.e-3,1.e-4,1.e-5]:
    eta=d
    low=theoretical(a,b,c,eta)[0]
    assert abs(low/(4*a*c*d)-1)<1.e-5
    checks+=1
print('TWO_GAUSSIAN_BIN_SPECTRUM_CHECKS_PASSED',checks)
