import numpy as np
# larger GUE non-Hermitian simulation, recheck spectrum & edge
def gue2(n):
    X = np.zeros((n,n),dtype=complex)
    d = np.random.randn(n)/np.sqrt(n)
    X[np.diag_indices(n)] = d
    iu = np.triu_indices(n,1)
    z = (np.random.randn(len(iu[0]))+1j*np.random.randn(len(iu[0])))/np.sqrt(2*n)
    X[iu]=z
    X[(iu[1],iu[0])]=np.conj(z)
    return X

# IMPORTANT: s1,s2 selfadjoint (Hermitian): use Hermitian GUE. r is non-normal.
# earlier sim used Hermitian correctly. Check eigenvalues again with n=800.
np.random.seed(0)
n=800
S1=gue2(n); S2=gue2(n)
R=S1@S1 - S2@S2 + S1@S2
evR=np.linalg.eigvals(R)
print("real range",evR.real.min(),evR.real.max())
print("imag range",evR.imag.min(),evR.imag.max())
# frac in right lobe beyond 3.0?
print("frac Re>3.2:",np.mean(evR.real>3.2),"Re<-3.2:",np.mean(evR.real<-3.2))
# gap: histogram of Re
H,edges=np.histogram(evR.real,bins=50,range=(-4,4))
for h,e in zip(H,edges):
    print(f"{e:6.2f} {h:4d} {'#'*int(h/3)}")
print("imag hist")
H2,e2=np.histogram(evR.imag,bins=30)
for h,e in zip(H2,e2):
    print(f"{e:7.3f} {h:4d}")
# modulus: support radius
print("max |z|",np.max(np.abs(evR)), "quantiles",np.quantile(np.abs(evR),[0.9,0.95,0.99,1.0]))
np.save("output/artifacts/evR800.npy",evR)
