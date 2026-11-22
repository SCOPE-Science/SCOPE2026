# Scientific review: species-labelled single-catch retrieval time

## Correctness

**PASS.** The proof establishes the categorical probabilities of a stationary, independent Poisson competing-capture process, explicitly separates total intensity from conditional species proportions, computes the full-rank Fisher determinant in the original per-species rate coordinates, and uses a strictly decreasing logarithmic derivative to prove one global positive-duration optimum for every integer \(k\ge3\). The stationary equation has exactly one root above two. The monotone dependence on \(k\), logarithmic expansion, and timestamp-coarsening ratio follow from exact equations and not extrapolated numerical experiments. The independent finite-difference checker passes 1,283 deterministic diagnostics in its current packaged form.

## Originality

**PASS relative to the inspected evidence, with residual priority risk.** Wu–Huang (2014) give related competing-risk Fisher-information matrices and numerical, multi-interval D-optimal criteria, principally for two risks. Their Section VII suggests general risk counts, and is the strongest potential overlap; it does not explicitly prove the specific single-terminal-category global optimum, strict all-\(k\) monotonicity, its logarithmic asymptotics, or the universal coarsening ratio. Distiller–Borchers (2015) use first-capture times in spatially explicit trapping and do not optimize the reduced observation's retrieval time. Zhou et al. (2026) use general multinomial competing-risk information but select the number of pre-specified inspection periods and treatment allocation, rather than proving this free continuous all-species retrieval-time law. A published two-visit occupancy design result concerns a different state/observation process and does not imply the first-capture categorical objective. These statement-and-implication distinctions are substantive; numerical absence of a matching title alone would not establish novelty. General optimal-design treatises and less accessible cause-specific inspection papers remain historical-priority risks.

## Value

**PASS.** Species-labelled single-catch stations face a concrete tension: long exposure reveals categorical species identity with high probability but almost eliminates the empty-station observations needed to estimate the total encounter rate. This result resolves that tension sharply for all species counts. The increasing dimensionless optimum and its logarithmic growth, the asymptotic one-in-\(k\) empty fraction, and the exact time-coarsening determinant penalty are interpretable benchmarks for low-information ecological instruments. The fact is not merely a fitted numerical design, arbitrary parameter slice, or a reparameterized familiar bound. The model is stylized; it does not recommend real-world trap durations without cost, spatial and animal-behavior calibration.

## Scientific limitations

The design is local in unknown rates, uses independent stationary Poisson encounters, correctly identified first-capture species, fixed station count, and no operation cost. Timestamp information, variable site intensities, species misclassification, finite observation caps, dependence among stations and recapture are outside the theorem. The contribution may have precursors in broader one-shot reliability or interval-censoring design literature. No independent expert validation has occurred.

Self-review: passed. Independent audit: not yet performed.
