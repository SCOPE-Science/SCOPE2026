# Review of the signed spherical Poisson kernel positivity theorem

## Correctness
**PASS.** The claimed kernel is unambiguously normalized on \(\mathbb S^2\). Expansion into \((2n+1)r^nP_n\) yields the explicit multipliers \(r^n(1+bR_n)\); the closed rational identity for \(R_{n+1}-R_n\) is positive for every nonnegative integer degree, and the limit is strictly unattained. Schoenberg's theorem therefore gives an exact all-configuration positivity criterion. A direct point-mass density argument proves strictness even on the critical boundary, and an exact gap expansion establishes the stated inverse-degree eigenvalue law. Executable symbolic and high-precision checks corroborate the critical algebra without being misused as an infinite proof.

## Originality
**PASS, bounded-literature assessment.** The inspected Jäger (2020), Buhmann–Jäger (2022) and Sun–Gao–Sun (2024) papers establish general spherical harmonic criteria and the ordinary Poisson expansion, but not this sharp signed \(P_2\) modulation threshold. Three closely related published kernel classifications were compared at statement and proof level: their kernels are, respectively, a geodesic exponential with a linear angular factor, a difference of geodesic exponentials, and a nonstationary Poisson modulation on the circle. None yields the explicit cone here by specialization. An unindexed equivalent or a treatment in a broader signed-polynomial spectral theory remains possible.

## Mathematical value
**PASS.** Signed angular modulation of a basic isotropic covariance model poses a natural exact admissibility problem. The sharp negative budget is not controlled by any finite harmonic degree: all finite modes remain strictly positive at the boundary, yet arbitrarily high degrees obstruct any more negative multiplier. This gives a genuine ultraviolet positivity phenomenon with a quantifiable spectral damping correction and explains why checking finitely many covariance harmonics cannot certify the sharp threshold.

## Limits
The classification covers only the degree-two Legendre factor, the standard ball Poisson family, and the unit two-sphere. It does not establish historical priority independently or extend to other dimensions.

Self-review: passed. Independent audit: not yet performed.
