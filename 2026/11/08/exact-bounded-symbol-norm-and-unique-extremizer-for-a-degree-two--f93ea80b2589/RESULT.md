# Exact bounded-symbol norm and unique extremizer for a degree-two truncated Toeplitz rank-one operator

## Finding

Let \(0<r<1\), \(\theta_r(z)=(r-z^2)/(1-rz^2)\), and \(K_{\theta_r}=H^2\ominus\theta_r H^2\). Let \(R_0^{\theta_r}\) be the norm-one rank-one truncated Toeplitz operator from the normalized conjugate kernel at zero, defined below. Its infimal bounded-symbol norm is

\[
\boxed{\beta_{\theta_r}(R_0^{\theta_r})=F_r^{-1}},
\qquad v_r=\frac{2r}{1+r^2},
\]
where the **explicit positive definite integral** is
\[
F_r=\frac{1}{2\pi}\int_0^{2\pi}
\frac{1-r^2}{1+r^2-2r\cos u}
\sqrt{1+v_r^2-2v_r\cos u}\,du.
\]

Moreover the infimum is attained by **exactly one** bounded symbol, modulo boundary null sets. The symbol is continuous and has constant modulus:
\[
\boxed{\varphi_r(e^{ix})=-\frac{e^{-ix}-v_r e^{ix}}
{F_r\,|e^{ix}-v_r e^{-ix}|}}.
\]
In particular, \(\|\varphi_r\|_\infty=F_r^{-1}\), and \(A_{\varphi_r}^{\theta_r}=R_0^{\theta_r}\).

The key exact geometric identity is that the Euclidean spatial median of the probability measure with Poisson density \(P_r(e^{iu})=(1-r^2)/|1-re^{iu}|^2\) on the unit circle is the real point \(v_r=2r/(1+r^2)\). Equivalently, \(F_r=\min_{c\in\mathbb C}\int_{\mathbb T}|z-c|P_r(z)\,dm(z)\), and the minimizer is unique.

## Assumptions and scope

The Hardy space \(H^2\) is over the complex unit disk and \(dm(e^{ix})=dx/(2\pi)\) on its boundary. Inner products are linear in the first variable, and \((u\otimes v)f=\langle f,v\rangle u\). The model space has the orthonormal basis
\[
e_0(z)=\frac{\sqrt{1-r^2}}{1-rz^2},\qquad e_1(z)=ze_0(z).
\]
Write \(A_\varphi^{\theta_r}f=P_{K_{\theta_r}}(\varphi f)\) for bounded \(\varphi\in L^\infty(\mathbb T)\). The normalized rank-one operator is
\[
R_0^{\theta_r}=
\frac{\widetilde{k}_0^{\theta_r}\otimes k_0^{\theta_r}}
{\|k_0^{\theta_r}\|_2^2}=-e_1\otimes e_0,
\quad k_0^{\theta_r}=1-r\theta_r,
\quad \widetilde{k}_0^{\theta_r}=\frac{\theta_r(z)-r}{z}.
\]
The infimal bounded-symbol norm is
\[
\beta_{\theta_r}(R_0^{\theta_r})
=\inf\{\|\varphi\|_\infty:A_\varphi^{\theta_r}=R_0^{\theta_r}\}.
\]
The statement is for all real \(r\) strictly between zero and one, and asserts no classification of general inner functions or unrelated truncated Toeplitz operators.

## Proof

**1. Matrix reduction.** Put \(z=e^{ix}\) and
\[
w_r(z)=|e_0(z)|^2=\frac{1-r^2}{|1-rz^2|^2}.
\]
The weight is positive, integrates to one, and obeys \(w_r(-z)=w_r(z)\). Define \(m_j(\varphi)=\int_{\mathbb T}\varphi(z)z^{-j}w_r(z)\,dm(z)\). In the ordered basis \((e_0,e_1)\), direct inner products give
\[
[A_\varphi^{\theta_r}]=
\begin{pmatrix}m_0(\varphi)&m_1(\varphi)\\m_{-1}(\varphi)&m_0(\varphi)\end{pmatrix}.
\]
Since \([R_0^{\theta_r}]=\begin{psmallmatrix}0&0\\-1&0\end{psmallmatrix}\), the symbol conditions are exactly
\[
m_0(\varphi)=m_1(\varphi)=0,\qquad m_{-1}(\varphi)=-1.
\tag{1}
\]

**2. An exact weighted-circle median.** Define the continuous strictly convex function
\[
H_r(c)=\int_{\mathbb T}|z-c|P_r(z)\,dm(z),
\quad P_r(z)=\frac{1-r^2}{|1-rz|^2},\quad c\in\mathbb C.
\]
Strict convexity follows from strictness in the Euclidean triangle inequality off the affine line joining two proposed centers: the positive-density circle measure assigns that line measure zero. Coercivity gives existence and hence uniqueness of a minimizer; invariance of \(P_r\) under conjugation forces the minimizer to be real.

