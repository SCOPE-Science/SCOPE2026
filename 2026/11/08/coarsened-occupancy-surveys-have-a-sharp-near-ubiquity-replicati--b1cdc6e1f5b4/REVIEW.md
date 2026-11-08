# Scientific review

## Correctness — PASS

The model separates latent stable site occupancy from independent conditional per-visit misclassification. Exact Bernoulli likelihoods yield the OR information, variance coefficient, and the fixed-interior finite optimizer. The threshold \(1-p=(1-f)^2\) follows from the exponential growth/decay of the boundary information per unit effort; a uniform inequality handles equality. In the divergent regime, the two exponential terms in the exact variance have opposing monotonicities, forcing the optimizer into a bounded lattice window around \(\log(1/\varepsilon)/\log(b/a)\). This establishes both the full integer phase and its periodic leading coefficient, not only an observed numerical trend. Full-data information is bounded by information in the latent occupancy state for interior prevalence, but the boundary chi-squared information grows exponentially for all distinct detection rates. The independently implemented finite calculations passed 191 assertions. Limitation: only ideal fixed-rate independent surveys are proved.

## Originality — PASS within inspected sources; historical priority provisional

Clement (2016) studies numerical allocation of survey effort with false positives; Guillera-Arroita, Ridout and Morgan (2010) study occupancy replication with different observation assumptions; Ferguson, Conroy and Hepinstall-Cymerman (2015) study confirmation and heterogeneity; Royle and Link (2006) establish the detection-mixture model. Their inspected statements do not include the exact \(p>2f-f^2\) near-ubiquity design transition, integer-lattice law, and the sharply distinct behavior under full-history retention. Related semantic searches on archived mathematical findings likewise located no matching claim. The explicitly inaccessible McClish–Quade (1985) paper is a serious priority risk because it concerns repeated-test prevalence accuracy and cost. Its abstract was inspected, not its full text; it is not claimed to have been excluded by a complete source comparison. Exact model likelihoods and general information inequalities are pre-existing ingredients, not claimed contributions.

## Value — PASS

The precise question is motivated by actual occupancy protocols that trade the number of sites against repeated visits under false-positive and false-negative detections. The result distinguishes a biologically important high-occupancy boundary that is invisible in finite moderate-occupancy design tables and isolates when discarding visit histories changes even the qualitative optimal replication law. It supplies an exact benchmark and exposes the cost of one-bit reporting. The proof is not a prescription for a finite-budget survey with unknown error rates, persistent detection heterogeneity, or ecological state changes. A later analysis with calibrated field costs and parameter uncertainty would be needed for practical deployment.

## Closest literature and limits

- Royle and Link (2006): https://doi.org/10.1890/0012-9658(2006)87[835:GSOMAF]2.0.CO;2
- Guillera-Arroita, Ridout and Morgan (2010): https://doi.org/10.1111/j.2041-210X.2010.00017.x
- Ferguson, Conroy and Hepinstall-Cymerman (2015): https://doi.org/10.1111/2041-210X.12442
- Clement (2016): https://doi.org/10.1111/2041-210X.12617
- McClish and Quade (1985): https://doi.org/10.2307/2530645 — accessible abstract only, unresolved historical overlap risk.

Self-review: passed. Independent audit: not yet performed.
