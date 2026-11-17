# The complete \(200\)-symmetry character of the five-by-five torus Rips four-spheres

## Finding
Let \(A=(\mathbb Z/5\mathbb Z)^2\), equipped with the shortest-path product metric of \(C_5\square C_5\), and let \(X=\operatorname{VR}_{\le3}(A)\) use the **inclusive** pairwise-distance convention. The group
\[
G=(D_5\times D_5)\rtimes C_2,\qquad |G|=200,
\]
acts on \(X\) by the affine maps
\[
(x,y)\longmapsto(sx+a,ty+b),\quad
(x,y)\longmapsto(sy+a,tx+b),
\qquad s,t\in\{\pm1\},\ a,b\in\mathbb Z/5\mathbb Z.
\]
In the additive translation subgroup \(A\), put \(L_+=\langle(1,2)\rangle\) and \(L_-=\langle(1,-2)\rangle\). Each of the five-point coset sets \(A/L_+\) and \(A/L_-\) is permuted by \(G\), with the **two sets allowed to be interchanged**. Define the rational \(G\)-module
\[
W=\ker\big(\mathbb Q[A/L_+]\xrightarrow{\operatorname{sum}}\mathbb Q\big)
\oplus\ker\big(\mathbb Q[A/L_-]\xrightarrow{\operatorname{sum}}\mathbb Q\big).
\]
Write \(\varepsilon_{\rm swap}\) for the one-dimensional character equal to \(-1\) precisely when the two cyclic coordinates are interchanged, regardless of subsequent signs or translations. Then
\[
\boxed{\widetilde H_4(X;\mathbb Q)\cong\varepsilon_{\rm swap}\oplus W,}
\qquad X\simeq\bigvee^9 S^4,
\]
and every other reduced integral homology group vanishes. The nonequivariant homotopy equivalence and the translation-only rational module are prior results, recalled here solely to specify the new extension.

The full character \(\chi_4(g)=\operatorname{tr}(g\mid\widetilde H_4(X;\mathbb Q))\) has the following complete description:

| Element type | Number of elements | Character |
|---|---:|---:|
| Identity | 1 | \(9\) |
| Nonzero translation in \(L_+\cup L_-\) | 8 | \(4\) |
| All remaining nonzero translations | 16 | \(-1\) |
| Nonswapping maps with a coordinate reflection | 75 | \(1\) |
| All swapping maps | 100 | \(-1\) |

In particular the invariant subspace for all \(200\) symmetries is zero, despite the one-dimensional translation-invariant subspace. Since rational homology of a finite-group orbit space is the invariant rational homology, the quotient has no positive-degree rational homology:
\[
\boxed{\widetilde H_i(X/G;\mathbb Q)=0\quad(i\ge1).}
\]

## Assumptions and scope
All coordinates are in \(\mathbb Z/5\mathbb Z\) and the cyclic distance between two coordinate values is the smaller of their two path distances around \(C_5\). A simplex in \(X\) is any finite set with all pairwise distances at most three. The group \(G\) is the factor-preserving-or-interchanging coordinate-dihedral group explicitly displayed above. The theorem does not rely on an assertion that this is the complete abstract automorphism group of \(X\).

For a line \(L\le A\), a coset \(v+L\) is acted on by \(g\) through \(g(v)+g_{\rm lin}(L)\). The two special lines form a \(G\)-stable pair, since their slopes are \(2\) and \(-2\) in the field of five elements; independent coordinate signs and factor interchanges either preserve or exchange those lines. Consequently \(W\) is well-defined without choosing any noncanonical isomorphism between its two summands. The summand \(\varepsilon_{\rm swap}\) is not the sign of the permutation of the 25 graph vertices.

