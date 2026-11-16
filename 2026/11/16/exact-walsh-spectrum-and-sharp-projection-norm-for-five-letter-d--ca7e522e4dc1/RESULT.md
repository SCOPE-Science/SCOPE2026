# Exact Walsh spectrum and sharp projection norm for five-letter derangements

## Finding

Let \(G=M_5(\mathbb F_2)\) be the additive group of binary \(5\)-by-\(5\) matrices, and let \(\mathcal D\subset G\) consist of the incidence matrices of the \(44\) fixed-point-free permutations of five letters. Define the unnormalized Walsh transform of its indicator by
\[
W(A)=\sum_{B\in\mathcal D}(-1)^{\langle A,B\rangle},\qquad
\langle A,B\rangle=\sum_{i,j=0}^4 A_{ij}B_{ij}\pmod2.
\]
The **complete absolute Fourier-value distribution** over all \(2^{25}\) matrices \(A\in G\) is:

| \(|W(A)|\) | \(0\) | \(2\) | \(4\) | \(6\) | \(8\) | \(10\) | \(12\) | \(16\) | \(22\) | \(44\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Multiplicity divided by \(2^{14}\) | 338 | 504 | 405 | 260 | 130 | 240 | 90 | 60 | 20 | 1 |

Consequently the orthogonal Fourier projection \(P_{\mathcal D}\) onto the \(44\) characters indexed by \(\mathcal D\) has sharp endpoint norms
\[
\boxed{\|P_{\mathcal D}\|_{\ell^1(G)\to\ell^1(G)}=\|P_{\mathcal D}\|_{\ell^\infty(G)\to\ell^\infty(G)}=\frac{1269}{256}.}
\]
The convolution operator \(T_{\mathcal D}:h\mapsto\mathbf1_{\mathcal D}*h\), with **unnormalized convolution**, has exactly \(28,016,640\) nonzero Fourier multipliers and \(5,537,792\) zero multipliers. Its least positive singular value is \(2\), and
\[
\boxed{\|T_{\mathcal D}^{\dagger}\|_{\ell^2\to\ell^2}=\frac12.}
\]
Equivalently, the permanent of a uniformly signed hollow \(5\)-by-\(5\) matrix is zero with probability \(169/1024\). Here “hollow” means the diagonal entries are fixed at zero and all \(20\) off-diagonal entries are independent uniform signs.

## Assumptions and scope

Rows and columns are indexed by \(\{0,1,2,3,4\}\). A derangement \(\sigma\) satisfies \(\sigma(i)\ne i\) for every \(i\). The ambient group contains all \(25\) binary matrix coordinates, but derangement matrices have zero diagonal; the five diagonal frequencies are therefore inert. A Fourier projection is the operator whose normalized Fourier transform multiplies by the indicator of \(\mathcal D\). The convolution eigenvalues of \(T_{\mathcal D}\) are the unnormalized Walsh coefficients \(W(A)\). All \(\ell^p\) norms use counting measure; the adjoint pseudoinverse statement uses the standard Euclidean Hilbert structure. This is an exact finite theorem at order five, not a statement for arbitrary permutation sizes.

## Proof

**1. Walsh–hollow-permanent identity.** For a frequency \(A\in G\), put \(S_{ij}=(-1)^{A_{ij}}\) when \(i\ne j\), and \(S_{ii}=0\). Then
\[
W(A)=\sum_{\sigma:\,\sigma(i)\ne i}\prod_{i=0}^4S_{i,\sigma(i)}=\operatorname{per}(S),
\]
with the permanent evaluated in ordinary integers. Its value does not depend on the five entries \(A_{ii}\). There are \(20\) relevant binary sign coordinates.

**2. Gauge reduction.** For each left row vertex \(R_i\) and right column vertex \(C_j\), consider the bipartite graph with edges \((R_i,C_j)\) exactly when \(i\ne j\). It is connected, with \(10\) vertices and \(20\) edges. The following nine edges form a spanning tree:
\[
T=\{(0,1),(0,2),(0,3),(0,4),(1,0),(2,0),(3,0),(4,0),(1,2)\}.
\]
Multiplying entire rows or columns of \(S\) by a sign multiplies \(\operatorname{per}(S)\) by an overall sign. On a spanning tree, row/column gauge switches can make all nine signs positive, uniquely up to the global simultaneous switch of every row and column. For each normalized assignment on the remaining \(11\) edges, exactly \(2^9=512\) original signings have the same permanent magnitude. Reinstating the inert diagonal frequencies yields a total multiplicity factor \(2^{9+5}=2^{14}\).

**3. Exact complete integer certificate.** Let \(F\) be the \(11\) edges not in \(T\), ordered lexicographically, and enumerate all \(44\) derangements \(\sigma\). For each such \(\sigma\), let \(m_\sigma\) be the \(11\)-bit mask of the edges \((i,\sigma(i))\) lying in \(F\). For each mask \(b\in\{0,\ldots,2047\}\), the normalized hollow permanent is precisely
\[
H(b)=\sum_{\sigma\text{ derangement}}(-1)^{\operatorname{popcount}(b\mathbin{\&}m_\sigma)}.
\]
This is an *explicit finite formula over a completely enumerated domain*: each of the \(2^{11}\) cases is covered, with no numerical approximation. Exact integer evaluation gives the coefficient identity
\[
\boxed{\sum_{b=0}^{2047}z^{|H(b)|}=338+504z^2+405z^4+260z^6+130z^8+240z^{10}+90z^{12}+60z^{16}+20z^{22}+z^{44}.}
\]
The standalone certificate `check_derangement_walsh.py` implements this expression and, separately, builds the \(2^{20}\)-entry Boolean indicator on the *full off-diagonal group* and computes its entire integer Walsh–Hadamard transform. The latter check independently verifies every displayed multiplicity, rather than presuming gauge normalization. Since both computations are finite exact arithmetic over fully specified domains and the source is included, the displayed identity admits exhaustive replay. The formula and algorithm constitute the finite proof of this coefficient identity; it is not an extrapolation from smaller examples.

**4. Fourier consequences.** The Walsh-value distribution follows by multiplying each coefficient of the polynomial by \(2^{14}\). In particular there are \(338\cdot2^{14}=5,537,792\) zero frequencies; the other \(33,554,432-5,537,792=28,016,640\) have nonzero multipliers. By the displayed polynomial, the least strictly positive magnitude is exactly \(2\). Unitary Walsh diagonalization proves the rank and pseudoinverse claims, regardless of the counting-measure normalization of the underlying Hilbert space.

The Fourier-projection convolution kernel is \(K(A)=2^{-25}W(A)\). On a finite abelian group, convolution by \(K\) has sharp \(\ell^1\) and \(\ell^\infty\) operator norms both equal to \(\sum_{A\in G}|K(A)|\), attained respectively on a delta input and on a sign-matched input. Therefore
\[
\|P_{\mathcal D}\|=2^{-25}\sum_{A\in G}|W(A)|
=\frac1{2048}\sum_{b=0}^{2047}|H(b)|=\frac{1269}{256}.
\]
As uniform off-diagonal sign matrices correspond exactly to Walsh frequencies modulo inert diagonals, their zero-permanent probability is \(338/2048=169/1024\).

## Verification

Run `python3 check_derangement_walsh.py` in the same directory (Python 3.10 or later; standard library only). It independently compares the complete \(2048\)-assignment gauge evaluation with the complete length-\(1,048,576\) Walsh–Hadamard transform, and checks the exact coefficient histogram, total mass, Parseval second moment, zero count, rank, minimum positive magnitude, sharp endpoint projection norm, and zero probability. Expected output starts `DERANGEMENT_FIVE_EXACT_PASS`. The exhaustive arithmetic is a finite proof component; no claim of independent peer verification is made.

## Relationship to prior work

The derangement count \(44\) and the permanent of the unsigned matrix \(J-I\) are classical, developed among other places in Feinsilver–McSorley's study of generalized derangements. Their formulas for \(sI+tJ\) and the Johnson scheme do **not** supply the complete distribution obtained by assigning signs independently to all off-diagonal entries. Wanless investigates permanents of complete \(\pm1\) matrices, including attainable magnitudes, but those matrices have nonzero diagonals and his inspected results do not give the signed hollow-permanent histogram. Tao–Vu study asymptotic permanents of unrestricted random sign matrices, not the exact hollow order-five distribution.

A closely related published calculation, *Exact order-five binary permutation Fourier spectrum and endpoint norm*, gives the full \(120\)-permutation orbit, not the \(44\)-derangement suborbit; its eight-level spectrum and endpoint norm differ because deleting the diagonal-permitted matchings changes every Walsh coefficient, rather than simply deleting frequencies from that transform. The published derangement-incidence covariance classification studies only degree-one statistics; its two covariance eigenvalues do not determine the entire degree-\(25\) Walsh transform. Neither inspected statement implies the distribution above. Literature priority comparison was bounded, not exhaustive.

## Limitations

The statement is only for order five; no large-order law, approximate random-sign distribution, or endpoint pseudoinverse bound is established. The coefficient identity is a transparent finite exhaustive integer certificate, not a closed symbolic coefficient derivation. A historic table, signed rook-polynomial computation, or equivalent code weight-enumerator classification may predate this treatment and remains a priority risk. No independent mathematical validation has been performed.

## References

1. P. Feinsilver and J. McSorley, *Zeons, Permanents, the Johnson Scheme, and Generalized Derangements*, International Journal of Combinatorics (2011), Article ID 539030, first published 2011-06-02; DOI: `10.1155/2011/539030`. Available at `https://doi.org/10.1155/2011/539030`.
2. I. M. Wanless, *Permanents of matrices of signed ones*, Linear and Multilinear Algebra **53** (2005), 427–433; DOI: `10.1080/03081080500093990`; open author PDF: `https://users.monash.edu.au/~iwanless/papers/wangconjLAMA.pdf`.
3. T. Tao and V. Vu, *On the permanent of random Bernoulli matrices*, first arXiv submission 2008-04-15, `https://arxiv.org/abs/0804.2362`.
4. *Exact order-five binary permutation Fourier spectrum and endpoint norm*, published research record `2026/11/8/SCOPE-exact-order-five-binary-permutation-fourier-spectrum-and-endpoin--69d359ed8a05`, public source `https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-order-five-binary-permutation-fourier-spectrum-and-endpoin--69d359ed8a05`.
5. *The complete covariance spectrum of uniform derangement assignment scores*, published research record `2026/10/26/SCOPE-the-complete-covariance-spectrum-of-uniform-derangement-assignme--a208797ec285`, public source `https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-the-complete-covariance-spectrum-of-uniform-derangement-assignme--a208797ec285`.
