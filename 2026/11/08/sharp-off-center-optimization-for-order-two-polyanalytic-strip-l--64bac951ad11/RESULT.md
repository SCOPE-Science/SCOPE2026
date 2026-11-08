# Sharp off-center optimization for order-two polyanalytic strip localization

## Finding

For every \(a>0\), let \(\mathcal F_{1,2}\) be the order-two polyanalytic Bargmann–Fock space and let \(T_a\) be compression of multiplication by the indicator of \(S_a=\{z:|\operatorname{Im}z|<a/\sqrt2\}\). In the standard normalization,
\[
\mathcal F_{1,2}=\{F:\mathbb C\to\mathbb C:\bar\partial^2F=0,\ \int_{\mathbb C}|F(z)|^2e^{-|z|^2}\,dA(z)/\pi<\infty\}.
\]
Define the normalized Hermite functions
\[
h_0(t)=\pi^{-1/4}e^{-t^2/2},\qquad h_1(t)=\sqrt2\,t\,h_0(t),
\]
and the interval Gram matrix
\[
\Gamma_a(x)=\int_{x-a}^{x+a}\begin{pmatrix}h_0(t)^2&h_0(t)h_1(t)\\h_0(t)h_1(t)&h_1(t)^2\end{pmatrix}\,dt.
\]
The norm is \(M(a)=\|T_a\|=\max_{x\in\mathbb R}\lambda_+(\Gamma_a(x))\). The maximum is achieved at finite fiber parameters, although the multiplication operator \(T_a\) need not have a norm-attaining vector. Every nonnegative maximizing fiber \(x_a\) satisfies
\[
\lim_{a\downarrow0}x_a=1/\sqrt2,\qquad \lim_{a\downarrow0}\frac{M(a)}a=\frac{4e^{-1/2}}{\sqrt\pi},
\]
and
\[
\lim_{a\to\infty}\bigl(a x_a-\log(2a)\bigr)=0,\qquad \lim_{a\to\infty}\sqrt\pi\,a^3e^{a^2}(1-M(a))=1.
\]
In particular \(x=0\) is *never* an optimizing fiber: \(\lambda_+(\Gamma_a(0))=\operatorname{erf}(a)\) and
\[
\left.\frac{d^2}{dx^2}\lambda_+(\Gamma_a(x))\right|_{x=0}=\frac{4a}{\sqrt\pi}e^{-a^2}>0.
\]
As \(a\to\infty\), this noncentral optimization reduces the concentration deficit by a factor asymptotic to \(a^2\) compared with the centered fiber.

## Assumptions and scope

The Gaussian weight, the strip orientation, its half-height \(a/\sqrt2\), the order-two (not true-order-two alone) polyanalytic subspace, and the Hermite normalization above are fixed. All limits hold for real \(a>0\), and the optimizing-fiber statements hold for *every* selection of a nonnegative maximizing fiber. Reflected negative maximizers are obtained by parity. No finite-Fock truncation is assumed.

## Proof

**1. Exact direct-integral reduction.** Proposition 10.4, equation (51), of Lee-Guzmán–Maximenko–Ramos-Vazquez–Sánchez-Nungaray [1] expresses a Toeplitz operator with symbol \(g(\operatorname{Im}z)\) as the matrix function
\[
\gamma_g(\xi)_{jk}=\sqrt2\int_{\mathbb R}g(v)\,h_j((\xi+2v)/\sqrt2)h_k((\xi+2v)/\sqrt2)\,dv,\quad j,k\in\{0,1\}.
\]
For \(g(v)={\bf1}_{|v|<a/\sqrt2}\), set \(t=(\xi+2v)/\sqrt2\) and \(x=\xi/\sqrt2\). This gives \(\Gamma_a(x)\) exactly. Positivity, continuity and \(\Gamma_a(x)\to0\) as \(|x|\to\infty\) show that the direct-integral norm is the attained fiber maximum.

