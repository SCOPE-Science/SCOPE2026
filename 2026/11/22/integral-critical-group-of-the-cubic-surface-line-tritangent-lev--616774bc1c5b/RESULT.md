# Integral critical group of the cubic-surface line–tritangent Levi graph

## Finding

For any smooth complex cubic surface, let \(\Gamma\) be the bipartite incidence graph of its 27 geometric lines and 45 tritangent planes. Then

\[
K(\Gamma)\cong
(\mathbb Z/3\mathbb Z)^{10}\oplus
(\mathbb Z/9\mathbb Z)^5\oplus
(\mathbb Z/27\mathbb Z)^8\oplus
(\mathbb Z/135\mathbb Z)^6.
\]

The Smith form of a reduced graph Laplacian is \(\operatorname{diag}(1^{[42]},3^{[10]},9^{[5]},27^{[8]},135^{[6]})\); the graph has 72 vertices, 135 edges and cycle rank 64. It has exactly \(3^{62}5^6\) spanning trees and critical-group exponent 135.

## Assumptions and scope

The ground field is \(\mathbb C\). Every smooth cubic surface is a blowup of six points in general position in \(\mathbb P^2\). The vertices of \(\Gamma\) are *objects*, not their individual geometric intersection points. Its edges express that a geometric line is contained in a tritangent plane. The critical group is \(\operatorname{coker}(L_\Gamma)_{\mathrm{tors}}\) for the ordinary integer graph Laplacian \(L_\Gamma\); equivalently it is the cokernel of any reduced Laplacian (delete one row and the corresponding column). This graph is the point-line Levi graph of the classical generalized quadrangle \(\mathrm{GQ}(2,4)\).

## Proof

Write \(H,E_1,\ldots,E_6\) for the blowup divisor basis and \(-K_S=3H-\sum_{i=1}^6 E_i\). The 27 \((-1)\)-curve classes are
\[
E_i,\qquad L_{ij}=H-E_i-E_j\ (i<j),\qquad Q_i=2H-\sum_{k\ne i} E_k.
\]
The 45 tritangent triples are exactly the 30 \(\{E_i,L_{ij},Q_j}\) for ordered \(i\ne j\), and the fifteen triples \(\{L_{ab},L_{cd},L_{ef}}\) indexed by partitions of six labels into three pairs. Indeed each such triple sums to \(-K_S\), and any triple of distinct line classes summing to \(-K_S\) must have \(H\)-degrees \((0,1,2)\) or \((1,1,1)\); comparing exceptional coefficients gives precisely those cases. All pairs of meeting lines belong to precisely one tritangent plane. Therefore the \(27\times45\) zero-one incidence matrix \(N\) has five ones in each row and three in each column, and
\[
NN^{\mathsf T}=5I_{27}+A,
\]
where \(A\) is the meeting-line adjacency matrix. Its graph is the \(\mathrm{GQ}(2,4)\) point graph, strongly regular with parameters \((27,10,1,5)\), as is also verified directly from the 45 explicit triples. Hence \(A^2=5I-4A+5J\), and \(A\) has spectrum \(10^{[1]},1^{[20]},(-5)^{[6]}\).

The Laplacian is the block integer matrix
\[
L_\Gamma=\begin{pmatrix}5I_{27}&-N\\-N^{\mathsf T}&3I_{45}\end{pmatrix}.
\]
The nonzero singular values implied by \(NN^{\mathsf T}\) give the following exact Laplacian spectrum:
\[
0^{[1]},\;8^{[1]},\;(4+\sqrt 7)^{[20]},\;(4-\sqrt 7)^{[20]},\;5^{[6]},\;3^{[24]}.
\]
There is only one zero eigenvalue, so \(\Gamma\) is connected. The matrix-tree theorem gives
\[
\tau(\Gamma)=\frac{8\,(16-7)^{20}\,5^6\,3^{24}}{72}=3^{62}5^6.
\]

