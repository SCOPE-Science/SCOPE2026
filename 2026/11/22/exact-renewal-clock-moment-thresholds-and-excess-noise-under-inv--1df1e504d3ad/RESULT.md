# Exact renewal-clock moment thresholds and excess noise under inverse-square adaptive resetting

## Finding

Consider a Brownian particle with adaptive resetting to the origin at position-dependent rate \(r(x)=a/(b+|x|)^2\). The first time between resets has a complete sharp hierarchy of integer moment thresholds, and, whenever its variance is finite, its normalized variance strictly exceeds that of a homogeneous Poisson clock. More precisely, for \(\eta=(\sqrt{1+4a/D}-1)/2\), its \(m\)-th time moment exists if and only if \(\eta>2m-1\), or equivalently \(a/D>2m(2m-1)\), for each integer \(m\ge1\). Equality belongs to the divergent side.

The first two finite moments are
\[
\mathbb E[R]=\frac{b^2}{D\eta(\eta-1)}\qquad(\eta>1),
\]
\[
\mathbb E[R^2]=\frac{2b^4(2\eta-3)}{D^2\eta^2(\eta-1)(\eta-3)(2\eta-1)}\qquad(\eta>3).
\]
Consequently, for \(\eta>3\),
\[
\frac{\operatorname{Var}R}{(\mathbb ER)^2}=1+\frac{4\eta}{(\eta-3)(2\eta-1)}>1.
\]
This ratio decreases strictly with \(a/D\); its limits as \(a/D\downarrow12\) and \(a/D\to\infty\) are \(+\infty\) and \(1\), respectively. After every reset the Brownian motion restarts independently, so the long-run Fano factor of the number \(N(t)\) of completed reset events converges to the same ratio when \(a/D>12\).

## Assumptions and scope

Let \(D,a,b>0\), let \(W_t\) be a one-dimensional standard Brownian motion, let \(X_t=\sqrt{2D}\,W_t\) start at \(X_0=0\), and let \(E\) be a unit exponential random variable independent of \(W\). Define
\[
R=\inf\left\{t\ge0:\int_0^t\frac{a}{(b+|X_s|)^2}\,ds\ge E\right\}.
\]
For successive reset intervals use independent copies of \((W,E)\), and count completed resets by \(N(t)\). The generator of the free diffusion is \(D\partial_{xx}\), not \(D\partial_{xx}/2\). Set \(c=a/D\) and \(\eta=(\sqrt{1+4c}-1)/2\), so \(c=\eta(\eta+1)\). No finite-time cutoff is imposed. The theorem concerns the *clock between resets*, not the time needed to reach a separate spatial target, nor the instantaneous stationary position.

## Proof

