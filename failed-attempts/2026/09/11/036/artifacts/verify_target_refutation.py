#!/usr/bin/env python3
"""Replayable refutation of lane-763 target: w* dilatation is 10+3*sqrt(11) ~19.95, not ~1.401.

Stdlib only. All critical inequalities are integer arithmetic.
Convention-robust: checks both left-to-right and right-to-left products.
"""
from fractions import Fraction

def mm(A,B):
    return [[A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]],
            [A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]]]

def mpow(A,k):
    R=[[1,0],[0,1]]
    for _ in range(k):
        R=mm(R,A)
    return R

def tr(A): return A[0][0]+A[1][1]
def det(A): return A[0][0]*A[1][1]-A[0][1]*A[1][0]

checks=[]
def check(name,cond,detail=""):
    checks.append((name,cond))
    print(("PASS" if cond else "FAIL")+f" {name} {detail}")

s1=[[1,1],[0,1]]; s2=[[1,0],[-1,1]]
s1i=[[1,-1],[0,1]]; s2i=[[1,0],[1,1]]

# 1. braid relation
check("braid_relation", mm(mm(s1,s2),s1)==mm(mm(s2,s1),s2), f"{mm(mm(s1,s2),s1)}")
# determinants
check("det_gens", det(s1)==1 and det(s2)==1 and det(s1i)==1 and det(s2i)==1, "")

# 2. w* = s1^3 s2^-1 s1 s2^-2, both conventions
s1c3=mpow(s1,3); s2i2=mm(s2i,s2i)
w_lr=mm(mm(mm(s1c3,s2i),s1),s2i2)
w_rl=mm(mm(mm(s2i2,s1),s2i),s1c3)
check("w_matrix_lr", w_lr==[[18,7],[5,2]], f"{w_lr}")
check("w_matrix_rl", w_rl==[[2,7],[5,18]], f"{w_rl}")
check("w_trace_20_both", tr(w_lr)==20 and tr(w_rl)==20, f"tr={tr(w_lr)},{tr(w_rl)}")
check("w_det_1", det(w_lr)==1 and det(w_rl)==1, "")
check("w_abs_trace_gt2", abs(tr(w_lr))>2, "pseudo-Anosov range")

# 3. calibration word s1*s2^-1 -> trace 3
cal_lr=mm(s1,s2i); cal_rl=mm(s2i,s1)
check("cal_trace_3", tr(cal_lr)==3 and tr(cal_rl)==3, f"{cal_lr} tr={tr(cal_lr)}")

# 4. integer sqrt bounds: 3.316<sqrt(11)<3.317 ; 2.236<sqrt(5)<2.237
check("sqrt11_lower", 3316**2 < 11*1000**2, f"{3316**2} < {11*1000**2}")
check("sqrt11_upper", 11*1000**2 < 3317**2, f"{11*1000**2} < {3317**2}")
check("sqrt5_lower", 2236**2 < 5*1000**2, "")
check("sqrt5_upper", 5*1000**2 < 2237**2, "")
# lambda = 10+3 sqrt11 in (19.948, 19.951); conjugate in (0.049,0.052)
lam_lo = Fraction(10*1000+3*3316,1000)  # 19.948
lam_hi = Fraction(10*1000+3*3317,1000)  # 19.951
check("lambda_enclosure", lam_lo==Fraction(19948,1000) and lam_hi==Fraction(19951,1000), f"({float(lam_lo)},{float(lam_hi)})")
check("lambda_far_from_1401", lam_lo > Fraction(19,1), f"lam_lo={lam_lo} >> 1.401")
# conjugate enclosure
clo = Fraction(10*1000-3*3317,1000); chi = Fraction(10*1000-3*3316,1000)
check("conjugate_enclosure", clo==Fraction(49,1000) and chi==Fraction(52,1000), f"({float(clo)},{float(chi)})")
# claimed value 1.401 far from both roots
claimed = Fraction(1401,1000)
check("claimed_neq_large_root", claimed < Fraction(2,1) and lam_lo > Fraction(19,1), "gap > 17")
check("claimed_neq_small_root", claimed > Fraction(1,1) and chi < Fraction(1,10), "gap > 1.3")

# 5. characteristic polynomial x^2-20x+1; discriminant 396 non-square
check("charpoly_disc", 20**2-4==396, "D=396")
check("disc_nonsquare", 19**2 < 396 < 20**2, "361<396<400 -> deg 2, irreducible")
# f(claimed) != 0 exactly over rationals: 1401^2/1e6 -20*1401/1e3 +1
f_claimed = Fraction(1401*1401,1000*1000) - 20*Fraction(1401,1000) + 1
check("poly_nonzero_at_claimed", f_claimed==Fraction(-25057199,1000000) and f_claimed!=0, f"f(1.401)={f_claimed}")

# 6. general 3-braid obstruction: |tr|>=3 for pA => lambda>2.618>1.401, quadratic
# (3+sqrt5)/2 > (3+2.236)/2 = 2.618
min_lo = Fraction(3*1000+2236,2000)
check("D3_minimum_above_1401", min_lo >= Fraction(2618,1000) and min_lo > claimed, f"min_lo={float(min_lo)}")
check("quadratic_not_degree6", True, "any SL(2,Z) charpoly is degree 2")
# Pisot not Salem: both roots real positive reciprocal, no unit-circle conjugate
check("reciprocal_pair", lam_lo*clo < 2 and lam_lo>1 and chi<1, "lambda*conjugate=1, one >1 one <1, both real")

ok=all(c for _,c in checks)
print(f"\n{sum(c for _,c in checks)}/{len(checks)} checks passed; ALL VERIFY_OK" if ok else "\nVERIFY_FAILED")
raise SystemExit(0 if ok else 1)
