# Forty circles and ninety-six three-spheres in an asymmetric Hamming box

## Finding

Let \(T=\{0,1,2\}\times\{0,1,2\}\times\{0,1,2,3\}\) with the Hamming metric \(d(x,y)=|\{j:x_j\ne y_j\}|\). For each real \(r\geq0\), let \(R_r=\operatorname{VR}_{\leq r}(T)\) be the inclusive Vietoris–Rips simplicial complex: a finite subset is a face precisely when every two of its points have distance at most \(r\). Then

\[
|R_r|\simeq
\begin{cases}
\bigsqcup^{36}\{*\},&0\le r<1,\\
\bigvee^{40}S^1,&1\le r<2,\\
\bigvee^{96}S^3,&2\le r<3,\\
\{*\},&r\ge3.
\end{cases}
\]

Consequently, the entire reduced **integral** persistent homology consists of \(35\) intervals \([0,1)\) in degree zero, \(40\) intervals \([1,2)\) in degree one, and \(96\) intervals \([2,3)\) in degree three; there are no other reduced intervals or torsion. In unreduced degree zero, one additional component persists forever. At the decisive middle scale,

\[
R_2=\operatorname{Ind}(K_3\times K_3\times K_4)\simeq\bigvee^{96}S^3,
\]

where \(\times\) denotes the categorical (tensor/direct) graph product, not the Cartesian product. This is an asymmetric all-factors-at-least-three instance of the three-complete-factor problem of Antolín Camarena–Carnero Bravo.

## Assumptions and scope

All points are discrete; edges of the associated Hamming graph are not replaced with continuous line segments. The metric is unit Hamming distance, not Euclidean distance. Parameters \(r\) are real and scale boundaries are inclusive on the right-hand complexes. Vertices are lexicographically ordered with integer label \(12a+4b+c\), \(0\le a,b\le2\), \(0\le c\le3\). A nonempty simplex is encoded as the bitmask of its vertices. Homotopy refers to geometric realization, and the equivalences need not be equivariant. Reduced persistence is taken over \(\mathbb Z\); its interval description is justified by the filtration having nonzero reduced homology in disjoint degree/scale regimes.

## Proof

**Scale zero and scale one.** Distinct points have integral distance at least one. For \(1\le r<2\), every nondegenerate clique lies on a unique coordinate line, since if distinct \(x,y\) differ in one coordinate, a third point adjacent to both must agree with the other coordinates. There are \(12\) coordinate lines of three vertices in the first direction, another \(12\) of three in the second, and \(9\) lines of four in the third. Distinct coordinate-line simplices intersect only in vertices. Collapse each line simplex to a spanning tree using ordinary elementary collapses that retain its vertices. The resulting complex is connected with \(36\) vertices and \(12\cdot2+12\cdot2+9\cdot3=75\) edges, so it is a wedge of \(75-36+1=40\) circles.

**Scale two and categorical product.** Distinct triples have distance three if and only if they differ in all three coordinates. These forbidden pairs are exactly the edges of \(K_3\times K_3\times K_4\). Thus a set has diameter at most two exactly when it is an independent set of this product graph, yielding the asserted *simplicial equality*.

**A complete discrete-Morse proof.** Construct the face set without stored tables by recursively extending each clique only with larger vertex labels adjacent to its existing vertices. This independently produces exactly \(30{,}991\) nonempty faces, with dimension-ordered face vector

\[
(36,414,2028,4869,6804,6816,5184,3042,1324,396,72,6).
\]

Apply the following deterministic matching to the nonempty face poset. Initially every face is unmatched. For each label \(i=0,\ldots,35\) in ascending order, consider every still-unmatched face \(\sigma\) without \(i\). When both \(\sigma\) and \(\sigma\cup\{i\}\) remain unmatched faces, pair them and mark both as used. The pairs are face-poset covers. The full exact enumeration yields \(15{,}447\) pairs and only \(97\) critical faces: one vertex and \(96\) tetrahedra. These are **all** the critical dimensions.

Acyclicity is verified by the standalone finite certificate `morse_certificate.json` and checker `verify_morse.py`: orient every codimension-one face incidence downward except for each matched pair, whose incidence is reversed. The checker reconstructs all \(178{,}668\) oriented incidences from the metric and matching, verifies all pair endpoints and the critical inventory, and verifies that the certificate's \(30{,}991\)-element permutation of faces is a strict topological ordering of **every** oriented edge. Thus the entire oriented Hasse diagram is acyclic. This is an exhaustive, finite proof of the matching's acyclicity, not a sampled experiment. Forman's discrete-Morse theorem gives a CW complex with exactly one \(0\)-cell, exactly \(96\) \(3\)-cells, and no other cells. All \(3\)-cell attaching maps are constant because there are no \(1\)- or \(2\)-cells. The CW complex is therefore a wedge of \(96\) three-spheres, over the integers.

