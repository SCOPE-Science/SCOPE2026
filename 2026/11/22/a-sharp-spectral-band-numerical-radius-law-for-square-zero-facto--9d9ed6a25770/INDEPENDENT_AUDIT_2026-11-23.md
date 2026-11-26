# Independent mathematical audit

## correctness

PASS

For rank-one u⊗v with orthogonal unit vectors the radius is 1/2, and w((Au)⊗v)=(||Au||+|⟨Au,v⟩|)/2 by the standard rank-one numerical radius formula (compress to the span of the two vectors). Optimizing v gives the norm of the perpendicular component. For any square-zero B, the block form relative to ker B and its orthogonal complement gives w(B)=||B||/2, also when the block norm is approached only by a sequence. For each x with Bx≠0 replace B by ||B|| times the rank-one operator from the normalized ker(B)⊥ component of x to Bx/||Bx||. The factors are orthogonal, the radius is preserved, and the new value on x dominates the old in absolute value after multiplication by A. With ||A||=1, functional calculus gives q=⟨A²u,u⟩≤(1+r)s−r for s=⟨Au,u⟩, and q−s²≤(1−s)(s−r). Both terms of the rank-one objective increase in q at fixed s. Put s=r+(1−r)t; disjoint spectral slices approaching both endpoints supply all the required limiting two-point weights, irrespective of eigenvalue attainment. At r=1 the normalized operator is I. For r<1 strict concavity and the one-sided slopes give the unique interior maximizer and the derivative equation. At r=0 the root is t=3/4, with derivative of the optimum in r equal to −√3/4 by differentiating at that nondegenerate maximum. Near r=1 the profile expands uniformly as 1+(1−r)[t−1+√(t(1−t))]+O((1−r)²); the bracket has a unique maximizer at (1+1/√2)/2. A t just below 1 gives C(r)>1 for r<1; convex decomposition of A into rI plus the positive r=0 part gives C(r)≤r+(1−r)C(0) for r>0. For rank-one exact attainment with r<1, equality in the nonnegative functional-calculus defect (A−rI)(I−A) forces spectral support at both endpoints because the maximizing weight is interior; endpoint eigenvectors also suffice. This does not rule out higher-rank attainment without endpoint eigenvectors. The uploaded numerical check was read but not run; it does not certify the Hilbert-space result.

## originality

PASS

The universal positive-factor constant and quadratic-operator product bounds with commutation are known. The supported distinction is the sharp fixed-operator profile for every spectral band with rank-one endpoint-attainment criterion. In particular, Ando's factorization gives a broad tool to derive a mixed-vector bound, but does not state a fixed positive multiplier profile or the sharp two-endpoint spectral construction. No available statement of an equivalent or dominating fixed-operator theorem was identified in the bounded comparison; the closest universal-constant paper's detailed proof remains an access risk.

## value

PASS

A fixed positive operator may have a strictly better optimal coefficient than the universal constant; the exact scalar profile quantifies the improvement without any compactness assumption. The endpoint-eigenvalue criterion explains when this optimum has an actual rank-one witness, versus only an approximating sequence. The sharpness construction and infinite-dimensional attainment distinction add substance beyond a numerical interpolation or the universal endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