**2. Matrix entries and noncentrality.** Write \(u=x-a\) and \(v=x+a\), and \(\Gamma_a=\begin{psmallmatrix}A&B\\B&C\end{psmallmatrix}\). Elementary Gaussian integration gives
\[
A=\tfrac12(\operatorname{erf}v-\operatorname{erf}u),\quad B=(e^{-u^2}-e^{-v^2})/\sqrt{2\pi},\quad C=A+(ue^{-u^2}-ve^{-v^2})/\sqrt\pi.
\]
At zero, \(B=0\), \(A=\operatorname{erf}(a)\), \(A-C=2ae^{-a^2}/\sqrt\pi>0\). Moreover \(A''(0)=-4ae^{-a^2}/\sqrt\pi\) and \(B'(0)=2\sqrt2ae^{-a^2}/\sqrt\pi\). Perturbing the simple top eigenvalue yields
\[
\lambda_+''(0)=A''(0)+2B'(0)^2/(A-C)=4ae^{-a^2}/\sqrt\pi>0.
\]
The function is even in \(x\) (its off-diagonal entry reverses sign), so the origin is a strict local minimum.

**3. Narrow-strip law.** Uniformly for \(x\) on compact sets, \(\Gamma_a(x)/(2a)\to h(x)h(x)^\mathsf T\), where \(h=(h_0,h_1)^\mathsf T\). Its unique maximizing absolute locations satisfy
\[
\|h(x)\|^2=(1+2x^2)e^{-x^2}/\sqrt\pi,\qquad |x|=1/\sqrt2.
\]
The trace estimate \(\lambda_+(\Gamma_a(x))\le\int_{x-a}^{x+a}\|h(t)\|^2dt\) bounds all candidate maximizers away from infinity as \(a\downarrow0\). Compactness and the strict maxima of this profile then prove the thin-strip statements.

**4. Wide-strip tail matrices.** Because \((h_0,h_1)\) are orthonormal on \(\mathbb R\), set \(Q_a(x)=I_2-\Gamma_a(x)\). For \(0\le x<a\), put \(t_-=a-x\), \(t_+=a+x\) and define
\[
p(t)=\tfrac12\operatorname{erfc}(t),\quad m(t)=e^{-t^2}/\sqrt{2\pi},\quad v(t)=p(t)+te^{-t^2}/\sqrt\pi.
\]
The left and right Gaussian tails have matrices
\[
L(t)=\begin{pmatrix}p(t)&-m(t)\\-m(t)&v(t)\end{pmatrix},\qquad R(t)=\begin{pmatrix}p(t)&m(t)\\m(t)&v(t)\end{pmatrix},\quad Q_a(x)=L(t_-)+R(t_+).
\]
Thus \(1-\lambda_+(\Gamma_a(x))=\lambda_{\min}(Q_a(x))\). An exact determinant expansion is
\[
\det Q_a=\det L(t_-)+\det R(t_+)+p(t_-)v(t_+)+p(t_+)v(t_-)+2m(t_-)m(t_+).
\]
Integration by parts, with uniform remainders for large \(t\), yields
\[
p(t)=\frac{e^{-t^2}}{2\sqrt\pi t}\left(1-\frac1{2t^2}+\frac3{4t^4}+O(t^{-6})\right),\qquad \det L(t)=\frac{e^{-2t^2}}{8\pi t^4}(1+O(t^{-2})).
\]
At \(x=(\log(2a)+s)/a\) with bounded real \(s\), \(t_\pm\sim a\) and direct substitution gives uniformly on each bounded set of \(s\),
\[
\lambda_{\min}(Q_a(x))=\frac{e^{-a^2}}{2\sqrt\pi a^3}\bigl(e^{2s}+e^{-2s}\bigr)(1+o(1)).\tag{*}
\]
Indeed \(\operatorname{tr}Q_a\sim a e^{-t_-^2}/\sqrt\pi\), the dominant single-tail determinant contributes \(e^{-t_-^2}/(8\sqrt\pi a^5)\) to the small eigenvalue, and the mixed tails contribute \(2e^{-t_+^2}/(\sqrt\pi a)\); the other single-tail determinant is negligible. The two contributions become the two terms of (*).

**5. Global exclusion and sharp optimization.** The competitor \(x=\log(2a)/a\) in (*) gives a deficit at most \((1+o(1))e^{-a^2}/(\sqrt\pi a^3)\). A maximizing fiber can be taken nonnegative by parity. For \(x\ge a/2\), the missing left-tail Gram matrix satisfies \(Q_a(x)\succeq L(a/2)\) (including \(x\ge a\)); its smallest eigenvalue is much larger than the competitor deficit, by the determinant expansion. Hence all nonnegative maximizers lie in \([0,a/2]\) for large \(a\).

On \(0\le x\le a/2\), the positive determinant summands and the trace bound imply, with constants independent of \(a,x\) for large \(a\),
\[
\lambda_{\min}(Q_a(x))\ \ge\ c\left(\frac{e^{-(a-x)^2}}{a^5}+\frac{e^{-(a+x)^2}}a\right).\tag{**}
\]
For the first term use \(\det L(t_-)\ge c e^{-2t_-^2}/a^4\) and \(\operatorname{tr}Q_a\le C a e^{-t_-^2}\); for the second use the strictly positive mixed terms \(p(t_-)v(t_+)+p(t_+)v(t_-)+2m(t_-)m(t_+)\ge c e^{-t_-^2-t_+^2}\). Comparing (**) at any global maximizer with the competitor proves first \(x=O(\log a/a)\) (since \(2ax-x^2\ge3ax/2\) here), then \(a x=\log a+O(1)\) using each exponential term. Therefore \(s=ax-\log(2a)\) is bounded, so the uniform asymptotic (*) applies along *all* maximizing fibers. Its strictly minimized profile \(e^{2s}+e^{-2s}\) has unique minimum at \(s=0\). Comparison with the \(s=0\) competitor forces \(s\to0\) and establishes the coefficient in the wide-strip norm law.

Finally, \(1-\operatorname{erf}(a)=\operatorname{erfc}(a)\sim e^{-a^2}/(\sqrt\pi a)\), giving the factor-\(a^2\) improvement.

## Verification

The standalone Python 3 (standard library) script `checks/strip_checker.py` tests the exact integrated matrix entries against independent Simpson quadrature, confirms local curvature at six widths, checks thin- and wide-strip asymptotics at representative widths, and checks the complementary-tail determinant identity. Running it produced `ORDER_TWO_STRIP_CHECKS_PASS 404`. These finite tests are supplementary: they cannot establish universal limits or the localization theorem, which are proved above. The operator is a direct integral; the computed fiber maxima are not asserted to be eigenvectors of the whole operator.

## Relationship to prior work

The unitary matrix-function reduction is **not** claimed as new: it is Proposition 10.4 and equation (51) of [1], closely related to Theorem 9 of [2]. Earlier polyanalytic Toeplitz work [3] also describes horizontal matrix symbols. The contribution here is the exact noncentrality for every width and the sharp two-endpoint optimizing-fiber/norm asymptotics, including the logarithmic displacement and the inverse-cubic Gaussian leakage. These are statements about maximizing a moving Hermite Gram matrix and are not immediate assertions of the cited direct-integral theorems. A stronger general historical theorem with the same sharp asymptotics would cover the claim; no such theorem was established by the inspected texts.

## Limitations

Only the two lowest Hermite modes and the stated Gaussian strip normalization are handled. No classification of the number of finite-width off-center extrema is claimed. The strict-center local minimum is proved for all widths but does not imply uniqueness of the positive global maximizer at arbitrary finite width. The asymptotic results are not uniform in the polyanalytic order. The first-public date refers to the focal source [1], not to a claimed publication date for this new result. Historical priority is provisional; no independent mathematical audit was performed.

## References

[1] E. Lee-Guzmán, E. A. Maximenko, G. Ramos-Vazquez and A. Sánchez-Nungaray, *Horizontal Fourier transform of the polyanalytic Fock kernel*, arXiv:2309.03410v1, first posted 2023-09-07, Section 7, Proposition 10.4 and equation (51). https://arxiv.org/html/2309.03410v1

[2] J. L. Arroyo Neri, A. Sánchez-Nungaray, M. Hernández Marroquin and R. R. López-Martínez, *Toeplitz Operators with Lagrangian Invariant Symbols Acting on the Poly-Fock Space of Cn*, Journal of Function Spaces 2021, 9919243, Theorem 9. https://doi.org/10.1155/2021/9919243

[3] A. Sánchez-Nungaray, M. González-Flores, R. López-Martínez and J. L. Arroyo Neri, *Toeplitz Operators with Horizontal Symbols Acting on the Poly-Fock Spaces*, 2018, DOI:10.1155/2018/8031259. https://doi.org/10.1155/2018/8031259