## Proof
**1. An exact independence-complex model.** The maximum distance in the product of two pentagons is four. Two distinct vertices are not joined by an edge of the radius-three Rips complex exactly when their coordinate differences both have cyclic length two, i.e. both differences are \(\pm2\) modulo five. The graph \(F\) of these forbidden pairs has degree four. Multiplying coordinates by three modulo five identifies \(F\) with the categorical graph product \(C_5\times C_5\): each forbidden difference \((\pm2,\pm2)\) becomes \((\pm1,\pm1)\). Thus \(X\) is exactly the independence complex of \(F\), not an approximation or an Alexander dual.

**2. The underlying integral homotopy type.** The cited primary article proves \(X\simeq\bigvee^9S^4\). For an independent exact certificate, `verify.py` constructs **all** 25,531 faces of the independence complex, counting the empty face. Face numbers in dimensions \(-1\) through nine are
\[
(1,25,250,1300,3850,6745,7100,4450,1550,250,10).
\]
It applies vertex-toggle Morse matching in the fixed priority order
`5,12,18,6,3,14,24,2,15,11,1,9,0,22,16,20,17,23,7,4,8,10,13,19,21`.
The resulting 12,761 pairs and nine unmatched faces (each with five vertices) cover the augmented face poset. For every one of 142,050 codimension-one covering relations, reverse precisely the matched arrows and perform an exhaustive directed-graph topological sort. All 25,531 vertices are removed, establishing acyclicity with no sampling. Unmatching the empty-face-to-vertex pair leaves one critical zero-cell and nine critical four-cells and nothing else. Forman's theorem therefore gives a point with nine four-cells attached trivially, proving the displayed wedge and torsion-freeness over \(\mathbb Z\).

**3. An exact finite character formula.** Fix one of the 200 affine group elements \(g\). Its permutation of the 25 vertices splits into disjoint cycles \(O_1,\dots,O_r\). A face fixed setwise by \(g\) must be a union of such complete cycles. Discard a cycle if it contains a forbidden pair, and on the remaining admissible cycles put an edge wherever the union of two cycles contains a forbidden pair. Let \(B_g\) be this finite conflict graph, and write its independence polynomial as \(I(B_g;t)=\sum_{J\text{ independent}}t^{|J|}\). The signed trace on the augmented simplicial chains satisfies the exact identity
\[
\widetilde L(g;X)= -I(B_g;-1).
\]
Indeed a set of \(r\) selected cycles contributes a simplex of dimension \(\sum|O_i|-1\), whose vertex-permutation orientation sign is \((-1)^{\sum(|O_i|-1)}\), so its signed simplicial trace is \((-1)^{r-1}\); the empty selected set contributes \(-1\) in the augmented convention. Since only reduced homology in even degree four survives, \(\widetilde L(g;X)=\chi_4(g)\). This reduces the character of **every** element to finite, exactly specified graph enumeration rather than assuming a previously known trace.

The recurrence \(I(B;-1)=I(B-v;-1)-I(B-N[v];-1)\), evaluated by integer bit masks, computes each trace. `verify.py` applies it to all affine maps displayed in the theorem and asserts the five classes of results in the character table. The 200 independently indexed elements are exhausted because there are \(2\cdot2\cdot2\cdot5\cdot5=200\) distinct maps. No probabilistic step or cutoff is used.