For any real \(v\) in \((-1,1)\), differentiation under the integral gives
\[
H_r'(v)=\int_{-\pi}^\pi
\frac{v-\cos u}{\sqrt{1+v^2-2v\cos u}}
P_r(e^{iu})\,\frac{du}{2\pi}.
\]
Put \(a=(1-r)/(1+r)\), so that \(0<a<1\) and \(v_r=(1-a^2)/(1+a^2)\). The half-angle substitution \(t=\tan(u/2)\) transforms the derivative into
\[
H_r'(v_r)=\frac{2a}{\pi}\int_0^\infty
\frac{t^2-a^2}{(t^2+a^2)\sqrt{(t^2+1)(t^2+a^4)}}\,dt.
\tag{2}
\]
This absolutely convergent integral equals zero: substitution \(t\mapsto a^2/t\) maps the differential-integrand product to its negative. The derivative therefore vanishes at \(v_r\). By strict convexity, \(v_r\) is the unique global minimizer on \(\mathbb C\). Since \(v_r<1\), the complex first-order optimality equation is
\[
\int_{\mathbb T}\frac{\overline{z-v_r}}{|z-v_r|}
P_r(z)\,dm(z)=0.
\tag{3}
\]
In particular, \(F_r=H_r(v_r)>0\).

**3. Exact dual bound.** On \(\mathbb T\), let \(g_r(z)=z-v_r z^{-1}\), so \(|g_r(z)|=|z^2-v_r|>0\). The map \(z\mapsto z^2\) carries the measure \(w_r(z)dm(z)\) to \(P_r(z)dm(z)\); hence
\[
\int_{\mathbb T}|g_r|w_r\,dm=F_r.
\tag{4}
\]
For any representing symbol satisfying (1),
\[
-1=\int\varphi(z)g_r(z)w_r(z)\,dm(z),
\]
because \(\int\varphi z w_r=-1\) while \(\int\varphi z^{-1} w_r=0\). Consequently \(1\le\|\varphi\|_\infty F_r\), proving \(\beta_{\theta_r}(R_0^{\theta_r})\ge F_r^{-1}\).

**4. Attainment and uniqueness.** Define \(\varphi_r=-\overline{g_r}/(F_r|g_r|)\) on the circle. Equation (4) gives \(\int\varphi_r g_r w_r=-1\). The equation (3), after the pushforward \(z\mapsto z^2\), becomes
\[
\int\varphi_r(z)z^{-1}w_r(z)\,dm(z)=0.
\]
It follows that \(\int\varphi_r z w_r=-1\). The identity \(\varphi_r(-z)=-\varphi_r(z)\), together with evenness of \(w_r\), gives \(\int\varphi_r w_r=0\). These are all three conditions (1). Hence the continuous \(\varphi_r\) represents the rank-one operator and has uniform modulus \(1/F_r\).

If some other bounded representing symbol has the same optimal norm, equality must hold in the preceding integral triangle inequality and \(L^\infty\)-\(L^1\) inequality. Because \(w_r>0\) and \(|g_r|>0\) everywhere, the only equality case with integral equal to \(-1\) is
\[
\varphi(z)g_r(z)=-\frac{|g_r(z)|}{F_r}\qquad\text{almost everywhere}.
\]
Thus \(\varphi=\varphi_r\) almost everywhere. This proves both exactness and unique attainment.

## Verification

All analytic steps are exact, including the half-angle substitution, involutive cancellation in (2), the three compression moments, and the equality case. A standalone standard-library Python script `CHECK.py` computes periodic trapezoidal approximations for seven values of \(r\) and checks the target matrix moments and constant symbol modulus. For example, at \(r=1/2\), numerical quadrature gives \(F_r^{-1}\approx 1.312078501\). These finite quadratures are diagnostics, **not** a proof of optimality or uniqueness.

Reproduction: run `python3 CHECK.py` with Python 3, no third-party dependencies. The script uses 32,768 midpoint quadrature nodes in each test and reports 28 grouped assertions.

## Relationship to prior work

Pan Ma, *Bounded Symbols and One-Component Inner Functions* (2026), Proposition 6.1, introduced exactly this degree-two family and determined two explicit **unequal** bounds and the sharp logarithmic asymptotic for \(\beta_{\theta_r}(R_0^{\theta_r})\), not its exact value or an optimal symbol for each parameter. Its compression matrix, basis, and rank-one normalization are acknowledged and reused here. The present result resolves the finite-parameter quotient minimization, gives the uniquely norm-minimizing symbol, and identifies a closed-form location for the weighted-circle geometric median. Classical bounded-symbol and factorization results provide the general background but do not, in the compared material, state this exact parameter formula.

## Limitations

The result is restricted to the origin rank-one operator for the real one-parameter degree-two Blaschke family. The scalar one-dimensional integral is explicit, but no claim is made that it simplifies to elementary or classical special functions. It does not optimize all rank-one kernels or arbitrary degrees. Publication-priority assessment is limited to sources actually inspected; general duality and circle-median results may yield alternative proofs or implicit deductions. This statement has not undergone independent mathematical validation.

## References

1. Pan Ma, *Bounded Symbols and One-Component Inner Functions*, arXiv:2610.28417v1 (first posted 2026-10-20), especially §6 and Proposition 6.1. https://arxiv.org/abs/2610.28417
2. A. Baranov, I. Chalendar, E. Fricain, J. Mashreghi, D. Timotin, *Bounded symbols and reproducing kernel thesis for truncated Toeplitz operators*, arXiv:0909.0131 and J. Funct. Anal. 259 (2010), 2673–2701. https://arxiv.org/abs/0909.0131
3. A. Baranov, R. Bessonov, V. Kapustin, *Symbols of truncated Toeplitz operators*, arXiv:1009.5123 and J. Funct. Anal. 261 (2011), 3437–3456. https://arxiv.org/abs/1009.5123
