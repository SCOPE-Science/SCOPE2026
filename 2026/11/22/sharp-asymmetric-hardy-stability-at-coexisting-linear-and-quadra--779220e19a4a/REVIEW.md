# Independent mathematical audit

## correctness

PASS

The original's assertion that every asymptotically extremal sequence converges to one fixed monomial up to phases is false: alternate the supplied inner f_t with t=1/j and t=1-1/j (j>=3). Both deficits tend to zero through positive values, whereas |f_t'(0)| tends to 0 and 1 on alternating terms, regardless of phase. Original Step 5 also needed an accumulation-point rather than a full-sequence dichotomy. The repaired result asserts distance to the union and branchwise subsequential convergence. Its quantitative core passes: f=zg gives y=|g'(0)|<=1-x, and the 2x2 squared singular values have sum 4x+3y² and product 3x². The nonnegative matrix norm grows in y. At y=1-x, det(3I-H)=6x(1-x) with positive first minor on 0<x<1, so dividing by the other eigenvalue 3-lambda_-≤3 gives the sharp stated lower bound; endpoint equality gives just the two monomial classes. As deficits tend to zero, x clusters at {0,1}; the trace bound forces y→1 on the x→0 branch, and coefficient order separates the nearer classes. In the quadratic branch s=1-y≥x and the smaller eigenvalue is O(x²); thus delta=6s-4x+O(s²) and d_2²≤2s. In the linear branch h=1-x bounds y, the diagonal gap of the squared matrix stays nonzero and the off-diagonal term is O(y); hence delta=3h+O(h²) and d_1²≤h+O(h²). Exact inner-family distances and the two parameter limits attain both constants and the mixing coefficient. The repair also corrects the v1 equality-section pointer.

## originality

PASS

The surviving claim is the sharp anchored mixing deficit and both sharp symbol-distance coefficients at the critical unequal weights, not the background spectral-set constant, equality case existence, or a new universal Crouzeix estimate. No inspected theorem gives these quantitative two-branch conclusions by specialization. Restricting the convergence statement to distance from the union does not change the novelty object.

## value

PASS

The unequal critical weights are the natural coexistence point where the two power norms agree. The exact coexistence penalty and different local rates quantify what a nearly extremal function must look like in the full Hardy norm. This is more than repeating norm attainment or qualitative convergence and remains useful with the corrected union-of-classes statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
