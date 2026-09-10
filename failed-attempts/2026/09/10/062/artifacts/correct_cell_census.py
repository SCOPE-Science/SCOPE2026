# Correct-cell census for FALLBACK: tmf-based ASS for sphere E2 = Ext_{A//E? }...
# Standard identification: tmfASS E2^{s,t}(S) = Ext^{s,t}_{A//A(2)}?? No:
# tmf-resolution E1 = Ext_A(H^*tmf^{tensor}) ; the tmf-ASS E2 = Ext_{A(2)_*}(F2, F2 tensor ...)?
# Careful, auditable statement: tmf-ASS for X has E2 = Ext_{A_*}(H_*tmf tensor H_*X)? The standard:
#   E_2^{s,t}(X) = Ext^{s,t}_{A(2)_*}(F2, H_*(tmf \wedge X))... for X=S: H_*(tmf)=A_*//A(2)? No: H^*tmf = A//A(2) as A-modules, so H_*tmf = (A//A(2))_* = A_* \square_{A(2)_*} F2 (cotensor).
# So E2(S) = Ext_{A_*}(F2, H_*tmf) = Ext_{A_*}(F2, A_*\square F2) \cong Ext_{A(2)_*}(F2,F2) by change-of-rings!
# ==> The tmf-ASS E2 for the sphere IS Ext_{A(2)}(F2,F2) (Shapiro/change-of-rings). Our recomputation was the RIGHT algebra after all; the 'wrong coalgebra' worry in target_exit was mistaken.
# Verify consistency: known Ext_{A(2)} chart: classes in stems 52-56?
# Compute Poincare series of A//A(2) to cross-check cell size: P(A//A(2)) = P(A_*)/P(A(2)_*) as graded vec spaces (free over A(2)).
# dim A(2)_* = 64. P(A_*,t) = prod_{i>=1}(1-t^{2^i-1})^{-1}.
# Then (A//A(2))_d dims for d<=56 via series division.
from fractions import Fraction
N=60
# series for A_* dual: product over i=1..6 of 1/(1-t^{2^i-1})
import sympy as sp
t=sp.Symbol('t')
P=1
for i in range(1,7):
    d=2**i-1
    # truncate series: sum_{k>=0} t^{kd} up to N
    s=sum(t**(k*d) for k in range(N//d+1))
    P=sp.expand(P*s)
cA=sp.Poly(P,t).all_coeffs()[::-1]
cA += [0]*(N+1-len(cA))
# A(2) dims to degree <=23 (64-dim, zero above 23)
b2={0:1,1:1,2:1,3:2,4:2,5:2,6:3,7:4,8:3,9:4,10:5,11:4,12:4,13:5,14:4,15:3,16:4,17:3,18:2,19:2,20:2,21:1,22:1,23:1}
# quotient dims q_d = cA_d - sum_{i>=1} b2_i q_{d-i} (free module division)
q=[0]*(N+1)
for d in range(N+1):
    s=cA[d] if d < len(cA) else 0
    for i in range(1,min(d,23)+1):
        s-=b2.get(i,0)*q[d-i]
    q[d]=s
print("A_* dims d=0..12:", [cA[d] for d in range(13)])
print("A//A(2) dims d=0..16:", q[:17])
print("A//A(2) dims d=50..56:", q[50:57])
# change-of-rings check: E2(tmfASS sphere) = Ext_{A(2)}(F2,F2): our s=1..4 census applies DIRECTLY.
# Classical known Ext_{A(2)}: polynomial generators... check first nonzero stem>=52 at low s from our kernel data:
print("ker3(t)=0 t=55..59 => Ext^3=0 there; ker4-im3: H^4(t)=ker4(t)-dimC3(t) with dimC3(t)=[1014..39]")
print("H^4(59)=315-315=0? ker4(t=59)=315 (stem55 s4) yes => Ext^4(stem55)=0.")
