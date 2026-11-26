# Sharp weak-partial-reset stationary tails with a dilogarithmic rate and boundary prefactor

## Finding

For one-dimensional Brownian diffusion with diffusion coefficient \(D>0\), partial resetting at Poisson rate \(r>0\) by multiplication with \(a=e^{-\varepsilon}\), and its unique stationary position \(X_\varepsilon\), put \(\ell=\sqrt{D/r}\) and \(Y_\varepsilon=\varepsilon X_\varepsilon\). For every fixed \(y>0\), as \(\varepsilon\downarrow0\),

\[
\boxed{\Pr(Y_\varepsilon\ge y)=\frac{\sqrt{\varepsilon}\,e^{-I_\ell(y)/\varepsilon}}{\theta_y\sqrt{2\pi\Lambda_\ell''(\theta_y)}\sqrt{1-\ell^2\theta_y^2}}\,(1+o(1)).}
\]

Here \(\operatorname{Li}_2(z)=\sum_{k\ge1}z^k/k^2\) on \([0,1]\),
\[
\Lambda_\ell(\theta)=\frac12\operatorname{Li}_2(\ell^2\theta^2),\quad |\theta|<1/\ell,
\qquad I_\ell(y)=\sup_{|\theta|<1/\ell}\{\theta y-\Lambda_\ell(\theta)\},
\]
\(\theta_y\in(0,1/\ell)\) is the unique solution of
\[
y=\Lambda_\ell'(\theta_y)=-\frac{\log(1-\ell^2\theta_y^2)}{\theta_y},
\]
and
\[
\Lambda_\ell''(\theta)=\frac{2\ell^2}{1-\ell^2\theta^2}+\frac{\log(1-\ell^2\theta^2)}{\theta^2}>0
\]
for nonzero \(\theta\), with continuous value \(\Lambda_\ell''(0)=\ell^2\). The left tail is identical by symmetry: \(\Pr(Y_\varepsilon\le-y)=\Pr(Y_\varepsilon\ge y)\).

The laws of \(Y_\varepsilon\) also obey a full large-deviation principle on \(\mathbb R\) with speed \(\varepsilon^{-1}\) and the good rate \(I_\ell\). In particular \(\lim_{\varepsilon\downarrow0}\varepsilon\log\Pr(Y_\varepsilon\ge y)=-I_\ell(y)\), whereas the displayed prefactor supplies the first sharp multiplicative scale missing from that exponential statement. The rate interpolates between
\[
I_\ell(y)=\frac{y^2}{2\ell^2}-\frac{y^4}{8\ell^4}+O(y^6)\quad(y\to0),
\qquad I_\ell(y)=\frac{|y|}{\ell}-\frac{\pi^2}{12}+o(1)\quad(|y|\to\infty).
\]

## Assumptions and scope

The process has backward generator \(\mathcal Lf(x)=Df''(x)+r[f(ax)-f(x)]\), with \(D,r>0\), \(0<a=e^{-\varepsilon}<1\), and independent rate-\(r\) Poisson resetting events. Observations are made in the stationary law; the initial transient is not part of the assertion. The large-deviation threshold \(y>0\) and \(D,r\) are fixed before \(\varepsilon\downarrow0\). The relative-error statement is pointwise in \(y>0\), not uniform as \(y\to0\) or \(y\to\infty\).

The stationary sum representation, proved in the primary partial-reset literature, is
\[
X_\varepsilon\stackrel{d}{=}\sum_{j=0}^{\infty}e^{-\varepsilon j}L_j,
\qquad \Pr(L_j\in dx)=\frac{e^{-|x|/\ell}}{2\ell}\,dx,
\]
where the \(L_j\) are independent. The sum converges in \(L^2\) and almost surely because its total variance is finite for each \(\varepsilon>0\). This fixes the diffusion, resetting and Laplace scale normalizations.

## Proof

