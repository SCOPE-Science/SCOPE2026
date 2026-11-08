# Exact minimax first-step progress for ellipsoidal zeroth-order sampling

## Finding

Consider the first step of the POEM-ES two-point method using a fixed, full-rank, normalized preconditioner in two dimensions. For each \(0<\delta<1\), let \(\widehat\Sigma_\delta=\operatorname{diag}(1,\delta)\), and let \(D_\delta(a)\) denote the expected decrease in a unit-slope linear objective after the normalized first step, with \(\|a\|_2=1\). Set
\[
 m_\delta=\min_{\|a\|_2=1}D_\delta(a),\qquad L_\delta=\log(1/\delta).
\]
Then
\[
 \boxed{\lim_{\delta\downarrow0}\frac{m_\delta}{\sqrt{\delta L_\delta}}=\frac{2\sqrt2}{\pi}.}
\]
Writing any minimizing slope, up to coordinate sign changes, as \(a_\delta=(q_\delta,\sqrt{1-q_\delta^2})\), every minimizer obeys
\[
 \boxed{q_\delta\sqrt{L_\delta}\longrightarrow\sqrt2.}
\]
For comparison, isotropic sampling \(\widehat\Sigma=I_2\) gives exactly \(D_{\mathrm{iso}}(a)=2/\pi\) in every direction. Thus the sharp worst-direction first-step progress for the specified anisotropic estimator vanishes, with normalized anisotropy condition number \(\kappa=1/\delta\), at rate \(\sqrt{\log\kappa/\kappa}\), and the worst slope is not exactly aligned with the weak eigenvector.

A finite-\(\delta\) formula is available. Put \(q=|a_1|\), \(s=|a_2|=\sqrt{1-q^2}\), and \(H=\sqrt{q^2+\delta s^2}\). Then
\[
 \boxed{D_\delta(a)=\frac{2}{\pi\sqrt{1-\delta}}\left[\sqrt\delta\,q\,\operatorname{arsinh}\!\left(\sqrt{\frac{1-\delta}{\delta}}\frac{q}{H}\right)+s\,\arcsin\!\left(\sqrt{1-\delta}\frac{\sqrt\delta\,s}{H}\right)\right].}
\]
The exact formula includes the coordinate-axis endpoints \(q=0\) and \(q=1\), and extends continuously to \(\delta=1\) with the stated isotropic value.

## Assumptions and scope

Fix \(0<\delta<1\), a unit vector \(a\in\mathbb R^2\), the compact convex feasible disk \(\mathcal X=\{x\in\mathbb R^2:\|x\|_2\le2\}\), and the deterministic Lipschitz convex objective \(F(x)=f_a(x)=a^\top x\) for all \(x\in\mathbb R^2\). Its minimizer on the disk is \(x_*=-2a\). Initialize at \(x_0=0\) and use initial mobility \(r_\epsilon=1\). The fixed preconditioner is \(\widehat\Sigma_\delta=\operatorname{diag}(1,\delta)\), with maximal eigenvalue one, active rank \(r=2\), and effective dimension \(d^*=1+\delta\). Hence all coordinates belong to the active subspace, the objective is exactly subspace aligned, and the projection and initial-distance assumptions are satisfied.

Use the rank-scaled ellipsoidal two-point estimator and distance-over-accumulated-gradient step rule of the POEM-ES algorithm in Sholokhov--Rogozin (arXiv:2609.38561v2), not a generic covariance-adapted algorithm. At its first iteration, draw \(v=(\cos t,\sin t)\) uniformly on the circle, use smoothing \(\mu_0=\sqrt{1+\delta}\), and compute
\[
 g_0=\frac{2}{2\mu_0}\bigl[f_a(\mu_0\widehat\Sigma^{1/2}v)-f_a(-\mu_0\widehat\Sigma^{1/2}v)\bigr]\widehat\Sigma^{-1/2}v
 =2(a^\top\widehat\Sigma^{1/2}v)\widehat\Sigma^{-1/2}v.
\]
The zero-gradient event has probability zero. With \(G_0=\|g_0\|_2^2\), the first stepsize is \(\eta_0=1/\sqrt{G_0}\), and \(x_1=-g_0/\|g_0\|_2\). Projection is inactive because \(\|x_1\|_2=1<2\). We study only the expected first-step objective decrease
\[
 D_\delta(a)=\mathbb E[f_a(x_0)-f_a(x_1)]=\mathbb E\left[\frac{a^\top g_0}{\|g_0\|_2}\right].
\]
All expectations are over the single uniform spherical direction, and there is no oracle noise. The statement does not address later iterations, output averaging, or multi-step convergence.

