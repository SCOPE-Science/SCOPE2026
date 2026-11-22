# Cubic stretched-exponential norm correction for Blaschke composition on weighted Hardy spaces

## Finding

Fix \(0<\lambda<1\) and \(2/3<\theta<1\). Write
\[
b_\lambda(z)=\frac{z-\lambda}{1-\lambda z},\qquad
U=\frac{1+\lambda}{1-\lambda},\qquad
c=\frac{\lambda(1+\lambda)}{12(1-\lambda)^3}=\frac{U(U^2-1)}{48}.
\]
In the coefficient-weighted Hardy Hilbert space \(\mathcal H_\theta\) with
\[
\left\|\sum_{k\ge0}a_kz^k\right\|_\theta^2
 =\sum_{k\ge0}|a_k|^2\exp(k^\theta),
\]
the normalized monomial images under composition by \(b_\lambda\) satisfy the two-scale sharp law
\[
\boxed{\ 
\log\frac{\|b_\lambda^n\|_\theta}{\|z^n\|_\theta}
=\frac{U^\theta-1}{2}\,n^\theta
+\frac{\theta^3U^{3\theta-2}(U^2-1)}{96}\,n^{3\theta-2}
+o(n^{3\theta-2})\ . }
\]
In fact the remainder after the two displayed terms is
\(O_{\lambda,\theta}(n^{5\theta-4}+\log(n+1))\).
Both displayed coefficients are strictly positive. In particular, composition by the disk automorphism \(b_\lambda\), initially defined on polynomials, has no bounded extension to \(\mathcal H_\theta\). The second coefficient detects an additional positive stretched-exponential amplification beyond the leading boundary-dilation rate.

## Assumptions and scope

All limits are as integers \(n\to\infty\), with the real parameters \(\lambda\) and \(\theta\) held fixed in the open ranges above. The weight at degree zero is \(\exp(0)=1\), and \(\|z^n\|_\theta=\exp(n^\theta/2)\). For each fixed \(n\), \(b_\lambda^n\) is rational with its only pole outside the closed unit disk, so its \(\mathcal H_\theta\)-norm is finite. The operator \(C_{b_\lambda}\) is understood on polynomials; the unbounded-extension conclusion concerns this densely defined operator. The proof uses complex Hardy-space Parseval identities, but the coefficient weights are real positive. No estimate is claimed for \(\theta\le2/3\), \(\theta\ge1\), or arbitrary finite Blaschke products.

## Proof

**Step 1: positive coefficient distribution and an exact moment-generating identity.** Write \(b_\lambda(z)^n=\sum_{k\ge0}a_{n,k}z^k\), and \(p_{n,k}=|a_{n,k}|^2\). Since \(b_\lambda\) is inner, Parseval on the unit circle yields \(\sum_{k\ge0}p_{n,k}=1\). For real \(s>0\) small enough that \(e^{s/2}<1/\lambda\), put
\[
M_n(s)=\sum_{k\ge0}p_{n,k}e^{sk}
=\frac1{2\pi}\int_{-\pi}^{\pi}
\left|b_\lambda(e^{s/2+it})\right|^{2n}\,dt.
\tag{1}
\]
Define \(F(s)=2\log b_\lambda(e^{s/2})\) for small positive \(s\). For \(r>1\),
\[
|b_\lambda(re^{it})|^2
=\frac{r^2+\lambda^2-2\lambda r\cos t}
{1+\lambda^2r^2-2\lambda r\cos t}.
\]
The derivative of this ratio with respect to \(\cos t\) is strictly positive, because the denominator minus the numerator is \((1-r^2)(1-\lambda^2)<0\). Thus its maximum occurs at \(t=0\), with value \(e^{F(s)}\). As \(r\) stays near one, the second angular derivatives of its logarithm remain uniformly bounded. Integrating over \(|t|\le1/n\) and using the trivial maximum upper bound gives
\[
nF(s)-\log(\pi n)-O(1/n)\le\log M_n(s)\le nF(s).
\tag{2}
\]
The error \(O(\log(n+1))\) is uniform when \(s\), \(s/2\), and \(3s/2\) tend to zero through positive values.

**Step 2: the cubic boundary jet.** The real analytic identity
\[
F(s)=2\log\frac{e^{s/2}-\lambda}{1-\lambda e^{s/2}}
\]
is odd near zero, as follows from \(b_\lambda(e^{-u})=b_\lambda(e^u)^{-1}\). Direct differentiation at zero gives \(F'(0)=U\), \(F''(0)=0\), and \(F'''(0)/6=c\). Consequently,
\[
F(s)=Us+cs^3+O_\lambda(s^5).
\tag{3}
\]
The included reproducibility script checks the cubic Taylor coefficient at rational parameter values; (3) itself is the exact analytic identity, not an inference from numerical checks.

**Step 3: upper estimate by the concave tangent.** Set \(h(x)=x^\theta\) for \(x\ge0\) and choose
\[
s_n=h'(Un)=\theta U^{\theta-1}n^{\theta-1}.
\]
Strict concavity implies for every integer \(k\ge0\),
\[
h(k)\le h(Un)+s_n(k-Un).
\tag{4}
\]
Writing \(Z_n=\|b_\lambda^n\|_\theta^2=\sum_kp_{n,k}e^{h(k)}\) and applying (1), (2), (3), and (4),
\[
\log Z_n\le U^\theta n^\theta-s_nUn+\log M_n(s_n)
=U^\theta n^\theta+cns_n^3+O(ns_n^5+\log(n+1)).
\tag{5}
\]

