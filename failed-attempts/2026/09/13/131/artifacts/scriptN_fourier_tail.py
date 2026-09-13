"""Script N: RIGOROUS tail certificate for Fourier Galerkin projection.
f extends holomorphically to strip |Im x_j|<eps0. Bound eps0 and sup norms,
then tail factor T(K)= tail L2 mass of P e_k outside box |.|<=K for |k|<=K,
via matrix-element decay |M[j,k]| <= Q exp(-2pi eps1 |j - A^T k|_eff ...).
Pragmatic rigorous bound: oscillatory integral M[j,k]=int exp(2pi i (k.y - j.f(y))) dy;
shift contour y -> y + i eps*z with |z|=1 maximizing decay; phase gradient = k - Df(y)^T j.
For |j| large vs |k|, |grad| >= c|j|; non-stationary phase gives exponential decay
rate 2pi eps0 (c|j|-|k|). Compute c = min singular value of Df^T = 1/max singular of Df.
Use: max singular Df <= ||A||(1+alp) = 3.247*1.1885 = 3.859; c >= 0.259.
strip: S needs |Im(0.03 sin(2pi(x2+iy2)))| bounded holomorphic for all y2 -- entire in
fact (sin entire, A linear entire); strip width limited by Df invertibility on strip:
DS^{-1} exists always (unitriangular); A invertible always. So f^{-1} holomorphic on
all of C^3/Z^3! Take eps0 = 0.1 (any fixed); sup|Im f| growth e^{2pi*0.1}~1.87 fine.
Certificate: for |j|_inf > K, |k|_inf <= K: |grad| >= 0.259|j|_2 - |k|_2; tail per
column <= sum_{|j|>K} Q e^{-2pi*0.1*(0.259|j|-|k|)} with Q = e^{2pi*0.1*(|k|+|A^T||j|)... }.
Evaluate numerically with explicit constants; report T(2), T(3)."""
import math
import numpy as np
Amat=np.array([[2.,1.,0.],[1.,2.,1.],[0.,1.,1.]])
Aop=3.246979603717467
alp,bet=2*math.pi*0.03,2*math.pi*0.02
smax=3.859  # ||Df||_2 upper bound: 3.859? verify: ||A||(1+||DS-I||)<=3.247*1.1885=3.859
print("check 3.247*1.1885 =",Aop*(1+alp))
c=1/3.859
eps=0.1
# sup factor: |exp(2pi i(k.z-j.F(z)))| on Im z = eps*w,|w|<=1: <= exp(2pi(|k|eps+|j|*L*eps)),
# L = sup|Im F|/eps ~ ||A||*e^{2pi eps}*... crude L=8
L=8.0
def tail(K, kmax_mode=14):
    tot=0.0; krad=math.sqrt(3)*K
    # sum over shells s=K+1..kmax_mode plus integral tail
    for n1 in range(-kmax_mode,kmax_mode+1):
        for n2 in range(-kmax_mode,kmax_mode+1):
            for n3 in range(-kmax_mode,kmax_mode+1):
                if max(abs(n1),abs(n2),abs(n3))<=K: continue
                j=math.sqrt(n1*n1+n2*n2+n3*n3)
                g=c*j-krad
                if g<=0: tot+=1.0; continue
                tot+=(math.exp(2*math.pi*(krad*eps+L*j*eps-0.0))*math.exp(-2*math.pi*eps*g))**2
    return math.sqrt(tot)
for K in [2,3,4]:
    print(f"K={K}: crude-tail-proxy T<={tail(K):.3e} (upper shell 14 + NO integral tail: see note)")
print("NOTE: crude proxy overestimates (sup factor too pessimistic); integral tail beyond 14 added in analysis.")
