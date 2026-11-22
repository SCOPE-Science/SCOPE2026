# A continuum of stationary-position aliases for two-stage resetting with powered returns

## Finding

A stationary Brownian particle that explores for an Erlang-two renewal time and then returns deterministically to the origin can have **exactly the same full stationary position distribution under uncountably many physically different return protocols**. The parameter fibers, their exact range, an isosbestic point, the complete stochastic ordering, and a phase-resolved recovery mechanism are characterized below.

Let \(\kappa=\sqrt{r/D}\) and let the powered-return speed at traveled distance \(u\) be \(c u^{\alpha}\), with \(0\le\alpha<1\), \(c>0\). Define
\[
 w=\frac{4c\kappa^{1-\alpha}}{4c\kappa^{1-\alpha}+r\Gamma(1-\alpha)(3-\alpha)},\qquad
 b=\frac{w}{4}+\frac{1-w}{3-\alpha}.
\]
For every \(D,r,c>0\) and \(0\le\alpha<1\), the stationary position has density
\[
 \boxed{p_{\alpha,c}(x)=\frac{\kappa}{2}e^{-\kappa|x|}\left[1-b+b\kappa|x|\right].}
\]
Its complete attainable shape interval is \(1/4<b<1/2\). Every \(b\) in this interval arises from uncountably many distinct pairs \((\alpha,c)\): for each
\[
 0\le\alpha<1,\quad \alpha>3-\frac1b,\quad
 c=\frac{r\Gamma(1-\alpha)(3-\alpha)}{4\kappa^{1-\alpha}}
   \frac{(3-\alpha)^{-1}-b}{b-1/4},
\]
the same full density is obtained. Conversely, two members of this family have identical stationary position distributions if and only if their values of \(b\) agree. For fixed \(\alpha\), the shape \(b\) determines \(c\) uniquely.

The absolute-position distribution function and the total variation distance between any two stationary laws are exactly
\[
 \Pr(\kappa|X|\le z)=1-e^{-z}(1+bz)\quad(z\ge0),\qquad
 d_{\rm TV}(p_{b_1},p_{b_2})=\frac{|b_1-b_2|}{e}.
\]
For \(b_1<b_2\), the first absolute-position law is strictly stochastically smaller. All densities share the value \(\kappa/(2e)\) at each of the two nonzero positions \(x=\pm\kappa^{-1}\), and their density differences switch sign there.

As a concrete physical alias, for \(D=r=1\), the constant-speed return \((\alpha,c)=(0,1/2)\) and the constant-acceleration return \((\alpha,c)=(1/2,5\sqrt\pi/4)\) have exactly the same stationary density \(e^{-|x|}(7+3|x|)/20\). Yet the probabilities of observing the particle in the Brownian-exploration phase are \(2/5\) and \(2/3\), respectively. The latter return law has acceleration \(25\pi/32\).

The inverse obstruction disappears with phase-labelled stationary observations: the conditional return-phase second moment identifies \(\alpha\), and the exploration-phase frequency identifies \(c\). Explicitly, if \(M_R=\mathbb E[X^2\mid\text{return}]\), then
\[
 b_R=\frac{\kappa^2 M_R-2}{4}=\frac{1}{3-\alpha},\qquad
 \alpha=3-\frac1{b_R},\qquad
 c=\frac{r\Gamma(1-\alpha)(3-\alpha)}{4\kappa^{1-\alpha}}\frac{w}{1-w}.
\]

## Assumptions and scope

During each exploration phase, a particle begins at \(X=0\) and evolves as one-dimensional Brownian motion with generator \(D\partial_{xx}\), with independent noise across cycles. The exploration time \(T\) has Gamma shape two and rate \(r\), i.e. density \(r^2t e^{-rt}\) for \(t>0\), and is independent of the noise. At time \(T\) the endpoint is \(Y=X_T\). In the return phase, if \(Y\ne0\), the particle moves monotonically along the segment from \(Y\) toward zero, with distance traversed from the endpoint equal to
\[
 u(s)=[(1-\alpha)cs]^{1/(1-\alpha)},\quad
 0\le s\le |Y|^{1-\alpha}/[(1-\alpha)c].
\]
There is no hesitation at the endpoint, no reset while returning, and the next independent exploration starts upon reaching zero. This explicit trajectory selects the immediate-return solution when \(\alpha>0\), for which the equation \(du/ds=cu^\alpha\) alone admits waiting-time solutions. The exceptional event \(Y=0\) has zero probability. All formulas refer to the unique stationary equilibrium-renewal observation law, not to finite-time transients or first-passage search targets. Known \(D,r\) are required for the inverse statement.

## Proof

