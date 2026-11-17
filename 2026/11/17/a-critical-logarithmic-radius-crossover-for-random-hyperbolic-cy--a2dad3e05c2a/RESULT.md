# A critical logarithmic-radius crossover for random hyperbolic cyclic-polygon area

## Finding
In the hyperbolic plane of curvature \(-1\), sample \(n\ge3\) points independently and uniformly by arclength on a centered geodesic circle of radius \(R_n>0\). Let \(P_n\) be their geodesic convex hull and let \(A_n\) be its hyperbolic area. Write
\[
q_n=\tanh^2(R_n/2),\qquad \lambda_n=n(1-q_n)=n\operatorname{sech}^2(R_n/2).
\]
**Critical window.** If \(\lambda_n\to\lambda\in(0,\infty)\), then
\[
\frac{A_n}{n}\xrightarrow{L^2}\Phi(\lambda)
=2\int_0^\infty e^{-x}\arctan\!\left(\frac{2\pi x}{\lambda}\right)\,dx.
\]
The area of the containing hyperbolic disk is \(B_n=4\pi q_n/(1-q_n)\), and hence \(A_n/B_n\to\Psi(\lambda)=\lambda\Phi(\lambda)/(4\pi)\) in probability. The function \(\Psi\) is continuous and strictly increasing from zero to one. Thus a logarithmically growing radius produces a nontrivial, invertible area-coverage transition. More precisely \(R_n=\log(4n/\lambda)+o(1)\) in this window.

