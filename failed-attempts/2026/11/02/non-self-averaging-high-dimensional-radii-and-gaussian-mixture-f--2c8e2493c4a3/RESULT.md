# Non-self-averaging high-dimensional radii and Gaussian-mixture fluctuations of harmonically trapped run-and-tumble particles

## Finding

Fix a tumbling-to-trap ratio \(\alpha=\gamma/\mu>0\). For each integer \(d\ge2\), consider the stationary athermal isotropic run-and-tumble process in \(\mathbb R^d\)
\[
\dot X_d(t)=-\mu X_d(t)+v_0 U_d(t),
\]
where \(\mu,v_0,\gamma>0\), the orientation stays fixed between rate-\(\gamma\) Poisson tumbles, and every tumble redraws it independently uniformly from \(S^{d-1}\). Write \(Q_d=(\mu\lVert X_d\rVert/v_0)^2\).

Let \(V_j\) be independent \(\mathrm{Beta}(1,\alpha)\) variables and set \(P_j=V_j\prod_{i<j}(1-V_i)\). Define the random concentration statistics
\[
S=\sum_{j\ge1}P_j^2,\qquad H_4=\sum_{j\ge1}P_j^4.
\]
Coupling all dimensions to these same weights gives the following joint large-dimension theorem:

1. The squared stationary radius converges to the *nonconstant* Poisson--Dirichlet homozygosity variable: \(Q_d\to S\) in \(L^2\), with the exact finite-dimensional error
\[
\mathbb E (Q_d-S)^2=\frac{2\alpha}{d(\alpha+1)(\alpha+2)(\alpha+3)}.
\]
Consequently the actual normalized radius converges in distribution to \(\sqrt S\), rather than to a fixed shell.

2. Conditionally on the entire stick-breaking sequence \(P=(P_j)_{j\ge1}\), there is a central limit theorem
\[
\sqrt d\,(Q_d-S)\ \Longrightarrow\ \mathcal N\bigl(0,\,2(S^2-H_4)\bigr).
\]
This conditional convergence also gives joint (stable with respect to the weights) convergence, and the unconditional limit is a nontrivial centered Gaussian *scale mixture*, not a single Gaussian. An explicit representation is \(2\sum_{i<j}P_iP_j Z_{ij}\), where the \(Z_{ij}\) are independent standard normals, independent of the weights.

3. The limiting near-turning-surface probability has the sharp amplitude, for \(\varepsilon\downarrow0\),
\[
\Pr\{S>1-\varepsilon\}\sim 2^{-\alpha}\varepsilon^\alpha,
\qquad
\Pr\{\sqrt S>1-\varepsilon\}\sim\varepsilon^\alpha.
\]
All limits in this theorem take \(d\to\infty\) at fixed \(\alpha\), before any edge limit \(\varepsilon\downarrow0\).

In particular,
\[
\mathbb ES=\frac1{\alpha+1},\qquad
\operatorname{Var}(S)=\frac{2\alpha}{(\alpha+1)^2(\alpha+2)(\alpha+3)}>0,
\]
and the exact finite-dimensional variance is
\[
\operatorname{Var}(Q_d)=\operatorname{Var}(S)\left(1+\frac{\alpha+1}{d}\right).
\]

## Assumptions and scope

The environment is a single athermal particle with complete isotropic orientation refresh at each Poisson tumble; the restoring force is linear and isotropic. Position is observed in its unique stationary state. There is no translational thermal diffusion and no orientation drift or rotational-diffusion interpolation. Dimensions \(d\) vary while \(\alpha>0\) remains fixed. All expectations are with respect to both the Poisson tumbling history and independent orientation draws. Conditional assertions always condition on the complete infinite sequence of random weights.

The same weights can be used in all dimensions although sphere directions differ with dimension. The convergence assertion is thus a valid explicit coupling, with the one-dimensional marginals equal to the actual stationary radius distributions. Statements about \(\Pr\{\sqrt S>1-\varepsilon\}\) concern the limiting random radius and do not assert any uniform-in-d edge asymptotic.

## Proof

**1. Stationary stick-breaking representation.** Integrate the dissipative linear equation backwards from stationarity:
\[
\frac{\mu X_d}{v_0}=\int_0^\infty\mu e^{-\mu t}U_d(-t)\,dt.
\]
The backward run lengths are independent \(\mathrm{Exp}(\gamma)\) by Poisson stationarity. Partitioning the integral at the tumble times yields the weights \(P_j=V_j\prod_{i<j}(1-V_i)\), with \(V_j=1-e^{-\mu T_j}\sim\mathrm{Beta}(1,\alpha)\), and independent uniform sphere directions \(U_{j,d}\). Hence
\[
\frac{\mu X_d}{v_0}\overset{\mathrm{law}}=\sum_{j\ge1}P_jU_{j,d},\qquad\sum_{j\ge1}P_j=1\quad\text{a.s.}
\]
The series converges absolutely. This stationary Dirichlet/stick-breaking representation is *previously known*; see Guéneau--Majumdar--Schehr (2026), Section III and its dimension-reduction discussion. It is the starting point, not a newly claimed identity.

