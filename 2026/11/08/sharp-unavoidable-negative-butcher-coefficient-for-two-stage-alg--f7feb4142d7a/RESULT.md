# Sharp unavoidable negative Butcher coefficient for two-stage algebraically stable third-order Runge–Kutta rules

## Finding
Let \(A=(a_{ij})\in\mathbb R^{2\times2}\) and \(b\in\mathbb R^2\) define a real two-stage Runge–Kutta method with classical order at least three, positive weights, and algebraic stability. Assume both stage abscissas lie in the normalized step interval \([0,1]\). Define the negative-entry size \(\nu(A)=\max_{i,j}\max\{0,-a_{ij}\}\).

After sorting stages by abscissa, put \(b=(p,1-p)^T\). There is a **unique** \(p_*\in(1/4,3/4)\) with
\[
p_*^3(1-p_*)=\frac1{12},\qquad p_*\simeq0.5861069554217853.
\]
Then the exact sharp minimax value is
\[
\boxed{\inf\nu(A)=\delta_*:=\sqrt{\frac{1-p_*}{12p_*}}-\frac{1-p_*}{2}\simeq0.0356390699388833.}
\]
The infimum is attained by exactly one two-stage tableau up to simultaneous permutation of stages, and the attaining tableau is symplectic. In every admissible tableau with the abscissas sorted, \(a_{12}\le-\delta_*\).

## Assumptions and scope
Write \(e=(1,1)^T\), \(c=Ae\), \(B=\operatorname{diag}(b)\). Assume \(b_i>0\), \(0\le c_1<c_2\le1\), and the four order conditions
\[
b^Te=1,\qquad b^Tc=\frac12,\qquad b^T(c\circ c)=\frac13,\qquad b^TAc=\frac16.
\]
Algebraic stability means \(M=BA+A^TB-bb^T\succeq0\). Equality of abscissas is ruled out by the positive second central moment \(b^T(c\circ c)-(b^Tc)^2=1/12\). Stage permutations do not change the conditions or \(\nu(A)\). Two is the smallest stage count capable of classical order three: a one-stage rule would require simultaneously \(c=1/2\) and \(c^2=1/3\). No assumption of diagonal implicitness, stiff accuracy, or positive Butcher entries is made.

## Proof
**1. Two-point moment representation.** With \(b=(p,q)^T\), \(q=1-p\), positivity implies \(0<p<1\). The first three order conditions give exactly
\[
c_1=\frac12-\sqrt{\frac{q}{12p}},\qquad c_2=\frac12+\sqrt{\frac{p}{12q}}.
\]
Indeed the weighted mean is \(1/2\), weighted variance \(1/12\), and the larger abscissa is \(c_2\). Thus \(0\le c_1<c_2\le1\) is equivalent to \(1/4\le p\le3/4\).

**2. A forced negative entry.** Since the first diagonal entry of the positive-semidefinite algebraic-stability matrix is nonnegative,
\[
M_{11}=2pa_{11}-p^2\ge0,\qquad a_{11}\ge\frac p2.
\]
The first row sum is \(a_{11}+a_{12}=c_1\), hence
\[
a_{12}\le c_1-\frac p2=-f(p),\qquad f(p):=\sqrt{\frac{1-p}{12p}}-\frac{1-p}{2}.
\]
For \(p\in[1/4,3/4]\), \(f(p)>0\), because \(3p(1-p)<1\). Consequently \(\nu(A)\ge f(p)\).

