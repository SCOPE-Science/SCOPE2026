# Sharp Walsh stability and a four-column singularity for rectangle-free binary matrices

## Finding

For every integer \(n\ge2\), let \(\mathcal R_n\subseteq\mathbb F_2^{3n}\) comprise the binary incidence matrices of the labelled bipartite subgraphs of \(K_{3,n}\) that contain no four-cycle, equivalently no all-one \(2\times2\) submatrix. For \(s\in\mathbb F_2^{3n}\), define the **unnormalized** Walsh multiplier
\[
W_n(s)=\sum_{X\in\mathcal R_n}(-1)^{\langle s,X\rangle}.
\]
The following statements hold simultaneously:

1. Convolution by \(\mathbf1_{\mathcal R_n}\) on \(\ell^2(\mathbb F_2^{3n})\), with unnormalized counting measure, is invertible precisely for \(n=2,3\). For every \(n\ge4\) it has a nonzero Fourier kernel.
2. The greatest common divisor of the nonzero integer multipliers is **equal** to their smallest positive absolute value:
\[
\delta_n=\min_{W_n(s)\ne0}|W_n(s)|=\gcd_{s}|W_n(s)|
=\begin{cases}2,&n=2,3,\\2^{n-2},&n\ge4.\end{cases}
\]
3. The exact inverse-on-range (Moore--Penrose) Hilbert-space operator norm is \(\|T_n^\dagger\|_{2\to2}=\delta_n^{-1}\); the exact positive-spectrum condition number is \(N_n/\delta_n\), where
\[
N_n=\sum_{k=0}^{\min(3,n)}\binom3k (n)_k4^{n-k}+n4^{n-1},\qquad
(n)_k=\prod_{j=0}^{k-1}(n-j).
\]
The first singular instance, \(n=4\), additionally has exactly \(621\) zero multipliers among \(4096\) frequencies, so its convolution rank is \(3475\), by exhaustive exact-integer verification.

## Assumptions and scope

Rows are the three labelled vertices in one shore and columns are the \(n\) labelled vertices in the other shore. No identification under row/column permutations is made. A four-cycle is forbidden even when additional edges are present. Character frequencies are binary \(3\times n\) matrices; the convention is \(s_{ij}=1\) for a negative sign \(\sigma_{ij}=(-1)^{s_{ij}}\). No normalization factor is inserted into either the Walsh transform or the convolution. The assertions concern all \(n\ge2\), not arbitrary numbers of rows; the case \(n=1\) is deliberately excluded, since the whole \(3\)-cube then occurs.

## Proof

**A complete signed enumerator.** Call a column *light* if it contains zero or one \(1\), and *heavy* otherwise. Label the three unordered row pairs by \(P=\{12,13,23\}\). A column containing exactly pair \(p\) consumes that pair; a column of three \(1\)'s consumes all three pairs. The matrix is four-cycle-free if and only if no row pair is consumed by more than one column. Thus its heavy columns are either one all-one column with every other column light, or at most three two-one columns with distinct row-pair labels.

For each frequency column \(j\), put
\[
A_j=1+\sigma_{1j}+\sigma_{2j}+\sigma_{3j},\quad
b_{p,j}=\prod_{i\in p}\sigma_{ij},\quad
c_j=\sigma_{1j}\sigma_{2j}\sigma_{3j}.
\]
An exact partition of the admissible matrices gives
\[
W_n(s)=
\sum_{S\subseteq P}\ \sum_{\phi:S\hookrightarrow[n]}
\left(\prod_{p\in S}b_{p,\phi(p)}\right)
\left(\prod_{j\notin\phi(S)}A_j\right)
+\sum_{j=1}^n c_j\prod_{h\ne j}A_h. \tag{1}
\]
The inner maps \(\phi\) are injections, including the unique empty injection. This formula covers every matrix once: the first sum has no all-one column, and the last sum has one.

**Uniform dyadic divisibility.** Every \(A_j\) is even. For \(|S|\le2\), each summand in (1) is divisible by \(2^{n-2}\), as are all terms in the last sum for \(n\ge3\). For \(|S|=3\), group injections according to their *unordered* image \(J\) of size three. The grouped coefficient is the permanent of a \(3\times3\) matrix of signs \(b_{p,j}\). Modulo \(2\), each of its six terms is \(1\), so the permanent is even. The remaining \(n-3\) light-column factors give another factor \(2^{n-3}\). Hence
\[
2^{n-2}\mid W_n(s)\qquad(n\ge3,\ \text{all }s). \tag{2}
\]

**Sharpness and zeros.** Encode the negative rows of each frequency column by a three-bit mask: \(1=\{1\}\), \(3=\{1,2\}\), and \(5=\{1,3\}\). For all \(n\ge3\), choose \(n-3\) columns of type \(1\), two of type \(3\), and one of type \(5\). The three exceptional columns have \(A_j=0\). For a nonzero contribution to (1), they must receive the three different row-pair labels, leaving every other column light. The permanent of the three exceptional sign columns, with pair rows \(12,13,23\), is exactly \(-2\). All other light columns have \(A_j=2\), yielding
\[
W_n(\underbrace{1,\ldots,1}_{n-3},3,3,5)=-2^{n-2}. \tag{3}
\]
For \(n=2\), the frequency columns \((3,3)\) give \(W_2=-2\), directly by the two-heavy-column terms of (1). Equations (2)--(3) give the sharp nonzero gaps.

