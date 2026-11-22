# Certified leading covariance eigenvalue for a characterization-based uniformity test

## Finding
Consider the characterization-based uniformity statistic of Ebner, Liebenberg and Visagie [1], under independent observations from a fully specified continuous null. Let \(\mathcal K\) be its limiting Gaussian covariance operator on \(L^2(0,1)\), and write \(\lambda_1=\|\mathcal K\|_{\mathrm{op}}\). Then the following *strict, exact-rationally certified* enclosure holds:

\[
\boxed{0.11573423652792<\lambda_1<0.11573423652794.}
\]

In particular the largest eigenvalue is simple. If \(T_\infty=\sum_{j\ge1}\lambda_j Z_j^2\) denotes the simple-null limit of the statistic, with independent standard normal \(Z_j\), then its sharp logarithmic right-tail constant is

\[
\lim_{x\to\infty}\frac{1}{x}\log\Pr(T_\infty>x)=-\frac{1}{2\lambda_1},
\qquad \frac{1}{2\lambda_1}=4.32024278208\ldots.
\]

The numerical enclosure is a certified evaluation of a natural eigenvalue, **not** a claim of an elementary closed form.

## Assumptions and scope
Let \(U_1,U_2,\ldots\) be independent and uniform on \((0,1)\). The published statistic is

\[
T_n=n\int_0^1\left[\frac1n\sum_{i=1}^n(2U_i-1)\mathbf{1}_{\{U_i\ge t\}}-t(1-t)\right]^2dt.
\]

Its established weak limit [1] is \(T_\infty=\|Z\|_{L^2(0,1)}^2\), with mean-zero Gaussian \(Z\) and continuous covariance kernel

\[
K(s,t)=\frac{1-(2\max(s,t)-1)^3}{6}-s(1-s)t(1-t),\qquad 0\le s,t\le1.
\]

Define \((\mathcal Kf)(s)=\int_0^1K(s,t)f(t)\,dt\). This is a compact, positive, trace-class, self-adjoint operator. Let its eigenvalues be \(\lambda_1\ge\lambda_2\ge\cdots\ge0\), counting multiplicity.

## Proof
Put \(w(u)=(2u-1)^2\) and \(a(u)=u(1-u)\). Fubini's theorem gives the **exact polynomial-preserving action**

\[
(\mathcal Kf)(s)=\int_s^1w(u)\left(\int_0^u f(t)\,dt\right)du-a(s)\int_0^1a(t)f(t)\,dt.\tag{1}
\]

The kernel is the covariance of \((2U-1)\mathbf{1}_{\{U\ge t\}}-a(t)\) under uniform \(U\), so positivity and trace class follow from square integrability of this random \(L^2\)-valued function.

For completeness, compute the Hilbert–Schmidt trace independently. Writing \(\mathcal K=\mathcal K_0-a\otimes a\), where \(K_0(s,t)=\int_{\max(s,t)}^1w(u)du\), direct polynomial integration yields

\[
\operatorname{tr}(\mathcal K_0^2)=2\int_0^1w(v)\int_0^vw(u)u^2\,du\,dv=\frac{13}{630},
\]
\[
\langle a,\mathcal K_0a\rangle=\int_0^1w(u)\left(\int_0^ua(t)dt\right)^2du=\frac{47}{11340},
\qquad \|a\|_2^2=\frac1{30}.
\]

Consequently,

\[
H:=\operatorname{tr}(\mathcal K^2)=\frac{13}{630}-2\frac{47}{11340}+\frac1{900}=\frac{109}{8100}.
\tag{2}
\]

Define polynomials \(f_0(s)=1\) and \(f_{k+1}=\mathcal Kf_k\) for \(0\le k\le5\), using (1). Set \(f=f_5\), \(g=f_6=\mathcal Kf\), and define exact rational numbers

\[
q=\frac{\langle f,g\rangle}{\langle f,f\rangle},\qquad
r^2=\frac{\langle g,g\rangle}{\langle f,f\rangle}-q^2.
\tag{3}
\]

