# Complete Fourier support and a characteristic-two rank collapse for the \(3\times3\) adjugate graph

## Finding
Let \(q\) be any prime power, \(V=M_3(\mathbb F_q)\), and \(\Gamma_q=\{(X,\operatorname{adj}X):X\in V\}\). For the coordinate-wise trace-character pairing on \(V\times V\), all additive Fourier coefficients of \(\mathbf1_{\Gamma_q}\) are evaluated up to exact magnitude, and their complete nonzero set is classified by the rank of the second frequency matrix.

Write \(Q_B(X)=\langle B,\operatorname{adj}X\rangle\), \(\mathcal R_B=\{Z:Q_B(X+Z)-Q_B(X)-Q_B(Z)=0\text{ for every }X\}\). For \(r=\operatorname{rank}B\), the following table is exhaustive. The column headed “number of \(A\)” counts the first-frequency matrices for each fixed \(B\).

| \(r\) | Support condition on \(A\) | Number of \(A\) | \(|F(A,B)|\) when supported |
|---|---|---:|---:|
| \(0\) | \(A=0\) | \(1\) | \(q^9\) |
| \(1\) | \(\langle A,Z\rangle=0\) for every \(Z\in\mathcal R_B\) | \(q^4\) | \(q^7\) |
| \(2\) | \(\langle A,Z\rangle=0\) for every \(Z\in\mathcal R_B\) | \(q^6\) | \(q^6\) |
| \(3\), odd \(q\) | every \(A\) | \(q^9\) | \(q^{9/2}\) |
| \(3\), even \(q\) | \(\operatorname{tr}(AB)=(\det B)^{q/2}\) | \(q^8\) | \(q^5\) |

At ranks zero, one, and two, the dimensions of \(\mathcal R_B\) are \(9,5,3\) and \(Q_B\) is identically zero on that radical. At rank three the radical dimension is zero in odd characteristic, while in characteristic two \(\mathcal R_B=\mathbb F_q B^{\mathsf T}\).

Define
\[
N_1=\frac{(q^3-1)^2}{q-1},\qquad
N_2=q(q+1)(q^3-1)^2,\qquad
N_3=(q^3-1)(q^3-q)(q^3-q^2).
\]
For complex convolution by \(\mathbf1_{\Gamma_q}\) on the group \(V\times V\), the exact operator rank is
\[
\operatorname{rank}T_{\Gamma_q}=
\begin{cases}
1+N_1q^4+N_2q^6+N_3q^9,&q\text{ odd},\\
1+N_1q^4+N_2q^6+N_3q^8,&q\text{ even}.
\end{cases}
\]
The nullity is \(q^{18}-\operatorname{rank}T_{\Gamma_q}\). For increasing odd field orders its normalized rank tends to one; for increasing powers of two its normalized rank is asymptotic to \(q^{-1}\).

## Assumptions and scope
Fix the canonical nontrivial additive character \(\psi(u)=\exp(2\pi i\operatorname{Tr}_{\mathbb F_q/\mathbb F_p}(u)/p)\), where \(p\) is the characteristic, and the coordinate pairing \(\langle A,X\rangle=\sum_{i,j}A_{ij}X_{ij}\). Define the unnormalized coefficient
\[
F(A,B)=\sum_{X\in V}\psi\left(\langle A,X\rangle+\langle B,\operatorname{adj}X\rangle\right).
\]
The rank and support assertions hold for all prime powers \(q\ge2\), including nonprime finite fields; no genericity assumption is imposed on \(A\) or \(B\). A matrix adjugate is the transpose of its cofactor matrix, including for singular matrices. The characteristic-two condition is stated for this canonical character; changing the nontrivial additive character changes the affine square-root factor.

