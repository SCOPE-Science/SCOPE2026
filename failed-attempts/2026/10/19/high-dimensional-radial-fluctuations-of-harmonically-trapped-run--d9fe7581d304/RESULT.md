# High-dimensional radial fluctuations of harmonically trapped run-and-tumble particles

## Finding

Consider an isotropic run-and-tumble particle in Euclidean dimension \(d\ge2\), with fixed propulsion speed \(v_0>0\), Poisson reorientation rate \(\gamma>0\), and harmonic restoring rate \(\mu>0\), without translational thermal diffusion. Let \(X^{(d)}\) be its unique stationary position. Set \(\alpha=\gamma/\mu>0\) and
\[
Q_d=\left(\frac{\mu\|X^{(d)}\|}{v_0}\right)^2.
\]
Let \(V_1,V_2,\ldots\) be independent \(\operatorname{Beta}(1,\alpha)\) variables, and set \(P_j=V_j\prod_{i<j}(1-V_i)\). These positive random weights sum to one almost surely. Put
\[
H=\sum_{j\ge1}P_j^2,\qquad K=\sum_{j\ge1}P_j^4.
\]

**Radial limit and exact error.** There is a common probability space on which \(Q_d\to H\) almost surely as \(d\to\infty\), and the mean-square error is exact in every dimension:
\[
\mathbb E[(Q_d-H)^2]=\frac{2\alpha}{d(\alpha+1)(\alpha+2)(\alpha+3)}.
\]
In particular, the high-dimensional radius does **not** converge to a deterministic shell for any fixed \(\alpha>0\). More precisely,
\[
\mathbb E Q_d=\frac1{\alpha+1},\qquad
\operatorname{Var}(Q_d)=\frac{2\alpha(d+\alpha+1)}{d(\alpha+1)^2(\alpha+2)(\alpha+3)},
\]
so the limiting variance \(2\alpha/[(\alpha+1)^2(\alpha+2)(\alpha+3)]\) is strictly positive. The limiting \(H\) is the well-known sum-of-squared-masses (Simpson concentration index) of the one-parameter Dirichlet-process stick-breaking weights. Neither its definition nor the existence of the Dirichlet process is claimed as new.

**Second-order fluctuations.** The residual randomness due to high-dimensional orientations is conditionally Gaussian. For almost every realization of the full sequence \((P_j)_{j\ge1}\),
\[
\mathcal L\left(\sqrt d\,(Q_d-H)\mid(P_j)_{j\ge1}\right)
\Longrightarrow
\mathcal N\left(0,\,2(H^2-K)\right).
\]
The variance \(2(H^2-K)\) is positive and genuinely random. Thus the unconditional second-order limit is a non-Gaussian **normal scale mixture**, not a single normal law. For the normalized radius itself, the conditional delta method gives
\[
\mathcal L\left(\sqrt d\left(\frac{\mu\|X^{(d)}\|}{v_0}-\sqrt H\right)\mid(P_j)_{j\ge1}\right)
\Longrightarrow\mathcal N\left(0,\frac{H^2-K}{2H}\right).
\]
The assertions concern \(d\to\infty\) at fixed \(\alpha>0\), \(v_0>0\), and \(\mu>0\).

## Assumptions and scope

For each integer \(d\ge2\), the position follows the ordinary differential equation between jumps
\[
\dot X_t^{(d)}=-\mu X_t^{(d)}+v_0 U_t^{(d)},
\]
where the orientation \(U_t^{(d)}\) lies on the unit sphere in \(\mathbb R^d\). At Poisson times of rate \(\gamma\), the orientation is replaced by an independent uniformly distributed spherical vector. The jump process has been running from the infinite past; the stationary stochastic convolution exists since \(\mu>0\), and it lies in the closed ball of radius \(v_0/\mu\). There is no translational Brownian forcing or interaction between particles. The dimension is changed while the ratio \(\alpha\) stays fixed.

To compare dimensions on one probability space, use the same stick-breaking weights \((P_j)\) for all \(d\). For each \(j\), take an independent infinite sequence of standard Gaussian coordinates \((G_{j,k})_{k\ge1}\), independent of the weights, and let \(U_{j,d}=(G_{j,1},\ldots,G_{j,d})/(\sum_{k=1}^dG_{j,k}^2)^{1/2}\). Then \(U_{j,d}\) are independent uniform spherical orientations for each fixed \(d\), and
\[
\frac{\mu X^{(d)}}{v_0}\stackrel{\mathcal L}=\sum_{j\ge1}P_jU_{j,d}.
\]
This is a coupling of stationary laws, not a coupling of physical trajectories across different dimensions. The common weights represent the shared renewal ages in the stationary stochastic integral, rather than independent history for each coordinate.

## Proof

