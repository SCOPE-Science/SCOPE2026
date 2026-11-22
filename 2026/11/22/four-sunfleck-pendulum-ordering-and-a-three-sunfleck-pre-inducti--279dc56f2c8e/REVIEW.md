# Scientific assessment

## Correctness — PASS

The theorem's exact domain consists of positive light and shade rates, positive unequal lightfleck durations, a common positive dark gap, and initial induction in the closed unit interval for three lightflecks or exactly zero for four. Integrating one lightfleck yields the stated affine map and carbon deficit. Three signed permutation exchanges eliminate four competing orders and produce a unique critical initial induction \(s=qa\), including both tie regimes. For four pulses the finite polynomial \(Q\) is obtained by unrolling the recurrence, and strictly signed transpositions force the two smaller durations to the ends and the two larger durations to the center; reversal is an exact symmetry. The standalone rational test suite checked 124005 assertions. General correctness rests on the proof, not on finite enumerations.

## Originality — PASS (qualified historical priority)

The closest published model literature treats experimentally measured photosynthetic induction and lightfleck utilization (Jackson et al. 1991; Pons et al. 1992), dynamic carbon-gain acclimation (Retkute et al. 2015), multi-layer canopy sunflecks (Durand et al. 2022), and genotype-specific memory (Burgess et al. 2023). The inspected 2022 and 2023 full articles discuss responses to duration, frequency, intensity, and entrainment, but do not supply a theorem for the exact permutation of the same fixed multiset of different-length lightflecks under equal dark gaps. OEIS A101986 provides the related adjacent-product pendulum pattern; it does not state the finite-\(q\) nonadjacent-product optimization or the initial-induction switch. Indexed searches returned no covering statement in the inspected result summaries. The earlier 1991/1992 full texts and the 2015 full text were not all materially accessible; abstract-level evidence cannot rule out their contents. Generic rearrangement methods remain a priority risk.

## Value — PASS

The theorem answers a natural finite scheduling question motivated by induction-memory loss under repeated canopy lightflecks. Three pulses are the first count at which order matters from a completely uninduced state; four are the first count producing a nontrivial two-element interior block. The exact three-pulse phase boundary demonstrates that even a small pre-induced fraction can change the globally optimal order, while the four-pulse pendulum structure is universal across all positive time scales and nonidentical durations. This classification is useful as a benchmark for evaluating more physiologically detailed dynamic photosynthesis models and distinguishes fixed-total-light patterning from simple pulse frequency comparisons. It is not an empirical yield recommendation, and the theorem does not cover five or more pulses.

## Closest literature and scientific limits

See the links and statement-level discussion in RESULT.md. Relevant original studies include https://doi.org/10.1104/pp.95.2.498, https://doi.org/10.1111/j.1365-3040.1992.tb01491.x, https://doi.org/10.1093/jxb/erv055, https://doi.org/10.1111/nph.18222, and https://doi.org/10.3389/fpls.2023.1116367. The related adjacent-product entry is https://oeis.org/A101986. Remaining risks are historical theorem coverage in inaccessible older papers, classic rearrangement literature, and mismatches of the single-state kinetics to real leaves.

Self-review: passed. Independent audit: not yet performed.