To recover the *integral* group rather than only its order, delete any one vertex and apply exact local Smith reduction to the resulting \(71\times71\) integer matrix. In \(\mathbb Z/3^{65}\mathbb Z\) the diagonal pivot valuations have multiplicities \(e_0=42,e_1=10,e_2=5,e_3=14\). In \(\mathbb Z/5^{10}\mathbb Z\) they are \(e_0=65,e_1=6\). Reduction modulo 2 shows all 71 pivots are units, and the tree count excludes all primes other than 3 and 5. Consequently the nonunit elementary divisors are ten 3s, five 9s, fourteen 27s, and six 5s; sorting the 3- and 5-parts into invariant-factor order combines the last six 27s with the six 5s, giving the displayed decomposition. This finishes the determination of \(K(\Gamma)\).

The calculation just used is an exact finite certificate, not a floating-point spectrum inference: `tritangent_levi_verify.py` constructs the entire matrix from divisor classes and performs unit-pivot integer congruence arithmetic, with each pivot chosen to have *minimum* prime valuation in the remaining submatrix. Row and column operations are invertible over the prime-power ring. Two choices of deleted vertex and two pivot tie-order conventions reproduce the same valuations. The specified moduli exceed all measured valuation bounds; the independent tree count forces completeness.

## Verification

Run `python3 tritangent_levi_verify.py` with Python 3.8 or newer. This standalone, standard-library script reconstructs 27 curve classes and all \(\binom{27}{3}\) candidate triples; checks exactly 45 anticanonical triples and the strongly regular parameters; builds the 72-vertex Laplacian; verifies its connectivity; then performs four independent local pivot calculations at each of the primes 3 and 5, plus corresponding checks at 2, agreeing with the spanning-tree order. Expected terminal line: `CUBIC_SURFACE_TRITANGENT_LEVI_CRITICAL_GROUP_VERIFIED_OK`.

## Relationship to prior work

The classical six-point blowup/tritangent incidence and its identification with \(\mathrm{GQ}(2,4)\) are not new. The published \(\mathrm{GQ}(2,4)\) study of Saniga and collaborators analyzes 27 points, 45 lines and Veldkamp geometry; it does not provide this graph critical-group decomposition in the inspected full text. Brouwer's account identifies the Schläfli graph, cubic-surface lines and its strongly regular parameters. His Smith-form discussion treats adjacency matrices of various graphs, not this reduced 72-vertex bipartite Laplacian in the sections inspected. Indexed investigations of the integral tritangent \(E_6\) weight presentation and toric trades analyze distinct integral objects; neither its rectangular incidence Smith form nor toric ideal generators determine the displayed reduced-Laplacian Smith form without an additional calculation. The contribution asserted here is *only* the full critical-group decomposition, not any of those classical configurations.

## Limitations

This is an invariant of one canonical, fixed finite incidence graph, not a new classification of cubic surfaces. A prior unindexed sandpile calculation for the isomorphic generalized-quadrangle Levi graph could anticipate the answer; historical priority is provisional. The group is the graph Jacobian and is **not** asserted to equal a Picard, Chow, Néron–Severi or Albanese invariant of the surface. The proof is fully exact but its local Smith certificate is computer-assisted, with reproducible source supplied. No independence or external certification is claimed.

## References

1. M. Saniga, R. M. Green, P. Lévay, P. Pracna and P. Vrana, *The Veldkamp Space of GQ(2,4)*, first public preprint 4 March 2009, arXiv:0903.0715, https://arxiv.org/abs/0903.0715 .
2. A. E. Brouwer, *Schläfli graph*, https://aeb.win.tue.nl/graphs/Schlaefli.html (section on the 27 lines and the 45 tritangent planes).
3. A. E. Brouwer and H. Van Maldeghem, *Strongly Regular Graphs*, 2021, https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf (sections 9.4 and 10.10).
4. *Integral tritangent presentation of the \(E_6\) weight lattice*, public indexed result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-integral-tritangent-presentation-of-the-e-6-weight-lattice--d458bb2de263 .
5. *The 540 indispensable quartic trades of the cubic-surface tritangent configuration*, public indexed result, https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-the-540-indispensable-quartic-trades-of-the-cubic-surface-tritan--511e3e06b7dc .
