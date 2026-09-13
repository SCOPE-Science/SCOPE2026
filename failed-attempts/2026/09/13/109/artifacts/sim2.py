import numpy as np

def gue(n):
    # GUE normalized: semicircle radius 2, var 1: E[|Xij|^2]=1/n for i!=j, E[Xii^2]=1/n? Actually diagonal var 1/n? For semicircle var 1 need entries var 1/n.
    A = np.random.randn(n,n)+1j*np.random.randn(n,n)
    A = (A+A.conj().T)/2/np.sqrt(2*n)
    # check var: for i!=j, Aij=(Zij+conj(Zji))/2/sqrt(2n), Zij~N(0,1)+iN(0,1) var E|Z|^2=2. So E|Aij|^2 = (2+2)/4/(2n)=1/(2n)?? Hmm factor 2 off.
    # Let's instead construct directly: diag N(0,1/n), off-diag (N+iN)/sqrt(2n)
    return A

def gue2(n):
    X = np.zeros((n,n),dtype=complex)
    d = np.random.randn(n)/np.sqrt(n)
    X[np.diag_indices(n)] = d
    iu = np.triu_indices(n,1)
    z = (np.random.randn(len(iu[0]))+1j*np.random.randn(len(iu[0])))/np.sqrt(2*n)
    X[iu]=z
    X[(iu[1],iu[0])]=np.conj(z)
    return X

# verify spectrum
n=400
import sys
X=gue2(n)
ev=np.linalg.eigvalsh(X)
print("spec range",ev.min(),ev.max(), "mean sq", np.mean(ev**2))

# Now r
S1=gue2(n); S2=gue2(n)
R=S1@S1 - S2@S2 + S1@S2
evR=np.linalg.eigvals(R)
print("eig R: real range",evR.real.min(),evR.real.max(),"imag range",evR.imag.min(),evR.imag.max())
np.save("/tmp/evR.npy", evR)
# histogram: count near 0 vs gap?
# check number with |z|<0.5, annulus?
for rad in [0.3,0.5,1.0,1.5,2.0]:
    print(rad, np.mean(np.abs(evR)<rad))
# check real projection histogram
import collections
reals=np.sort(evR.real)
print("real quantiles", np.quantile(evR.real,[0,.1,.25,.5,.75,.9,1.0]))
print("imag quantiles", np.quantile(evR.imag,[0,.1,.25,.5,.75,.9,1.0]))
# gap detection: sort by real, look for empty intervals
H,edges=np.histogram(evR.real,bins=40)
print(H)
H2,edges2=np.histogram(evR.imag,bins=40)
print(H2)
# 2D histogram
Hxy,xe,ye=np.histogram2d(evR.real,evR.imag,bins=[30,30])
# print rows with zero density in middle?
print(Hxy[:,15])
print(Hxy[15,:])
