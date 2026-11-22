# Zero-free Fourier kernels of rank-two matrix balls and a binary square transition

## Finding
Let \(q\) be any prime power, \(n\ge m\ge3\), and \(G=M_{m\times n}(\mathbb F_q)\) with its additive group structure. Let \(C=\{A\in G:\operatorname{rank}A\le2\}\). For a fixed nontrivial additive character \(\psi\) of \(\mathbb F_q\), identify the dual group with \(G\) using \(\chi_B(A)=\psi(\operatorname{tr}(B^{\mathsf T}A))\).

For a frequency matrix \(B\) of rank \(r\), write \(t=m-r\), \(\left[\begin{smallmatrix}a\\b\end{smallmatrix}\right]_q\) for the Gaussian binomial coefficient (zero outside \(0\le b\le a\)), and
\[
 b_m=\left[\begin{smallmatrix}m-1\\1\end{smallmatrix}\right]_q-1=q\left[\begin{smallmatrix}m-2\\1\end{smallmatrix}\right]_q,\qquad
 c_m=b_m\left[\begin{smallmatrix}m\\1\end{smallmatrix}\right]_q-\left[\begin{smallmatrix}m\\2\end{smallmatrix}\right]_q+1
 =\frac{q^3(q^{m-2}-1)(q^{m-1}-1)}{(q-1)^2(q+1)}.
\]
The unnormalized Fourier transform of the ball is exactly
\[
 F_t=\sum_{A\in C}\chi_B(A)
 =q^{2n}\left[\begin{smallmatrix}t\\2\end{smallmatrix}\right]_q
 -b_m q^n\left[\begin{smallmatrix}t\\1\end{smallmatrix}\right]_q+c_m.
\]
Every \(F_t\) is a nonzero integer. Its sign is negative precisely for \(t=1\), with one exception: when \(q=2\), \(n=m\), and \(m\ge5\), the additional shell \(t=2\) is negative. All other rank shells are positive.

Let \(P_C\) be the Fourier projection retaining frequencies in \(C\) on the space of complex functions on \(G\). Put
\[
 N_r=\left[\begin{smallmatrix}m\\r\end{smallmatrix}\right]_q\prod_{i=0}^{r-1}(q^n-q^i),\qquad
 J=\begin{cases}\{1,2\},&q=2,\ n=m\ge5,\\\{1\},&\text{otherwise}.\end{cases}
\]
The exact sharp endpoint norms are
\[
 \boxed{\|P_C\|_{\ell^1(G)\to\ell^1(G)}
 =\|P_C\|_{\ell^\infty(G)\to\ell^\infty(G)}
 =1+\frac{2}{q^{mn}}\sum_{t\in J}N_{m-t}(-F_t).}
\]
Thus convolution by the indicator \(1_C\) is invertible on complex functions on \(G\) for all \(n\ge m\ge3\), including characteristic two. In the exceptional binary square case, writing \(X=2^{m-2}\) gives the explicit extra negative coefficient
\[
 F_2=-\frac83(X^2-6X-1).
\]
For the boundary \(m=2\), \(C=G\); the Fourier transform vanishes at all nonzero dual frequencies, so the zero-free conclusion is not asserted there.

## Assumptions and scope
The field \(\mathbb F_q\) is arbitrary of prime-power order. The integers \(m,n\) satisfy \(3\le m\le n\). The rank is ordinary matrix rank, the pairing is the entrywise trace pairing, and the transform uses no averaging. Endpoint \(\ell^p\) norms are operator norms on counting-measure \(\ell^p(G)\). The Fourier projection uses the usual normalized Fourier coefficients, so its convolution kernel is \(q^{-mn}F_{m-\operatorname{rank}(x)}\). Neither the result nor its proof assumes that \(q\) is prime.

## Proof
**Subspace-incidence Fourier identities.** For \(j=0,1,2\), let \(H_j(B)\) be the sum over all \(j\)-dimensional subspaces \(U\le\mathbb F_q^m\) of the character sums over matrices whose image lies in \(U\). Character orthogonality gives
\[
 H_j(B)=q^{jn}\left[\begin{smallmatrix}m-r\\j\end{smallmatrix}\right]_q.
\]
Indeed, the inner character sum is \(q^{jn}\) exactly when \(U\subseteq\ker(B^{\mathsf T})\), and zero otherwise. If \(K_i(B)\) denotes the Fourier sum over rank-exactly-\(i\) matrices, then
\[
 H_0=K_0=1,\quad
 H_1=\left[\begin{smallmatrix}m\\1\end{smallmatrix}\right]_q+K_1,\quad
 H_2=\left[\begin{smallmatrix}m\\2\end{smallmatrix}\right]_q+
 \left[\begin{smallmatrix}m-1\\1\end{smallmatrix}\right]_q K_1+K_2.
\]
The factors count the \(j\)-subspaces containing an image of dimension \(i\). Eliminating \(K_1,K_2\) from \(F_t=K_0+K_1+K_2\) gives the displayed polynomial and the expression for \(c_m\).

