# Independent mathematical audit

## correctness

PASS

In one independently stopped cycle S=min(R,τ₀), let Λ be the cycle local time and J the terminal mark. The stopped point local-time potential is EₐΛ=G: the local-time occupation potential is the killed r-resolvent density with respect to dy (equivalently the continuous one-dimensional Green kernel with its speed-density factor). The stated normalization is physical occupation time per unit length, not semimartingale local time. A direct check of the marked step uses the strict inverse local time T_u. On T_u<S, X(T_u)=a and the remaining exponential clock is fresh. Thus the remaining marked transform conditional on the past is F_j=Eₐ[e^(−sΛ);J=j]. Integrating this identity over u≥0, using 1−e^(−sΛ)=∫₀^Λ s exp(−s(Λ−u))du, gives p_j−F_j=s EₐΛ F_j=sG F_j. This justifies the same marked formula as the ordered-time Kac argument without needing a pointwise-limit interchange at every moment order. Segment independence and 0<h<1 give a geometric number of failures, no infinite concatenation, and a Gamma shape n+1 sum given N=n. Summing yields the joint transform and normalized density, and division by the exponential marginal gives the Poisson law for almost every ℓ>0 (with the displayed continuous conditional version). Cov(N,L)=(1−h)G/h² and the two variances give √(1−h). The killed Brownian image Green agrees with the stated convention. For the OU example, independent replay via python /workspace/reproductions/frozen_checks.py (fourth check, mpmath) obtains G=0.504146804919318329 from reduction of order and a derivative jump of −1/D, rather than time-image quadrature, and verifies the four rounded values. The frozen finite-state diagnostic was inspected, not run; some counted assertions are identities, and finite-grid agreement alone does not prove the continuum statement. Scope remains same starting/reset/local-time point, independent exponential resets and the indicated regular killed diffusion with finite diagonal potential.

## originality

PASS

The Brownian joint law is already a mathematical consequence of an earlier joint exposure transform, and the Brownian and OU local-time marginals are prior work. The supported distinct contribution is the general regular-diffusion count/local-time law, with parameters h and G and the terminal-mark independence mechanism. No novelty of Poisson marking, the geometric count or the Kac identity itself is credited.

## value

PASS

The contribution in the stated regular-diffusion class gives an exact conditional calibration of reset effort from a natural physical exposure, not just one more marginal or re-evaluation of Brownian constants. One-cycle killing probability and one diagonal Green density suffice for the entire coupling, including for a nonzero drift for which the first-passage path functionals need not be available jointly. The correlation and count-conditioned Gamma law give independently useful quantitative consequences within the specified scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
