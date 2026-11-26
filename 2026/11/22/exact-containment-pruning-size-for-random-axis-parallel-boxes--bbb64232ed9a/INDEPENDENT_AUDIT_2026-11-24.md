# Independent mathematical audit

## correctness

PASS

This pass is for the repaired result, not the original pointwise pruning statement. In the original definition, equality with another label excludes minimality. A realized input consisting of two identical labeled nonempty boxes can then lose both constraints, changing the optimum from 1 to 0. The replacement files state the original sampling rule's almost-sure equivalence, and give a correct deterministic rule for arbitrary finite inputs: deduplicate, then descend strict inclusion to a remaining minimal set. This change leaves the mean formulas unchanged. For a box with side lengths X_i, independent endpoints give a conditional domination mass Q=prod X_i². The conditional survival is (1-Q)^{n-1}, giving the binomial sum from the moments 2/[(2k+1)(2k+2)], including n=1. For S=-log prod X_i the convolution has density 2^d e^{-s} times a simplex integral with integrand prod(1-e^{-t_i}); subtracting from simplex volume is bounded by the sum of the integrals of e^{-t_i}, each O((1+s)^{d-2}). The change of variables u=sqrt(n) prod X_i yields an integrable Gaussian times a polynomial in |log u| after normalizing by sqrt(n)(log n)^{d-1}; the limiting integral is sqrt(pi)/(d-1)!. Independently, in dimension two integrate 4[(1+z)log(1/z)-2(1-z)] via I(a)=B((1+a)/2,n)/2 and its a-derivative. The exact result is n B(1/2,n)[psi(n+1/2)-psi(1/2)-4]+H_n+4. With psi(1/2)=-gamma-2log 2, the beta ratio and large-argument digamma give the specified planar coefficient and O(log n) error. Verified the repaired scope and proof against these calculations. The original check.py and reported tests are finite comparisons only and were not used as a proof of either asymptotic.

## originality

PASS

Best-of-knowledge pass on the repaired multidimensional exact mean, sharp fixed-d growth and planar correction. The shared d=1 identity is verified existing coverage and explicitly not a distinct contribution. Known piercing, packing and union observables do not imply this containment-frontier count. Deduplication and descending containment are standard, not novelty claims.

## value

PASS

The expected size after an exact redundancy-elimination step is a motivated finite-input invariant in the standard random piercing model. The corrected rule preserves the objective even with coincident constraints, and the random mean shrinks from linear to a dimension-dependent sublinear scale with a sharp constant and planar correction. This quantifies a natural preprocessing question without claiming an optimal hitting-set algorithm, a concentration bound or a runtime gain. The value does not depend on the known d=1 specialization or the elementary pruning rule considered alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
