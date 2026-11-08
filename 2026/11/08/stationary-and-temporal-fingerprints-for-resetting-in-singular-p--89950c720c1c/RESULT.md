# Stationary and temporal fingerprints for resetting in singular planar diffusion

## Finding

Consider planar heterogeneous diffusion with the exact singular diffusivity \(D(\rho)=D_0/\rho^2\), radial distance \(\rho\geq0\), and noise-interpretation parameter \(0\leq\alpha\leq1\), starting at the origin and returning there at independent Poisson rate \(r>0\). The no-flux radial extension specified below has a stationary radius \(R\). Put \(k=1-\alpha/2\). Its natural fourth-power variable \(Y=R^4/(16D_0)\) admits an exact stationary product representation

\[
Y\ \stackrel{d}{=}\ T G_k,\qquad T\sim\operatorname{Exp}(r),\quad G_k\sim\operatorname{Gamma}(k,1),\quad T\perp G_k.
\]

For any \(t>0\), the stationary two-time radial-fourth-power correlation is exactly

\[
\operatorname{Corr}(R_0^4,R_t^4)=e^{-rt},
\]

independent of \(D_0\) and \(\alpha\), whereas the stationary scale-free ratio is

\[
\chi(\alpha):=\frac{\mathbb E[R^4]}{(\mathbb E[R^2])^2}
 =\frac{4k}{\pi}\left[\frac{\Gamma(k)}{\Gamma(k+1/2)}\right]^2.
\]

The latter is strictly increasing in \(\alpha\in[0,1]\), from \(16/\pi^2\) to \(2\). Thus the stationary second and fourth radial moments, together with one positive-lag fourth-power correlation, uniquely identify the **three** parameters \((\alpha,r,D_0)\) without preliminary calibration. In addition, the stationary radial densities are strictly ordered in *monotone likelihood ratio*: if \(\alpha_1<\alpha_2\), then the density quotient \(p_{\alpha_1}(\rho)/p_{\alpha_2}(\rho)\) increases strictly in \(\rho>0\). Consequently, the two radial densities cross exactly once, and \(R_{\alpha_1}\) strictly dominates \(R_{\alpha_2}\) in first-order stochastic order at equal \(D_0,r\).

## Assumptions and scope

Take \(D_0>0\), \(r>0\), \(\alpha\in[0,1]\) and use the planar rotationally invariant Fokker--Planck evolution

\[
\partial_t P(\rho,t)=\frac1\rho\partial_\rho\!\left[\rho D(\rho)^\alpha\,\partial_\rho\{D(\rho)^{1-\alpha}P(\rho,t)\}\right],
\qquad D(\rho)=\frac{D_0}{\rho^2},
\]

where \(\int_0^\infty P(\rho,t)\rho\,d\rho=1\). At \(\rho=0\), take the conservative instantaneous no-flux extension obtained by transporting the nonnegative squared-Bessel diffusion \(dY=k\,dt+\sqrt{2Y}\,dW_t\) through \(\rho=(16D_0Y)^{1/4}\), including its canonical behavior at zero. Resetting replaces \(\rho\) by zero at a state-independent Poisson clock and restarts the diffusion with fresh Brownian increments. This specifies the process even at the singular origin; other boundary extensions are **not** included. The equality and likelihood-ratio results concern the area-normalized *radial probability density* \(p_\alpha(\rho)=\rho P^{\mathrm{st}}_\alpha(\rho)\), not an unnormalized plot. Temporal statements assume ordinary Markov diffusion without fractional memory; the latter can change the two-time law.

The Itô, Stratonovich and Hänggi--Klimontovich cases are respectively \(\alpha=0,1/2,1\). The results hold also for intermediate Fokker--Planck interpolation parameters, although these need not represent an additional named stochastic calculus.

## Proof

**1. A radial squared-Bessel conjugacy.** On smooth radial test functions \(f\), integration by parts against the area measure \(\rho\,d\rho\) gives the backward generator

