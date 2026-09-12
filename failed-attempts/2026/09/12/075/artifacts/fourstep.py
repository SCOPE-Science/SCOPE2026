"""4-step prefactor: Z_n(x,y) = K_n(x,y) Z_{n-4}(x,y), K_n explicit monomial.
Two double-steps: each double-step Z_m = D_m * Z_{m-2}(T(params)), D_m = explicit.
Double-step prefactor: shuffle1 Deltas: (2x^2)^E (2y^2)^O [E=ceil(m^2/2), O=floor(m^2/2)] times f1=1;
shuffle2 (on B-pattern (p,q)=(1/(2x),1/(2y))): Deltas per face = 2pq (all faces! since alternating (p,q,q,p): ac+bd = pq+qp=2pq).
  # faces of Aztec_{m-1} = (m-1)^2. So D2 = (2pq)^{(m-1)^2} = (1/(2xy))^{(m-1)^2}. times f2=1.
After double-step, params T(x,y), graph needs GAUGE to match standard normalization? T-params are the actual face weights (read via iso) — no gauge needed if iso-face-weights match convention. But the iso might FLIP parity (even↔odd) — since T flips ratio, parity flips are absorbed in (x,y) order. Also possible global vertex-gauge discrepancy: gauge changes Z by product of vertex factors; if the reduced graph's weights equal T-face-weights EXACTLY (we read 1.08532 = X'' exactly), no gauge needed. ✓ (verified numerically for n=3.)
So: Z_m(x,y) = (2x^2)^E_m (2y^2)^O_m (2pq)^{(m-1)^2} Z_{m-2}(X,Y), (X,Y)=T(x,y), (p,q)=(1/(2x),1/(2y)).
Two double-steps: Z_n = D(n)D(n-2) * (gauge T^2: T^2(x,y)=λ(x,y), λ=4x^2y^2/(x^2+y^2)^2) Z_{n-4}(λx,λy).
Z_{n-4}(λx,λy) = λ^{(n-4)(n-3)} Z_{n-4}(x,y) [homogeneity: degree = #dimers = #white = (n-4)(n-3)].
Thus K_n = D(n) D(n-2) λ^{(n-4)(n-3)}. Take logs and verify against closed form: log K_n =?= 8F0(n-2)+4F1 (for y=1).
"""
import math
def logK(n,x,y):
    E=(n*n+1)//2; O=n*n-E
    lD1=E*math.log(2*x*x)+O*math.log(2*y*y)
    p,q=1/(2*x),1/(2*y)
    lD2=(n-1)*(n-1)*math.log(2*p*q)
    X,Y=2*x*y*y/(x*x+y*y), 2*x*x*y/(x*x+y*y)
    m=n-2
    E2=(m*m+1)//2; O2=m*m-E2
    lD3=E2*math.log(2*X*X)+O2*math.log(2*Y*Y)
    P,Q=1/(2*X),1/(2*Y)
    lD4=(m-1)*(m-1)*math.log(2*P*Q)
    lam=4*x*x*y*y/(x*x+y*y)**2
    lg=(n-4)*(n-3)*math.log(lam)
    return lD1+lD2+lD3+lD4+lg
from validate_ops import build_aztec_cj, brute_Z
for a in [0.3,0.5,0.7]:
    print(f"--- a={a} ---")
    for n in [6,8,10]:
        print(f"  n={n}: logK={logK(n,a,1):.9f} actual={math.log(brute_Z(build_aztec_cj(n,a,1))/brute_Z(build_aztec_cj(n-4,a,1))):.9f}")
