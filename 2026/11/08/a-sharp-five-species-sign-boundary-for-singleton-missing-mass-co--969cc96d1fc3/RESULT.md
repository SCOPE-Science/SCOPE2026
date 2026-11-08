# A sharp five-species sign boundary for singleton–missing-mass covariance

## Finding

Let \(m\geq 1\) species have strictly positive abundances \(p_1,\ldots,p_m\), with \(\sum_i p_i=1\). Draw \(n\geq 1\) individuals independently with replacement. Write \(N_i\) for the number of observations of species \(i\), \(S_n=\sum_i\mathbf1\{N_i=1\}\) for the number of singleton species, and \(M_n=\sum_i p_i\mathbf1\{N_i=0\}\) for the true missing probability mass. Thus \(S_n/n\) is the ordinary Good–Turing singleton estimate of missing mass, while \(M_n\) is the (random) next-observation discovery probability conditional on the sample.

**Theorem.** For exactly two observations, \(\operatorname{Cov}(S_2,M_2)<0\) for every strictly positive abundance vector with \(2\leq m\leq4\). With one species the covariance is zero. Five species are necessary and sufficient for strictly positive covariance: the five-species abundance profile \((4/5,1/20,1/20,1/20,1/20)\) gives \(\operatorname{Cov}(S_2,M_2)=1/800>0\). For every \(m\geq5\) there is a strictly positive \(m\)-species profile with positive covariance at two draws. More generally, for each fixed integer \(n\geq2\) there are finite strictly positive species profiles attaining either covariance sign. For one common species of mass \(a\in(0,1)\) and \(L\) equally rare species of mass \((1-a)/L\), the limit as \(L\to\infty\) is

\[
\lim_{L\to\infty}\operatorname{Cov}(S_n,M_n)
=n a^2(1-a)^n\big[1-(1-a)^{n-1}\big]>0.
\]

This last statement gives existence for finite, sufficiently large \(L\), not an asserted sharp species cutoff for \(n>2\). Under independent Poissonized species counts with intensity \(t p_i\), in contrast, the same unnormalized singleton count and missing mass always have negative covariance \(-t\sum_i p_i^2e^{-2tp_i}\); this elementary Poissonized identity is contextual and is **not** claimed novel.

## Assumptions and scope

All species abundances are fixed and strictly positive; the number of species is finite and the observations are independent identically distributed with replacement. All covariance statements refer to repeated sampling from one fixed abundance profile, not to variation across communities, not to an estimated abundance distribution, and not to sampling without replacement. The two-draw sharp lower bound is over *all* strictly positive profiles of a fixed support size, not merely symmetric profiles. The main result concerns the raw Good–Turing singleton count; dividing by the fixed positive sample size preserves its covariance sign.

## Proof

**1. Joint moments for arbitrary sample size.** The elementary multinomial indicator identities give

\[
\begin{aligned}
\mathbb E[M_n]&=\sum_i p_i(1-p_i)^n,\\
\mathbb E[S_n]&=n\sum_j p_j(1-p_j)^{n-1},\\
\mathbb E[M_nS_n]&=n\sum_{i\ne j}p_ip_j(1-p_i-p_j)^{n-1}.
\end{aligned}
\]

The diagonal terms in the third equality vanish because a species cannot simultaneously be unseen and a singleton. The remaining terms follow by fixing the singleton's one observation and requiring all other draws to avoid both species. These equations are exact for every integer \(n\geq2\); no Poisson or large-sample approximation is used.

**2. The two-draw sign polynomial.** Put \(Q=\sum_i p_i^2\) and \(R=\sum_i p_i^3\). With \(n=2\), the preceding identities reduce to

\[
\mathbb E[S_2]=2(1-Q),\quad
\mathbb E[M_2]=1-2Q+R,\quad
\mathbb E[M_2S_2]=2(1-3Q+2R),
\]

and consequently

\[
\operatorname{Cov}(S_2,M_2)
=2\big[(1+Q)R-2Q^2\big].
\]

**3. An all-profile nonnegativity certificate for four species.** For \(m\leq4\), append zero coordinates until there are exactly four entries, denoted \(x_1,\ldots,x_4\). Define \(P=\sum_i x_i\), \(Q=\sum_i x_i^2\), and \(R=\sum_i x_i^3\). The following homogeneous polynomial identity holds identically for arbitrary real \(x_i\):

\[
\begin{aligned}
2P Q^2-(P^2+Q)R
={}&\sum_{i=1}^{4}x_i^3
\sum_{\substack{j<k\\j,k\ne i}}(x_j-x_k)^2\\
&+4\sum_{i<j}x_i^2x_j^2\sum_{k\ne i,j}x_k.
\end{aligned}
\]

This follows by expanding both sides (the standalone checker independently compares every integer monomial coefficient). As all \(x_i\geq0\), the right-hand side is nonnegative. For any probability vector \(P=1\), the left-hand side equals \(2Q^2-(1+Q)R=-\operatorname{Cov}(S_2,M_2)/2\). If at least two entries are positive, the right-hand side is strictly positive: with exactly two positive entries, the first sum is positive; with three or four positive entries, the second sum is positive. The case of one species is deterministic. This proves the universal negative sign for support sizes two, three, and four.

**4. Sharp witness and larger supports.** At the five-species profile \(p=(4/5,1/20,1/20,1/20,1/20)\), direct rational arithmetic gives

\[
Q=13/20,\quad R=41/80,\quad
(\mathbb E[M_2],\mathbb E[S_2],\mathbb E[M_2S_2])=(17/80,7/10,3/20),
\]

