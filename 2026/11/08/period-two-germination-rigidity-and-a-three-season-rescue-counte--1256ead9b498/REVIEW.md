# Self-review

## Correctness: PASS

The two-cohort recurrence, chronological product, trace, determinant, and two endpoint factorizations were reconstructed. The comparison point \(L=a\max\{b,s\}\) lies strictly to the right of the characteristic parabola's vertex because the trace is convex and has both endpoint values below \(2L\). The signs of the factorizations certify the entire parameter domain, including boundary equality \(s=b\) and both pure policies. The three-season example was independently multiplied using rational arithmetic: both endpoint spectra lie below one; the mixed spectrum lies above one. `verify.py` passed symbolic identities and 1,235 exact-rational comparisons.

## Originality: PASS within inspected evidence, with priority risk

Brown–Venable (1986), pp. 33–34, optimize a scalar mean of logarithms across random year types, not the age-two periodic matrix product. Rees–Long (1992) study stochastic annual persistence in another framework. Rees (1994) treats a distinct stage-structured density-dependent invasion model, derives constant-environment conditions, and uses numerical simulations for stochastic environments; its pp. 44–50 do not state an exact period-two Floquet switch. The age-specific germination work of Valleriani–Tielbörger (2006) and correlated-yield work of Valleriani (2006) are close enough to warrant special priority caution, but their accessible abstracts do not assert this exact deterministic Floquet cutoff. Verin (2018), supplementary Text S3, examines much longer banking durations and seasonal periods numerically. No result implying both the all-parameter period-two theorem and three-season rescue was identified in the inspected materials or mathematical database searches. Full source examination is incomplete; priority should be independently checked before publication.

## Value: PASS

The two-age model is the minimal age structure that distinguishes obligatory second-opportunity germination from indefinitely renewable dormancy. A complete, parameter-uniform threshold at the **poor-season**, not average, fecundity has ecological interpretation. More importantly, the exact three-season witness demonstrates genuinely positive growth from a mixed strategy while both pure strategies decline, proving that the period-two bang–bang conclusion does not persist under the smallest longer cycle. The claim is limited to a tractable baseline model rather than asserted as a general conservation prescription.

## Closest literature and limitations

Sources: Brown and Venable (1986), DOI 10.1086/284465 (full text pp. 33–34); Rees and Long (1992) (available repository PDF); Rees (1994), DOI 10.1086/285660 (full repository text, especially pp. 44–50); Tielbörger and Valleriani (2005), DOI 10.1111/j.0030-1299.2005.14041.x (abstract); Valleriani and Tielbörger (2006), DOI 10.1016/j.tpb.2006.02.003 (abstract only); Valleriani (2006), DOI 10.1016/j.tpb.2006.07.008 (abstract only); Verin (2018), supplementary Text S3 (thesis text). No claim of an independently exhaustive history check is made. The theorem excludes density dependence, climate-adaptive decisions, and seed ages beyond two opportunities.

Self-review: passed. Independent audit: not yet performed.