**Step 4: matching lower estimate, including the boundary-escape scale.** Tilt the coefficient distribution by \(s=s_n\):
\[
\mathbb P_s(K=k)=\frac{p_{n,k}e^{sk}}{M_n(s)}.
\]
For \(L>0\), Chernoff's inequality with shifts \(\pm s/2\) and (2)--(3) give
\[
\begin{aligned}
\log\mathbb P_s(K-Un\ge Lns^2)
 &\le (19c/8-L/2)ns^3+O(ns^5+\log(n+1)),\\
\log\mathbb P_s(K-Un\le-Lns^2)
 &\le (-7c/8-L/2)ns^3+O(ns^5+\log(n+1)).
\end{aligned}
\tag{6}
\]
Choose, for instance, \(L=10(c+1)\). Because \(ns^3\asymp n^{3\theta-2}\to\infty\) and \(ns^5=o(ns^3)\), (6) shows that the event
\(E_n=\{|K-Un|\le Lns^2\}\) has tilted probability tending to one, with an exponentially small complement on the scale \(ns^3\).

Define the nonnegative tangent deficit \(D_n(k)=h(Un)+s(k-Un)-h(k)\). On \(E_n\), we have \(k\ge Un/2\) eventually. Taylor's formula and \(|h''(x)|=\theta(1-\theta)x^{\theta-2}\) therefore imply
\[
0\le D_n(K)\le C_{\lambda,\theta}n^{\theta-2}(Lns^2)^2
=O_{\lambda,\theta}(n^\theta s^4).
\tag{7}
\]
There is an *exact* identity
\[
Z_n=e^{h(Un)-sUn}M_n(s)\,\mathbb E_s[e^{-D_n(K)}].
\tag{8}
\]
Using the probability of \(E_n\) and (7) in (8) yields
\[
\log\mathbb E_s[e^{-D_n(K)}]
\ge-O(n^\theta s^4)+o(1),
\]
where the reverse bound is zero. Since \(n^\theta s^4=O(n^{5\theta-4})=o(ns^3)\), (2), (3), and (8) give
\[
\log Z_n=U^\theta n^\theta+cns^3
+O_{\lambda,\theta}(n^{5\theta-4}+\log(n+1)).
\tag{9}
\]
Substitute \(s=\theta U^{\theta-1}n^{\theta-1}\), subtract \(\log\|z^n\|_\theta^2=n^\theta\), and divide by two. The asserted coefficient is \(\frac12c\theta^3U^{3\theta-3}=\theta^3U^{3\theta-2}(U^2-1)/96\). Its positivity proves that the normalized monomial images diverge, as claimed. \(\square\)

## Verification

The core checks are: (i) direct Parseval at radius \(e^{s/2}\) in (1); (ii) elementary monotonicity of the rational modulus in \(\cos t\) and a short arc lower bound in (2); (iii) the exact third derivative of \(F\); (iv) the two Chernoff signs and constants in (6); and (v) the strict inequalities \(3\theta-2>0\), \(5\theta-4<3\theta-2\) for \(2/3<\theta<1\). All are proved above. The supplementary script `verify_coefficients.py` executes finite rational checks of the cubic jet and sample coefficient identities, but finite checks are not substituted for (1)--(9). No extensive coefficient enumeration or unverified numerical saddle is needed.

## Relationship to prior work

Lefèvre, Li, Queffélec and Rodríguez-Piazza (arXiv:2311.01062, first public version 2 November 2023) study boundedness of composition on coefficient-weighted Hardy spaces. Their Example 2.18 includes the algebra property of the subexponential weights \(\exp(\sqrt n)\); their theory gives qualitative obstruction to disk-automorphism composition on non-slowly-oscillating weights. It does not state the sharp logarithmic normalized monomial asymptotic (9).

Szehr and Zarouf (arXiv:1701.02358, 9 January 2017) derive unweighted \(\ell^p\)-coefficient norms of powers of a Blaschke factor. Borichev, Fouchet and Zarouf (arXiv:2107.00405, 1 July 2021) derive detailed pointwise coefficient asymptotics across oscillatory, Airy and exponential regions. Their detailed estimates are an important potential route to *derive* weighted asymptotics after additional summation; the present result does not claim that the coefficient mechanisms are new. Rather, its object is the precise coefficient-weighted Hilbert norm and its second stretched-exponential growth term, obtained directly by a radial moment-generating identity and a tilted concentration argument. Searches described in the accompanying review did not identify this exact aggregate norm law. Priority remains subject to an independent literature audit.

## Limitations

The theorem treats one Blaschke factor with fixed real \(\lambda\) and the fixed supercritical range \(2/3<\theta<1\). It does not identify the power-law prefactor, describe the critical \(\theta=2/3\) transition, or classify arbitrary weighted composition operators. The cited 2021 pointwise asymptotics might yield this aggregate law after a separate asymptotic summation; this is the main prior-coverage risk. The statement has undergone only the described internal mathematical review, not independent validation.

## References

1. P. Lefèvre, D. Li, H. Queffélec, and L. Rodríguez-Piazza, *On some questions about composition operators on weighted Hardy spaces*, arXiv:2311.01062, public version dated 2023-11-02, https://arxiv.org/abs/2311.01062 .
2. A. Borichev, K. Fouchet, and R. Zarouf, *On the Fourier coefficients of powers of a Blaschke factor and strongly annular fonctions*, arXiv:2107.00405, public version dated 2021-07-01, https://arxiv.org/abs/2107.00405 .
3. O. Szehr and R. Zarouf, *\(\ell^p\)-norms of Fourier coefficients of powers of a Blaschke factor*, arXiv:1701.02358, public version dated 2017-01-09, https://arxiv.org/abs/1701.02358 .
