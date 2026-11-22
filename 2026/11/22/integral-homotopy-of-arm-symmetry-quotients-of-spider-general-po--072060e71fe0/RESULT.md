# Integral homotopy of arm-symmetry quotients of spider general-position complexes

## Finding
Let \(T_{r,L}\) be the finite tree obtained by identifying one endpoint of \(r\ge3\) pairwise disjoint paths of \(L\ge1\) edges. Its **general-position complex** \(X_{r,L}\) is the simplicial complex of vertex sets containing no three vertices on a common tree geodesic. The natural arm-permutation group \(S_r\) acts on the geometric realization. Write \(Q_{r,L}=|X_{r,L}|/S_r\) for the **ordinary geometric orbit space**, not the homotopy-orbit construction.

**Theorem.** For all integers \(r\ge3\) and \(L\ge1\), there is an integral homotopy equivalence
\[
Q_{r,L}\simeq
\bigvee^{\binom{L}{2}+L-1}S^1\;\vee\;
\bigvee^{\binom{L-1}{r}}S^{r-1}.
\]
As usual, a zero-fold wedge contributes nothing, and binomial coefficients outside their natural range are zero. More precisely, the quotient of the subcomplex consisting of faces selecting at most one vertex per arm admits a **strong deformation retraction** onto the \((r-1)\)-skeleton of the simplex on the \(L\) depth labels, with this skeleton understood as the entire simplex if \(L\le r\). The other faces attach exactly \(\binom L2+L-1\) independent loops up to homotopy.

Consequently, \(\pi_1(Q_{r,L})\) is a free group of rank \(\binom L2+L-1\); all reduced integral homology groups are free abelian, with precisely that rank in degree one and rank \(\binom{L-1}{r}\) in degree \(r-1\), and zero otherwise. A positive-degree top sphere survives **if and only if \(L\ge r+1\)**. For example, \(Q_{3,4}\simeq\bigvee^9 S^1\vee S^2\), whereas \(Q_{4,4}\simeq\bigvee^9S^1\).

## Assumptions and scope
Each arm has vertices \(v_{i,d}\), where \(1\le i\le r\) indexes the arms and \(1\le d\le L\) their distances from the common center \(c\). All edges have unit length, and general position means exclusion of a **vertex triple** with one selected vertex lying on the unique geodesic joining the other two. The group \(S_r\) permutes arm indices while preserving depths and fixing \(c\). Topological statements concern geometric realizations and their ordinary finite-group quotients. No claim is made for arbitrary arm subgroups or unequal arm lengths.

## Proof
**1. Exact faces and the equivariant join.** All singletons and pairs are faces of \(X_{r,L}\). Any face with at least three vertices cannot contain \(c\): two other vertices either lie on distinct arms, making \(c\) intermediate, or on the same arm, making one of the three collinear. It also cannot contain two vertices on the same arm, because any third chosen vertex puts one of the two on a path between the other two chosen vertices. Conversely, a subset disjoint from \(c\) and meeting each arm in at most one vertex is general-position: any geodesic between two chosen vertices traverses only their respective arms and \(c\).

Put \(B_i=\{v_{i,1},\ldots,v_{i,L}\}\), and let \(D(B_i)\) be the discrete simplicial complex on \(B_i\). The resulting subcomplex
\[
J=D(B_1)*\cdots*D(B_r)
\]
contains every face of cardinality at least three and every cross-arm edge. The remaining faces are exactly the \(r\binom L2\) edges joining two distinct vertices **on the same arm** and the \(rL\) edges from \(c\) to arm vertices, plus the central vertex. Each is a one-cell which is not contained in a higher-dimensional face, and the decomposition is \(S_r\)-invariant.