## Proof
**1. Reduction to the rank of \(B\).** Under invertible matrices \(U,W\), the polynomial identity \(\operatorname{adj}(UYW)=\det(U)\det(W)W^{-1}\operatorname{adj}(Y)U^{-1}\) holds even at singular \(Y\). Thus \(Q_B(UYW)=Q_{B'}(Y)\), where \(B'=\det(U)\det(W)W^{-\mathsf T} B U^{-\mathsf T}\). This realizes invertible left/right transformations of \(B\) (up to a nonzero scalar), so its polarization rank and radical dimension may be calculated with \(B=\operatorname{diag}(b_1,b_2,b_3)\) of the same matrix rank. The induced transformation of the first-frequency matrix is invertible and preserves the support count.

**2. Radical calculation.** For diagonal \(B\), with entries of \(X\) denoted \(x_{ij}\),
\[
Q_B(X)=b_1(x_{22}x_{33}-x_{23}x_{32})+b_2(x_{11}x_{33}-x_{13}x_{31})+b_3(x_{11}x_{22}-x_{12}x_{21}).
\]
Each nonzero \(b_i\) contributes an off-diagonal hyperbolic plane. The diagonal three-coordinate polarization matrix is
\[
\begin{pmatrix}0&b_3&b_2\\b_3&0&b_1\\b_2&b_1&0\end{pmatrix},
\]
whose determinant is \(2b_1b_2b_3\). Counting the off-diagonal planes and the diagonal block gives polarization ranks \(0,4,6,9\) for ranks \(r=0,1,2,3\) when \(q\) is odd, and \(0,4,6,8\) when \(q\) is even. Accordingly the radical dimensions are \(9,5,3,0\) and \(9,5,3,1\). Inspecting the free coordinates in the displayed quadratic formula gives \(Q_B|_{\mathcal R_B}=0\) for ranks at most two. At rank three in characteristic two, the diagonal radical is spanned by \((b_1,b_2,b_3)\), which transports back under the invertible changes of coordinates to \(\mathbb F_q B^{\mathsf T}\). For \(Z=tB^{\mathsf T}\), the cofactor identity \(B^{\mathsf T}\operatorname{adj}(B^{\mathsf T})=(\det B)I\) yields
\[
Q_B(Z)=3t^2\det B=t^2\det B
\]
in characteristic two. This proves all radical assertions.

**3. Quadratic character-sum lemma and the exact zero criterion.** For a quadratic form \(Q\) on \(\mathbb F_q^n\), a linear form \(\ell\), and the radical \(\mathcal R\) of the polar form \(P\), let \(S=\sum_x\psi(Q(x)+\ell(x))\). Translating by \(z\in\mathcal R\) shows that \(S=0\) unless \(\psi(Q(z)+\ell(z))=1\) for all \(z\in\mathcal R\). This condition is sufficient: orthogonality and the identity
\[
|S|^2=\sum_{z}\psi(Q(z)+\ell(z))\sum_y\psi(P(y,z))
\]
give \(|S|^2=q^n\sum_{z\in\mathcal R}\psi(Q(z)+\ell(z))=q^{n+\dim\mathcal R}\) under that condition. In odd characteristic, at ranks at most two, this requires \(\ell=0\) on \(\mathcal R\), while at rank three the radical is zero. In characteristic two at rank three, write \(z=tB^{\mathsf T}\), so \(Q_B(z)+\langle A,z\rangle=t^2\det B+t\operatorname{tr}(AB)\). Since \(\operatorname{Tr}(c t^2)=\operatorname{Tr}(c^{q/2}t)\) for all \(c,t\in\mathbb F_q\), the character is trivial in \(t\) if and only if \(\operatorname{tr}(AB)=(\det B)^{q/2}\). The absolute values from \(|S|^2=q^{9+\dim\mathcal R}\) are those in the table. This covers all characters and all frequencies, not only sampled ones.

**4. Count and convolution rank.** For \(0\le r\le3\), the number \(N_r\) of rank-\(r\) matrices in \(M_3(\mathbb F_q)\) is
\[
N_r=\frac{\prod_{j=0}^{r-1}(q^3-q^j)^2}{\prod_{j=0}^{r-1}(q^r-q^j)}
\]
with the empty product interpreted as one. Simplifying for \(r=1,2,3\) yields the displayed \(N_1,N_2,N_3\). Every fixed \(B\) of rank \(r\) contributes the number of nonzero Fourier multipliers in the table. Because the complex characters form a basis of the functions on \(V\times V\), convolution by \(\mathbf1_{\Gamma_q}\) is diagonal with entries \(F(A,B)\), giving the rank formula and nullity. The asymptotics follow from \(N_3/q^9\to1\) and the lower-rank terms: for odd \(q\), \(N_3q^9/q^{18}\to1\); for even \(q\), \(N_3q^8/q^{18}\sim q^{-1}\).

## Verification
A standalone exact checker, `check_adjugate_graph.py`, accompanies the result. Over \(\mathbb F_2\) it evaluates every one of the \(2^{18}=262144\) Fourier coefficients with an integer Walsh–Hadamard transform and confirms all zero/nonzero decisions and magnitudes. The count is \(62609\) nonzero and \(199535\) zero coefficients. Over \(\mathbb F_3\) it verifies polarization ranks for canonical and noncanonical frequency matrices and evaluates \(221\) frequency pairs by exact three-class cyclotomic counts, checking squared complex magnitudes without floating point error. The algebraic proof, rather than these finite checks, covers all prime powers.

For illustration, the convolution ranks are \(62609\) at \(q=2\), \(227020483\) at \(q=3\), and \(12216331009\) at \(q=4\).

## Relationship to prior work
Quadratic Gauss-sum orthogonality and rank-stratified matrix Fourier analysis are established techniques. Gadouleau and Yan (first public preprint 2007-06-12) study rank-metric MacWilliams transforms, which depend on rank weights but do not supply the matrix-adjugate graph's full frequency-dependent Fourier support. Iosevich and Koh (first public preprint 2008-04-28) analyze Fourier restriction to nondegenerate quadratic level sets in odd characteristic, not the nonlinear graph of the \(3\times3\) cofactor map and not characteristic-two affine-radical effects. In the accessible literature and record comparisons, no result explicitly implying the complete formula above was found; this is a bounded-priority assessment, not a proof of historical uniqueness.

## Limitations
No formula is asserted for matrix sizes other than three or for arbitrary finite rings. The claimed exact Fourier magnitudes do not determine all complex phases. The binary full-frequency computation and ternary sampled exact computation are finite checks and do not independently certify the universal algebraic argument. An older quadratic-form specialization or a source inaccessible during the bounded literature search might imply these statements. Independent mathematical review has not occurred.

## References
1. M. Gadouleau and Z. Yan, *MacWilliams Identity for Codes with the Rank Metric*, first public preprint 2007-06-12, arXiv:0706.1751, https://arxiv.org/abs/0706.1751.
2. A. Iosevich and D. Koh, *Extension theorems for the Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, first public preprint 2008-04-28, arXiv:0804.4505, https://arxiv.org/abs/0804.4505.
