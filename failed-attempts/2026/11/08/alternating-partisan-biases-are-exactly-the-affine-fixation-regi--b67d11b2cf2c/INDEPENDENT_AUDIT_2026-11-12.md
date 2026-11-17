# Independent mathematical audit

## correctness

PASS

The actual generator on an undirected finite simple connected graph yields Lf(s)=1/2 sum_{ij in E}[(a_i/d_i-a_j/d_j)(s_j-s_i)+(a_i h_i/d_i+a_j h_j/d_j)(1-s_i s_j)]. For any affine harmonic fixation f=c+sum a_i s_i, independent Walsh coefficients force edge (a_i h_i/d_i+a_j h_j/d_j)=0 and the degree-normalized a_i/d_i to be graph-harmonic and hence constant. Boundary consensus values give c=1/2 and a_i=deg(i)/(4|E|), forcing h_i+h_j=0. Conversely cancellation makes this affine f harmonic with correct absorbing boundary values; every nonconsensus finite configuration has a positive-probability path to absorption for |h_i|<1. Thus claimed iff, degree-weighted formula and bipartite/odd-cycle corollaries follow. Companion verify.py was read but does not replace the proof.

## originality

FAIL

Exact overlapping prior Resultary publication November 2 applies the same partisan copying rule with arbitrary real h_i∈(-1,1) on an even BROADER class of connected undirected positively weighted graphs and proves degree-weighted fixation is unbiased iff all edge endpoint preferences cancel. Another prior November 8 result proves uniqueness of ALL linear opinion martingales on this microscopic model (for binary signed preferences); that universal linear-martingale uniqueness is extended to arbitrary real h_i by the routine vertex-harmonic/Walsh coefficient argument already present in the assigned proof. Under equivalence and implication comparison, the substantial final fixation classification and exact probability are already known. The only separate general-real preference affine-uniqueness phrasing is a direct low-complexity deduction from prior generator method, not an independent new theorem.

## value

FAIL

While useful as a clear restatement of affine uniqueness, the main neutrality locus, exact degree-weighted fixation law, and bipartite consequence are contained in a stronger weighted-network publication; the remaining step is elementary uniqueness of the stationary degree vector using graph harmonicity. This lacks an independently motivated unknown invariant or boundary beyond the covered theorem. Correctness and nice exposition do not prove distinct research value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
