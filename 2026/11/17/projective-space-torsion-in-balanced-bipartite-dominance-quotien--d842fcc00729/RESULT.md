# Projective-space torsion in balanced bipartite dominance quotients

## Finding
Let \(k\ge3\) be an integer, let \(G=K_{k,k}\), and let \(\mathcal D(G)\) be its dominance complex: a subset of vertices is a face when its complement dominates \(G\). Put \(A=A_k\), \(S=S_k\), and let \(\iota\) exchange the two shores of the balanced complete bipartite graph. For ordinary **geometric orbit spaces** (not homotopy quotients), there are natural homotopy classifications
\[
\begin{aligned}
|\mathcal D(G)|/(A\times A)&\simeq S^{2k-3}\vee S^{k-1}\vee S^{k-1},\\
|\mathcal D(G)|/((A\times A)\rtimes\langle\iota\rangle)&\simeq
\Sigma^{k-1}\mathbb{RP}^{k-2}\vee S^{k-1},\\
|\mathcal D(G)|/((S\times S)\rtimes\langle\iota\rangle)&\simeq\{\mathrm{pt}\}.
\end{aligned}
\]
Here \(\Sigma\) denotes reduced suspension, and the semidirect product interchanges the two factors. In particular, for \(k=4\), the middle space has type
\[
S^3\vee M(\mathbb Z/2,4),
\]
where \(M(\mathbb Z/2,4)\) is the mod-two Moore space with its unique nonzero reduced integral homology \(\mathbb Z/2\) in degree four. For every \(k\ge4\), the middle orbit space contains integral two-primary torsion in degree \(k\); the torsion lies in every degree \(k+2j\) for \(0\le j\) with \(2j+1<k-2\). Thus the three canonical symmetry levels have sharply different homotopy and torsion behavior.

## Assumptions and scope
The two shores \(L\) and \(R\) each contain exactly \(k\) labeled vertices. A dominating subset \(T\) meets or neighbors every vertex; \(\mathcal D(G)=\{\sigma\subseteq L\sqcup R:(L\sqcup R)\setminus\sigma\text{ is dominating}\}\). The alternating groups act by even permutations independently on the two shores. The exchange \(\iota\) uses a fixed bijection between the two equally sized shores, conjugating \((a,b)\) into \((b,a)\). No claim is made for \(k<3\), unequal shore sizes with exchange, or alternative domination definitions. All quotients are ordinary realizations divided by the indicated finite actions, including points with nontrivial stabilizers. Reduced suspensions have their ordinary based homotopy meaning.

## Proof
**1. An equivariant three-piece decomposition.** Write \(\Delta_L\), \(\Delta_R\) for the simplices on the two shores and \(\partial\Delta_L\), \(\partial\Delta_R\) for their boundaries. A subset of vertices is a dominance face exactly when neither entire shore is contained in it, or it equals one entire shore and contains nothing from the other. Indeed, the closed neighborhood of any vertex on one shore consists of that vertex and the opposite shore, so avoiding all closed neighborhoods is equivalent to the stated criterion. Consequently, as simplicial complexes,
\[
\mathcal D(G)=(\partial\Delta_L*\partial\Delta_R)\cup\Delta_L\cup\Delta_R,
\]
with \(\Delta_L\cap(\partial\Delta_L*\partial\Delta_R)=\partial\Delta_L\), the analogous intersection for \(R\), and disjoint geometric realizations of the two full shore simplices. This decomposition is equivariant for all three indicated groups.

**2. The alternating quotient of a simplex boundary.** Radially identify \(|\partial\Delta^{k-1}|\) with the unit sphere in the sum-zero standard representation \(V=\{(x_1,\ldots,x_k)\in\mathbb R^k:\sum x_i=0\}\). The reflection group \(S_k\) has a closed spherical fundamental chamber \(x_1\le\cdots\le x_k\), homeomorphic to a closed \((k-2)\)-ball. Its orientation-preserving index-two subgroup \(A_k\) identifies exactly the even chambers. The quotient of the sphere by \(A_k\) is the double of one chamber along its entire boundary, therefore is homeomorphic to \(S^{k-2}\). In the same way, the simplex itself is the cone over its boundary, so its quotient by \(A_k\) is a closed \((k-1)\)-ball. The quotient by \(S_k\) of the boundary is the single chamber, a closed \((k-2)\)-ball. These homeomorphisms may be chosen identically on the two shores, so shore exchange interchanges the factors without an additional twist.

**3. The side-preserving alternating quotient.** Quotienting the join by the two independent factors gives
\[
(\partial\Delta_L*\partial\Delta_R)/(A\times A)
\cong(\partial\Delta_L/A)*(\partial\Delta_R/A)
\cong S^{k-2}*S^{k-2}\cong S^{2k-3}.
\]
The two full simplices become closed \((k-1)\)-balls attached along their boundary spheres \(S^{k-2}\) embedded as the two endpoint factors of the join. As \(k-2<2k-3\), both attaching maps are nullhomotopic. Attaching a \((k-1)\)-ball along a nullhomotopic map from its entire boundary adds a wedge summand \(S^{k-1}\). There are two such attachments, proving the first line.

