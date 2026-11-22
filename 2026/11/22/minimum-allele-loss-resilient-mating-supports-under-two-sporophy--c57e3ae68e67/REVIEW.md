# Scientific review of the allele-loss-resilient mating-support theorem

## Correctness (PASS)

The donor-to-recipient compatibility predicate is explicit and asymmetric only for the pollen-dominant model. The genotype coverage lower bound follows because each type uses two allele labels. Three- and four-label impossibility boundaries are proved by the number of remaining labels; all four-label DOMCOD supports are characterized by the three triple restrictions. At five labels, deleting an allele from any three-edge covering cohort leaves at most one edge; a four-edge path provides the upper bound. For COD, after any deletion the four surviving labels need a perfect matching, implying degree at least two; the five-cycle is uniquely extremal up to relabeling. Explicit disjoint-edge constructions work for every larger even and odd label count. Finite exhaustive checks on up to six labels and construction tests through sixty reinforce the proof without asserting infinite computation.

## Originality (PASS, qualified)

The biological SSIcod/SSIdomcod phenotype models themselves are established in Schierup, Vekemans and Christiansen (1997) and the dominance-selection analysis of Schoen and Busch (2009). Thrall and colleagues (2014) simulate mate limitation and allelic richness. None of the inspected substantive later primary texts states the exact worst-case post-allele-deletion minimum genotype-support classification. The full 1997 article could not be read; residual priority risk remains. The five-cycle COD characterization is **known factor-critical matching theory**, not asserted novel by itself. The claimed distinction is the integrated classification under the same biological removal rule, notably the four-allele DOMCOD possibility and its complete three-support extremal family. No search result alone establishes novelty.

## Value (PASS)

The number of distinct compatible diploid S-locus genotype types is an interpretable discrete diversity budget. A conservation-motivated worst-case loss of a single S-allele motivates the test independently of the mathematics, and the boundary between absolute failure (codominance at four labels), five required types (pollen dominance at four), and four-vs-five at five labels is structural rather than an arbitrary slice. For six or more alleles the simple covering bound becomes attainable, explaining exactly where dominance ceases to help this criterion. No population persistence or empirical breeding guarantee is inferred.

## Sources, risks and verification status

Sources: Schierup et al., *Genetics* 147 (1997), DOI 10.1093/genetics/147.2.835 (bibliography and abstract; full text unavailable); Schoen and Busch, *Evolution* 63 (2009), DOI 10.1111/j.1558-5646.2009.00686.x (substantial accessible full text); Thrall et al., *Ecology and Evolution* 4 (2014), DOI 10.1002/ece3.963 (full open-access paper); classical factor-critical graph theory (known codominant reduction). The main risks are uninspected older full texts and an idealized shared pollen hierarchy. See `AUDIT.json` for implication comparisons and source-inspection scopes.

Self-review: passed. Independent audit: not yet performed.
