# A universal square-root transverse correlation ridge for burst-born mortal Brownian particles

## Finding

For the stationary one-dimensional Brownian population introduced below, the connected factorial density of every order \(j\ge3\) for which the burst-size factorial moment is positive has an exact common-age representation. Its normalization by the product of one-point densities has a sharp far-field geometric classification: for any fixed nonzero vector \(\mathbf u=(u_1,\ldots,u_j)\),
\[
\lim_{R\to\infty}\frac{1}{R}\log G_j(Ru_1,\ldots,Ru_j)
=-\sqrt{\delta/D}\left(\sqrt{j\sum_i u_i^2}-\sum_i|u_i|\right).
\]
The rate is zero precisely when all \(|u_i|\) are equal, and otherwise is strictly negative. This distinguishes a simultaneous equal-distance correlation ridge from the exponential suppression of configurations at unequal source distances.

The transverse width is exactly the square-root scale. For arbitrary signs \(\epsilon_i\in\{-1,1\}\), fixed offsets \(v_i\in\mathbb R\), and \(\bar v=j^{-1}\sum_i v_i\),
\[
\lim_{R\to\infty}\frac{G_j(\epsilon_1(R+v_1\sqrt R),\ldots,\epsilon_j(R+v_j\sqrt R))}{G_j(\epsilon_1R,\ldots,\epsilon_jR)}
=\exp\!\left[-\frac12\sqrt{\delta/D}\sum_i(v_i-\bar v)^2\right].
\]
If \(v_i\) are not all equal and \(\sqrt R\) is replaced by \(R^\gamma\) with \(0<\gamma<1\), this ratio tends to one for \(\gamma<1/2\), to the displayed nontrivial Gaussian for \(\gamma=1/2\), and to zero for \(\gamma>1/2\). On the equal-distance ridge the normalized cumulant is proportional, at leading order, to \(R^{(1-j)/2}\), with a strictly positive constant depending on model parameters and order.

## Assumptions and scope

A point source at the origin of the real line emits independent Poisson bursts of rate \(b>0\), from the infinite past. Each burst independently releases a positive integer number \(K\) of particles, with mean \(m_1=\mathbb E K<\infty\). Fix an integer \(j\ge3\) such that the factorial moment \(m_j=\mathbb E[(K)_j]\) is finite and positive, where \((K)_j=K(K-1)\cdots(K-j+1)\). Independently conditional on the burst, each particle follows free Brownian motion of diffusion coefficient \(D>0\), with transition density \(p_t(x)=(4\pi Dt)^{-1/2}\exp[-x^2/(4Dt)]\), and dies after an independent exponential lifetime of rate \(\delta>0\). There are no reactions, interactions, absorbing boundaries, or particle relocation. The source is the only production site.

Let \(\rho(x)\) be the stationary one-point particle density and let \(\kappa_j(x_1,\ldots,x_j)\) be the order-\(j\) **factorial cumulant density**, defined as the coefficient obtained by differentiating the log probability-generating functional in \(j\) test-function directions. It is not an ordinary pointwise random-field cumulant and contains no diagonal self-particle delta term. The formula is initially read at pairwise distinct coordinates and extends continuously wherever \(\sum_i x_i^2>0\). Define \(G_j=\kappa_j/\prod_i\rho(x_i)\). All far-field vectors have nonzero coordinates; no assertion is made at the origin.

## Proof

**Stationary construction and exact cluster cumulants.** The Poisson bursts are marked by iid sizes and independent killed Brownian paths. Because their expected surviving population is \(bm_1/\delta\), the stationary configuration is locally and globally finite almost surely. For bounded compactly supported test functions \(f\) sufficiently close to zero, its probability-generating functional is
\[
\log\mathbb E\prod_{X\in\mathcal N}(1+f(X))
=b\int_0^\infty\!\left[\mathbb E\left(1+e^{-\delta t}\int_\mathbb R p_t(x)f(x)\,dx\right)^K-1\right]dt.
\]
Taking \(j\) factorial functional derivatives at the origin (justified using \(m_j<\infty\)) gives
\[
\kappa_j(\mathbf x)=b m_j\Phi_j(S),\qquad
\Phi_j(S)=\frac1{(4\pi D)^{j/2}}\int_0^\infty t^{-j/2}\exp\left(-j\delta t-\frac S{4Dt}\right)dt,
\quad S=\sum_{i=1}^j x_i^2.
\]
The order-one derivative gives \(\rho(x)=bm_1 e^{-\alpha|x|}/(2\sqrt{D\delta})\), with \(\alpha=\sqrt{\delta/D}\). For \(S>0\) the integral is finite, positive and has the Bessel representation
\[
\Phi_j(S)=\frac{2}{(4\pi D)^{j/2}}\left(\frac S{4j\delta D}\right)^{(1-j/2)/2}K_{1-j/2}\!\left(\alpha\sqrt{jS}\right).
\]
In particular \(\Phi_3(S)=e^{-\alpha\sqrt{3S}}/(4\pi D\sqrt S)\). All dependences on the burst-size law enter through the positive prefactor \(m_j\), not through the spatial geometry.