Set \(z=\kappa|x|\). The heat kernel is \(G_t(x)=(4\pi Dt)^{-1/2}\exp[-x^2/(4Dt)]\). Since \(\Pr(T>t)=e^{-rt}(1+rt)\), the expected exploration occupation density in a complete cycle is
\[
 \rho_D(x)=\int_0^\infty e^{-rt}(1+rt)G_t(x)\,dt
 =\frac{e^{-z}(z+3)}{4\sqrt{Dr}}.
\]
The endpoint density follows by differentiating the heat-kernel resolvent in \(r\):
\[
 g_Y(y)=\int_0^\infty r^2t e^{-rt}G_t(y)\,dt
 =\frac{\kappa}{4}e^{-\kappa|y|}(1+\kappa|y|).
\]
At a point \(x\) strictly between a return endpoint \(y\) and zero, the infinitesimal time per unit position is \(c^{-1}(|y|-|x|)^{-\alpha}\). Therefore the expected return occupation density is
\[
 \begin{aligned}
 \rho_R(x)&=\frac1c\int_{|x|}^\infty g_Y(y)(y-|x|)^{-\alpha}\,dy\\
 &=\frac{\Gamma(1-\alpha)\kappa^\alpha}{4c}
   e^{-z}(z+2-\alpha),
 \end{aligned}
\]
where the last identity uses the two Gamma integrals of orders \(1-\alpha\) and \(2-\alpha\). These integrals exist exactly within the stated range \(\alpha<1\). Their total masses give the mean phase durations
\[
 \mu=\int_{\mathbb R}\rho_D(x)\,dx=\frac2r,
 \qquad \nu=\int_{\mathbb R}\rho_R(x)\,dx
 =\frac{\Gamma(1-\alpha)\kappa^{\alpha-1}(3-\alpha)}{2c}.
\]
These quantities are strictly positive and finite. Regenerative renewal-reward theory therefore yields the stationary density \((\rho_D+\rho_R)/(\mu+\nu)\). The conditional phase densities are
\[
 p_D(x)=\frac\kappa8 e^{-z}(z+3),\qquad
 p_R(x)=\frac\kappa{2(3-\alpha)}e^{-z}(z+2-\alpha).
\]
Writing \(w=\mu/(\mu+\nu)\), their mixture simplifies to the claimed \(p_{\alpha,c}\) with \(b=w/4+(1-w)/(3-\alpha)\).

For each \(\alpha\in[0,1)\), varying \(c\) over positive values makes \(w\) range bijectively over \((0,1)\). Hence \(b\) ranges over \((1/4,1/(3-\alpha))\); its union over \(\alpha<1\) is precisely \((1/4,1/2)\), and solving for \(c\) gives all preimages shown above. Equality of full densities forces equality of \(b\), by evaluation at zero or by the variance identity \(\kappa^2\mathbb E X^2=2+4b\). The admissible return exponents for a given \(b\) contain an open interval, giving uncountably many distinct preimages. The two explicit protocols are verified by their weights \(w=2/5\) and \(w=2/3\), which both yield \(b=3/10\).

Integrating the radial density \(e^{-z}(1-b+bz)\) gives \(1-e^{-z}(1+bz)\). For \(b_1<b_2\) its radial CDF is strictly larger for all \(z>0\). The density difference is \(\kappa(b_1-b_2)e^{-z}(z-1)/2\), so its only nonzero-position crossings occur at \(z=1\) and direct integration of its absolute value yields total variation \(|b_1-b_2|/e\). Finally, conditioning on return gives \(b_R=(3-\alpha)^{-1}\) and \(\kappa^2M_R=2+4b_R\). The observed phase probability \(w\) and known \(D,r\) then determine \(c\) uniquely via the displayed relation.

## Verification

The included standalone `verify.py` numerically re-integrates the Brownian exploration resolvent, the endpoint law, and the singular return occupation integral for three \((D,r)\) choices, four exponents, and three positive positions. It also checks normalization, second moments, exact ballistic/accelerated aliasing, phase recovery, total variation and the common crossing. It passes 192 assertions, including three symbolic moment identities. Near the integrable return-endpoint singularity, quadrature comparisons use relative-or-absolute tolerance \(10^{-12}\). The proof is analytic and does not extrapolate from those checks. Run `python verify.py` with Python 3, `mpmath`, and `sympy`.

## Relationship to prior work

The renewal-reward stationary occupation construction for noninstantaneous returns is established in Bodrova and Sokolov (2019) and developed for Gamma-timed, **constant-speed** returns by Radice (2022), whose equation (26) is the natural starting point and whose Section 4 establishes speed dependence at nonexponential clocks. Radice supplies constant-speed Gamma stationary formulas; they are not claimed here as new. Zhou, Xu, and Deng (2021) investigate acceleration-type returns with different exploration/rest clocks. The contribution assessed here is the closed all-powered-return Gamma-two family, its complete **cross-protocol stationary inverse fibers**, the exact universal crossing and total-variation ordering, and recovery using a phase-labelled moment. In particular, constant-speed shape-two formulas alone do not determine how a different return exponent can be compensated to produce the identical complete law. General renewal occupation formulas provide a route to derive the result and are not misrepresented as novel.

## Limitations

The statement is confined to one-dimensional Brownian excursions, Gamma shape two, deterministic immediate powered returns with \(0\le\alpha<1\), no return-phase resets, and known exploration parameters \(D,r\). It does not assert invisibility of protocols to temporal correlations, phase labels, or finite-time measurements. The endpoints \(b=1/4\) and \(b=1/2\) are limits, not realizable at finite admissible parameters. The theorem gives no finite-noise statistical inversion guarantees. Its literature-priority status is qualified by the possibility that general renewal formulas yield some consequences as unrecorded corollaries; no claim of independently certified publication novelty is made.

## References

1. M. Radice, *Diffusion processes with Gamma-distributed resetting and non-instantaneous returns* (first public preprint 2022-01-05), https://arxiv.org/abs/2201.01829 .
2. A. S. Bodrova and I. M. Sokolov, *Resetting processes with noninstantaneous return* (first public preprint 2019-07-29), https://arxiv.org/abs/1907.12326 .
3. T. Zhou, P. Xu, and W. Deng, *Gaussian Process and Lévy Walk under Stochastic Non-instantaneous Resetting and Stochastic Rest* (first public preprint 2021-05-25), https://arxiv.org/abs/2105.12571 .
