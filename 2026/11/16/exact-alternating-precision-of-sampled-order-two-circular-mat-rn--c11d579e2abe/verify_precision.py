"""Independent finite-matrix checks for the sampled periodic order-two Matérn kernel.

Dependency: mpmath (pip install mpmath). This numerical test does not replace
any proof involving all positive range parameters or all sample counts.
"""
import mpmath as mp

mp.mp.dps = 60


def covariance(n, kappa):
    a = kappa / n
    r = mp.exp(-a)
    z = r**n
    c = []
    for d in range(n):
        rd, rn = r**d, r**(n-d)
        u = (rd * (1 + a*d) + rn * (1 + a*(n-d))) / (1-z)
        v = kappa*z * (rd+rn) / (1-z)**2
        c.append((u+v)/(4*kappa**3))
    return mp.matrix([[c[(i-j)%n] for j in range(n)] for i in range(n)])


def explicit_inverse_first_row(n, kappa):
    a = kappa/n
    r = mp.exp(-a)
    A = 1-r**4-4*a*r**2
    B = 2*r*(a*(1+r**2)-(1-r**2))
    s = mp.sqrt(A**2-B**2)
    t = B/(A+s)
    eta = -t
    V = 4*r*r/B
    W = (-4*r*(1+r*r)-V*A)/B
    R = (1+r*r+2*r*A/B)**2
    assert A>B>0 and R>0 and 0<t<1
    q = []
    for d in range(n):
        local = (W if d==0 else mp.mpf(0)) + (V/2 if d in (1,n-1) else mp.mpf(0))
        tail = (R/s)*(eta**d+eta**(n-d))/(1-eta**n)
        q.append(4*kappa**3 * (local+tail))
    return q, t


def run():
    test_count=0
    ranges=['0.12','0.8','2.5','7','19']
    for n in range(3, 17):
        for kstr in ranges:
            kappa=mp.mpf(kstr)
            S=covariance(n,kappa)
            Q=S**-1
            q,t=explicit_inverse_first_row(n,kappa)
            for i in range(n):
                for j in range(n):
                    d=(j-i)%n
                    scale=max(1,abs(Q[i,j]),abs(q[d]))
                    assert abs(Q[i,j]-q[d])/scale < mp.mpf('1e-45'), (n,kstr,i,j,Q[i,j],q[d])
                    test_count+=1
                    if i!=j:
                        dist=min(d,n-d)
                        assert Q[i,j]*(-1)**dist>0, (n,kstr,dist,Q[i,j])
                        test_count+=1
            # check Fourier multiplier independently from covariance eigenvalues
            a=kappa/n;r=mp.exp(-a)
            A=1-r**4-4*a*r*r
            B=2*r*(a*(1+r*r)-(1-r*r))
            for j in range(n):
                th=2*mp.pi*j/n
                D=1-2*r*mp.cos(th)+r*r
                eig=(A+B*mp.cos(th))/(4*kappa**3 * D**2)
                direct=sum(S[0,d]*mp.exp(-1j*th*d) for d in range(n))
                assert abs(eig-direct) < mp.mpf('1e-42')*max(1,abs(eig))
                test_count+=1
            if n>=4:
                assert all(q[d]!=0 for d in range(2,n-1))
            test_count+=1
    print('PASS:',test_count,'independently reconstructed precision, sign, and Fourier checks')
    # compare first- and second-order sampled inverse sparsity on one circle
    n=9;kappa=mp.mpf('3.3')
    r=mp.exp(-kappa/n); z=r**n
    c1=[(r**d+r**(n-d))/(1-z)/(2*kappa) for d in range(n)]
    S1=mp.matrix([[c1[(i-j)%n] for j in range(n)] for i in range(n)])
    Q1=S1**-1
    assert all(abs(Q1[0,d])<mp.mpf('1e-45') for d in range(2,n-1))
    print('PASS: order-one inverse is exactly nearest-neighbour in the control case')

if __name__=='__main__':
    run()
