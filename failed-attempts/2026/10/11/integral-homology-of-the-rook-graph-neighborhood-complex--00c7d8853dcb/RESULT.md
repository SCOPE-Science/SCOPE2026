# Integral homology of the rook-graph neighborhood complex
## Finding
For the Hamming graph
\[
R=H(2,4)=K_4\square K_4=L(K_{4,4}),
\]
the Lovász neighborhood complex \(\mathcal N(R)\) admits an acyclic discrete-Morse matching with exactly one critical \(0\)-cell, one critical \(1\)-cell, and \(56\) critical \(2\)-cells. Its integral homology is
\[
H_i(\mathcal N(R);\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,\\
\mathbb Z/2\mathbb Z,&i=1,\\
\mathbb Z^{55},&i=2,\\
0,&i\ge 3.
\end{cases}
\]
Consequently \(\mathcal N(R)\) is not homotopy equivalent to a wedge of spheres.

## Assumptions and scope
The graph \(R\) has vertex set \(\{0,1,2,3\}^2\). Distinct vertices are adjacent exactly when they agree in one coordinate, equivalently when they differ in exactly one coordinate. Thus \(R\) is the \(4\)-by-\(4\) rook graph, the Hamming graph \(H(2,4)\), the Cartesian product \(K_4\square K_4\), and the line graph \(L(K_{4,4})\).

The neighborhood complex \(\mathcal N(R)\) consists of all nonempty sets of vertices having a common neighbor in \(R\). The claim concerns ordinary open neighborhoods. It does not concern the closed-neighborhood complex, a clique complex, or a Rips complex.

Exhaustive generation gives \(808\) nonempty faces and face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(16,120,320,240,96,16).
\]

## Proof
Index the sixteen vertices row-major by \(0,\ldots,15\). The verifier reconstructs \(R\) directly from the coordinate rule and generates every nonempty face of \(\mathcal N(R)\) as a nonempty subset of one of the sixteen open neighborhoods.

Apply the stagewise element matching with vertex order
\[
(9,1,6,13,11,3,5,8,7,14,0,12,10,15,2,4).
\]
At the stage for a vertex \(v\), every still-unmatched face \(\sigma\) not containing \(v\) is paired with \(\sigma\cup\{v\}\) whenever both faces are still unmatched. The resulting matching has \(375\) pairs and leaves exactly \(58\) critical faces: one of dimension \(0\), one of dimension \(1\), and \(56\) of dimension \(2\). The verifier orients every one of the \(2736\) nonempty Hasse covers in the Forman orientation and topologically sorts the entire directed graph; all \(808\) faces are visited. Hence the matching is acyclic, and discrete Morse theory gives a homotopy-equivalent CW complex with cells only in dimensions \(0,1,2\) and Morse vector
\[
(1,1,56).
\]

It remains to determine the integral attaching data. The \(1\)-skeleton of \(\mathcal N(R)\) is \(K_{16}\), so its integral cycle lattice has rank \(120-16+1=105\). Choose the star at vertex \(0\) as a spanning tree. For \(1\le i<j\le15\), let
\[
z_{ij}=e_{0i}+e_{ij}-e_{0j}.
\]
These \(105\) cycles form an integral basis. Express the boundaries of all \(320\) triangles in this basis, obtaining an integer \(105\times320\) relation matrix \(B\).

The verifier gives three exact determinantal facts. First, a displayed \(104\times104\) minor of \(B\) has determinant \(1\). Second, a displayed \(105\times105\) minor has determinant \(-2\). Third, reduction modulo \(2\) has rank \(104\), so every \(105\times105\) minor is even. Therefore the first \(104\) Smith factors of \(B\) equal \(1\), while the last equals \(2\). Thus
\[
\operatorname{coker} B\cong\mathbb Z/2\mathbb Z.
\]
Because the \(z_{ij}\) form the complete integral cycle lattice and triangle boundaries generate \(\operatorname{im}\partial_2\), this cokernel is exactly \(H_1(\mathcal N(R);\mathbb Z)\).

The Morse model has no cells above dimension \(2\), so \(H_i=0\) for \(i\ge3\). Its Euler characteristic is
\[
16-120+320-240+96-16=56.
\]
Since \(H_1\) has rank \(0\), Euler characteristic gives \(\operatorname{rank}H_2=55\). As \(H_2\) is a subgroup of a free cellular chain group, it is free. Hence \(H_2\cong\mathbb Z^{55}\).

## Verification
Run `verify.py` with the Python standard library. It independently reconstructs the graph, all faces, the full staged matching, and the complete Forman-oriented Hasse diagram. It then rebuilds the triangle-relation matrix from the graph definition.

The verifier checks
\[
\operatorname{rank}_{\mathbb F_2}B=104,\qquad
\operatorname{rank}_{\mathbb F_3}B=
\operatorname{rank}_{\mathbb F_5}B=105,
\]
and evaluates the two archived determinant witnesses by fraction-free Bareiss elimination. The output terminates with `VERIFY_OK`.

## Relationship to prior work
Shukla's 2018 neighborhood-complex paper studies the same functor and proves homotopy classifications for graphs of maximum degree at most \(3\) and for \(4\)-regular circulant graphs. The graph \(R\) is \(6\)-regular, so those classification theorems do not cover it. Matsushita's work describes fundamental groups of neighborhood complexes through graph-theoretic fundamental groups, but the inspected statement does not give the present finite calculation or its integral homology.

Searches under the equivalent names `H(2,4)`, `rook graph`, `lattice graph`, `K4 Cartesian K4`, and `line graph K4,4`, together with neighborhood-complex and Lovász/Hom terminology, did not locate an equivalent statement or a stronger result implying the displayed Smith data. The closest indexed neighborhood-complex computation found was for a different canonical graph, the icosahedral graph.

## Limitations
The theorem is specific to \(H(2,4)\). It does not classify neighborhood complexes of general Hamming graphs, rook graphs, line graphs, or \(6\)-regular graphs. The discrete-Morse certificate proves the existence of a \(2\)-dimensional CW model, but the package does not identify the attaching maps up to homotopy beyond the integral homology consequences above. Originality remains subject to the ordinary residual risk of an obscure or unindexed computation under equivalent graph or box-complex terminology.

## References
1. Samir Shukla, *Homotopy Type of the Neighborhood Complexes of Graphs of Maximal Degree at most \(3\) and \(4\)-Regular Circulant Graphs*, arXiv:1802.04526, first posted 13 February 2018; *Electronic Journal of Combinatorics* 26(2) (2019), P2.4, DOI 10.37236/7549.
2. Takahiro Matsushita, *Fundamental Groups of Neighborhood Complexes*, *Journal of Mathematical Sciences, the University of Tokyo* 24 (2017), 321–353.
3. Robin Forman, *Morse Theory for Cell Complexes*, *Advances in Mathematics* 134 (1998), 90–145.