**1. Exact cumulants and the singular scaling.** For \(|\theta|<1/\ell\), the moment-generating function and its logarithm are
\[
M_\varepsilon(\theta)=\prod_{j\ge0}(1-\ell^2\theta^2e^{-2\varepsilon j})^{-1},
\qquad K_\varepsilon(\theta)=\sum_{j\ge0}f_\theta(\varepsilon j),\quad f_\theta(t)=-\log(1-\ell^2\theta^2e^{-2t}).
\]
The product converges on the indicated real open interval and diverges at its endpoints. The function \(f_\theta\) is smooth and exponentially decaying in \(t\), uniformly with its needed derivatives on compact subintervals of \((-1/\ell,1/\ell)\). The trapezoidal Euler–Maclaurin estimate, including its first endpoint term, gives
\[
K_\varepsilon(\theta)=\frac1\varepsilon\int_0^\infty f_\theta(t)\,dt+\frac12 f_\theta(0)+O(\varepsilon)
=\frac{\Lambda_\ell(\theta)}\varepsilon-\frac12\log(1-\ell^2\theta^2)+O(\varepsilon).
\]
The same estimate can be differentiated twice on compact interior parameter sets. The integral evaluates by substituting \(u=e^{-2t}\), expanding the logarithm absolutely and integrating termwise:
\[
\int_0^\infty f_\theta(t)\,dt
=-\frac12\int_0^1\frac{\log(1-\ell^2\theta^2u)}u\,du
=\frac12\operatorname{Li}_2(\ell^2\theta^2).
\]
Consequently \(\varepsilon K_\varepsilon'(\theta)\to\Lambda_\ell'(\theta)\) and \(\varepsilon K_\varepsilon''(\theta)\to\Lambda_\ell''(\theta)\). Strict positivity of \(\Lambda_\ell''\) follows also by differentiating under the positive integral of the individual positive Laplace variances. The derivative \(\Lambda_\ell'\) is odd, strictly increasing and has limits \(\pm\infty\) at the parameter endpoints, proving the asserted unique optimizer for each real \(y\).

**2. Local tilted central limit theorem with density control.** Fix \(y>0\), write \(\theta=\theta_y\) and let \(Q_\varepsilon\) be the exponential tilt
\[
\frac{dQ_\varepsilon}{dP}=\exp[\theta X_\varepsilon-K_\varepsilon(\theta)].
\]
Under \(Q_\varepsilon\), define \(W_\varepsilon=\sqrt\varepsilon(X_\varepsilon-K_\varepsilon'(\theta))\). By the preceding cumulant expansions, its characteristic functions tend pointwise to those of the centered normal law of variance \(\Lambda_\ell''(\theta)\). To justify *uniform density* convergence rather than relying on a weak central limit alone, the individual tilted Laplace factors yield the explicit bound
\[
|\mathbb E_{Q_\varepsilon}e^{itW_\varepsilon}|
\le\prod_{j=0}^{\lfloor1/\varepsilon\rfloor}(1+\ell^2e^{-2}\varepsilon t^2)^{-1}
\le(1+\ell^2e^{-2}\varepsilon t^2)^{-\lfloor1/\varepsilon\rfloor}.
\]
Indeed each factor's characteristic-function modulus is at most \((1+\ell^2e^{-2\varepsilon j}\varepsilon t^2)^{-1}\), by comparing its denominator to its positive real part. On \(|t|\le\varepsilon^{-1/2}\) this bound has an integrable Gaussian majorant; on the complementary range its integral vanishes exponentially in \(1/\varepsilon\) after the substitution \(u=\sqrt\varepsilon t\). Fourier inversion and dominated convergence therefore give uniform convergence of the density \(g_\varepsilon\) of \(W_\varepsilon\) to the centered Gaussian density, in particular
\[
\sup_w g_\varepsilon(w)=O(1),\qquad g_\varepsilon(z_\varepsilon)\longrightarrow[2\pi\Lambda_\ell''(\theta)]^{-1/2}
\quad\text{whenever }z_\varepsilon\to0.
\]

**3. Exact boundary prefactor.** Inverting the exponential tilt at the sharp threshold gives
\[
\Pr(X_\varepsilon\ge y/\varepsilon)
=e^{K_\varepsilon(\theta)-\theta y/\varepsilon}
\int_0^\infty e^{-\theta u}\,p_{Q_\varepsilon}(y/\varepsilon+u)\,du.
\]
By the differentiated Euler–Maclaurin estimate and \(\Lambda_\ell'(\theta)=y\),
\[
K_\varepsilon'(\theta)=y/\varepsilon-\frac12\frac{d}{d\theta}\log(1-\ell^2\theta^2)+O(\varepsilon)=y/\varepsilon+O(1).
\]
Thus \(p_{Q_\varepsilon}(y/\varepsilon+u)=\sqrt\varepsilon\,g_\varepsilon(\sqrt\varepsilon[u+O(1)])\) tends, for each fixed \(u\), to \(\sqrt\varepsilon/[2\pi\Lambda_\ell''(\theta)]^{1/2}\) at the level of the ratio. The uniform bound on \(g_\varepsilon\), together with \(\theta>0\), allows dominated convergence in the last integral. It is consequently asymptotic to \(\sqrt\varepsilon/[\theta\sqrt{2\pi\Lambda_\ell''(\theta)}]\). The cumulant endpoint term supplies \(\exp[-\tfrac12\log(1-\ell^2\theta^2)]=(1-\ell^2\theta^2)^{-1/2}\), completing the exact relative asymptotic.

**4. Full large-deviation principle and rate geometry.** For an open neighborhood of any \(y\), tilt at its unique \(\theta_y\) and use \(\operatorname{Var}_{Q_\varepsilon}(Y_\varepsilon)=\varepsilon^2K_\varepsilon''(\theta_y)=O(\varepsilon)\) to obtain the local lower bound. Local upper bounds follow from exponential Markov inequalities with any interior tilt. Applying finitely many local upper bounds to compact sets and using exponential tightness from fixed positive and negative interior tilts proves the full upper bound for arbitrary closed sets. The rate is good since its Legendre representation dominates \(c|y|-\Lambda_\ell(c)\) for every \(c\in(0,1/\ell)\). The stated tail logarithm follows by squeezing closed and open half-lines and using continuity and strict increase of \(I_\ell\) on positive arguments. Near zero, expand the dilogarithm and invert \(\Lambda_\ell'\); for large positive \(y\), the optimizer tends to \(1/\ell\), while \(\Lambda_\ell(1/\ell-)=\pi^2/12\), so \(I_\ell(y)=y/\ell-\pi^2/12+o(1)\). Symmetry handles negative arguments.

## Verification

Run `python verify.py` with Python 3.10 or later; no third-party packages are needed. It checks the exact stationary-product cumulants against their Euler–Maclaurin expansion, the convexity and optimizer identities, the small/large rate limits, and independent Fourier inversion of the stationary product for several positive tail thresholds and contraction strengths. The delivered source was executed from its package path and reported **289 deterministic diagnostic assertions passed**. These are finite numerical checks of normalization and constants, not an infinite proof or independent validation; the analytical argument above provides the theorem.

## Relationship to prior work

Pierce (2022) and Tal-Friedman, Roichman and Reuveni (2022) establish the stationary laws of proportional/partial Brownian resetting. The latter explicitly gives the geometric sum of independent Laplace variables and shows the Gaussian weak-reset bulk limit; Di Bello et al. (2023) give time-dependent and stationary densities; Biroli et al. (2024) derive exact stationary densities with fixed-contraction Gaussian cores and exponential spatial tails. Those published formulas supply the starting transform, not the **pointwise sharp relative asymptotic with \(\sqrt\varepsilon\) prefactor and exact endpoint correction** in the simultaneous weak-reset/large-position regime. Vysotsky's (2019) weighted-sum Cramér theorem, and the earlier broad theorem of Najim cited there, cover general logarithmic large-deviation principles; thus the mere existence of a rate principle is *not* asserted to be original. The contribution is the sharp, physically normalized special-model tail including its multiplicative coefficient, obtained by density-level exponential tilting and the subleading Euler–Maclaurin term. General saddlepoint/Bahadur–Rao machinery is classical and is not claimed as original.

## Limitations

The relative tail asymptotic is pointwise for fixed \(y>0\) and \(\ell>0\); a uniform threshold-to-zero or threshold-to-infinity crossover, arbitrary resetting distributions, drift, and finite-time initial conditions are not proved. It is not a claim that fixed-\(a\) exponential tails cease to hold. The method identifies a weak-reset *joint scaling*, not a new stationary transform. As with any specialized sharp asymptotic, a sufficiently general unindexed precise-deviation theorem might imply this special coefficient; the literature comparison does not certify publication priority. No external independent audit has been performed.

## References

1. J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215v1 (first public 2022-04-14). https://arxiv.org/abs/2204.07215
2. O. Tal-Friedman, Y. Roichman and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363v1 (first public 2022-05-06), especially stationary product and Gaussian limit. https://arxiv.org/abs/2205.03363
3. C. Di Bello, A. V. Chechkin, A. K. Hartmann, Z. Palmowski and R. Metzler, *Time-dependent probability density function for partial resetting dynamics*, arXiv:2305.13722v1 (first public 2023-05-23). https://arxiv.org/abs/2305.13722
4. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387 (2024). https://arxiv.org/abs/2406.08387
5. V. Vysotsky, *Contraction principle for trajectories of random walks and Cramér's theorem for kernel-weighted sums*, arXiv:1909.00374 (2019), Theorem 6.1, and its discussion of earlier general weighted-sum large deviations. https://arxiv.org/abs/1909.00374
