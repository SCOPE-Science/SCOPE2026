# Integral homotopy and symmetry of multipartite geodesic general-position complexes

## Finding
Let \(t\ge2\) and let \(a_1,\ldots,a_t\) be positive integers. For the connected complete multipartite graph \(G=K_{a_1,\ldots,a_t}\), define \(\operatorname{GP}(G)\) as the abstract simplicial complex consisting of all vertex sets with no three distinct selected vertices occurring on a common shortest path in \(G\). Write \(N=\sum_i a_i\) and \(P=\prod_i(a_i-1)\). Then the **integral homotopy classification** is
\[
|\operatorname{GP}(G)|\simeq\left(\bigvee^{N-t}S^1\right)\vee\left(\bigvee^{P}S^{t-1}\right).
\]
A wedge with zero summands is omitted. For \(t=2\) the two families both lie in degree one, so the type is \(\bigvee^{a_1a_2-1}S^1\). For \(t\ge3\), the only possibly nonzero reduced integral homology groups are \(\widetilde H_1\cong\mathbb Z^{N-t}\) and \(\widetilde H_{t-1}\cong\mathbb Z^P\). In particular no integral torsion occurs.

The classification also has a **canonical integral symmetry refinement** when \(t\ge3\). Let \(V_i\) be the partite sets and \(I_i=\ker(\mathbb Z^{V_i}\xrightarrow{\sum}\mathbb Z)\), with its natural permutation action. Under the full graph automorphism group (including exchanges of equally sized parts), the natural modules are
\[
H_1(\operatorname{GP}(G);\mathbb Z)\cong\bigoplus_{i=1}^t I_i,
\qquad
\widetilde H_{t-1}(\operatorname{GP}(G);\mathbb Z)\cong\bigotimes_{i=1}^t I_i.
\]
A part exchange permutes the corresponding summands in degree one, and acts on the tensor factors in degree \(t-1\) with the sign of the permutation of part positions. For part-preserving automorphisms there is no extra sign. Both identifications are natural, not merely rational character equalities.

## Assumptions and scope
All graphs are finite, undirected, simple and unweighted, and shortest paths use ordinary graph distance. The parts \(V_1,\ldots,V_t\) are nonempty, with \(t\ge2\); singleton parts and repeated part sizes are permitted. A general-position set has no ordered triple of distinct members \(u,w,v\) for which \(d(u,v)=d(u,w)+d(w,v)\). The complex includes the empty face. The group action is induced by permutations of vertices preserving graph adjacency, including permutations of equal-sized parts. The homotopy equivalence need not be equivariant; the displayed integral homology identifications are equivariant.

## Proof
**1. Identify every face.** Vertices in different parts have distance one, and distinct vertices in one part have distance two, with any vertex in another part lying on a shortest path between them. Therefore a vertex set is in general position precisely when it is contained in one part or it contains at most one vertex from each part. This criterion is also Theorem 3.1 of Rather (2026), and is used here with explicit credit.

Let \(D_i\) be the zero-dimensional simplicial complex on \(V_i\), \(\Delta_i\) the full simplex on \(V_i\), and \(J=D_1*\cdots*D_t\) the join. The exact labelled face decomposition is
\[
\operatorname{GP}(G)=J\cup\bigcup_{i=1}^t\Delta_i,
\qquad J\cap\Delta_i=D_i,
\qquad |\Delta_i|\cap|\Delta_j|=\varnothing\quad(i\ne j).
\]
The last assertion concerns geometric realizations; all abstract complexes share the empty face. The join \(J\) is path connected since \(t\ge2\).

**2. Attaching the full part simplices.** For each \(i\), \(\Delta_i\) is contractible and its intersection with the previously assembled connected complex consists of the \(a_i\) isolated vertices \(D_i\). The ordinary union is a homotopy pushout of cellular inclusions. The map from the discrete \(D_i\) to the connected preceding complex can be homotoped to a constant map; likewise the map into \(\Delta_i\) can be homotoped to a constant. Homotopy invariance of the pushout then gives a wedge of the preceding complex with \(a_i-1\) circles. Iterate for all \(i\) to obtain
\[
|\operatorname{GP}(G)|\simeq |J|\vee\bigvee^{\sum_i(a_i-1)}S^1.
\]
This is a homotopy equivalence, not just a calculation of ranks.

