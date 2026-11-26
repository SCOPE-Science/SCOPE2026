# Independent mathematical audit

## correctness

PASS

In the stated real full-line BV class, Df is a finite signed measure and f is a constant plus the L²(γ) integral of the unit jumps H_t against Df. Thus the projection error norm per unit variation equals the supremum over jumps. For a jump the coefficient in mode k≥1 is φ(t)He_{k−1}(t)/√(k!), by integrating the Gaussian-weighted Hermite primitive. Differentiating the resulting finite Pythagoras formula gives E′_n=−2φ²(G−Q_n), with G′−tG=1. In (d/dt−t)(He_{k−1}He_k/k!), the two terms remaining by the Hermite recurrence are He_{k−1}²/(k−1)!−He_k²/k!. Telescoping gives E″_n+tE′_n=−2φ²He_n²/n!, also for n=0, and E′_n(0)=0. The integrating factor and the nonzero polynomial square give E′_n(t)<0 for every t>0; reflection gives the unique maximum at 0. The variation measure of an extremizer must be supported at 0, since otherwise integrating the strictly lower jump norms against variation loses strictly. The center coefficients vanish in even positive degrees and in degree 2j+1 have square (2π)⁻¹ binom(2j,j)/(4^j(2j+1)); this gives C₀=1/2 and strictly decreasing successive odd–even plateaus. The arcsine tail and Stirling give C²_{2m}∼1/(2π^{3/2}√m), hence the displayed limit with n∼2m. Inspected the frozen finite checker without executing it. Replay: python3 -B /workspace/review_evidence/independent_checks.py 4; 45 numerical comparisons of the squared jump residual by quadrature in x, degrees 0–8 and thresholds 0, 0.25, 0.5, 1, 2, with strict ordering at these thresholds. This is diagnostic, not a proof of strictness or the asymptotic.

## originality

PASS

The supported distinct claim is the strict all-degree threshold maximum for the full finite-degree projection residual, and its exact positive-degree norms and extremizers. The degree-zero case and general jump-reduction method are not novelty grounds. No exact or stronger covering positive-degree claim was established in the inspected material.

## value

PASS

The exact worst error for all degrees and all real Gaussian BV input is a natural approximation benchmark. The question is not which coefficient is largest: simultaneously controlling a whole tail gives a universal and unique median jump despite off-center optima for some individual modes. The formula, parity plateaus and sharp rate make the extremizer theorem quantitatively useful without claiming a new parity or asymptotic tool.

The dated certificate retains the supplied scientific assessment, sources and limitations.
