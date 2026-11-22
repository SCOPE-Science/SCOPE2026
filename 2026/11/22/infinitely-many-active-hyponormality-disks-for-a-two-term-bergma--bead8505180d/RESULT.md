# Infinitely many active hyponormality disks for a two-term Bergman Toeplitz symbol

## Finding

For the analytic Bergman space of the unit disk with normalized area measure, consider the Toeplitz operator with bounded nonharmonic symbol \(\varphi_\lambda(z)=z+\lambda z^2\overline z=z(1+\lambda|z|^2)\), where \(\lambda\in\mathbb C\). Put \(x=\operatorname{Re}\lambda\) and \(y=|\lambda|^2\), and for integers \(k\ge0\) define

\[
\begin{aligned}
A_k&=(k+3)(k+4)^2,\\
B_k&=4(k+2)(k+3)(k+4),\\
C_k&=(k+2)^2(3k+11),\\
L_k(x)&=-\frac{A_k+B_kx}{C_k}.
\end{aligned}
\]

**Complete classification.** The operator \(T_{\varphi_\lambda}\) is hyponormal if and only if \(y\ge F(x)\), where \(F(x)=\sup_{k\ge0}L_k(x)\). Unlike a generic infinite family of tests, this supremum is explicitly localized by the strictly increasing rational switching abscissae

\[
X_k=-\frac{5k^3+54k^2+187k+206}{8(k+2)(k+3)(k+4)},\qquad k\ge0.
\]

Indeed \(X_0=-103/96\), \(X_k\nearrow-5/8\), and

\[
F(x)=\begin{cases}
L_0(x),&x\le X_0,\\
L_k(x),&X_{k-1}\le x\le X_k,\quad k\ge1,\\
-(1+4x)/3,&x\ge-5/8.
\end{cases}
\]

The overlapping formulas coincide at their common endpoints. In the final regime the displayed value is the supremum of the finite-index lines, not necessarily a finite-index maximum.

Equivalently, the **nonhyponormal parameter locus** is the union of the open disks

\[
\bigcup_{k\ge0}\left\{\lambda\in\mathbb C:\left|\lambda+\frac{2(k+3)(k+4)}{(k+2)(3k+11)}\right|<\frac{(k+4)\sqrt{(k+1)(k+3)}}{(k+2)(3k+11)}\right\}.
\]

Every disk contributes a nonempty exposed circular arc to the boundary of this union: its consecutive crossings occur at \(\lambda=X_k\pm i\sqrt{Y_k-X_k^2}\), where \(Y_k=(k+5)/(2(k+2))>X_k^2\). The infinitely many corners of the upper and lower boundary arcs accumulate at the two nonreal points \(-5/8\pm i\sqrt7/8\). On the real line the answer collapses to the exact reentrant classification

\[
T_{\varphi_t}\text{ hyponormal for real }t
\quad\Longleftrightarrow\quad
 t\le-\frac{12+2\sqrt3}{11}\quad\text{or}\quad t\ge-\frac13.
\]

## Assumptions and scope

The Hilbert space is \(A^2(\mathbb D)\) with normalized planar area measure \(dA\); the orthonormal basis is \(e_n(z)=\sqrt{n+1}\,z^n\), for \(n\in\mathbb N_0\). Toeplitz means \(T_\varphi f=P(\varphi f)\), where \(P\) is the Bergman orthogonal projection. Hyponormality means \(T^*T-TT^*\succeq0\). The parameter \(\lambda\) is arbitrary in \(\mathbb C\), with no smallness assumption. Disk boundaries are included in the hyponormal locus when all other inequalities hold. No weighted-area exponents other than the unweighted case are asserted.

## Proof

**1. Exact shift reduction.** Bergman orthogonal projection gives \(P(z^{n+2}\overline z)=\frac{n+2}{n+3}z^{n+1}\), hence

\[
T_{\varphi_\lambda}e_n=w_ne_{n+1},\qquad
w_n=\sqrt{\frac{n+1}{n+2}}\left(1+\lambda\frac{n+2}{n+3}\right).
\]

This bounded unilateral weighted shift has self-commutator diagonal entries \(|w_0|^2\) at \(e_0\), and \(|w_{k+1}|^2-|w_k|^2\) at \(e_{k+1}\). A direct subtraction, without dividing by any possibly zero weight, gives

\[
|w_{k+1}|^2-|w_k|^2
=\frac{A_k+B_kx+C_ky}{(k+2)(k+3)^2(k+4)^2}.
\]

All denominators and \(C_k\) are strictly positive. Therefore hyponormality is equivalent to \(y\ge L_k(x)\) for every integer \(k\ge0\), proving the reduction to \(F\).

**2. Solving the infinite upper envelope.** The slopes \(m_k=-B_k/C_k\) strictly increase, since

\[
m_{k+1}-m_k=\frac{16(k+4)^2}{(k+2)(k+3)(3k+11)(3k+14)}>0.
\]

The consecutive lines intersect at \(x=X_k\), with common value \(L_k(X_k)=L_{k+1}(X_k)=Y_k\). Direct subtraction yields

\[
X_{k+1}-X_k=\frac{3(3k+14)}{8(k+2)(k+4)(k+5)}>0,
\qquad \lim_{k\to\infty}X_k=-\frac58.
\]