\[
\mathcal L_\alpha f(\rho)=\frac{D_0}{\rho^2}f''(\rho)
 +\frac{(1-2\alpha)D_0}{\rho^3}f'(\rho),\quad\rho>0.
\]

For \(y(\rho)=\rho^4/(16D_0)\), direct differentiation yields \(\mathcal L_\alpha y=k\) and \(D(\rho)(y'(\rho))^2=y\). Hence on functions of \(y\),

\[
\mathcal L^{Y}_\alpha g(y)=y g''(y)+k g'(y),\qquad k=1-\alpha/2\in[1/2,1].
\]

For the specified canonical nonnegative extension starting from zero, this is a scaled squared-Bessel process with one-time law \(Y_t\stackrel d=tG_k\), where \(G_k\) has density \(z^{k-1}e^{-z}/\Gamma(k)\). Equivalently, its transition Laplace transform from zero is \((1+st)^{-k}\) for \(s\geq0\). All these laws have positive finite moments, and the process is conservative.

**2. Stationary resetting.** A stationary Poisson reset clock has age \(T\sim\operatorname{Exp}(r)\), independent of the post-reset diffusion. Renewal conditioning thus gives the asserted product representation \(Y\stackrel d=T G_k\), and, for \(p\geq0\),

\[
\mathbb E[R^p]=\left(\frac{16D_0}{r}\right)^{p/4}
 \Gamma(1+p/4)\frac{\Gamma(k+p/4)}{\Gamma(k)}.
\]

In particular \(\mathbb E[Y]=k/r\), \(\mathbb E[Y^2]=2k(k+1)/r^2\), \(\operatorname{Var}(Y)=k(k+2)/r^2>0\), \(\mathbb E[R^4]=16D_0k/r\), and the displayed formula for \(\chi\) follows.

**3. Temporal correlation.** The resetting generator on \(Y\) is

\[
\mathcal A f(y)=y f''(y)+k f'(y)+r\{f(0)-f(y)\}.
\]

Since \(\mathcal A y=k-ry\), Dynkin's formula and the Markov property imply, for all starting values \(y\geq0\),

\[
\mathbb E[Y_t\mid Y_0=y]=\frac{k}{r}+
 \left(y-\frac{k}{r}\right)e^{-rt}.
\]

Multiplying the centered relation by the stationary \(Y_0-k/r\), then integrating, proves \(\operatorname{Cov}(Y_0,Y_t)=\operatorname{Var}(Y_0)e^{-rt}\). Multiplication by \((16D_0)^2\) proves the claimed correlation for \(R^4\).

**4. Strict monotonicity and parameter inversion.** The logarithmic derivative of \(\chi\) with respect to \(k\) is

\[
\frac{d}{dk}\log\chi=\frac1k-2\{\psi(k+1/2)-\psi(k)\}.
\]

The digamma integral identity gives

\[
\psi(k+1/2)-\psi(k)=\int_0^\infty
 \frac{e^{-ku}}{1+e^{-u/2}}\,du>\frac1{2k}
\]

for every \(k>0\). Thus \(\chi\) decreases strictly in \(k\), hence increases in \(\alpha\). Endpoint values follow from \(\Gamma(1/2)=\sqrt\pi\) and \(\Gamma(3/2)=\sqrt\pi/2\). For observed exact moments \(m_2=\mathbb E[R^2]\), \(m_4=\mathbb E[R^4]\) and positive-lag correlation \(c_t\), invert uniquely via

\[
 k=\chi^{-1}(m_4/m_2^2),\quad
 \alpha=2(1-k),\quad
 r=-\frac{\log c_t}{t},\quad
 D_0=\frac{r m_4}{16k}.
\]

Here \(m_4/m_2^2\in[16/\pi^2,2]\) and \(c_t\in(0,1)\) for finite positive parameters; at the endpoints the interpretation remains unique.

**5. Strict stationary likelihood-ratio hierarchy.** At fixed \(r\), write \(S=T G_k\) and let \(f_k(s)\) denote its positive density for \(s>0\). For \(k_2>k_1>0\), changing the gamma shape at fixed scale multiplies the density of \(G_{k_1}\) by \(\Gamma(k_1)z^{k_2-k_1}/\Gamma(k_2)\). Given \(S=s\) under the smaller shape, the conditional density of \(G_{k_1}=z\) is proportional to

\[
z^{k_1-2}\exp(-z-rs/z),\qquad z>0.
\]

For \(s_2>s_1\) the quotient of these conditional densities is proportional to \(\exp[-r(s_2-s_1)/z]\), which is strictly increasing in \(z\). Therefore the conditional expectation of the strictly increasing function \(z^{k_2-k_1}\) grows strictly with \(s\); Bayes' formula shows \(f_{k_2}(s)/f_{k_1}(s)\) is strictly increasing in \(s\). The densities are positive, continuous and integrate to one. Their increasing ratio must cross one exactly once, implying strict first-order stochastic domination. The map \(s\mapsto(16D_0s)^{1/4}\) is increasing, so the same statements hold for radial densities. Since \(k\) decreases with \(\alpha\), the Itô stationary radius is strictly larger in likelihood-ratio order than Stratonovich, which is strictly larger than Hänggi--Klimontovich.

## Verification

Run `python checks/check_theorem.py`. The standalone script checks the radial-generator conjugacy symbolically, evaluates stationary Bessel-density integrals against the product-gamma moments, checks likelihood-ratio monotonicity on a numerical grid, and simulates a stationary two-time pair using exact squared-Bessel transitions and exact reset-clock sampling. The script was run successfully. None of the finitely many numerical tests proves the universal inequalities; the preceding arguments do.

The static dimensionless ratios for the three conventions are \(16/\pi^2\approx1.6211389383\) (Itô), \(1.7454073705\) (Stratonovich), and \(2\) (Hänggi--Klimontovich). In all three, the exact normalized fourth-radius correlation is \(e^{-rt}\).

## Relationship to prior work

Sandev, Fumeron, Henkel and Lenzi (2026) give the reset-free radial densities and the Poisson-reset stationary Bessel densities for the three named interpretations, and study the mean-square displacement, first-passage behavior, and a half-population confinement threshold. Those formulas are used as **prior inputs**, not claimed as new. Liu and collaborators (2026) examine interpretation-dependent free diffusion, time-averaged MSD and model selection in a related *regularized* radial medium. Rose and collaborators (2018) establish general spectral shifting under Poisson resetting. The particular squared-Bessel radial conjugacy, the complete likelihood-ratio ordering, the stationary fourth-power time-correlation calculation and the joint, scale-free three-parameter inversion are the assertions investigated here, without claiming a new general resetting theorem.

## Limitations

These conclusions depend on the exact \(\rho^{-2}\) diffusivity, the stated boundary extension, full resets to the origin and a state-independent Poisson clock. A regularized diffusivity \(D_0/(A+\rho^2)\), other reset positions, age-dependent clocks, or subordination can alter the dynamical correlation and the parameter inversion. The result is an exact *population-level* identifiability theorem, not an error bound or a guarantee of accurate estimation from finite samples. The general spectral-shift theorem and standard gamma-family likelihood-ratio ordering cover pieces of the argument; an unindexed earlier synthesis specific to this radial model remains possible. 

## References

1. T. Sandev, S. Fumeron, M. Henkel and E. K. Lenzi, *Heterogeneous planar diffusion with axisymmetric power-law decaying diffusion coefficient under stochastic resetting*, arXiv:2609.24427v1, first posted 2026-09-21, https://arxiv.org/abs/2609.24427.
2. H.-C. Liu et al., *Identifying the interpretation in two-dimensional diffusion processes with power-law spatially dependent diffusivity*, Phys. Rev. Research **8**, 013143 (2026), https://doi.org/10.1103/xz7y-n8w2.
3. D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, Phys. Rev. E **98**, 022129 (2018), arXiv:1806.01298, https://arxiv.org/abs/1806.01298.
4. M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, Phys. Rev. Lett. **106**, 160601 (2011), https://arxiv.org/abs/1102.2704.
