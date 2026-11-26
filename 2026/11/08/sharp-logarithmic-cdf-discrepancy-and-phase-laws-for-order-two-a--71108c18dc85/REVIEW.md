# Independent mathematical audit

## correctness

PASS

Cloitre–Joshi Proposition 3.1 matches the exact greedy dyadic formula. On B=2^k, writing n=B+j, division yields h(1+j/B) plus exactly 1/[2(B+j)] for odd j on the first branch, and zero otherwise. The sublevel of h is the interval between inverse endpoints u(y) and v(y) on its range; its intersection with [1,θ] gives the stated additional mass and continuous CDF. The unnormalized numerator has mass θ. Each monotone branch contributes grid-count error at most one, and its inverse is 9-Lipschitz, so the strip of width 1/(2B) contains at most six grid points per branch. Thus each complete or truncated block contributes at most 14 count error. Complete block lengths total 2^K−4; the last block includes N and differs from the phase integral by one endpoint cell. Accounting for the initial three indices bounds the discrepancy by [14(K−1)+8]/N, certainly at most 30(K+1)/N. For j≤B/2, 4a(B+j)−3(B+j) is −j for even j and 2−j for odd j; for j>B/2 it is j−B. Only j=0 and 1 qualify in each block, plus n=1,2. The floor-log count is therefore exact, including cutoffs that are powers of two. The phase law has no atom at 3/4, so the left-hand CDF limit there supplies the lower bound without dropping the equality cases. Continuity in θ, compactness of [1,2], and integer cutoffs approaching each phase give all weak limits; for y=7/10 the first partial interval contributes zero on θ∈[1,5/4], so F_θ(y)=(5/12)/θ varies strictly there.

## originality

PASS

The arithmetic formula and pointwise oscillation are already known; the same paper also proves nonconvergence of the Cesàro mean and gives two explicit subsequential mean values, a stronger overlap than the frozen relationship section mentions. Neither those scalar means nor the inspected sequence entry and alternative Beatty solutions give the full weak-limit family or the uniform sharp-order phase-matched CDF estimate. The exact endpoint count is an elementary consequence of the existing formula and is credited principally as the mechanism forcing the new discrepancy lower bound, not as a new sequence formula.

## value

PASS

The result describes the fluctuation when pointwise and mean convergence fail: cutoff phase selects the whole probability law, and the exceptional ratios precisely force a logarithmic penalty missed by a single-block approximation. The matching uniform rate and complete limit family are useful beyond rechecking the published dyadic formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