**2. Angular orthogonality and sharp mean-square error.** Set \(C_{ij,d}=U_{i,d}\cdot U_{j,d}\). Then
\[
Q_d=S+2\sum_{i<j}P_iP_j C_{ij,d}.
\]
For distinct unordered pairs, the \(C_{ij,d}\) are conditionally uncorrelated and centered, including when two pairs share one index. Independence and rotational invariance give \(\mathbb E[C_{ij,d}^2]=1/d\). Consequently, *without any limiting approximation*,
\[
\mathbb E[(Q_d-S)^2\mid P]=\frac{4}{d}\sum_{i<j}P_i^2P_j^2
=\frac{2}{d}(S^2-H_4).
\]

**3. Moments of the concentration index.** Splitting off the first stick gives \(S\overset{\rm law}=V^2+(1-V)^2S'\), with \(V\sim\mathrm{Beta}(1,\alpha)\) independent of \(S'\overset{\rm law}=S\). The beta moment identity \(\mathbb E[V^k(1-V)^l]=\alpha B(k+1,\alpha+l)\) gives
\[
\mathbb ES=\frac1{\alpha+1},\qquad
\mathbb ES^2=\frac{\alpha+6}{(\alpha+1)(\alpha+2)(\alpha+3)}.
\]
The same recursion for \(H_4\) gives
\[
\mathbb EH_4=\frac6{(\alpha+1)(\alpha+2)(\alpha+3)},\quad
\mathbb E(S^2-H_4)=\frac\alpha{(\alpha+1)(\alpha+2)(\alpha+3)}.
\]
Together with Step 2 these prove the claimed exact error, \(L^2\) limit and both variance formulas. The positive limiting variance proves failure of shell self-averaging.

**4. Conditional Gaussian-mixture fluctuations.** For fixed \(m\), construct each of \(U_{1,d},\ldots,U_{m,d}\) by normalizing independent standard Gaussian vectors in \(\mathbb R^d\). The multivariate central limit theorem applied to their coordinate products, followed by the law of large numbers for their squared norms, yields
\[
(\sqrt d\, C_{ij,d}:1\le i<j\le m)
\Longrightarrow (Z_{ij}:1\le i<j\le m),
\]
with *independent* standard-normal limits: cross-covariances of different coordinate-product pairs vanish, and the joint limit is Gaussian. For the contribution of indices beyond \(m\), conditional uncorrelatedness bounds its scaled second moment uniformly in \(d\) by
\[
4\sum_{i<j:\,j>m}P_i^2P_j^2\longrightarrow0.
\]
Thus the fixed-\(m\) Gaussian limit passes to the absolutely \(L^2\)-convergent infinite Gaussian series \(2\sum_{i<j}P_iP_jZ_{ij}\). This proves the conditional characteristic-function limit for almost every weight sequence; bounded convergence then yields the stated joint/stable and unconditional conclusions. The conditional variance is \(2(S^2-H_4)\), nonconstant since the weights vary nondegenerately.

**5. Sharp limiting turning-surface tail.** Let \(M=\max_jP_j\). The size-biased intensity of the GEM weights is
\[
\mathbb E\sum_j\delta_{P_j}(dp)=\alpha p^{-1}(1-p)^{\alpha-1}\,dp.
\]
This identity follows independently by considering the probability measure \(p\,\mathbb E\sum_j\delta_{P_j}(dp)\): its moments, computed by geometric stick recursion, equal those of \(\mathrm{Beta}(1,\alpha)\); uniqueness of moments on \([0,1]\) identifies the measure. For \(0<\delta<1/2\), at most one weight exceeds \(1-\delta\), so
\[
\Pr(M>1-\delta)=\alpha\int_{1-\delta}^1p^{-1}(1-p)^{\alpha-1}\,dp
\sim\delta^\alpha.
\]
If \(S>1-\varepsilon\) and \(0<\varepsilon<1/2\), then \(M\ge S>1-\varepsilon\); setting \(\eta=1-M\), one also has \(S\le M^2+(1-M)^2\), so \(2\eta(1-\eta)<\varepsilon\). Conversely, \(M>1-\varepsilon/2\) implies \(S\ge M^2>1-\varepsilon\). Therefore
\[
\Pr(M>1-\varepsilon/2)
\le\Pr(S>1-\varepsilon)
\le\Pr\left(M>1-\frac{1-\sqrt{1-2\varepsilon}}2\right).
\]
Both outer probabilities are asymptotic to \((\varepsilon/2)^\alpha\), proving the first edge law. Replace \(\varepsilon\) by \(1-(1-\delta)^2\sim2\delta\) to obtain the second.

