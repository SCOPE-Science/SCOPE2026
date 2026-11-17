# The Singer-seven quotient of the Heawood perfect-matching complex is four two-spheres

## Finding
Let \(H\) be the incidence graph of the seven-point Fano plane, with points \(p_j\) and lines \(\ell_a\), for \(j,a\in\mathbb Z/7\mathbb Z\), incident exactly when \(j-a\in\{0,1,3\}\). Let \(\mathcal P(H)\) be the simplicial complex whose vertices are the 21 edges of \(H\), and whose simplices are precisely the edge sets contained in some perfect matching. Simultaneous translation \(p_j\mapsto p_{j+1}\), \(\ell_a\mapsto\ell_{a+1}\) induces the Singer symmetry \(C_7\) of \(\mathcal P(H)\). Then the **ordinary geometric orbit space** has integral homotopy type
\[
\boxed{|\mathcal P(H)|/C_7\simeq\bigvee^{4}S^2.}
\]
In particular the quotient is simply connected, its reduced integral homology is \(\mathbb Z^4\) in degree two and zero in every other degree, and it has no integral homology torsion. The conclusion is a homotopy equivalence, not a homeomorphism classification.

## Assumptions and scope
A perfect matching of \(H\) consists of seven edges covering all fourteen graph vertices, exactly once. A face of \(\mathcal P(H)\) is a subset of at least one perfect matching, with the empty face included as usual. Do not confuse this extendibility complex with the larger ordinary matching complex containing all partial matchings. The chosen Singer generator has order exactly seven. All quotients below are topological geometric quotients; they are not merely quotient posets formed by discarding nontrivial simplex stabilizers.

For reproducibility, order the 21 edges lexicographically by line index \(a=0,\ldots,6\), then point index \(j\in\{a,a+1,a+3\}\), using their representatives in \(\{0,\ldots,6\}\). The accompanying Python verifier enumerates all 24 perfect matchings and their downward-closed face set. The resulting face vector, in dimensions zero through six, is
\[
(21,168,560,756,504,168,24).
\]

## Proof
**1. The covering complex is simply connected.** Enumerating all incidence-respecting point-to-line bijections yields exactly 24 perfect matchings. Every nonempty subset of each perfect matching is admitted, giving precisely 2201 nonempty simplices. On this face poset, scan the 21 ordered edge labels. For each label, pair every currently unmatched face not containing that edge with its one-edge extension whenever both remain unmatched. This produces 1092 disjoint face pairs. The verifier constructs all 8736 nonempty-face Hasse incidences, directing matched incidences upward and every other one downward. A complete topological sort visits all 2201 vertices and therefore proves acyclicity. Exactly one critical vertex and 16 critical two-faces remain. Forman's theorem gives \(\mathcal P(H)\simeq\bigvee^{16}S^2\), in particular \(\pi_1(|\mathcal P(H)|)=0\). This premise is also independently known in the published perfect-matching-complex literature listed below.

**2. A smaller equivariant nerve.** Cover \(|\mathcal P(H)|\) by its 24 maximal seven-vertex simplices, indexed by the perfect matchings. The intersection of any nonempty family of covering simplices is the simplex on the graph edges shared by every matching in that family. Thus all nonempty intersections are contractible. Moreover, if a subgroup fixes the family setwise, it fixes its intersection's barycenter. The equivariant nerve lemma (or its standard equivariant poset-mapping proof) therefore gives a \(C_7\)-homotopy equivalence to the nerve \(N\), and hence a homotopy equivalence of ordinary orbit spaces. The nerve's vertices are the 24 perfect matchings; a set of its vertices is a simplex exactly when those matchings share a graph edge. Each of the 21 graph edges belongs to eight perfect matchings, so the nerve is the union of 21 seven-dimensional facets. Exhaustive downward closure yields its face vector
\[
(24,252,896,1386,1176,588,168,21).
\]

**3. Stabilizers and integral orbit chains.** Singer rotation fixes exactly three of the 24 perfect matchings. These three matchings are pairwise edge-disjoint, so no nerve edge joins two of them. The other 21 perfect matchings lie in three seven-element orbits. Any nonempty positive-dimensional nerve simplex with nontrivial rotational stabilizer would have to be a union of entire seven-orbits of nerve vertices, possibly together with fixed vertices. Such a seven-orbit cannot have a common graph edge: each graph edge itself has a seven-element rotational orbit, so a common edge of seven rotated matchings would force a fixed edge. Consequently the **only** nontrivially stabilized nerve simplices are the three isolated (as fixed simplices, not as graph vertices) singletons. This is independently checked on every one of the 4511 nerve simplices by the verifier.

The barycentric orbit quotient therefore has a valid simplex-orbit \(\Delta\)-complex cellular chain model, with ordinary integer incidence numbers and no higher-dimensional orientation isotropy. Orbit-cell numbers in dimensions zero through seven are
\[
(6,36,128,198,168,84,24,3).
\]
The counts agree independently with Burnside's lemma: there are three fixed vertices and no fixed positive-dimensional faces. For every orbit representative of an ordered simplex, each codimension-one boundary face is transported to its chosen orbit representative by a rotation; the sign of the corresponding vertex permutation is included in the integer incidence coefficient. The verifier computes every boundary matrix and checks \(\partial^2=0\) exactly over \(\mathbb Z\).

