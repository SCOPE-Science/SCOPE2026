import math
# Recovery test: even with extreme assumptions can 0.70 close?
# Model A: shrink bad-block length bound. FS Green-optimal L_max formula:
def Lmax_green(sig,D):
    a=min(1+sig,D)
    num=sig*(sig+1-a)
    den=a+sig+sig**2-sig*a
    return num/den if den>1e-12 else 0.0
sig=0.9; D=2.0
L=Lmax_green(sig,D)
print("Lmax/r (pure-red upper bound):",L)
# best value if bad-block per-unit rate could be pushed from sigma'=0.9 to 1.0 (full recovery, impossible since dy<=1)
for rate in [0.9,1.0]:
    v=min(rate*1.0, 0.18+0.8*0.568896)
    print(rate,v)
# Model B: decoupling inequality K(w)>=K_s(x)+sig(r-s) already saturated; show factor needed
# To reach 0.70 via larger t-cap T: value formula with general T: min_L max? upper envelope = sig'*(1 - G/((sig'+1)*G-(sig')^2*(...))) -- increases as T drops.
# Compute value if T could be 0 (i.e., direction complex at all scales, maximal OSW gain): alpha unchanged, but t-constraint removed -> bound unchanged? Actually t only enters projection theorem, not final energy step. So no gain.
# Confirm: final energy step has no t. The 0.651 is intrinsic to admissible-partition ledger given (sig,D).
print("conclusion: within FS ledger, 0.70 unreachable without changing (sigma,D) inputs or c; D<=1.585 needed, contradicts D=2 general class.")
