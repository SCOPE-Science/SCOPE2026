# Exact Walsh rank and endpoint projection norm of three-cube spanning-tree convolution

## Finding
Let \(G=\mathbb F_2^{12}\), with coordinates indexed by the twelve edges of the three-dimensional cube graph \(Q_3\). Let \(f:G\to\{0,1\}\) indicate the edge sets of all spanning trees of \(Q_3\), and let \(C_f\) be **counting convolution**, \((C_f g)(x)=\sum_{y\in G}f(y)g(x\oplus y)\). Its unnormalized Walsh multipliers are \(W(s)=\sum_{x\in G}f(x)(-1)^{\langle s,x\rangle}\). Then exactly \(1,522\) of the \(4,096\) multipliers vanish, and
\[
\operatorname{rank}C_f=2,574,\qquad
\min_{W(s)\ne0}|W(s)|=8,\qquad
\max_s|W(s)|=384.
\]
In particular, its positive-spectrum condition number is \(48\) and \(\|C_f^\dagger\|_{2\to2}=1/8\).

Let \(R=\operatorname{ran}C_f\). Among **all** real linear projections \(P\) onto \(R\), without any translation-invariance assumption, the least \(\ell^1\)- and \(\ell^\infty\)-operator norms agree and equal
\[
\boxed{\inf_{P^2=P,\,\operatorname{ran}P=R}\|P\|_{1\to1}
=\inf_{P^2=P,\,\operatorname{ran}P=R}\|P\|_{\infty\to\infty}
=\frac{14243}{1024}.}
\]
The infima are attained by the canonical Walsh-support projection. All multipliers are divisible by \(8\), and this divisibility is sharp. The complete absolute-multiplier distribution is:

| Absolute multiplier | Number of frequencies |
|---:|---:|
| 0 | 1522 |
| 8 | 1632 |
| 16 | 288 |
| 24 | 16 |
| 32 | 456 |
| 40 | 48 |
| 56 | 48 |
| 64 | 36 |
| 72 | 48 |
| 384 | 2 |

## Assumptions and scope
Vertices of \(Q_3\) are the integers \(0,\ldots,7\), interpreted as three-bit words. Distinct vertices \(u,v\) are adjacent when \(v=u\oplus2^k\) for one \(k\in\{0,1,2\}\). Edges are ordered by increasing \(u\) and then increasing \(k\), keeping only \(u<v\). This produces the list `[(0,1),(0,2),(0,4),(1,3),(1,5),(2,3),(2,6),(3,7),(4,5),(4,6),(5,7),(6,7)]`. The coordinates of \(G\) follow this order. All graph vertices and edges are labelled, all arithmetic is exact over the integers, and the convolution contains no probability normalization. The ambient function spaces are real-valued functions on all \(4,096\) elements of \(G\), equipped with counting-measure norms.

## Proof
**(1) Exact tree enumeration and signed frequencies.** Every spanning tree of \(Q_3\) has exactly seven edges. There are \(\binom{12}{7}=792\) seven-edge candidates. For each candidate, joining the endpoints of its edges and rejecting any cycle exhaustively decides whether it is a spanning tree. The `spanning_tree` routine in `verify.py` implements this criterion and finds exactly \(384\) accepted sets. Thus the characteristic vector \(f\) of length \(4096\) is completely determined by finite elementary tests. Its unnormalized Walsh transform is computed by twelve exact butterfly stages (`fwht_inplace`); by the standard identity \(H_2^{\otimes12}H_2^{\otimes12}=4096I\), this computes every \(W(s)\) exactly.

**(2) Independent coefficient proof and finite certificate.** For each frequency \(s\) give edge \(e_j\) the integer weight \(w_j=(-1)^{s_j}\). Form the signed weighted Laplacian \(L_s\), where the diagonal entry at a vertex is the sum of its incident edge weights and the off-diagonal entry is minus the edge weight. The weighted Matrix-Tree Theorem gives
\[
W(s)=\det L_s^{(7)},
\]
where \(L_s^{(7)}\) deletes row and column of vertex \(7\). The `matrix_tree` implementation uses exact fraction-free integer elimination, independently of tree enumeration and butterfly computation. It agrees with the latter at **all** \(4096\) frequencies. The complete output is `frequency_certificate.csv`; the certificate is regenerated and compared byte-for-byte by `python verify.py`. Moreover, every one of the \(4096\) sign patterns lies in exactly one of the \(144\) orbits under the \(48\) coordinate-permutation and translation automorphisms of \(Q_3\), as certified by `automorphism_orbits.csv`. Each orbit is checked to have a constant signed multiplier, and orbit-weighted counts reproduce the zero count. The signed histogram is also recovered from the absolute histogram above: every nonzero absolute level has equally many positive and negative values because flipping all twelve edge signs changes every seven-edge tree contribution by \(-1\). This agrees with the two extreme coefficients \(W(0)=384\) and \(W((1,\ldots,1))=-384\).

