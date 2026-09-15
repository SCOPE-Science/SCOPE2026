"""Pointwise admissibility obstruction for entropy-anchored Weyl-pinching gap.
Verifies:
 (1) Ricci data at a putative f-minimum with s=lambda1+lambda2<0, R>0,
     Hess f = 1/2 g - Ric >= 0, and W=0 satisfying Zhang pinch strictly.
 (2) S2xR2 (radius sqrt(2) x R^2) saturates gamma = 1+sqrt(3).
Norms use Frobenius (full-sum) convention consistently on both sides.
"""
import math

def ric0_norm(lams):
    R = sum(lams)
    m = R/4.0
    return math.sqrt(sum((x-m)**2 for x in lams)), R

# (1) Counterexample data at f-minimum
lams = [-1.0, 0.5, 0.5, 0.5]
n0, R = ric0_norm(lams)
s = lams[0]+lams[1]
hess = [0.5-x for x in lams]
threshold = abs(n0 - R/(2*math.sqrt(3)))
print(f"Ric eigs: {lams}")
print(f"R={R}, s=lambda1+lambda2={s}, s/R={s/R}")
print(f"|Ric0|={n0:.6f}, R/(2sqrt3)={R/(2*math.sqrt(3)):.6f}, diff={threshold:.6f}")
print(f"Hess eigs={hess}, Hess>=0: {all(h>= -1e-12 for h in hess)}")
print(f"W=0 satisfies |W|<=gamma*diff for every gamma>=0: {threshold>0}")
print(f"Gap violated for any c>0 since s={s}<0<R={R}")
assert R>0 and s<0 and all(h>=-1e-12 for h in hess) and threshold>0

# (2) S2xR2 saturation
# Ricci eigs (1/2,1/2,0,0), R=1
lams2 = [0.5,0.5,0.0,0.0]
n02, R2 = ric0_norm(lams2)
diff2 = abs(n02 - R2/(2*math.sqrt(3)))
# |W| for S2xR2: components 1/6,1/6,-1/12 x4 -> full-sum norm sqrt(1/3)
Wnorm = math.sqrt(1.0/3.0)
ratio = Wnorm/diff2
print(f"\nS2xR2: |Ric0|={n02:.6f}, diff={diff2:.6f}, |W|={Wnorm:.6f}, ratio={ratio:.6f}")
print(f"1+sqrt(3)={1+math.sqrt(3):.6f}")
assert abs(ratio-(1+math.sqrt(3)))<1e-9, "saturation check failed"

# (3) S3xR check: ratio s/R = 1/3, W=0, diff=0 (cone vertex)
lams3 = [0.5,0.5,0.5,0.0]
n03, R3 = ric0_norm(lams3)
diff3 = abs(n03 - R3/(2*math.sqrt(3)))
s3 = lams3[0]+lams3[1] if False else sorted(lams3)[0]+sorted(lams3)[1]
print(f"\nS3xR: R={R3}, s={s3}, s/R={s3/R3:.6f}, diff={diff3:.2e} (vertex, W=0 admissible)")
print("\nPASS: pointwise algebraic step cannot force gap; global sign recovery needed.")