Because (1) maps rational polynomials to rational polynomials, (2) and (3) are finite rational computations. The attached standard-library verifier implements rational polynomial multiplication, integration and the six iterations; it establishes, by exact integer comparisons,

\[
0.11573423652792<q,\quad q>\frac1{100},\quad
0<H-q^2<\frac1{10000},\quad
q+\frac{r^2}{q-1/100}<0.11573423652794.\tag{4}
\]

The Rayleigh variational principle yields \(\lambda_1\ge q\). Since \(\sum_j\lambda_j^2=H\),

\[
\lambda_2^2\le H-\lambda_1^2\le H-q^2<\frac1{10000}.
\]

Thus \(\lambda_2<b:=1/100<q\), which also proves simplicity of the top eigenvalue. To give the elementary Temple bound, expand the normalized \(f\) in an orthonormal eigenbasis, with spectral weights \(p_j\). Since \((\lambda_j-\lambda_1)(\lambda_j-b)\ge0\) for every \(j\ge2\) and the first factor vanishes for \(j=1\),

\[
0\le\sum_jp_j(\lambda_j-\lambda_1)(\lambda_j-b)
=r^2-(\lambda_1-q)(q-b).
\]

Hence \(\lambda_1\le q+r^2/(q-b)\). Combining this with (4) proves the announced strict enclosure. No computed finite-dimensional eigenvalue is taken as an exact infinite-dimensional eigenvalue.

Finally, \(T_\infty=\sum_j\lambda_jZ_j^2\) because \(\mathcal K\) is positive trace class. The lower bound \(\Pr(T_\infty>x)\ge\Pr(\lambda_1Z_1^2>x)\) gives one logarithmic-tail inequality. For every \(h<1/(2\lambda_1)\), the Laplace transform \(\mathbb E e^{hT_\infty}=\prod_j(1-2h\lambda_j)^{-1/2}\) is finite by trace class; Chernoff's inequality, followed by \(h\uparrow1/(2\lambda_1)\), gives the reverse inequality.

## Verification
Run `python3 verify_bounds.py` using Python 3's standard library. The verifier constructs the degree-20 polynomial \(f_5\) and degree-24 polynomial \(f_6\), confirms the three rational integrals in (2), and proves all strict inequalities in (4) using `fractions.Fraction`. It reports the approximate Rayleigh quotient \(0.115734236527925\), residual variance \(4.59375659577\times10^{-16}\) and conservative Temple upper value \(0.11573423652792934\). These decimals are descriptive only; all assertions use exact rationals. An independent floating-point Nyström calculation is useful as a diagnostic but is not part of the proof.

## Relationship to prior work
Ebner, Liebenberg and Visagie [1, Theorem 2.1 and Section 6] proved the Gaussian covariance limit and calculated its first four cumulants. Section 6 explicitly notes that the largest eigenvalue needed for local Bahadur-slope approximations had not been explicitly calculated. This note retains their covariance kernel, derives an exact polynomial power recursion and supplies a rigorously verified narrow interval for that specific missing value. The Rayleigh variational principle and Temple bound are classical tools, not claimed as new methods. The improvement lies in their exact implementation and strong enclosure for this particular open model-specific invariant.

## Limitations
The result is restricted to the simple, fully specified continuous null; no assertion is made for composite hypotheses with fitted parameters. It does not give closed-form eigenfunctions, exact finite-sample quantiles, a complete spectrum, or a finite-sample significance correction. The logarithmic tail concerns the asymptotic null law; any specific alternative's Bahadur slope additionally depends on its population discrepancy. Numerical enclosure and literature comparison do not independently certify historical priority.

## References
[1] B. Ebner, S. Liebenberg and I. J. H. Visagie, *A new omnibus test of fit based on a characterisation of the uniform distribution*, arXiv:2108.06391v1, first posted 13 August 2021, https://arxiv.org/abs/2108.06391 ; published in *Statistics*, 56(6), 1364–1384 (2022), https://doi.org/10.1080/02331888.2022.2133121 .
