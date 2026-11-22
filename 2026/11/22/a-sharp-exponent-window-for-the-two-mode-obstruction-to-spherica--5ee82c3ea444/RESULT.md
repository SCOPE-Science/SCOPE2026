# A sharp exponent window for the two-mode obstruction to spherical Poisson hypercontractivity

## Finding
Let \(d\ge4\) be an integer, \(M=d+1\), and \(R_d=\sqrt{2(d+1)/d}\). There is exactly one number \(q_c(d)>2\), apart from the trivial endpoint \(q=2\), solving
\[
(q-1)^{1-R_d}\big(M(q-1)+1\big)=M+q-1.
\]
For every \(2<q<q_c(d)\), the fractional-Laplacian Poisson semigroup \(P_s=e^{-s\sqrt{-\Delta_{\mathbb S^d}}}\) fails the purported sharp spectral-gap \(L^2\)-to-\(L^q\) contraction at the Nelson time \(s_*=\log(q-1)/(2\sqrt d)\): there is a positive, real, degree-two zonal polynomial \(f\) with \(\|P_{s_*}f\|_q>\|f\|_2\). On the explicit two-mode perturbation class described below, \(q_c(d)\) is the *exact* boundary of fourth-order positivity: its maximized quartic defect is positive below, vanishes at, and is negative above that exponent. In particular,
\[
q_c(4)=6.8035120211789\ldots,\qquad
q_c(d)\sim (d+1)^{1+\sqrt2}\quad(d\to\infty).
\]
The latter statement concerns this local two-mode test, not the exact unrestricted hypercontractive time or global contractivity for larger \(q\).

## Assumptions and scope
The unit sphere \(\mathbb S^d\subset\mathbb R^{d+1}\) carries normalized surface measure. The nonnegative Laplace–Beltrami operator \(L=-\Delta_{\mathbb S^d}\) has degree-\(k\) eigenvalue \(k(k+d-1)\). All \(L^p\) norms refer to this probability measure. Write \(x=\xi_1\), and put \(X=x\) and \(Y=x^2-1/M\). These are spherical harmonics of degrees one and two. For each \(q>2\), define \(t=q-1\), \(a=t^{-1/2}\), and \(b=t^{-R_d/2}\). At \(s_*\), \(P_{s_*}X=aX\) and \(P_{s_*}Y=bY\). Consider \(f_{\varepsilon,c}=1+\varepsilon X+c\varepsilon^2Y\), for real \(c\) and sufficiently small nonzero real \(\varepsilon\). Both \(f_{\varepsilon,c}\) and its image are strictly positive, so no ambiguity in real \(q\)-powers arises.

## Proof
The coordinate-moment identities for the uniform sphere are
\[
\mathbb E X^2=\frac1M,\quad
\mathbb E X^4=\frac3{M(M+2)},\quad
\mathbb E Y^2=\mathbb E(X^2Y)=w=\frac{2(M-1)}{M^2(M+2)}.
\]
They follow either from the beta distribution of the squared first coordinate or from rotational invariance. Set \(h=1-tb^2=1-t^{1-R_d}>0\). Analytic expansion at \(\varepsilon=0\), with all odd powers integrating to zero, gives
\[
\|P_{s_*}f_{\varepsilon,c}\|_q^q-\|f_{\varepsilon,c}\|_2^q
=\varepsilon^4\big(Ac^2+Bc+C\big)+O_{d,q,c}(\varepsilon^6),
\]
where
\[
 A=-\frac q2wh,\qquad
 B=\frac{q(q-2)}2bw,\qquad
 C=-\frac{q(q-2)(M+q-1)}{4(q-1)M^2(M+2)}.
\]
The order-two coefficient is exactly zero because \((q-1)a^2=1\). To verify these coefficients directly, expand \((1+a\varepsilon X+bc\varepsilon^2Y)^q\) to degree four, and subtract \((1+\varepsilon^2\mathbb E X^2+c^2\varepsilon^4\mathbb E Y^2)^{q/2}\). The only quartic expectation terms are \(\mathbb E Y^2\), \(\mathbb E X^2Y\), and \(\mathbb E X^4\), listed above. Uniform positivity of the two polynomials for small \(\varepsilon\) justifies Taylor expansion even for nonintegral \(q\).

