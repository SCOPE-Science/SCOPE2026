# Scientific review: two-sex occupancy and redundant mating sites

## Correctness — PASS

The independent male/female Poisson split yields an exact binomial law for the number of sites containing both sexes. Existence of an integer optimizer follows from a finite positive success chance at every feasible \(k\) and the vanishing success bound \(\Pr(W_k\ge r)\le\theta(1-\theta)L^2/(rk)\). An exact expression for the no-success factor separates the minority-sex exponent from a site-count-dependent correction. In the balanced case, localization by a lower bound and a unique scalar minimization gives the \(\sqrt L\) law. In the unbalanced case, complementary exponential-penalty and missing-site lower bounds localize the optimum on the scale \(L/\log L\). The proof explicitly covers all integer maximizers, finite-parameter boundary conditions and the distinct \(r=1\) case. A standard-library checker independently evaluates binomial-tail recurrences and illustrative optimizing site counts. The limiting theorem is proved analytically; finite tests are supplementary.

## Originality — PASS on inspected evidence

The closest source is Cuddington et al., *Landmarking and strong Allee thresholds* (2015), https://doi.org/10.1007/s12080-015-0254-z. Its main body and combinatorial appendix treat male/female co-location, the exact number of matched individuals, and the effects of site number on mate-finding. That source covers the finite combinatorial foundation but does not present the new objective of guaranteeing \(r\ge2\) distinct two-sex sites and does not imply either optimal large-pressure scaling without further analysis. Chase et al., https://doi.org/10.1111/1365-2664.14326, experimentally test propagule pressure/Allee effects; Koontz et al., https://doi.org/10.1002/ece3.4226, examine temporal introduction number and size; neither establishes the stated mathematical law. Dupuis et al., https://doi.org/10.1239/jap/1175267167, give a colored-ball large-deviations principle for balls proportional to bins, whereas the optimizing limits here have per-site occupancy intensity diverging with total pressure. Mathematical priority remains provisional because uninspected extreme-tail and spatial mating-model literature may contain overlapping formulations.

## Value — PASS

Spatial distribution of founders creates a fundamental tradeoff: more distinct locations offer redundancy but separate potential mates. For a target of two or more independent mating-capable locations, the theorem provides a specific scale on which that tradeoff is optimized and exposes a sharp qualitative dependence on the sex ratio. The square-root versus nearly linear scaling is a structural distinction, not a routine finite parameter substitution. It is pertinent as an idealized null benchmark for mate limitation and distributed colonization, while remaining deliberately separate from ecological claims about actual reproduction or establishment.

## Boundaries and closest prior work

The strongest conceptual antecedent is Cuddington et al., 2015. The most relevant quantitative ecological motivation is Chase et al., first public manuscript 2022-11-01, which is within the source interval. All sites are assumed equivalent and free to maintain. A site containing both sexes is only *potentially* reproductive. The fixed bias asymptotic is not uniform in sex ratios approaching equality; this crossover and real-life habitat costs remain unproved. No human verification or field calibration has been performed.

Self-review: passed. Independent audit: not yet performed.
