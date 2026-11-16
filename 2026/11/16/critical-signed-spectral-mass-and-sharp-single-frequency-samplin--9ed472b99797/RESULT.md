# Critical signed spectral mass and sharp single-frequency sampling cost for compact ball-power kernels

## Finding
For every integer \(d\ge2\), define the compactly supported radial function
\[
k_\beta(x)=(1-\|x\|_2^2)_+^\beta,\qquad \beta>0.
\]
The spectral total variation of this kernel has a sharp integrability boundary. Put
\[
\beta_c=\frac{d-1}{2},\qquad
A_d=\frac{4\Gamma((d+1)/2)}{\pi^{3/2}\Gamma(d/2)}.
\]
With the definitions and Fourier convention below, the full signed Fourier spectrum has finite total variation precisely when \(\beta>\beta_c\). Moreover,
\[
V_d(\beta_c+\varepsilon)=\frac{A_d}{\varepsilon}+O_d(1)
\quad(\varepsilon\downarrow0).
\]
At a finite frequency cutoff a more precise uniform law holds: for each fixed \(L>0\), as \(R\to\infty\),
\[
\sup_{|\lambda|\le L}\left|V_{d,R}\!\left(\beta_c+\frac{\lambda}{\log R}\right)-A_d\log R\,\frac{1-e^{-\lambda}}{\lambda}\right|=O_{d,L}(1),
\]
where the quotient at \(\lambda=0\) is one. The borderline variation is therefore \(A_d\log R+O_d(1)\).

For an unbiased one-frequency complex Fourier estimator of this kernel at *every* displacement, the minimum possible second moment is exactly \(V_d(\beta)^2\) when \(\beta>\beta_c\), and is infinite at or below the threshold. The optimal sampling density is proportional to the absolute signed spectrum. In particular, the minimum second moment is asymptotic to \(A_d^2/\varepsilon^2\) as \(\varepsilon\downarrow0\). This is a sharp spectral sampling cost, not a claim about arbitrary estimators based on multiple jointly sampled frequencies.

## Assumptions and scope
The dimension \(d\) is a fixed integer at least two. The parameter \(\beta\) is positive, and no positive-definiteness assumption is imposed. Fourier transforms use
\[
\widehat f(\xi)=\int_{\mathbb R^d}e^{-ix\cdot\xi}f(x)\,dx,
\qquad
\rho_\beta(\xi)=\frac{\widehat{k_\beta}(\xi)}{(2\pi)^d}.
\]
Define the truncated total variation and its monotone extended limit by
\[
V_{d,R}(\beta)=\int_{\|\xi\|_2\le R}|\rho_\beta(\xi)|\,d\xi,
\qquad V_d(\beta)=\lim_{R\to\infty}V_{d,R}(\beta)\in[0,\infty].
\]
A one-frequency estimator means a measurable random variable \(Z_x=w(\omega)e^{i\omega\cdot x}\), with \(\omega\) sampled from a probability distribution independent of \(x\), satisfying \(\mathbb E Z_x=k_\beta(x)\) for every \(x\in\mathbb R^d\). Its complex second moment is \(\mathbb E|Z_x|^2\), independent of \(x\). The signed-spectral optimizer uses an absolutely continuous frequency distribution.

## Proof
**1. Exact radial transform.** Polar Fourier integration and Sonine's Bessel identity give, for \(r=\|\xi\|_2>0\),
\[
\widehat{k_\beta}(\xi)=(2\pi)^{d/2}2^\beta\Gamma(\beta+1)
 r^{-d/2-\beta}J_{d/2+\beta}(r).
\]
Its continuous value at zero is
\[
\widehat{k_\beta}(0)=\frac{\pi^{d/2}\Gamma(\beta+1)}{\Gamma(d/2+\beta+1)}.
\]
Consequently the nonnegative radial total-variation integrand, apart from a positive analytic prefactor, is \(r^{d/2-\beta-1}|J_{d/2+\beta}(r)|\). It is locally integrable at zero, uniformly for \(\beta\) in a compact positive interval, because \(J_\nu(r)=O(r^\nu)\).

**2. Oscillatory asymptotics and constant.** Let \(\varepsilon=\beta-\beta_c\) and \(\nu=d/2+\beta\). The fixed-order Bessel expansion, uniform when \(\beta\) ranges in a compact interval around \(\beta_c\), is
\[
J_\nu(r)=\sqrt{\frac{2}{\pi r}}
\left(\cos(r-\pi\nu/2-\pi/4)+O_d(r^{-1})\right).
\]
Using \(\big||u+v|-|u|\big|\le|v|\), the radial variation integral from one to \(R\) equals
\[
B_d(\beta)\int_1^Rr^{-1-\varepsilon}|\cos(r-\phi_\beta)|\,dr+O_d(1),
\]
where
\[
\phi_\beta=\frac{\pi(d/2+\beta)}2+\frac\pi4,
\quad
B_d(\beta)=\frac{2\pi^{d/2}}{\Gamma(d/2)}
\frac{(2\pi)^{d/2}2^\beta\Gamma(\beta+1)}{(2\pi)^d}
\sqrt{\frac2\pi}.
\]
Here the remainder is uniform for \(|\varepsilon|\le1/4\) because \(\int_1^\infty r^{-2-\varepsilon}\,dr\) is uniformly bounded. The periodic function \(|\cos(r-\phi)|-2/\pi\) has a bounded primitive, uniformly in the phase. One integration by parts gives
\[
\int_1^Rr^{-1-\varepsilon}|\cos(r-\phi_\beta)|\,dr
=\frac2\pi\int_1^Rr^{-1-\varepsilon}\,dr+O_d(1)
\]
uniformly for \(|\varepsilon|\le1/4\) and \(R\ge1\). (The formula is valid at \(\varepsilon=0\); for \(\varepsilon<0\) the exponent remains positive under this restriction.) Simplifying the prefactor yields
\[
\frac2\pi B_d(\beta_c)=\frac{4\Gamma((d+1)/2)}{\pi^{3/2}\Gamma(d/2)}=A_d.
\]
Since \(B_d(\beta)=B_d(\beta_c)+O_d(\varepsilon)\), we have the master estimate
\[
V_{d,R}(\beta)=\frac2\pi B_d(\beta)
\int_1^Rr^{-1-\varepsilon}\,dr+O_d(1)
\]
uniformly near \(\beta_c\). For fixed \(\varepsilon>0\), taking \(R\to\infty\) gives the pole law \(A_d/\varepsilon+O_d(1)\). With \(\varepsilon=\lambda/\log R\) it gives \(\int_1^Rr^{-1-\varepsilon}\,dr=\log R\,(1-e^{-\lambda})/\lambda\). Since \(|\lambda|\le L\), replacing \(B_d(\beta)\) by its critical value changes this expression by at most \(O_{d,L}(1)\), proving the full uniform window law. The same oscillatory mean also proves divergence when \(\varepsilon\le0\), and absolute convergence when \(\varepsilon>0\). For parameters away from the critical compact interval, the identical Bessel tail exponent proves the global iff claim.

