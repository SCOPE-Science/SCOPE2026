# A parity-syndrome construction resolves the asymptotic odd independence of even hypercubes

## Finding
For every even integer \(d\ge 2\), put \(m=\lfloor\log_2d\rfloor\) and \(q=2^m\). The odd independence number of the binary hypercube \(Q_d\) satisfies
\[
\alpha_{\mathrm{od}}(Q_d)\ge 2^{d-1}\left(1-\frac1q\right).
\]
Combining this constructive bound with Corollary 27 of Caro–Petruševski–Škrekovski–Tuza gives the quantitative density-defect bounds
\[
\frac{1}{4d-2}\le \frac12-\frac{\alpha_{\mathrm{od}}(Q_d)}{2^d}\le\frac1{2q}<\frac1d.
\]
In particular, the limit explicitly asked about in their Problem 40 has the affirmative answer
\[
\lim_{\substack{d\to\infty\\d\ \mathrm{even}}}\frac{\alpha_{\mathrm{od}}(Q_d)}{2^d}=\frac12.
\]
Thus the density deficit is of exact order \(1/d\); the exact finite-dimensional optimum is not claimed.

## Assumptions and scope
The hypercube \(Q_d\) has vertex set \(\mathbb F_2^d\), with two vertices adjacent precisely when they differ in one coordinate. An *odd independent set* \(S\) is an independent set such that every vertex outside \(S\) has either zero or an odd number of neighbors in \(S\). Its largest possible size is \(\alpha_{\mathrm{od}}(Q_d)\). Only even integer dimensions \(d\ge2\) are considered. All arithmetic involving labels and syndromes is over \(\mathbb F_2\).

## Proof
**1. Odd-multiplicity coordinate labeling.** Fix even \(d\ge2\), and write \(m=\lfloor\log_2 d\rfloor\), \(q=2^m\). Because \(q\) and \(d\) are even and \(q\le d\), list all \(q\) elements of \(\mathbb F_2^m\) once as \(a_1,\ldots,a_q\), and append \(d-q\) further copies of the zero vector. Thus there are exactly \(d\) labels \(a_1,\ldots,a_d\), and for every label \(s\in\mathbb F_2^m\) its multiplicity \(c_s=|\{i:a_i=s\}|\) is odd (equal to one unless \(s=0\), where it equals \(1+d-q\)).

**2. Linear code.** For \(x=(x_i)\in\mathbb F_2^d\), define its parity \(p(x)=\sum_i x_i\) and its syndrome \(\sigma(x)=\sum_i x_i a_i\). Let
\[
H=\{x:p(x)=0,\ \sigma(x)=0\},\qquad
S=\{x:p(x)=0\}\setminus H.
\]
The linear map \(x\mapsto(p(x),\sigma(x))\) onto \(\mathbb F_2^{m+1}\) has rank \(m+1\): its matrix contains the column \((1,0)\) and each \((1,e_j)\), where \(e_j\) is a coordinate basis vector; their sums yield every \((0,e_j)\). Hence \(|H|=2^{d-m-1}\). Exactly \(2^{d-1}\) vertices have even parity, so
\[
|S|=2^{d-1}-2^{d-m-1}=2^{d-1}(1-1/q).
\]

**3. Odd-neighborhood condition.** The set \(S\) is independent because every hypercube edge changes parity. Every even-parity vertex outside \(S\) belongs to \(H\) and has no neighbors in \(S\). If \(y\) has odd parity, the neighbor \(y+e_i\) is in \(H\) if and only if \(\sigma(y)+a_i=0\). Consequently exactly \(c_{\sigma(y)}\) of the \(d\) neighbors of \(y\) are in \(H\), and exactly \(d-c_{\sigma(y)}\) are in \(S\). Every \(c_s\) is odd and \(d\) is even; therefore this last count is odd. Thus \(S\) is an odd independent set of the asserted size.

**4. Limit and sharp order.** A perfect matching of \(Q_d\), obtained by toggling one fixed coordinate, proves that every independent set has cardinality at most \(2^{d-1}\). It follows that
\[
0\le\frac12-\frac{\alpha_{\mathrm{od}}(Q_d)}{2^d}\le\frac1{2q}<\frac1d,
\]
since \(q\le d<2q\). This proves the limit. The stronger previously published upper bound \(\alpha_{\mathrm{od}}(Q_d)\le (1-1/(2d-1))2^{d-1}\) (Caro et al., Corollary 27) supplies the lower bound \(1/(4d-2)\) on the density deficit, hence its exact \(\Theta(1/d)\) order.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3.9 or newer. It constructs the labels and the full subset \(S\), directly tests independence and every outside vertex's neighbor count for all even dimensions from \(2\) through \(16\), verifies the exact cardinality and matrix rank, checks the published small exact values at dimensions \(4,6,8\), and separately checks the arithmetic for all even dimensions through \(4096\). This finite verification corroborates, but does not replace, the preceding unrestricted proof.

## Relationship to prior work
Caro, Petruševski, Škrekovski and Tuza, *The odd independence number of graphs, I: Foundations and classical classes*, arXiv:2509.20763 (first submitted 2025-09-25), introduce the invariant. Their Section 5, Corollary 27 gives the upper bound used above; Proposition 28 proves exact values \(6,24,112\) at \(d=4,6,8\) and a constant-density lower bound \(7/16\) for even \(d\ge8\). Their Problem 40 explicitly asks whether the normalized optimum tends to \(1/2\) along even dimensions. The present construction agrees with their small exact values and strictly improves the constant \(7/16\) bound at even dimensions \(d\ge16\); it answers the asymptotic question without solving the exact-value problem. Their companion paper arXiv:2510.01897 studies finite and infinite integer-lattice grids and chessboard graphs, not the binary hypercube in this question. General parity-domination and coding-theoretic techniques are related but use distinct constraints or optimization objectives.

## Limitations
The exact value of \(\alpha_{\mathrm{od}}(Q_d)\) at general even dimension is not established. The construction is one lower-bound family; its best possible within other methods is not asserted. The finite checks cannot establish an infinite theorem and no independence of external mathematical review is claimed. Historical priority beyond the specifically compared records remains subject to further literature review.

## References
1. Y. Caro, M. Petruševski, R. Škrekovski, and Zs. Tuza, *The odd independence number of graphs, I: Foundations and classical classes*, arXiv:2509.20763v2 (first public version 2025-09-25), https://arxiv.org/html/2509.20763v2, especially Corollary 27, Proposition 28, and Problem 40.
2. Y. Caro, M. Petruševski, R. Škrekovski, and Zs. Tuza, *The odd independence number of graphs, II: Finite and infinite grids and chessboard graphs*, arXiv:2510.01897v1 (2025-10-02), https://arxiv.org/html/2510.01897v1.
3. Y. Caro, W. F. Klostermeyer, and J. L. Goldwasser, *Odd and residue domination numbers of a graph*, Discussiones Mathematicae Graph Theory 21 (2001), 119–136, https://doi.org/10.7151/dmgt.1137 (related but different parity-domination constraint).