**(3) Divisibility, sharpness and rank.** Modulo two, every edge weight is \(1\), so every reduced Laplacian has the same reduction. Over \(\mathbb F_2\) that \(7\)-by-\(7\) matrix has rank \(4\), with reduced row echelon form (rows shown as bit strings)
```
1000111
0100110
0010101
0001011
0000000
0000000
0000000
```
Unimodular integer row operations can therefore produce three entirely even rows of every reduced signed Laplacian. Its determinant is divisible by \(2^3=8\). The complete certificate shows exactly \(1632\) coefficients of absolute value \(8\), proving sharpness; all nonzero magnitudes and their multiplicities are in the displayed table. Hence there are \(4096-1522=2574\) nonzero multipliers. Fourier diagonalization of counting convolution proves the stated rank, singular values, and pseudoinverse norm. The exact Parseval check is \(\sum_s W(s)^2=4096\cdot384\).

**(4) Unrestricted sharp endpoint projection constants.** Put \(S=\{s:W(s)\ne0\}\) and define the integer Fourier sum \(H(z)=\sum_{s\in S}(-1)^{\langle s,z\rangle}\). The Fourier-support projection has convolution kernel \(K(z)=H(z)/4096\), so its \(\ell^1\)- and \(\ell^\infty\)-operator norms are both \(4096^{-1}\sum_z|H(z)|\). Exhaustive integer transform of the certified support gives
\[
|S|=2574,\qquad \sum_{z\in G}|H(z)|=56972,
\qquad \frac{56972}{4096}=\frac{14243}{1024}.
\]
The checker verifies the inverse-transform identity \(\mathcal W H=4096\,1_S\), Parseval, and direct character sums at every automorphism-orbit representative. To prove global rather than merely translation-invariant optimality, take any projection \(P\) onto \(R\) and average its conjugates under the \(4096\) translations of \(G\). The average still projects onto \(R\), is translation-invariant, and has norm no larger than \(\|P\|\) in either translation-invariant endpoint norm. A translation-invariant projection onto \(R\) has Fourier multiplier \(1\) on \(S\) and \(0\) outside, hence is uniquely the Fourier-support projection. The displayed constant is thus the minimum over all projections.

## Verification
Run `python verify.py` in the directory containing `verify.py`, `frequency_certificate.csv`, and `automorphism_orbits.csv`. The checker uses only the Python standard library and exact integers/Fractions; it exhaustively tests the \(792\) possible seven-edge sets, all \(4096\) signed Matrix-Tree determinants, both finite Walsh transforms, all \(48\) cube automorphisms, and all \(144\) signed-frequency orbits. It asserts the exact histogram, Parseval identities, divisibility, rank, and endpoint norm. Successful execution prints `Q3_SPANNING_TREE_WALSH_EXACT_PASS trees=384 frequencies=4096 orbits=144 rank=2574 lambda=14243/1024`. This is an exhaustive proof certificate for the finite object, not a computational extrapolation to larger cubes.

## Relationship to prior work
Martin and Reiner (first public preprint in 2003) established factorizations of cube spanning-tree enumerators that track edge directions and decoupled degrees, together with the general weighted Matrix-Tree framework. Their parametrized factorization does not evaluate all \(2^{12}\) *independently* signed edge assignments or the Fourier support. Tuffley (preprint in 2011) gave a bijective proof that \(Q_3\) has \(384\) spanning trees and analyzed edge slides; this unsigned count is prior knowledge, not the contribution here. The present result evaluates the **complete independent-edge sign distribution**, its exact convolution rank, and the minimum endpoint norm of projection onto the Fourier range. Standard translation averaging supplies the qualitative projection-optimality argument; the new finite invariant is its exact evaluated value. These distinctions are mathematical implication comparisons, not claims that the cited sources are unrelated.

## Limitations
The exact spectrum and projection constant are proved only for the **three-dimensional cube**; no claim is made about all hypercubes, arbitrary signed weights beyond \(\pm1\), or endpoint norms of the original convolution operator. The finite certificate is mathematically exhaustive but has not received independent external validation. Historical-priority comparison of the full mathematical literature is not exhaustive; an earlier unpublished or differently indexed full signed-cube census could affect originality.

## References
- Jeremy L. Martin and Victor Reiner, *Factorizations of some weighted spanning tree enumerators*, arXiv:math/0302213, first posted 2003-02-18; Journal of Combinatorial Theory, Series A 104 (2003), 287–300. https://arxiv.org/abs/math/0302213
- Christopher Tuffley, *Counting the spanning trees of the 3-cube using edge slides*, arXiv:1109.6393, first posted 2011-09-29; Australasian Journal of Combinatorics 54 (2012), 189–206. https://arxiv.org/abs/1109.6393
