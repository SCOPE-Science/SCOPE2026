# Sharp admissibility and hidden rank predictability in a two-harmonic cosine copula

## Finding
For real parameters \(a,b\), consider the absolutely continuous, symmetric, two-harmonic cosine copula candidate with density
\[
c_{a,b}(u,v)=1+2a\cos(2\pi u)\cos(2\pi v)+2b\cos(4\pi u)\cos(4\pi v),\qquad 0\le u,v\le1.
\]
Its CDF is a copula **if and only if**
\[
-\frac12\le b\le\frac12,\qquad |a|\le
\begin{cases}
\dfrac{1+2b}{2},&-\dfrac12\le b\le\dfrac16,\\[3pt]
2\sqrt{b(1-2b)},&\dfrac16\le b\le\dfrac12.
\end{cases}
\]
For every admissible parameter pair, Spearman's rho and Kendall's tau are both identically zero, yet the symmetric population Chatterjee coefficient is
\[
\xi(V\mid U)=\xi(U\mid V)=\frac{3}{2\pi^2}\left(a^2+\frac{b^2}{4}\right).
\]
In particular, the **sharp maximum within this entire two-harmonic family** is
\[
\boxed{\max\xi=\frac{24}{31\pi^2}},
\]
attained exactly at \(b=8/31\) and \(a=\pm4\sqrt{30}/31\). The stationary reversible Markov transition operator of the copula has sharp maximal nonconstant-mode correlation \(1/\sqrt2\), attained at \(b=1/4\) and \(a=\pm1/\sqrt2\), as opposed to the universal \(|a|+|b|\le1/2\) sufficient-domain restriction in the originating construction. All these limits permit nonnegative densities that may vanish at isolated or boundary points.

## Assumptions and scope
The variables \(U,V\) have uniform margins on \([0,1]\), and the two frequencies are exactly \(1\) and \(2\) in the cosine basis of Longla's sine–cosine copula family. Parameters \(a,b\) are unrestricted real numbers before the positivity test. A candidate with the displayed density has uniform margins automatically, because the integral of each positive-frequency cosine over \([0,1]\) vanishes. Hence the density being nonnegative everywhere is necessary and sufficient for copula validity. The CDF is
\[
C_{a,b}(u,v)=uv+\frac{a}{2\pi^2}\sin(2\pi u)\sin(2\pi v)
+\frac{b}{8\pi^2}\sin(4\pi u)\sin(4\pi v).
\]
The Chatterjee coefficient is the population conditional-CDF functional, not a finite-sample estimate:
\[
\xi(V\mid U)=6\int_0^1\!\int_0^1
\bigl[\Pr\{V\le v\mid U=u\}-v\bigr]^2\,du\,dv.
\]
The maximal-mode correlation is the supremum of the absolute Pearson correlation of centered square-integrable functions of two successive states of the stationary copula Markov chain; no claim about an optimal test, finite-sample efficiency, or universal extremality among arbitrary copulas is made.

## Proof
Put \(x=\cos(2\pi u)\), \(y=\cos(2\pi v)\). Since \(\cos(4\pi u)=2x^2-1\), the density is the polynomial
\[
p(x,y)=1+2axy+2b(2x^2-1)(2y^2-1),\qquad -1\le x,y\le1.
\]
Write \(A=|a|\), \(s=|x|\), \(t=|y|\) and \(z=st\in[0,1]\). Both signs of \(xy\) are attainable independently of \((s,t)\); thus the least density at these magnitudes is
\[
1-2Az+2b\bigl(4z^2-2(s^2+t^2)+1\bigr).
\]
For fixed product \(z=st\), the exact attainable extrema are
\[
2z\le s^2+t^2\le1+z^2.
\]
The lower bound follows from \((s-t)^2\ge0\) and is attained at \(s=t=\sqrt z\); the upper bound follows from \((1-s^2)(1-t^2)\ge0\) and is attained at \((s,t)=(1,z)\). These inequalities include \(z=0,1\), so the reduction involves no missing endpoints.

If \(b<0\), the least density at fixed \(z\) occurs at \(s^2+t^2=2z\), and equals
\[
q_-(z)=1-2Az+2b(2z-1)^2.
\]
This is a concave quadratic in \(z\); its global minimum on \([0,1]\) lies at an endpoint. Since \(A\ge0\), the smaller endpoint value is \(q_-(1)=1+2b-2A\), hence validity is precisely \(A\le(1+2b)/2\) with \(-1/2\le b<0\). At \(b=0\), the same inequality follows from \(1-2Az\ge0\).

If \(b>0\), the least density at fixed \(z\) occurs at \(s^2+t^2=1+z^2\), giving the convex quadratic
\[
q_+(z)=1-2b-2Az+4bz^2.
\]
When \(A\ge4b\), its minimum is \(q_+(1)=1+2b-2A\); when \(A\le4b\), the minimizing point is \(z=A/(4b)\) with minimum \(1-2b-A^2/(4b)\). These two branches meet at \(b=1/6\). More explicitly, if \(0<b\le1/6\), all \(A\le4b\) pass and the remaining domain is \(4b\le A\le(1+2b)/2\). If \(1/6\le b\le1/2\), the condition is exactly \(A\le2\sqrt{b(1-2b)}\), with the endpoint at \(A=4b\) allowed only for \(b=1/6\). Necessity outside the displayed region is witnessed by the attaining \((s,t)\) above and suitable signs of \(x,y\); hence the phase diagram is **necessary and sufficient**, not merely a sufficient norm bound.

