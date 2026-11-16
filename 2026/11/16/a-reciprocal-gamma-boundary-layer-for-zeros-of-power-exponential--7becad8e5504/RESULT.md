# A reciprocal-Gamma boundary layer for zeros of power-exponential Gaussian entire functions

## Finding

For every real \(\beta>0\), let \((\xi_n)_{n\ge0}\) be independent standard *circular* complex Gaussian random variables and define the almost surely entire function
\[
F_\beta(z)=\sum_{n=0}^{\infty}\frac{\xi_n z^n}{\sqrt{\Gamma(2(n+1)/\beta)}}.
\]
At the unit-circle boundary scale, define the entire function
\[
G_\beta(u)=\beta^{-1/2}e^{u/\beta}F_\beta(e^{u/\beta}),\qquad u\in\mathbb C.
\]
Its zeros on any fixed bounded \(u\)-domain correspond, for large enough \(\beta\), to zeros of \(F_\beta\) under the local logarithmic coordinate \(z=e^{u/\beta}\). Put
\[
L(s)=\int_0^\infty\frac{e^{sx}}{\Gamma(2x)}\,dx,\qquad s\in\mathbb C,
\]
where \(1/\Gamma(0)=0\). This is entire. Then, as \(\beta\to\infty\):

1. \(G_\beta\) converges in distribution, in the topology of uniform convergence on compact subsets of \(\mathbb C\), to a nondegenerate proper Gaussian analytic function \(G\) with covariance \(\mathbb E[G(u)\overline{G(v)}]=L(u+\bar v)\) and zero pseudocovariance. Its locally finite zero counting measures converge in distribution in the vague topology to those of \(G\). The limiting zero process is invariant and mixing under vertical translation \(u\mapsto u+it\).
2. For each compact \(C\subset\mathbb C\) and any prescribed nonnegative mixed-derivative order, uniformly for \(u,v\in C\), the covariance has the **universal second-order defect**
\[
\mathbb E[G_\beta(u)\overline{G_\beta(v)}]
=L(u+\bar v)-\frac{1}{6\beta^2}+O_C(\beta^{-4}),
\]
including all the indicated derivatives. The coefficient \(-1/6\) is independent of the two spatial variables; there is no order-\(\beta^{-1}\) term.
3. The one-point zero intensity per unit Euclidean area is the strictly positive function
\[
\rho(t)=\frac1\pi\left.\frac{d^2}{ds^2}\log L(s)\right|_{s=2t},\qquad t=\Re u.
\]
For \(t\) in a fixed compact interval, the finite-parameter intensity has the refined expansion
\[
\rho_\beta(t)=\rho(t)-\frac{1}{6\pi\beta^2}
\left.\frac{d^2}{ds^2}\bigl(L(s)^{-1}\bigr)\right|_{s=2t}
+O(\beta^{-4}).
\]
The profile connects two quantitatively different regimes:
\[
\rho(t)\sim\frac1{2\pi t^2}\quad(t\to-\infty),\qquad
\rho(t)\sim\frac{e^t}{4\pi}\quad(t\to+\infty).
\]
The second-order intensity correction is not identically zero, hence the displayed \(\beta^{-2}\) scale is genuinely present. For any fixed \(a<b\), the expected number of zeros of \(F_\beta\) in \(e^{a/\beta}<|z|<e^{b/\beta}\), divided by \(\beta\), tends to \((\log L)'(2b)-(\log L)'(2a)\).

The statement concerns the *unconditioned* zero process and the large-exponent limit; it makes no claim about zeros conditioned on a large disk hole.

## Assumptions and scope

The coefficient variance in \(F_\beta\) is exactly \(\Gamma(2(n+1)/\beta)^{-1}\), with no additional radial normalization. All limits in \(\beta\) are over arbitrary real \(\beta\to+\infty\). Convergence of fields is in \(\operatorname{Hol}(\mathbb C)\) with its compact-open topology; zero measures are counted with multiplicities. Compact-uniform error estimates also hold after any fixed number of derivatives in the real and imaginary components of \(u,v\). The tail limits \(t\to\pm\infty\) are taken **after** the \(\beta\to\infty\) limit; there is no claim of uniformity in jointly diverging \(\beta,t\).

## Proof

