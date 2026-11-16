# An arithmetic zero-free criterion for four-cycle Walsh projections on \(K_{3,n}\)

## Finding
For every integer \(n\ge2\), let \(G_n=\mathbb F_2^{3n}\) index the edges of the complete bipartite graph \(K_{3,n}\). Let \(\mathcal C_n\subset G_n\) be the edge-incidence vectors of its \(3\binom n2\) four-cycles, and put
\[
W_n(s)=\sum_{C\in\mathcal C_n}(-1)^{\langle s,C\rangle},\qquad s\in G_n.
\]
The Walsh transform is explicitly classified below. In particular, **some Walsh coefficient vanishes if and only if** one of the following holds:

1. \(n=8k+1\) for an integer \(k\ge1\);
2. \(n=8k\) for an integer \(k\ge1\) for which \(6k\) is representable as a sum of three integer squares, equivalently \(6k\ne4^a(8b+7)\) for every pair of nonnegative integers \(a,b\).

For every other integer \(n\ge2\), every Fourier coefficient is nonzero. Thus convolution by \(\mathbf1_{\mathcal C_n}\) on \(G_n\) is invertible exactly in those dimensions. The criterion is not purely periodic: for example the transform has a zero for \(n=8\), but no zero for \(n=80\), since \(6(80/8)=60=4(8\cdot1+7)\).

More generally let \(t=(t_0,t_1,t_2,t_3)\) run over nonnegative integer quadruples with \(\sum_a t_a=n\). Define \(w(t)=2\sum_a t_a^2-n(n+3)/2\). For **each** integer \(w\), the exact multiplicity of the unnormalized Walsh coefficient \(w\) on \(G_n\) is
\[
M_n(w)=2^n\sum_{\substack{t_0+\cdots+t_3=n\\t_a\ge0,\ w(t)=w}}\frac{n!}{t_0!t_1!t_2!t_3!}.
\]
In particular the rank of the corresponding XOR-convolution matrix is \(2^{3n}-M_n(0)\), and its nullity is \(M_n(0)\).

## Assumptions and scope
The bipartite side of size three has labeled vertices \(1,2,3\); the other side has labeled vertices \(1,\ldots,n\). Edges carry signs \(s_{p,i}\in\{-1,1\}\). The Walsh coefficient is **unnormalized**; Fourier inversion on \(G_n\) gives the normalized convolution kernel \(2^{-3n}W_n(s)\). The assertion concerns the entire four-cycle frequency orbit, not signed adjacency eigenvalues or spanning-tree characters.

## Proof
For each column \(i\), form its three pair products
\[
x_{i,1}=s_{1,i}s_{2,i},\quad x_{i,2}=s_{1,i}s_{3,i},\quad x_{i,3}=s_{2,i}s_{3,i}.
\]
Every pair-product triple has product one and belongs to exactly one of the four patterns \((1,1,1)\), \((1,-1,-1)\), \((-1,1,-1)\), \((-1,-1,1)\). Each pattern has exactly two lifts to the three original signs. Let \(t_a\) count its occurrence across the \(n\) columns. Every four-cycle chooses a pair of distinct columns and one pair of rows. With \(S_r=\sum_i x_{i,r}\), the elementary identity \(2\sum_{i<j}x_{i,r}x_{j,r}=S_r^2-n\) yields
\[
W_n=\tfrac12\left(S_1^2+S_2^2+S_3^2-3n\right).
\]
The four allowed sign patterns are the nonconstant columns of a four-by-four Hadamard matrix. Orthogonality gives \(S_1^2+S_2^2+S_3^2=4\sum_a t_a^2-n^2\), whence \(W_n=w(t)\). Choosing a sequence of four pattern labels with multiplicities \(t\) gives the multinomial factor; each of the \(n\) columns has two sign lifts. This proves the exact multiplicity formula and all normalization factors.