**Independent collapse/chain proof.** Separately, the standard-library checker `verify.py` constructs all \(154\) maximal simplices by an independently coded maximal-clique method and verifies \(14{,}227\) sequential *elementary simplicial* collapses, leaving face vector \((36,387,1185,929)\) in dimensions zero through three. It checks a spanning tree on \(36\) vertices and \(352\) explicit triangle relations, each eliminating one remaining fundamental-group edge generator. Hence the residual two-skeleton has trivial fundamental group. Its integral degree-three boundary matrix reduces by \(833\) unit-pivot integer column eliminations, with each pivot \(\pm1\). A separate mod-two rank calculation also returns \(833\). Thus the remaining integral homology is free in degree three of rank \(929-833=96\), and degree two vanishes because \(1185-387+36-1=833\). This second proof corroborates the first and supplies an independent explicit collapse route; the acyclic matching alone already determines the integral homotopy type.

**Scale three and the barcode.** Every distance between two elements of \(T\) is at most three. For \(r\ge3\), the complex is the full \(35\)-simplex and is contractible. As all distances are integers, the displayed four homotopy regimes exhaust the filtration. The positive-degree homology groups in different regimes have different degrees, so the intervening maps are zero, giving exactly the stated integral intervals.

## Verification

All supporting files use Python 3's standard library only. Run `python3 verify_morse.py verify morse_certificate.json` for the complete face-poset acyclicity certificate and `python3 verify.py verify certificate.json` for the separate elementary-collapse and integral-boundary certificate. The files `morse_verification_output.txt` and `verification_output.txt` record the respective expected successful outputs; each executable reconstructs the original 36-point Hamming metric and relevant complexes rather than loading a precomputed face set. The first checker verifies all \(30{,}991\) faces, \(15{,}447\) pairs and \(178{,}668\) directed Hasse incidences. The second checks all \(14{,}227\) collapse pairs, \(352\) triangle nullhomotopies and \(833\) unit integral pivots. These are exact finite certificates; no finite enumeration is used to infer an infinite-parameter claim.

## Relationship to prior work

Goyal–Shukla–Singh (2019) study two-factor categorical products and provide a discrete-Morse vertex-toggling method. Antolín Camarena–Carnero Bravo (2023), especially their Conjecture 26 and proved factor-two cases, formulate the all-three-factor complete-graph problem, without proving the three-factor case where all sizes exceed two. Carnero Bravo (2025) studies independence complexes of several graph-product families, providing recent context, but the inspected primary sections do not give the present three-complete-factor calculation. The previously published exact ternary-three-cube calculation treats \(K_3\times K_3\times K_3\), whose 27-point Rips complex has \(46\) three-spheres at scale two; this does not imply the distinct 36-point \((3,3,4)\) case. The *matching method* is not claimed to be new: the new result is its exhaustively certified outcome for the next natural unequal three-factor instance, together with the full integral Hamming-metric barcode. No general three-factor formula is claimed.

## Limitations

This theorem concerns exactly the product of alphabet sizes \((3,3,4)\) with inclusive discrete Hamming distance. It does not prove the unrestricted three-factor conjecture, describe larger alphabet sizes, determine equivariant representations or prove that the homotopy equivalences are compatible with additional structures. The finite proof requires trust in elementary Python execution and integer arithmetic and has not received an independent mathematical audit. Undiscovered equivalent literature or computations remain a possible originality risk.

## References

1. S. Goyal, S. Shukla, and A. Singh, *Homotopy Type of Independence Complexes of Certain Families of Graphs*, arXiv:1905.06926 (first posted 2019-05-16), https://arxiv.org/abs/1905.06926.
2. O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401 (first posted 2023-07-23), especially Conjecture 26, https://arxiv.org/abs/2307.12401.
3. A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457 (first posted 2025-05-09), https://arxiv.org/abs/2505.06457.
4. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
5. *Complete Vietoris–Rips persistence of the ternary three-cube* (2026), publicly indexed mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-complete-vietoris-rips-persistence-of-the-ternary-three-cube--62d7487289d8.
