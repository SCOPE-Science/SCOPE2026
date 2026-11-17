# Scientific review of the quadratic B-spline variation theorem

## Correctness
**PASS.** The centered spline moments give the sole quadratic-reproducing parameter \(a=1/8\). The exact step derivative has five knot values \(0,-a,1+2a,-a,0\), so the two outer and two inner negative triangles sum to \(a+a^2/(1+3a)\). This proves the displayed norm with no reliance on numerical interpolation. Absolute jump decomposition and an \(L^1\) triangle inequality prove the bound for every two-sided finite-variation sequence; a step attains it. Exact-rational checker results are corroboration, not a replacement for the infinite proof.

## Originality
**PASS on the inspected evidence, with historical-priority qualifications.** Sablonnière's complete accessible April 2005 manuscript displays exactly the interior correction \(\mu_j=(-f_{j-1}+10f_j-f_{j+1})/8\) and a finite-interval maximum norm, but not the bi-infinite discrete-to-continuous variation norm. His December 2005 paper concerns the same classical construction and quadrature. Dũng's accessible 2010 manuscript gives general B-spline quasi-interpolant representations and Besov recovery estimates; the inspected operator definitions and theorems do not give this exact norm. The classical variation-diminishing result concerns the positive-sampling baseline, which is not the signed quadratic-reproducing operator. Nearby published records involving spline orthoprojections and cubic-spline interpolation concern different operators. An earlier 2003 precursor and the full 1986 variation-diminishing paper were not available for complete text-level priority resolution; their existence remains a residual risk.

## Mathematical value
**PASS.** This is an exact edge-stability benchmark for a classical low-cost, polynomial-reproducing reconstruction rule, not an arbitrary coefficient or an exercise in rescaling. It quantifies the cost of correcting the positive B-spline sampler to reproduce curvature: the unique quadratic-exact correction raises the worst-case variation from \(1\) to \(14/11\), and the whole parameter family has an explicit strict monotonic stability frontier. It specifies a concrete worst-case step input and rules out nonexpansiveness for any positive correction in this natural class. No broader optimality among all spline algorithms is asserted.

## Limitations and closest prior results
The theorem concerns a bi-infinite uniform grid, not finite-interval boundary rules. General nonuniform and higher-order problems are not settled. Full-text inspection of the 2003 precursor and Marsden's 1986 article was unavailable; an exact prior characterization cannot be categorically excluded. Sablonnière (2005), Dũng (2010) and the classical positive spline literature remain the closest sources discussed in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
