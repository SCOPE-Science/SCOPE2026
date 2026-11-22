# Universal inverse-distance germination penalty in a heterogeneous habitat corridor

## Finding

Consider a single seed crossing an ordered chain of \(n\ge1\) unsuitable habitat patches before reaching one suitable target. In each season a living seed has the same habitat-blind germination probability \(g=1-q\) at every patch, including the target; germination in an unsuitable patch is fatal, while germination in the target establishes the seed. A nongerminating seed survives with patch-dependent probability and may move forward one patch. All probabilities below refer to eventual establishment, with no deadline.

**Theorem.** Let the unsuitable patches be indexed \(j=1,\ldots,n\), with dormant-season survival \(s_j\in(0,1]\) and conditional forward-movement probability \(p_j\in(0,1]\), such that \(A_j=s_j(1-p_j)<1\). Let the target's dormant-season survival be \(s_0\in[0,1)\). Set \(b_j=s_jp_j>0\). For every \(q\in[0,1]\), the establishment probability for a uniform policy equals

\[
H_n(q)=\frac{1-q}{1-s_0q}\prod_{j=1}^n\frac{b_jq}{1-A_jq}.
\]

For every finite \(n\ge1\), there is **exactly one** maximizing \(q_n\in(0,1)\), characterized by

\[
\frac{(1-q_n)(1-s_0q_n)}{q_n}
\sum_{j=1}^n\frac{1}{1-A_jq_n}=1-s_0.
\tag{1}
\]

Appending any further unsuitable patch strictly **increases** the optimal dormancy probability \(q_n\), even if the added patch has different movement and survival rates.

If seeds can recognize the habitat and separately choose germination at each patch, the best policy is to remain dormant throughout the unsuitable chain and germinate immediately at the target. Its success probability is

\[
H_n^{\rm cue}=\prod_{j=1}^n\frac{b_j}{1-A_j}.
\tag{2}
\]

Now consider any infinite sequence of patches for which \(A_j\le 1-\varepsilon\) with the same \(\varepsilon>0\) at every index; retain a fixed \(s_0<1\). Put

\[
K_n=\sum_{j=1}^n\frac{1}{1-A_j}.
\]

Then \(K_n\) grows linearly in \(n\), and the exact heterogeneous long-distance laws are

\[
(1-q_n)K_n\longrightarrow1,
\qquad
\frac{H_n(q_n)}{H_n^{\rm cue}}
\sim\frac{1}{e(1-s_0)K_n}.
\tag{3}
\]

Thus even an optimally chosen, habitat-blind germination fraction incurs an additional **inverse-distance penalty** relative to perfect habitat recognition. The universal factor \(e^{-1}\) comes from accumulated premature-germination risk across many unsuitable patches. These are single-seed establishment probabilities, not population growth or evolutionary fitness theorems.

## Assumptions and scope

The habitat chain is **one-way**, with precisely one permitted forward transition from each unsuitable patch; movement never skips or reverses sites. The seed begins alive and dormant in patch \(1\). Each season at every occupied patch: it germinates with probability \(1-q\); otherwise it survives with the patch's \(s_j\), and on survival at an unsuitable patch it moves one patch forward with probability \(p_j\), or remains there. Death and germination in unsuitable patches are absorbing failures. The target is absorbing success upon germination. The same independent transition mechanism repeats every season, with no reproduction before establishment and no finite time limit. At the target the seed cannot move; if nongerminating it may survive with probability \(s_0\) to try again.

The constraints \(b_j>0\) and \(A_j<1\) ensure a nonzero chance to traverse each patch and convergent residence-time sums. The target condition \(s_0<1\) is essential. In the comparison policy, habitat recognition permits a different germination probability at the target from those in the unsuitable corridor; all other transition rates are identical.

The limit in (3) assumes the uniform bound \(A_j\le1-\varepsilon\); no stationarity, periodicity, or limiting empirical distribution of patch parameters is required. Absolute success may still decay exponentially with distance. The statement is about the **ratio** of optimal habitat-blind success to habitat-aware success.

## Proof

**1. Patch passage and target establishment.** Write \(T_j(q)\) for the probability of leaving unsuitable patch \(j\) alive and dormant at patch \(j+1\), before germinating or dying, starting dormant in patch \(j\). A first-season decomposition gives

\[
T_j(q)=q s_jp_j+q s_j(1-p_j)T_j(q).
\]