**2. A concrete model for the arm quotient of the join.** A point of \(|J|\) is described by nonnegative barycentric weights \(w_{i,d}\), summing to one, with **at most one nonzero coordinate in each arm** \(i\). Arm permutations merely reorder the arm slots. An orbit is therefore uniquely specified by a multiset of at most \(r\) *weighted depth labels*: for each depth \(d\), list its positive weights in descending order and pad with zeros to obtain
\[
w_{d,1}\ge\cdots\ge w_{d,r}\ge0,\qquad
\sum_{d=1}^{L}\sum_{j=1}^{r}w_{d,j}=1,
\]
with at most \(r\) strictly positive entries over all depths. Sorting the coordinates in each depth class is continuous (finite sorting is continuous and piecewise linear). The sorted data determine the orbit uniquely, and compactness of \(|J|/S_r\) makes the resulting bijection with this closed Euclidean chamber a homeomorphism. Vanishing coordinates cause no ambiguity because they are padded by zeros.

Define, for \(0\le t\le1\),
\[
w_{d,1}(t)=w_{d,1}+t\sum_{j=2}^r w_{d,j},\qquad
w_{d,j}(t)=(1-t)w_{d,j}\quad(2\le j\le r).
\]
The resulting coordinates remain nonnegative, nonincreasing within each depth, and sum to one; the total count of positive entries never increases. Thus this is a continuous homotopy inside the **actual geometric quotient**. It fixes every point having at most one positive weight at each depth. At \(t=1\), all repeated-depth weights have coalesced into a single weight. The fixed endpoint subspace is precisely the complex of nonnegative weights on the \(L\) distinct depth labels supported on at most \(r\) labels: the \((r-1)\)-skeleton \(K_{r,L}=\operatorname{sk}_{r-1}\Delta^{L-1}\) of a standard simplex (or the full simplex if \(r\ge L\)). Hence \(|J|/S_r\) **strongly deformation retracts** to \(K_{r,L}\), fixing the \(L\) depth vertices throughout.

**3. Integral homotopy of the skeleton.** For \(r\ge3\), match each nonempty simplex of \(K_{r,L}\) not containing the first depth label and having at most \(r-1\) vertices with the simplex formed by adding that label. The matching is acyclic: after a reversed matched inclusion, membership of the first label cannot be returned to the prior state through a different matched pair. The sole critical vertex is the first label, and the sole remaining critical higher cells are the \(r\)-vertex faces omitting it. Their number is \(\binom{L-1}{r}\), each of dimension \(r-1\). In particular, the Morse CW complex has one zero-cell and top-dimensional cells only, with no attaching obstructions. It is homotopy equivalent to \(\bigvee^{\binom{L-1}{r}}S^{r-1}\); this is a statement of **integral homotopy**, not a field rank calculation. If \(L\le r\), the simplex is contractible and the count is zero.

**4. Attaching the remaining orbit edges.** In the quotient, the \(r\binom L2\) intra-arm edges form exactly \(\binom L2\) distinct one-cells: one for every unordered pair of *distinct depths*. Their endpoints lie in the connected quotient \(|J|/S_r\), and they are not identified with any cross-arm one-cell. The common center gives one new vertex \(c\), with \(L\) distinct orbit edges \(c-v_d\), one for every depth. The first of these edges attaches the new vertex contractibly, while each of the remaining \(L-1\) central edges adds a circle. Every intra-arm edge also adds a circle, because both its endpoints already lie in the connected base and it is not bounded by a new higher cell. More formally, an interval attached along its two endpoints to a path-connected CW complex is homotopy equivalent to wedging a circle; apply the statement successively, first attaching a spanning edge to the new vertex. Since the deformation retraction in Step 2 fixes all depth vertices, this identification of attaching points is compatible with replacing \(|J|/S_r\) by the simplex skeleton. The resulting wedge is exactly the theorem.

