# Independent mathematical audit

## correctness

PASS

The final-size equation follows by integrating incidence and using total infectious person-time. The survival-odds equation follows by averaging the conditional Poisson offspring generating function over the exponential infectious lifetime; B and K are similar by diagonal population scaling, and the transpose in the backward equation is essential. For positive fixed data, rescaling entry (i,j) of K by (p_i h_i)z_j gives a positive matrix with prescribed row and column margins. This proves the compatibility, dimension and rank-one assertions directly (see originality). Nonzero margin-preserving directions exist already for n=2 and small perturbations of a strictly positive point stay positive. The fitted positive fixed points are not extraneous: Kz=-log(1-z)>z implies supercriticality, and both maps are increasing and strictly subhomogeneous on positive rays. The maximum coordinate-ratio comparison excludes two distinct positive fixed points; branching iteration from survival vector 1 selects the maximal fixed point. The positive rank-one eigenvalue in the finding is its trace and is >1 by the same comparison. This is an all-size argument for the stated idealized model, not for empirical finite-sample data or for non-exponential recovery. RESULT.md lines 21–50 and VERIFICATION.md lines 19–23 were checked. verify.py lines 9–82 were inspected, not run: it is a finite Decimal example and basis-generator check, not independent proof or certification.

## originality

FAIL

The exact epidemiological wording was not found in a distinct inspected source. The scientific content of the inverse classification, however, is covered as a direct corollary of the classical prescribed-margins problem once the known forward relations are written for the stated arbitrary effective kernel. The reduction is invertible diagonal scaling, which also preserves rank; it needs no new inverse theorem. This is a finding of implication rather than an assertion that a prior paper prints the same epidemic formula.

## value

FAIL

Joint observability of burden and seeding risk is a meaningful question, and distinguishing conditional rank-one identification from testing the mixing assumption is useful. But for the expressly unrestricted positive-kernel class and noiseless observations, the answer is exactly an invertible reexpression of prescribed margins and their independence table. No new obstruction for constrained contact classes, inference with error, or other substantive result survives that reduction; none of those harder variants is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
