# Gaussianity resonance and a strict fourth-moment defect in random-batch harmonic sampling

## Finding

For random-batch Euler sampling of an all-to-all linear attractive interaction, the invariant distribution is Gaussian at exactly **one** positive stepsize within the entire finite-second-moment stability interval. Outside that isolated point the stationary pair contrast has a strictly positive fourth-moment defect, even though the forcing is Gaussian and the equilibrium covariance has an elementary closed form. This is a statement about distributional shape, not a claim of sampling the exact continuous-time target.

Fix integers \(N,p\) with \(2\le p<N\) and \(p\mid N\), and parameters \(\alpha,\kappa,\sigma>0\). Put
\[
c=\frac p{p-1},\quad m=\frac N{N-1},\quad
D=\alpha^2+2\alpha\kappa m+\kappa^2cm,
\quad h_{\max}=\frac{2(\alpha+\kappa m)}D,
\quad h_*=\frac2{2\alpha+\kappa c}.
\]
For \(0<h<h_{\max}\), the invariant covariance and its Gaussianity frontier are
\[
\operatorname{Cov}(X_\infty)=uJ+v(I-J),\quad
u=\frac{\sigma^2}{2\alpha-\alpha^2h},\quad
v=\frac{\sigma^2}{2(\alpha+\kappa m)-Dh},
\quad J=\frac{\mathbf1\mathbf1^\top}N,
\]
\[
\mathcal L(X_\infty)\text{ is Gaussian}\ \Longleftrightarrow\ h=h_*;
\qquad h=h_*\Longrightarrow X_\infty\sim N(0,uI).
\]
For \(Y=X_\infty^1-X_\infty^2\), with \(a=1-\alpha h\) and \(b=1-(\alpha+\kappa c)h\), the fourth-moment defect satisfies (in the extended sense when the fourth moment is infinite)
\[
\mathbb E[Y^4]-3(\mathbb E[Y^2])^2
\ge\frac{12v^2(p-1)(N-p)}{p^2(N-1)^2}(b^2-a^2)^2,
\qquad \mathbb E[Y^2]=2v.
\]
This lower bound is strictly positive at every stable stepsize other than \(h_*\). No stationary law with finite second moment exists when \(h\ge h_{\max}\).

## Assumptions and scope

At every integer time \(k\), independently draw a uniformly random equipartition \(\mathcal B_k\) of \(\{1,\ldots,N\}\) into unlabeled groups of size \(p\). Independently draw \(\xi_k\sim N(0,I_N)\). The stochastic update is, for the unique group \(B_k(i)\) containing coordinate \(i\),
\[
X_{k+1}^i=X_k^i-h\alpha X_k^i
-\frac{h\kappa}{p-1}\sum_{j\in B_k(i),\ j\ne i}(X_k^i-X_k^j)
+\sigma\sqrt h\,\xi_k^i.
\]
Here \(h\) is constant and every group is redrawn each step; batch randomness, Gaussian forcing and initial state are mutually independent. Unbiased random batching alone is not treated as a Gaussian approximation. Existence/uniqueness is asserted within the space of invariant laws with finite second moment.

## Proof

**1. Random orthoprojectors.** For a partition \(\mathcal B\), let \(P_\mathcal B\) subtract each group's arithmetic mean from its coordinates. It is an orthogonal projector of rank \(N-N/p\), annihilates \(\mathbf1\), and the batch force matrix equals \(cP_\mathcal B\). Define \(H=I-J\). Permutation symmetry and the trace give
\[
\mathbb E P_\mathcal B=qH,\qquad q=\frac{N(p-1)}{p(N-1)}=\frac mc,
\qquad P_\mathcal B^2=P_\mathcal B.
\]
Indeed, every coordinate pair has the same probability \((p-1)/(N-1)\) of occupying one group. Thus the random Euler matrix is \(A_\mathcal B=aI-\kappa hcP_\mathcal B\), with eigenvalues \(a\) on groupwise constants and \(b=a-\kappa hc\) on within-group contrasts. Direct expansion yields
\[
\mathbb E A_\mathcal B^2=a^2J+\rho H,
\quad \rho=(1-q)a^2+qb^2
=1-2(\alpha+\kappa m)h+Dh^2.
\]

**2. Sharp second-moment condition.** Since the fresh batch is independent of the previous iterate, for any synchronously coupled trajectories the squared center-mode difference contracts by \(a^2\) and the expected squared contrast-mode difference by \(\rho\). Thus \(|a|<1\) and \(\rho<1\) imply an \(L^2\)-convergent stationary perpetuity, uniqueness among finite-second-moment invariant laws and convergence to it under synchronous coupling. Here \(\rho<1\) is exactly \(0<h<h_{\max}\); moreover \(h_{\max}<2/\alpha\), so this condition also implies \(|a|<1\). Conversely any stationary finite-second-moment law must satisfy
\[
\mathbb E\|HX\|^2=\rho\,\mathbb E\|HX\|^2+(N-1)\sigma^2h,
\]
which is impossible for \(\rho\ge1\). Exchangeability and uniqueness force a covariance \(uJ+vH\). Solving its two independent trace equations gives
\[
u=\frac{\sigma^2h}{1-a^2},\qquad v=\frac{\sigma^2h}{1-\rho},
\]
which reduce to the displayed rational formulas.

