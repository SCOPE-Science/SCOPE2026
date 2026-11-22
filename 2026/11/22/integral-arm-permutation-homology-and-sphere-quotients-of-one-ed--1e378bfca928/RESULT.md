# Integral arm-permutation homology and sphere quotients of one-edge hexagon books

## Finding
For each integer \(h\ge2\), define a simple graph \(B_h\) with two poles \(a,b\), the edge \(ab\), and \(h\) pairwise internally disjoint five-edge paths \(a-x_{i1}-x_{i2}-x_{i3}-x_{i4}-b\), for \(1\le i\le h\). Give its vertices unit-edge shortest-path distance. Let \(X_h=\operatorname{VR}_{\le2}(V(B_h))\) be the **inclusive vertex-metric** Vietoris–Rips complex, not the Rips complex of all points of the geometric metric graph.

The full graph automorphism group is \(G_h=\mathfrak S_h\times C_2\), acting by permuting the arms and interchanging the poles while reversing each arm. The following statements hold integrally, for every \(h\ge2\):

\[
X_h\simeq\bigvee^h S^2,\qquad
\widetilde H_2(X_h;\mathbb Z)\cong\mathbb Z[\{1,\ldots,h\}],
\]
where \(\mathfrak S_h\) permutes an **explicit integral sphere basis without signs** and the pole interchange \(C_2\) acts **trivially**. All other reduced integral homology vanishes.

More strongly, for **every subgroup** \(H\le G_h\), let \(o_H\) count the orbits of the image of \(H\) on the set of \(h\) arms. The *actual topological orbit space* satisfies
\[
\boxed{|X_h|/H\simeq\bigvee^{o_H}S^2.}
\]
In particular \(|X_h|/G_h\simeq S^2\); no Borel or homotopy quotient is intended. This is distinct from the known two-edge-spine six-cycle books, for which pole reversal acts with negative sign and the full orbit space is contractible.

## Assumptions and scope
Every edge of \(B_h\) is specified above. Distinct arm interiors have no common vertices or edges, and the common spine consists of **one** edge. The parameter \(h\) is any integer at least two, and the scale is exactly the inclusive threshold two for graph-vertex shortest-path distance. \(\Delta[S]\) denotes the full simplex on vertex set \(S\), and \(\mathbb Z[\{1,\ldots,h\}]\) is the free abelian permutation lattice on the arms. An empty wedge convention is not needed because every subgroup has at least one arm orbit.

## Proof
**1. Exact all-parameter clique decomposition.** For each arm let \(K_i\) be the induced scale-two Rips complex on the six vertices \(\{a,x_{i1},x_{i2},x_{i3},x_{i4},b\}\). Distances in that six-vertex subgraph agree with the distances in the whole book: all alternative routes through another arm have at least five edges except the edge \(ab\), already present. The only pairs of distance three in this six-cycle are \(\{a,x_{i3}\}\), \(\{x_{i1},x_{i4}\}\), and \(\{x_{i2},b\}\). Consequently
\[
K_i=\{a,x_{i3}\}^0*\{x_{i1},x_{i4}\}^0*\{x_{i2},b\}^0,
\]
where each superscript-zero pair is a discrete two-point set; this is the boundary of the three-dimensional cross-polytope, hence a simplicial two-sphere.

For distinct arms, the only pairs of interior vertices at distance at most two are \(x_{i1},x_{j1}\) (via \(a\)) and \(x_{i4},x_{j4}\) (via \(b\)). No clique crossing two different arms can mix the first and last positions or include an interior position two or three. Thus every cross-arm clique lies in one of two full simplices
\[
F=\Delta[\{a,b,x_{11},\ldots,x_{h1}\}],\qquad
R=\Delta[\{a,b,x_{14},\ldots,x_{h4}\}].
\]
Writing \(L=F\cup R\), this proves **equality of simplicial complexes**
\[
X_h=L\cup K_1\cup\cdots\cup K_h,
\qquad K_i\cap L=I_i=\Delta[\{a,b,x_{i1}\}]\cup\Delta[\{a,b,x_{i4}\}],
\]
and \(K_i\cap K_j=\Delta[\{a,b\}]\) when \(i\ne j\). Every simplex of \(L\) lies in a maximal simplex containing the edge \(ab\); each \(I_i\) likewise consists of two triangles sharing \(ab\). Thus \(|L|\) and each \(|I_i|\) are contractible by straight-line contraction to the midpoint \(p\) of \(ab\).

**2. Absolute homotopy and an integral basis.** Contracting the contractible CW subcomplex \(L\) gives a homotopy equivalence \(|X_h|\to|X_h|/|L|\). Because distinct local spheres meet only within \(L\), this quotient is **literally** the pointed wedge \(\bigvee_i|K_i|/|I_i|\). Each quotient \(K_i/I_i\simeq K_i\cong S^2\), as \(I_i\) is a contractible CW subcomplex. The resulting relative fundamental classes \([K_i,I_i]\) give an integral free basis of \(\widetilde H_2(X_h;\mathbb Z)\), and the remaining reduced homology vanishes.

**3. Full automorphism group and integral orientation.** Since \(h\ge2\), the only degree-\(h+1\) vertices are \(a,b\); all others have degree two. An automorphism freely permutes the \(h\) path components between these poles, and may independently exchange the poles, giving precisely \(\mathfrak S_h\times C_2\). Arm permutations carry the ordered pair differences
\[
(a-x_{i3}),\quad(x_{i1}-x_{i4}),\quad(x_{i2}-b)
\]
to the identically ordered differences in another arm, so preserve their join-orientation basis. Pole reversal sends the three differences respectively to \(-(x_{i2}-b)\), \(-(x_{i1}-x_{i4})\), and \(-(a-x_{i3})\). Its signed permutation determinant is \((-1)^3(-1)=+1\): there are three orientation reversals and one transposition of the three coordinate pairs. Hence pole reversal preserves each integral sphere class. This proves the stated integral \(G_h\)-module, not merely a rational character.

