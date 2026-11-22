# The sharp critical boundary for fractional Volterra power commutators

## Finding
Let \(I^\alpha\) be the left Riemann–Liouville integral on \(L^2(0,1)\), and let \(M_\beta\) denote multiplication by \(x^\beta\). On \(C_c^\infty(0,1)\) form the commutator
\[
T_{\alpha,\beta}=I^\alpha M_\beta-M_\beta I^\alpha.
\]
For every \(0<\alpha<1/2\) and \(-1/2<\beta<0\), the following **complete three-phase classification** holds:

1. If \(\alpha+\beta>0\), \(T_{\alpha,\beta}\) extends uniquely to a Hilbert–Schmidt (hence compact) operator, with the exact norm
   \[
   \|T_{\alpha,\beta}\|_{\mathcal S_2}^2
   =\frac{1}{2(\alpha+\beta)\Gamma(\alpha)^2}
   \int_0^1(z^\beta-1)^2(1-z)^{2\alpha-2}\,dz.
   \tag{1}
   \]
2. If \(\beta=-\alpha\), it extends uniquely to a bounded **noncompact** operator; the exact, unattained operator and essential norms coincide:
   \[
   \boxed{\|T_{\alpha,-\alpha}\|_{2\to2}
   =\|T_{\alpha,-\alpha}\|_{\rm ess}
   =\frac{\Gamma(\frac12-\alpha)}{\Gamma(\frac12)}-
   \frac{\Gamma(\frac12)}{\Gamma(\frac12+\alpha)}.}
   \tag{2}
   \]
3. If \(\alpha+\beta<0\), it has **no bounded extension** to \(L^2(0,1)\).

There is a matching sharp Hilbert–Schmidt energy law on both sides of the compact/noncompact transition. Define the strictly positive finite coefficient
\[
Q_\alpha=\frac{1}{\Gamma(\alpha)^2}\int_0^1(z^{-\alpha}-1)^2(1-z)^{2\alpha-2}\,dz.
\]
For fixed \(0<\alpha<1/2\), as \(\delta\downarrow0\),
\[
\boxed{\lim_{\delta\downarrow0}2\delta\,\|T_{\alpha,-\alpha+\delta}\|_{\mathcal S_2}^2=Q_\alpha.}
\tag{3}
\]
At the critical exponent, if \(E_\varepsilon\) is multiplication by \(\mathbf1_{(\varepsilon,1)}\), then
\[
\boxed{\|E_\varepsilon T_{\alpha,-\alpha}E_\varepsilon\|_{\mathcal S_2}^2
=Q_\alpha\log(1/\varepsilon)+O_\alpha(1)}
\quad(\varepsilon\downarrow0).
\tag{4}
\]
Thus the compact-side Hilbert–Schmidt pole and critical spatial cutoff have the *same exact coefficient*, although the critical operator has finite norm.

## Assumptions and scope
Work over real or complex \(L^2(0,1)\) with Lebesgue measure. For \(\alpha>0\),
\[
(I^\alpha f)(x)=\frac1{\Gamma(\alpha)}\int_0^x(x-y)^{\alpha-1}f(y)\,dy.
\]
The power multiplier \(M_\beta\) may be unbounded, so \(T_{\alpha,\beta}\) is **initially** defined only on the dense common core \(C_c^\infty(0,1)\), where the two compositions make sense. In the parameter range of the theorem, its kernel is
\[
k_{\alpha,\beta}(x,y)=\frac{\mathbf1_{0<y<x<1}}{\Gamma(\alpha)}(y^\beta-x^\beta)(x-y)^{\alpha-1}\ge0.
\tag{5}
\]
"Essential norm" means distance to the compact operators on \(L^2(0,1)\). The signs in (5) are fixed by choosing \(I^\alpha M_\beta-M_\beta I^\alpha\); reversing the commutator changes its sign but not its norms. The ranges \(0<\alpha<1/2\), \(-1/2<\beta<0\) are intentional: the critical line \(\beta=-\alpha\) lies strictly inside this rectangle, and its Mellin kernel is integrable. No statement about boundary values \(\alpha=1/2\), \(\beta=-1/2\), or about other function spaces is made.