**Sign classification.** For \(m\ge3\), \(b_m,c_m>0\). At \(t=0\), \(F_0=c_m>0\). At \(t=1\), \(F_1=c_m-b_m q^n<0\), because
\[
 \frac{c_m}{b_m}=
 \frac{q^2(q^{m-1}-1)}{q^2-1}<q^m\le q^n.
\]
For \(t\ge2\), use the exact factorization
\[
 F_t=q^n\left[\begin{smallmatrix}t\\1\end{smallmatrix}\right]_q
 \left(\frac{q^n(q^{t-1}-1)}{q^2-1}-b_m\right)+c_m.
\]
For \(t\ge3\), the parenthesis is at least \(q^m-b_m>0\). For \(t=2\), the formula simplifies to
\[
 F_2=q^n\bigl(q^n-(q+1)b_m\bigr)+c_m.
\]
When \(q\ge3\) and \(n\ge m\), the inequality \(q^n>(q+1)b_m\) follows from \(q(q-1)>q+1\). When \(q=2\) and \(n\ge m+1\), it follows from \(2^{m+1}>3(2^{m-1}-2)\). Therefore \(F_2>0\) in these cases. In the remaining binary square case, put \(X=2^{m-2}\). Direct algebra gives \(F_2=-8(X^2-6X-1)/3\), positive at \(X=2,4\) and strictly negative for every \(X\ge8\). It never vanishes: the polynomial has the irrational roots \(3\pm\sqrt{10}\). This establishes every sign and nonvanishing assertion.

**Sharp norms and invertibility.** The Fourier projection has convolution kernel \(k(B)=q^{-mn}F_{m-\operatorname{rank}B}\). Its \(\ell^1\)- and \(\ell^\infty\)-operator norms both equal \(\sum_B|k(B)|\): translation-invariance gives the upper bounds, while a point mass (respectively, a phase-matching bounded function) attains them. There are \(N_r\) matrices of rank \(r\), by choosing their image and a surjective linear map onto it. Since the zero frequency belongs to \(C\), \(\sum_B k(B)=1\). Hence \(\sum_B|k(B)|=1+2\sum_{k(B)<0}(-k(B))\), and the sign theorem yields the claimed finite formula. Finally, the Fourier multiplier of convolution by \(1_C\) is the nowhere-zero function \(F_t\), proving invertibility.

## Verification
The accompanying self-contained `check_rank2.py` independently constructs exact rank-at-most-two indicators and full Walsh transforms on binary \(3\times3\), \(3\times4\), and \(4\times4\) matrix spaces (\(512\), \(4096\), and \(65536\) Fourier values). It checks the rank-stratified polynomial, rank multiplicities, and Parseval's identity. A separate ternary \(3\times3\) enumeration examines all \(19683\) matrices and independently computes four canonical character sums. Exact integer evaluations also check the sign theorem, absence of zeros, rank enumeration, and zero-frequency counts for \(q\in\{2,3,4,5,7,8,9,11,16\}\), \(3\le m\le24\), and \(n\in\{m,m+1,m+2,m+4\}\). Run `python3 check_rank2.py`; success ends in `RANK_TWO_BALL_ALL_EXACT_CHECKS_PASS`. Finite checks support but do not replace the universal proof.

For example, the sharp norms are \(163/16\) for binary \(3\times3\) matrices, \(24137/512\) for binary \(4\times4\) matrices, and \(11059/243\) for ternary \(3\times3\) matrices.

## Relationship to prior work
Delsarte's bilinear-forms association-scheme character table gives general eigenvalues of individual rank relations; its explicit formulas are acknowledged as prior work and imply the unsimplified rank-two ball transform by summation. Gadouleau and Yan's rank-metric MacWilliams analysis gives another generalized Krawtchouk representation. Brouwer, Cioabă, Ihringer, and McGinnis analyze signs and extremal eigenvalues of **individual** distance relations in bilinear-forms graphs. The claim here is the cumulative radius-two ball's complete nonzero **sign-shell classification**, the exceptional binary square transition, and the resulting evaluated sharp endpoint norm. General Krawtchouk formulas alone are not claimed as new.

## Limitations
The classification concerns the radius-two rank ball, not arbitrary higher radii, and provides no universal closed-form inverse-convolution kernel. The exact norm formula is a short Gaussian-binomial expression rather than a single polynomial in all parameters. The 1978 character table is mathematically stronger as an input formula but does not state the sign/zero-free/norm theorem. Independent mathematical validation and exhaustive historical-priority verification have not occurred; other deductions from the classical formulas may exist. The verification program uses only prime fields for direct character-enumeration tests, although the algebraic proof applies to all prime powers.

## References
1. Philippe Delsarte, *Bilinear Forms over a Finite Field, with Applications to Coding Theory*, Journal of Combinatorial Theory, Series A 25 (1978), 226–241, DOI: 10.1016/0097-3165(78)90015-8. Especially Section 3 and Appendix, Theorem A2.
2. Maximilien Gadouleau and Zhiyuan Yan, *Properties of Rank Metric Codes*, arXiv:cs/0702077, first submitted 13 February 2007. Especially Section VI, Corollary 5, and equation (42).
3. Andries E. Brouwer, Sebastian M. Cioabă, Ferdinand Ihringer, and Matt McGinnis, *The smallest eigenvalues of Hamming graphs, Johnson graphs and other distance-regular graphs with classical parameters*, arXiv:1709.09011, first submitted 26 September 2017. Especially Section 7.
