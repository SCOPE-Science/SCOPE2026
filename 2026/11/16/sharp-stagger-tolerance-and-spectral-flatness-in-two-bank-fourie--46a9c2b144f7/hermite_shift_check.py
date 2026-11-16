"""Independent finite checks for shifted two-bank Fourier–Hermite sampling.
Run: python hermite_shift_check.py (NumPy required).
"""
import numpy as np

def full_matrix(m, shift, weight):
    freqs=np.arange(-m,m)
    j=np.arange(m)
    x=j/m
    z=(j+shift)/m
    top=np.exp(2j*np.pi*x[:,None]*freqs[None,:])/np.sqrt(m)
    deriv=(freqs[None,:]/m)*np.exp(2j*np.pi*z[:,None]*freqs[None,:])/np.sqrt(m)
    return np.vstack([top,weight*deriv])

def fibers(m, shift, weight):
    result=[]
    for k in range(m):
        s=k/m
        F=np.array([[1,1],[weight*s*np.exp(2j*np.pi*s*shift),
                  weight*(s-1)*np.exp(2j*np.pi*(s-1)*shift)]],complex)
        result.extend(np.linalg.svd(F,compute_uv=False))
    return np.sort(np.array(result))

checks=0
for m in range(1,33):
    umax=(m*m//4)/(m*m)
    bound=.5-umax/4
    for shift in [0,.05,.16,.229,.235,.28,.4,.5,.68,.9,1.0]:
        for weight in [.25,1,np.sqrt(2),2.8]:
            s=np.linalg.svd(full_matrix(m,shift,weight),compute_uv=False)
            f=fibers(m,shift,weight)
            np.testing.assert_allclose(np.sort(s),f,atol=4e-12,rtol=5e-12)
            checks+=1
        f=fibers(m,shift,np.sqrt(2))
        critical=1-1/np.sqrt(2)
        if m%2==0 and abs(shift-.5)<1e-12:
            assert f[0]<1e-12
            checks+=1
        else:
            kappa=f[-1]/f[0]
            optimal=1+np.sqrt(2)
            if m==1 or np.sin(np.pi*shift)**2<=critical+1e-12:
                assert abs(kappa-optimal)<1e-10,(m,shift,kappa)
            else:
                assert kappa>optimal+1e-7,(m,shift,kappa)
            q=np.sin(np.pi*shift)**2
            u=(m*m//4)/(m*m)
            tau=4*(1-u); det=2*(1-4*u*q)
            lammin=(tau-np.sqrt(max(0,tau*tau-4*det)))/2
            expected=np.sqrt((2+np.sqrt(2))/min(2-np.sqrt(2),lammin))
            assert abs(kappa-expected)<1e-9,(m,shift,kappa,expected)
            checks+=1
    # Critical phase meets the second sharp lower-eigenvalue contact.
    if m>1:
        alph=np.arcsin(np.sqrt(1-1/np.sqrt(2)))/np.pi
        sv=fibers(m,alph,np.sqrt(2))
        assert abs(sv[-1]/sv[0]-(1+np.sqrt(2)))<1e-11
        checks+=1
print('HERMITE_SHIFT_CHECKS_PASS',checks)
