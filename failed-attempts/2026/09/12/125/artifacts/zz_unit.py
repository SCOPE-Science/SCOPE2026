import numpy as np
def B3(x):
    x=np.asarray(x,float); ax=np.abs(x); o=np.zeros_like(x)
    m1=ax<1; o[m1]=(4-6*x[m1]**2+3*ax[m1]**3)/6
    m2=(ax>=1)&(ax<=2); o[m2]=(2-ax[m2])**3/6
    return o
a=0.5; b=11/6; p=11; q=12
# Zak of B3 with period a: Za(x,nu)=sum_k B3(x-a k)e^{2pi i k nu}
def Za(x,nu):
    tot=0j
    for k in range(-8,9):
        tot+=B3(np.array([x-a*k]))[0]*np.exp(2j*np.pi*k*nu)
    return tot
# ZZ matrix Z[r,s]=Za(x + s/q *? ...) standard: rows r=0..p-1, cols s=0..q-1? Here p=11 should give 11x12.
# Convention: x in [0,a/q)? Let's build G directly as Gram: G = (1/b) Z Z*? Check constants.
# Our tau formula: G_tilde[r,r']=2 sum_s exp(2pi i s(r-r')/12) A_r conj(A_r'), r,r'=0..10.
# Let's scan its min eig vs direct: direct S min ~0 suggests different normalization.
# Recompute Gmat with proper Zak Tr of period q*a? different conventions -> factor q.
# Instead test: is lambda_min(G_tilde)/b == frame bound? G_tilde already includes factor?
# Let's compute lambda_min(G_tilde) map: earlier ~1.036 -> /b ~0.565. But fiber M gave ~0 -> contradiction means one of the two matrices wrong by covering/wrapping.
# Key check: direct S on finite box will have artificial boundary near-zero (edge vectors lose mass) -> min->0 spuriously. Check interior: compute smallest eig restricted / or count near-zero.
# Count eigenvalues < 0.1
e=np.load("output/artifacts/direct_eig.npy")
print("count<0.01:",np.sum(e<0.01),"count<0.1:",np.sum(e<0.1),"count<0.5:",np.sum(e<0.5))
# localization of lowest eigenvector
