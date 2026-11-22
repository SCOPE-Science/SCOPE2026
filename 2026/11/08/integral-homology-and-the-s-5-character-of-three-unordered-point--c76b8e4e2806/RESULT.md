# The torsion-free second integral homology of three unordered points on the complete graph K5

## Finding and exact scope

Let \(G=|K_5|\) denote the geometric realization of the five-vertex complete graph, and let
\[
B_3(G)=\bigl\{\{x_1,x_2,x_3\}\subseteq G:x_1,x_2,x_3\text{ are distinct}\bigr\}
\]
be the unordered, collision-free three-point configuration space. Then
\[
\boxed{H_2(B_3(G);\mathbb Z)\cong\mathbb Z^{30}.}
\]
In particular, the second integral homology has no torsion of any order. The claim concerns exactly this graph and this number of particles; it does not assert a theorem for all complete graphs or all graph configuration spaces.

**Precise novelty boundary.** The rank \(30\), the rational second-homology character of the natural vertex-permutation action \(S_5\), and its five-Specht-summand decomposition were already established in *The \(\mathfrak S_5\)-character of three-point configuration homology on \(K_5\)* (October 18, 2026; linked below). The first integral homology and its order-two torsion follow from Ko–Park's general graph-braid first-homology theorem. Neither result by itself proves the integral *second*-homology torsion-freeness asserted here. The new assertion is the integral saturation computation for the third cubical boundary, combined with the known rational rank. The previously known rational symmetry character is contextual information, not an additional novelty claim.

## Integral chain model