Set \(z_r=S_r\). A Fourier zero is equivalent to \(z_1^2+z_2^2+z_3^2=3n\). These three integers have parity \(n\); moreover their pattern counts are recovered by
\[
\begin{aligned}
t_0&=(n+z_1+z_2+z_3)/4,&t_1&=(n+z_1-z_2-z_3)/4,\\
t_2&=(n-z_1+z_2-z_3)/4,&t_3&=(n-z_1-z_2+z_3)/4.
\end{aligned}
\]
If \(n\) is odd, each \(z_r\) is odd, so \(3n\equiv3\pmod8\), hence \(n\equiv1\pmod8\). Conversely let \(n=8k+1\ge9\). Legendre's three-square theorem supplies integers \(z_1,z_2,z_3\) with sum of squares \(3n\), since \(3n\equiv3\pmod8\). Every \(z_r\) is odd. Independently reversing their signs, we may assume each \(z_r\equiv1\pmod4\). The displayed inverse formulas are then integers. By Cauchy–Schwarz, \(\sum_r|z_r|\le3\sqrt n\le n\), so all four counts are nonnegative. Thus the required zero exists.

If \(n\) is even, every \(z_r\) is even; consequently \(n\) must be divisible by four. Write \(n=4h\) and \(z_r=2v_r\). A zero requires \(v_1^2+v_2^2+v_3^2=3h\). The inverse formula implies \(v_1+v_2+v_3\) even, but that sum has the parity of \(3h\), so \(h\) is even. Therefore \(n=8k\), and a zero necessarily gives a three-square representation of \(6k\).

Conversely suppose \(n=8k\) and \(6k=v_1^2+v_2^2+v_3^2\). Put \(z_r=2v_r\). Because the square sum is even, \(\sum_r v_r\) is even, so each inverse count is an integer. For \(k\ge2\), the bound \(\sum_r|v_r|\le\sqrt{18k}\le4k\) ensures every count is nonnegative. For \(k=1\), the explicit choice \((v_1,v_2,v_3)=(1,1,2)\) yields \(t=(4,1,1,2)\), also valid. Finally, Legendre's theorem characterizes the positive integers representable by three squares as precisely those not of the form \(4^a(8b+7)\). Applying it to \(6k\) completes the classification.

The convolution operator by \(\mathbf1_{\mathcal C_n}\) on functions on \(G_n\) has eigenvalues \(W_n(s)\), indexed by the Walsh characters. Its nullity and invertibility statements therefore follow from the proved exact multiplicities.

## Verification
The accompanying standalone Python checker independently enumerates all edge-sign assignments for \(2\le n\le5\) and compares every Walsh level against the four-cell multinomial formula, including the \(2^n\) sign-lift factor. For \(2\le n\le8\), it also checks exact coefficient multiplicities, the vanishing first moment, and Parseval's identity \(\mathbb E W_n^2=3\binom n2\). Finally, the zero criterion is checked against explicit multinomial sums through \(n=22\). Executing the checker prints `ALL_C4_CHECKS_PASS`. These finite verifications are corroboration, not the general proof.

## Relationship to prior work
Goodall's treatment of Fourier methods for graphical objects supplies general background but not the arithmetic zero criterion for these four-cycle orbits. Pirzada, Shamsher and Bhat study the spectra of signed complete bipartite adjacency matrices, particularly structured sign classes; an adjacency-spectrum identity by itself does not classify when the **sum** of all signed four-cycle products vanishes for arbitrary signings. Legendre's three-square theorem is an essential established input, not a new claim. The present statement identifies the exact Fourier-zero locus, its multiplicities, and its exceptional arithmetic dimensions. Searches included equivalent signed-cycle, Walsh, finite-character, and adjacency-spectrum formulations; an unlocated specialization remains possible.

## Limitations
The proof relies on Legendre's classical three-square theorem and makes no assertion about higher even cycle frequency sets or arbitrary bipartite graphs. The displayed multinomial expression is exact but is not claimed to be a closed product for all nonzero Fourier levels. Historical priority cannot be established exhaustively, and independent mathematical validation has not been performed.

## References
- A. Goodall, “Fourier Analysis on Finite Abelian Groups: Some Graphical Applications,” *Combinatorics, Complexity, and Chance*, 2007, doi:10.1093/acprof:oso/9780198571278.003.0007.
- S. Pirzada, T. Shamsher and M. A. Bhat, “On the eigenvalues of signed complete bipartite graphs,” arXiv:2111.07262 (2021).
- A. Moreno, “On sums of three squares,” arXiv:0812.0540 (2008); Legendre's classical three-square theorem is applied as prior mathematical input.
