# Twelve-vertex crown sides form a productive Schur core

## Finding
Let \(C_n\) be the bipartite graph with \(n\) row vertices and \(n\) column vertices, whose zero-one incidence matrix is \(J_n-I_n\). For each integer \(n\ge12\), attach to every vertex a complete rooted tree of height \(100\), with \(10{,}000\) children at every nonterminal vertex, retaining the alternating bipartition. Denote the resulting finite graph by \(G_n\). Then its complex operator-norm Schur-multiplier projection satisfies
\[
\|G_n\|_{\bullet}>2>\|C_n\|_{\bullet}=\frac{2(n-1)}n.
\]
In particular every crown core \(C_n\), \(n\ge12\), is **productive** in the terminology of Levene's theorem. The result establishes a simple, single-crown productive core with twelve vertices on each shore; it makes no assertion about productivity for smaller crowns or optimality of the branching or height.

## Assumptions and scope
For a finite zero-one matrix \(M\), define \(\|M\|_{\bullet}\) as the norm of the Schur map \(X\mapsto M\circ X\) on complex square/rectangular Hilbert-space operator matrices with the operator norm. All parameters and graph sizes in the displayed construction are finite integers, even though the number of graph vertices is enormous. The scientific source is the publicly posted 2026-11-05 paper cited below, primary MSC 47A30. Its Theorem 3.8 supplies an exact, proved trace-norm variational formula for uniformly weighted attached trees.

## Proof
It suffices to treat \(n=12\), because \(G_{12}\) is an induced bipartite subgraph of \(G_n\) for every \(n\ge12\), and Schur projection norm cannot decrease when a finite submatrix is enlarged (Levene, Lemma 2.1). The crown core has singular values \((n-1)/n\) once and \(1/n\) with multiplicity \(n-1\) after normalization by \(n\). Its Schur norm is therefore \(2(n-1)/n<2\).

Write \(m=10000\), \(h=100\), and choose \(u_0=1\), \(u_j=a r^{j-1}\) for \(1\le j\le h\), with \(a=3/4\) and \(r=97/100\). Let \(S=\sum_{j=0}^{h}u_j^2\), \(x_j=u_j^2/S\), and \(P_j=nm^j\). Then \(x\) is a probability vector and the nonnegative chain coefficients of Theorem 3.8 are \(c_j=\sqrt{x_jx_{j+1}}/P_j\). Taking the two-by-two upper-left principal corner of every root tridiagonal matrix, and of every positive-depth chain, gives the trace-norm lower bounds
\[
\begin{split}
S\|G_{12}\|_{\bullet}\ \ge L
&=\frac{\sqrt{121+4a^2}+11\sqrt{1+4a^2}}{12}
+2\left(1-\frac1m\right)T,\\
S&=1+a^2\frac{1-r^{2h}}{1-r^2},\\
T&=\sum_{j=1}^{h-1}u_ju_{j+1}=a^2r\frac{1-r^{2(h-1)}}{1-r^2}.
\end{split}
\]
Here pinching cannot increase trace norm, so these are genuine lower bounds, not numerical approximations. The factor \(1-1/m\) follows from \((P_j-P_{j-1})/P_j\) for positive levels.

Since \((11101/1000)^2<493/4=121+4a^2\) and \((1802/1000)^2<13/4=1+4a^2\), we obtain
\[
L-2S>\frac{6923}{12000}-\frac98\frac{(1-\alpha r)+r(\alpha-r)r^{198}}{1-r^2},\qquad \alpha=\frac{9999}{10000}.
\]
The integer inequalities \(30\cdot97^{33}<11\cdot100^{33}\) and \(400\cdot11^6<30^6\) imply \(r^{198}<1/400\). All coefficients of the power \(r^{198}\) in the negative term are positive, so
\[
L-2S>\frac{6923}{12000}-\frac98\frac{(1-\alpha r)+r(\alpha-r)/400}{1-r^2}
=\frac{496253}{189120000}>0.
\]
Consequently \(\|G_{12}\|_{\bullet}>L/S>2\). The same holds for all \(n\ge12\) by subgraph monotonicity, proving the claim.

## Verification
The standalone standard-library script `verify_certificate.py` reconstructs the rational lower bound, checks both radical lower squares and the power inequality with exact integers, verifies the displayed rational margin, and confirms that \(L>2S\). Running it requires only Python 3; no optimization, floating point, full graph construction, or outside data is needed.

## Relationship to prior work
Levene's 2026 Theorem 3.8 is explicitly used, not claimed as new. That paper proves productivity for the different core \((J_3-I_3)\otimes(J_4-I_4)\) and records unverified numerical evidence for \(J_{15}-I_{15}\); it does not certify \(J_{12}-I_{12}\). Previous proven crown-core results cover \(n\ge13\), which does not imply the \(n=12\) case. The new point is the exact positive witness for this previously uncovered crown size, with a rational geometric depth profile. Nearby Schur-multiplier and graph invariants do not imply this finite attached-tree norm threshold.

## Limitations
No upper bounds or exact multiplier norms are asserted; \(2\) is only crossed by a strictly positive rational certificate. Productivity of crown cores with \(n\le11\), optimal attachment depth, minimal branching, and any smallest-core theorem remain open here. A literature search cannot exclude an equivalent result absent from the searched sources. This is a mathematical proof plus self-review, not an independent audit.

## References
1. Rupert H. Levene, *A half-line of Schur idempotent norms*, arXiv:2611.08419v1 (2026-11-05), https://arxiv.org/html/2611.08419v1. Definitions 3.4–3.7, Lemma 2.1, Theorem 3.8, Definition 4.2, Section 6.
2. Csongor Beke, Marcel K. Goh, Hamed Hatami, Sean Jaffe and Daniel Naylor, *A characterization of idempotent Schur multipliers*, arXiv:2607.14316 (2026); structural decomposition of idempotent Schur multipliers, not a finite attached-crown productivity certificate.