**6. Independent stationarity cross-check.** Directly apply the stationary Markov generator in rescaled time to \(Q=\lVert\mu X/v_0\rVert^2\), \(H=(\mu X/v_0)\cdot U\), and their products. The moment equations yield \(\mathbb EQ=1/(\alpha+1)\), \(\mathbb EH^2=(2+\alpha/d)/[(\alpha+1)(\alpha+2)]\), and
\[
\mathbb EQ^2=\frac{\alpha+6+2\alpha/d}{(\alpha+1)(\alpha+2)(\alpha+3)},
\]
in exact agreement with Steps 2--3. This derivation checks the normalizations separately from stick-breaking algebra.

## Verification

Run `python3 verify.py` with the Python standard library. It performs exact-rational comparisons between the GEM recursion and independent stationary generator calculations, verifies the two-dimensional beta-law special case, checks the endpoint-event squeeze, and samples genuine independent isotropic orientations at several dimensions. It also checks the fixed-weight Gaussian-fluctuation variance numerically. On the prepared package it reports `PASS: 260 finite exact/numeric assertions`.

The code is finite supporting evidence. The infinite series, all-d exact formula, conditional limit theorem, and edge coefficient are justified analytically in Steps 1--5, not by Monte Carlo, truncation or the assertions alone.

## Relationship to prior work

Guéneau, Majumdar and Schehr (2026) obtained the stationary Dirichlet-process/stick-breaking description for the trapped isotropic particle and all-dimensional coordinate/radial moment formulas. Their \(d=2\) radial beta law and explicit \(d=3\) density, and their stationary representation, remain prior work. The present theorem does not claim to rediscover these formulas or the Dirichlet process; the evaluated new result is the fixed-activity \(d\to\infty\) *random radial limit*, its exact conditional Gaussian-mixture correction, and the associated high-dimensional edge law and amplitude. The exact finite-dimensional variance follows already from the earlier all-dimensional moments; it is displayed as a normalization check rather than separately claimed novelty.

The GEM distribution and homozygosity statistic are classical in Poisson--Dirichlet theory; Feng and Gao (2008) study parameter-asymptotics of that statistic, unlike the fixed-parameter ambient-dimension limit here. Classical high-dimensional spherical inner-product Gaussian limits (for example Stam, 1982) supply a standard finite-dimensional ingredient, not the full random-weighted infinite series or its stochastic-physics interpretation. The limiting right-tail formula follows from the classical GEM intensity identity but is expressed here as a precise prediction for the high-dimensional trapped-particle radius.

## Limitations

No theorem is asserted for fixed nonzero translational thermal diffusivity, interacting particles, anisotropic force, biased orientation redraws, persistent rotational diffusion, simultaneous \(\alpha\)-and-\(d\) scaling or a finite-\(d\) uniform edge limit. The limiting Gaussian mixture is conditional on the entire latent Poisson history; it need not have an elementary closed density. The exact location of any high-dimensional interior radial mode is not determined. The priority comparison is best-knowledge rather than a guarantee against earlier implicit corollaries of general Dirichlet-process or spherical-array theorems; no independent validation is claimed.

## References

1. M. Guéneau, S. N. Majumdar and G. Schehr, *Exact stationary state of a \(d\)-dimensional run-and-tumble particle in a harmonic potential*, Physical Review E **114**, 014144 (2026). First public preprint February 9, 2026, arXiv:2602.08436. DOI: https://doi.org/10.1103/mlkm-vgbd. Relevant material: Sections II--IV, especially the stick-breaking representation in Section III, and Appendix A.
2. S. Feng and F. Gao, *Moderate deviations for Poisson--Dirichlet distribution*, Annals of Applied Probability **18** (2008), 1794--1824. arXiv:0710.3419, https://arxiv.org/pdf/0710.3419. Relevant material: Section 1 (GEM weights, homozygosity) and Section 3 (previous parameter-limit fluctuation theorems).
3. A. J. Stam, *Limit theorems for uniform distributions on spheres in high-dimensional Euclidean spaces*, Journal of Applied Probability **19** (1982), 221--228. DOI: https://doi.org/10.2307/3213932. The elementary Gaussian normalization/CLT argument needed here is supplied explicitly in the proof.
