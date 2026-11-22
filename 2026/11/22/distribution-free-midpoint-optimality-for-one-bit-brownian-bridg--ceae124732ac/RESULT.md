# Distribution-free midpoint optimality for one-bit Brownian-bridge occupation sensing

## Finding

**Theorem (a universal one-bit observation location).** Let \(B_t=W_t-tW_1\), \(0\le t\le1\), be a standard zero-to-zero Brownian bridge and let
\[
Q=\int_0^1\mathbf1_{\{B_s>0\}}\,ds.
\]
At any predetermined \(t\in(0,1)\), observe only the binary value
\[
Y_t=\operatorname{sgn}(B_t+\sigma(t)N),
\]
where \(N\) is independent of the entire bridge, finite almost surely, and has a distribution symmetric about zero. Assume \(\sigma(t)\ge0\) is deterministic and finite and that its *standardized noise scale*
\[
r(t)=\frac{\sigma(t)}{\sqrt{t(1-t)}}
\]
satisfies \(r(t)\ge r(1/2)\) for every \(t\in(0,1)\). Then \(t=1/2\) is the **unique global minimizer** of the Bayes mean-square error \(\mathbb E[(Q-\mathbb E[Q\mid Y_t])^2]\). The result holds for every such symmetric noise law, including discrete, heavy-tailed, and degenerate laws. In particular it holds both for fixed absolute noise amplitude \(\sigma(t)=\sigma_0\) and fixed relative noise amplitude \(\sigma(t)=r_0\sqrt{t(1-t)}\).

The optimal conditional estimator has the form
\[
\widehat Q_t=\frac12+C(t)Y_t,\qquad
R(t)=\frac1{12}-C(t)^2,
\]
where \(C(t)=\mathbb E[QY_t]\). For Gaussian \(N\sim\mathcal N(0,1)\), put \(r_*=r(1/2)\), \(a=(1+r_*^2)^{-1/2}\), and
\[
F(a)=\frac{-\arcsin(a)+\frac{2a}{\sqrt{1+a^2}}\arctan\!\sqrt{\frac{1+a^2}{1-a^2}}}{\pi},\quad 0<a<1,
\]
with its continuous value \(F(1)=(\sqrt2-1)/2\). Then the **exact globally minimal risk** is
\[
R_{\min}=\frac1{12}-F(a)^2.
\]
With no measurement noise, \(C(t)=(\sqrt t+\sqrt{1-t}-1)/2\), and therefore
\[
t_*=\frac12,\quad R_{\min}=\frac{3\sqrt2-4}{6},\quad
\frac{\operatorname{Var}(\mathbb E[Q\mid Y_{t_*}])}{\operatorname{Var}(Q)}=9-6\sqrt2\approx0.5147186258.
\]

## Assumptions and scope

The functional is the *positive* occupation fraction of a unit-time standard Brownian bridge. The decision is the observation time of one binary sign of a noisy point sample; no real-valued amplitude is retained. The noise has the same distribution at every candidate time up to the known multiplicative scale \(\sigma(t)\), and is independent of \(B\). Atoms in \(N\) are permitted: since \(B_t\) is nondegenerate normal for interior \(t\), ties occur with probability zero. The Bayes prior is the Brownian-bridge law, and squared loss is used. The standardized-noise minimum is a substantive assumption; arbitrary time-dependent asymmetric signal-to-noise schedules are not covered.

## Proof

**1. Binary Bayes-risk reduction.** Symmetry of \(B\) and of \(N\) gives \(\Pr(Y_t=1)=\Pr(Y_t=-1)=1/2\) and \(\mathbb E Q=1/2\). Thus \(\mathbb E[Q\mid Y_t]=1/2+C(t)Y_t\), where \(C(t)=\mathbb E[QY_t]\ge0\). The classical Lévy law states that the occupation fraction of a zero-to-zero Brownian bridge is uniform on \([0,1]\); hence \(\operatorname{Var}(Q)=1/12\), and the law of total variance gives \(R(t)=1/12-C(t)^2\). The cited two-time bridge sign-correlation and occupation results provide a separate route to this variance.

