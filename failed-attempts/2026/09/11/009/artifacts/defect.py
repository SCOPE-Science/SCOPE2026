import numpy as np
L=3.7081493546027438
us=np.load("lane_work/ugrid.npy"); M=len(us)
Uh=np.fft.rfft(us)/M
k0=2*np.pi/L
def spec(cd,N,half=False):
    dim=2*N+1; H=np.zeros((dim,dim)); kk=float(k0)
    for i in range(dim):
        n=i-N
        q=(n+0.5)*kk if half else n*kk
        H[i,i]=q*q+cd[0]
        for j in range(dim):
            d=n-(j-N)
            if d!=0 and abs(d) in cd: H[i,j]+=cd[abs(d)]
    return np.sort(np.linalg.eigvalsh(H))
cd={n: float(Uh[n].real) for n in range(100)}
N=30
p=spec(cd,N); a=spec(cd,N,half=True)
E0=p[0]; E1=a[0]; E2=a[1]; Em=p[1]; Ep=p[2]
mean=float(np.mean(us))
print(f"E0={E0:.10f} E1={E1:.10f} E2={E2:.10f} Em={Em:.10f} Ep={Ep:.10f} mean={mean:.10f}")
# Dirichlet on [0,L]: matrix in sine basis via quadrature (scout, N=12)
xs=np.linspace(0,L,M,endpoint=False); h=L/M
ND=12
gg=np.zeros((M,ND))
for n in range(1,ND+1):
    gg[:,n-1]=np.sqrt(2/L)*np.sin(n*np.pi*xs/L)
V=(gg*us[:,None]).T @ gg * h
T=np.diag([(n*np.pi/L)**2 for n in range(1,ND+1)])
w=np.sort(np.linalg.eigvalsh(T+V))
mu1=w[0]
print("mu1=", mu1)
# candidate defect: d1 = |E0+E1+E2-2*mu1-mean|
d1=abs(E0+E1+E2-2*mu1-mean)
print("d1 candidate =", d1)
# also print Dirichlet list vs periodic/antiperiodic for interlacing sanity
print("dir:", np.round(w[:6],6))
print("per:", np.round(p[:5],6))
print("ant:", np.round(a[:5],6))
