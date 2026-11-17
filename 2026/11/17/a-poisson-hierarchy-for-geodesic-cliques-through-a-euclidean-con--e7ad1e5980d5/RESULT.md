# A Poisson hierarchy for geodesic cliques through a Euclidean cone apex

## Finding

Let a complete two-dimensional Euclidean metric cone have total angle \(\theta\ge 2\pi\). Sample \(n\) independent points with independent uniform azimuths on \([0,\theta)\); each point has positive radius almost surely, and its radius may have any conditional distribution given its azimuth. Join two sample points when their unique minimizing intrinsic geodesic passes through the cone apex. For an integer \(k\ge3\), let \(T_{n,k}\) count unordered \(k\)-vertex cliques in this apex-passage graph.

**Exact feasible-clique law.** There are no \(k\)-cliques for \(\theta\le k\pi\), almost surely. For \(\theta>k\pi\),
\[
\Pr(\text{a fixed }k\text{-subset is a clique})
=\left(\frac{\theta-k\pi}{\theta}\right)^{k-1},\qquad
\mathbb E T_{n,k}=\binom nk\left(\frac{\theta-k\pi}{\theta}\right)^{k-1}.
\]
If the \(k\) selected azimuths are traversed cyclically, beginning at a *specified labeled sampled vertex*, their successive gaps \(G_1,\ldots,G_k\), conditional on the clique event, obey
\[
(G_1,\ldots,G_k)\overset{\mathrm d}{=}(\pi,\ldots,\pi)+(\theta-k\pi)(V_1,\ldots,V_k),\quad
(V_1,\ldots,V_k)\sim\operatorname{Dirichlet}(1,\ldots,1).
\]
The specified labeled anchor is important: starting instead at the smallest numerical azimuth introduces a seam-related bias in the first gap.

**Sharp random appearance window.** Fix \(k\ge3\), \(c\ge0\), and set \(\theta_n=k\pi+c n^{-k/(k-1)}\). Then
\[
T_{n,k}\xrightarrow{\mathrm{TV}}\operatorname{Poisson}\left(
\frac{c^{k-1}}{k!(k\pi)^{k-1}}\right).
\]
For \(c>0\), the total-variation error is \(O_{k,c}(n^{-1/(k-1)})\). More generally, if \(\theta_n=k\pi+\delta_n\), where \(\delta_n>0\) and \(\delta_n\to0\), then the probability of at least one clique tends to zero when \(n^k\delta_n^{k-1}\to0\), and tends to one when \(n^k\delta_n^{k-1}\to\infty\).

**An exact finite-size consequence.** If \(k=3\), \(3\pi<\theta<4\pi\), and \(\delta=\theta-3\pi\), put \(p=(\delta/\theta)^2\) and \(q=2\delta^3/(3\theta^3)\). Then
\[
\operatorname{Var}(T_{n,3})=\binom n3p(1-p)
+2\binom n2\binom{n-2}2(q-p^2).
\]
These laws depend on azimuth but are completely independent of the radii and of their conditional distributions.

## Assumptions and scope

The intrinsic Euclidean cone is the metric completion of the warped polar space with line element \(ds^2=dr^2+r^2d\varphi^2\), with \(r>0\) and azimuth \(\varphi\in\mathbb R/\theta\mathbb Z\). No embedding of this wide cone in ordinary three-dimensional space is assumed. The cone has nonpositive Alexandrov curvature for \(\theta\ge2\pi\), so the minimizing geodesic between any two points is unique. The independent sample points have uniform azimuth marginals and no mass at the tip. Their radii need not be uniformly distributed, need not be identically distributed, and may depend on azimuth. Each azimuth is independent of the others. The count uses every unordered subset of exactly \(k\) distinct sampled vertices; equal azimuths and threshold-angle equalities have probability zero. The asymptotic assertions hold for each fixed integer \(k\), not uniformly as \(k\to\infty\).

## Proof

**1. Apex-passage criterion.** For two nonapex points, let \(r,s>0\) be their radial coordinates and let \(\Delta\in[0,\theta/2]\) be their shorter angular separation. The intrinsic metric-cone distance formula is
\[
d^2=r^2+s^2-2rs\cos(\min\{\Delta,\pi\}).
\]
When \(\Delta<\pi\), unfolding along that angular interval gives a straight chord of length strictly less than \(r+s\). When \(\Delta>\pi\), any avoiding-apex locally straight path would have to sweep more than a half-turn about the origin, impossible for a Euclidean straight segment; the radial route through the apex is minimizing. Equivalently, the distance formula and uniqueness of geodesics give the same criterion. Therefore an edge is present precisely when both circular arcs between the two azimuths have length at least \(\pi\), apart from null equality cases.

