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
for N in [30,40]:
    p=spec(cd,N); a=spec(cd,N,half=True)
    print(f"N={N} per[0:8]=", [f"{v:.10f}" for v in p[:8]])
    print(f"N={N} anti[0:8]=", [f"{v:.10f}" for v in a[:8]])
# Hill band edges standard ordering: E0(per) < E1(anti) <= E2(anti) < E3(per) <= E4(per) < ...
# Identify: E0=0.9673(per), E1=1.3222(anti), E2=2.2740(anti), E3=3.9991(per), E4=4.0817(per) => second gap = (E3,E4)? width .082
# Target says E3^-,E3^+ with width in [1e-3,0.5] -> matches (3.999,4.0817) width ~0.0826 >= 1e-3. 
# But 7.59 pair width 0.0018, 12.61 pair width 7.6e-5.
# So the "first collapsed gap" of TRUE lame: for m=1, per pairs (3.4284,3.4284) closed. Under u0=2sn^2 it's already open at 0.0816!
# and u* keeps it open 0.0826. Hmm so "first collapsed gap" from whose perspective?