**4. Genuine subgroup orbit spaces.** Let \(H\le G_h\). The subspace \(|L|/H\) is contractible: the straight-line contraction toward the midpoint \(p\) of \(ab\) is well-defined on each maximal simplex of \(L\), and is equivariant for the arm permutations and pole reversal (both fix \(p\)). After an equivariant barycentric subdivision, \(|L|/H\subset|X_h|/H\) is a CW subcomplex; collapsing it is an ordinary homotopy equivalence. Quotienting the literal wedge \(|X_h|/|L|\) by \(H\) now gives one local summand per arm orbit. A stabilizer of an individual arm acts on its \(K_i\) either trivially or by the pole-reversal involution \(\tau\); the induced quotient is \((|K_i|/|I_i|)/\langle\tau\rangle\) in the latter case.

The signed coordinate permutation of \(\tau\) in Step 3 has eigenvalues \(1,-1,-1\), and is a genuine half-turn of the octahedral sphere \(|K_i|\cong S^2\). Its quotient is topologically \(S^2\), not a disk. Meanwhile \(|I_i|/\langle\tau\rangle\) contracts to \(p\), since the two triangles are interchanged and both contain \(ab\). By the CW contractible-subcomplex quotient lemma, \((|K_i|/|I_i|)/\langle\tau\rangle\simeq S^2\). The trivial stabilizer has the same result. Each arm orbit therefore contributes exactly one sphere to \(|X_h|/H\), proving the formula. \(\square\)

## Verification
The dependency-free Python program `verify.py` constructs all exact graph shortest-path distances, enumerates all Rips simplices, and checks that they equal the explicit union of \(h\) octahedral boundaries with the two full simplices for \(2\le h\le6\). Exhaustive mod-two boundary ranks return only \(\widetilde\beta_2=h\). Independently computed signed simplicial Lefschetz traces for pole reversal and a transposition of two arms are respectively \(h\) and \(h-2\), as required by the claimed integral permutation module. The verifier is finite corroboration only; the uniform claims follow from Steps 1–4, including the quotient proof, not from extrapolation. Run `python3 verify.py` in the package directory and compare `verification_output.txt`.

## Relationship to prior work
Adamaszek, Adams, Gasparovic and collaborators, *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings* (arXiv:1712.06224, first public 18 December 2017), Theorems 3.13 and 3.15, cover certain metric graph gluings along a sufficiently short shared path. Their short-path condition \(1<6/3\) applies to the one-edge spine and can already yield the **nonequivariant** wedge of \(h\) spheres. Thus neither that homotopy type alone nor its sphere count is claimed as new here. Their results do not state the full **integral automorphism module** or **every genuine subgroup orbit-space type**.

The public result *Two-edge hexagon books: signed sphere modules and a contractible symmetry quotient* (17 November 2026, full RESULT.md inspected) treats the same six-cycle length but a different two-edge common spine: pole reversal acts by minus the identity and the full geometric quotient is contractible. Its local octahedral orientation and cone-intersection geometry differ, and its statement does not imply the one-edge subgroup quotient classification. The public *A hexagon-packing classification of scale-two graph Rips complexes* (11 October 2026, full RESULT.md inspected) requires any two six-cycles to share no graph edges; that hypothesis fails for every pair here. The graph-line-complex hexagon classification concerns \(\operatorname{VR}(L(G))\), not \(\operatorname{VR}(G)\). No exact covering statement was found in the queried literature and published-result index; this does not prove absolute bibliographic novelty.

## Limitations
The result concerns only scale two on the **vertex set** and does not classify later Rips stages or the continuum of points along edges. It classifies ordinary geometric orbit spaces and the integral homology module, not Borel quotients, full equivariant homotopy groups or subgroup fixed-point spaces. The new content is the unsigned integral symmetry action and all subgroup quotients; the nonequivariant sphere-wedge classification is covered by older metric-gluing techniques. An equivalent unpublished or unindexed equivariant statement may exist. Independent external verification has not been performed.

## References
1. M. Adamaszek, H. Adams, E. Gasparovic, M. Gommel, E. Purvine, R. Sazdanovic, B. Wang, Y. Wang, and L. Ziegelmeier, *On Homotopy Types of Vietoris–Rips Complexes of Metric Gluings*, arXiv:1712.06224, first publicly submitted 18 December 2017; Theorems 3.13 and 3.15. https://arxiv.org/html/1712.06224v5
2. *Two-edge hexagon books: signed sphere modules and a contractible symmetry quotient*, public mathematical finding dated 17 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-two-edge-hexagon-books-signed-sphere-modules-and-a-contractible--d9bd0f937f84
3. *A hexagon-packing classification of scale-two graph Rips complexes*, public mathematical finding dated 11 October 2026. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-hexagon-packing-classification-of-scale-two-graph-rips-complex--70b9bc9b3abb
4. *Hexagon two-cell model for scale-two Rips complexes of line graphs of high-girth graphs*, public mathematical finding dated 8 November 2026. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-hexagon-two-cell-model-for-scale-two-rips-complexes-of-line-grap--d6e392803a48