## Proof

**1. Angular reduction and the exact formula.** Coordinate reflections commute with the diagonal preconditioner and preserve the uniform law, so take \(a=(q,s)\) with \(q,s\ge0\) and \(q^2+s^2=1\). Let \(H=\sqrt{q^2+\delta s^2}\), \(\alpha\in[0,\pi/2]\) be specified by \(\cos\alpha=q/H\), \(\sin\alpha=\sqrt\delta\,s/H\), and put \(v=(\cos t,\sin t)\). The sign of \(a^\top\widehat\Sigma^{1/2}v\) is that of \(\cos(t-\alpha)\). Canceling the positive magnitude of this inner product in the normalized estimator and then pairing antipodal directions gives
\[
 D_\delta(q)=\frac1\pi\int_{\alpha-\pi/2}^{\alpha+\pi/2}
 \frac{q\cos t+(s/\sqrt\delta)\sin t}{\sqrt{\cos^2t+(1/\delta)\sin^2t}}\,dt.
\]
For \(c=1-\delta\), elementary substitutions yield the primitives
\[
 \int\frac{\cos t\,dt}{\sqrt{\cos^2t+\delta^{-1}\sin^2t}}=\frac{\sqrt\delta}{\sqrt c}\operatorname{arsinh}\left(\sqrt{c/\delta}\sin t\right),
\]
\[
 \int\frac{\sin t\,dt}{\sqrt{\cos^2t+\delta^{-1}\sin^2t}}=-\frac{\sqrt\delta}{\sqrt c}\arcsin(\sqrt c\cos t).
\]
At the two endpoints, \(\sin(\alpha\pm\pi/2)=\pm\cos\alpha\) and \(\cos(\alpha\pm\pi/2)=\mp\sin\alpha\). Evaluation proves the boxed exact formula, with no approximation or numerical integration. At \(\delta=1\), uniform-angle symmetry directly gives \(\mathbb E|a^\top v|=2/\pi\).

**2. Compactness and the upper estimate.** The expression is continuous in \(q\in[0,1]\) for every \(\delta>0\), so the minimum exists. Put \(L=\log(1/\delta)\) and choose the trial direction \(q=\sqrt{2/L}\), for \(L>2\). As \(\delta\downarrow0\), \(s=1+o(1)\), \(H=q(1+o(1))\), and
\[
 \operatorname{arsinh}\left(\sqrt{(1-\delta)/\delta}\frac qH\right)=\tfrac12 L+O(1),\qquad
 \arcsin\left(\sqrt{1-\delta}\frac{\sqrt\delta\,s}{H}\right)=\frac{\sqrt\delta}{q}(1+o(1)).
\]
Consequently \(m_\delta\le(2\sqrt2/\pi+o(1))\sqrt{\delta L}\).

**3. All minimizing directions have scale \(L^{-1/2}\).** Let \(q_\delta\) be any minimizer and write \(s_\delta=\sqrt{1-q_\delta^2}\). First, \(q_\delta<1/\sqrt2\) for all sufficiently small \(\delta\). Indeed, for \(q\ge1/\sqrt2\), \(H\le1\) and the first positive term in the exact formula has size at least a fixed constant times \(\sqrt\delta L\), strictly larger than the trial upper bound \(O(\sqrt{\delta L})\). Thus \(s_\delta^2\ge1/2\).

Since \(\arcsin u\ge u\) for \(u\in[0,1]\), the second term yields
\[
 D_\delta(q_\delta)\ge\frac{2\sqrt\delta\,s_\delta^2}{\pi H}\ge\frac{\sqrt\delta}{\pi H}.
\]
The trial upper bound forces \(H\ge c/\sqrt L\) for a fixed \(c>0\); as \(H^2=q_\delta^2+\delta s_\delta^2\) and \(\delta L\to0\), this implies \(q_\delta\ge c'/\sqrt L\). Uniformly over such directions, \(q_\delta/H=1+O(\delta L)\) and the inverse-hyperbolic-sine factor is \(L/2+O(1)\). The first positive term then gives a bound proportional to \(\sqrt\delta\,q_\delta L\). Combining with the trial upper bound yields \(q_\delta\le C'/\sqrt L\). Therefore
\[
 0<c'\le q_\delta\sqrt L\le C'<\infty
\]
for every minimizing direction when \(\delta\) is sufficiently small.

