# Optimal heat-to-Poisson calibration on the circle: uniqueness, strict moment bias, and a sharp Gaussian–Cauchy boundary law

## Finding

Let \(m(d\theta)=d\theta/(2\pi)\) on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). For each heat time \(t>0\), the mean-one circle heat kernel and the centered Poisson kernel are
\[
H_t(\theta)=\sum_{n\in\mathbb Z}e^{-tn^2}e^{in\theta},\qquad
P_{r,\phi}(\theta)=\sum_{n\in\mathbb Z}r^{|n|}e^{in(\theta-\phi)},\quad 0\le r<1.
\]
Minimize \(\|H_t-P_{r,\phi}\|_{L^2(m)}^2\) jointly over radius and center. The following statements hold.

1. There is exactly one minimizing pair \((r_t,\phi_t)\), with \(0<r_t<e^{-t}\) and \(\phi_t=0\) modulo \(2\pi\). Writing \(a_t=-\log r_t\), the unique minimizer is characterized by
\[
4\sinh^2(a_t)\sum_{n=1}^{\infty}n e^{-tn^2-a_tn}=1,
\qquad a_t>t.
\]
The scalar left side increases strictly from zero to infinity with its positive argument.

2. At large heat time, writing \(q=e^{-t}\), the optimal radius is
\[
r_t=q-2q^3+11q^5+O(q^7)\qquad (t\to\infty).
\]
In particular, matching only the first trigonometric moment (\(r=q\)) is strictly suboptimal at every finite positive time.