Subdivide each of the ten original edges of \(K_5\) once. The resulting graph \(G'\) has 15 vertices and 20 half-edges. Every path joining two distinct original degree-four vertices has at least two half-edges, and each nontrivial simple cycle has at least six. For three particles, these satisfy the Prue–Scrimshaw strengthened Abrams subdivision conditions (essential paths of length at least \(3-1=2\), simple cycles of length at least \(3+1=4\)). The finite cubical complex of unordered triples of pairwise closure-disjoint graph cells therefore models \(B_3(G)\) up to homotopy.

A degree-\(k\) cubical generator consists of \(k\) pairwise closure-disjoint open half-edges together with \(3-k\) vertices disjoint from their endpoints. Orient half-edges by ascending endpoint index and the product cube by ascending half-edge index. Replacing one moving half-edge by its terminal or initial endpoint, with the alternating cubical incidence sign, gives the integral boundary \(\partial_k\). Enumerating all cells gives
\[
\operatorname{rank}(C_0,C_1,C_2,C_3)=(455,1560,1650,520).
\]
Direct signed integer expansion verifies \(\partial_1\partial_2=0\) and \(\partial_2\partial_3=0\); there are no cells in degrees exceeding three.

## Integral torsion argument

The essential step is an **integer** elimination of the map
\(\partial_3:\mathbb Z^{520}\to\mathbb Z^{1650}\), not merely a modular or rational rank calculation. Work with sparse columns and choose a coefficient \(+1\) or \(-1\) in a row not yet used as a pivot; using integral elementary row/column operations, clear the chosen pivot and continue. On the actual degree-three boundary all 520 columns admit such unit pivots and the residual matrix is empty. Thus the Smith invariant factors of \(\partial_3\) are exactly 520 copies of 1, and
\[
C_2/\operatorname{im}\partial_3\cong\mathbb Z^{1130}
\]
is free. Since \(\partial_2\partial_3=0\), the group
\[
H_2(B_3(G);\mathbb Z)=\ker\partial_2/\operatorname{im}\partial_3
\]
embeds in \(C_2/\operatorname{im}\partial_3\). Every subgroup of a finitely generated free abelian group is free. Therefore **\(H_2\) is torsion-free**. This is the integral statement not implied by an earlier rational computation.

To determine its rank without relying on an uncited numerical experiment, the previously published exact rational calculation gives \(\dim_{\mathbb Q}H_2=30\). It can also be recovered directly from this same cubical model: an integer unit-pivot reduction of \(\partial_2\) has 1,098 unit pivots and a 23-by-37 residual with Smith nonzero factors 1 and 2. Thus \(\operatorname{rank}\partial_2=1100\); together with \(\operatorname{rank}\partial_3=520\),
\[
\operatorname{rank} H_2=1650-1100-520=30.
\]
The full nonzero Smith factors of \(\partial_2\) are \(1\) repeated 1,099 times and one 2. That 2 contributes to the **known torsion in \(H_1\)**, not to \(H_2\). The connected degree-zero cubical incidence graph yields \(\operatorname{rank}\partial_1=454\), and hence the complete integral groups are
\[
H_0\cong\mathbb Z,\quad H_1\cong\mathbb Z^6\oplus\mathbb Z/2,\quad H_2\cong\mathbb Z^{30},\quad H_i=0\ (i\ge3).
\]
Only the degree-two integral torsion conclusion is advanced as new in this corrected statement.

## Verification and interpretation

The accompanying `k5_three_point_verify.py` constructs every cell and signed boundary, checks both integral chain identities, runs the unit-pivot reductions, and computes the Smith normal form of the exact 23-by-37 residual matrix using SymPy. The adjacent-transposition chain actions, 120 signed Lefschetz traces and rational Specht decomposition are additional consistency checks of previously established representation theory. The printed output `k5_three_point_verify.out` records a successful run; the mathematical reason for torsion-freeness is the primitive integer image of \(\partial_3\), not a success marker or a finite-field check.

The use of an integral computation is substantive: knowing the rational Betti vector and character does not detect integral torsion. Here the lowest nonplanar complete graph has order-two first homology but no second-homology torsion, a concrete distinction relevant to integral graph-configuration homology. No integral \(\mathbb Z[S_5]\)-module structure, canonical integral basis of \(H_2\), or general all-graphs torsion theorem is asserted.

## Relation to prior literature

1. *The \(\mathfrak S_5\)-character of three-point configuration homology on \(K_5\)* (October 18, 2026), https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-the-mathfrak-s-5-character-of-three-point-configuration-homology--2c0746967d76/RESULT.md. Exact same unordered space, its rational degree-two dimension 30, seven-class \(S_5\) character, and Specht decomposition; the prior paper explicitly does **not** rule out integral torsion in degree two.
2. K. H. Ko and H. W. Park, *Characteristics of graph braid groups*, arXiv:1101.2648 (2011), https://arxiv.org/abs/1101.2648. The general first-homology theorem covers the free rank and nonplanar order-two torsion in degree one.
3. P. Prue and T. Scrimshaw, *Abrams's stable equivalence for graph braid groups*, arXiv:0909.5511 (2009), https://arxiv.org/abs/0909.5511. Supplies the graph subdivision criterion used to identify the finite cubical model with the continuous configuration space.
4. E. Ramos and C. H. Yun, *Computing stable homology representations of graph configuration spaces*, arXiv:2606.13813v1 (June 11, 2026), https://arxiv.org/abs/2606.13813. Section 4 and Table 8 study ordered three-point complete-graph configuration homology over \(\mathbb Q\); those data do not establish torsion-freeness for the unordered integral degree-two group.
5. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, Communications in Mathematical Physics 371 (2019), https://doi.org/10.1007/s00220-019-03583-5. Contains general methods and complete wheel-graph cases, including \(K_4\), but not an integral degree-two computation of \(B_3(K_5)\).
6. B. H. An, *Torsion of every finite order in the homology of graph braid groups*, arXiv:2610.04305 (October 3, 2026), https://arxiv.org/abs/2610.04305. Its explicit second-degree torsion results concern complete bipartite graph families, not \(K_5\); they demonstrate why integral torsion is a meaningful issue rather than a rational afterthought.

## Limitations

The torsion-free conclusion is a fully finite, exact statement for \(B_3(K_5)\). The existing rational result is credited. An unindexed earlier integral treatment or a stronger torsion-vanishing theorem specialized to this graph may exist; novelty is best-of-knowledge, not certified universal priority. The code checks integral matrices but does not formally verify the cited subdivision theorem, which is invoked as an external mathematical result.