**2. Monotonicity for arbitrary symmetric noise.** Put \(Z_s=B_s/\sqrt{s(1-s)}\) for interior \(s\). For standard normal \((X,Z)\) with correlation \(\rho\in[0,1]\), and independent symmetric \(N\), define
\[
K_r(\rho)=\mathbb E[\operatorname{sgn}(X)\operatorname{sgn}(Z+rN)].
\]
For \(r>0\) and almost all \(z>0\), symmetry yields
\[
f_r(z):=\mathbb E[\operatorname{sgn}(z+rN)]=\Pr(|N|<z/r)\ge0,
\]
with \(f_0(z)=1\). Consequently \(f_r(z)\) is nonincreasing in \(r\). Conditioning on \(Z=z\) gives, for \(0<\rho<1\),
\[
K_r(\rho)=2\int_0^\infty \phi(z)f_r(z)
\left[2\Phi\!\left(\frac{\rho z}{\sqrt{1-\rho^2}}\right)-1\right]dz,
\]
where \(\phi,\Phi\) are the standard normal density and distribution function. For \(z>0\), the term in brackets is strictly increasing in \(\rho\), and because \(N\) is finite almost surely, \(f_r\) is positive on a set of positive Gaussian measure for every finite \(r\). It follows that \(K_r(\rho)>0\) and strictly increases with \(\rho\in[0,1]\), and is nonincreasing in \(r\). Endpoint values follow by dominated convergence.

**3. Log-odds transform and the strict convolution lemma.** Define \(x=\log(s/(1-s))\) and \(z=\log(t/(1-t))\). Direct use of the Brownian-bridge covariance gives
\[
\operatorname{Corr}(Z_s,Z_t)=e^{-|x-z|/2},\quad
ds=w(x)dx,\quad w(x)=\frac{e^x}{(1+e^x)^2}=\frac1{4\cosh^2(x/2)}.
\]
The weight \(w\) is even and strictly decreasing on \((0,\infty)\). For every *fixed* finite \(r\), let \(k_r(v)=K_r(e^{-|v|/2})\). This function is even, strictly decreasing for \(v>0\), nonnegative, and tends to zero at infinity. Since \(Q=1/2+(1/2)\int_0^1\operatorname{sgn}(B_s)ds\),
\[
C_r(z)=\frac12\int_{-\infty}^{\infty}w(x)k_r(x-z)dx.
\]
The following strict rearrangement statement is used: if \(w\) is even and strictly decreasing away from zero and \(k\) is nonzero, even, nonnegative, decreasing away from zero and vanishing at infinity, then \(w*k\) is even and strictly decreasing for positive shifts whenever \(k\) is strictly decreasing. To prove this without differentiability assumptions on \(k\), write \(k(u)=\int_{(0,\infty)}\mathbf1_{\{|u|<v\}}\,\mu(dv)\) by its Stieltjes layer-cake measure. For each \(v>0\), the derivative of \(\int_{z-v}^{z+v}w(x)dx\) is \(w(z+v)-w(z-v)<0\) for every \(z>0\). Integrating these strict inequalities against the nonzero positive measure \(\mu\) proves the assertion. Thus \(C_r(z)<C_r(0)\) whenever \(z\ne0\).

**4. Time-dependent noise and global uniqueness.** Set \(r_*=r(1/2)\). Pointwise monotonicity of \(K_r\) in its noise scale gives \(C(t)\le C_{r_*}(\log(t/(1-t)))\). For every \(t\ne1/2\), the strict convolution result makes the right-hand side strictly smaller than \(C_{r_*}(0)=C(1/2)\). Since \(C\ge0\), minimizing \(R(t)=1/12-C(t)^2\) is equivalent to maximizing \(C(t)\). This proves unique global midpoint optimality under the stated assumption, with no continuity assumption on \(\sigma\) or density assumption on \(N\).

