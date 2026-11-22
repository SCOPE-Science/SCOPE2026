# Review: A unique sequencing-depth sign reversal of co-detection under coupled occupancy

## Correctness — PASS
The full proof reconstructs the likelihood, inclusion–exclusion covariance and strictly decreasing exponential quotient for all allowed positive parameters. The critical strict inequalities are elementary and are displayed explicitly. The unique crossing, exact tie at two reads, high-prevalence limit and Poisson-thinning alternative follow without numerical extrapolation. The independent exact enumeration and checker confirm the formulas on tested instances; they are not substitutes for the proof.

## Originality — PASS on inspected evidence
Courtaillac et al. (2024, DOI 10.1002/edn3.70023) motivate fixed-effort metabarcoding design but give no co-detection sign theorem. Fukaya et al. (2021, DOI 10.1111/2041-210X.13732) provide a general multinomial occupancy observation model, which is a relevant broader starting model but not a published conclusion about all-depth pairwise detection covariance. Boshuizen and te Beest (2022) and Kurtz et al. (2015) explain compositional correlation artifacts without this precise one-crossing regime.

The nearest indexed published co-detection theorem, *An irreversible co-detection sign switch under incidence-based rarefaction* (2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-an-irreversible-co-detection-sign-switch-under-incidence-based-r--37418c61ba8c), applies to uniform **without-replacement sampling of distinct sites** from fixed incidence sets, with the reverse possible sign order. It does not subsume the **within-site fixed multinomial-read budget mixed over random occupancy**. Searches cannot exhaust historical literature; priority is therefore provisional.

## Value — PASS
Fixed read totals induce negative short-depth co-detection even when biological occupancy is perfectly positively associated. The exact crossing quantifies when interpretation becomes reliable, while the Poissonization result isolates the dependence mechanism rather than simply restating that compositions may mislead. The narrowly specified setting provides a reproducible benchmark for broader occupancy-detection work.

## Limits
Results concern population covariances under idealized shared Bernoulli occupancy, constant category proportions, zero false positives and iid reads. No finite-site sample power, real-world sequencing protocol, or causal interaction is inferred. Full texts of key direct sources were inspected, but no historical priority guarantee or external independent audit is claimed.

Self-review: passed. Independent audit: not yet performed.
