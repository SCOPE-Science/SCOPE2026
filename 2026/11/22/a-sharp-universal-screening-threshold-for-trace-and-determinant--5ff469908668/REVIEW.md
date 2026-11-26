# Independent mathematical audit

## correctness

PASS

For U the unselected sites, block inversion gives Nyström residual 0 on the selected rows and columns and (A_UU)^−1 on U; Jacobi gives det K_SS=det A_UU/det A. Removing landmarks splits the precision into interior continuants F_j (all diagonals μ+2) and free-end tail continuants H_j=F_j−F_(j−1) for j≥1 (one diagonal μ+1); empty blocks contribute determinant one and trace zero. The sinh and cosh solutions follow from their initial conditions and recurrences. For t=exp(θ), each tail determinant ratio is <t, while each interior increment ratio is >t. With k≥2 an outward move transfers one tail site to the adjacent interior gap, strictly improving determinant. For trace the interior increments are strictly below c=1/sqrt(μ(μ+4)), tend to c, and are strictly increasing because x coth(θx) has positive second derivative. At μ≥1/2, t≥2 and each tail increment is ≥c: its excess has the sign of t^(2a−1)[(a−1/2)(t²−1)−1]−1, nonnegative for all integer a≥1 with equality only at a=1,t=2. Strict interior inequality ensures an outward move strictly lowers trace even at the threshold. Once tails vanish, strict discrete convexity of trace and strict log-concavity of determinant give exactly the balanced gap profiles and their binomial multiplicity. Below threshold, g(1)=1/(μ+1)<c. The k=2 endpoint pair loses in trace to {2,n} for every sufficiently large n, since the interior marginal tends to c. This is sharpness of uniform agreement, not a claim of disagreement for every individual n and k. For n=6, μ=1/4 I independently compared all 15 pairs by exact cofactors: form B=4A_UU with diagonal 5 at free ends, 9 elsewhere and off-diagonal −4 on unselected neighbouring sites, and compute 4Σ_i det B_(−i,−i)/det B. The unique minimum is {2,5} at 176/65; the next value is 5984/2205, while {1,6} gives 8208/2929. This verifies the strict witness and its asserted uniqueness. Supplied scripts were inspected, not executed.

## originality

PASS

The same 1/2 boundary marginal, the gap-balancing calculus, and stationary models showing determinant–trace disagreement all have explicit indexed overlaps. Credit those, rather than calling the number or the smoothing argument new. The supported distinct contribution is the free-end finite path theorem for both objective optimizer sets over all budgets at least two, with all-screening determinant classification and an exact uniform trace agreement transition. That requires the finite-path tail-to-interior comparisons; the same-day records establish overlap, not order of priority.

## value

PASS

This supplies a complete finite design rule for when trace and determinant select the same landmarks, including all ties, no subset search, and an exact threshold valid across path lengths and budgets. The below-threshold witness construction shows why the regime cannot be relaxed uniformly. The boundary mechanism distinguishes the problem from both cycle balancing and rank-one path optimization, and can matter when these two selection criteria are used interchangeably.

The dated certificate retains the supplied scientific assessment, sources and limitations.