hence \(\operatorname{Cov}(S_2,M_2)=1/800\). For any fixed \(m>5\), scale these five masses by \(1-\varepsilon\) and give each of the remaining \(m-5\) species mass \(\varepsilon/(m-5)\). Continuity of the exact covariance polynomial at \(\varepsilon=0\) preserves strict positivity for all sufficiently small \(\varepsilon>0\), giving fully positive abundance vectors of every larger support size.

**5. Both signs at every fixed sampling depth.** A two-species vector \((1/2,1/2)\) has \(\operatorname{Cov}(S_n,M_n)<0\) for every \(n\geq2\). Indeed, \(M_n>0\) only if all observations are the same species, whereas \(S_n>0\) requires the appearance of both species (for \(n=2\)) or at least one singleton (for \(n>2\)), in either case forcing \(M_n=0\). Both expectations are strictly positive, so \(\mathbb E[S_nM_n]=0\) and the covariance is strictly negative.

For positivity, take \(p_0=a\in(0,1)\), and \(L\) other species each of abundance \((1-a)/L\). If \(K\) is the count of the common species, then \(K\sim\operatorname{Bin}(n,a)\). As \(L\to\infty\) with \(n\) fixed, the chance of a collision among rare observations is at most \(\binom n2(1-a)^2/L\), while the total rare mass observed is at most \(n(1-a)/L\); both tend to zero. Since both observables are bounded for fixed \(n\), their joint moments converge to those of

\[
S_\infty=n-K+\mathbf1\{K=1\},\qquad
M_\infty=1-a+a\mathbf1\{K=0\}.
\]

Now \(\Pr(K=0)=(1-a)^n\), \(\Pr(K=1)=na(1-a)^{n-1}\), and \(\mathbb E[S_\infty]=n(1-a)+na(1-a)^{n-1}\). Therefore

\[
\operatorname{Cov}(S_\infty,M_\infty)
=a\Pr(K=0)\big(n-\mathbb E[S_\infty]\big)
=na^2(1-a)^n\big[1-(1-a)^{n-1}\big]>0.
\]

Joint-moment convergence implies strict positivity for sufficiently large *finite* \(L\). This completes the theorem.

**6. Poissonized contrast.** If the sample count is Poisson with mean \(t>0\), each species count is independent with law \(\operatorname{Poisson}(tp_i)\). The corresponding single-species indicators \(\mathbf1\{N_i=1\}\) and \(p_i\mathbf1\{N_i=0\}\) are mutually exclusive. Independent species contributions give

\[
\operatorname{Cov}(S(t),M(t))
=-t\sum_i p_i^2 e^{-2tp_i}<0.
\]

This follows directly from the classical independent-Poisson occupancy representation and is not asserted as a separate new contribution; it highlights why Poissonization cannot be substituted for fixed-size sampling when analyzing the new sign boundary.

## Verification

Run `python checker.py` using Python's standard library. It verifies the four-variable nonnegativity identity coefficient by coefficient; independently enumerates all sampling outcomes for many exact rational probability profiles and sample sizes through five; tests the universal small-support sign on all positive denominator-bounded profiles; reproduces the five-species rational witness and its three joint moments; and checks numerical convergence to the analytic rare-species limit for nine sample sizes. It reports 984 checks. These finite checks establish particular algebraic identities and examples but do not replace the universal proofs in sections 3 and 5. The exact polynomial identity has only integer coefficients; no numerical tolerance is involved in its verification.

## Relationship to prior work

Good (1953) introduced the singleton-based prediction of unseen species probability. Chao and Jost (2012) explain ecological sample coverage and the distinction between unobserved community mass and the observed sample. Ben-Hamou, Boucheron and Ohannessian (first posted 2014-12-30) studied occupancy counts and missing mass jointly, with concentration and Poissonized covariance methods; their familiar occupancy formulas and Poissonization are not claimed novel here. Related finite-population modifications (Hwang, Lin and Shen, 2014) concern another sampling scheme. The specific sign classification for two fixed draws, the sharp five-species boundary, and the all-sampling-depth finite-richness sign construction are the proposed contributions. General joint-moment identities are elementary and not independently claimed. The historical literature is extensive and an unlocated equivalent analysis remains possible; no independent priority certification is asserted.

## Limitations

This is a theorem about idealized fixed-abundance iid replacement sampling; no ecological detection heterogeneity, spatial correlation or estimator calibration is assessed. The universal minimal-support classification is **only** for sample size two; for larger fixed sample sizes the proof shows existence with sufficiently many species, not the minimal count. The positive covariance in a finite five-species community can be small, and does not imply superior accuracy, positive regression, consistency, or monotone conditional calibration of a Good–Turing estimator. Older literature includes the 1953 source with only month-level public-date evidence in the inspected records; the exact 2012-12-01 dating used for the archived ecological literature anchor is verified directly by the publisher. The closest accessible reviews and methods do not replace independent historical-priority review.

## References

1. I. J. Good, *The population frequencies of species and the estimation of population parameters*, Biometrika **40** (1953), 237–264, DOI: https://doi.org/10.1093/biomet/40.3-4.237. Original 1953 issue verified; exact day of first public distribution not established.
2. A. Chao and L. Jost, *Coverage-based rarefaction and extrapolation: standardizing samples by completeness rather than size*, Ecology **93** (2012), 2533–2547, first published 2012-12-01, DOI: https://doi.org/10.1890/11-1952.1.
3. A. Ben-Hamou, S. Boucheron and M. I. Ohannessian, *Concentration inequalities in the infinite urn scheme for occupancy counts and the missing mass, with applications*, first public arXiv version 2014-12-30, https://arxiv.org/abs/1412.8652.
4. W.-H. Hwang, C.-W. Lin and T.-J. Shen, *Good–Turing frequency estimation in a finite population*, first publicly posted 2014-11-12, DOI: https://doi.org/10.1002/bimj.201300168 (abstract inspected; complete text not available).
