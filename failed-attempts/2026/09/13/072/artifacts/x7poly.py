"""Compute X'-coordinates of 7-torsion via x(3P)=x(4P) rational equation; filter exact order 7."""
import numpy as np
a2,a4,a6=-12.0,37.333333333333336,-29.037037037037038
b2=4*a2; b4=2*a4; b6=4*a6; b8=4*a2*a6-a4**2
def padd(*fs):
    n=max(len(f) for f in fs); o=np.zeros(n)
    for f in fs: o[:len(f)]+=f
    return o
def pmul(f,g): return np.convolve(f,g)
f=np.array([a6,a4,a2,1.0])
x=np.array([0.,1.])
H2=4*f
S=padd(2*np.array([0,0,0,0,0,0,1.0]), b2*np.array([0,0,0,0,0,1.0]), 5*b4*np.array([0,0,0,0,1.0]), 10*b6*np.array([0,0,0,1.0]), 10*b8*np.array([0,0,1.0]), (b2*b8-b4*b6)*np.array([0,1.0]), np.array([b4*b8-2*b6**2]))
H3=padd(3*np.array([0,0,0,0,1.0]), b2*np.array([0,0,0,1.0]), 3*b4*np.array([0,0,1.0]), 3*b6*np.array([0,1.0]), np.array([b8]))
# x3 = N3/D3, N3 = 2 x H3 - H2 S ... careful: x3 = x - H2 S/(2 H3)?? verify: psi2 psi4 = psi2^2 S/2 = H2 S/2 (as functions: psi2^2=H2). x3 = x - psi2 psi4/psi3^2 = x - (H2 S/2)/H3. Yes.
N3=psub2=padd(pmul(2*x,H3), -pmul(H2,S)/2.0) if False else None
def psub(f,g):
    n=max(len(f),len(g)); o=np.zeros(n); o[:len(f)]+=f; o[:len(g)]-=g; return o
N3=psub(pmul(padd(2*x),H3), pmul(H2,S)/2.0)
D3=2*H3
print("deg N3:",len(N3)-1,"deg D3:",len(D3)-1)
# compose x4 = N2(x3)/D2(x3), N2=x^4-2a4x^2-8a6x+(a4^2-4a2a6), D2=4f
cN2=np.array([a4**2-4*a2*a6, -8*a6, -2*a4, 0.0, 1.0]); cD2=4*f
def compose(c, N, D):
    # c(N/D) = sum c_k N^k D^{m-k} / D^m
    m=len(c)-1; num=np.array([0.]); Dpows=[np.array([1.])]; Npows=[np.array([1.])]
    for i in range(1,m+1): Dpows.append(pmul(Dpows[-1],D)); Npows.append(pmul(Npows[-1],N))
    for k in range(m+1): num=padd(num, pmul(c[k]*Npows[k], Dpows[m-k]))
    return num, Dpows[m]
N4d, D4d = compose(cN2, N3, D3)  # x4 = N4d/D4d
N4e, D4e = compose(cD2, N3, D3)
print("deg x4num:",len(N4d)-1,"deg x4den:",len(N4e)-1)
# x3 = x4  <=> N3*D4e - N4d*D3... wait x3=N3/D3, x4=N4d/D4e(after common denom? N4d,D4e have different degrees: N4d deg 4*9=36, D4e = compose of cubic: deg 3*9=27. equation: N3*D4e - D3*N4d = 0.
E = psub(pmul(N3,D4e), pmul(D3,N4d))
print("deg E:",len(E)-1)
# remove extraneous factors: H3 (poles, 3-torsion), f (2-torsion, doubling poles), H2? and gcd with... divide out H3 powers and f powers
def deflate(E, F):
    E=E.copy()
    while True:
        q,r=np.polydiv(np.poly1d(E[::-1]),np.poly1d(F[::-1]))
        if np.max(np.abs(r.coeffs))<1e-6*np.max(np.abs(E)): E=q.coeffs[::-1]
        else: break
    return E
E1=deflate(E,H3); print("after H3:",len(E1)-1)
E2=deflate(E1,f); print("after f:",len(E2)-1)
E3=deflate(E2,H3); print("after H3 again:",len(E3)-1)
print("expect deg 24 (H7/2: X-coords of primitive 7-torsion: (49-1)/2=24).")
rts=np.roots(np.poly1d(E3[::-1]))
print("roots:",np.sort_complex(rts))
np.save("output/artifacts/X7coords.npy",rts)
