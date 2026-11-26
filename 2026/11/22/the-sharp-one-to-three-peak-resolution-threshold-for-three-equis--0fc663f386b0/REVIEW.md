# Independent mathematical audit

## correctness

PASS

For normalized time y and c=2 cosh(d), u=2 cosh(y), adding the two translates gives (cu+4)/(u+c)^2 and the central density adds 1/(u+2). An independent way to check the full derivative sign classification is to set w=(u+2)/(u+c), in [4/(c+2),1). After multiplying by (u+2)^2 the derivative with respect to u is Q(w)=w^2(c+4-2(c+2)w)-1. It is negative at both ends (at the left end this follows from H_c(2)=-(c+2)((c-6)^2+32)); the only possible interior maximum is w=(c+4)/(3(c+2)), which is in the interval precisely when c>8. Its height has the sign of (c+4)^3-27(c+2)^2=(c+1)(c^2-16c-44). Thus above c=8+6 sqrt(3) exactly two simple stationary radii occur, with derivative signs minus, plus, minus; at equality the double zero does not change sign. The center stays a strict maximum because the derivative in u is strictly negative at u=2. The monotone half-line changes of variables give the exact t-mode counts and d threshold. The analogous two-density sum omits 1/(u+2); at symmetric half-separation d/2 its derivative changes regime at 2 cosh(d/2)=4, verifying the stated pairwise contrast. The frozen SymPy checker was inspected, not executed; its finite examples are supplementary, not an all-parameter argument.

## originality

PASS

Best-of-knowledge pass for the equal-weight, equal-scale, equispaced logistic triple and its exact stationary bifurcation only. The closest verified logistic result is pairwise. The closest catalogued direct triple transitions use different kernels and do not imply the logistic derivative classification.

## value

PASS

Equal-rate, equally spaced cohorts give a natural calibration problem. The exact onset of outer peaks and the nonextremal shoulders identify a resolution boundary not captured by the nearest-neighbor pair test. In particular there is a nonempty interval where each adjacent pair resolves but the aggregate does not. This is a useful idealized benchmark, not an empirical detection claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