**3. Optimal unbiased sampling.** When \(V_d(\beta)<\infty\), the signed Fourier measure \(\mu_\beta(d\xi)=\rho_\beta(\xi)d\xi\) is finite, and Fourier inversion gives \(k_\beta(x)=\int e^{ix\cdot\xi}\,d\mu_\beta(\xi)\). If an unbiased one-frequency estimator has \(\mathbb E|w(\omega)|^2<\infty\), its induced signed measure \(w\,q\) has total variation no greater than \(\mathbb E|w(\omega)|\le(\mathbb E|w|^2)^{1/2}\). Uniqueness of Fourier transforms of finite measures identifies it with \(\mu_\beta\), so
\[
\mathbb E|w(\omega)|^2\ge\bigl\|\mu_\beta\bigr\|_{\mathrm{TV}}^2=V_d(\beta)^2.
\]
If \(\mu_\beta\) is not finite, no finite-second-moment estimator can exist: its finite induced measure would have the same Fourier transform, forcing equality with the (distributional) Fourier transform \(\rho_\beta\), a contradiction. For \(\beta>\beta_c\), take
\[
q_\beta(\xi)=\frac{|\rho_\beta(\xi)|}{V_d(\beta)},\qquad
w(\xi)=V_d(\beta)\operatorname{sgn}(\rho_\beta(\xi)).
\]
This achieves equality. Equality in Cauchy–Schwarz also forces the sampling density and phase almost everywhere on the nonzero spectrum. As the kernel has \(k_\beta(0)=1\), its positive and negative spectral masses are \((V_d(\beta)+1)/2\) and \((V_d(\beta)-1)/2\), respectively, giving a negative-mass pole \(A_d/(2\varepsilon)+O_d(1)\). The minimum second moment scales as \(A_d^2/\varepsilon^2(1+o(1))\).

## Verification
The standalone `check.py` evaluates the Fourier transform both from the Bessel formula and by independently integrating the radial Hankel representation, checks the critical gamma prefactor, compares finite-cutoff logarithmic slopes, and checks the critical-window leading term numerically. It passed 62 finite comparisons using Python 3, NumPy and SciPy. Running `python3 check.py` reproduces the checks. These tests are numerical supplements, not a proof of asymptotics or estimator optimality; those claims follow from the displayed analytic derivation.

## Relationship to prior work
Wang, Langrené and Chen (first public August 29, 2026) introduce signed random Fourier features for indefinite compactly supported kernels, including the Kuttner–Golubov family, and require an absolutely integrable signed spectrum. The present \(\alpha=2\) subfamily analysis supplies an exact spectral-variation boundary, pole residue, uniform critical-cutoff crossover and sharp cost for single-frequency signed sampling. The full manuscript of that most relevant source was not accessible for a statement-by-statement comparison; therefore priority relative to a possible uninspected appendix is unresolved. Classical ball-power Fourier and Bessel identities are inputs rather than newly claimed results. Unlike work on critical \(L^p\) norms of smoothed Fourier-ball kernels, here the norm is \(L^1\) of a signed spectrum for variable boundary powers, and the sampling cost follows from that variation.

## Limitations
The law is for fixed dimension \(d\) and the quadratic-radial subfamily \(\alpha=2\); no uniform-in-dimension estimate is claimed. It applies to unbiased *one-frequency* estimators of every displacement, not nonlinear, biased or correlated multi-frequency methods. No sharp finite-cutoff constant term is established beyond the \(O(1)\) remainder. Novelty remains subject to comparison with the inaccessible full motivating manuscript and possible equivalent older Bessel-integral results. No independent mathematical audit has been performed.

## References
1. X. Wang, N. Langrené and W. Chen, *Signed random Fourier features for fast density estimation with indefinite kernels*, arXiv:2608.29265 (first posted August 29, 2026), https://arxiv.org/abs/2608.29265.
2. NIST Digital Library of Mathematical Functions, §10.17, especially (10.17.3) and real-order error estimates, https://dlmf.nist.gov/10.17.
3. E. Güldoğan Lekesiz, R. Aktaş and I. Area, *Fourier Transform of the Orthogonal Polynomials on the Unit Ball and Continuous Hahn Polynomials*, Axioms 11 (2022), 558, https://www.mdpi.com/2075-1680/11/10/558.
4. Classical Sonine integral identity for Bessel functions; see NIST DLMF, §10.22, https://dlmf.nist.gov/10.22.
