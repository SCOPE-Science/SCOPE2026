# Sharp complete-Pick threshold for a sparse Schur factor of a fractional Hardy kernel

## Finding

**Theorem.** Fix \(0<\alpha\le1\), an integer \(m\ge2\), and \(0\le\tau\le1\). On the unit disk \(\mathbb D\), consider the normalized holomorphic positive kernel
\[
K_{\alpha,m,\tau}(z,w)=\frac{1}{(1-z\overline w)^\alpha\bigl(1-\tau(z\overline w)^m\bigr)}.
\]
Both factors are complete Nevanlinna–Pick kernels. Their Schur product \(K_{\alpha,m,\tau}\) is complete Nevanlinna–Pick **if and only if**
\[
0\le\tau\le T_{\alpha,m}:=\frac{(1-\alpha)(2-\alpha)\cdots(m-\alpha)}{(m+1)!}.
\]
At the Hardy endpoint \(\alpha=1\), this gives the sharp cutoff \(T_{1,m}=0\). For \(0<\alpha<1\), the first coefficient violating the complete-Pick criterion when \(\tau>T_{\alpha,m}\) occurs at degree exactly \(m+1\); at threshold that coefficient vanishes and every other nonconstant coefficient is strictly positive.

The threshold is strictly decreasing in \(m\), with
\[
\frac{T_{\alpha,m+1}}{T_{\alpha,m}}=\frac{m+1-\alpha}{m+2},\qquad
T_{\alpha,m}\sim\frac{m^{-1-\alpha}}{\Gamma(1-\alpha)}\quad(m\to\infty),\qquad 0<\alpha<1.
\]
Thus the Schur product of two normalized complete-Pick kernels can lose the complete-Pick property through an explicitly sharp and vanishingly small sparse second factor, despite both factors retaining that property separately.

There is also a geometric distinction from concave weighted shifts. At \((\alpha,m,\tau)=(1/2,2,1/10)\), the product kernel is complete Pick, but multiplication by \(z\) on its Hilbert space is **not** a concave operator, in the sense that \(M_z^{*2}M_z^2-2M_z^*M_z+I\not\preceq0\).

## Assumptions and scope

The disk is open, \(z,w\in\mathbb D\), and all kernels are scalar, normalized at \(0\), holomorphic in the first argument and antiholomorphic in the second. The Schur product is pointwise multiplication of kernels. A complete-Pick kernel means a normalized, nonvanishing positive kernel with the complete matrix-valued Nevanlinna–Pick interpolation property. We use the standard criterion that this is equivalent to positive semidefiniteness of \(1-1/K\). For a radial kernel \(F(z,w)=\sum_{n\ge0} f_n(z\overline w)^n\) analytic on \(\mathbb D\times\mathbb D\), positive semidefiniteness is equivalent to nonnegativity of all real coefficients \(f_n\). This follows from orthogonal Fourier characters on small circles or differentiation of positive Gram kernels at the origin. The parameter \(\tau\) is real and nonnegative.

## Proof

**Positivity and normalization.** The binomial coefficients in \((1-t)^{-\alpha}\) are strictly positive for \(\alpha>0\). The second factor has the positive expansion \(\sum_{j\ge0}\tau^jt^{mj}\) for \(|t|<1\), hence both factors and their product define positive kernels. Each is normalized and nonvanishing in the disk. For \(0<\alpha\le1\),
\[
1-(1-t)^\alpha=\sum_{n\ge1}c_n t^n,\qquad
c_1=\alpha,\qquad c_n=\alpha\frac{\Gamma(n-\alpha)}{\Gamma(1-\alpha)\Gamma(n+1)}>0
\quad(0<\alpha<1).
\]
This proves the first factor is complete Pick. The second factor satisfies \(1-1/K_2=\tau t^m\), also a positive kernel, so it is complete Pick.

**Exact coefficient criterion.** Put \(t=z\overline w\) and \(F(t)=1-1/K_{\alpha,m,\tau}(t)\). Then
\[
F(t)=1-(1-t)^\alpha(1-\tau t^m)
=\sum_{n\ge1}c_nt^n+\tau t^m-\tau\sum_{n\ge1}c_nt^{n+m}.
\]
Consequently the coefficient of \(t^n\) is \(c_n\) for \(1\le n<m\), is \(c_m+\tau\) for \(n=m\), and is \(c_n-\tau c_{n-m}\) for \(n\ge m+1\). For \(0<\alpha<1\), the ratio is
\[
\frac{c_n}{c_{n-m}}=\prod_{j=1}^{m}\frac{n-j-\alpha}{n-j+1}
\qquad(n\ge m+1).
\]
Each factor is strictly increasing with \(n\), since \((x-\alpha)/(x+1)\) increases for \(x>\alpha\). Hence the ratio is strictly increasing with \(n\) and its minimum occurs at \(n=m+1\), where
\[
\frac{c_{m+1}}{c_1}=\frac{\Gamma(m+1-\alpha)}{\Gamma(1-\alpha)\Gamma(m+2)}=T_{\alpha,m}.
\]
The complete-Pick coefficient criterion therefore holds exactly when \(\tau\le T_{\alpha,m}\), and the claimed first-negative-coefficient and equality descriptions follow. For \(\alpha=1\), direct cancellation gives \(F(t)=t+\tau t^m-\tau t^{m+1}\); since \(m\ge2\), its \((m+1)\)-coefficient is negative for \(\tau>0\), proving the endpoint.