Since \(qA_j<1\), the unique solution is \(T_j(q)=b_jq/(1-A_jq)\). At the target, the eventual successful-germination probability \(G(q)\) obeys \(G(q)=(1-q)+q s_0G(q)\), so \(G(q)=(1-q)/(1-s_0q)\). Successive applications of the strong Markov property, or elementary conditioning at each first advancement, give \(H_n(q)=G(q)\prod_jT_j(q)\). At \(q=0\) there is certain premature germination at the first unsuitable patch, and at \(q=1\) germination never occurs: both endpoint success probabilities are zero.

**2. Unique global optimum.** For \(0<q<1\), logarithmic differentiation yields

\[
\frac{H'_n(q)}{H_n(q)}
=\sum_{j=1}^n\frac{1}{q(1-A_jq)}
-\frac{1-s_0}{(1-q)(1-s_0q)}.
\tag{4}
\]

Define

\[
F_n(q)=\sum_{j=1}^n
\frac{(1-q)(1-s_0q)}{q(1-A_jq)}.
\]

For each summand the logarithmic derivative equals

\[
-\frac1{1-q}-\frac{s_0}{1-s_0q}-\frac1q
+\frac{A_j}{1-A_jq}<0,
\]

because \(A_j/(1-A_jq)<1/(1-q)\) follows strictly from \(A_j<1\). Thus \(F_n\) is strictly decreasing, with limits \(\infty\) and \(0\) at \(q\downarrow0\) and \(q\uparrow1\). Because \(1-s_0>0\), equation (1) has exactly one interior solution. By (4), \(H'_n\) is positive before this solution and negative after it. This proves a strict unique **global** maximum, not merely a stationary point.

If one further unsuitable patch is appended, its strictly positive summand raises \(F_n(q)\) at every fixed \(q\). A strictly decreasing function reaches the same level \(1-s_0\) at a strictly greater argument, proving \(q_{n+1}>q_n\).

**3. Habitat-aware benchmark.** For fixed \(s_j,p_j\), \(T_j(q)\) increases strictly on \([0,1]\) because \(T'_j(q)=b_j/(1-A_jq)^2>0\). At the target, \(G(q)\) decreases strictly because \(G'(q)=-(1-s_0)/(1-s_0q)^2<0\). Consequently, independently choosing \(q=1\) in each unsuitable patch and \(q=0\) at the target achieves and uniquely maximizes success, giving (2). The habitat-blind maximum is strictly less than this benchmark for finite \(n\ge1\).

**4. Universal heterogeneous long-distance law.** The hypothesis \(0\le A_j\le1-\varepsilon\) implies \(n\le K_n\le n/\varepsilon\). For every fixed \(q<1\), the sum in \(F_n(q)\) is at least \(n(1-q)(1-s_0q)/q\); therefore the unique roots satisfy \(q_n\to1\). Put \(\delta_n=1-q_n\). Equation (1) becomes

\[
\delta_n\frac{1-s_0+s_0\delta_n}{1-\delta_n}
\sum_{j=1}^n\frac{1}{1-A_j+A_j\delta_n}=1-s_0.
\]

The uniform bound on \(A_j\) gives

\[
\sum_{j=1}^n\frac{1}{1-A_j+A_j\delta_n}
=K_n(1+O(\delta_n/\varepsilon)),
\]

where the implicit constant is independent of \(n\). Thus \(\delta_n K_n\to1\), and in particular \(\delta_n=O(1/n)\). Dividing the habitat-blind probability by (2) gives

\[
\frac{H_n(q_n)}{H_n^{\rm cue}}
=\frac{\delta_n}{1-s_0+s_0\delta_n}
\prod_{j=1}^n\frac{(1-\delta_n)(1-A_j)}{1-A_j+A_j\delta_n}.
\]

Uniform Taylor expansion of the logarithm of the product yields

\[
\sum_{j=1}^n\log\frac{(1-\delta_n)(1-A_j)}{1-A_j+A_j\delta_n}
=-\delta_nK_n+O(n\delta_n^2/\varepsilon^2)\longrightarrow-1.
\]

The leading prefactor is \(\delta_n/(1-s_0)\), hence (3). This derivation uses no numerical extrapolation.

**5. The essential target-survival boundary.** If \(s_0=1\), then for every \(q<1\) eventual target germination is certain conditional on arrival; \(G(q)=1\). The uniform-policy success is then strictly increasing with \(q\) on \([0,1)\), with supremum (2) as \(q\uparrow1\), but \(q=1\) never germinates and has success zero. Therefore no interior maximizer and no inverse-distance cue penalty of form (3) exist at this singular boundary. If \(n=0\) and \(s_0<1\), immediate germination \(q=0\) is uniquely optimal instead.

## Verification

An exact homogeneous test takes \(n=5\), \(s_j=s_0=3/4\), and \(p_j=1/2\). Then \(A_j=3/8\), and the unique maximizer is the smaller quadratic root

\[
q_5=\frac{4(36-\sqrt{66})}{123}=0.9065353364\ldots.
\]

It produces \(H_5(q_5)=0.010581862916\ldots\), whereas perfect habitat recognition produces \(H_5^{\rm cue}=(3/5)^5=0.07776\) and the uniform choice \(q=1/2\) gives only \(0.0005235757205\ldots\). These numbers are illustrative, not field measurements. In this homogeneous family, \(K_n=8n/5\), so the proven asymptotic ratio is \(H_n(q_n)/H_n^{\rm cue}\sim5/(2en)\).

Run `python3 check_seed_corridor.py` with Python 3 and no third-party packages. The checker independently evolves a finite-horizon Markov probability distribution and compares it with the exact infinite-horizon expression on 400 randomized heterogeneous instances, checks unique maximizers against dense grids, verifies the radical example, and tests heterogeneous large-chain asymptotics. It reports 42,228 supplementary finite numerical checks. These tests corroborate rather than replace the analytic proof of all-parameter and infinite-chain statements.

## Relationship to prior work

Szojka and Germain (2021 preprint; 2024 journal article) measured dormant seed banks and adult plants across suitable–unsuitable grassland boundaries. They explicitly identify successive transport of dormant seeds through an unsuitable matrix as a plausible connectivity mechanism and motivate quantifying survival before burial or death; they do not state the optimization and cue-penalty law (1)–(3). Satterthwaite (2009) analyzes evolutionarily stable dormancy under competition for discrete safe sites, and Venable and Lawlor (1980) study dormancy–dispersal tradeoffs under variable reproductive environments. Both establish the prior conceptual relevance of optimal germination; neither accessible account establishes the ordered, one-seed, first-establishment corridor comparison here. Chen and colleagues (2020) empirically analyze spatial and temporal seed dispersal; Pausas and colleagues (2022) discuss environmental cues and spatial bet hedging.

The first-step identities and absorbing-chain techniques are classical. No claim of novelty is made for geometric-series hitting probabilities, the qualitative fact that dormancy may assist dispersal, or the general existence of plant germination tradeoffs. The specific assessed mathematical contribution is the heterogeneous uniqueness/extension law and the sharp universal \(e^{-1}/K_n\) asymptotic **loss from habitat-blind germination relative to habitat-aware establishment**. Historical priority is not independently certified; the full Venable–Lawlor article was not accessible for complete comparison.

## Limitations

This is an intentionally idealized single-seed, one-way, time-homogeneous, infinite-horizon model. It excludes reverse and long jumps, seed production during passage, state-dependent movement while dormant, spatial and seasonal environmental correlations, density dependence, predation differences between behavior states, species interactions, and finite observation deadlines. Optimal establishment from one seed is not generally the same as optimal evolutionary fitness. The benchmark assumes perfect detection of suitable habitat, which is a theoretical upper bound. The \(e^{-1}/K_n\) limit requires a uniform upper bound below one on the within-patch retention products, and fails without qualification as target survival approaches unity. Parameters and outcomes have not been field-calibrated; no independent mathematical audit has been performed.

## References

- Szojka, M. C., and Germain, R. M. (2024). *Dispersing across habitat boundaries: Uncovering the demographic fates of populations in unsuitable habitat*. Ecosphere 15, e4814. Journal article first published 24 March 2024; preprint publicly posted 23 March 2021. https://doi.org/10.1002/ecs2.4814 ; https://doi.org/10.1101/2021.03.22.436493
- Venable, D. L., and Lawlor, L. (1980). *Delayed germination and dispersal in desert annuals: Escape in space and time*. Oecologia 46, 272–282. https://doi.org/10.1007/BF00540137
- Satterthwaite, W. H. (2009). *Competition for space can drive the evolution of dormancy in a temporally invariant environment*. Plant Ecology 208, 167–185. https://doi.org/10.1007/s11258-009-9696-y
- Chen, S.-C., et al. (2020). *Trade-off between seed dispersal in space and time*. Ecology Letters 23, 1635–1642. https://doi.org/10.1111/ele.13595
- Pausas, J. G., et al. (2022). *Bet-hedging and best-bet strategies shape seed dormancy*. New Phytologist 236, 1232–1236. https://doi.org/10.1111/nph.18436
