# An integral two-torsion staircase in signed toroidal path homology

## Finding

**Theorem.** Fix an integer \(r\ge2\) and integers \(m_1,\ldots,m_r\ge5\). Let \(G\) be the bidirected Cartesian product of undirected cycles \(C_{m_1}\square\cdots\square C_{m_r}\). Give every edge positive sign except the edges crossing the seam between residues \(m_1-1\) and \(0\) in the first coordinate; these edges have negative sign, with the same sign in both directions. The corresponding connected signed double cover is the bidirected graph
\[
\widetilde G=C_{2m_1}\square C_{m_2}\square\cdots\square C_{m_r},
\]
with deck involution \(\tau\) translating the first coordinate by \(m_1\).

For integral *regular* GLMY path chains define the signed chain complex to be
\[
\Omega_p^-(\widetilde G;\mathbb Z)
=\{c\in\Omega_p(\widetilde G;\mathbb Z):\tau c=-c\},
\]
with the inherited boundary; its homology is denoted \(H_p^-(\widetilde G;\mathbb Z)\). Here \(\Omega_p\) consists of integer combinations of allowed regular directed \(p\)-paths whose regular boundaries remain allowed. Then for every \(q\ge0\),
\[
\boxed{H_q^-(\widetilde G;\mathbb Z)\cong
\begin{cases}
(\mathbb Z/2\mathbb Z)^{\binom{r-1}{q}},&0\le q\le r-1,\\
0,&q\ge r.
\end{cases}}
\]
In particular, all positive-dimensional degrees up to \(r-1\) carry integral two-torsion, yet the corresponding real signed path homology vanishes in every degree. The cover itself has torsion-free integral path homology of a topological \(r\)-torus. These are three different constructions: homology of the integral anti-invariant *chain subcomplex*, anti-invariants taken *after* homology, and ordinary unsigned homology of the cover.

## Assumptions and scope

Cycles have the standard undirected edges \(i\sim i+1\pmod{m_j}\), replaced by both directed arrows. All lengths are at least five to avoid triangles and intrinsic four-cycles in a factor. Cross-product edges change precisely one coordinate. The regular boundary deletes one entry with its alternating sign and drops resulting paths with adjacent equal vertices. The signed group uses anti-invariants **before** taking homology, not \(H_q(\widetilde G;\mathbb Z)^-\). A deck-free orbit of ordinary allowed paths has two elements, and the anti-invariant module has integral basis their differences. All assertions are integral; rational vanishing is a consequence, not an input.

The chosen signing has negative holonomy around each first-coordinate fundamental cycle and positive holonomy around the other coordinate cycles and elementary coordinate squares. Its cover is a Cartesian product, which makes the integral calculation possible without assuming a general signed Künneth theorem.

## Proof

**1. A cycle has an equivariant cellular chain model.** Let \(N\ge5\), and let \(B_N\) be the bidirected cycle. In degree zero the regular path complex has basis its \(N\) vertices; in degree one it has both oriented arcs on each of the \(N\) edges. In degree \(p\ge2\), every integer \(\partial\)-invariant allowed chain is a combination of the two alternating walks of length \(p\) on each undirected edge. Indeed, an allowed nonalternating path contains a triple of distinct consecutive vertices. Deleting its middle vertex creates a forbidden shortcut between distance-two vertices. In a cycle of length at least five, that ordered distance-two pair has a unique common neighbor, so the corresponding forbidden regular face has a unique possible allowed insertion. Its coefficient cannot be canceled by any other path. Repeating this argument eliminates all nonalternating paths. Conversely, the alternating walks are \(\partial\)-invariant because every internal deletion makes consecutive vertices equal and hence is zero in the regular complex.

For each undirected edge choose the cyclic orientation and write \(a_p,b_p\) for its two alternating \(p\)-paths, starting respectively in the positive and reverse direction. When \(p\ge3\),
\[
\partial a_p=b_{p-1}+(-1)^p a_{p-1},\qquad
\partial b_p=a_{p-1}+(-1)^p b_{p-1}.
\]
For \(p=2\), both alternating paths have boundary equal to the sum of the two directed one-arcs. Therefore the sequence in degrees \(p\ge2\) is an integral split acyclic complex after identifying the two directions of each edge via the degree-two boundaries; the matrices above have rank one and a unit entry, and each kernel is the image in the next degree. This identification gives a chain-homotopy equivalence between \(\Omega_*(B_N;\mathbb Z)\) and the standard cellular cycle complex
\[
\mathbb Z^{N}\xrightarrow{\ d\ }\mathbb Z^{N},
\qquad d(e_i)=v_{i+1}-v_i.
\]
The edge orientations, integral direct-sum splittings, and contractions are chosen identically at all edge positions, so this chain equivalence commutes with every cyclic translation, in particular with translation by half of an even cycle.

**2. Integral product and the sign subcomplex.** The natural, integral Eilenberg–Zilber shuffle for the box product is a chain isomorphism of regular path complexes over a principal ideal domain (Fu–Yau, Theorem 2.7; see References). For bidirected graphs the box product is the directed Cartesian graph product. Iteration, with naturality in graph automorphisms, gives
\[
\Omega_*(\widetilde G;\mathbb Z)\cong
\Omega_*(C_{2m_1};\mathbb Z)\otimes
\bigotimes_{j=2}^{r}\Omega_*(C_{m_j};\mathbb Z).
\]
The deck involution acts only on the first tensor factor. All other factor chain groups are free, so taking first-factor anti-invariants commutes with this tensor product. Replacing the factors by the cellular cycle chain models from Step 1 preserves chain homotopy equivalences integrally and equivariantly in the first factor.