For every \(n\ge4\), choose *all* frequency columns of type \(3\). Then \(A_j=0\) for every column. Every admissible matrix has at most three heavy columns, so in each summand of (1) at least one light-column factor remains and vanishes. Thus
\[
W_n(3,3,\ldots,3)=0\qquad(n\ge4). \tag{4}
\]

**No zeros for \(n=2,3\).** Counting the disjoint heavy-pair assignments at the all-positive frequency in (1) gives the stated formula for \(N_n\); in particular \(N_2=54\) and \(N_3=334\), both congruent to \(2\) modulo \(4\). The number of admissible matrices containing any fixed entry is \(24\) at \(n=2\) and \(138\) at \(n=3\), by row-column symmetry. These counts can also be obtained by fixing that entry to one: at \(n=2\), the allowed first-column choices give \(8+6+6+4=24\); at \(n=3\), they give \(54+34+34+16=138\). For any frequency \(s\), the parity of the number of matrices on which \(\langle s,X\rangle=1\) is the parity of the sum of the coordinate marginals indexed by \(s\), hence is even. Consequently \(W_n(s)\equiv N_n\equiv2\pmod4\), for \(n=2,3\). In particular, neither case has a zero, and (3) and its \(n=2\) counterpart attain the gap \(2\).

**Operator norms.** The Walsh characters are an orthogonal basis of the finite Boolean group, and convolution by \(\mathbf1_{\mathcal R_n}\) has multipliers \(W_n(s)\). Its largest absolute multiplier is \(N_n\), attained by the trivial character (and never exceeded by the triangle inequality). Its smallest nonzero absolute multiplier is \(\delta_n\), proved above. Taking reciprocals on the nonzero character sectors proves the Moore--Penrose inverse norm, the condition-number formula, and the invertibility threshold.

## Verification

The standalone integer programs `check_walsh.cpp` and `check_independent.py` use different constructions of the admissible set. The former recursively assigns labelled columns while tracking the three consumed pairs, then applies a complete integer fast Walsh--Hadamard transform. The latter directly inspects every binary matrix through \(n=5\), independently checks (1) against a separate eight-state recurrence, and tests explicit witnesses through \(n=20\). Both use exact integer operations.

The exhaustive results are:

| \(n\) | \(N_n\) | zero multipliers | smallest nonzero magnitude |
|---|---:|---:|---:|
| 2 | 54 | 0 | 2 |
| 3 | 334 | 0 | 2 |
| 4 | 1,952 | 621 | 4 |
| 5 | 10,944 | 3,138 | 8 |
| 6 | 59,392 | 58,788 | 16 |
| 7 | 313,856 | 551,862 | 32 |

The full Walsh computations check the integer Parseval identity \(\sum_s W_n(s)^2=2^{3n}N_n\). The infinite-family conclusions, including the sharpness witnesses, follow from the proof above rather than extrapolation from finite checks.

## Relationship to prior work

Kitaev, Mansour and Vella (2005) studied enumeration and transfer methods for binary matrices avoiding small patterns. Their all-equal \(2\times2\) avoidance treats monochromatic configurations of both binary colors, not solely the forbidden four-one submatrix defining this family. In particular their \(3\times3\) both-color count is \(168\), whereas the one-color family in this theorem contains \(334\) matrices.

Ju and Seo (2011) explicitly distinguish avoidance of one constant \(2\times2\) pattern from simultaneous avoidance of both constant patterns and identify the one-pattern enumeration with \(C_4\)-free bipartite graphs. Their paper focuses on ordinary counts and generating functions, not signed coordinatewise Walsh transforms or sharp nonzero Fourier gaps. Previously established finite-group Fourier diagonalization is used as standard background, not claimed as new. The contribution here is the all-frequency divisible-and-sharp law, its invertibility boundary, and exact inverse-on-range stability.

## Limitations

Only bipartite graphs with one shore of exactly three vertices are classified. The full number of zero characters for arbitrary \(n\ge5\) is not determined by the theorem. The \(n=4\) nullity is a finite exact computation, not a closed all-\(n\) formula. Neither unindexed historical results nor an independent external mathematical audit have been exhaustively ruled out. The proof makes no claim about sharp \(\ell^1\) or \(\ell^\infty\) inverse norms.

## References

1. S. Kitaev, T. Mansour and A. Vella, *Pattern Avoidance in Matrices*, Journal of Integer Sequences **8** (2005), article 05.2.2, published 2005-04-07. https://cs.uwaterloo.ca/journals/JIS/VOL8/Mansour/mansour.html
2. H.-K. Ju and S. Seo, *Enumeration of (0,1)-Matrices Avoiding Some \(2\times2\) Matrices*, initial arXiv release 2011-07-07, arXiv:1107.1299. https://arxiv.org/abs/1107.1299
