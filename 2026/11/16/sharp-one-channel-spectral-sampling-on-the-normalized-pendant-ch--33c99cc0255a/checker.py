"""Supplementary finite-frequency checks for normalized decorated-path sampling."""
import numpy as np
import sympy as sp

root3=sp.sqrt(3)
u_left=sp.Matrix([sp.Rational(1,2),root3/2]); u_right=sp.Matrix([root3/2,sp.Rational(1,2)])
dot=sp.simplify((u_left.T*u_right)[0])
assert dot==root3/2
optimal=sp.simplify((1+dot)/2)
assert optimal==(2+root3)/4
w=sp.Matrix([1,1])/sp.sqrt(2)
for u in (u_left,u_right):
 assert sp.simplify((w.T*u)[0]**2)==optimal
assert sp.simplify((u_left.T*u_left)[0])==1
assert sp.simplify((u_right.T*u_right)[0])==1

def upper(c):
    lam=(c+np.sqrt(c*c+3))/3
    return np.array([np.sqrt(3)*lam,1],dtype=float)/np.sqrt(1+3*lam*lam)

def val(c,w):
    u=upper(c)
    return abs(np.vdot(w,u))**2

rng=np.random.default_rng(91023)
count=0
for cutoff in (0.08,0.25,0.6,0.75,1.0,4/3):
    if cutoff < 2/3:
       eig=1-cutoff
       cmin=(3*eig**2-1)/(2*eig)
    else:cmin=-1
    um=upper(cmin); up=upper(1)
    middle=(um+up)/np.linalg.norm(um+up)
    bound=(1+np.dot(um,up))/2
    for c in np.linspace(cmin,1,257):
       assert val(c,middle)>=bound-1e-13
       assert val(c,middle)<=1+1e-13
       assert abs(val(c,np.array([1,1j])/np.sqrt(2))-.5)<1e-12
       count+=2
    for k in range(100):
       v=rng.normal(size=2)+1j*rng.normal(size=2)
       v/=np.linalg.norm(v)
       assert min(val(cmin,v),val(1,v))<=bound+1e-12
       count+=1

# The Toeplitz fiber is diagonalized directly, independent of the closed-form eigenvectors.
for theta in np.linspace(-np.pi,np.pi,601):
    c=np.cos(theta)
    block=np.array([[2*c/3,1/np.sqrt(3)],[1/np.sqrt(3),0]])
    eigs,vecs=np.linalg.eigh(block)
    assert np.allclose(eigs,[ (c-np.sqrt(c*c+3))/3, (c+np.sqrt(c*c+3))/3],atol=1e-13)
    u=upper(c)
    assert np.linalg.norm(block@u-eigs[1]*u)<1e-12
    assert abs(np.vdot(vecs[:,1],u))>1-1e-12
    count+=3

# Construct a nontrivial multichannel signal on a finite periodic comb, then test its samples.
for n in (16,32,80,256):
    angles=2*np.pi*np.arange(n)/n
    h=rng.normal(size=n)+1j*rng.normal(size=n)
    F=np.array([upper(np.cos(t))*h[k] for k,t in enumerate(angles)])
    f=np.fft.ifft(F,axis=0,norm='ortho')
    yq=(f[:,0]+1j*f[:,1])/np.sqrt(2)
    yr=(f[:,0]+f[:,1])/np.sqrt(2)
    lhs=np.linalg.norm(f)**2
    assert abs(np.linalg.norm(yq)**2-lhs/2)<3e-12*lhs
    assert np.linalg.norm(yr)**2>=float(optimal)*lhs-3e-12*lhs
    count+=2
print('PASS',count,'fiber and signal checks; exact endpoint identities')