**4. Recognition of the rational representation.** The quotient-coordinate on \(A/L_s\), \(s\in\{2,3\}\), can be taken as \(q=y-sx\pmod5\). For any affine map preserving \(L_s\), the induced coset map has the form \(q\mapsto cq+e\). Its augmentation-kernel trace is exactly \(\#\operatorname{Fix}(q\mapsto cq+e)-1\). If a map exchanges \(L_+\) and \(L_-\), it has trace zero on their direct-sum augmentation module. Adding \(+1\) or \(-1\) according to whether the coordinate factors are preserved or swapped yields the candidate representation's trace. The standalone verifier evaluates these coset-action traces independently of the simplicial chain traces for all 200 group elements and asserts equality at every element, not merely agreement of their character histograms. Rational characters determine rational representations of finite groups by semisimplicity, proving the claimed isomorphism.

**5. Quotient.** The sum of the 200 character values is \(9+8\cdot4+75\cdot1-116=0\). By character averaging, the rational dimension of the full invariant fourth homology is zero. The only possible positive-degree rational homology of \(X\) is in degree four. For a finite simplicial group action, rational simplicial chains of a barycentric subdivision descend to the orbit cellular chain complex, and averaging is exact in characteristic zero. Therefore the positive-degree rational homology of \(X/G\) is the invariant part of that of \(X\), hence vanishes. This does not determine quotient integral torsion or its homotopy type.

## Verification
`verify.py` is a complete Python 3.9+ deterministic certificate relying only on the standard library. Running `python3 verify.py` must return `PASS` after confirming the exact 25,531-face enumeration, the nine critical four-cells, an acyclic matching on all 142,050 Hasse covers and **elementwise** equality between signed chain Lefschetz traces and independently calculated coset-module traces for every one of the 200 affine symmetries. `verification_output.txt` contains the exact observed replay. The fixed five-by-five case is exhaustively covered. No experiment for other grid dimensions is interpreted as a proof.

## Relationship to prior work
Adams, Adetowubo, Barriga-Acosta, Feng and Sterling, *Vietoris–Rips complexes of torus grids*, first public 10 February 2025, Theorem 7.1, proves the nine-four-sphere nonequivariant homotopy equivalence and explicitly identifies the five-by-five, scale-three case. It notes possible usefulness of equivariant questions but does not calculate the 200-element group character.

The published **translation-only** classification *Translation-fixed spaces of the \(5\times5\) torus-grid Rips complex at scale \(3\)* computes the same nine-dimensional representation restricted to \(A\), namely \(\mathbb Q\oplus V_2\oplus V_3\). That restriction cannot decide whether coordinate interchange negates or preserves the one-dimensional translation-fixed class, nor can it determine reflection actions. The present extension supplies the extra 175 nontranslation character values, the signed line, and disappearance of the translation-fixed class on taking the full symmetry quotient. This distinction is a statement-level comparison, not a novelty inference from differing paper titles.

*Nine integral four-spheres in the fully periodic five-by-five hard-square complex* computes the independence complex of the **square-grid adjacency** graph \(C_5\square C_5\), not of the forbidden-pair graph \(C_5\times C_5\) used in the present exact Rips model. In particular it does not supply the present equivariant character. We do not claim novelty for the nine-four-sphere homotopy type, the translation restriction, or classical fixed-point and character theorems.

## Limitations
The new result is a rational representation classification for the displayed order-200 action, not an integral \(\mathbb Z[G]\)-lattice identification or full equivariant homotopy equivalence. Quotient rational homology need not detect integral torsion or its fundamental group. The complete 25-vertex case has an exhaustive finite certificate, but there is no uniform theorem for larger grids. An equivalent unindexed preprint or differently expressed full symmetry calculation remains a bibliographic priority risk. No independent mathematical validation is represented by this package.

## References
1. H. Adams, A. Y. Adetowubo, H. Barriga-Acosta, Z. Feng, J. Sterling, *Vietoris–Rips complexes of torus grids*, arXiv:2502.07134 (first public 2025-02-10), Theorem 7.1 and §§7–8. https://arxiv.org/html/2502.07134v2
2. *Translation-fixed spaces of the five-by-five torus-grid Rips complex at scale three*, RESULT.md, 2026-11-08. https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-translation-fixed-spaces-of-the-5-times5-torus-grid-rips-complex--84079f5fd0c0
3. *Nine integral four-spheres in the fully periodic five-by-five hard-square complex*, RESULT.md, 2026-10-25. https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-nine-integral-four-spheres-in-the-fully-periodic-five-by-five-ha--374b6b4d37f7
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145.
