# Self-review

## Correctness — PASS

The exact primitive is a strictly increasing global coordinate for each positive source-dominated Monod flow. The divided-difference identity for the relative speeds proves one strict displacement maximum because the product of the current concentration and its forward flow increases from zero to infinity. The translation increment therefore has at most one sign change and yields the unique positive length threshold, all inlet endpoints, and strict crossover motion. Boundary assumptions \(s>k>0\), \(K>L>0\), \(a,b>0\), and \(x\ge0\) are maintained throughout; the equality case is separately checked. The standard-library checker was replayed at the actual package path and passed 2,331 supplementary assertions, which do not replace the analytic proof.

## Originality — PASS (provisional)

The closest fully read published mathematical result is the finite-step, no-source reach-ordering classification, whose assumptions expressly exclude exact continuous plug-flow kinetics. Another fully read three-stage stormwater result has a linear wash-off law and a cumulative-exposure objective. The recoverable earlier source-driven two-reach result uses discrete maps and a between-reach concentration jump, not a continuous source in both reaches. Covino et al. (2010) supply empirical serial-uptake motivation, while O’Brien et al. (2007) investigate nitrogen turnover but report no corresponding exact order theorem. Possible stronger historical rearrangement theorems or inaccessible reactor texts remain priority risks, so the assessment is a best-knowledge literature comparison and does not certify unconditional novelty.

## Value — PASS

The claim gives a sharp, unique and monotone phase boundary for an idealized but motivated spatially successive saturating-uptake setting. It clarifies when reach ordering depends on incoming concentration and when sufficiently long high-affinity downstream treatment eliminates that dependence. Its qualitative conclusion contrasts with linear constant-supply wash-off and parameter-only finite-step sorting. The result is not field-validated and does not cover the lower-source regime or heterogeneous flow hydraulics.

## Limits and closest literature

Sources: O’Brien et al. (2007), doi:10.1007/s10533-007-9073-7; Covino et al. (2010), doi:10.1029/2009JG001263; the published finite-step reach-ordering and three-stage stormwater exposure results linked in RESULT.md. Plausibly relevant older membrane reactor optimization and newer bioreactor zone-volume texts were only accessible as abstracts. Historical priority is therefore provisional; no external expert audit is asserted.

Self-review: passed. Independent audit: not yet performed.