## Proof
**1. Compact phase and exact Hilbert–Schmidt norm.** In the triangle \(0<y<x<1\), substitute \(y=xz\) into the squared kernel (5). The Jacobian gives the exact factorization
\[
\iint |k_{\alpha,\beta}(x,y)|^2\,dy\,dx
=\frac1{\Gamma(\alpha)^2}\left(\int_0^1x^{2(\alpha+\beta)-1}\,dx\right)
\left(\int_0^1(z^\beta-1)^2(1-z)^{2\alpha-2}\,dz\right).
\tag{6}
\]
The second integral is finite: at zero its integrand is \(O(z^{2\beta})\), integrable because \(\beta>-1/2\), and at one the cancellation \(z^\beta-1=O(1-z)\) makes it \(O((1-z)^{2\alpha})\). Hence (6) is finite precisely when \(\alpha+\beta>0\), proving (1) and the Hilbert–Schmidt extension in that regime.

**2. Exact critical transformation.** At \(\beta=-\alpha\), use the unitary map \(U:L^2(0,1)\to L^2(0,\infty)\) given by
\[
(Uf)(u)=e^{-u/2}f(e^{-u}).
\]
The substitutions \(x=e^{-u}\) and \(y=xe^{-s}\) in (5) yield, first on a dense core and then by bounded extension,
\[
(UT_{\alpha,-\alpha}U^{-1}g)(u)=\int_0^\infty h_\alpha(s)g(u+s)\,ds,
\quad h_\alpha(s)=\frac{(e^{\alpha s}-1)e^{-s/2}(1-e^{-s})^{\alpha-1}}{\Gamma(\alpha)}.
\tag{7}
\]
The kernel is strictly positive for \(s>0\), behaves as \(O(s^\alpha)\) at zero and as \(O(e^{-(1/2-\alpha)s})\) at infinity. It is therefore integrable. The triangle inequality for translations gives \(\|UTU^{-1}\|\le \int_0^\infty h_\alpha(s)\,ds\).

For the matching lower bound, set \(g_L=L^{-1/2}\mathbf1_{[0,L]}\). For any fixed \(R>0\), on \(0\le u\le L-R\) equation (7) gives \((UTU^{-1}g_L)(u)\ge L^{-1/2}\int_0^R h_\alpha\). Let \(L\to\infty\) and then \(R\to\infty\) to obtain equality. Substitution \(z=e^{-s}\) and two beta integrals evaluate the mass as
\[
\int_0^\infty h_\alpha(s)\,ds
=\frac{B(\frac12-\alpha,\alpha)-B(\frac12,\alpha)}{\Gamma(\alpha)}
=\frac{\Gamma(\frac12-\alpha)}{\Gamma(\frac12)}-
\frac{\Gamma(\frac12)}{\Gamma(\frac12+\alpha)},
\]
proving the operator-norm part of (2).

There is no nonzero norming vector: for \(g\ne0\), the right-translation \(g(\cdot+s)\) has norm \(\big(\|g\|_2^2-\int_0^s|g(v)|^2dv\big)^{1/2}\), strictly less than \(\|g\|_2\) for a positive-measure set of \(s>0\). Integrating against the strictly positive \(h_\alpha\) makes the triangle bound strict.

To prove the **essential norm** equals the same mass, translate the normalized plateaus out to infinity: \(g_{L,A}=L^{-1/2}\mathbf1_{[A,A+L]}\) with \(A\to\infty\) (for example \(A=L\)). These vectors converge weakly to zero, while the output norm on \([A,A+L-R]\) gives the same lower limit \(\int_0^R h_\alpha\). Every compact operator sends a bounded weakly-null sequence to a norm-null sequence. Consequently \(\|T-K\|\ge\int h_\alpha\) for every compact \(K\), while \(\|T\|\) is itself an upper bound. This proves (2) and noncompactness.

**3. Failure of boundedness below the critical line.** Let \(0\le f\in C_c^\infty(1/4,1/2)\) be nonzero, and set \(f_\varepsilon(y)=\varepsilon^{-1/2}f(y/\varepsilon)\). Its \(L^2(0,1)\) norm is constant. By the exact homogeneity in (5), for \(x=\varepsilon z\) with \(3/4\le z\le7/8\),
\[
(T_{\alpha,\beta}f_\varepsilon)(\varepsilon z)
=\varepsilon^{\alpha+\beta-1/2}(T_{\alpha,\beta}f)(z).
\]
The latter function is strictly positive on that fixed \(z\)-interval. Thus the output norm is at least \(c_{\alpha,\beta,f}\varepsilon^{\alpha+\beta}\), which diverges as \(\varepsilon\downarrow0\) if \(\alpha+\beta<0\). This proves the third case.

**4. The matching energy coefficient.** Define \(j_\alpha(z)=(z^{-\alpha}-1)^2(1-z)^{2\alpha-2}\). Both \(j_\alpha\) and \(|\log z|j_\alpha\) are integrable on \((0,1)\): at zero use \(2\alpha<1\), and at one use the cancellation from Step 1. With \(\beta=-\alpha+\delta\), the numerator integral in (1) converges to \(\int j_\alpha\) by dominated convergence for \(0<\delta<\alpha\), proving (3).