**4. Integral reduction.** A cellular boundary coefficient \(+1\) or \(-1\) permits a unimodular cancellation of an adjacent pair of basis cells. At each step, all remaining coefficients are updated by the corresponding integer Schur complement, and the neighboring chain maps are updated consistently. The finite verifier performs precisely 321 such exact unit cancellations, in boundary degrees one through seven respectively
\[
(5,31,93,105,63,21,3).
\]
The reduced **chain complex** has one generator in degree zero and four generators in degree two, with no other generators or nonzero boundary coefficients. These are algebraic chain cancellations, not an assertion that each is a geometric elementary collapse. Thus
\[
H_0(|N|/C_7;\mathbb Z)=\mathbb Z,\qquad
\widetilde H_2(|N|/C_7;\mathbb Z)=\mathbb Z^4,
\]
and all other reduced integral homology groups vanish. The argument is over the integers, not an inference from rational ranks or modular experiments.

**5. The homotopy type.** Each of the three rotation-invariant perfect matchings indexes a maximal simplex of \(\mathcal P(H)\) whose barycenter is fixed by all of \(C_7\). Hence the normal subgroup generated by point stabilizers is the whole cyclic group. Since \(|\mathcal P(H)|\) is simply connected, Armstrong's orbit-space fundamental-group theorem gives \(\pi_1(|\mathcal P(H)|/C_7)=0\). The simply connected finite CW quotient has reduced integral homology only in degree two, freely generated by four classes. Hurewicz supplies sphere representatives, giving a map \(\bigvee^4 S^2\to |\mathcal P(H)|/C_7\) inducing an isomorphism on all integral homology. The homological Whitehead theorem makes this map a homotopy equivalence, completing the proof.

## Verification
Run `python3 verify_heawood_rotation.py` using Python 3's standard library only and compare the deterministic JSON to `verification_output.json`. The successful marker is `VERIFY_OK`. The code regenerates graph incidences, all 24 perfect matchings, the full 2201-face covering complex, its acyclic Hasse matching, the 4511-face equivariant nerve, every rotation orbit and orientation sign, exact integer cellular boundary matrices and all 321 unimodular cancellations. The quotient and covering-space arguments in steps two and five are mathematical applications of standard equivariant-nerve, Armstrong, Hurewicz and Whitehead theorems; a finite computation by itself would not prove those general implications.

## Relationship to prior work
The published *Perfect Morse reduction of the Heawood perfect-matching complex* already identifies the **unquotiented** space as \(\bigvee^{16}S^2\). The published *A duality-sign twist between Heawood perfect and ordinary matching homology* and *Fano duality twists Heawood perfect-matching homology* establish rational characters of the full Heawood automorphism action. Their order-seven trace determines that the Singer quotient has four degree-two **rational** invariant directions, but does not determine its integral homology, possible seven-torsion, fundamental group or homotopy type. The present claim is precisely this integral Singer-orbit homotopy refinement, not the known covering-space wedge or known rational trace.

Bayer, Jelić Milutinović and Vega define perfect-matching complexes and classify selected honeycomb graphs. Their honeycomb classifications do not cover the nonplanar Fano incidence graph or its Singer orbit quotient. The Fano cap-complex quotient and polarity fixed loci of ordinary Heawood matching complexes are different spaces; their homotopy invariants do not imply this result.

## Limitations
The theorem concerns this explicit 14-vertex graph and its specified order-seven subgroup only; it does not classify all Heawood subgroup quotients, general projective-plane incidence graphs or a quotient's homeomorphism type. The exact integer computations are supplied as reproducible exhaustive code rather than short closed-form incidence formulas. The literature comparison includes directly inspected closest public records, but unindexed or unpublished equivalent work remains a priority risk. No independent validation is claimed.

## References
1. *Heawood Graph*, AMS Visual Insight, 2015-08-01, https://blogs.ams.org/visualinsight/2015/08/01/heawood-graph/ .
2. M. Bayer, M. Jelić Milutinović, J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803 (first public 2022-09-06).
3. *Perfect Morse reduction of the Heawood perfect-matching complex*, public record 0994476b8c0d, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-perfect-morse-reduction-of-the-heawood-perfect-matching-complex--0994476b8c0d/RESULT.md .
4. *A duality-sign twist between Heawood perfect and ordinary matching homology*, public record 87b7b3a5140f, https://github.com/published-finding corpus/2026/blob/main/2026/10/18/SCOPE-a-duality-sign-twist-between-heawood-perfect-and-ordinary-matchi--87b7b3a5140f/RESULT.md .
5. *Fano duality twists Heawood perfect-matching homology*, public record 170613b1af40, https://github.com/published-finding corpus/2026/blob/main/2026/11/1/SCOPE-fano-duality-twists-heawood-perfect-matching-homology--170613b1af40/RESULT.md .
6. M. A. Armstrong, *The fundamental group of the orbit space of a discontinuous group*, Proc. Cambridge Philos. Soc. 64 (1968), 299–301, https://doi.org/10.1017/S0305004100042845 .
7. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
