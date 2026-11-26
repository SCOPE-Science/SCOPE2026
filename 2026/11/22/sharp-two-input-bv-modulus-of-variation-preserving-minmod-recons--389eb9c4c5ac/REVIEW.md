# Independent mathematical audit

## correctness

PASS

On the open interval the derivative measure consists of the cell slopes and atoms of sizes d_j−λ(s_j+s_{j+1})/2. For a single input, both slopes bordering d_j have its sign or vanish and are no larger in magnitude; 0≤λ≤1 preserves the sign of the jump. Summing the absolute jumps subtracts precisely the interior slope variation because both end slopes are zero. For a pair of inputs, along a segment minmod locally selects either zero or one adjacent increment, yielding nonnegative secant weights α,β with α+β≤1, also valid across ties by continuity and compactness of the coefficient simplex. Fix the secant coefficients and express the input difference in step columns plus a constant. A unit step can drive only the two adjacent cell slopes a,b in [0,1], with endpoint slopes zero. Its interior contribution is λ(a+b), its two exterior jumps sum in magnitude to λ(a+b)/2, and its central jump is nonnegative and equals 1−λ(a+b)/2. The column gain is 1+λ(a+b). Triangle inequality bounds it by 1, 1+λ or 1+2λ depending on available interior cells. For n=3 the witness increments (1,2) become (3/2,2), driving the only slope; for n≥4 the increments (2,1,2,3,…) become (2,3/2,2,3,…), driving two slopes by the same perturbation. The two-site constant and λ=0 follow directly from the piecewise constant difference.

## originality

PASS

Pass for the exact two-input dimension- and scale-dependent law for the discontinuous cellwise-affine reconstruction. The single-input TV property and minmod itself are not new. The strongest catalogue overlap concerns cubic Hermite interpolation; primary source access limits the comparison, but no available statement gives this pairwise norm for this reconstruction.

## value

PASS

The sharp norm determines how data perturbations can be amplified in distributional variation even when each reconstruction preserves variation exactly. The dimension cutoffs quantify the number of slopes responding to one edge, and the scaling law lets an analyst choose λ for a specified perturbation amplification limit. Exact jump accounting and positive-size witnesses are needed; individual TVD alone does not give this information.

The dated certificate retains the supplied scientific assessment, sources and limitations.