For arbitrary indices \(j<k\), telescoping the identities \(L_{r+1}(x)-L_r(x)=(m_{r+1}-m_r)(x-X_r)\) shows that \(L_k\) dominates every preceding line for \(x\ge X_{k-1}\); similarly it dominates every following line for \(x\le X_k\). For \(x\ge-5/8\), the sequence of lines increases to \(-(1+4x)/3\). This proves the displayed piecewise formula for every real \(x\), including all endpoints.

**3. Circular disks and exposed switches.** Completing the square in \(A_k+B_k\operatorname{Re}\lambda+C_k|\lambda|^2<0\) yields the stated open disk. The exact discriminant identity

\[
B_k^2-4A_kC_k=4(k+1)(k+2)^2(k+3)(k+4)^2
\]

provides its radius. At every consecutive switch the upper/lower complex boundary points are nonreal because

\[
Y_k-X_k^2=
\frac{7k^6+132k^5+1006k^4+3952k^3+8383k^2+8972k+3644}
{64(k+2)^2(k+3)^2(k+4)^2}>0.
\]

Consequently each finite-index line is the strict maximizing line on a real open interval meeting the set \(F(x)>x^2\); thus every corresponding circle contributes an exposed nondegenerate arc. Their successive intersections produce genuine corners because the adjacent slopes differ strictly. Taking limits \(X_k\to-5/8\) and \(Y_k\to1/2\) gives the two announced accumulation points.

**4. Exact real slice.** Put \(\lambda=t\in\mathbb R\), so \(x=t\) and \(y=t^2\). The cubic numerator has coefficients, in descending powers of \(k\),

\[
(1+t)(1+3t),\quad 11+36t+23t^2,\quad40+104t+56t^2,\quad48+96t+44t^2.
\]

All four coefficients are nonnegative for \(t\ge-1/3\) and for \(t\le-(12+2\sqrt3)/11\), proving sufficiency at every index. Between the latter endpoint and \(-1\), the constant coefficient is negative. For \(-1<t<-1/3\), the leading cubic coefficient is negative, so sufficiently large indices violate positivity. At \(t=-1\) the constant coefficient is negative. Necessity follows, including endpoint equality.

## Verification

The standalone \(\texttt{CHECK.py}\) uses only Python's standard library and verifies, with exact fractions, the weight-difference identity for 80 indices and four coefficient pairs, the consecutive intersection formulas, their strict ordering, the radius discriminant identity, exposed-switch inequalities, and finite real-parameter diagnostics. Run \(\texttt{python3 CHECK.py}\) in the directory containing this document. The test completed with 1,688 passing checks. The proof above establishes the infinite-index statements; the finite checker does not certify them independently.

## Relationship to prior work

Fleeman–Liaw (arXiv:1707.09677, initially public 30 July 2017), Section 4, quotes the Liu–Lu Mellin-transform criterion for fixed-angular-degree Toeplitz operators, gives a broad quarter-plane sufficient condition (Theorem 11), and demonstrates the limitations of its necessity (Example 12). The criterion implies individual index inequalities after substitution, but the inspected text does not identify the exact upper envelope, its infinitely many exposed switches, or this specific real-coefficient reentrance. Kim–Lee (2021 and 2022) give general sufficient and necessary conditions for related two-term polynomial symbols; their inspected same-relative-degree result is a sufficient half-plane condition, not the full complex-parameter phase diagram. Kim–Lee (2023) treats different relative degrees. Le–Simanek (2020) treats a shift plus a diagonal perturbation, not the present sum of two shift terms. Thus the claim is an explicit all-parameter solution and boundary geometry of a natural case beyond qualitative quarter-plane sufficiency, not a claim to invent the weighted-shift/Mellin method.

## Limitations

This theorem concerns one concrete nonharmonic polynomial family on the unweighted Bergman disk. It does not classify higher-degree polynomials, weighted Bergman norms, subnormality, or related spectral invariants. The Liu–Lu 2009 original article was identified through its abstract and through the account in Fleeman–Liaw but was not available for direct full-text inspection; the possibility of an equivalent parameter-envelope classification in that or other unindexed material is a residual priority risk. No independent mathematical audit has been performed.

## References

1. M. Fleeman and C. Liaw, *Hyponormal Toeplitz operators with non-harmonic symbol acting on the Bergman space*, arXiv:1707.09677 (first version 30 July 2017), https://arxiv.org/abs/1707.09677 .
2. C. Liu and Y. Lu, *Commutativity and hyponormality of Toeplitz operators on the weighted Bergman space*, J. Korean Math. Soc. 46 (2009), 621–642, https://doi.org/10.4134/JKMS.2009.46.3.621 .
3. S. Kim and J. Lee, *Hyponormality of Toeplitz operators with non-harmonic symbols on the Bergman spaces*, J. Inequal. Appl. 2021, 67, https://doi.org/10.1186/s13660-021-02602-1 .
4. S. Kim and J. Lee, *Hyponormal Toeplitz operators with non-harmonic symbols on the weighted Bergman spaces*, Ann. Funct. Anal. 14 (2023), article 14 (online 4 December 2022), https://doi.org/10.1007/s43034-022-00241-1 .
5. S. Kim and J. Lee, *Remarks on hyponormal Toeplitz operators with nonharmonic symbols*, Open Math. 21 (2023), article 20230114, https://doi.org/10.1515/math-2023-0114 .
6. T. Le and B. Simanek, *Hyponormal Toeplitz Operators on Weighted Bergman Spaces*, arXiv:2003.07330 (first version 16 March 2020), https://arxiv.org/abs/2003.07330 .