**3. Identify the join.** Each discrete \(D_i\) has reduced degree-zero homology \(I_i\), a free group of rank \(a_i-1\). The join of two nonempty complexes is homotopy equivalent to a suspension of their smash product after choosing basepoints. Inductively,
\[
|J|\simeq\bigvee^{\prod_i(a_i-1)}S^{t-1}.
\]
If any \(a_i=1\), the join is a cone and the product is zero. Combining this with Step 2 proves the complete homotopy statement and its integral torsion-freeness. When \(t=2\), the total number of circles is \((a_1-1)(a_2-1)+(a_1-1)+(a_2-1)=a_1a_2-1\).

**4. Natural integral symmetry.** For \(t\ge3\) the join has \(H_1(J;\mathbb Z)=0\). Excision for the pair \((\operatorname{GP}(G),J)\) identifies its relative homology with the direct sum of \(H_q(\Delta_i,D_i;\mathbb Z)\). Since each \(\Delta_i\) is contractible, this relative group is \(I_i\) in degree one and zero in every higher degree. The long exact sequence of the pair therefore gives a natural isomorphism \(H_1(\operatorname{GP}(G);\mathbb Z)\simeq\bigoplus_i I_i\) and a natural isomorphism \(\widetilde H_{t-1}(J;\mathbb Z)\simeq\widetilde H_{t-1}(\operatorname{GP}(G);\mathbb Z)\). The integral join chain construction identifies the latter with \(\bigotimes_i I_i\). Interchanging two consecutive join factors reverses orientation of every top simplex, hence contributes a sign \(-1\); arbitrary part permutations contribute their permutation sign. Naturality supplies the stated full automorphism action without requiring an equivariant wedge decomposition.

## Verification
The accompanying standalone `verify.py` constructs the graph distances independently, checks all selected triples against the geodesic criterion, and verifies equality with the join-plus-full-simplex face description for ten labelled parameter cases, including singleton parts, two parts, three parts, four parts, and unequal sizes. Exact bitwise mod-two boundary reduction then checks every reduced Betti rank against the formula. Additional signed simplicial Lefschetz computations for within-part transpositions and equal-sized part exchanges check the two integral-module character predictions. Run `python3 verify.py`; the complete expected stdout appears in `expected.txt`. These finite tests are corroboration; the proof above covers **all** positive part sizes and all \(t\ge2\).

## Relationship to prior work
Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials* (first publicly posted March 6, 2026), Theorem 3.1, established the precise face criterion, and Theorem 3.4 computed its entire face polynomial. Those combinatorial statements are not new here and are expressly credited. The present addition is the all-parameter integral **homotopy** classification together with canonical integral homology representations, including the signs from permuting equal-sized parts. Related published classifications of geodesic-avoidance complexes of clique bouquets concern avoidance of entire inclusion-maximal geodesics in another graph, whereas this complex forbids triples on *any* shortest path. Published total mutual-visibility complexes of complete multipartite graphs impose another visibility condition on every vertex pair, and their homotopy ranks and dimensions differ.

## Limitations
The classification does not concern disconnected graphs, weighted metrics, induced-path or maximal-geodesic avoidance, mutual visibility, or arbitrary graph classes. A homotopy equivalence is provided but is not claimed equivariant. The degree-one integral symmetry module for the special case of exactly two parts is not classified here, although its ordinary homotopy type is. An unindexed equivalent topological result cannot be excluded merely by search; no independent external mathematical audit has been performed.

## References
1. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930 (first posted 2026-03-06), especially Theorems 3.1 and 3.4, https://arxiv.org/abs/2603.06930.
2. S. Klavžar, J. Tuite and U. Chandran, *The General Position Problem: A Survey*, arXiv:2501.19385, https://arxiv.org/abs/2501.19385 (context and terminology).
3. *Mixed-dimensional integral homotopy of geodesic-avoidance complexes of clique bouquets*, publicly available scientific note, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-mixed-dimensional-integral-homotopy-of-geodesic-avoidance-comple--225b533c1864 (different forbidden-geodesic construction).
4. *Nonpure sphere-wedge total-visibility complexes of complete multipartite graphs*, publicly available scientific note, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-nonpure-sphere-wedge-total-visibility-complexes-of-complete-mult--a3ad239f881c (different mutual-visibility construction).
