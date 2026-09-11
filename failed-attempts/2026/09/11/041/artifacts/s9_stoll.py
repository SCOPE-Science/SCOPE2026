# Stoll/Coleman ceiling check at p=13 under rank-1 hypothesis + toolchain probe.
# #C(F13) = 18 (16 affine + 2 rational infinities), g=2, r=1.
# Stoll: #C(Q) <= #C(Fp) + 2r = 20. Target needs 4. Gap = 16 unkilled classes.
def f_int(x): return x**6 - 3*x**5 + x**4 + 3*x**2 - x + 1
p=13
sq=set((t*t)%p for t in range(p))
aff=sum(sum(1 for t in range(p) if (t*t)%p==f_int(x)%p) for x in range(p))
C=aff+2; g=2; r=1
print(f"affine={aff} proj={C} stoll_ceiling={C+2*r} target=4 gap={(C+2*r)-4}")
import shutil
tools={t:shutil.which(t) for t in ["sage","magma","gp","pari"]}
print("tools:",tools)
try:
    import sageall; print("coleman_backend=sageall")
except ImportError:
    print("coleman_backend=NONE (no Sage/PARI/Magma/mwrank; sympy has no Coleman integration)")
print("PARTIAL_TARGET_BLOCKED: annihilating differential + infinity-disk expansions + sieve images uncomputable")