**4. Adjoining shore exchange to the alternating action.** After the preceding quotient, exchange acts on \(S^{k-2}*S^{k-2}\) by swapping identical sphere factors. Write the ambient orthogonal representation as \(V\oplus V\), and diagonalize exchange into its \(+1\) eigenspace \(V_+\) and its \(-1\) eigenspace \(V_-\), each of real dimension \(k-1\). The unit-sphere join description gives the homeomorphism
\[
(S^{k-2}*S^{k-2})/\langle\iota\rangle
\cong S(V_+)*\bigl(S(V_-)/\{\pm1\}\bigr)
\cong S^{k-2}*\mathbb{RP}^{k-2}
\simeq\Sigma^{k-1}\mathbb{RP}^{k-2}.
\]
The two attached shore balls are interchanged and hence descend to a **single** \((k-1)\)-ball. Its entire attaching boundary \(S^{k-2}\) maps into the displayed join quotient. That target is \((k-1)\)-connected for \(k\ge3\): projective space is path connected and each suspension increases connectivity by one. The attaching map is therefore nullhomotopic, giving exactly one extra \(S^{k-1}\) summand. This proves the second line. The reduced integral homology of \(\mathbb{RP}^{k-2}\) has \(\mathbb Z/2\) in each positive odd degree below \(k-2\); suspension shifts these degrees upward by \(k-1\). At \(k=4\), the threefold suspension of \(\mathbb{RP}^2\) is the mod-two Moore space in degree four. This proves all torsion assertions.

**5. The full symmetry quotient.** Under \(S_k\times S_k\), each boundary factor becomes a closed \((k-2)\)-ball, and the base join becomes a ball. Each full shore simplex becomes a \((k-1)\)-ball, attached along a closed \((k-2)\)-ball. By elementary homotopy pushout (or contracting these ball pairs), the side-preserving symmetric quotient is contractible. More directly for the full wreath group, the base join admits an exchange-equivariant contraction: contract each factor ball toward its unique barycenter using the same linear homotopy, then contract the resulting segment of joins to its midpoint, which is exchange fixed. Its exchange quotient is therefore contractible. The two shore simplex balls are interchanged and become one ball, attached along a contractible boundary chamber; the homotopy pushout of these contractible spaces remains contractible. This proves the third line.

## Verification
The standalone Python 3 file `verify_quotients.py` enumerates every nonempty face of \(\mathcal D(K_{k,k})\), constructs the independent permutations and shore exchange, and computes the exact Euler characteristic of each orbit space using signed fixed-face Lefschetz sums followed by Burnside averaging. The checked cases are \(k=3,4\), with respectively 50 and 226 nonempty faces. For the alternating product, alternating exchange, symmetric product, and full wreath quotient, the computed Euler-characteristic quadruples are \((2,1,1,1)\) for \(k=3\) and \((-2,0,1,1)\) for \(k=4\). They agree with the displayed homotopy types. This is a finite independent consistency check; the uniform theorem is proved by the chamber and homotopy-pushout argument rather than extrapolation from computation.

## Relationship to prior work
Ehrenborg and Hetyei introduced dominance complexes and studied their homotopy for forests, not the balanced complete-bipartite symmetry orbit spaces. The pre-existing complete-multipartite dominance-complex classification yields the unquotiented wedge \(S^{2k-3}\vee S^{k-1}\vee S^{k-1}\), and expressly does not provide equivariant quotients. Matsushita and Wakatsuki establish a general Alexander-duality relation with neighborhood complexes and compute other graph families; their published formulation does not imply the orbit-space projective suspension, attaching map, or parity threshold. The present argument explicitly passes from alternating chamber doubles to a factor-swap representation sphere, which creates integral torsion not detected by the unquotiented free homology.

## Limitations
All assertions concern ordinary geometric quotients, not Borel quotients. The result depends on the special independent full-shore simplex attachments in balanced complete bipartite dominance complexes and does not automatically extend to arbitrary bipartite graphs or arbitrary subgroup actions. The theorem is a homotopy classification, not a PL homeomorphism classification of the full complexes. The proof uses standard Coxeter chamber and join topology but supplies the required identifications and nullhomotopies; no external formal proof certification is claimed. Literature priority cannot be guaranteed against unindexed equivalent formulations.

## References
1. R. Ehrenborg and G. Hetyei, *The topology of the independence complex*, European Journal of Combinatorics 27 (2006), 906–923, first online 28 November 2005, DOI: `10.1016/j.ejc.2005.04.010`, author-hosted PDF: https://www.ms.uky.edu/~jrge/papers/independence.pdf.
2. T. Matsushita and S. Wakatsuki, *Dominance complexes, neighborhood complexes and combinatorial Alexander duals*, arXiv:`2312.02639` (first posted 5 December 2023), https://arxiv.org/abs/2312.02639.
3. *A perfect Morse matching and the full homotopy type of complete-multipartite dominance complexes*, published research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-perfect-morse-matching-and-the-full-homotopy-type-of-complete--66f0f7d8ef3a (the unquotiented comparison result).
