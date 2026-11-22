# Arbitrarily many spurious depth peaks under relative-read filtering

## Finding

For an idealized metabarcoding sample containing a weak spurious sequence source, an abundance filter that retains sequences at or above a fixed fraction of reads can have **arbitrarily many separate local maxima in false-call probability as sequencing depth grows**. This holds even though the expected spurious fraction is strictly below the threshold at every depth. The result concerns the probability of retaining a *particular* spurious taxon; it does not concern expected total richness or the probability that any spurious taxon occurs.

More precisely, fix \(0<\gamma<1\) and integer \(K\ge2\), with a filter retaining relative read abundance at least \(1/K\). At a scaled effort \(s>0\) let the spurious count \(C_K(s)\) and all other reads \(G_K(s)\) be independent with
\[
C_K(s)\sim\operatorname{Pois}(\gamma s),\qquad G_K(s)\sim\operatorname{Pois}((K-\gamma)s).
\]
Define \(N_K=C_K+G_K\). The false retention probability is
\[
q_K(s)=\Pr\big\{C_K(s)\ge1,\;K C_K(s)\ge N_K(s)\big\}.
\]
Here \(\mathbb E N_K(s)=Ks\), and the expected spurious read fraction conditional on any positive total is \(\gamma/K<1/K\). (The fraction is undefined at zero reads, where we do not retain the taxon.)

**Theorem.** For every fixed \(\gamma\in(0,1)\) and each noninteger \(s>0\), set \(d_s=\operatorname{dist}(s,\mathbb Z)>0\). Then
\[
\left|q_K(s)-H_\gamma(s)\right|\le\frac{s}{Kd_s^2},\qquad
H_\gamma(s)=\Pr\{Z_s>s\},\quad Z_s\sim\operatorname{Pois}(\gamma s).
\]
On each interval \(j<s<j+1\), for integer \(j\ge0\), the limiting function is strictly increasing, while at every integer \(j\ge1\) its left limit exceeds its right limit by
\[
\Delta_j=e^{-\gamma j}\frac{(\gamma j)^j}{j!}>0.
\]
Consequently, for every \(L\ge1\) there exists \(K_0(\gamma,L)\) such that each integer \(K\ge K_0(\gamma,L)\) makes the continuous analytic function \(q_K\) possess at least \(L\) *distinct strict local maxima* and at least \(L-1\) intervening local minima on \(s>0\).

There is also a concrete finite-cutoff result: at \(K=1000\), \(\gamma=1/4\), the model has at least seven strict local maxima. This is a \(0.1\%\) abundance filter with an actual mean spurious fraction of \(0.025\%\). The certificate uses interval-bounded probabilities at \(s=j-3/20\), \(s=j+3/20\), and \(s=3/20\), for \(j=1,\ldots,7\).

## Assumptions and scope

1. Each read belongs either to one spurious taxon or to background sequences, with independent Poisson read counts at a fixed underlying read composition; this is the standard Poissonization of multinomial sampling and is not a model of PCR amplification bias.
2. The total mean number of reads is the freely varying continuous quantity \(Ks\), not a fixed observed integer. The filter tests realized sample-relative abundance, not the expected fraction.
3. The cutoff is inclusive, retaining the spurious sequence at equality, and the taxon is never retained when the total number of reads is zero.
4. When the cutoff \(1/K\) varies, the spurious fraction is scaled as \(\gamma/K\), with \(\gamma\) held in \((0,1)\). The theorem does not assert unbounded maxima at one *fixed* cutoff \(K\).

## Proof

**1. Quantitative rare-read limit.** Poisson addition gives \(N_K(s)\sim\operatorname{Pois}(Ks)\), hence \(\mathbb EN_K(s)/K=s\) and \(\operatorname{Var}(N_K(s)/K)=s/K\). For \(s\notin\mathbb Z\), on the event \(|N_K(s)/K-s|<d_s\), the two inequalities \(C_K(s)\ge N_K(s)/K\) and \(C_K(s)>s\) are equivalent because \(C_K(s)\) is integer-valued and the interval contains no integer crossing. The zero-read exception causes no difference: \(C_K=0\) never satisfies either inequality when \(s>0\) and the total is positive, and a zero total has \(C_K=0\) so the excluded outcome is not present in the comparison event \(C_K>s\). Chebyshev's inequality therefore bounds the difference of the two event probabilities by \(s/(Kd_s^2)\). Since the marginal law of \(C_K(s)\) is exactly \(\operatorname{Pois}(\gamma s)\), the claim follows.

**2. The discontinuous limiting profile.** If \(j<s<j+1\), integer \(j\ge0\), then
\[
H_\gamma(s)=1-e^{-\gamma s}\sum_{r=0}^{j}\frac{(\gamma s)^r}{r!},\qquad
H_\gamma'(s)=\gamma e^{-\gamma s}\frac{(\gamma s)^j}{j!}>0.
\]
At integer \(j\ge1\), the threshold \(Z_s>s\) advances from \(Z_s\ge j\) on the left to \(Z_s\ge j+1\) on the right; therefore the jump has the stated positive size \(\Delta_j\). No continuity of \(H_\gamma\) at integers is claimed.

