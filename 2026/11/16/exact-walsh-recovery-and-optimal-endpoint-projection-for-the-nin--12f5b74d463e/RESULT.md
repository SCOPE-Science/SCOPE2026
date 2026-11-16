# Exact Walsh recovery and optimal endpoint projection for the nine-vertex square grid

## Finding
Let \(G=P_3\square P_3\) be the free-boundary \(3\times3\) square grid, with nine labelled vertices and twelve labelled edges. In \(H=(\mathbb Z/2\mathbb Z)^{E(G)}\), let \(f\) indicate the edge-incidence vectors of the spanning trees, and let
\[
W(s)=\sum_{T\text{ spanning tree of }G}(-1)^{|T\cap s|},\qquad s\in H.
\]
The number of trees is \(192\). The complete distribution of \(|W(s)|\) is as follows:

| Absolute Walsh multiplier | Number of frequencies |
| ---: | ---: |
| 0 | 1186 |
| 4 | 1536 |
| 8 | 496 |
| 12 | 320 |
| 16 | 176 |
| 20 | 64 |
| 24 | 48 |
| 28 | 64 |
| 32 | 68 |
| 36 | 64 |
| 40 | 16 |
| 64 | 24 |
| 72 | 16 |
| 80 | 16 |
| 192 | 2 |

Consequently unnormalized counting convolution \(T_f:u\mapsto f*u\) on \(\ell^2(H)\) has rank \(2910\), nullity \(1186\), least positive singular value \(4\), greatest singular value \(192\), positive-spectrum condition number \(48\), and Moore–Penrose inverse operator norm \(1/4\).

Let \(\mathcal R=\operatorname{ran}T_f\). The orthogonal Fourier projection \(P\) onto \(\mathcal R\) has sharp endpoint norms
\[
\|P\|_{\ell^1\to\ell^1}=\|P\|_{\ell^\infty\to\ell^\infty}=\frac{2561}{256}.
\]
These are also the **minimum** possible endpoint operator norms among *all* real or complex linear projections onto \(\mathcal R\), not merely translation-invariant projections.

## Assumptions and scope
Vertices are \((r,c)\) for \(r,c\in\{0,1,2\}\); edges are the twelve unordered nearest-neighbour pairs, with no periodic wrap-around. A spanning tree has eight edges. Addition on \(H\) is coordinatewise modulo two. Fourier transforms are **unnormalized** as in the displayed definition; the inverse includes a factor \(2^{-12}\), and counting convolution has eigenvalues \(W(s)\). A ``positive singular value'' means the absolute value of a nonzero eigenvalue. The norm statements concern counting-measure \(\ell^p(H)\), whose endpoint norms agree with the corresponding normalized-counting norms.

## Proof
**1. Exact exhaustive certificate.** There are exactly \(\binom{12}{8}=495\) potential edge sets of size eight. `verify_enumeration.py` constructs the twelve grid edges, tests each of the 495 candidates by a nine-vertex disjoint-set cycle and connectivity criterion, and obtains exactly \(192\) spanning trees. It places one at each tree incidence mask in a length-\(4096\) integer vector. The ordinary twelve-stage Walsh–Hadamard butterfly computes every \(W(s)\) with integer additions/subtractions. The resulting histogram is the 15-row table above; its entries sum to \(4096\). The code asserts the histogram rather than merely recording it.

An independent exhaustive certificate, `verify_determinant.py`, generates the same unlabelled grid in a different edge order and for each of the \(4096\) possible sign assignments \(w_e\in\{-1,1\}\), forms the \(8\times8\) reduced weighted Laplacian
\[
L^{(8)}(w)=\left(\sum_{e=\{a,b\}}w_e(\mathbf e_a-\mathbf e_b)(\mathbf e_a-\mathbf e_b)^{\mathsf T}\right)^{(8)}.
\]
Exact fraction-free Bareiss elimination obtains the integer determinant, which equals the signed spanning-tree sum by the weighted matrix-tree theorem. It recovers the same absolute-value histogram **without enumerating trees or using a Walsh butterfly**. Hence each histogram is certified by two distinct finite algorithms, not by a numerical approximation or an unverified output log. Both scripts use only the Python standard library and terminate with explicit assertions.