**Uniform Laplace expansion.** Put \(S=R^2s\), where \(s\) ranges over a compact subset of \((0,\infty)\), and substitute \(t=Rz\). The phase is \(R(j\delta z+s/(4Dz))\); it has a unique nondegenerate minimum at \(z_*=(1/2)\sqrt{s/(jD\delta)}\), with value \(\alpha\sqrt{js}\). Uniform one-dimensional Laplace asymptotics thus give
\[
\Phi_j(R^2s)=C_j(s)R^{(1-j)/2}
\exp[-\alpha R\sqrt{js}](1+O(R^{-1})),
\]
where \(C_j(s)>0\) is smooth on \(s>0\). For example the positive coefficient is \(C_j(s)=(4\pi D)^{-j/2}z_*^{-j/2}\sqrt{2\pi/(2s/(4Dz_*^3))}\). The error is uniform on compact positive \(s\)-ranges. Combining with the exact product of one-point densities gives
\[
\log G_j(\mathbf x)
=-\alpha\left(\sqrt{j\sum_i x_i^2}-\sum_i|x_i|\right)
+\tfrac{1-j}2\log R+O(1)
\]
when \(\mathbf x/R\) is confined to a compact set of nonzero vectors.

**Geometry and critical width.** For \(x_i=Ru_i\), Cauchy–Schwarz yields \(\sum_i|u_i|\le\sqrt{j\sum_i u_i^2}\), with equality exactly at equal absolute coordinates. The normalized logarithmic limit follows. For the moving shell let \(x_i=\epsilon_i(R+v_i\sqrt R)\); all radial factors are positive for sufficiently large \(R\). Taylor expansion gives
\[
\sqrt{j\sum_i(R+v_i\sqrt R)^2}-\sum_i(R+v_i\sqrt R)
=\frac12\sum_i(v_i-\bar v)^2+O(R^{-1/2}).
\]
The ratio of smooth Laplace prefactors approaches one, proving the Gaussian profile. For offsets \(v_iR^\gamma\) and nonconstant \(v\), the same difference equals \(\frac12R^{2\gamma-1}\sum_i(v_i-\bar v)^2(1+o(1))\); the prefactor ratio still tends to one for \(\gamma<1\). This yields the three claimed regimes. Finally, on \(x_i=\epsilon_iR\), the exponential factor in \(G_j\) cancels exactly, leaving \(R^{(1-j)/2}\) times a positive constant.

## Verification

`checker.py` uses independent numerical quadrature of the common-age kernel against the Bessel expression for orders three, four and five; checks the closed triplet formula; and compares the exact finite-radius normalized cumulant against the large-deviation exponent, Gaussian ridge profile and transverse-scale trichotomy. The numerical comparisons test formulas but do not substitute for the infinite-radius Laplace proof. Execute `python checker.py` with NumPy and SciPy installed. This is an independent computational recomputation of the displayed identities, not independent scholarly validation.

## Relationship to prior work

Boyer and Mercado-Vásquez (arXiv:2611.04843, first public 2026-11-03) formulate stochastic synthesis–degradation and bursty production, deriving one-point density and first-passage quantities. Their sections 3 and 6 do not establish an order-three-and-higher stationary spatial factorial-cumulant far-field ridge. Cottrell, Swain and Tupper (PNAS 2012, doi:10.1073/pnas.1201103109) derive spatial means, variances and two-point covariances in a related gene-expression branching-diffusion model; a general claim of new pairwise spatial covariance would therefore be incorrect. Kerscher (Phys. Rev. E 64, 056109, 2001) develops the general Poisson-cluster higher-order factorial-cumulant formalism. That established formalism supplies the cluster calculus here, so the exact generating-functional mechanism itself is not asserted to be novel. The specific combined higher-order equal-source-distance large-deviation zero set, uniform sharp square-root transverse profile, and three-scale classification are the proposed additional results. A stronger unexamined Poisson-cluster large-deviation theorem could subsume these results.

## Limitations

These are stationary factorial cumulant densities, not spatial covariance coefficients of pointwise occupancies and not statements about individual realization detection. The source is point-like, Brownian motion is noninteracting and homogeneous, death is exponential, and finite positive order-\(j\) factorial moment is essential. Claims of novelty remain provisional pending independent primary-literature review; prior general cluster theory must be credited. Although the exact formulas are valid for \(j=2\), this result does **not** claim a new second-order spatial correlation. Finite-radius numerical tests do not certify the asymptotic theorem.

## References

- D. Boyer and G. Mercado-Vásquez, *Stochastic synthesis and degradation of arbitrary diffusive processes*, arXiv:2611.04843 (2026), https://arxiv.org/abs/2611.04843.
- D. Cottrell, P. S. Swain and P. F. Tupper, *Stochastic branching-diffusion models for gene expression*, Proc. Natl. Acad. Sci. USA 109 (2012), 9699–9704, https://doi.org/10.1073/pnas.1201103109.
- M. Kerscher, *Constructing, characterizing, and simulating Gaussian and higher-order point distributions*, Phys. Rev. E 64 (2001), 056109, https://arxiv.org/abs/astro-ph/0102153.
