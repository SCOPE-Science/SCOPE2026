# A square-root transverse correlation ridge for burst-born mortal Brownian particles

## Finding and scope

A point source at the origin of the line emits independent Poisson bursts of rate \(b>0\) from the infinite past. Burst sizes have a common positive-integer law \(K\), with mean \(m_1<\infty\). Conditional on each burst, particles move independently as Brownian motions with diffusion coefficient \(D>0\), and have independent exponential lifetimes of rate \(\delta>0\). Fix an integer \(j\ge3\) for which \(m_j=\mathbb E[(K)_j]\in(0,\infty)\), where \((K)_j\) is the falling factorial. No exponential moment of \(K\) is assumed. This model has no interactions, other sources, or boundaries.

Write \(\rho(x)\) for the stationary one-point density, \(\kappa_j(\mathbf x)\) for the stationary factorial cumulant density (mixed derivatives of the log probability-generating functional), and \(G_j(\mathbf x)=\kappa_j(\mathbf x)/\prod_i\rho(x_i)\). These are factorial cumulants, with no self-particle delta term. Using their continuous representatives away from the joint origin, set \(\alpha=\sqrt{\delta/D}\). For every fixed \(\mathbf u\in\mathbb R^j\setminus\{0\}\),

\[
 \lim_{R\to\infty} R^{-1}\log G_j(R\mathbf u)
 =-\alpha\left(\sqrt{j\sum_i u_i^2}-\sum_i|u_i|\right).
\]

The rate is zero exactly when all \(|u_i|\) are equal. On each equal-distance ray, \(G_j(\epsilon_1 R,\ldots,\epsilon_j R)\sim c_j R^{(1-j)/2}\), with \(\epsilon_i\in\{-1,1\}\) and a positive model-dependent constant \(c_j\). More precisely, for fixed real \(v_1,\ldots,v_j\) with mean \(\bar v\),

\[
 \lim_{R\to\infty}
 \frac{G_j(\epsilon_1(R+v_1\sqrt R),\ldots,\epsilon_j(R+v_j\sqrt R))}{G_j(\epsilon_1 R,\ldots,\epsilon_j R)}
 =\exp\!\left[-\frac{\alpha}{2}\sum_i(v_i-\bar v)^2\right].
\]

For nonconstant \(v\) and offsets \(v_iR^\gamma\) instead, with \(0<\gamma<1\), the ratio tends to one for \(\gamma<1/2\), to the displayed Gaussian for \(\gamma=1/2\), and to zero for \(\gamma>1/2\). In particular, an exponential rate alone would not distinguish the transverse scales or give the algebraic decay on the ridge.

## Proof

**Stationary construction and common age.** The expected number of live particles is \(b\int_0^\infty m_1 e^{-\delta t}\,dt=bm_1/\delta\), hence the configuration is finite almost surely. With \(p_t(x)=(4\pi Dt)^{-1/2}\exp[-x^2/(4Dt)]\), define \(a_t(h)=e^{-\delta t}\int p_t(x)h(x)\,dx\). For bounded compactly supported \(h_i\ge0\), let \(s_i\in[-\eta,0]\), with \(\eta\sum_i\|h_i\|_\infty<1\). The Poisson marked-process formula gives

\[
 \log\mathbb E\prod_{X\in\mathcal N}\left(1+\sum_i s_i h_i(X)\right)
 =b\int_0^\infty\left[\mathbb E\left(1+\sum_i s_i a_t(h_i)\right)^K-1\right]dt.
\]

The integral is finite by the bound \(m_1\sum_i |s_i|a_t(h_i)\) on the absolute integrand. On this cube the base is in \((0,1]\). For a mixed derivative of order \(k\le j\), the integrand is bounded in absolute value by \(m_k e^{-k\delta t}\) times the product of the norms of the \(k\) test functions. Here \(m_k<\infty\) follows from the finiteness of \(m_j\); realizations with \(K<k\) have derivative zero. Thus dominated convergence justifies differentiation and the limits to the origin **from the nonpositive side**, not from a two-sided neighborhood. The resulting multilinear forms determine the cumulant densities, also for signed test functions by linearity. In particular,

\[
 \rho(x)=\frac{bm_1}{2\sqrt{D\delta}}e^{-\alpha|x|},\qquad
 \kappa_j(\mathbf x)=bm_j\Phi_j(S),\quad S=\sum_i x_i^2,
 \quad\Phi_j(S)=\frac{1}{(4\pi D)^{j/2}}\int_0^\infty t^{-j/2}e^{-j\delta t-S/(4Dt)}\,dt.
\]

