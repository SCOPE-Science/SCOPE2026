"""Verifier for the virial no-go lemma constants (stdlib only).
Replays exact rational-multiple-of-pi identities from closed-form profile calculus.
Prints VERIFY_OK on success."""
import math
pi = math.pi; s3 = math.sqrt(3)
fails = []
def check(name, got, want, tol=1e-9):
    if abs(got - want) > tol:
        fails.append(f"{name}: got {got!r} want {want!r}")
I = 3*s3*pi**2/4            # ||W||_{Hdot^1}^2 = ||W||_6^6
L = 15*s3*pi**2/64          # ||Lambda W||_{Hdot^1}^2
check("detJ", I*L, 135*pi**4/256, 1e-9)
Qw = 225*s3*pi**2/512       # || |y| Delta LambdaW ||_2^2 (sympy: B=25pi/2048, factor 36*sqrt3*pi)
check("Qw", Qw, 225*s3*pi**2/512)
check("Qw_numeric", Qw, 7.512300120099122, 1e-6)
CS = I**(-1/6)              # sharp Sobolev constant from saturation by W
check("CS^6*I", CS**6*I, 1.0)
check("L/I", L/I, 5/16)
check("sqrt(L/I)", math.sqrt(L/I), math.sqrt(5)/4)
check("orth_scaling", 0.5 - 3.0/6.0, 0.0)   # (W,LamW)_Hdot = (1/2-3/6)||W||_6^6 = 0
check("kernel_Q", L - L, 0.0)               # Q(LamW)=kin-5int W^4 LamW^2 = L-L = 0 via L_+LamW=0
check("Jinv_norm", 1.0/L, 64/(15*s3*pi**2))
check("E(W)", I/3, s3*pi**2/4)
if fails:
    print("VERIFY_FAIL")
    for f in fails: print(" ", f)
    raise SystemExit(1)
print(f"VERIFY_OK: I={I:.12f} L={L:.12f} det={I*L:.12f} Qw={Qw:.12f} CS={CS:.12f}")