**1. Stationary renewal representation.** Directly solving the stable linear equation backward from stationary time zero yields
\[
\frac{\mu X_0^{(d)}}{v_0}=\int_0^\infty\mu e^{-\mu t}U_{-t}^{(d)}\,dt.
\]
The Poisson intervals traversed backward have independent exponential lengths \(T_j\) of rate \(\gamma\). The mass of the first interval under the exponential kernel is \(V_1=1-e^{-\mu T_1}\), and successive interval masses are \(V_j\prod_{i<j}(1-V_i)\). Since \(\Pr(e^{-\mu T_j}\le x)=x^\alpha\) on \((0,1)\), \(V_j\sim\operatorname{Beta}(1,\alpha)\). Independent isotropic directions on these intervals give the asserted vector-valued stick-breaking representation; the residual mass tends to zero almost surely. This directly recovers the Dirichlet-process representation of the motivating stationary model, but does not identify it as new.

**2. Dimension-free conditional mean and exact mean-square error.** With \(W_d=\sum_jP_jU_{j,d}\), expand
\[
\|W_d\|^2=H+2\sum_{i<j}P_iP_j\langle U_{i,d},U_{j,d}\rangle.
\]
Conditional on the entire weight sequence, \(\mathbb E\langle U_{i,d},U_{j,d}\rangle=0\), \(\mathbb E\langle U_{i,d},U_{j,d}\rangle^2=1/d\), and distinct unordered pairs have zero covariance, even if they share one index. This last statement follows by conditioning on an orientation that appears in just one of the pairs. Consequently
\[
\mathbb E[Q_d\mid(P_j)]=H,\qquad
\operatorname{Var}(Q_d\mid(P_j))=\frac4d\sum_{i<j}P_i^2P_j^2
=\frac2d(H^2-K).
\]
All series are bounded in absolute value by sums of nonnegative products of masses, justifying the interchange of expectation and summation. Hence the exact finite-dimensional mean-square identity will follow from the explicit moments of \(H\) and \(K\).

