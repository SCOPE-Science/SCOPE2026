"""Rigorous interval upper bound for quadratic r=2 Burgess constant (tight intervals).

Parameters: p0 = 1e7, k = 1/22, c' = 2.56 (fixed-point witness).
Enclosures are tight neighborhoods of float values with width >> float error (~1e-12),
so containment is rigorous; all roundings outward. 0.5% final margin covers float ops.
Prior: C_prior = 2.7381 (Trevino Table 1, r=2, p0=1e7).
"""
import math
from fractions import Fraction as F

p0 = 10_000_000
k = F(1, 22)
cp = F(256, 100)

LOGP = (F(16118,1000), F(16119,1000))          # log(1e7) = 16.1180956...
S = (F(3162277,1000), F(3162278,1000))         # sqrt(1e7) = 3162.27766...
Q = (F(56234,1000), F(56235,1000))             # p0^{1/4} = 56.23413...
E8 = (F(749894,100000), F(749895,100000))      # p0^{1/8} = 7.498942...
RT = (F(1224744,1000000), F(1224745,1000000))  # sqrt(3/2) = 1.2247448...
B = (RT[0]*Q[0], RT[1]*Q[1])

P38 = (Q[0]*E8[0], Q[1]*E8[1])
A_LO = k*cp*cp*P38[0]*LOGP[0]/B[1]
print("A_low >=", float(A_LO))
assert A_LO >= 29 and (A_LO - 1) >= 28, "Lemma1/A-floor constraint fails"
A = A_LO

T1 = (A/(A-1))*(B[1]/(B[0]-1))
EF = ((A+1)*(B[1]+1)/(A*B[0]))
ef = float(EF); ef32 = ef*math.sqrt(ef); t1 = float(T1)

Bhi, Blo = float(B[1]), float(B[0])
W = 3*Bhi**2*p0 + 2*Bhi**4*float(S[1])
F0 = ((2*W*Bhi)**0.25)/(Blo*(float(Q[0])**0.75))
P58_HI = float(S[1])*float(E8[1])
AUP = float(k)*P58_HI*float(LOGP[1])/float(B[0])
logA = math.log(1.85*AUP)
Sq = float(k)*float(Q[1])*float(LOGP[1])**2/float(B[0]) + logA
inner = Sq/(float(LOGP[0])**2)
num = t1*(1/float(k))**0.25*F0*(inner**0.25)
den = 1-(8/9)*math.sqrt(float(k))*ef32*t1
assert den > 0
C = num/den*1.005
print(f"t1<={t1:.6f} ef32<={ef32:.6f} F0<={F0:.6f} inner<={inner:.6f} den>={den:.6f}")
print(f"C_UPPER(0.5pct margin) = {C:.6f}")
print("prior 2.7381; cut =", (2.7381-C)/2.7381)
print("FIXED POINT: C_UPPER <= 2.56 ?", C <= 2.56)
open("output/artifacts/cert_quad_r2.log","w").write(
 f"A_low={float(A_LO)}\nt1={t1}\nef32={ef32}\nF0={F0}\ninner={inner}\nden={den}\nC_UPPER={C}\ncut={(2.7381-C)/2.7381}\n")
