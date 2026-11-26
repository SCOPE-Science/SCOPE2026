# Independent mathematical audit

## correctness

PASS

Center the vertex values to have zero discrete sum. Regularity makes their affine lifts have zero arclength mean; the remaining mean subtraction is the average of the edge Dirichlet integrals. The energy splitting is orthogonal, since each residual vanishes at both endpoints. The affine evaluation contributes tr(L+)/N minus R_uv t(1-t), by constant pseudoinverse diagonal. For the residuals the Dirichlet kernel min(s,t)-st gives t(1-t), its first integral t(1-t)/2, and its double integral 1/12, hence the correction (1-1/m)t(1-t)+1/(12m). Foster's trace identity makes the average curvature coefficient 1-2/d, so its positive maximum for d>=3 is attained exactly at minimum-resistance edges, with t=1/2. Cauchy-Schwarz yields exactly their nonzero scalar Green representers. The cycle coefficient vanishes and the mean-zero interval diagonal is t²-t+1/3; dilating lengths by ell divides energy by ell. For cubes, the eigenvalues 2k and the Foster edge value give (3); A_4=103/384>1/4 and A_(n+1)=A_n/2+(1-2^(-n-1))/(2(n+1)) inductively give A_n>1/n, forcing all claimed strict differences. The binomial reciprocal expansion to third order on X>=n/4 uses zero odd central moments up to exponentially small tails and fourth moment O(n²), giving the stated O(n^-3) remainder. Independently solved the exact mean-constrained variational equations in vertex hats and quadratic segment bubbles, recovering 181/546 and 89/273 on the two C7 edge types (difference 1/182) and the four cube values 1/3, 1/3, 113/288 and 19/48. Replay: python3 /workspace/review-evidence/replay.py 2. Frozen 565 comparisons are recorded evidence, not this review's run.

## originality

PASS

Credit the electrical and generic Green/resistance approach as overlapping prior material, not as original. The distinct evaluated contribution is the explicit extremal comparison across all cube dimensions, including the strict descending tail and exact dimension-four peak; computing Kirchhoff indices or evaluating a general quadratic envelope graph by graph does not make that comparison. The specific minimum-edge-resistance criterion is an explicit equilateral symmetry reduction, not a new general method for computing the evaluation norm. Neither priority over the distinct same-day general envelope nor originality of a quadratic-profile framework is established here.

## value

PASS

The non-edge-transitive witness distinguishes genuinely different norming and non-norming midpoints even though all vertices look identical. The exact all-dimension cube comparison answers a natural extremal question for a canonical graph family: the peak is finite and occurs at dimension four, not at high connectivity or in the large-dimension limit. This contribution goes beyond re-evaluating a known resistance sum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
