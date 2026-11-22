# Scientific review

## Correctness — PASS
The claim is the exact intrinsic normalized volume, not ambient Euclidean volume. The signed cyclic determinant is nonzero for every stated integer triple. The integral cofactor normal has first coordinate equal to the signed geometric sum and its coordinate differences generate precisely the exceptional-weight difference: these facts reconstruct the gcd formula. A primitive-normal lattice-index calculation converts the coordinate gcd into normalized volume. Bézout's identity closes the critical number-theoretic step, and a separate exact-integer checker confirms 264 parameter triples using independently computed maximal minors. The proof, not finite checks, handles all dimensions and weights.

Risk: a change of normalization would change the statement. The affine lattice and factor of the dimension factorial are explicitly fixed; the proof is not a Euclidean-volume assertion.

## Originality — PASS (historical priority provisional)
Biermann–Lin–O'Keefe, arXiv:2611.17047, Definition 2.5 and Theorem 4.5, introduce the weighted oriented cycle and establish an equal-weight non-IDP result, not the arithmetic lattice-index classification. The closest publicly available weighted-cycle Ehrhart result (published-finding corpus, `b7680edb541b`, its complete RESULT.md inspected) gives arbitrary-weight coefficient reciprocity and a *uniform* five-cycle Ehrhart numerator; its specialized volume does not imply the one-defect gcd stratification. A root-polytope volume statement (`e32575b66377`) concerns signed difference vectors and so does not cover this family. The exact one-defect volume and divisor census were compared by content, not merely by titles, against this literature, published-finding corpus searches, and relevant public claims.

Risk: an unindexed paper might contain the cofactor-gcd calculation. Lack of a search hit is not mathematical proof of historical novelty. The cited primary paper was materially read in the incidence/IDP sections, not exhaustively certified for every possible reformulation.

## Mathematical value — PASS
The volume is the sum of the Ehrhart numerator coefficients and a natural invariant of an integer polytope. The question is whether the non-IDP, exponentially large uniform-weight edge simplex is stable under an elementary defect in one vertex weight. Instead, one step produces a unimodular simplex in *every* dimension, and the full defect parameter exactly realizes the divisor lattice of a geometric-series integer, with a sharp least period and totient density. These are structural classifications and a strong arithmetic stability discontinuity rather than a one-off computed example. The distinction between Euclidean and intrinsic lattice volume is prominently disclosed.

Risk: no result is asserted for general heterogeneous weights or IDP when normalized volume exceeds one; no downstream general theorem is claimed.

Self-review: passed. Independent audit: not yet performed.