**3. Global minimization.** Direct differentiation gives
\[
f'(p)=\frac12-\frac{1}{4\sqrt3\,p^{3/2}\sqrt{1-p}}.
\]
The function \(p^3(1-p)\) is strictly increasing over \([1/4,3/4]\). Its values at the endpoints straddle \(1/12\), so \(f'\) changes sign exactly once, from negative to positive, at \(p_*\). Thus \(f(p)\ge f(p_*)=\delta_*\), with equality only at \(p=p_*\). This proves the universal lower bound.

**4. Sharpness and classification.** For any \(p\in[1/4,3/4]\), define \(q=1-p\), the abscissas as in step 1, and set
\[
A_p=\begin{pmatrix}
 p/2&c_1-p/2\\
 c_2-q/2&q/2
\end{pmatrix},\qquad b_p=\begin{pmatrix}p\\q\end{pmatrix}.
\]
Both row sums equal the stated abscissas. By the first two moment equations,
\[
2p(a_p)_{11}-p^2=0,\quad 2q(a_p)_{22}-q^2=0,\quad
p(a_p)_{12}+q(a_p)_{21}-pq=0,
\]
so \(M=0\) exactly: the tableau is algebraically stable and symplectic. Also \(A_p^Tb_p=b_p-B_pc\), whence
\[
b_p^TA_pc=(A_p^Tb_p)^Tc=\frac12-\frac13=\frac16.
\]
Thus it has order at least three. The only negative entry of \(A_p\) is the upper-right one: the diagonal entries are strictly positive and \(c_2-q/2>0\). Therefore \(\nu(A_{p_*})=f(p_*)=\delta_*\).

Finally equality in the universal bound forces \(p=p_*\), \(a_{11}=p_*/2\), and \(M_{11}=0\). A positive-semidefinite matrix with a zero diagonal entry has zero corresponding row, so \(M_{12}=0\). Also \(e^TMe=2b^Tc-(b^Te)^2=0\); positive semidefiniteness then forces \(Me=0\), hence \(M_{22}=0\). This fixes \(a_{22}=q/2\), and both row-sum constraints fix the off-diagonal entries. The unique minimizer, up to stage relabeling, is \(A_{p_*}\).

## Verification
The standalone `verify.py` requires only the Python standard library. Run `python verify.py`. It checks the full order-three tableau identities and \(M=0\) with exact rational arithmetic for six nontrivial choices of abscissas, brackets the critical quartic root by exact rational inequalities, and checks 1,500 supplementary sampled weight choices against the bound. These finite checks corroborate but do not replace the all-parameter proof above. A numerical evaluation gives \(p_*\simeq0.5861069554217853\), \(\delta_*\simeq0.0356390699388833\).

## Relationship to prior work
Yu, Zhu and Weng (arXiv:2610.37425v1, first submitted 2026-10-27) determine optimal positive-coefficient/SSP radii at second and third order by a phase-type representation. The present problem instead enforces algebraic stability, and measures the least unavoidable *negative Butcher entry* with two normalized stages. These are different optimization criteria; the paper's SSP-optimal tableau is not asserted to attain our bound. Earlier Ketcheson–Macdonald–Gottlieb work establishes how negative coefficients obstruct positive-radius SSP. Gottlieb and collaborators (arXiv:2611.07981v1, posted 2026-11-05) give a general *qualitative* incompatibility between third-order nonnegative coefficients and algebraic stability; their inspected Section 5 does not give this normalized two-stage sharp coefficient, optimizer or uniqueness. Its general impossibility statement is not claimed as new here.

## Limitations
The value depends on restricting to exactly two stages and requiring both stage times in \([0,1]\), along with positive weights. It does not give a universal lower bound for arbitrary stage count, or a positive SSP coefficient for the attaining tableau. It is an exact-arithmetic coefficient optimization, not an error, step-size or stiffness performance guarantee. The precise extremal formula was not found in inspected related sources, but equivalent unindexed calculations may exist.

## References
1. Z. Weng, H. Yu, Q. Zhu, *Phase-type representations for Strong Stability Preserving Runge–Kutta methods*, arXiv:2610.37425v1 (2026-10-27), https://arxiv.org/html/2610.37425v1 .
2. D. I. Ketcheson, C. B. Macdonald, S. Gottlieb, *Optimal Implicit Strong Stability Preserving Runge–Kutta Methods*, 2007 preprint, https://www.cfm.brown.edu/people/sg/implicitSSP.pdf .
3. S. Gottlieb et al., *A stability order barrier and SSP bound for Runge–Kutta methods with non-negative coefficients*, arXiv:2611.07981v1 (2026-11-05), Section 5, https://arxiv.org/html/2611.07981v1 .
