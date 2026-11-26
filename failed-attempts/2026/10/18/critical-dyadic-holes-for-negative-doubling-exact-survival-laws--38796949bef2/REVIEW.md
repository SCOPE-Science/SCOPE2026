# Independent mathematical audit

## correctness

PASS

The negative branches are affine with slope -2, so length-L codes correspond to equiprobable dyadic cells of width 2^(-L) off endpoints. The inward one-sided codes at the center begin 00 followed by alternating bits, or the complement, agreeing with the proposed two forbidden words. The equality-defect transformation bijects each binary word with its initial bit and a defect word. The forbidden patterns become precisely 1 followed by r=m-2 zeros. Counting by the last 1 gives b_N=1+sum_{j=1}^r b_(N-j) (b_0=1 and b_k=0 for k<0), giving the stated generating function via a_L=2b_(L-1). Appending all ones in defect coordinates extends each allowed word when r>=1, and r=0 uses all zeros. The recurrent renewal component has gaps 1 through r, so for r>=2 its Perron parameter solves sum_{j=1}^r lambda^(-j)=1; r=0 and 1 have constant and linear word counts. The count gives the dimension upper bound, and the renewal measure with cylinder bound C lambda^(-L) gives the lower bound since intervals of size 2^(-L) meet a bounded number of level-L cells. Entropy also follows from the coding, or directly from exponential growth of dyadic-cell coverings and uniformly expanding Bowen balls. At dyadic boundaries every nonzero dyadic rational eventually visits the hole center, so only the zero circle point can survive among these exceptional points; the two alternating endpoint codes there do not alter entropy or dimension. Formula (4) tests exactly n windows in n+m-1 bits, so the finite-time and escape rate follow including both degenerate cases. Write r=m-2 and t=1-lambda/2. The small root of t(1-t)^r=q lies in [q,2q] for large m, since rq tends to zero and the function is increasing on that interval. Uniform Taylor expansion gives t=q+rq^2+O(r^2q^3), then -log(1-t)=q+(r+1/2)q^2+O(r^2q^3). This confirms the sign, logarithm base and remainder. The other algebraic root t=1/2 is not the positive-entropy branch.

## originality

FAIL

The exact all-depth law is a direct specialization of the existing correlation-matrix theorem, not merely a problem for which rationality was previously known. Reflection reduces survival to ordinary doubling exactly, and its two forbidden words have correlation matrix with diagonal z^(m-1) and off-diagonal 1. Substituting that matrix in the verified general count formula gives the entire claimed numerator and denominator, not just the asymptotic rate. Its largest pole, the equal cylinder lengths and a Taylor expansion of the pole equation yield all the quantitative claims, including the second-order coefficient and remainder. The failure is established by the published general theorem and this direct substitution, not by search misses, inaccessible texts or inferred order of indexed records.

## value

FAIL

The symmetric dyadic family is natural and the formulas are useful benchmarks. As a separate contribution, however, the finite counts and boundary depths are determined by a two-entry overlap calculation in the existing exact method, and the quoted refinement is the second-order Taylor coefficient of the same known pole equation, with a routine uniform remainder on t=O(q). The alternate defect coding does not yield a distinct scientific claim beyond those mechanically determined outputs in the frozen finding. There is no supported new valuable remainder to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