**Gaussian critical fluctuations.** If \(q_n=1-\lambda/n\) for all sufficiently large \(n\), let \(E\) be exponentially distributed with mean one, and define
\[
c=2\pi/\lambda,\quad g(x)=2\arctan(cx),\quad
\alpha=\mathbb E[E g'(E)]=2c\mathbb E\left[\frac{E}{1+c^2E^2}\right],
\]
\[
\sigma^2(\lambda)=\operatorname{Var}(g(E)-\alpha E)>0.
\]
Then
\[
\sqrt n\left(\frac{A_n}{n}-\Phi(\lambda)\right)
\Longrightarrow N(0,\sigma^2(\lambda)).
\]
The same central limit theorem holds when \(\lambda_n=\lambda+o(n^{-1/2})\). If \(\lambda_n\to0\), then \(A_n/n\to\pi\) in probability (the ideal-polygon regime). If \(\lambda_n\to\infty\), then \(A_n/B_n\to1\) in probability (the disk-filling regime). These regimes classify positive radius sequences for which \(\lambda_n\) has a limit in the extended interval \([0,\infty]\); oscillating parameters need not produce a single limiting fraction.

The critical profile has explicitly different endpoint behaviors:
\[
\Phi(\lambda)=\pi-\frac{\lambda}{\pi}\left(\log\frac{2\pi}{\lambda}+1-\gamma\right)+o(\lambda)
\quad(\lambda\downarrow0),
\]
\[
\Phi(\lambda)=\frac{4\pi}{\lambda}-\frac{32\pi^3}{\lambda^3}+O(\lambda^{-5})
\quad(\lambda\to\infty),
\]
where \(\gamma\) is Euler's constant.

## Assumptions and scope
The hyperbolic curvature is normalized to \(-1\). The vertices are independent and uniform with respect to hyperbolic arclength on the same centered circle; this is equivalent to independent uniform angular coordinates in the Poincaré disk. Hull edges are shortest hyperbolic geodesic segments, and area uses the hyperbolic area form. We take \(n\to\infty\); the Gaussian statement requires the specified critical-window accuracy. No claim is made for nonuniform boundary densities, arbitrary convex domains, or a Gaussian fluctuation law outside the critical window.

## Proof
**1. Exact geometric area identity.** In the Poincaré disk, circle points are \(z_j=\rho e^{i\theta_j}\), with \(\rho=\tanh(R_n/2)\) and \(q=\rho^2\). In ascending cyclic order, let \(\delta_j=\theta_{j+1}-\theta_j\) modulo \(2\pi\), so \(\sum_j\delta_j=2\pi\). The area form is \(4(1-|z|^2)^{-2}\,dx\wedge dy\). Its primitive \(2|z|^2(1-|z|^2)^{-1}\,d\arg z\), integrated along a geodesic from \(\rho e^{i\theta}\) to \(\rho e^{i(\theta+t)}\), gives the oriented area contribution
\[
F_q(t)=2\operatorname{Arg}(1-qe^{-it})
=2\operatorname{atan2}(q\sin t,1-q\cos t).
\]
This follows by mapping the initial vertex to the disk origin with a Möbius isometry, along whose radial geodesic the pulled-back primitive vanishes; the primitive changes by the exact differential of the argument of the Möbius denominator. Stokes' theorem therefore yields the **exact** identity
\[
A_n=\sum_{j=1}^n F_{q_n}(\delta_j).
\tag{1}
\]
When a gap exceeds \(\pi\), its contribution can be negative, but the oriented sum still equals the positive polygon area. The identity is also independently checked against the Gauss--Bonnet interior-angle formula in the supplied checker.

For every \(n\ge3\), the normalized gaps have a \(\operatorname{Dirichlet}(1,\ldots,1)\) distribution. Thus \(\delta_j=2\pi E_j/(E_1+\cdots+E_n)\), where the \(E_j\) are independent unit exponentials. In particular, the exact finite-sample mean is
\[
\mathbb E[A_n/n]=(n-1)\int_0^1 F_{q_n}(2\pi u)(1-u)^{n-2}\,du.
\tag{2}
\]

**2. Critical law.** Write \(\overline E_n=n^{-1}\sum_j E_j\), and let \(G_{n,\lambda}(x)=F_{1-\lambda/n}(2\pi x/n)\). For any fixed \(\lambda>0\), Taylor expansion of sine and cosine gives
\[
G_{n,\lambda}(x)=g(x)+O_\lambda((x+x^3)/n)
\]
for \(x\) in a range at most a fixed multiple of \(\log n\), with \(g(x)=2\arctan(2\pi x/\lambda)\). Standard exponential maximum and empirical-mean bounds imply that the complement of this range has probability decaying faster than \(n^{-2}\). The average of the errors over the normalized exponential spacings is \(O_{L^2}(n^{-1})\). Thus
\[
\frac{A_n}{n}=\frac1n\sum_{j=1}^n g(E_j/\overline E_n)+O_{L^2}(n^{-1}).
\tag{3}
\]
As \(\overline E_n\to1\) and \(g\) is bounded and continuously differentiable, the law of large numbers gives the asserted \(L^2\) limit \(\Phi(\lambda)=\mathbb E[g(E)]\). For general \(\lambda_n\to\lambda\), the same conclusion follows by continuity and the boundedness of the summands. The formula for \(B_n\) gives the area-ratio limit.

**3. Central limit theorem.** Taylor expansion in the random denominator \(\overline E_n\), followed by the independent central limit theorem, yields
\[
\sqrt n\left[\frac1n\sum_jg(E_j/\overline E_n)-\mathbb E g(E)\right]
=\frac1{\sqrt n}\sum_j\{g(E_j)-\mathbb E g(E)-\alpha(E_j-1)\}+o_p(1),
\]
where \(\alpha=\mathbb E[E g'(E)]\). Equation (3) makes its remainder negligible on this scale. Since \(g\) is nonaffine on \((0,\infty)\), \(\sigma^2(\lambda)>0\). The stated accuracy condition on \(\lambda_n\) ensures that changing the window parameter does not shift the limiting centering.

**4. Boundary regimes and monotonicity.** If \(\lambda_n\to0\), then \(q_n\to1\); for typical exponential spacings \(F_{q_n}(\delta_j)\to\pi\), since \((1-q_n)/\delta_j\to0\). Boundedness by \(\pi\) and the empirical gap law yield \(A_n/n\to\pi\). If \(\lambda_n\to\infty\), the relevant gaps satisfy \(\delta_j/(1-q_n)\to0\) in the size-biased empirical mean. Their normalized contribution obeys \(F_{q_n}(\delta_j)/\delta_j\sim2q_n/(1-q_n)\), and summation of \(\delta_j\) gives \(A_n/B_n\to1\). The contribution of exceptional macroscopic gaps is exponentially small in \(n\).

Strict decrease of \(\Phi\) follows by differentiating the integrand. For \(\Psi\), rewrite
\[
\Psi(\lambda)=\mathbb E\left[E\,\frac{\arctan(2\pi E/\lambda)}{2\pi E/\lambda}\right].
\]
Because \(\arctan(y)/y\) strictly decreases with \(y>0\), this expression strictly increases with \(\lambda\); dominated convergence gives endpoint limits zero and one. For the small-\(\lambda\) expansion, differentiate \(I(b)=\mathbb E[\arctan(b/E)]\): \(I'(b)=\int_0^\infty e^{-x}x/(x^2+b^2)\,dx=-\log b-\gamma+o(1)\), and integrate from zero to \(b=\lambda/(2\pi)\). For large \(\lambda\), expand \(\arctan(2\pi E/\lambda)\) and use \(\mathbb E[E]=1\), \(\mathbb E[E^3]=6\), with exponential-tail control.

## Verification
Run `python checks/hyperbolic_circle_checker.py` after installing the packages in `checks/requirements.txt`. The checker compares (1) with a separately implemented Gauss--Bonnet angle calculation for random polygons; integrates (2) for finite \(n\); evaluates \(\Phi,\alpha,\sigma^2\) independently through one-dimensional quadrature; and compares independent exponential-spacing simulations with the finite-sample mean and the critical normal variance. The diagnostic output ends with `HYPERBOLIC_CYCLIC_CRITICAL_AREA_CHECK_OK`. Such finite calculations are consistency checks, not replacements for the limiting arguments.

## Relationship to prior work
Hyperbolic cyclic-polygon existence and uniqueness and triangle-coordinate area formulas are classical or previously established; they are not claimed as new. The distinctive result here is the logarithmic-radius / sample-size coupling, its strictly invertible area-coverage profile, its two boundary regimes and nondegenerate critical Gaussian law. The probabilistic machinery uses standard exponential/Dirichlet spacings and the classical delta method. Closest compared sources address hyperbolic polygon geometry without this stochastic critical scaling, Euclidean random-polygon area fluctuations, or different hyperbolic geometric probabilities. Priority over any unindexed equivalent treatment is not independently certified.

## Limitations
The limit is an asymptotic theorem for boundary-uniform sampling on a constant-curvature disk, not a universal law for all hyperbolic random convex sets. The central limit theorem is stated only for a fixed positive crossover parameter and sufficiently accurate tuning. The reference corpus is not exhaustive; independent mathematical and historical validation remain outstanding.

## References
- H. Bao and X. Chen, "A New Hyperbolic Area Formula of a Hyperbolic Triangle and Its Applications," *Journal of Mathematics* (2014), DOI: 10.1155/2014/838497. First published 2014-08-13. Open full text: https://onlinelibrary.wiley.com/doi/10.1155/2014/838497.
- H. Kourimska, L. Skuppin and B. Springborn, "A variational principle for cyclic polygons with prescribed edge lengths," arXiv:1506.08069, first posted 2015-06-26. https://arxiv.org/abs/1506.08069.
- I. Barany and W. Steiger, "On the variance of random polygons," *Computational Geometry* 46 (2013), 173--180, DOI: 10.1016/j.comgeo.2012.01.003. Different Euclidean interior-sampling setting.