**3. Infinitely many distinct finite-cutoff peaks.** Fix an arbitrary positive integer \(L\). By the finitely many positive jump sizes \(\Delta_j\), choose a common \(\eta\in(0,1/2)\) so small that \(H_\gamma(j-\eta)>H_\gamma(j+\eta)\) for each \(j=1,\ldots,L\). Strict increase on \((j-1,j)\) additionally gives \(H_\gamma(j-\eta)>H_\gamma(j-1+\eta)\). The quantitative convergence in Step 1, applied to these finitely many noninteger points, transfers all strict inequalities to \(q_K\) for every sufficiently large \(K\). Thus \(q_K\) achieves a maximum strictly inside each disjoint closed interval \([j-1+\eta,j+\eta]\).

The Poisson series defining \(q_K\) converges absolutely and locally uniformly together with all derivatives in \(s>0\), so \(q_K\) is real analytic. It is not constant, since it is positive for \(s>0\) but tends to zero as \(s\downarrow0\). Therefore its interior maxima cannot lie on an interval of constancy and are strict local maxima. The maxima are distinct because the intervals are disjoint. Continuity between them supplies at least \(L-1\) intervening minima. This is an existence statement for \(K_0\); no unproved uniform-in-\(L\) estimate is used.

**4. Finite \(0.1\%\) cutoff certificate.** For integer \(K\ge2\), conditioning on a positive spurious read count \(c\) gives the exact positive-series formula
\[
q_K(s)=\sum_{c=1}^\infty e^{-\gamma s}\frac{(\gamma s)^c}{c!}\;\Pr\{\operatorname{Pois}((K-\gamma)s)\le(K-1)c\}.
\]
At \(K=1000\), \(\gamma=1/4\), let \(a_0=3/20\), \(x_j=j-3/20\), and \(a_j=j+3/20\) for \(j=1,\ldots,7\). The standalone checker `check.py` sums the first \(30\) terms using outward-rounded decimal interval arithmetic and adds to each upper endpoint the analytic remainder bound
\[
\Pr\{C_K(s)>30\}\le\frac{(\gamma s)^{31}}{31!\,[1-\gamma s/32]},\qquad s\le7+3/20.
\]
It verifies the fourteen strict inequalities \(q_K(x_j)>q_K(a_{j-1})\) and \(q_K(x_j)>q_K(a_j)\). Analyticity and the interval-maxima argument prove at least seven distinct strict local maxima for this exact finite cutoff. This is a certificate of a **lower bound** on the number of peaks, not an exhaustive peak census.

## Verification

Run `python3 check.py` with the standard Python library. The checker uses two directed-rounding recursions for the Poisson mass series, conservative exponential seeds and a positive bound for omitted spurious-count tails; it checks fourteen strict interval inequalities. All fourteen passed in the packaged copy. Representative intervals rounded for display (not used for certification) at the first two witness triples are \((0.03680558,0.19143963,0.03419981)\) and \((0.03419981,0.07903203,0.01743331)\) for the probabilities at \((a_{j-1},x_j,a_j)\).

The proof of arbitrarily many peaks is analytic; it does not extrapolate a finite grid or finite computer test to an infinite claim. The computation establishes only the specific seven-peak lower bound at the specified cutoff and parameter.

## Relationship to prior work

Westerduin et al. (2023) applied an inclusive \(0.1\%\) relative-read abundance filter in metabarcoding and studied nonlocal sequences potentially caused by contamination. Drake et al. (2022) and Alberdi et al. (2018) describe the practical dependence of filtering outcomes on sequencing depth and read thresholds. Separately, Chernick and Liu (2002) and Gentile and Sambucini (2023) document sawtooth behavior of exact discrete-test power functions. Those statistical sawtooth phenomena are related in mechanism but concern changing deterministic sample size or test critical values, not the continuous Poissonized two-source relative-abundance event proven here. None of the specifically inspected works states the rare-fraction limit, the general arbitrarily-many-peaks theorem, or the exact \(0.1\%\) seven-peak certificate. Absence from these works is not a claim of globally established priority.

## Limitations

The model assumes independent Poisson reads, fixed composition with increasing depth and a single specific spurious taxon. It omits PCR stochasticity, index hopping, sample-level heterogeneity, filtering across multiple species, and correlated or overdispersed counts. Maxima of false-retention probability are not necessarily maxima of ecological loss or of optimal sequencing cost. The result does not recommend withholding additional sequencing or using any particular practical filter; replicate controls remain important. The finite seven-maxima certificate does not prove there are exactly seven maxima.

## References

- Westerduin, C., et al. (2023), *Exploring and validating observations of non-local species in eDNA samples*, Ecology and Evolution 13, e10612. First published October 14, 2023. https://doi.org/10.1002/ece3.10612
- Drake, L. E., et al. (2022), *An assessment of minimum sequence copy thresholds for identifying and reducing the prevalence of artefacts in dietary metabarcoding data*, Methods in Ecology and Evolution 13, 694–710. https://doi.org/10.1111/2041-210X.13780
- Alberdi, A., et al. (2018), *Scrutinizing key steps for reliable metabarcoding of environmental samples*, Methods in Ecology and Evolution 9, 134–147. https://doi.org/10.1111/2041-210X.12849
- Chernick, M. R., and Liu, C. Y. (2002), *The Saw-Toothed Behavior of Power Versus Sample Size and Software Solutions*, The American Statistician 56, 149–155. https://doi.org/10.1198/000313002317572835
- Gentile, S., and Sambucini, V. (2023), *Exact sample size determination for a single Poisson random sample*, Biometrical Journal 65, 2200183. https://doi.org/10.1002/bimj.202200183