**Threshold decay.** The displayed gamma quotient gives \(T_{\alpha,m+1}/T_{\alpha,m}=(m+1-\alpha)/(m+2)\), strictly between zero and one. The gamma-ratio asymptotic \(\Gamma(m+1-\alpha)/\Gamma(m+2)\sim m^{-1-\alpha}\) gives the exact leading power and constant.

**Complete Pick without concavity.** For \(\alpha=1/2,m=2,\tau=1/10\), the threshold is \(T_{1/2,2}=1/8\), so the kernel is complete Pick. Its first four Taylor coefficients \(K(t)=\sum_{n\ge0}k_nt^n\) are
\[
(k_0,k_1,k_2,k_3)=\left(1,\frac12,\frac{19}{40},\frac{29}{80}\right).
\]
The monomials are orthogonal with squared norms \(1/k_n\). Hence the squared weights of \(M_z\) on the orthonormal monomial basis at indices one and two are \(k_1/k_2=20/19\) and \(k_2/k_3=38/29\). The diagonal quadratic form of \(M_z^{*2}M_z^2-2M_z^*M_z+I\) at the basis vector indexed one is
\[
\frac{20}{19}\frac{38}{29}-2\frac{20}{19}+1=\frac{151}{551}>0.
\]
Thus the concavity inequality fails although the kernel remains complete Pick. Multiplication is bounded in this example: its coefficients satisfy \(k_n\sim (1-\tau)^{-1}n^{\alpha-1}/\Gamma(\alpha)\), which makes consecutive coefficient ratios bounded, and the finitely many initial ratios are finite.

## Verification

`CHECK.py` is a standalone standard-library exact-rational checker. It evaluates the critical coefficients and finite coefficient windows for \(\alpha\in\{1/4,1/3,1/2,2/3,3/4,1\}\), \(2\le m\le12\), and amplitudes on, below, and above the theoretical phase boundary. It additionally verifies the explicit nonconcavity example and monotonicity identities. Its finite arithmetic tests are only supplementary; the complete all-degree proof is the monotonic ratio argument above. Run `python CHECK.py`.

## Relationship to prior work

Sau's 2026 article establishes criteria for *admitting a complete-Pick factor*, and explicitly distinguishes that weaker property from being complete Pick. Every kernel here trivially admits such a factor, but that fact cannot decide whether the **whole Schur product** is complete Pick; the exact positive-to-negative coefficient transition is an additional statement. The closest published published-finding corpus phase diagram instead studies **monomial defect kernels**, with a factor \(1-s(z\overline w)^m\) in the numerator. It is not the present resolvent multiplier \((1-\tau(z\overline w)^m)^{-1}\); its coefficient threshold does not imply the present exact ratio criterion or the nonconcavity witness. Classical complete-Pick characterization supplies the test but not this classification. The comparison includes factorization, reciprocal, and sign-alias formulations, but no exhaustive claim of worldwide priority is made.

## Limitations

Only this one-factor fractional-power and one sparse resolvent family on the disk is classified. No statement is made for complex or negative \(\tau\), multiple sparse factors, general symbols, complete-Pick factor uniqueness, or curvature and multiplier interpolation constants. The example does not classify concavity elsewhere in parameter space. The threshold follows from an elementary coefficient-ratio structure specific to the family; it is not automatically a classification of arbitrary products of complete-Pick kernels. Some older literature may formulate an equivalent coefficient test under different analytic terminology; independently verified novelty is not claimed.

## References

1. H. Sau, *On de Branges–Rovnyak Kernels Admitting a Complete Pick Factor*, arXiv:2606.09680, first publicly submitted 2026-06-08, https://arxiv.org/abs/2606.09680 (primary MSC2020 46E22).
2. J. Agler and J. E. McCarthy, *Complete Nevanlinna–Pick kernels*, Journal of Functional Analysis 175 (2000), 111–124.
3. H. Ahmed, B. K. Das, S. Panja, *de Branges–Rovnyak spaces which are complete Nevanlinna–Pick spaces*, arXiv:2403.19377, https://arxiv.org/abs/2403.19377.
4. *Sharp complete-Pick phase diagram for monomial defects of power kernels*, published-finding corpus record `2026/11/8/SCOPE-sharp-complete-pick-phase-diagram-for-monomial-defects-of-power--a614d1883358`, https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-sharp-complete-pick-phase-diagram-for-monomial-defects-of-power--a614d1883358.