The integral for the density is positive and smooth as a function of \(S>0\), including positions with coinciding or zero coordinates, unless all coordinates are zero. Its integral over position space is \(1/(j\delta)\) by Tonelli and the normalization of \(p_t\), so the singularity at the joint origin is locally integrable. The standard integral representation of the modified Bessel function gives

\[
 \Phi_j(S)=\frac{2}{(4\pi D)^{j/2}}\left(\frac S{4j\delta D}\right)^{(1-j/2)/2}
 K_{1-j/2}(\alpha\sqrt{jS}).
\]

For example, \(\Phi_3(S)=e^{-\alpha\sqrt{3S}}/(4\pi D\sqrt S)\). Burst-size moments and burst rate contribute only spatially constant factors to \(G_j\).

**Large distance.** For \(S=R^2s\), the fixed-order asymptotic \(K_\nu(y)=\sqrt{\pi/(2y)}e^{-y}(1+O(y^{-1}))\) gives

\[
 \Phi_j(R^2s)=C_j(s)R^{(1-j)/2}e^{-\alpha R\sqrt{js}}(1+O(R^{-1})),\qquad
 C_j(s)=\frac{2}{(4\pi D)^{j/2}}\left(\frac{s}{4j\delta D}\right)^{(1-j/2)/2}\sqrt{\frac{\pi}{2\alpha\sqrt{js}}}.
\]

This is uniform for \(s\) in compact positive intervals. The normalizing product of one-point densities contributes \(e^{\alpha\sum_i|x_i|}\) and a positive constant. The rate follows, with equality characterized by Cauchy–Schwarz for the vector of absolute coordinates. On the equal-distance ray, \(s=j\) and the exponential cancels exactly, proving the leading power.

**Transverse geometry.** For \(r_i=R+v_iR^\gamma>0\) (eventually) the spatial exponent is minus \(\alpha\) times the deficit

\[
 \sqrt{j\sum_i r_i^2}-\sum_i r_i
 =\frac{j\sum_i(r_i-\bar r)^2}{\sqrt{j\sum_i r_i^2}+\sum_i r_i}
 =\tfrac12 R^{2\gamma-1}\left(\sum_i(v_i-\bar v)^2\right)(1+o(1)).
\]

The denominator is asymptotic to \(2jR\); when the offsets are all equal the deficit vanishes exactly. The moving value of \(s=\sum_i r_i^2/R^2\) tends to \(j\), so the smooth prefactor ratio tends to one. This yields all three limits and the stated transverse profile.

## Reproducibility and limitations

The accompanying `checker.py` can be run with Python, NumPy and SciPy. Its finite tests compare time quadrature with the exact Bessel kernel and probe the triplet formula, the rate, and the three transverse regimes. They do not replace the proof. No assertion is made about pointwise random-field correlations, detection in individual realizations, the density at the joint origin, or a new second-order result. Homogeneous diffusion, a point source and independent exponential death are used in the common-age integral.

## Relationship to prior work

The Poisson-cluster cumulant mechanism is standard: M. Kerscher, *Constructing, characterizing, and simulating Gaussian and higher-order point distributions*, Phys. Rev. E **64**, 056109 (2001), [arXiv:astro-ph/0102153](https://arxiv.org/abs/astro-ph/0102153). The Bessel asymptotic used above is [DLMF §10.40(i), Eq. 10.40.2](https://dlmf.nist.gov/10.40.E2). D. Boyer and G. Mercado-Vásquez, *Stochastic synthesis and degradation of arbitrary diffusive processes*, [arXiv:2611.04843](https://arxiv.org/abs/2611.04843), study one-point quantities and burst production. D. Cottrell, P. S. Swain and P. F. Tupper, *Stochastic branching-diffusion models for gene expression*, PNAS **109**, 9699–9704 (2012), [DOI:10.1073/pnas.1201103109](https://doi.org/10.1073/pnas.1201103109), study a related spatial branching-diffusion model. The public result *A dimension–order threshold for local burst-diffusion cumulants* gives a common-age identity for the factorial cumulants of counts in a single ball centered at the source and analyzes the shrinking-ball limit. The claim here concerns the simultaneous normalized higher-order ridge, the sharp Gaussian transverse profile and the classification by width, not general cluster theory, first- and second-order observables, or a shrinking-detector threshold. Historical priority beyond the sources compared is not certified.