**2. Clique equivalence and simplex volume.** For a \(k\)-subset, arrange its azimuths in circular order. It is a clique if and only if every successive circular gap is at least \(\pi\). Necessity follows by applying the pair criterion to each consecutive pair; sufficiency follows since the two arcs joining any pair are sums of at least one of these gaps. Choose one vertex by its label as angular origin; the other \(k-1\) independent azimuths relative to this origin are uniform on \([0,\theta)\). After ordering, the \(k\) circular gaps are uniform on the simplex of positive gaps summing to \(\theta\), with density \((k-1)!/\theta^{k-1}\) relative to \(k-1\) gap coordinates. The translated simplex with all gaps at least \(\pi\) has linear size \(\delta=\theta-k\pi\), hence probability \((\delta/\theta)^{k-1}\) when \(\delta>0\), and probability zero otherwise. Conditioning on this translated simplex, normalizing by \(\delta\), proves the exact Dirichlet law.

**3. The Poisson approximation.** In the positive critical window let \(\delta_n=c n^{-k/(k-1)}\) with \(c>0\). Write \(I_S\) for the indicator that a \(k\)-subset \(S\) is a clique. Its success probability is \(p_n=(\delta_n/\theta_n)^{k-1}\), and \(\lambda_n=\binom nk p_n\to c^{k-1}/[k!(k\pi)^{k-1}]\). The family \(\{I_S\}\) is dissociated: events indexed by disjoint subsets are independent. In a dependency-graph Chen–Stein bound, the first error term is
\[
b_1\le C_k n^{2k-1}p_n^2=O_{k,c}(n^{-1}).
\]
For distinct \(k\)-subsets \(S,T\) overlapping in \(s\in\{1,\ldots,k-1\}\) vertices, fix one of their common vertices as azimuthal origin. If both clique events occur, all of the other \(2k-s-1\) *distinct* vertices must lie inside the union of the \(k-1\) intervals of length \(\delta_n\) immediately following the angles \(\pi,2\pi,\ldots,(k-1)\pi\). Indeed, in either clique the \(j\)-th vertex encountered after the anchor lies between \(j\pi\) and \(j\pi+\delta_n\). Uniformity and independence of the other azimuths yield
\[
\Pr(I_S=I_T=1)
\le \left(\frac{(k-1)\delta_n}{\theta_n}\right)^{2k-s-1}.
\]
There are at most \(C_k n^{2k-s}\) such ordered overlapping pairs, so
\[
b_2\le C_k\sum_{s=1}^{k-1}n^{2k-s}\delta_n^{2k-s-1}
=O_{k,c}(n^{-1/(k-1)}).
\]
The dependency-graph Poisson bound consequently gives \(d_{\mathrm{TV}}(\mathcal L(T_{n,k}),\operatorname{Poisson}(\lambda_n))=O_{k,c}(n^{-1/(k-1)})\). Since \(\lambda_n\) approaches its limit at rate \(O_{k,c}(n^{-1})\), the claimed total-variation law and rate follow. If \(c=0\), the clique count is identically zero.

**4. Sharpness of the window.** If \(n^k\delta_n^{k-1}\to0\), the expectation tends to zero, so Markov's inequality rules out any clique. If it tends to infinity, the same overlap estimate gives
\[
\frac{\operatorname{Var}T_{n,k}}{(\mathbb E T_{n,k})^2}
\le \frac1{\mathbb E T_{n,k}}+C_k\sum_{s=1}^{k-1}\frac1{n^s\delta_n^{s-1}}.
\]
Writing \(\delta_n=n^{-k/(k-1)}a_n\) with \(a_n\to\infty\), each summand is bounded by \(n^{(s-k)/(k-1)}a_n^{-(s-1)}\), which tends to zero. Chebyshev's inequality proves existence with probability tending to one.