For the rank functional, differentiating the CDF gives the conditional distribution
\[
\Pr\{V\le v\mid U=u\}=v+\frac{a}{\pi}\cos(2\pi u)\sin(2\pi v)
+\frac{b}{2\pi}\cos(4\pi u)\sin(4\pi v).
\]
Orthogonality of distinct integer Fourier harmonics and their squared integrals \(1/2\) give
\(\xi=3(a^2+b^2/4)/(2\pi^2)\). The copula is symmetric, giving the reverse-direction equality. To optimize, for fixed \(b\) choose \(|a|\) at the positive boundary. For \(-1/2\le b\le1/6\) the bracket becomes \(1/4+b+5b^2/4\), a convex function whose largest endpoint value is \(65/144\). For \(1/6\le b\le1/2\), the bracket becomes \(4b-31b^2/4\), strictly concave with a unique maximum \(16/31\) at \(b=8/31\), which exceeds \(65/144\). The corresponding coefficient and unique maximizers up to the sign of \(a\) follow.

For concordance, the integral formula \(\rho_S=12\iint C_{a,b}\,du\,dv-3\) is zero because each sine factor has integral zero. Also \(\tau=4\iint C_{a,b}(u,v)c_{a,b}(u,v)\,du\,dv-1=0\): every perturbation integral vanishes by \(\int_0^1\sin(2\pi j u)du=\int_0^1u\cos(2\pi j u)du=\int_0^1\sin(2\pi j u)\cos(2\pi k u)du=0\), for positive integers \(j,k\). Finally, the orthonormal functions \(\sqrt2\cos(2\pi u)\) and \(\sqrt2\cos(4\pi u)\) are eigenfunctions of the stationary transition operator with eigenvalues \(a\) and \(b\); all remaining centered eigenvalues are zero. Hence the maximal correlation equals \(\max\{|a|,|b|\}\). The phase boundary shows \(\max|b|=1/2\), and \(|a|\) has unique maximum \(1/\sqrt2\) at \(b=1/4\), proving the stated sharp spectral cap.

## Verification
The standalone `verify.py` uses exact symbolic algebra for both reduced density polynomials, checks the junction \(b=1/6\), the optimal rank-predictability parameter \(b=8/31\), Fourier orthogonality, and independent rational admissibility probes. It also reports the exact equations used to reproduce all phase boundaries. The analytic \(s^2+t^2\) extrema and one-variable convexity arguments provide the global proof; finite probes alone are not used as proof. The checker requires Python 3 and SymPy and can be run with `python verify.py`.

## Relationship to prior work
Longla's *New copula families and mixing properties* (first public preprint 21 August 2023, published 2024), Sections 2.1–2.2 and equations (7), (15), introduces the general orthogonal sine–cosine perturbation and uses the sufficient restriction \(\sum_k(|\lambda_k|+|\mu_k|)\le1/2\). Its Lemma 2 and Remark 3 establish vanishing classical concordance for cosine-only modes; those are acknowledged, **not** claimed new. The 2025 follow-up by Longla and Hamadou uses this same restricted parameter domain for inference and gives no full two-cosine-mode admissibility region in its inspected model, estimator, and likelihood sections. Chatterjee's coefficient is a pre-existing general dependence functional. The new content is the **complete curved necessary-and-sufficient two-harmonic admissibility domain together with its sharp within-family Chatterjee and spectral extrema**, which do not follow numerically from the prior sufficient diamond or generic global copula inequalities. A previously indexed two-mode shifted-Legendre copula gives a different basis and different positivity constraints, not a direct implication for this trigonometric density. Published global Chatterjee–Spearman inequalities likewise do not optimize within this two-parameter harmonic subfamily.

## Limitations
The phase diagram pertains only to the two specified diagonal cosine harmonics, not arbitrary frequencies, sine terms, other orthogonal bases, or all square-integrable copulas. The value \(24/(31\pi^2)\) is sharp **within this family** and is not asserted to be the maximum among all zero-concordance copulas. Boundary copula densities may vanish, so arguments requiring strict positivity of the transition density must be checked separately. No independent mathematical audit or historical-uniqueness certification has been performed; unindexed or inaccessible prior calculations remain a priority risk.

## References
1. Martial Longla, *New copula families and mixing properties*, arXiv:2308.11074, first submitted 21 August 2023; *Statistical Papers* 65 (2024), 4331–4363. https://arxiv.org/abs/2308.11074 and https://doi.org/10.1007/s00362-024-01559-9.
2. Martial Longla and Mous-Abou Hamadou, *Estimation problems for some perturbations of the independence copula*, *Statistical Papers* 66 (2025), article 156. https://doi.org/10.1007/s00362-025-01778-8.
3. Sourav Chatterjee, *A New Coefficient of Correlation*, *Journal of the American Statistical Association* 116 (2021), 2009–2022. https://doi.org/10.1080/01621459.2020.1758115.
4. Holger Dette, Karl F. Siburg, and Pavel A. Stoimenov, *A copula-based non-parametric measure of regression dependence*, *Scandinavian Journal of Statistics* 40 (2013), 21–41. https://doi.org/10.1111/j.1467-9469.2011.00767.x.
