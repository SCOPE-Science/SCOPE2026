# Consecutive habitat-activation thresholds for Poisson founder quorums

## Finding

Fix integers \(n\ge2\) and \(r\ge3\). An introduction budget \(B>0\) is divided into nonnegative *Poisson mean founder intensities* \(x_1,\ldots,x_n\) satisfying \(\sum_i x_i=B\). At each of \(n\) identical, noninteracting habitats, founder receipt is Poisson with mean \(x_i\); that habitat is initially viable if it receives at least \(r\) founders. Write
\[
 Q_r(x)=\Pr\{\operatorname{Pois}(x)\ge r\}=1-e^{-x}\sum_{j=0}^{r-1}\frac{x^j}{j!},\qquad x\ge0.
\]
The expected number of viable habitats is \(\sum_i Q_r(x_i)\). For \(m=1,\ldots,n\), put \(V_m(B)=mQ_r(B/m)\).

**Exact consecutive-activation theorem.** There is a uniquely determined number \(a_r>0\) satisfying \(a_r Q_r'(a_r)=Q_r(a_r)\). There are unique budget thresholds \(B_{r,m}\), for every integer \(m\ge1\), defined by
\[
 mQ_r(B_{r,m}/m)=(m+1)Q_r(B_{r,m}/(m+1)).
\]
They satisfy the *strict interlacing and ordering*
\[
 m a_r<B_{r,m}<(m+1)a_r<B_{r,m+1}.
\]
Set \(B_{r,0}=0\) and \(B_{r,n}=+\infty\). When \(B_{r,m-1}<B<B_{r,m}\), **all** global optimizers have exactly \(m\) positive coordinates, each \(B/m\); the choice of the \(m\) habitats is arbitrary. At \(B=B_{r,m}\) for \(1\le m<n\), exactly the equal-\(m\) and equal-\((m+1)\) patterns are global optimizers, up to permutation. There are no skipped support sizes, unequal-positive optima, triple ties, or additional optimizers.

For any fixed integer \(m\ge1\), the thresholds have the **large-quorum Gaussian-quantile law**
\[
 \lim_{r\to\infty}\frac{B_{r,m}/(m+1)-r}{\sqrt r}
 =\Phi^{-1}\!\left(\frac{m}{m+1}\right),
\]
where \(\Phi\) is the standard normal distribution function. For example, at quorum \(r=3\), the first four thresholds are approximately \(4.781210650\), \(8.285064731\), \(11.718896449\), and \(15.130198012\), respectively. The previously established \(r=2\) specialization has first threshold \(2.512862417\ldots\), the positive root of \(e^{B/2}=1+B\); this is provided only as a comparison and not claimed as new.

## Assumptions and scope

The effort \(B\) is a continuous *mean founder-arrival budget*, not a fixed integer number of individuals. Founder counts are independent Poisson variables. Habitats are identical; there are no fixed activation costs, density-dependent interactions between sites, migration, time steps, site-quality heterogeneity or post-founding population dynamics. The quorum event is treated as a proxy for initial establishment, not as a biological guarantee of persistence. The sole objective is the expected number of habitats meeting the quorum; maximizing the probability that at least one or at least two habitats succeed is a different optimization problem. The evaluated higher-quorum claim holds for all indicated \(B>0\), integer \(r\ge3\), and finite \(n\ge2\). The proof also specializes to the previously established \(r=2\) case, which is credited rather than accepted as new work. The case \(r=1\) has a concave response and is optimally spread equally over all \(n\) sites for every positive budget.

## Proof

**1. Pairwise elimination of unequal positive coordinates.** Differentiating the Poisson upper tail gives
\[
 Q_r'(x)=\frac{e^{-x}x^{r-1}}{(r-1)!}\quad(x>0),\qquad
 Q_r''(x)=Q_r'(x)\left(\frac{r-1}{x}-1\right).
\]
For a pair with fixed sum \(s>0\), let \(H_s(x)=Q_r(x)+Q_r(s-x)\) for \(0\le x\le s/2\). The sign of \(H_s'(x)\) is the sign of
\[
 h_s(x)=(r-1)\log\frac{x}{s-x}+s-2x.
\]
Here \(h_s(0+)=-\infty\), \(h_s(s/2)=0\), and
\[
 h_s'(x)=(r-1)\left(\frac1x+\frac1{s-x}\right)-2
\]
is strictly decreasing on \((0,s/2)\). Consequently \(h_s\) is either negative throughout the open half interval or changes sign exactly once there, from negative to positive. Thus \(H_s\) is either strictly decreasing or first strictly decreasing and then strictly increasing. In either case no unequal positive split can maximize \(H_s\): the only possible pairwise maxima are \((s,0)\), \((0,s)\) and \((s/2,s/2)\). Replacing any two unequal positive coordinates in a purported global optimizer by the strictly better endpoint or midpoint split is feasible. Therefore every global optimizer has \(m\) equal positive coordinates and \(n-m\) zeros for some \(1\le m\le n\). Its value is \(V_m(B)\). This step proves more than existence of one equal-support optimizer.

**2. Strictly decreasing elasticity.** Define \(E_r(x)=xQ_r'(x)/Q_r(x)\) for \(x>0\). The absolutely convergent Poisson series gives
\[
 E_r(x)=\frac{r}{\displaystyle\sum_{j=0}^{\infty}\frac{r!}{(r+j)!}x^j}.
\]
Every positive-degree coefficient in the denominator is strictly positive, so \(E_r\) is strictly decreasing from \(r\) at zero to \(0\) at infinity. Let \(g_r(x)=Q_r(x)/x\). Then
\[
 g_r'(x)=\frac{Q_r(x)}{x^2}\bigl(E_r(x)-1\bigr).
\]
As \(r\ge3\), there is a unique \(a_r>0\) with \(E_r(a_r)=1\). Consequently \(g_r\) increases strictly on \((0,a_r)\) and decreases strictly on \((a_r,\infty)\).

**3. One and only one adjacent crossing.** Because \(V_m(B)=B g_r(B/m)\), the ratio
\[
 R_m(B)=\frac{V_m(B)}{V_{m+1}(B)}=\frac{g_r(B/m)}{g_r(B/(m+1))}
\]
has logarithmic derivative
\[
 \frac{d}{dB}\log R_m(B)
 =\frac{E_r(B/m)-E_r(B/(m+1))}{B}<0.
\]
The small-budget expansion \(Q_r(x)\sim x^r/r!\) gives \(R_m(0+)=((m+1)/m)^{r-1}>1\); the large-budget limit \(Q_r(x)\to1\) gives \(R_m(+\infty)=m/(m+1)<1\). Hence the crossing equation has exactly one positive root \(B_{r,m}\). At \(B=m a_r\), unimodality of \(g_r\) gives \(R_m(B)>1\). At \(B=(m+1)a_r\), it gives \(R_m(B)<1\). Thus \(m a_r<B_{r,m}<(m+1)a_r\), and the thresholds for consecutive \(m\) are strictly ordered and disjoint.

**4. Global phase diagram and equality cases.** Fix \(B\) strictly between two consecutive thresholds. All adjacent differences \(V_{j+1}(B)-V_j(B)\) are positive for \(j<m\) and negative for \(j\ge m\); hence \(V_m\) is the unique maximum over all positive support sizes. At \(B=B_{r,m}\), precisely the adjacent values \(V_m=V_{m+1}\) tie and exceed every other \(V_j\). Step 1 excludes every non-equal-positive competing allocation. This completes the exact all-budget classification.

**5. Large-quorum law.** Hold \(m\ge1\) fixed and set \(B=(m+1)(r+z\sqrt r)\), with fixed real \(z\) and sufficiently large \(r\). The Poisson central limit theorem gives
\[
 Q_r\!\left(\frac B{m+1}\right)\longrightarrow\Phi(z),
 \qquad Q_r\!\left(\frac Bm\right)\longrightarrow1,
\]
where the second limit follows because \((m+1)/m>1\). Therefore
\[
 V_m(B)-V_{m+1}(B)\longrightarrow m-(m+1)\Phi(z).
\]
The right side changes sign exactly at \(z_m=\Phi^{-1}(m/(m+1))\). For any \(z_-<z_m<z_+\), the strict single-crossing property proven in step 3 traps \(B_{r,m}/(m+1)\) between \(r+z_-\sqrt r\) and \(r+z_+\sqrt r\) for all sufficiently large \(r\). Letting \(z_-,z_+\to z_m\) proves the claimed limit.

## Verification

The standalone, standard-library Python script `check.py` reproduces the finite diagnostics. Run `python3 check.py`. It evaluates 15,753 numerical assertions for Poisson tail normalization, pairwise endpoint/equal-half dominance on sampled pairs, numerical existence and ordering of adjacent thresholds, unique winning support count between thresholds, pairwise ties and the concave \(r=1\) boundary. The script reproduces the new \(r=3,5\) threshold examples and the previously established \(r=2\) boundary case. Computations here are **diagnostics only**: the continuum and all-integer statements rest on the analytic proof, and the large-quorum limit on the stated Poisson CLT.

## Relationship to prior work

The equal-positive-support reduction for **identical sigmoid response functions in general** is already present in Corollary 5 of Srivastava and Bullo (2014), which reduces the objective to maximizing \(m f(B/m)\) over integer \(m\). That generic reduction is not claimed as novel. An earlier two-founder Poisson-habitat result already established the exact all-budget adjacent-step staircase and its large-number-of-sites asymptotic when \(r=2\); that case is fully credited as prior coverage, not new work. The contribution evaluated here is the **all-quorum extension for every integer \(r\ge3\)**, with strictly ordered support crossings, explicit interval bounds and the **new high-quorum Gaussian-quantile law** (which has no counterpart when the quorum is fixed at two). The prior corollary alone does not provide this full ordered phase diagram or its asymptotic coefficients. The generalized shape is motivated by multi-founder establishment rather than an unmotivated change of numerical parameter. Some earlier nonconvex resource-allocation literature is not fully accessible, and historical priority remains provisional.

Grevstad (1999) motivates an establishment threshold through stochastic simulations of small biological-control introductions. Shea and Possingham (2000) optimize biological-control releases through a **multi-period, state-dependent dynamic program**, including objectives involving established sites and a preselected set of release strategies; their inspected equations and results do not give the exact continuous one-shot Poisson all-budget threshold sequence. Duncan and colleagues (2014) examine how establishment probability varies with founding population size, without the allocation classification. Goodsman and Lewis (2016) analyze founding-size thresholds in a spatial integrodifference model, a distinct mechanism. The previously established two-founder habitat result does not imply the large-\(r\) quantile limit without an additional high-quorum argument. A previously reported two-candidate astronomical scheduling limit involves the same positive root \(e^{c/2}=1+c\) as this theorem's isolated \((r,m)=(2,1)\) example. The numerical coincidence is acknowledged, not treated as new or as implying the general theorem.

## Limitations

An identical Poisson receipt model with a hard quorum simplifies biologically important variation in founding success, mate structure, dispersal, habitat suitability, environmental fluctuations, and adaptive releases. The classification does not extend automatically to unequal habitat quality, fixed release costs, indivisible founders, correlated arrivals, nonlinear expected-fecundity objectives, or maximizing the chance of at least one viable site. It has no empirical calibration. A historically plausible but uninspected full-text source, Ginsberg (1974), treats identical increasing-returns allocations, and the full texts of Grevstad (1999) and Ağralı and Geunes (2009) were not available during the literature comparison. The documented limitations constrain historical priority claims, not the self-contained mathematical proof.

## References

- Ginsberg, W. (1974), *The multiplant firm with increasing returns to scale*, Journal of Economic Theory 9, 283–292. DOI: https://doi.org/10.1016/0022-0531(74)90053-2. Bibliographic record only; full text not inspected.
- Grevstad, F. S. (1999), *Factors influencing the chance of population establishment: implications for release strategies in biocontrol*, Ecological Applications 9, 1439–1447. https://doi.org/10.1890/1051-0761(1999)009[1439:FITCOP]2.0.CO;2. Abstract inspected; publicly dated November 1, 1999.
- Shea, K. and Possingham, H. P. (2000), *Optimal release strategies for biological control agents: an application of stochastic dynamic programming to population management*, Journal of Applied Ecology 37, 77–86. https://doi.org/10.1046/j.1365-2664.2000.00467.x. Full text inspected.
- Ağralı, S. and Geunes, J. (2009), *Solving knapsack problems with S-curve return functions*, European Journal of Operational Research 193, 605–615. https://ideas.repec.org/a/eee/ejores/v193y2009i2p605-615.html. Abstract and bibliographic description inspected; DOI suffix not confirmed in available evidence.
- Srivastava, V. and Bullo, F. (2014), *Knapsack problems with sigmoid utilities: approximation algorithms via hybrid optimization*, European Journal of Operational Research 236, 488–498. https://doi.org/10.1016/j.ejor.2013.12.035. Author manuscript https://motion.me.ucsb.edu/pdf/2012n-sb.pdf, Sections 1–3 and Corollary 5 inspected.
- Duncan, R. P., Blackburn, T. M., Rossinelli, S. and Bacher, S. (2014), *Quantifying invasion risk: the relationship between establishment probability and founding population size*, Methods in Ecology and Evolution 5, 1255–1263. https://doi.org/10.1111/2041-210X.12288. Full text inspected.
- Goodsman, D. W. and Lewis, M. A. (2016), *The minimum founding population in dispersing organisms subject to strong Allee effects*, Methods in Ecology and Evolution 7, 1100–1109. https://doi.org/10.1111/2041-210X.12573. Full text inspected.