At criticality, restricting both variables to \((\varepsilon,1)\), then using \(y=xz\) and Fubini, gives the **exact finite-cutoff identity**
\[
\|E_\varepsilon T_{\alpha,-\alpha}E_\varepsilon\|_{\mathcal S_2}^2
=\frac1{\Gamma(\alpha)^2}\int_\varepsilon^1 j_\alpha(z)\log(z/\varepsilon)\,dz.
\tag{8}
\]
Decomposing \(\log(z/\varepsilon)=\log(1/\varepsilon)+\log z\) and using the two integrability facts yields (4); in fact the difference from \(Q_\alpha\log(1/\varepsilon)\) converges to \(\Gamma(\alpha)^{-2}\int_0^1j_\alpha(z)\log z\,dz\). All limits are infinite-dimensional identities or consequences of dominated convergence, not numerical extrapolations.

## Verification
The algebraic and analytic ingredients to check are (i) the Jacobian and exponents in (6), (ii) the unitary Mellin-coordinate conjugacy (7), (iii) positivity and integrability of its kernel, (iv) the plateau and weakly-null lower bounds, (v) exact scaling of the localized test functions, and (vi) the Fubini formula (8). The accompanying `verify_fractional_commutator.py` is runnable with Python and `mpmath`; it checks 17 supplementary beta-integral, gamma-normalization, cutoff-slope, pole, and scaling identities. Its tests are not proofs of the operator or essential norm and do not replace Steps 1–4.

## Relationship to prior work
Carvalho-Neto and Fehlberg Júnior (first posted August 4, 2021, arXiv:2108.02291) establish general \(L^p\)-boundedness and compactness of the **unweighted** Riemann–Liouville operator, but their targeted Sections 3–4 do not calculate this unbounded-power commutator or its sharp Mellin norm. Fernandez and Fahad (2022) study weighted fractional integrals as conjugates of unweighted operators; their detailed Sections 3–4 do not state the power-commutator trichotomy or the energy coincidence (3)–(4). Bernardis and Lorente (2008) prove weighted \(L^p\) inequalities for Riemann–Liouville commutators with BMO symbols; their full text could not be inspected and remains a priority risk, although the available abstract concerns different hypotheses and conclusions. The published work *A universal singular-value Weyl law for Hardy power commutators* treats \([H,M_{x^\eta}]\) for \(\eta>0\), where \(Hf=x^{-1}\int_0^x f\), and obtains singular-value asymptotics. That is a different integration kernel, power sign, and parameter regime; the complete inspected result does not assert (2)–(4). A 2026 fractional Volterra essential-norm manuscript concerns analytic Hardy/Bergman spaces on a complex disk, not this real half-line Mellin boundary.

## Limitations
This theorem treats only \(0<\alpha<1/2\) and \(-1/2<\beta<0\), and says nothing about operators on \(L^p\) for \(p\ne2\), trace ideals smaller than Hilbert–Schmidt, or compactness behavior under more general multiplier symbols. No singular-value counting law is claimed. The specialized 2008 source and some older weighted Volterra literature were not fully available for a conclusive historical-priority assessment. The self-contained proof establishes the mathematical statements, not bibliographic uniqueness or independent scientific certification.

## References
1. P. M. Carvalho-Neto and R. Fehlberg Júnior, *The Riemann-Liouville fractional integral in Bochner-Lebesgue spaces I*, arXiv:2108.02291, first submitted 2021-08-04, https://arxiv.org/abs/2108.02291.
2. A. Fernandez and H. M. Fahad, *Weighted Fractional Calculus: A General Class of Operators*, Fractal and Fractional 6 (2022), 208, https://doi.org/10.3390/fractalfract6040208.
3. A. L. Bernardis and M. Lorente, *Sharp Two Weight Inequalities for Commutators of Riemann-Liouville and Weyl Fractional Integral Operators*, Integral Equations and Operator Theory 61 (2008), 449–475, https://doi.org/10.1007/s00020-008-1600-y (full text unavailable in this comparison).
4. *A universal singular-value Weyl law for Hardy power commutators*, published mathematical record dated 2026-10-18, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-a-universal-singular-value-weyl-law-for-hardy-power-commutators--33677ede3aa1 (complete `RESULT.md` inspected).
5. Z. Wang and Z. Si, *Commutator Theorems for Fractional Integral Operators on Weighted Morrey Spaces*, Abstract and Applied Analysis (2014), article 413716, https://doi.org/10.1155/2014/413716.