**2. Divisibility and sharp gap.** The enumeration independently gives \(136\) spanning trees through each of the eight exterior perimeter edges, and \(112\) through each of the four interior edges incident to the central vertex. For any frequency set \(S\), the parity count \(N_{\mathrm{odd}}(S)\) of trees meeting \(S\) oddly satisfies
\[
N_{\mathrm{odd}}(S)\equiv \sum_{e\in S}\#\{T:e\in T\}\equiv0\pmod2.
\]
Thus \(W(S)=192-2N_{\mathrm{odd}}(S)\) is divisible by four. The first enumerator's edge order is the order in which each grid vertex \((r,c)\), in lexicographic order, contributes its right neighbour and then its lower neighbour when those exist. The sign frequency with decimal mask \(116\) in this order has \(W(116)=4\); this witnesses sharpness. By the triangle inequality \(|W(S)|\le192\), and equality occurs for the empty frequency (also the all-edge frequency, since every tree contains eight edges). Hence the exact positive-spectrum condition number is \(192/4=48\).

**3. Projection.** Write \(B(s)=\mathbf1_{W(s)\ne0}\). The Fourier multiplier of the orthogonal range projection is \(B\). Therefore its translation-invariant convolution kernel is
\[
k(x)=2^{-12}\sum_{s\in H}B(s)(-1)^{x\cdot s}.
\]
Both independent programs compute the complete integer numerator array, and both assert
\[
\sum_{x\in H}\left|\sum_{s\in H}B(s)(-1)^{x\cdot s}\right|=40976.
\]
For a convolution operator on a finite group, its \(\ell^1\) and \(\ell^\infty\) norms equal the \(\ell^1\)-norm of its kernel, so the claimed value is \(40976/4096=2561/256\). The norm bound is achieved by an input whose signs match a translated/reflected kernel.

To see optimality among *all* projections, take an arbitrary bounded linear projection \(Q\) onto \(\mathcal R\) on either endpoint space and average \(\tau_xQ\tau_x^{-1}\) over the \(4096\) translations \(\tau_x\) of \(H\). The average remains a projection onto the same translation-invariant range, has norm at most \(\|Q\|\), and commutes with all translations. A translation-invariant projection onto exactly \(\mathcal R\) must be identity at every character in \(\operatorname{supp}W\) and zero at every character outside it, hence equals \(P\). Therefore \(\|Q\|\ge\|P\|\).

## Verification
Run `python3 verify_enumeration.py` and `python3 verify_determinant.py` in a directory containing the two files. They independently assert the tree count, complete histogram, sharp gap, Fourier rank, and exact integer kernel absolute-sum \(40976\). The first verifies that all single-edge tree counts are even, proving the divisibility lemma. The second uses no external data or libraries. The computations range over all \(495\) candidate eight-edge sets and all \(4096\) signed weights, respectively; no extrapolation is used. This is a finite, exact theorem about the single specified graph.

## Relationship to prior work
The unweighted finite-grid tree enumeration and its connection with Laplacian/Tutte techniques form the archival starting point in Shrock and Wu's *Spanning Trees on Graphs and Lattices in d Dimensions* (arXiv:cond-mat/0004341, posted 2000-04-19, notably §§1,4,6). The weighted matrix-tree identity used for the independent determinant certificate is classical; Klee and Stamps, *Linear Algebraic Techniques for Weighted Spanning Tree Enumeration* (arXiv:1903.03575, §1), gives an accessible statement. These sources supply general computational machinery and tree counting, not the explicit full \(4096\)-frequency Walsh histogram or sharp projection constant claimed here. Comparable computations for hypercube, wheel and ladder tree families concern different graphical matroids, and their numerical values do not imply the square-grid values here.

## Limitations
This result makes no all-grid-size rank or stability claim. The weighted matrix-tree theorem makes any finite signed coefficient computable in principle, so the originality claim concerns the complete exact values and their reconstruction interpretation, not a new determinant identity. The finite enumeration gives no monotonicity law for larger grids. Unindexed historical tabulations of signed grid-tree polynomials or equivalent character spectra could change the priority assessment. The result has not received independent external validation.

## References
- R. Shrock and F. Y. Wu, *Spanning Trees on Graphs and Lattices in d Dimensions*, arXiv:cond-mat/0004341 (first posted 2000-04-19), https://arxiv.org/abs/cond-mat/0004341.
- S. Klee and M. T. Stamps, *Linear Algebraic Techniques for Weighted Spanning Tree Enumeration*, arXiv:1903.03575 (first posted 2019-02-27), https://arxiv.org/abs/1903.03575.
