# Fixed-time stretched spatial tails and jointly selected disorder in tempered fractional Laplace transport

## Finding

For the gamma-clock, gamma-diffusivity tempered fractional Laplace transport model defined below, the **fixed-positive-time** far-displacement density has a sharp stretched-exponential equivalent, including the previously unresolved multiplicative contribution of finite correlation time. Moreover, conditioning on an extreme observed displacement selects *both* the diffusivity and operational clock at a common large scale, with a universal negatively correlated bivariate-Gaussian fluctuation law.

Define
\[
 a=H\Gamma(2H)\tau^{2H-1},\qquad c=(2H-1)\tau,\qquad
 q_x=\left(\frac{\lambda x^2}{4a\beta}\right)^{1/3},\qquad k=\lambda t.
\]
For every fixed \(t>0\), \(1/2<H<1\), and \(\tau,\lambda,\beta,\alpha>0\), as \(|x|\to\infty\) the even displacement density satisfies
\[
 \boxed{p_t(x)\sim
 \frac{\sqrt{\pi\lambda}}{\sqrt{3a\beta}\,\Gamma(\alpha)\Gamma(k)}
 q_x^{\alpha+k-2}\exp(-3q_x-\lambda c).}
\]
In particular, its ultimate fixed-time logarithmic far-tail scale is \(|x|^{2/3}\), not \(|x|\).

Write \(D\) for the static diffusivity and \(S_t\) for the gamma operational time. Under the Bayes conditional density of these variables given \(X_t=x\ne0\), put \(U_x=D/(\beta q_x)\) and \(W_x=\lambda S_t/q_x\). Then
\[
 (U_x,W_x)\ \xrightarrow{\mathbb P}\ (1,1),\qquad
 \sqrt{q_x}\begin{pmatrix}U_x-1\\W_x-1\end{pmatrix}
 \ \xrightarrow{d}\
 \mathcal N\!\left(\begin{pmatrix}0\\0\end{pmatrix},
 \frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix}\right).
\]
Consequently the asymptotic Gaussian correlation of the two *fluctuating, conditioned latent variables* is \(-1/2\). This statement concerns the regular conditional distribution given a displacement value, not the a priori independent \(D\) and \(S_t\).

## Assumptions and scope

Start at position zero. Let \(D\) be gamma with shape \(\alpha>0\), scale \(\beta>0\), and density \(d^{\alpha-1}e^{-d/\beta}/[\Gamma(\alpha)\beta^\alpha]\). Independently, let \(S_t\) have gamma shape \(k=\lambda t>0\), rate \(\lambda>0\), and density \(\lambda^k s^{k-1}e^{-\lambda s}/\Gamma(k)\), so \(\mathbb E S_t=t\). Assume the conditional normal law \(X_t\mid(D,S_t)=(d,s)\sim\mathcal N(0,2dV(s))\), with
\[
 V(s)=H(2H-1)\tau^{2H}\left[
 \frac{s}{\tau}\gamma\!\left(2H-1,\frac{s}{\tau}\right)
 -\gamma\!\left(2H,\frac{s}{\tau}\right)\right],\quad s>0.
\]
The incomplete gamma function is \(\gamma(\rho,z)=\int_0^z y^{\rho-1}e^{-y}\,dy\). All parameters are held fixed as \(|x|\to\infty\); there is no assertion of uniformity when time, tempering, or gamma parameters also vary. This one-time statement does not require independence of successive increments of the parent Gaussian process.

## Proof

**1. Exact Gaussian mixture.** The assumed conditional normal law yields
\[
 p_t(x)=\frac{\lambda^k}{\Gamma(\alpha)\Gamma(k)\beta^\alpha\sqrt{4\pi}}
 \int_0^\infty\!\int_0^\infty
 d^{\alpha-3/2}s^{k-1}V(s)^{-1/2}
 \exp\!\left(-\frac d\beta-\lambda s-\frac{x^2}{4dV(s)}\right)\,dd\,ds.
 \tag{1}
\]
For each \(x\ne0\), the normal density at \(x\) is bounded uniformly over all positive variances, so \(0<p_t(x)<\infty\). Normalizing the integrand in (1) defines the Bayes version of the regular conditional law for every such \(x\); no choice of version at zero enters the result.

