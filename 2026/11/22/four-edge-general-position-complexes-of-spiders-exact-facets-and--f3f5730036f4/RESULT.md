# Faces and facets of four-edge-general-position complexes of spiders

## Finding

The edge general-position number records the size of a largest set and does not tell whether all inclusion-maximal sets have that size. For spiders, the four-edge threshold allows a new kind of choice absent at the ordinary three-edge threshold: a doubled arm can coexist with a selected edge on **every** other arm, but a tripled arm must be used alone. The face and facet enumerators below count these different possibilities for arbitrary arm lengths and determine when both sizes of maximal sets occur.

Let \(T=S(\ell_1,\ldots,\ell_d)\) be a finite spider with \(d\ge2\) arms of positive integral edge lengths \(\ell_i\). The arms meet only at the center. Let \(\mathcal K_4(T)\) be the simplicial complex on \(E(T)\) whose faces are sets \(A\) such that no geodesic contains four edges of \(A\). With \(s_i=|A\cap E(\text{arm }i)|\) and \(s_{(1)}\ge s_{(2)}\) the two largest counts, \(A\) is a face exactly when \(s_{(1)}+s_{(2)}\le3\).

The face-size polynomial, including the empty face, is
\[
P_T(z)=\prod_{i=1}^d(1+\ell_i z)+z^2\sum_{i=1}^d\binom{\ell_i}{2}\prod_{j\ne i}(1+\ell_j z)+z^3\sum_{i=1}^d\binom{\ell_i}{3}.
\]
The facet-size polynomial (counting inclusion-maximal faces) is \(F_T(z)=z^d\) when all arms have length one. Otherwise it is
\[
F_T(z)=z^{d+1}\sum_{i=1}^d\binom{\ell_i}{2}\prod_{j\ne i}\ell_j+z^3\sum_{i=1}^d\binom{\ell_i}{3}.
\]
The complex is pure exactly when \(d=2\) or \(\max_i\ell_i\le2\). In the remaining cases, the only facet sizes are \(3\) and \(d+1\), so the purity gap \(d-2\) is unbounded even if all arms except a single length-three arm have length one.

## Assumptions and scope

A geodesic is the unique simple path connecting two vertices. Selected edges on that path need not be consecutive. Edges are distinguished by their positions, though the counts depend only on the lengths. Binomial coefficients with upper argument below the lower argument are zero. The formulas apply to spiders, not arbitrary trees.

## Proof

Every geodesic lies in at most two arms. The geodesic between the leaves of two arms with the largest counts realizes their sum, even when the second count is zero. Thus the maximum number of selected edges on a geodesic is \(s_{(1)}+s_{(2)}\).

The inequality \(s_{(1)}+s_{(2)}\le3\) gives exactly three disjoint cases: at most one selected edge per arm; two in one arm and at most one in every other; or three in one arm and none elsewhere. Choosing the edges on each arm in these cases gives the three terms of \(P_T\).

When all arms have length one, the full edge set is the only facet. Otherwise any face with at most one edge per arm can be enlarged: fill a vacant arm if one exists, or double an arm of length at least two. A face with a doubled arm is maximal exactly when every other arm has one edge, since an empty arm can otherwise be filled and every addition to the fully occupied pattern violates the two-arm bound. A tripled-arm face already is maximal, since every addition gives counts of at least \(4+0\) or \(3+1\). Counting these last two disjoint types gives \(F_T\), including the case \(d=2\) where both contribute to the same coefficient when they exist. If some arm has length at least three, both types occur; their sizes differ exactly when \(d\ge3\). This proves the purity criterion and the asserted gap.

## Verification

The path argument proves the formulas for all positive arm lengths. In the original companion `verify_spider4.py`, the spider enumeration section constructs actual graphs and compares their face and facet counts against the two formulas by testing vertex-pair paths. The program also contains topology tests for the two-edge-arm case, which are not used to establish the finding here.

## Relationship to prior work

Manuel, Prabha and Klavžar define the edge \(k\)-general-position predicate and study extremal sizes, not the face and facet enumerators here. Their earlier tree theorem and the indexed record *All edge general-position sets of spider trees* use the ordinary threshold, where three selected edges along a path are forbidden and a doubled arm must already stand alone. Neither determines the four-edge face/facet counts.

The two-edge-arm sphere wedge and signed integral homology are not separate novelty claims here. In that case the complex is the simplicial composition of the discrete \(d\)-point complex with \(d\) copies of the two-point zero-sphere, so the homotopy type follows from Ayzenberg's general composition theorem (Corollary 6.2). It also has an arm-equivariant model in the extended-star discrete Morse complex studied in Resultary record `348812728b63`. In the incidence notation of that record, replacing each \(y_i\) by \(w_i\) gives a simplicial retraction, contiguous to the identity after inclusion, onto the subcomplex on \(x_i,z_i,w_i\). The only cross-arm incompatibilities are between the \(x_i\), and within each retained arm the pair \(z_i,w_i\) is incompatible. This subcomplex is the subdivision obtained by placing \(x_i\) at the midpoint of the edge with endpoints \(z_i,w_i\). The retraction and subdivision respect the arm permutations, so the prior signed homology calculation transfers.

## Limitations

The enumeration concerns the four-edge threshold on spiders. It does not assert a formula for other thresholds or for general trees. Literature comparisons do not rule out older implicit enumerations.

## References

1. P. Manuel, R. Prabha and S. Klavžar, *Edge general position problem*, Bull. Malays. Math. Sci. Soc. 45 (2022), 2997–3009, arXiv:2105.04292.
2. P. Manuel, R. Prabha and S. Klavžar, *Generalization of edge general position problem*, Art Discrete Appl. Math. 8 (2025), P1.02, arXiv:2207.07357.
3. A. Ayzenberg, *Composition of simplicial complexes, polytopes and multigraded Betti numbers*, arXiv:1301.4459, Proposition 6.1 and Corollary 6.2.
4. *All edge general-position sets of spider trees*, Resultary `96369ffaa123`.
5. *Integral branch-permutation homology of extended-star Morse complexes*, Resultary `348812728b63`.