3. Let \(c_*>0\) be the unique solution to
\[
H(c_*):=4c_*^2\int_0^\infty x e^{-x^2-c_*x}\,dx=1.
\]
It satisfies \(c_*=1.077742254305174\ldots\). Define
\[
J_*:=2\int_0^\infty\bigl(e^{-c_*x}-e^{-x^2}\bigr)^2\,dx
=0.0673805565808255\ldots>0.
\]
Then \(a_t\sim c_*\sqrt t\), and the minimum squared error diverges at the sharp rate \(J_*/\sqrt t\) as \(t\downarrow0\). More precisely, with \(H'(c_*)>0\) and
\[
b_*:=\frac{c_*^4/20+c_*^2/30}{H'(c_*)}=0.0909824498025251\ldots,
\]
there is an unexpected cancellation of the first correction:
\[
a_t=c_*\sqrt t+b_*t^{5/2}+O(t^{7/2}),
\]
and the minimum squared error \(E_t\) obeys
\[
E_t=\frac{J_*}{\sqrt t}-\frac{c_*(2+c_*^2)}{60}\,t^{3/2}+O(t^{5/2}).
\]

For comparison, the first-moment-matched Poisson radius is \(r=e^{-t}\), whose squared error satisfies
\[
\|H_t-P_{e^{-t},0}\|_2^2=t^{-1}+O(t^{-1/2}),
\qquad
\frac{\|H_t-P_{e^{-t},0}\|_2^2}{E_t}\sim\frac{1}{J_*\sqrt t}\longrightarrow\infty
\quad(t\downarrow0).
\]
Thus the best-fit Poisson scale is universally proportional to the heat diffusion length at short times, while a strictly positive, quantitatively sharp mismatch survives at the corresponding singular norm scale. Moment matching loses an unbounded relative factor in this limit.

## Assumptions and scope

All functions and norms are on the unit circle with normalized Haar measure \(m\). The heat Fourier multiplier is \(e^{-tn^2}\) (generator \(\partial_\theta^2\)), whereas the Poisson Fourier multiplier is \(e^{-a|n|}\), where \(r=e^{-a}\). Both kernels have integral one. The minimization is over all circular centers \(\phi\) and all \(0\le r<1\), with no arbitrary amplitude rescaling or change of the target's total mass. The case \(t=0\) is excluded because its limiting point mass is not in \(L^2(m)\). All asymptotic remainders concern scalar \(t\), not simultaneous changes in other parameters.

## Proof

**Center alignment and reduction.** Parseval gives the loss for any radius and center:
\[
\|H_t-P_{r,\phi}\|_2^2
=2\sum_{n\ge1}\bigl(e^{-2tn^2}+r^{2n}-2e^{-tn^2}r^n\cos(n\phi)\bigr).
\]
For every \(r>0\), each term of the cross-correlation is maximized when \(\phi=0\), and the \(n=1\) term forces strict uniqueness modulo \(2\pi\). Hence it remains to minimize, over \(a>0\),
\[
F_t(a)=2\sum_{n\ge1}(e^{-an}-e^{-tn^2})^2.
\]
For each \(a>0\) this is a uniformly differentiable series on a neighborhood of \(a\). Differentiation yields
\[
F_t'(a)=4\left(\sum_{n\ge1}n e^{-tn^2-an}-\sum_{n\ge1}n e^{-2an}\right).
\]
Using \(\sum_{n\ge1}n e^{-2an}=(4\sinh^2 a)^{-1}\), put
\[
G_t(a)=4\sinh^2(a)\sum_{n\ge1}n e^{-tn^2-an}.
\]
The derivative \(F_t'(a)\) has the sign of \(G_t(a)-1\).

**Strict monotonicity.** For fixed \(a>0\), let \(N\) have the discrete probability distribution proportional to \(n e^{-an}\), \(n=1,2,\ldots\). Tilt its law by the strictly decreasing positive weight \(e^{-tn^2}\) to obtain \(N_t\). The covariance inequality between an increasing function and a decreasing function gives
\[
\mathbb E N_t\le\mathbb E N=\frac{1+e^{-a}}{1-e^{-a}}=\coth(a/2).
\]
(The inequality is strict for \(t>0\), though weak inequality suffices.) Consequently,
\[
\frac{d}{da}\log G_t(a)=2\coth a-\mathbb E N_t
\ge 2\coth a-\coth(a/2)=\tanh(a/2)>0.
\]
As \(a\downarrow0\), the Gaussian-weighted sum is bounded and \(G_t(a)\to0\). As \(a\to\infty\), its first term gives \(G_t(a)\sim e^{a-t}\to\infty\). Exactly one point \(a_t\) satisfies \(G_t(a_t)=1\); the loss decreases before and increases after it. At \(a=t\), the \(n=1\) contribution to \(F'_t(t)\) vanishes while every \(n\ge2\) contribution is negative, because \(e^{-tn^2}<e^{-tn}\). Thus \(a_t>t\) and \(0<r_t<e^{-t}\). Since \(F'_t\) is nonzero away from its single root, and the uniform kernel \(r=0\) is approached from larger \(a\) with increasing loss, this is the unique global minimum over the full parameter set.

**Large-time expansion.** With \(q=e^{-t}\) and \(r=e^{-a_t}\), the critical equation becomes
\[
\frac{r}{(1-r^2)^2}=\sum_{n\ge1}n q^{n^2}r^{n-1}
=q+2q^4r+O(q^9r^2).
\]
The already established bound \(0<r<q\) and this identity imply \(r=q+O(q^3)\). Substitute \(r=q+u q^3+v q^5+O(q^7)\) into the two sides, uniformly as \(q\downarrow0\). Matching the powers \(q^3\) and \(q^5\) gives \(u=-2\), \(v=11\). The remaining analytic series and the derivative of the left side near zero control the remainder as \(O(q^7)\).

**Short-time universal limit.** Write \(h=\sqrt t\) and \(a=ch\). For fixed \(c>0\), a Riemann-sum limit gives
\[
G_{h^2}(ch)\longrightarrow H(c)
=4c^2\int_0^\infty x e^{-x^2-cx}\,dx
=4\int_0^\infty y e^{-y-y^2/c^2}\,dy.
\]
The final representation shows strict increase of \(H\) from zero to four. Its derivative has the explicit positive form
\[
H'(c)=\frac8{c^3}\int_0^\infty y^3e^{-y-y^2/c^2}\,dy.
\]
Thus exactly one \(c_*\) solves \(H(c_*)=1\). Fixed positive values on either side of \(c_*\) bracket the unique root \(a_t/h\) for all sufficiently small \(h\), proving \(a_t/h\to c_*\). Another Riemann-sum limit gives
\[
h F_{h^2}(ch)\longrightarrow J(c)
=2\int_0^\infty(e^{-cx}-e^{-x^2})^2\,dx.
\]
The derivative \(J'(c)=[H(c)-1]/c^2\) shows that \(J\) has the unique global minimum \(J(c_*)=J_*>0\), and the first error equivalent follows.

**Failure of moment matching at short times.** Setting \(a=t\) in the Fourier formula, the square \(\sum_{n\ge1}e^{-2tn}\) has leading term \((2t)^{-1}\), whereas \(\sum_{n\ge1}e^{-2tn^2}\) and \(\sum_{n\ge1}e^{-t(n^2+n)}\) are each \(O(t^{-1/2})\). The factor of two in the normalized Parseval identity therefore gives \(\|H_t-P_{e^{-t},0}\|_2^2=t^{-1}+O(t^{-1/2})\). Division by the sharp optimum equivalent proves the stated relative factor.

**The first missing correction and the error expansion.** We give enough Euler–Maclaurin detail to make the unusually high-order correction reproducible. For \(c\) in any fixed compact subset of \((0,\infty)\), put \(\varphi_c(x)=xe^{-x^2-cx}\). The rapidly decaying smooth function has \(\varphi'_c(0)=1\) and \(\varphi'''_c(0)=3c^2-6\). Euler–Maclaurin (with a uniform remainder from integrable higher derivatives) yields
\[
h\sum_{n\ge1}\varphi_c(nh)
=I(c)-\frac{h^2}{12}+\frac{3c^2-6}{720}h^4+O(h^6),
\quad I(c)=\int_0^\infty\varphi_c(x)\,dx.
\]
Since \(\sinh^2(ch)=c^2h^2+c^4h^4/3+2c^6h^6/45+O(h^8)\), multiplication and \(I(c_*)=1/(4c_*^2)\) give
\[
G_{h^2}(c_*h)=1-
\left(\frac{c_*^4}{20}+\frac{c_*^2}{30}\right)h^4+O(h^6).
\]
In particular, the \(h^2\) term cancels *exactly*, rather than only numerically. Applying the ordinary implicit-root estimate, using \(H'(c_*)>0\), gives
\[
\frac{a_t}{h}=c_*+\frac{c_*^4/20+c_*^2/30}{H'(c_*)}h^4+O(h^6).
\]
Finally set \(f_c(x)=(e^{-cx}-e^{-x^2})^2\). Here \(f_c(0)=f'_c(0)=0\) and \(f_c'''(0)=-12c-6c^3\). A second uniform Euler–Maclaurin expansion is
\[
2\sum_{n\ge1}f_c(nh)
=\frac{J(c)}h-\frac{c(2+c^2)}{60}h^3+O(h^5).
\]
The minimizing value \(c=a_t/h=c_*+O(h^4)\) can replace \(c_*\) in this formula: \(J'(c_*)=0\) makes its effect on the leading term \(O(h^7)\), and the correction term also changes only by \(O(h^7)\). This yields the claimed expansion for \(E_t\).

## Verification

`CHECK.py` (Python standard library only) independently evaluates the strictly monotone critical function, brackets numerical minimizers, compares finite Fourier losses, checks the large- and small-time expansions, and numerically integrates the boundary constants. Running `python3 CHECK.py` in the extracted package returned `PASS 82 finite diagnostics`. The program does not certify an infinite series, a continuous global optimum, an Euler–Maclaurin remainder, or historical novelty: those rely on the analytic arguments above. The approximate constants were also evaluated at higher precision using independent numerical quadrature; exact statements define them by convergent integrals.

## Relationship to prior work

Chaubey (2018) develops the wrapped Cauchy/Poisson circular kernel and its connection to Fourier density estimation. Jones and Pewsey (2005, Section 4.1) compare wrapped normal and other circular families using \(L^2\) differences *after first-moment matching*, rather than minimizing the distance with respect to the wrapped Cauchy radius. The present strict inequality \(r_t<e^{-t}\) shows that such moment matching is never the optimal calibration for this pair. Ameijeiras-Alonso (2024, Sections 5.1–5.3) compares standard circular kernels and their optimal *estimator asymptotic mean integrated squared errors*; its statistical bandwidth objective is different from the deterministic cross-semigroup \(L^2\) projection considered here. Bailey (2020 publicly deposited thesis, Chapter 6, Section 6.3.2, equations (6.5)–(6.7)) explicitly gives the squared Fourier loss **and its stationary equation** for least-squares approximation of a mixture of two wrapped-normal distributions by a wrapped Cauchy law. Setting the mixture weight to zero, or equating its source concentrations, already gives exactly the present one-source objective and critical equation. Neither the loss formula nor that stationary equation is claimed new; the thesis obtains roots numerically and the inspected section does not establish the present strict global uniqueness, systematic inward bias, or the sharp two-term short-time and large-time asymptotics. Bailey and Codling (2020) study the related mixture model; the full accepted journal manuscript was inaccessible. The assessed extension is precisely the global uniqueness theorem and detailed singular calibration law, not the Fourier reduction.

## Limitations

The problem optimizes one centered/translated Poisson kernel of unit mass against one heat kernel in the circle \(L^2\) norm. It does not cover mixtures, other norms, data-dependent random estimators, non-circular domains, or higher-dimensional spheres. The strict uniqueness proof is for \(t>0\). Numerical checks support but do not replace the infinite-dimensional proof. Historical priority is best-knowledge only, particularly because a relevant accepted manuscript was inaccessible; independent audit has not been carried out.

## References

1. Y. P. Chaubey, “Smooth Kernel Estimation of a Circular Density Function: A Connection to Orthogonal Polynomials on the Unit Circle,” *Journal of Probability and Statistics* (2018), Article 5372803. First published 2018-04-01. https://doi.org/10.1155/2018/5372803
2. J. Ameijeiras-Alonso, “A reliable data-based smoothing parameter selection method for circular kernel estimation,” *Statistics and Computing* 34 (2024), article 73. Published 2024-02-07. https://doi.org/10.1007/s11222-024-10384-x
3. M. C. Jones and A. Pewsey, “A Family of Symmetric Distributions on the Circle,” *J. Amer. Statist. Assoc.* 100 (2005), 1422–1428. https://doi.org/10.1198/016214505000000286
4. J. D. Bailey, *Fitting probability models to mixtures of directional distributions*, PhD thesis, University of Essex, publicly deposited 2020-01-08. Chapter 6, Section 6.3.2. https://repository.essex.ac.uk/26383/1/Thesis_2%281%29.pdf
5. J. D. Bailey and E. A. Codling, “Emergence of the wrapped Cauchy distribution in mixed directional data,” *AStA Adv. Stat. Anal.* 105 (2021), 229–246, first online 2020-10-09. https://doi.org/10.1007/s10182-020-00380-7