**2. Precise tempered variance asymptotic.** Directly from its nonnegative integral representation,
\[
 V(s)=H(2H-1)\int_0^s(s-y)y^{2H-2}e^{-y/\tau}\,dy.
\]
It follows that \(0<V(s)\le as\) for all \(s>0\), and by extending both integrals to infinity and bounding their exponentially small tails,
\[
 V(s)=a(s-c)+O\!\left(e^{-s/\tau}(1+s/\tau)^{2H-2}\right)
 \quad(s\to\infty).
 \tag{2}
\]
Here \(a=H\Gamma(2H)\tau^{2H-1}\) and \(ac=H(2H-1)\Gamma(2H)\tau^{2H}\). The error in (2) may contain a parameter-dependent dimensional constant and is uniform on any scaled region \(s=q_x w/\lambda\) with \(w\) in a fixed compact subset of \((0,\infty)\).

**3. Scaled phase and unique minimizer.** Set \(q=q_x\), \(d=\beta q u\) and \(s=q w/\lambda\), where \(u,w>0\). Define \(R_q(w)=\lambda V(qw/\lambda)/(aq)\). Because \(V(s)\le as\), we have \(0<R_q(w)\le w\). The exponent in (1) equals
\[
 -q\left[u+w+\frac{1}{uR_q(w)}\right].
\]
For positive \(u,w\), the comparison phase
\[
 \Phi(u,w)=u+w+\frac{1}{uw}\ge3
\]
has equality **only** at \((u,w)=(1,1)\), by arithmetic--geometric mean. Its Hessian there and its inverse are
\[
 B=\begin{pmatrix}2&1\\1&2\end{pmatrix},\qquad
 B^{-1}=\frac13\begin{pmatrix}2&-1\\-1&2\end{pmatrix},\qquad \det B=3.
\]
Equation (2), uniformly on compact positive \((u,w)\) regions, gives
\[
 R_q(w)=w-\frac{\lambda c}{q}+o(q^{-1}),\qquad
 q\left[u+w+\frac{1}{uR_q(w)}\right]
 =q\Phi(u,w)+\frac{\lambda c}{uw^2}+o(1).
 \tag{3}
\]

**4. Localization and density prefactor.** After the substitution, equation (1) has the exact prefactor
\[
 C_0q^{\alpha+k-1},\qquad
 C_0=\frac{\sqrt\lambda}{\sqrt{4\pi a\beta}\,\Gamma(\alpha)\Gamma(k)},
\]
and the remaining amplitude equals
\[
 u^{\alpha-3/2}w^{k-1}R_q(w)^{-1/2}.
\]
On each compact positive region this tends to \(u^{\alpha-3/2}w^{k-3/2}\), and (3) supplies the additional continuous factor \(\exp[-\lambda c/(uw^2)]\). For a uniform noncompact bound, let \(\Phi_q=u+w+1/(uR_q(w))\), so \(\Phi_q\ge\Phi\). The level sets of \(\Phi\) are compact inside the positive quadrant: an upper bound on \(\Phi\) bounds \(u,w\) above and \(uw\) away from zero. By uniqueness of the minimizer, outside any fixed neighborhood of \((1,1)\) we therefore have \(\Phi\ge3+\epsilon\) for some \(\epsilon>0\). For \(q\ge1\), use one unit of the exponent to dominate the possibly singular variance weight. Writing \(v=1/(uR_q(w))\), we have \(R_q(w)^{-1/2}=\sqrt{u}\sqrt{v}\) and \(\sqrt v e^{-v}\) is bounded. Thus
\[
u^{\alpha-3/2}w^{k-1}R_q(w)^{-1/2}e^{-q\Phi_q}
\le M u^{\alpha-1}w^{k-1} e^{-u-w}e^{-(q-1)\Phi}.
\]
The gamma weight on the right is integrable for all \(\alpha,k>0\). On the complement of the neighborhood this gives an integral of order \(O(e^{-(q-1)(3+\epsilon)})=o(e^{-3q}q^{-1})\). Near the saddle, the smooth comparison phase is bounded below by \(3+\eta\lVert(u-1,w-1)\rVert^2\) for some \(\eta>0\), and the amplitude is uniformly bounded. These bounds justify the two-dimensional Laplace method and its use for bounded tests of the centered, rescaled latent variables.

The Gaussian integral about the unique saddle contributes
\[
 \int e^{-\frac q2 z^{\!T}Bz}\,dz\sim\frac{2\pi}{q\sqrt3}.
\]
Multiplying \(C_0q^{\alpha+k-1}\), the limiting saddle amplitude \(1\), the correction \(e^{-\lambda c}\), and \(2\pi/(q\sqrt3)\) produces exactly the displayed density equivalent.

