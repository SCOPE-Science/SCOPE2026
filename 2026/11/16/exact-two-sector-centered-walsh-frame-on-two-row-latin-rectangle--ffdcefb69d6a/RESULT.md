# Exact two-sector centered Walsh frame on two-row Latin rectangles

## Finding

Let \(n\ge3\). Uniformly sample a labelled two-row Latin rectangle \(R\) of order \(n\), with entries from \([n]=\{0,\dots,n-1\}\). For each row \(r\in\{0,1\}\), column \(j\in[n]\), and symbol \(k\in[n]\), define its binary incidence coordinate \(X_{rjk}(R)=\mathbf1_{\{R_{rj}=k\}}\). Define the centered one-coordinate Walsh character
\[
Y_{rjk}(R)=(-1)^{X_{rjk}(R)}-\left(1-\frac2n\right)=-2\left(X_{rjk}(R)-\frac1n\right).
\]
The probability-normalized Gram matrix of these \(2n^2\) characters is exactly
\[
G_n=\frac4{(n-1)^2}
\begin{pmatrix}n-1&-1\\-1&n-1\end{pmatrix}
\otimes P_n\otimes P_n,
\qquad P_n=I_n-\frac1n\mathbf1\mathbf1^{\mathsf T}.
\]
Consequently the entire nonzero spectrum, including multiplicities, is
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
4(n-2)/(n-1)^2&(n-1)^2\\
4n/(n-1)^2&(n-1)^2.
\end{array}
\]
The nullity is \(4n-2\). The row-symmetric contrasts are the least stable modes and row-antisymmetric contrasts are the most stable. The sharp nonzero singular-value condition number of the normalized centered Walsh sampling operator is
\[
\kappa_n=\sqrt{\frac n{n-2}}=1+\frac1n+O(n^{-2}).
\]
In particular the centered Walsh-coordinate system is injective modulo precisely the deterministic line-sum relations, and is asymptotically tight on that identifiable quotient. At the exceptional boundary \(n=2\), the first eigenvalue becomes zero, the second is \(8\), and the rank is one.

## Assumptions and scope

A two-row Latin rectangle is an ordered pair of permutations \((\sigma,\tau)\) of \([n]\) satisfying \(\sigma(j)\ne\tau(j)\) for every column \(j\). All such pairs have equal probability; their number is \(n!\, !n\), where \(!n\) counts derangements. The underlying finite additive group for the Walsh characters is \((\mathbb F_2)^{2n^2}\), and the result concerns the degree-one character restriction to the Latin-rectangle incidence set, **not** full counting convolution on that group. Probabilities and Gram products are normalized by \(n!\,!n\). The operator condition number refers only to its nonzero singular values.

## Proof

The first row is a uniform permutation, and conditional on it, the second row is a uniform permutation avoiding its symbol in every column. By column and symbol relabeling, a given entry has probability \(1/n\). For two incidences from the **same** row, their joint inclusion probability is \(1/n\) if they are identical, zero if their columns agree but symbols differ or vice versa, and \(1/[n(n-1)]\) if both columns and symbols differ.

For incidences from **different** rows, joint inclusion is zero if column and symbol both agree. If exactly one agrees, conditional uniformity of a derangement's image away from its forbidden value gives probability \(1/[n(n-1)]\). If neither agrees, first condition on the symbol occupying the second column in the first row: it equals the prescribed second-row symbol with probability \(1/(n-1)\), forbidding the desired incidence; otherwise that incidence has conditional probability \(1/(n-1)\). Thus the joint probability is exactly \((n-2)/[n(n-1)^2]\).

Center by subtracting \(1/n^2\) from each joint probability. Since each permutation matrix has fixed row and column sums, every covariance block annihilates tensors constant in at least one of its column/symbol coordinates. Therefore each covariance block is a multiple of \(P_n\otimes P_n\). The same-row diagonal entry is \((n-1)/n^2\), giving multiplier \(1/(n-1)\). For the cross-row block, the eigenvalue on the double-contrast space is the four-type difference
\[
0-\frac2{n(n-1)}+\frac{n-2}{n(n-1)^2}=-\frac1{(n-1)^2}.
\]
Hence the incidence covariance equals
\[
\begin{pmatrix}(n-1)^{-1}&-(n-1)^{-2}\\-(n-1)^{-2}&(n-1)^{-1}\end{pmatrix}\otimes P_n\otimes P_n.
\]
Centering Walsh rather than incidence coordinates multiplies it by four. The first factor diagonalizes on the symmetric and antisymmetric row combinations, with eigenvalues \((n-2)/(n-1)^2\) and \(n/(n-1)^2\). Both are positive for \(n\ge3\); each has multiplicity \((n-1)^2\), while every vector annihilated by \(P_n\otimes P_n\) is in the kernel. This proves all rank, nullity, and sharp condition-number assertions. The formula itself also proves the \(n=2\) boundary.

## Verification

Two independently implemented exact-rational programs accompany the result. `latin_enum_verify.py` enumerates all labelled rectangles for \(2\le n\le5\), checks all eight relative pair types directly against the displayed probabilities, and verifies their counts \(n!\,!n\). `latin_mode_verify.py` independently generates rectangles as a permutation composed with a derangement, computes the raw symmetric and antisymmetric double-contrast energies from the samples, and verifies both eigenvalues for \(2\le n\le5\). Both programs complete with assertions passing; neither program is used in place of the all-order proof.

## Relationship to prior work

The 1990 work of Godsil and McKay studies counting, random-entry probabilities, and asymptotic distributions for Latin rectangles; its Section 4 gives approximate containment probabilities in the general regime, rather than the exact full centered Walsh Gram spectrum for two rows. Doyle's publicly dated 2007 exposition describes two-row Latin rectangles as derangements and provides their enumeration. Related investigations of uniformly sampled **single derangements** address a different covariance object from the joint two-row Latin-rectangle incidence frame. The present result identifies the two precise row-symmetry sectors, the complete linear kernel, and sharp finite-sample condition numbers; the older counting or asymptotic assertions do not state these.

## Limitations

No statement is made about higher-degree Fourier characters, nonlinear recovery, nonuniform sampling laws, or rectangles with three or more rows. All-order correctness follows from pair probabilities and exact spectral algebra; finite enumeration is only corroboration. Historical originality could be affected by an unindexed identity for joint derangement-permutation covariance. The result has not undergone independent external validation.

## References

- C. D. Godsil and B. D. McKay, *Asymptotic Enumeration of Latin Rectangles*, J. Combinatorial Theory B 48 (1990), 19–44, https://users.cecs.anu.edu.au/~bdm/papers/LatinRectangles.pdf .
- P. G. Doyle, *The Number of Latin Rectangles*, initial public arXiv version 2007-03-29, https://arxiv.org/abs/math/0703896 .
- N. Astromujoff and M. Matamala, *Wide enough Latin rectangles are perfects*, public arXiv version 2015-04-24, https://arxiv.org/abs/1504.06480 .
