# Independent mathematical audit

## correctness

PASS

Positive harmonic drifts and contracting jumps make the infinite-past convolution well-defined; synchronous coupling is exponentially contracting, so its stationary law is unique. The Brownian coordinates are conditionally independent centered Gaussians even across distinct times when conditioned on the relevant entire clock history; hence positional cross-covariance vanishes. The variance bound D_h/a_h controls all needed moments. As a separate check on the moment-generator calculation, the two backward clock horizons x,y overlap over min(x,y). Multiplying their q-squared factors and averaging the Poisson counts gives the mixed conditional-variance integral 4D_iD_j times the integral of exp[-L_i x-L_j y+delta*u*min(x,y)]. Splitting at x=y gives E[X_i^2 X_j^2]=4D_iD_j(1/L_i+1/L_j)/B. Subtracting m_i*m_j gives the stated strictly positive C0. The conditional second moment over a future lag has initial-value factor exp(-L_j t), and additive noise contributes its remaining stationary mean term independently of the initial state; this gives the stated ordered covariance. The ratio cancels delta; for L_i!=L_j the difference of exponentials vanishes at both ends and its derivative vanishes at exactly the stated positive lag. One exact observation at known t>0 gives L_j=-log(C_forward(t)/C0)/t. Now delta>0, and the identity H=delta*u/(L_i+L_j-delta*u) gives a unique u in (0,1] and hence q and r. The q=0 case is valid with q^0=1 for zero clock events. Equal traps erase this lag-direction witness but leave the inversion intact. Independent exact rational replay checks the clock-overlap result and inverse including complete reset, finite partial reset and equal drift.

## originality

PASS

The supported distinction is the exact finite-jump, unequal-trap two-time squared-position law, its asymmetric peak and the joint recovery of rate and contraction from the stated moment/lag data. Common-clock positional decorrelation with correlated energies, the homogeneous partial-jump slice, and the heterogeneous complete-reset equal-time amplitude all have substantive prior/parallel coverage. They are not credited as new here. No inspected statement supplied the joint finite-partial and unequal-strength two-lag result or the specified inversion.

## value

PASS

The result pinpoints why zero positional cross-covariance is uninformative about a shared clock and when a pair-level fourth-order statistic detects a time arrow. Unlike the homogeneous case, simply exchanging the later-trap label produces a nonzero effect with a calculable optimum lag. The same low-order stationary and lag quantities separate reset frequency from contraction strength without needing the diffusivities. This is an exact diagnostic and identification result, not merely a covariance evaluated at particular parameter values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