**4. Uniform limiting optimization.** Set \(q=t/\sqrt L\) with \(t\) in any fixed compact subset of \((0,\infty)\). The exact formula, uniformly on that set, gives
\[
 \frac{D_\delta(t/\sqrt L)}{(2/\pi)\sqrt{\delta L}}
 =\frac t2+\frac1t+o(1).
\]
The positive function \(t/2+1/t\) has the **unique** global minimizer \(t=\sqrt2\) and minimum \(\sqrt2\). Since all true minimizers have \(t\) in a common compact subinterval, uniform convergence implies that every such minimizer satisfies \(q_\delta\sqrt L\to\sqrt2\), and \(m_\delta/\sqrt{\delta L}\to2\sqrt2/\pi\). This completes the proof.

## Verification

The self-contained standard-library checker `verify_progress.py` evaluates the exact closed formula, checks it against direct periodic Simpson integration at twenty parameter/direction pairs, tests ancillary sign geometry, tests three small-anisotropy numerical minima and the isotropic limit. Running `python3 verify_progress.py` prints `CHECKS_OK 460`. These finite numerical checks are corroboration only. The analytic integral evaluation, compactness, uniform bounds, and limiting minimization above prove the continuum and asymptotic assertions independently of the checker.

## Relationship to prior work

Sholokhov and Rogozin, *Parameter-Free Zeroth-Order Optimization with Ellipsoidal Sampling*, arXiv:2609.38561v2, Section 3 Algorithm 1, supplies the exact rank-scaled, fixed-preconditioner estimator and parameter-free normalization investigated here. Its analysis already incorporates the preconditioner's condition number in general oracle-complexity bounds. This finding does **not** contradict or improve those bounds: it identifies the exact worst-angle first-step expected-progress invariant and its sharp asymptotic on a unit-Lipschitz linear family. The public preprint first appeared September 29, 2026, under an earlier title and was revised in October 2026.

Ren and Luo, *A Parameter-Free and Near-Optimal Zeroth-Order Algorithm for Stochastic Convex Optimization*, arXiv:2502.05600 (2025), treats the isotropic parameter-free method, not this ellipsoidal directional minimax. The planar angular-central-Gaussian literature, including Vareilles, arXiv:2605.31536 (2026), studies angular distribution moments; those moments alone do not state the signed normalized first-step minimax. Gaussian sign-correlation formulas also precede this finding and are not asserted as new. The distinctive claim is the exact optimizer-dependent expected-progress frontier for the specified update.

## Limitations

The theorem is restricted to the first update, a full-rank two-dimensional diagonal preconditioner, deterministic unit-Lipschitz linear objectives on the radius-two disk, and the algorithm's unregularized distance-over-accumulated-norm rule. It says nothing about the final averaged iterate, subsequent iteration dependence, noisy function values, alternative stepsizes, adaptive covariance updates, finite-precision cancellations, or higher-dimensional minimax problems. The source's existing condition-number-dependent rate is not contradicted. Historical priority is not independently certified; a broader prior signed-angular minimax identity could imply this specialization.

## References

1. A. Sholokhov and A. Rogozin, *Parameter-Free Zeroth-Order Optimization with Ellipsoidal Sampling*, arXiv:2609.38561v2, 2026. https://arxiv.org/html/2609.38561v2 (first public arXiv posting 2026-09-29).
2. K. Ren and L. Luo, *A Parameter-Free and Near-Optimal Zeroth-Order Algorithm for Stochastic Convex Optimization*, arXiv:2502.05600, 2025. https://arxiv.org/abs/2502.05600.
3. S. Vareilles, *Closed-form linear moments of the two-dimensional angular central Gaussian distribution*, arXiv:2605.31536, 2026. https://arxiv.org/abs/2605.31536.
4. P. Li, *Sign-Full Random Projections*, Proceedings of AAAI 2019, DOI:10.1609/aaai.v33i01.33014205, 2019. https://doi.org/10.1609/aaai.v33i01.33014205.
