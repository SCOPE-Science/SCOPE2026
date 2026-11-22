# Objective-dependent seasonal phase rigidity for three Poisson-detected species

## Finding

Let three targets have equal-baseline, equally phase-shifted seasonal molecular intensities
\[
\lambda_j(\theta)=a+b\cos(\theta+2\pi j/3),\qquad j=0,1,2,
\]
where \(a>b>0\). Let a single sampling campaign have a nonnegative *common* efficiency \(E\), whose distribution does not depend on the seasonal phase \(\theta\), with \(E<\infty\) almost surely and \(\Pr(E>0)>0\). Conditional on \(E=e\), the three species generate mutually independent Poisson read counts with respective means \(e\lambda_j(\theta)\). A species is reported detected exactly when its count is positive; write \(K\in\{0,1,2,3\}\) for the number of detected species.

**Exact seasonal-order theorem.** Set \(c=\cos(3\theta)\). As a function of \(c\in[-1,1]\), the probabilities \(\Pr(K=1)\) and \(\Pr(K=3)\), and expected detected richness \(\mathbb E[K]\), are strictly increasing. The probabilities \(\Pr(K=2)\) and \(\Pr(K\ge 2)\) are strictly decreasing. The probabilities \(\Pr(K=0)\) and \(\Pr(K\ge1)\) are independent of phase. All statements persist for any distribution of common efficiency satisfying the assumptions. Thus the *only* global maximizers of expected richness, exactly one detection, and all-three detection are \(\theta\equiv0\pmod{2\pi/3}\); the *only* maximizers of exactly two detection and at-least-two detection are \(\theta\equiv\pi/3\pmod{2\pi/3}\). At these two respective seasons, the intensity patterns (up to permutation) are \((a+b,a-b/2,a-b/2)\) and \((a-b,a+b/2,a+b/2)\).

**Sharp effort contrast for one-versus-two coverage.** For deterministic efficiency \(E=e>0\), the absolute difference in \(\Pr(K=1)\) between the two extremal seasons equals the improvement in \(\Pr(K\ge2)\) in the opposite direction and is exactly
\[
\Delta(e)=4e^{-2ae}\sinh(be/2)\bigl(\cosh(be/2)-1\bigr)>0.
\]
The contrast has exactly one maximizer \(e_*>0\), characterized by
\[
\coth(be_*/2)+\coth(be_*/4)=4a/b.
\]
In particular \(\Delta(e)\sim b^3e^3/4\) as \(e\downarrow0\), and it decays exponentially as \(e\to\infty\). The unique effort maximizing sensitivity to *which of these two seasonal designs is chosen* is therefore finite.

## Assumptions and scope

The three target species are assumed present, identifiable without false positives, and conditionally independent given the campaign's common efficiency. Equal means and exactly \(120^\circ\) seasonal offsets are imposed; these are theoretical symmetry assumptions, not estimates from any cited field study. Phase is continuous over a full period, not restricted to discrete calendar months. A common random efficiency may model correlated field quality, but it may not have a phase-dependent distribution. The theorem concerns probability of molecular *detection*, not species occupancy, ecological abundance or abundance estimation. Its primary application is theoretical design of multispecies environmental-DNA screening.

## Proof

Write \(x_j(\theta)=\cos(\theta+2\pi j/3)\). Trigonometric identities give
\[
\sum_jx_j=0,\quad \sum_{j<k}x_jx_k=-3/4,\quad
4\prod_j(X-x_j)=4X^3-3X-c,
\]
where \(c=\cos3\theta\). For \(-1<c<1\) the three roots are distinct. Implicit differentiation of the cubic gives
\[
\frac{dx_j}{dc}=\frac1{4\prod_{k\ne j}(x_j-x_k)}.
\]
For a \(C^3\) function \(g\), let \(F_g(c)=\sum_jg(a+bx_j(c))\). Then
\[
F_g'(c)=\frac b4\sum_j\frac{g'(a+bx_j)}{\prod_{k\ne j}(x_j-x_k)}
=\frac b4\,[x_0,x_1,x_2]h,
\qquad h(x)=g'(a+bx).
\]
The bracket denotes the ordinary second divided difference. The mean-value theorem for divided differences gives \([x_0,x_1,x_2]h=h''(\xi)/2=b^2g'''(a+b\xi)/2\) for some \(\xi\) between the least and greatest roots. Consequently \(F_g'(c)\) has the strict sign of \(g'''\) whenever this derivative has a fixed nonzero sign on \([a-b,a+b]\). Endpoint continuity extends the resulting strict order to \([-1,1]\).