**1. Convergence and covariance expansion.** Set \(h=1/\beta\), \(s=u+\bar v\), and \(g_s(x)=e^{sx}/\Gamma(2x)\) for \(x\ge0\). Independence and circularity give the exact covariance and pseudocovariance
\[
K_\beta(u,v)=h\sum_{k=1}^\infty g_s(kh),\qquad
\mathbb E[G_\beta(u)G_\beta(v)]=0.
\]
Stirling's formula implies that \(g_s\) and all of its derivatives decrease superexponentially as \(x\to\infty\), uniformly with \(s\) in compact subsets of \(\mathbb C\). Near zero, the reciprocal Gamma function is entire, with
\[
\Gamma(2x)^{-1}=2x+4\gamma x^2+
\bigl(4\gamma^2-2\pi^2/3\bigr)x^3+O(x^4),
\]
so \(g_s(0)=0\) and \(g_s'(0)=2\) for every \(s\). Euler–Maclaurin summation on the half-line, with integrated fourth-derivative remainder, gives
\[
h\sum_{k=1}^\infty g_s(kh)
=\int_0^\infty g_s(x)\,dx
-\frac{B_2}{2!}h^2g_s'(0)+O_C(h^4)
=L(s)-\frac{h^2}{6}+O_C(h^4).
\]
The integrable derivative bounds yield the same formula after any prescribed \(s\)-derivatives. In fact the next term is \(h^4\bigl((s+2\gamma)^2-2\pi^2/3\bigr)/120\), but it is not needed. In particular \(K_\beta\to K=L(u+\bar v)\) locally uniformly with all derivatives. The integral kernel is positive definite, being the Gram kernel of the functions \(x\mapsto e^{ux}/\sqrt{\Gamma(2x)}\) in \(L^2((0,\infty),dx)\); it is strictly positive on the diagonal. The associated Gaussian analytic field \(G\) can be constructed as the complex isonormal integral \(\int_0^\infty e^{ux}\Gamma(2x)^{-1/2}\,dB(x)\).

For every finite set of points, the centered proper Gaussian vectors converge by their covariance matrices. On a compact disk, uniform bounds for the second moment on a slightly larger disk give compact-open tightness through the submean estimate for analytic functions and Cauchy's inequality. Hence \(G_\beta\Rightarrow G\) in \(\operatorname{Hol}(\mathbb C)\). The joint law of \((G(u),G'(u))\) is nonsingular at each \(u\): its covariance determinant is \(L(2t)^2\operatorname{Var}_{2t}(X)>0\), where \(X\) has probability density proportional to \(e^{2tx}/\Gamma(2x)\) on \((0,\infty)\). Therefore almost surely \(G\) has no multiple zero: on the event \(\sup_K|G''|\le M\), a double zero within mesh distance \(\delta\) of a grid point forces \(|G|\le C M\delta^2\) and \(|G'|\le C M\delta\) there; the uniformly bounded four-real-dimensional Gaussian density makes the probability \(O_M(\delta^6)\) at each point, and there are \(O(\delta^{-2})\) grid points. Letting \(\delta\downarrow0\), then \(M\uparrow\infty\), excludes all double zeros on every compact set. Its expected zero measure has a locally bounded density, so a fixed smooth boundary has no zero almost surely. Rouché's theorem / continuity of zeros then yields convergence of counting measures on all compact domains with such boundaries, hence vague convergence.

Vertical shifts leave \(K(u,v)\) invariant under simultaneous translation. For \(u,v\) fixed,
\[
K(u+it,v)=\int_0^\infty\frac{e^{x(u+\bar v)}e^{itx}}{\Gamma(2x)}\,dx\longrightarrow0
\quad (|t|\to\infty)
\]
by the Riemann–Lebesgue lemma. Joint proper Gaussian vectors in widely separated translated compact windows thus become independent in distribution. This proves mixing of the Gaussian field and of its zero process.

**2. Intensity and its correction.** For a proper GAF with nonzero diagonal covariance \(K(u,u)\), the Edelman–Kostlan identity reads
\[
\mathbb E[n_G](du)=\frac1{4\pi}\Delta\log K(u,u)\,dA(u).
\]
Since \(K(u,u)=L(2\Re u)\), this gives \(\rho(t)=\pi^{-1}(\log L)''(2t)\). It is strictly positive: \((\log L)''(s)\) is the variance of \(X\) under the exponentially tilted probability measure of density \(e^{sx}/(\Gamma(2x)L(s))\), which is not a point mass. Since \(L(2t)>0\), taking a logarithm of the Euler–Maclaurin expansion and differentiating twice yields, compact uniformly,
\[
(\log K_\beta(s))''=(\log L(s))''-\frac{h^2}{6}(L(s)^{-1})''+O(h^4).
\]
Thus the claimed correction is valid. As \(s\to-\infty\), \(L(s)\sim2s^{-2}\), so \((L^{-1})''(s)\to1\); the correction cannot vanish identically.

**3. Two tails of the profile.** For \(s\to-\infty\), substitute \(x=y/(-s)\) in the defining integral. The expansion \(\Gamma(2x)^{-1}=2x+O(x^2)\), with exponential-tail domination, shows that under the tilted measure \((-s)X\) converges in moments up to order two to a Gamma law of shape two and unit rate. Consequently \(\operatorname{Var}_s(X)\sim2/s^2\), proving the left tail.

For \(s\to+\infty\), write \(z=e^{s/2}\), \(Y=2X\). Its tilted density is proportional to \(z^y/\Gamma(y)\) on \(y>0\). Stirling's formula gives, uniformly for \(y=z+v\sqrt z\) with bounded \(v\),
\[
\log\bigl(z^y/\Gamma(y)\bigr)=z+\tfrac12\log(z/2\pi)-\tfrac12v^2+o(1).
\]
The phase is strictly concave because its second derivative is \(-\psi_1(y)<0\); its unique maximizer satisfies \(\psi(y_0)=\log z\) and \(y_0=z+1/2+O(z^{-1})\). Uniformly for \(z/2\le y\le2z\), Stirling bounds give \(c/z\le\psi_1(y)\le C/z\), hence a Gaussian bound \(\exp[-c(y-y_0)^2/z]\) relative to the maximal integrand. Outside this interval, the slope \(\log z-\psi(y)\) is bounded away from zero with its appropriate sign, so the remaining weighted second moments are exponentially smaller than the central mass. The local Taylor expansion on \(|y-y_0|\le z^{2/3}\) then gives both convergence in law and uniform integrability through order two: \((Y-z)/\sqrt z\Rightarrow N(0,1)\) and \(\operatorname{Var}(Y)\sim z\). Hence \(\operatorname{Var}_s(X)\sim e^{s/2}/4\). Substituting \(s=2t\) gives the right tail.

**4. Annular count.** For a radial Gaussian power series with diagonal variance \(M_\beta(r)=\sum_{n\ge0}r^{2n}/\Gamma(2(n+1)/\beta)\), the zero intensity identity and polar integration give
\[
\mathbb E\,N_\beta(D(0,r))=\tfrac12r\,\frac{d}{dr}\log M_\beta(r).
\]
Set \(r=e^{t/\beta}\). The right side divided by \(\beta\) equals \(\tfrac12\partial_t\log M_\beta(e^{t/\beta})=(\log K_\beta)'(2t)-1/\beta\), because \(K_\beta(t,t)=e^{2t/\beta}M_\beta(e^{t/\beta})/\beta\). The common term \(-1/\beta\) cancels on subtracting the two radii. Compact-uniform convergence with derivatives therefore gives the asserted annular difference.

## Verification

The supplementary `CHECK.py` evaluates independent quadratures of \(L\) and its first two derivatives and of the exact positive series \(K_\beta\), then tests the predicted \(-1/6\) covariance coefficient and the intensity correction at several fixed points. The computation is a numerical consistency test only; the infinite statements above follow from Euler–Maclaurin summation, Gaussian analytic tightness, Rouché continuity and asymptotic moment arguments. The covariance can also be reproduced directly from its displayed positive series, without numerical root finding.

## Relationship to prior work

The underlying power-exponential Gaussian entire family was studied by Y.-H. Du (arXiv:2602.24193v1, first submitted 27 February 2026) for **large-radius conditional hole events at fixed exponent**. The present theorem instead concerns the **unconditioned large-exponent microscopic limit**; one result does not imply the other through a change of radius. General Gaussian analytic zero-intensity and compact-open convergence tools are standard (Hough–Krishnapur–Peres–Virág; Sodin), and Euler–Maclaurin and Stirling methods are classical. The new conclusion is the specific reciprocal-Gamma interpolation profile, its two limiting regimes, and the explicit rank-one second-order covariance defect for this family. The motivating full text was not accessible beyond its abstract and first publisher-preview page; absence of an earlier equivalent theorem is therefore not independently certified.

## Limitations

The limit is local in the logarithmic coordinate; it does not cover jointly diverging \(t\) and \(\beta\), conditioned large holes, extreme zeros or higher-order correlation asymptotics. The compound source is not fully inspected, and an equivalent large-exponent result using a different weight or Volterra-function normalization is a residual originality risk.

## References

- Y.-H. Du, *Hole Phenomenon of Gaussian Analytic Functions with Power-exponential Weights*, arXiv:2602.24193v1 (first public preprint 27 February 2026), https://arxiv.org/abs/2602.24193 ; International Journal of Mathematics, 2026, DOI 10.1142/S0129167X26500588.
- J. B. Hough, M. Krishnapur, Y. Peres and B. Virág, *Zeros of Gaussian Analytic Functions and Determinantal Point Processes*, American Mathematical Society, University Lecture Series 51 (2009), Chapter 2, DOI 10.1090/ulect/051.
- M. Sodin, *Zeros of Gaussian Analytic Functions*, arXiv:math/0007030 (2000), https://arxiv.org/abs/math/0007030.
- A. Ledoan, M. Merkli and S. Starr, *A Universality Property of Gaussian Analytic Functions*, arXiv:1003.1951 (2010), https://arxiv.org/abs/1003.1951.