Since \(A<0\), the unique maximizing parameter is
\[
c_*=\frac{(q-2)b}{2h},
\]
and the maximized fourth-order defect is exactly
\[
 \mathcal D_{d,q}=\frac{q(q-2)}{4(q-1)M^2(M+2)h}
 \Big[t^{1-R_d}(Mt+1)-(M+t)\Big].
\]
Thus its sign is that of \(F_d(t)=(1-R_d)\log t+\log(Mt+1)-\log(M+t)\). It remains to prove the claimed sign transition rather than merely locate a numerical zero. Differentiating yields
\[
 tF_d'(t)=1-R_d+\frac{t(M^2-1)}{(Mt+1)(M+t)}.
\]
The second term is strictly decreasing for \(t>1\), because the derivative of \(t/[(Mt+1)(M+t)]\) has the sign of \(1-t^2\). Its value at \(t=1\) is \((M-1)/(M+1)\), and \(F_d'(1)>0\) precisely when \(M^2-4M-1>0\), which holds for every \(M\ge5\). Since \(F_d(1)=0\), \(F_d(t)\to-\infty\) as \(t\to\infty\), and \(tF_d'(t)\) decreases from positive to negative, \(F_d\) has one interior maximum and exactly one zero \(t_c>1\). Consequently, \(\mathcal D_{d,q}>0\) iff \(1<t<t_c\). For this interval, choosing \(c=c_*\) and sufficiently small \(\varepsilon\ne0\) makes the exact norm defect positive, proving strict contraction failure.

For the growth law, let \(\eta_d=R_d-1\in(0,1)\). The critical equation is \(t_c^{\eta_d}=(Mt_c+1)/(M+t_c)\). For each fixed \(\delta\in(0,1)\), substitute \(t=M^{1/\eta_d}(1\pm\delta)\). Since \(\eta_d\to\sqrt2-1\) and \(M^{1/\eta_d}/M\to\infty\), the right side is \(M(1+o(1))\), while the left side is \(M(1\pm\delta)^{\eta_d}\). The uniqueness just proved places \(t_c/M^{1/\eta_d}\to1\). Finally, \(1/\eta_d=1+\sqrt2+O(1/d)\) and \(\log M/d\to0\), yielding \(q_c(d)\sim M^{1+\sqrt2}\).

## Verification
The accompanying \(check.py\) reconstructs the moment identities with exact rational arithmetic, reproduces fourth-order coefficients for integer exponents, independently evaluates actual norm defects by normalized Gauss–Jacobi quadrature, and checks the unique sign-transition condition and several numerical roots. Its reported finite diagnostics supplement, but do not replace, the analytic proofs above. Numeric root isolation can be independently reproduced by bracketing \(F_4\) on \(t\in(5.80351,5.80352)\).

## Relationship to prior work
Frank–Ivanisvili (2021) prove the spectral-gap criterion sufficient in sphere dimensions at most three and establish failure in sufficiently large dimensions, leaving higher-dimensional sharp contraction times open. Their counterexample uses large-degree Gegenbauer modes, not the present exact low-degree, exponent-dependent boundary. A public 20 July 2026 calculation establishes the dimension-four case for \(q=4\), including the same degree-one/two quartic obstruction; that case is **previously known**, and not claimed as a new standalone result here. The contribution assessed here is the complete dimension-dependent interval of real target exponents, its unique threshold, and its sharp large-dimension growth. Hormozi–Zhu (2026) treat boundedness and ultracontractivity for Jacobi and other subordinated orthogonal-polynomial semigroups; boundedness with an unspecified constant does not imply contractivity with constant one at this time.

## Limitations
The exact threshold refers only to the specified fourth-order zonal perturbation with a second-harmonic coefficient of order \(\varepsilon^2\). For \(q\ge q_c(d)\), a nonpositive quartic coefficient does not prove unrestricted contraction, nor rule out other frequencies, perturbation orders, or finite-amplitude witnesses. The endpoint \(q=q_c(d)\) may be decided by sixth or higher order. This is a self-review; no independent audit or historical-priority certification has been performed. The cited 2026 web calculation is an independently posted result readout, not a peer-reviewed article.

## References
1. R. L. Frank and P. Ivanisvili, *Hypercontractivity of the semigroup of the fractional Laplacian on the \(n\)-sphere*, arXiv:2101.06209v1, first public 15 January 2021, https://arxiv.org/abs/2101.06209.
2. *Disproof of Nelson-time hypercontractivity for the Poisson semigroup on \(\mathbb S^4\)*, dated 20 July 2026, https://vikvang.github.io/poisson-hypercontractivity-s4/.
3. M. Hormozi and J.-X. Zhu, *Hypercontractivity of Poisson Semigroups with Orthogonal Polynomial Eigenfunctions*, arXiv:2603.28223v1, 30 March 2026, https://arxiv.org/abs/2603.28223.