**5. Exact three-clique variance.** Fix a pair of labeled azimuths at \(0,d\). For \(0<\delta<\pi\), the circular angular span available for a third point completing an apex triple has length \(\delta-(d-\pi)\) when \(\pi<d<\pi+\delta\), length \(d-2\pi\) when \(2\pi<d<2\pi+\delta\), and zero otherwise. Given the shared pair, two independent further points complete two triples with the square of this length divided by \(\theta^2\). Integrating the shared pair's uniform angular difference gives
\[
q=\frac{1}{\theta^3}\left[\int_0^\delta(\delta-t)^2dt+\int_0^\delta t^2dt\right]=\frac{2\delta^3}{3\theta^3}.
\]
Two different triples sharing one vertex are independent conditional on that vertex, because the conditional success probability is rotation-invariant; disjoint triples are independent unconditionally. There are \(\binom n2\binom{n-2}2\) unordered pairs of triple indicators sharing two vertices. Expanding the variance proves its exact formula. This last formula is not claimed for \(\theta\ge4\pi\).

## Verification

The standalone standard-library Python file `cone_apex_cliques_check.py` is run using `python3 cone_apex_cliques_check.py`. It directly enumerates the clique condition, independently counts sparse candidate subsets, checks exact fixed-subset probabilities for three clique orders, verifies the conditional Dirichlet first and second moments using a **labeled** angular anchor, checks the exact shared-pair overlap integral, compares the finite triple-count variance with independent simulation, and samples two critical windows. The checker reports `CONE_APEX_CLIQUE_CHECKS_OK`. The finite experiments corroborate but do not prove the asymptotic result; the proof is the simplex computation and dependency bounds above.

## Relationship to prior work

Charitos, Papadoperakis and Tsapogas (arXiv:1306.1759, first public 7 June 2013) analyze geodesics on Euclidean cone surfaces, including arbitrary cone angles and singularity passage; their paper establishes a geometric setting, but does not calculate random apex-passage clique counts. A publicly available analysis of mean-square distances on conical disks records the two-point apex event and its sharp transition at \(2\pi\); the present law concerns *simultaneous* apex-passing geodesics among every pair of a \(k\)-set and the hierarchy of thresholds \(k\pi\). The published escape-chain graph in spherical reflex sectors concerns minimizing great-circle arcs leaving a region, not apex-passage on a cone.

Arratia, Goldstein and Gordon (1989) supply the general dependency-graph Poisson approximation tool. Nikitin and Simarova (arXiv:2010.04460, first public 9 October 2020) discuss general circle-based \(U\)-maxima, including smooth, nondegenerate-Hessian extremizers and generic Poisson criteria. Their smooth-extremizer theorem does not directly apply to the nonsmooth minimum-circular-gap kernel; their general Poisson methodology is used rather than claimed as novel. Roos's work on extreme consecutive \(m\)-spacings of all sample points concerns a different statistic than unordered \(k\)-subsets with nearly equal angular gaps. The explicit cone-geodesic equivalence, all-\(k\) threshold and marked simplex law, and the individual constants and overlap control are the substantive assertions here; standard probabilistic machinery is not a novelty claim. Historical priority remains subject to independent scrutiny.

## Limitations

The cone must be a complete intrinsic nonpositively curved Euclidean cone with total angle at least \(2\pi\), not an arbitrary embedded cone or a general singular surface. The angular marginal must be uniform and independent across observations; arbitrary radial sampling is permitted. Each clique order \(k\) is fixed as sample size grows. Constants and rates need not hold for nonuniform azimuths. The finite triple-count variance formula is restricted to \(3\pi<\theta<4\pi\). There is no claim of independent mathematical certification, comprehensive historical priority, or uniformity of the Poisson error when \(k\) grows with \(n\).

## References

- C. Charitos, I. Papadoperakis and G. Tsapogas, *The geometry of Euclidean surfaces with conical singularities*, arXiv:1306.1759v1, submitted 7 June 2013, https://arxiv.org/abs/1306.1759 .
- R. Arratia, L. Goldstein and L. Gordon, *Two moments suffice for Poisson approximations: the Chen–Stein method*, Annals of Probability 17 (1989), 9–25, DOI:10.1214/aop/1176991491 .
- Ya. Yu. Nikitin and E. N. Simarova, *Generalized limit theorems for U-max statistics*, arXiv:2010.04460v1, submitted 9 October 2020, https://arxiv.org/abs/2010.04460 .
- M. Roos, *Compound Poisson approximations for the numbers of extreme spacings*, Advances in Applied Probability 25 (1993), 847–874, https://www.cambridge.org/core/journals/advances-in-applied-probability/article/abs/compound-poisson-approximations-for-the-numbers-of-extreme-spacings/F81FA907FAF63B4B9F8ADA227CE56146 .
