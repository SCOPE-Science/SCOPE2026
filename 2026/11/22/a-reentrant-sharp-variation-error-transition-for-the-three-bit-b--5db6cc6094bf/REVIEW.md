# Independent mathematical audit

## correctness

PASS

Mod constants, the adjacent variation is the ℓ¹ norm of the three increments, and their coordinate vectors are the three thresholds. Applying I−P and the triangle inequality gives the maximum of the threshold column norms; equality cannot combine two columns since they are linearly independent in the mean-zero range for ρ<1. Independent orthogonal centered Bernoulli products give degree weights (1−ρ^m)². Expanding OR, majority and AND gives the three claimed masses; the first dominates the third below p=1/2, and at p=1/2 the middle exceeds both. For the middle-versus-first comparison the positive prefactor leaves B. With a=(2−3p)/(1−p), S=1+ρ+ρ² and T=1+ρ, S²−aT²≥−4 on the specified rectangle, hence ∂pB≥2−2p>0; the displayed second ρ derivative is strictly positive. The endpoint slopes place the unique minimum inside for p<1/2. The endpoint zeros give p_0<p_1; the minimum is continuous and strictly increasing in p, negative at p_1 and positive at 1/2, giving the unique tangency and all endpoint/root cases. Complementation swaps the extremes and preserves the quotient. For two bits the degree-two masses tie and the degree-one preference is independent of ρ. A separate exact product-cube enumeration (`python3 /workspace/checks/ehrenfest.py`, with mpmath only for the numerical roots) found the winning indices 2,1,2 at p=87/250 and ρ=0,1/5,1/2; the critical and example root decimals also agree. Only the inequalities and norm argument, not the finite enumeration or root solver, prove the continuum result. The frozen checker was inspected, not executed.

## originality

PASS

Qualified for the explicit sharp BV-to-equilibrium-L² residual, including equality and minimal reentrant phase diagram. The composition chain, product diagonalization and ℓ¹ column-norm reduction are standard ingredients. The inspected statements do not resolve the specific cross-degree competition or the two-crossing bias range.

## value

PASS

The adjacent variation describes a natural control on a count signal, and its stationary mean-square one-step error has a concrete sharp constant and equality problem. The exact phase boundaries exhibit a bias range in which changing retention alone changes the uniquely worst count discontinuity from majority to the rare-count jump and back. Two bits cannot do this; the minimality, critical tie and rational signs make this a usable benchmark, not an arbitrary finite sample. The result is limited to identical refresh coordinates and the specified input/output norms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
