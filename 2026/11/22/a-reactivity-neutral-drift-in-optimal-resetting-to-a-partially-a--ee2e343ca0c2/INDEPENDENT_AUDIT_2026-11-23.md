# Independent mathematical audit

## correctness

PASS

The finite sink has killed-process absorption transform k exp[-(mu L+Gamma L)/(2D)]/(Gamma+k), Gamma=sqrt(mu^2+4Dr), at Laplace parameter r: the free resolvent from L to the sink is exp[-(mu L+Gamma L)/(2D)]/Gamma, and the rank-one sink divides it by 1+k/Gamma. Reset renewal gives (1-transform)/(r transform), exactly (1). For B=Phi-1-s Phi', B'=-s Phi'', and after removal of the positive factor of Phi'', the remaining polynomial is strictly increasing in u. B is positive at the small-rate end (at m=0 its first term is (1+eta)sqrt(s)/2) and negative for large s, so its sole crossing is transverse and is the global minimum. Independently, the coefficient G of eta after removal of exp(u+a) vanishes exactly at the unique u0>=1 with h(u0)=m, h(u)=u sqrt((u-1)/(u+1)), and G is positive before u0 and negative after. At that test point B=e^(u0+a)/(1+u0)-1 independently of eta. The sign of B there determines on which side of u0 the optimizer lies and hence the sign of its derivative with respect to k. For outward or zero drift B there is positive. For inward drift its sign is that of F(u0), which decreases strictly from 1-log(2) to minus infinity: h'(u)>u/(u+1) for u>1. This proves the stated threshold and both strict directions for every finite positive k. The intermediate condition u>1 in (5) can be u=1 for m=0 before imposing stationarity; this endpoint is impossible at stationarity since e/2-1>0. RESULT.md, VERIFICATION.md and verify.py were inspected; the supplied finite checks were not executed or used as proof.

## originality

PASS

The same finite point-sink model, renewal formula, all-drift uniqueness, zero-drift reactivity direction and several drift comparisons are prior. The sharp fixed-drift, all-k sensitivity reversal and the optimizer common to every finite reactivity were not covered by the decisive passages inspected; this is a best-of-knowledge finding, not certification of priority.

## value

PASS

The result identifies a sharp control threshold in the finite-reactivity resetting problem: tuning trap strength strictly moves the optimal reset rate in opposite directions across one drift, and exactly preserves the same optimum at that drift for arbitrarily weak or strong finite sinks. This is an actionable and structural distinction from perfect-trap zero-reset transitions and from optimizing the mean time itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