**3. Conditional Gaussian mixture and the exceptional reflection.** Construct the stationary solution from two-sided independent Gaussian forcing and the preceding independent random matrices. Its expected squared norm is finite by Step 2. Conditional on the entire past sequence of partitions, it is centered Gaussian with a finite random covariance \(S\); also \(\mathbb ES=uJ+vH\). When \(b=-a\), equivalently \(h=h_*\) (the case \(b=a\) would require \(h\kappa c=0\)), one has \(A_\mathcal B=a(I-2P_\mathcal B)\), a scalar multiple of an orthogonal reflection. Every product of these matrices is a scalar multiple of an orthogonal matrix, so the conditional covariance equals the deterministic matrix \(\sigma^2h(1-a^2)^{-1}I\). Thus the invariant law is exactly isotropic Gaussian. The value \(h_*\) lies strictly inside \((0,h_{\max})\), as is evident from \(\rho(h_*)=a(h_*)^2<1\).

**4. Strict non-Gaussianity away from reflection.** Let \(w=e_1-e_2\) and \(Y=w^\top X_\infty\). Given past partitions, \(Y\) is centered Gaussian with variance \(T=w^\top S w\). Therefore \(\mathbb EY^4=3\mathbb ET^2\), including the possibility \(+\infty\), and \(\mathbb ET=2v\). Conditional Jensen gives
\[
\mathbb EY^4-3(2v)^2=3\operatorname{Var}(T)
\ge3\operatorname{Var}(\mathbb E[T\mid\mathcal B_0]).
\]
Independence of the newest partition from the earlier covariance and the stationary covariance identity imply
\[
\mathbb E[T\mid\mathcal B_0]
=2\sigma^2h+v\big(2a^2+(b^2-a^2)\|P_{\mathcal B_0}w\|^2\big).
\]
The two coordinates \(1,2\) occur in one batch with probability \(s=(p-1)/(N-1)\). On this event \(\|P_\mathcal B w\|^2=2\); otherwise it equals \(2-2/p\). Consequently
\[
\operatorname{Var}(\|P_\mathcal B w\|^2)=\frac4{p^2}s(1-s)
=\frac{4(p-1)(N-p)}{p^2(N-1)^2}.
\]
Substituting yields the fourth-moment lower bound. Since \(0<s<1\), and \(b^2=a^2\) occurs precisely at \(h=h_*\) for \(h>0\), the defect is strictly positive elsewhere. Hence the contrast, and therefore the full invariant law, is not Gaussian. This completes the equivalence.

## Verification

Run `python3 verify_random_batch.py` with Python 3 and no third-party packages. The program enumerates equipartitions for \((N,p)=(4,2),(6,2),(6,3),(8,2),(8,4)\), verifies rational projector identities and pair-occupancy moments, checks the exact covariance contraction factor, and checks the reflection identity and stability location. For \(N=4,p=2,\alpha=\kappa=\sigma=1,h=1/4\), it verifies \(\rho=11/48\), \(v=12/37\), and fourth-excess lower bound \(24/1369\). The reflection occurs at \(h=1/2\), and the mean-square ceiling is \(h_{\max}=14/19\). These finite checks corroborate algebraic steps; the all-parameter and invariant-law claims are proved above, not inferred from enumeration.

## Relationship to prior work

Jin, Li and Liu introduced the random-batch methodology and its force-unbiasedness, with convergence analysis, in the 2018 preprint [1]. Jin, Li, Ye and Zhou [2] studied ergodicity and long-time sampling error in the continuous-time random-batch system, while Ye and Zhou [3] analyzed the time-discrete Euler scheme via strong error and Wasserstein bounds. Xu, Zhao and Zhou [4] studied variance compensation in Langevin random-batch simulation. These sources motivate the harmonic model and distributional question. Their inspected results do not report this exact finite-second-moment boundary, the unique Gaussian reflection step, or the explicit fourth-moment contrast defect. General Gaussian-mixture and random-affine-recursion principles are background tools, not claimed as new.

## Limitations

The finding treats the stated *fully discrete* uniformly repartitioned, linear overdamped, additively Gaussian model. It does not cover nonlinear interactions, nonuniform or correlated partitions, variable stepsizes, multiplicative noise, underdamped dynamics or continuously integrated random-batch flows. Even at the Gaussian reflection step, the invariant law is generally **not** the Gibbs law of the full interacting SDE: the full system has different center and contrast variances, whereas the resonant random-batch law is isotropic. The fourth-moment defect may equal \(+\infty\) at some mean-square stable stepsizes, and only a lower bound, not an exact fourth moment, is asserted. Specialist publication precedence, especially general random-affine-recursion formulations, remains a residual risk.

## References

[1] S. Jin, L. Li and J.-G. Liu, *Random Batch Methods (RBM) for Interacting Particle Systems*, arXiv:1812.10575v1 (first public 2018-12-26), https://arxiv.org/abs/1812.10575.

[2] S. Jin, L. Li, X. Ye and Z. Zhou, *Ergodicity and Long-time Behavior of the Random Batch Method for Interacting Particle Systems*, arXiv:2202.04952v1 (2022-02-10), https://arxiv.org/abs/2202.04952.

[3] X. Ye and Z. Zhou, *Error Analysis of Time-Discrete Random Batch Method for Interacting Particle Systems and Associated Mean-Field Limits*, arXiv:2206.02166v1 (2022-06-05), https://arxiv.org/abs/2206.02166.

[4] Z. Xu, Y. Zhao and Q. Zhou, *Variance-reduced Random Batch Langevin Dynamics*, arXiv:2411.01762v1 (2024-11-04), https://arxiv.org/abs/2411.01762.
