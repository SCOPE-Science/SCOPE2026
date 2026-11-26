# Independent mathematical audit

## correctness

PASS

The stationary transport profile is (p/gamma)exp[-(mu_0+alpha N)ell/gamma]; its scalar closure makes p(N) a strictly increasing bijection on the positive half-line because t/(1-exp(-t)) is increasing, including continuity at zero. The adult fraction is F_beta(t)=exp(-beta t)(1-exp(-(1-beta)t))/(1-exp(-t)), so the adult-count logarithmic derivative has sign 1-(t-t_0)H_beta(t), with H_beta=-F'_beta/F_beta. Independently differentiating yields H'_beta>0 by strict decrease of s/sinh(s), H_beta(0+)=beta/2>0, and H_beta(infinity)=beta. Consequently the root is unique for every 0<beta<1 and t_0>=0; the log curvature is strictly negative there. At large p, p~alpha N^2 and log A_h=log N-beta t+o(1), giving log A_h/sqrt(p) -> -h sqrt(alpha)/gamma. At beta=1/2 and mu_0=0, writing z=t/2 gives (z-1)exp(z)=1 and A_h(p_*)=2 gamma W_0(exp(-1))/(alpha L). The proofs and boundary regimes were independently reconstructed; frozen CHECK.py was inspected, not executed, and its finite diagnostics are not needed for the theorem. This is about stationary, unharvested, count-dependent linear mortality with constant growth and external flux, not dynamical stability, yielding harvest or validating a field prescription.

## originality

PASS

The model, stationary exponential profile in this subfamily and scalar closure come from established size-structure theory. The supported extension is the strict, all-interior-cutoff classification for the mature equilibrium count as a function of the external input, with high-input decay and the midpoint calibration. The closest prior primary text and inspected catalogue records address different response or optimization variables, not this conclusion.

## value

PASS

Standing mature count is a meaningfully different objective from total census or yield. The model gives a sharp counterexample to monotone mature-stock response despite strictly increasing total count; it supplies an all-cutoff uniqueness criterion and a quantitative high-input decline. This is useful for interpreting and checking this model class, not presented as a universal biological claim or stocking advice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
