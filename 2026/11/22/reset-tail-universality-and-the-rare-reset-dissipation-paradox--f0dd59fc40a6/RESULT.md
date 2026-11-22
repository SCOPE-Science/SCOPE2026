# Reset-tail universality and the rare-reset dissipation paradox

## Finding

Fix a Brownian diffusivity \(D>0\), a reset-location standard deviation \(\sigma>0\), and a positive Poisson resetting rate \(r\). Let the independently sampled reset location have density \(p_R(x)=\sigma^{-1}f(x/\sigma)\), where \(f\) is positive, continuous, bounded, and has mean zero and variance one. Let \(h(u)=-\log f(u)\). Suppose, for some \(p>0\) and \(c>0\), that
\[
\lim_{|u|\to\infty}h(u)/|u|^p=c,
\quad |h(u)|\le C(1+|u|^p),\quad
\mathbb E_{Y\sim f}|Y|^p<\infty.
\]
For free one-dimensional Brownian motion reset at rate \(r\) to fresh independent draws from \(p_R\), let \(\Sigma_f(r)\) be the stationary mean *trajectory-time-reversal* entropy-production rate (in units with Boltzmann's constant one), including reset jumps and with no external confining potential. Then
\[
\boxed{\displaystyle\lim_{r\downarrow0}\frac{\Sigma_f(r)}{r^{1-p/2}}
=c\,\Gamma(p+1)\left(\frac D{\sigma^2}\right)^{p/2}.}
\]
The coefficient is strictly positive. Consequently, as resetting becomes rare, the rate tends to zero for \(0<p<2\), to a finite nonzero constant for \(p=2\), and diverges for \(p>2\). This is a threshold determined by the far tail of the reset-location density, not by its (fixed) variance.

For the standardized generalized-normal reset family \(f_m(u)\propto\exp(-c_m|u|^{2m})\) with integer \(m\ge1\) and \(c_m=[\Gamma(3/(2m))/\Gamma(1/(2m))]^m\), the **complete finite-rate** expression is
\[
\boxed{\displaystyle\Sigma_m(r)=c_m\sum_{j=1}^m\frac{(2m)!}{(2m-2j)!}\,
\mathbb E Y_m^{2m-2j}\left(\frac D{\sigma^2}\right)^j r^{1-j},\quad Y_m\sim f_m.}
\]
Thus the Gaussian case \(m=1\) has \(\Sigma_1(r)=D/\sigma^2\) at every rate, while for every \(m\ge2\), \(\Sigma_m(r)\) is strictly decreasing in \(r\) and diverges as \(r^{1-m}\) as \(r\downarrow0\). In particular the quartic reset density, despite having finite variance and moments of every order, has
\[
\Sigma_2(r)=12c_2\frac D{\sigma^2}+24c_2\frac{D^2}{r\sigma^4},
\qquad c_2=[\Gamma(3/4)/\Gamma(1/4)]^2.
\]

## Assumptions and scope

The diffusion is \(dX_t=\sqrt{2D}\,dW_t\) between Poisson events, with independent fresh reset points and event clock. The stated entropy-production observable is exactly the path-reversal mean derived by Mori, Olsen and Krishnamurthy (2022, their Eq. (9)); physical actuator work, finite-duration return protocols, and alternative entropy conventions are outside the claim. The density is everywhere positive, its logarithm obeys the displayed growth bound, and the stated moments exist. No uniqueness claim about a reset law is made. The asymptotic refers to \(r\downarrow0\) with \(D,\sigma,f\) held fixed.

## Proof

**Step 1 (stationary renewal law).** In equilibrium the backward recurrence time since the last reset is exponentially distributed with rate \(r\), independently of the reset draw \(Y\). Conditional Brownian displacement at time \(A\sim\operatorname{Exp}(r)\) has characteristic function \(\mathbb E e^{-Dk^2A}=r/(r+Dk^2)\), the centered Laplace law of scale \(\sqrt{D/r}\). Therefore the pre-reset stationary location has the exact law \(X=\sigma Y+\sqrt{D/r}\,Z\), where \(Z\) is a unit-scale symmetric Laplace random variable independent of \(Y\). This is equivalent to the stationary convolution in [1, Eq. (4)].

**Step 2 (exact dissipation identity).** Since there is no confining drift, the medium-entropy term in [1, Eq. (10)] is zero. The reset-jump path-reversal term in [1, Eq. (9)] yields, with \(T=\sqrt{D/(r\sigma^2)}\),
\[
\Sigma_f(r)=r\Big(\mathbb E h(Y+TZ)-\mathbb E h(Y)\Big).
\]
The \(\log\sigma\) normalization terms cancel. Finiteness follows from the growth and moment assumptions; every expression is well-defined for \(r>0\).

**Step 3 (universal tail law).** For each fixed \((Y,Z)\) with \(Z\ne0\), \(T^{-p}h(Y+TZ)\to c|Z|^p\) as \(T\to\infty\). The assumed bound and the inequality \(|u+v|^p\le 2^{\max(p-1,0)}(|u|^p+|v|^p)\) give, uniformly for \(T\ge1\),
\[
T^{-p}|h(Y+TZ)|\le C_p(1+|Y|^p+|Z|^p),
\]
which is integrable. Dominated convergence and \(\mathbb E|Z|^p=\Gamma(p+1)\) show \(\mathbb E h(Y+TZ)=c\Gamma(p+1)T^p+o(T^p)\). Because \(\mathbb Eh(Y)\) is finite, substitution yields the boxed asymptotic and its three strict regimes.

**Step 4 (all-rate super-Gaussian classification).** For integer \(m\ge1\), the generalized-normal density with coefficient \(c_m\) has variance one, because \(\mathbb E|Y_m|^s=c_m^{-s/(2m)}\Gamma((s+1)/(2m))/\Gamma(1/(2m))\). Applying Step 2 to \(h(u)=c_m u^{2m}+\mathrm{constant}\), expand \((Y_m+TZ)^{2m}\). Symmetry eliminates odd powers, and \(\mathbb EZ^{2j}=(2j)!\), giving the exact finite sum in the finding. All summands are positive. For \(m=1\) only the constant term in \(r\) remains, equal to \(D/\sigma^2\). For \(m\ge2\) the \(j=2\) and higher terms have strictly negative derivatives with respect to \(r\), so the whole rate is strictly decreasing. The final \(j=m\) term gives the exact divergent leading constant. Taking \(m=2\) and \(\mathbb EY_m^2=1\) gives the quartic identity.

## Verification

The included standalone \(check.py\) reconstructs the generalized-normal variance normalization, independently computes the polynomial coefficients and exact Laplace moments, checks the Gaussian and quartic formulas at multiple rates, verifies the strict rate monotonicity for \(m=2,3,4\), and tests the leading constants. An independent 95-node tensor generalized-Gauss–Laguerre quadrature (not required by the standalone checker) evaluated \(p=1,1.5,2,3,4,6\): at \(r=1/256\) and \(D=\sigma=1\), the finite-rate/leading-asymptotic ratios were approximately \(0.958,0.992,1.000,1.002,1.002,1.002\), respectively. Numerics illustrate, but do not establish, the infinite-parameter theorem.

## Relationship to prior work

Mori, Olsen and Krishnamurthy [1] established the general trajectory-time-reversal entropy formula and explicitly treated exponential and Gaussian reset densities for full entropy-production fluctuations. Equations (4), (9), and (10) from [1] are prerequisites, not rediscoveries. The addition here is the general **tail-index weak-rate classification**, including unbounded entropy production from arbitrarily rare resets with a finite-variance super-Gaussian reset law, and the exact all-rate monotonicity of the complete even-power family. Neither a new expression for the general entropy functional nor a new entropy convention is claimed. Bressloff [2] develops a broad jump-diffusion stochastic-entropy framework; the accessible sections were compared, but a comprehensive full-text negative claim about [2] is not made.

## Limitations

The tail classification may be implicit in known entropy-production functional identities and its publication priority has not been independently established. The criterion is about one particular stationary path-reversal entropy observable, not all thermodynamic accounting schemes. Instantaneous resets to a super-Gaussian distribution may be costly or physically unrealizable; this cost is not included. No finite-sample estimation, adaptive resetting, external potential, or finite-time return result is asserted. The universal tail asymptotic alone does not classify the complete finite-rate monotonicity for non-even exponents.

## References

[1] F. Mori, K. S. Olsen and S. Krishnamurthy, *Entropy production of resetting processes*, arXiv:2211.15372 (first public 2022-11-28), https://arxiv.org/abs/2211.15372; Phys. Rev. Research 5, 023103 (2023), https://doi.org/10.1103/PhysRevResearch.5.023103.

[2] P. C. Bressloff, *Generalized Itô's lemma and the stochastic thermodynamics of diffusion with resetting*, J. Phys. A 57, 445003 (2024), https://doi.org/10.1088/1751-8121/ad8495.
