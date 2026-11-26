# Independent mathematical audit

## correctness

PASS

For a fixed nontrivial additive character of F_q, distinct F_q-linear functionals on the radical give distinct radical characters: a nonzero difference surjects onto F_q. Their torus stabilizer consists of diagonal units constant on each connected component of the nonzero unordered edge support; loops contribute free dual coordinates. Each support contributes q^L times the product of (q^{a_e}-1) dual vectors; divide by R^{r(S)} for orbit counts, then multiply by R^{c(S)} for the linear twists of the little-group extensions. This proves the multiplicities and, via subset expansions, the two Tutte specializations, including empty support and disconnected graphs. The split-basic extension uses lifting of orthogonal primitive idempotents to split the diagonal quotient. At q=2 the torus is trivial and the exponents do not resolve degrees. A direct bounded centralizer census over F_3 gives 6480 commuting pairs for the 216-element directed triangle, hence 30 classes. The abelianization has order 8 because diagonal conjugation generates every off-diagonal radical coordinate, so the degree-squares identity with degrees 1, 2 and 4 recovers multiplicities 8, 12 and 10. Replay: node /workspace/independent_checks.js, section 5. This is one finite case; the orbit argument proves the universal claim. The uploaded verifier was inspected, not executed.

## originality

FAIL

Earlier indexed results already give the complete class-size spectrum of the same groups, including arbitrary loops, repeated arrows and orientations. For q>2 the claimed degree spectrum is a direct coefficient extraction and rescaling: if K_j is the number of conjugacy classes of size R^j, the claimed degree-R^j multiplicity is R^{r(E)-j} K_j. Indeed the centralizer in the additive radical N of an element nt is Fix_N(t); the rest of its centralizer projects to the p'-group T. Thus its class size is prime to p=char(F_q) precisely when t acts trivially on N, which allows exactly R^{c(E)} diagonal projections. In each such fiber the class sizes are just the lengths of torus orbits on the radical. Primal and dual orbit counts at each length coincide because both have the same number of vectors per unordered support and the same stabilizer orders. The little-group count multiplies each dual orbit of length R^j by R^{n-j} instead of the R^{c(E)} copies in the class spectrum. This establishes coverage of the full degree polynomial, not merely equality of total class counts or similarity of the invariants in the titles. The q=2 branch is the immediate abelian endpoint. The Tutte and random-cluster forms are rewritings of the same enumerator.

## value

FAIL

The complete degree distribution is a natural invariant, and the proof is concise, but this specific exact result is already mechanically recoverable from the prior complete class spectrum with a one-coefficient rescaling. Neither the compact polynomial rewrite nor the separate abelian endpoint supplies a distinct nonroutine invariant or a new consequence not inherited by that conversion. No substantively different validated repair is supplied.

The dated certificate retains the supplied scientific assessment, sources and limitations.