**3. Stick-breaking moments.** Write \(H\overset{\mathcal L}=V^2+(1-V)^2H'\), with \(V\sim\operatorname{Beta}(1,\alpha)\) and independent \(H'\overset{\mathcal L}=H\). Similarly, \(K\overset{\mathcal L}=V^4+(1-V)^4K'\). Elementary beta integrals give
\[
\mathbb EH=\frac1{\alpha+1},\quad
\mathbb EH^2=\frac{\alpha+6}{(\alpha+1)(\alpha+2)(\alpha+3)},\quad
\mathbb EK=\frac6{(\alpha+1)(\alpha+2)(\alpha+3)}.
\]
For example \(\mathbb E[V^p(1-V)^q]=\alpha\,B(p+1,\alpha+q)\); the first and second moment recursions and the fourth-power recursion now solve algebraically. Therefore \(\mathbb E(H^2-K)=\alpha/[(\alpha+1)(\alpha+2)(\alpha+3)]\). Substitution into Step 2 proves the stated mean-square error. Total variance yields
\[
\operatorname{Var}(Q_d)=\operatorname{Var}(H)+\mathbb E[\operatorname{Var}(Q_d\mid(P_j))]
=\frac{2\alpha(d+\alpha+1)}{d(\alpha+1)^2(\alpha+2)(\alpha+3)}.
\]
In the known \(d=2\) case, this simplifies to \(\alpha/[(\alpha+1)^2(\alpha+2)]\), exactly the variance of the already-known \(\operatorname{Beta}(1,\alpha)\) law for \(Q_2\); this is an independent consistency check, not a new distributional claim.

**4. Almost-sure high-dimensional convergence.** In the common Gaussian coupling, for any distinct fixed \(i,j\), the strong law of large numbers implies \(\langle U_{i,d},U_{j,d}\rangle\to0\) almost surely. Consequently the squared norm of every fixed partial sum \(\sum_{j\le M}P_jU_{j,d}\) converges almost surely to \(\sum_{j\le M}P_j^2\). If \(T_M=\sum_{j>M}P_j\), then \(T_M\to0\) almost surely, and the norm of the discarded tail is uniformly bounded by \(T_M\) for every dimension. The error in replacing the full squared norm by the partial squared norm is bounded by \(2T_M+T_M^2\). Taking \(d\to\infty\) and then \(M\to\infty\) proves \(Q_d\to H\) almost surely. The limiting variance from Step 3 is positive for each finite positive \(\alpha\), so a deterministic-shell limit is impossible.

**5. Conditional Gaussian fluctuations.** For fixed \(M\), the multivariate central limit theorem applied to the independent coordinate arrays \((G_{i,k}G_{j,k})_{1\le i<j\le M}\), together with \(d^{-1}\sum_{k\le d}G_{i,k}^2\to1\) in probability, implies that the vector of inner products \((\sqrt d\,\langle U_{i,d},U_{j,d}\rangle)_{i<j\le M}\) converges to independent standard normal variables. Covariances of distinct products are zero by the centered Gaussian product formula. Thus the truncated fluctuation converges conditionally on the weights to a centered normal with variance \(4\sum_{i<j\le M}P_i^2P_j^2\).

The omitted pairs are controlled **at the fluctuation scale** by their exact conditional second moment:
\[
\mathbb E\left[\left.\left(2\sqrt d\sum_{i<j:\,j>M}P_iP_j\langle U_{i,d},U_{j,d}\rangle\right)^2\right|(P_j)\right]
=4\sum_{i<j:\,j>M}P_i^2P_j^2
\le4H\sum_{j>M}P_j^2\longrightarrow0.
\]
Consequently the conditional limits of characteristic functions (or bounded Lipschitz expectations) pass from finite \(M\) to the full sum, with variance \(4\sum_{i<j}P_i^2P_j^2=2(H^2-K)\). Conditional convergence holds for almost every positive stick sequence and implies a joint, stable form of convergence together with the weights. Since \(H>0\) almost surely, the conditional delta method yields the stated radial (rather than squared-radial) limit.

The mixing variance is strictly positive since every pair of distinct positive weights contributes. It is not almost surely constant: the event that the first stick takes almost all the mass makes it arbitrarily small, while an event where the first two sticks each retain a substantial fraction gives it a fixed positive lower bound. Both events have positive probability. A nonconstant normal variance mixture is not a single Gaussian, as follows for instance from strict convexity of its Laplace transform.

## Verification

The companion `check.py` uses only the Python standard library. Run `python check.py` to verify exact rational identities for multiple half-integer and integer rate ratios, the independent known two-dimensional beta-law variance, and seeded simulations of the stationary spherical stick representation in dimensions \(2\), \(8\), and \(32\). It reports **73 passed assertions**. The simulations compare the exact finite-dimensional mean, variance, and mean-square coupling error against empirical values; they do not establish any infinite-dimensional convergence statement. The proof in Steps 1–5 supplies the infinite-dimensional justification.

## Relationship to prior work

Guéneau, Majumdar, and Schehr (2026, arXiv:2602.08436v1) establish the generalized trapped run-and-tumble model, its Dirichlet-process stationary position representation, exact one-coordinate moments in arbitrary dimension, explicit radial laws for dimensions \(1\), \(2\), and \(3\), and radial moment relations for all dimensions. Their exact finite-dimensional moment results imply many moment identities used here and are not presented as new. They do not state the conditional high-dimensional mixed-Gaussian fluctuation law or identify the limiting radial history index in the inspected text.

Sethuraman (1994) establishes the standard beta stick-breaking construction of Dirichlet random measures. Cifarelli and Regazzini (1990) study distributions of their means, while the squared-weight Simpson concentration index is a pre-existing statistical object. Stam (1982) treats asymptotic Gaussian laws for finitely many high-dimensional spherical inner products; the present infinite, random-weighted conditional fluctuation limit additionally requires a uniform squared-weight tail argument. The new assessed mathematical-physics statement is the **stationary physical radius's dimension-asymptotic law, especially its conditional second-order Gaussian-mixture fluctuations around the random history index**, not any standalone invention of those probability-theoretic ingredients.

## Limitations

The high-dimensional limit keeps the tumble-to-trap ratio fixed. It does not establish a joint scaling where \(\gamma/\mu\) grows with dimension. Thermal Brownian forcing is absent; any fixed nonzero translational diffusivity changes the leading order of the squared radius in high dimension. The conditional Gaussian limit concerns angular fluctuations after the renewal weights have been fixed, not the total radial fluctuations around the deterministic mean. The stationary source formula and beta stick-breaking law are inherited from prior work. General random barycenter central limit principles may encompass aspects of the conditional fluctuation mechanism; this possibility is a residual originality risk and warrants independent literature assessment.

## References

1. M. Guéneau, S. N. Majumdar, and G. Schehr, *Exact Stationary State of a d-dimensional Run-and-Tumble Particle in a Harmonic Potential*, arXiv:2602.08436v1 (first posted 2026-02-09); published in *Physical Review E* **114**, 014144 (2026), DOI:10.1103/mlkm-vgbd. The v1 full text was used, particularly Eqs. (2)–(5), (19), (43), and (A20)–(A22).
2. J. Sethuraman, *A Constructive Definition of Dirichlet Priors*, *Statistica Sinica* **4** (1994), 639–650.
3. D. M. Cifarelli and E. Regazzini, *Distribution Functions of Means of a Dirichlet Process*, *Annals of Statistics* **18** (1990), 429–442, DOI:10.1214/aos/1176347509.
4. A. J. Stam, *Limit theorems for uniform distributions on spheres in high-dimensional Euclidean spaces*, *Journal of Applied Probability* **19** (1982), 221–228, DOI:10.2307/3213932.
