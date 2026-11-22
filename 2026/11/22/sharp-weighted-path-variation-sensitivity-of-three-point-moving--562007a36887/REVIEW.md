# Review of the weighted moving-MAD variation theorem

## Correctness — PASS

The exact three-sample MAD identity \(\min(|d_i|,|d_{i+1}|,|d_i+d_{i+1}|)\) follows by sorting the triple. Each local map is separately \(1\)-Lipschitz in its two first-difference variables. Changing one input edge affects only two neighboring output entries, giving the weighted column bound; telescoping across input edges gives the global two-input inequality. Strict finite rational windows \((-3/2,1,-3)\), with the middle first difference increased by \(1/10\), make the two output changes equal and opposite, saturating all three weighted contributions. Boundary-edge witnesses saturate the remaining ratios. No assumptions about genericity or numerical approximation enter the proof. The standalone rational checker corroborates every class of witness and the elementary algebra.

## Originality — PASS, qualified

The original MAD and Hampel-filter papers define and use this robust scale, but the 1993 paper studies scale efficiency, breakdown and influence functions, and the full 2016 Hampel paper addresses outlier-replacement filters, root/implosion sequences, and data-replication weighting. Neither computes an adjacent-variation two-input modulus with separately weighted input and output edges. Indexed running-median, morphology and sliding-standard-deviation results address different signal transforms and do not state an implication yielding this MAD coefficient; comparison was by operator definition and claim implication, not by title or matching sample count. Relevant full text inspected: author-hosted Rousseeuw–Croux (1993) and open Pearson et al. (2016). The 2015 conference record was inspected for date and provenance, while the longer 2016 article was read for the overlapping scientific content. Residual risk: unindexed older equivalent formulas and a conference-version detail not independently read in full.

## Value — PASS

The output is the local scale used to determine robust Hampel thresholds. While MAD reduces the effect of extreme observations in its usual statistical sense, that robustness does not imply nonexpansivity of the *difference between two moving-scale outputs* in discrete variation. The complete formula gives a sharp worst-case perturbation budget under arbitrary positive input/output edge weights, a precise nonexpansivity test and concrete attaining signals. The dimension onset and saturation at fourfold amplification are properties of the local scale itself, not of the median-replacement filter. This resolves a natural stability question for the smallest genuine moving-MAD window, rather than an arbitrarily selected numerical slice. The theorem makes no claim for longer windows or other filtering operators.

## Sources and residual risks

Primary sources: Rousseeuw–Croux (1993), DOI 10.1080/01621459.1993.10476408; Pearson–Neuvo–Astola–Gabbouj (2016), DOI 10.1186/s13634-016-0383-6; EUSIPCO 2015 version DOI 10.5281/zenodo.35878. The full 2016 article's sections on local MAD, weighted replication, case studies and conclusions and the 1993 paper's MAD definition and scale-estimation analysis were inspected. The 2015 conference PDF download was inaccessible through the textual retrieval route; the 2016 expanded full article is available. Published summaries of finite-window morphology and running median stability were checked as potentially stronger coverage and found to concern other operators. Residual risk is limited to unlocated historical equivalent statements, not a missing step in the direct proof.

Self-review: passed. Independent audit: not yet performed.