First fix \(E=e>0\), and set \(q_j=e^{-e(a+bx_j)}\) and \(Q=\prod_jq_j=e^{-3ea}\). Independence yields
\[
\begin{aligned}
\Pr(K=0)&=Q,\\
\Pr(K=1)&=Q\left(\sum_j e^{e(a+bx_j)}-3\right),\\
\Pr(K\ge2)&=1+2Q-Q\sum_j e^{e(a+bx_j)},\\
\Pr(K=3)&=\prod_j\bigl(1-e^{-e(a+bx_j)}\bigr),\\
\mathbb E[K]&=3-\sum_j e^{-e(a+bx_j)}.
\end{aligned}
\]
For \(g(u)=e^{eu}\), one has \(g'''>0\), hence the displayed exponential sum strictly increases with \(c\). The first two nonconstant probabilities therefore have the claimed opposite monotonicities. For \(g(u)=e^{-eu}\), one has \(g'''<0\), so expected richness strictly increases with \(c\). For \(g(u)=\log(1-e^{-eu})\), defined because \(u\ge a-b>0\), differentiation gives
\[
 g'''(u)=\frac{e^3e^{eu}(e^{eu}+1)}{(e^{eu}-1)^3}>0.
\]
Thus \(\log\Pr(K=3)=F_g(c)\) strictly increases. Since \(\Pr(K=2)=\Pr(K\ge2)-\Pr(K=3)\), exactly-two probability strictly decreases. Finally \(\Pr(K\ge1)=1-Q\) is constant. The only possible extrema occur where \(c=\pm1\), giving the stated congruence classes of phase.

For random common efficiency, condition on \(E=e\). Every strict inequality above holds for every \(e>0\); at \(e=0\) the relevant quantities are phase-independent. Integrating over an arbitrary phase-independent efficiency law with positive probability of \(e>0\) preserves strict inequalities and equalities. No assumption of independent efficiency multipliers across species is needed.

For constant positive \(e\), the three cosine values at \(c=1\) are \((1,-1/2,-1/2)\), while at \(c=-1\) they are \((-1,1/2,1/2)\). Substitute into the displayed formula for \(\Pr(K=1)\) to obtain
\[
\begin{aligned}
\Delta(e)&=e^{-2ea}\left(e^{eb}+2e^{-eb/2}-e^{-eb}-2e^{eb/2}\right)\\
&=4e^{-2ea}\sinh(eb/2)\left(\cosh(eb/2)-1\right).
\end{aligned}
\]
Because \(\Pr(K=1)+\Pr(K\ge2)=1-Q\), the opposite-direction gain in at-least-two detection is the same. Put \(y=be/2\). Logarithmic differentiation gives
\[
\frac{d}{de}\log\Delta(e)=-2a+\frac b2\left(\coth y+\coth(y/2)\right).
\]
The sum of the two hyperbolic cotangents strictly decreases from infinity to \(2\) as \(y\) increases from zero to infinity. Since \(4a/b>4>2\), it crosses \(4a/b\) exactly once, proving a unique global contrast maximum. Direct positive-function expansions give the asserted small- and large-effort behavior.

## Verification

Run `python verify.py` in the directory containing this file. The standard-library checker independently constructs the four detection-count probabilities, tests the three prescribed seasonal comparisons across 200 deterministic parameter triples and 41 phase samples per triple, compares the exact gap formula, checks a shared-efficiency mixture and computes the unique effort optimum for \(a=2,b=1\). It reports 34,603 finite numerical assertions passed. These finite tests are supplemental: the all-parameter conclusions follow from the divided-difference proof above, not enumeration.

For \(a=2,b=1,e=1\), the one-peak season has \(\Pr(K=1)=0.064568804914\), \(\Pr(K=2)=0.359473522306\), \(\Pr(K=3)=0.573478920603\); the two-above-average season has corresponding probabilities \(0.059696457314\), \(0.405220267262\), and \(0.532604523248\). Both seasons have \(\Pr(K\ge1)=0.997521247823\). For these parameters, \(e_*\approx0.768312620752\).

## Relationship to prior work

Rounds et al. (2024) document pronounced differences in seasonal detection among four aquatic invasive species and discuss multispecies scheduling priorities. Their empirical hierarchical occupancy analysis does not assume three phase-equidistant harmonic intensities or establish exact rankings of one-, two- and three-species observation objectives. Takahara et al. (2019) compare three frog species across three observed seasons and report different optimal detection times; they do not derive this symmetric continuous-phase Poisson classification. Bedwell and Goldberg (2020) analyze volume, spatial design and seasonal timing for amphibian environmental-DNA sampling, not the three-target objective reversal. The positivity of second divided differences is a standard mathematical technique; no novelty is asserted for that lemma in isolation. The finding is the joint, explicit seasonal design classification and its common-efficiency and effort-contrast consequences, not the existence of seasonality or elementary Poisson thinning. Published search results relating to multispecies richness, seasonal occupancy and triple-phase Fourier structure have not been shown to imply the statement under its exact assumptions. Priority is provisional; related uninspected sources may exist.

## Limitations

The harmonic equal-amplitude model is deliberately idealized and does not fit the species-specific empirical curves of cited studies. Unequal baselines, unequal amplitudes, non-equidistant phases, cross-species molecular dependence beyond a common efficiency variable, contamination, phase-dependent assay efficiency and discrete restricted sampling dates may invalidate the ranking. The contrast optimum maximizes the *difference between two stipulated sampling phases*, not absolute species detection or an economic benefit-cost function. The theorem makes no assertion about field-calibrated survey performance, occupancy inference, or the uniqueness of its mathematical formulation in unsearched historical literature.

## References

1. Rounds, C. I., et al. (2024), “Aquatic invasive species exhibit contrasting seasonal detectability patterns based on environmental DNA: Implications for monitoring.” *Freshwater Biology* **69**, 1479–1493. First online 2024-08-17. DOI: https://doi.org/10.1111/fwb.14320
2. Takahara, T., Iwai, N., Yasumiba, K., and Igawa, T. (2019), “Comparison of the detection of 3 endangered frog species by eDNA and acoustic surveys across 3 seasons.” *Freshwater Science* **39**. DOI: https://doi.org/10.1086/707365
3. Bedwell, M. E., and Goldberg, C. S. (2020), “Spatial and temporal patterns of environmental DNA detection to inform sampling protocols in lentic and lotic systems.” *Ecology and Evolution* **10**, 1602–1612. DOI: https://doi.org/10.1002/ece3.6014