**5. Exact Gaussian and noiseless constants.** If \(N\) is standard Gaussian, the Gaussian sign-correlation identity gives \(K_{r_*}(\rho)=\frac2\pi\arcsin(a\rho)\), \(a=(1+r_*^2)^{-1/2}\). By reflection symmetry around the midpoint,
\[
C_{r_*}(0)=\frac2\pi\int_0^{1/2}\arcsin\!\left(a\sqrt{\frac{s}{1-s}}\right)ds.
\]
Substitute \(u=\sqrt{s/(1-s)}\) and integrate by parts. This gives
\[
C_{r_*}(0)=\frac{-\arcsin a+2a\int_0^1\frac{du}{(1+u^2)\sqrt{1-a^2u^2}}}{\pi},
\]
and evaluating the remaining elementary integral gives \(F(a)\) as stated. The value at \(a=1\) is its continuous limit. More generally, at zero noise, integrate the bridge sign-correlation formula on either side of \(s=t\):
\[
\int_0^t\arcsin\rho(s,t)ds=\frac\pi2(t-1+\sqrt{1-t}),\quad
\int_t^1\arcsin\rho(s,t)ds=\frac\pi2(\sqrt t-t).
\]
Their sum divided by \(\pi\) yields the stated \(C(t)\). Its midpoint value and the uniform occupation variance give the displayed optimal risk and explained fraction. This completes the proof.

## Verification

The self-contained numerical script `verify.py` uses SciPy only, with its minimal dependency in `requirements.txt`. Running `python verify.py` checks the noiseless formula against direct quadrature at nine off-center times, the Gaussian midpoint closed form for seven noise correlations, strict midpoint superiority for 56 additional Gaussian designs and 24 fixed-absolute-noise designs, plus 18 non-Gaussian two-point-symmetric-noise comparisons and two exact-constant identities: 116 deterministic assertions in total. These are supplementary checks; the all-times, all-noise-law statement is proved analytically above.

## Relationship to prior work

Godrèche (2017), section 5.4, states the Brownian-bridge two-time sign correlation, and section 6 records the classical uniform occupation-time law. These are used as **known inputs**, not claimed as novel. The noiseless one-bit covariance formula follows by integrating the known correlation and should not be treated as independently new. Pozdnyakov et al. (2014) develop noisy full-valued Brownian-location interpolation and occupation estimators, not a one-bit design optimum. Ivanovs–Podolskij (2020) and Altmeyer–Le Guével (2021) study high-frequency full-valued observations of Brownian or Lévy occupation functionals. The present claim concerns a single binary sign, non-Gaussian symmetric sensor noise, a standardized-noise-minimum condition, and **unique globally optimal observation placement**; no implication covering that joint theorem was found in the inspected material.

## Limitations

Only one nonadaptive one-bit sign is retained. The prior process is a zero-to-zero *Gaussian* Brownian bridge and the objective is positive occupation under squared loss; a Brownian motion, drifted bridge, other excursion functional, multiple bits, adaptive choices, or asymmetric noise are not covered. Absolute noise with a constant amplitude is covered, but arbitrary time-varying scales need not have their standardized minimum at the midpoint. The exact minimal-risk closed form assumes Gaussian measurement noise; for arbitrary symmetric noise only the optimal location and the covariance integral characterization are proved. Search comparisons do not establish worldwide publication priority, and no independent audit is claimed.

## References

1. C. Godrèche, *Two-time correlation and occupation time for the Brownian bridge and tied-down renewal processes*, arXiv:1704.04406, first submitted 14 April 2017; especially sections 5.4 and 6. https://arxiv.org/abs/1704.04406
2. V. Pozdnyakov, T. Meyer, Y.-B. Wang, J. Yan, *On modeling animal movements using Brownian motion with measurement error*, Ecology 95 (2014), 247–253. https://doi.org/10.1890/13-0532.1
3. J. Ivanovs and M. Podolskij, *Optimal estimation of some random quantities of a Lévy process*, arXiv:2001.02517 (2020), section 3. https://arxiv.org/abs/2001.02517
4. R. Altmeyer and R. Le Guével, *Optimal L2-approximation of occupation and local times for symmetric stable processes*, arXiv:2108.11632 (2021). https://arxiv.org/abs/2108.11632