**5. Joint conditional limit.** Conditional on \(X_t=x\), the scaled latent density is the normalized two-dimensional integrand just analyzed. Its mass outside each neighborhood of \((1,1)\) is negligible by the same localization argument. Under \(u=1+z_1/\sqrt q\), \(w=1+z_2/\sqrt q\), Taylor expansion gives \(q(\Phi-3)\to\tfrac12 z^{T}Bz\). The multiplicative correction and gamma powers approach constants, which cancel upon normalization. Gaussian domination in the saddle neighborhood yields weak convergence to the centered normal with covariance \(B^{-1}\); the component variances are \(2/3\) and their covariance \(-1/3\), giving correlation \(-1/2\). This completes the proof.

## Verification

The separately supplied `verify_tail.py` checks the saddle Hessian and inverse **symbolically**. It approximates the single-clock integral obtained by analytically integrating out \(D\) via the modified Bessel function, using finite quadrature in the rescaled clock \(0.04\le w\le4\). For \((H,\tau,\lambda,\beta,\alpha,k)=(0.8,1,2,1,1.7,3)\), its estimates of the density divided by the displayed equivalent at \(q=20,40,80\) are approximately \(1.20144,1.09849,1.04870\). For \((0.65,0.7,1.3,0.9,2.3,1.4)\), the corresponding estimates are approximately \(1.04098,1.02035,1.01014\). The checker also verifies \(0<V(s)<as\) for sampled positive \(s\). These are finite numerical cross-checks, **not** substitutes for the localization and Laplace proof above.

Reproduce with `python verify_tail.py` using Python 3, NumPy, SciPy and SymPy. No observational data or numerical fit is needed for the theorem.

## Relationship to prior work

Zhao, Wang and Metzler (2026) introduce the precise tempered fractional Laplace transport model and derive its complete displacement-mixture integral and an exponential spatial-tail expression in the **long-time clock-self-averaging approximation**. Equations (11)--(12) and (35)--(43) of their paper were read. The result here instead takes \(|x|\to\infty\) at **fixed finite positive time**, without replacing the random clock by its mean. The different order of limits permits a much heavier ultimate spatial tail and leads to joint selection of hidden clock and diffusivity; the long-time approximation is not being invalidated within its own scaling regime.

For exactly linear \(V(s)=as\), one has \(X_t=\sqrt{2aDS_t}\,Z\) in law with \(Z\) an independent standard normal. Then \(\lambda X_t^2/(4a\beta)=(D/\beta)(\lambda S_t)(Z^2/2)\) in law, the product of three independent unit-rate gamma variables of shapes \(\alpha,k,1/2\). This is covered by Gaunt's product-distribution densities and tail asymptotics; Springer and Thompson's earlier work is a foundational product-distribution reference. The generic product saddle exponent and the unshifted reference constant are **not** claimed as new. The contributions here are the specific finite-tempering multiplier \(e^{-\lambda(2H-1)\tau}\) for the nonlinear variance and the joint conditional clock/diffusivity fluctuation law. Wang and colleagues' earlier fractional Laplace motion with drift is related but does not include this finite-tempering, gamma-diffusivity specification. An indexed result on the same tempered model addresses squared-displacement *time-window correlations*, not its fixed-time spatial rare-event limit.

## Limitations

The theorem is for a one-time marginal under positive gamma parameters and \(1/2<H<1\); it does not address negative or zero gamma shapes, simultaneous time--distance scaling, process-level path large deviations, empirical estimation error, or all multidimensional extensions. The asymptotic probability density in a far-tail region can be extremely small, so direct Monte Carlo evidence alone may be misleading. Known general product-tail machinery might imply portions of the local Gaussian saddle behavior through broader unexamined theorems; the assessment makes no priority claim for that general mechanism. Publication novelty remains conditional on external literature coverage and independent scrutiny.

## References

1. Y. Zhao, W. Wang and R. Metzler, *Non-Gaussian transport in tempered fractional Laplace motion*, arXiv:2610.40113v1 (first publicly available 29 October 2026), https://arxiv.org/html/2610.40113v1.
2. R. E. Gaunt, *Products of normal, beta and gamma random variables: Stein operators and distributional theory*, arXiv:1507.07696 (2015), https://arxiv.org/abs/1507.07696.
3. M. D. Springer and W. E. Thompson, *The distribution of products of beta, gamma and Gaussian random variables*, SIAM Journal on Applied Mathematics 18 (1970), https://doi.org/10.1137/0118065.
4. W. Wang et al., *Paradoxical non-Gaussian behavior in fractional Laplace motion with drift*, arXiv:2412.14674 (2024), https://arxiv.org/abs/2412.14674.