## Verification
The standalone standard-library Python script `verify.py` independently constructs each spider, computes every pairwise graph distance by breadth-first search, enumerates general-position faces directly from the no-collinear-triples condition, and compares them with the decomposition in Step 1. For each profile it barycentrically subdivides the **entire** complex, enumerates orbits of nested face flags under every arm permutation, and forms the signed integral cellular boundary maps of that finite geometric quotient. The script checks that consecutive boundaries compose to zero **over the integers**, then computes independent exact boundary ranks over each of the primes \(2,3,5,7\). Ten exhaustive profiles, \(r=3,4\) and \(1\le L\le5\), give forty agreeing field-rank comparisons. All tests pass and are recorded in `verification_output.txt`.

Examples: \((r,L)=(3,4)\) has quotient Betti vector \((1,9,1)\); \((4,5)\) has \((1,14,0,1)\). These tests cannot rule out torsion at untested primes or establish the unrestricted theorem. Integral torsion-freeness, the free fundamental group, and the full homotopy equivalence follow from Steps 2–4, not from the finite computations.

## Relationship to prior work
The graph general-position literature introduced counting polynomials and exact descriptions of general-position sets; Rather (first publicly posted 6 March 2026) studies further graph classes and distributional phenomena. The public result *General position polynomials of spiders and the smallest nonunimodal spider* already establishes the labelled spider face description and the general-position polynomial. Neither statement settles the geometric orbit space.

A directly overlapping prior scientific result, *Integral arm-symmetry homology of spider general-position complexes* (opaque item ID `82f2669d-efb7-42f8-9d07-3825da408f96`), determines the unquotiented integral homology and complete arm-permutation character, and deduces **only the rational Betti ranks** of this very same quotient, including the two numerical formulas above. Its stated limitations explicitly leave the quotient's fundamental group, integral torsion and homotopy type unresolved. The present theorem therefore does **not** claim those rational ranks or the face decomposition as original; it establishes the stronger actual quotient deformation retraction and **integral homotopy classification**, which are not implied by knowing rational ranks or an integral representation before quotienting. As a basic warning, integral torsion can be introduced by taking finite symmetry quotients even when the original space has free integral homology.

A further closely related result, *Partwise-symmetric orbit spaces of higher independence complexes*, treats independent permutations **within** the parts of complete multipartite higher-independence complexes and similarly obtains simplex skeletons. Its graph complex, admissible faces and group action differ: here the group exchanges whole arms, and the additional intra-arm and central one-cells are essential to the circle count. Likewise, the prior classification of geodesic-avoidance complexes of clique bouquets applies to avoidance of maximal geodesics, not general-position triples of spiders. No statement among these inspected sources gives an exact integral homotopy of the present arm quotient. The weighted-label collapsing argument may be recognized as an instance of broader symmetric-join topology; unindexed equivalent formulations remain a priority risk.

## Limitations
This theorem applies only to equal-length spider arms, \(r\ge3\), and the **full** arm-permutation group; it does not classify quotients by proper subgroups, arbitrary nonuniform spiders, fixed-point spaces, cohomology operations, or homotopy-orbit spaces. The statement is an ordinary integral homotopy equivalence, not a PL homeomorphism. Computational verification is finite and uses four primes; its role is to test implementations and examples, not to certify an all-parameter assertion or publication uniqueness. Independent mathematical review has not been performed.

## References
1. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930v1, first posted 2026-03-06, https://arxiv.org/abs/2603.06930.
2. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, Results in Mathematics 79 (2024), article 110; arXiv:2401.05696v1, first posted 2024-01-11, https://doi.org/10.1007/s00025-024-02133-3.
3. *General position polynomials of spiders and the smallest nonunimodal spider*, publicly indexed 2026 research result, stable identifier `86888c8b4991`.
4. *Integral arm-symmetry homology of spider general-position complexes*, earlier research result, stable identifier `82f2669d-efb7-42f8-9d07-3825da408f96`.
5. *Partwise-symmetric orbit spaces of higher independence complexes*, publicly indexed 2026 research result, stable identifier `64a4b2681b9d`.
6. *Mixed-dimensional integral homotopy of geodesic-avoidance complexes of clique bouquets*, publicly indexed 2026 research result, stable identifier `225b533c1864`.