**1. Reflected killed diffusion and almost-sure reset.** Put \(Y_t=b+|X_t|\). Then \(Y\) is reflecting Brownian motion on \([b,\infty)\), with interior generator \(D\partial_{yy}\), reflecting boundary derivative \(u'(b)=0\), and killing rate \(a/y^2\). One-dimensional recurrence implies \(\int_0^\infty\mathbf 1_{\{|X_s|\le b\}}ds=\infty\) almost surely. During this occupation the reset hazard is at least \(a/(4b^2)>0\); thus \(R<\infty\) almost surely, even in regimes where its mean diverges.

**2. The Green kernel at the starting point.** The homogeneous killed equation \(Du''-ay^{-2}u=0\) has independent power solutions \(y^{\eta+1}\) and \(y^{-\eta}\). The solution satisfying the reflecting condition is \(u_{\rm ref}(y)=y^{\eta+1}+[(\eta+1)/\eta]b^{2\eta+1}y^{-\eta}\). Combining it with the decreasing solution gives the positive zero-resolvent density at the reflecting endpoint
\[
G(b,y)=\frac{b^{\eta+1}}{D\eta}y^{-\eta},\qquad y\ge b.
\]
For the nonnegative killed functional \(M_m(y)=\mathbb E_y[R^m]\), \(M_0(y)=1\), the Kac recursion at the endpoint reads (allowing \(+\infty\) on either side)
\[
M_m(b)=m\int_b^\infty G(b,y)M_{m-1}(y)\,dy.\tag{1}
\]
The formula follows from the tail-integral identity for time moments and the strong Markov property of the killed diffusion; monotone convergence removes integrability assumptions.

**3. Exact moment thresholds.** For any integer \(m\ge1\), Brownian scaling ensures constants \(\delta,p>0\) such that, uniformly for starting positions \(y\ge b\), the reflected process remains between \(y/2\) and \(3y/2\) for \(\delta y^2/D\) units of time with probability at least \(p\). While there, the accumulated killing hazard is at most \(4a\delta/D\). Hence \(\Pr_y(R>\delta y^2/D)\ge p\exp(-4a\delta/D)\), and, for \(m\ge2\), \(M_{m-1}(y)\ge C_m y^{2m-2}\); the same lower bound for \(m=1\) is simply \(M_0=1\). Applying (1), its integral dominates a constant multiple of \(\int_b^\infty y^{2m-2-\eta}\,dy\), which diverges if \(\eta\le 2m-1\), including equality.

Conversely, suppose \(\eta>2m-1\), equivalently \(a/D>2m(2m-1)\). For each \(1\le k\le m\), consider the positive Neumann supersolution
\[
B_k(y)=y^{2k}+\frac{2k}{\eta}b^{2k+\eta}y^{-\eta}.
\]
It satisfies \(B_k'(b)=0\) and
\[
(-D\partial_{yy}+ay^{-2})B_k
=D\bigl[\eta(\eta+1)-2k(2k-1)\bigr]y^{2k-2}>0.
\]
Assuming inductively \(M_{k-1}(y)\le C y^{2k-2}\) (true initially for \(M_0=1\)), multiply \(B_k\) by a sufficient constant to dominate the inhomogeneity \(kM_{k-1}\). The positive Feynman–Kac resolvent, or equivalently the comparison principle applied to its minimal nonnegative solution, then gives \(M_k(y)\le C' B_k(y)\). Since \(B_k(y)\le C''y^{2k}\) on \([b,\infty)\), the induction closes. In particular \(M_m(b)<\infty\). This establishes the full strict threshold.

**4. Exact first and second moments.** For \(\eta>1\), solving the Neumann problem \(DM_1''-ay^{-2}M_1=-1\) by the minimal positive resolvent gives
\[
M_1(y)=\frac{y^2+(2/\eta)b^{\eta+2}y^{-\eta}}{D(\eta+2)(\eta-1)}.
\]
At \(y=b\), using \(\eta(\eta+1)=a/D\), this simplifies to the first-moment expression in the Finding. If \(\eta>3\), substituting into (1) with \(m=2\) requires only
\[
\int_b^\infty y^{2-\eta}dy=\frac{b^{3-\eta}}{\eta-3},\qquad
\int_b^\infty y^{-2\eta}dy=\frac{b^{1-2\eta}}{2\eta-1}.
\]
Simplification gives the stated \(\mathbb E[R^2]\), and subtracting the squared mean yields
\[
\operatorname{CV}^2(R)=1+\frac{4\eta}{(\eta-3)(2\eta-1)}.
\]
Its derivative with respect to \(\eta\) equals \(-4(2\eta^2-3)/[(\eta-3)^2(2\eta-1)^2]<0\) for \(\eta>3\). The mapping \(a/D\mapsto\eta\) is strictly increasing, giving monotonicity and the boundary limits. Independent identical reset intervals form a renewal process; the standard finite-variance renewal limit \(\operatorname{Var}N(t)/\mathbb EN(t)\to\operatorname{Var}R/(\mathbb ER)^2\) finishes the counting-noise assertion.

## Verification

The accompanying `verify.py` independently checks the Neumann backward equation, closed first and second moment formulas, reflected Green-kernel integral, coefficient-of-variation formula, and its strict negative derivative by symbolic algebra. It also independently solves truncated-domain killed backward equations numerically for \(\eta=4,5,8\). All included checks passed; the finite differences are secondary consistency checks, not substitutes for the infinite-domain Green/resolvent proof. Run `python verify.py` with Python 3, SymPy, NumPy and SciPy installed.

## Relationship to prior work

Keidar and Reuveni (2026) establish inverse-square adaptive-reset localization and the sharp finite-mean reset-time boundary \(a/D=2\), together with a hierarchy for **stationary spatial** moments. These published results are prior art and explicitly not claimed as new here. The present claim is the separate full sequence of **temporal reset-interval** moments, the exact first and second temporal moments for the specified nonsingular inverse-square profile, the positive excess in their squared coefficient of variation, and its renewal-count interpretation. The equality of the second temporal-moment threshold and a previously identified stationary spatial-variance threshold does not by itself furnish the temporal formula or excess-noise classification.

Roldán and Gupta (2017) formulate the first-reset-time distribution for arbitrary space-dependent rates and solve examples involving constant or parabolic rates and harmonic confinement, without the inverse-square reset-clock formula above. Pinsky (2018) studies target-hitting times under spatially dependent resetting, not the reset-event waiting time. Aspman, Mastropietro, and Mareček (2026) consider mean target first-passage times under spatially varying resetting, not these temporal moments. The positive killed resolvent and moment recursion are standard Feynman–Kac tools; only their derived specialized classification is being claimed.

## Limitations

This is a one-dimensional, free, driftless Brownian model with the **specific** regularized rate \(a/(b+|x|)^2\). Other regularizations can have the same power-law thresholds without sharing these exact finite moment values. The claim does not establish finite-sample estimation accuracy or universality of the closed coefficient-of-variation formula. The renewal Fano limit is asserted only when the first two moments exist (\(a/D>12\)); no finite-variance central limit claim is made in the divergent-variance regimes. An unindexed equivalent prior exact resolvent calculation remains a publication-priority risk. All evidence here is proof and mathematical reproducibility, not independent scientific validation.

## References

1. T. D. Keidar and S. Reuveni, *Localization–Delocalization Transition in Diffusion with Adaptive Resetting*, arXiv:2608.27090 (first posted 2026-08-27), https://arxiv.org/abs/2608.27090.
2. É. Roldán and S. Gupta, *Path-integral formalism for stochastic resetting: Exactly solved examples and shortcuts to confinement*, Physical Review E 96, 022130 (2017), https://arxiv.org/abs/1703.10615.
3. R. G. Pinsky, *Diffusive Search with Spatially Dependent Resetting*, arXiv:1805.00320 (2018), https://arxiv.org/abs/1805.00320.
4. J. Aspman, D. Mastropietro, and J. Mareček, *First-passage time in space-dependent stochastic resetting*, Physical Review E 114, 024110 (2026), https://doi.org/10.1103/w2yj-91m8.
