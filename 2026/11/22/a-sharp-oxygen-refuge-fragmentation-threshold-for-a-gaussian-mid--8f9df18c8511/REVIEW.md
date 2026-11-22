# Scientific review: Gaussian oxygen-deficit viability bands

## Correctness — PASS

The explicit score and domain are fixed in the theorem. Direct differentiation produces the one-dimensional derivative factor \(a-\rho(a-x)e^{-x^2/2}\), whose Gaussian-weighted linear term has one negative maximum. Its two-root/no-root structure and the location of the right root relative to the surface prove both branches of the exact threshold. The derivative sign pattern establishes the complete positive-width superlevel-band classification on \([0,H]\), and local Taylor expansion and integration yield the fold coefficient. The included `CHECK.py` passed 25,814 supplementary assertion groups, including near-critical checks; sampling is not the continuum proof.

## Originality — PASS on inspected evidence

The 2024 Fröb et al. study already uses the metabolic index to identify potential aerobic habitat and abrupt changes, and Wishner et al. (2020) document upper and lower oxygen-minimum boundaries. Essington et al. (2022) explicitly report deep metabolic-index recovery. Thus neither the metric nor the physical possibility of layered habitats is new. Their inspected full texts do not derive the present Gaussian-profile finite-domain threshold or the sharp surface effect. Generic fold exponent laws are prior mathematical knowledge (see Maloney and Lacks, 2005/2006); the precise parameter threshold and coefficient are the subject of this result. No matching claim was identified in the accessible mathematical-record searches. Historical priority is provisional, particularly for unindexed analytical oxygen-profile literature.

## Value — PASS

The theorem gives a necessary-and-sufficient answer to a precise habitat-connectivity question: whether any physiological threshold could separate shallow and deeper viable depths, as the strength and depth of an oxygen-minimum profile vary. The surface correction is crucial when the minimum sits relatively close to the surface, the result is independent of the model bottom depth once that depth exceeds the oxygen centre, and the potentially misleading oxygen-core location differs from the metabolic bottleneck. The fold opening law quantifies sensitivity near the onset. These conclusions are model benchmarks, not field predictions or statements about biological dispersal.

## Closest literature and limitations

- Fröb et al., *Earth's Future* (2024), https://doi.org/10.1029/2023EF004141 — source of the metabolic-index habitat framing; full methodology/results/discussion inspected; no Gaussian-depth classification found.
- Wishner et al., *Biogeosciences* (2020), https://doi.org/10.5194/bg-17-2315-2020 — observed upper and lower oxycline and species distribution shifts; full article inspected; distinct empirical focus.
- Essington et al., *Ecography* (2022), https://doi.org/10.1111/ecog.06249 — spatial breakpoint models and deep metabolic-index recovery, not the stated exact phase diagram.
- Maloney and Lacks, *Physical Review E* (2006), https://arxiv.org/abs/cond-mat/0508534 — generic \(3/2\) fold/barrier exponent is prior knowledge.

The oxygen profile, exponential thermal correction, and fixed viability cutoff are assumptions; no physiological calibration, empirical validation, claim of broad mathematical uniqueness, or independent audit is supplied.

Self-review: passed. Independent audit: not yet performed.