**3. The integer sign obstruction.** In the first cellular factor, use anti-invariant bases \(w_i=v_i-v_{i+m_1}\) and \(f_i=e_i-e_{i+m_1}\), \(0\le i<m_1\). The boundary is
\[
\partial f_i=w_{i+1}-w_i\quad(0\le i<m_1-1),
\qquad \partial f_{m_1-1}=-w_0-w_{m_1-1}.
\]
Integral elimination along the first \(m_1-1\) edges identifies all vertex generators; the last column gives precisely twice that generator. Equivalently this \(m_1\)-square integer boundary matrix has Smith diagonal \((1,\ldots,1,2)\). Thus its two-term chain complex has \(H_0\cong\mathbb Z/2\mathbb Z\) and \(H_1=0\). It is chain-homotopy equivalent over \(\mathbb Z\) to \(\mathbb Z\xrightarrow{2}\mathbb Z\), with the source in degree one.

**4. Tensor and homology.** For every other cycle, the ordinary cellular complex splits integrally into contractible pairs and one rank-one group in degree zero and one in degree one, both with zero differentials. Consequently the signed product chain model is homotopy equivalent to a direct sum of \(\binom{r-1}{q}\) copies of \((\mathbb Z\xrightarrow{2}\mathbb Z)[q]\) for each \(0\le q\le r-1\). Each such summand has its only homology \(\mathbb Z/2\mathbb Z\) in degree \(q\). This proves the theorem, including the absence of other degrees and of odd-primary torsion. Tensoring with \(\mathbb R\) makes multiplication by two invertible, so all real signed homology vanishes. The unsigned cover instead has tensor products of ordinary cycle chain models and therefore free rank \(\binom rq\) in degree \(q\).

## Verification

The bundled standalone `verify_signed_toroidal.py` constructs the integral signed incidence matrix from deck-anti-invariant edge and vertex bases and computes its exact integer Smith normal form for first-cycle lengths \(5,6,8\). It constructs the reduced cubical tensor differential over \(\mathbb Z\) for \(r=2,\ldots,6\), checks \(\partial^2=0\) and all nonunit invariant factors, and independently enumerates allowed regular paths in bidirected cycles of lengths ten and twelve up to degree six to calculate the precise dimensions of the corresponding \(\partial\)-invariant chain groups over \(\mathbb F_2\). The expected torsion-rank rows are respectively \((1,1)\), \((1,2,1)\), \((1,3,3,1)\), \((1,4,6,4,1)\), and \((1,5,10,10,5,1)\). Run `python3 verify_signed_toroidal.py` with Python 3 and SymPy installed; exact output is in `verification.log`.

The finite computations check the reduced integer model and local path combinatorics. They do not replace the universal proof, whose nonstandard steps are the translation-equivariant integral cycle contraction and the integral natural path-product chain isomorphism.

## Relationship to prior work

Fu and Yau (first public March 10, 2026) established a much more general integral/PID path-chain shuffle and equivariant construction for marked simplicial sets. Their product theorem is used as an essential tool; it does not explicitly calculate integral *anti-invariant-chain* homology of a negatively wound Cartesian toroidal graph. Bai, Li and Yau (first public September 22, 2026) introduced signed GLMY via double covers over real coefficients and identified signed real homology with the real anti-invariant cover homology. The present integer groups are not determined by that real calculation. Classical graph path-product Künneth methods go back to Grigor'yan–Muranov–Yau (2017).

An existing integral signed-GLMY result computes \(\mathbb Z/2\mathbb Z\) in degree zero for connected unbalanced graphs and the first homology for graphs without triangles or quadrilaterals. Its degree-zero statement agrees with the theorem's first row; the toroidal products contain quadrilaterals and it does not determine their positive-degree torsion. Existing signed-cactus path-homology classifications use real coefficients and their underlying graphs have edge-disjoint cycles, not toroidal square complexes. The contribution here is the simultaneous **exact integral higher-degree classification for every toroidal dimension**, rather than the already known degree-zero obstruction, an unspecified Künneth decomposition, or a standard rational Betti count.

## Limitations

Only the coordinate-seam negative signing, bidirected factor cycles of lengths at least five, and the anti-invariant *integral chain* refinement are classified. No statement is made about arbitrary sign patterns with negatively signed elementary squares, about twisted local systems on graph products without a Cartesian cover, or about Borel-equivariant path homology. The covering-complex homology and the anti-invariant subgroup of its homology are **not** the same as the homology computed here. The exact local-coefficient computation is related to classical sign-twisted torus cellular homology, so specialist priority comparison with equivalent formulations remains warranted. No independent mathematical audit has been performed.

## References

1. Xin Fu and Shing-Tung Yau, *Szczarba's twisted shuffle and equivariant path homology of directed graphs*, arXiv:2603.09406, first posted March 10, 2026. In particular Theorem 2.7 on product chain isomorphisms over a PID. https://arxiv.org/abs/2603.09406
2. Shuliang Bai, Jingyan Li and Shing-Tung Yau, *Signed GLMY Homology of Signed Graphs via Double Covers*, arXiv:2609.25557, first posted September 22, 2026, §§3–4. https://arxiv.org/abs/2609.25557
3. Alexander Grigor'yan, Yuri Muranov and Shing-Tung Yau, *Homologies of digraphs and Künneth formulas*, Communications in Analysis and Geometry 25 (2017), Theorem 4.7. https://doi.org/10.4310/CAG.2017.v25.n5.a4
4. Alexander Grigor'yan, Yong Lin, Yuri Muranov and Shing-Tung Yau, *Path complexes and their homologies*, Journal of Mathematical Sciences 248 (2020). https://doi.org/10.1007/s10958-020-04897-9
