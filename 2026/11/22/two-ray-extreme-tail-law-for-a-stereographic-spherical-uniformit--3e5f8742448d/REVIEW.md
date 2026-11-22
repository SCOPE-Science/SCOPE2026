# Scientific review

## Correctness — PASS

The exact one-pair law \(F_Z(z)=z^2/(1+z^2)\) follows from the uniform dot product of two uniform sphere points. The expectation \(\pi/2\) matches the source centering. Distinct pair variables are independent even with a common endpoint, by conditioning on that endpoint and invoking spherical rotation invariance. Each of the two singular ends has a sharp index-two tail, and simultaneous extremes of two different pairs cost \(O(x^{-4})\). A complete finite-sum one-large-pair argument gives the exact two-ray measure, from which all constants and moment thresholds follow. The explicit reproducibility code passes 64 supplementary checks. There is no claim of mutual independence of all pairs or of an infinite theorem based only on experiments.

## Originality — PASS, with residual historical risk

The 2024 source introduces the stereographic test, and explicitly recognizes infinite variance at sphere dimension two. Its inspected definitions, null asymptotics, power sections and proof appendix do not provide the fixed-sample upper/lower tail coefficients or joint two-ray law. The 2023 work by the same authors treats different bounded tuned kernels, so its moments do not dominate this singular-kernel result. The closest accessible historical claim about the same stereographic family concerns \(n\to\infty\) Gaussian normalization, not fixed \(n\) and an extreme threshold; neither implication direction supplies the new two-ray tail theorem. Relevant general U-statistic large-deviation work is not specific to this sphere kernel or its exact two-sided coefficients. No independent historical-priority certification is asserted.

## Value — PASS

The exact upper-tail constant yields a direct asymptotic calibration of extremely small null significance levels for a published test whose second moment is infinite. The negative extreme mechanism exists only for negative tuning parameters; positive extremes mix close and antipodal pair events in the explicit ratio \(1:a^2\) for positive tuning. Joint tails identify dependence of tests at different tunings, and the truncated-second-moment law quantifies how badly variance-based calibration depends on truncation. These are natural tail invariants of the original, practically motivated statistic, not arbitrary parameter slices or a restatement of infinite variance.

## Closest literature and limitations

Primary source: Fernández-de-Marcos and García-Portugués, *A stereographic test of spherical uniformity*, arXiv:2405.13531, 2024, Eq. (2), Sections 3--5 and Appendix. Nearby distinct kernels: the same authors, *On new omnibus tests of uniformity on the hypersphere*, arXiv:2304.04519, 2023. General setting: Bakhshizadeh, *Exponential tail bounds and Large Deviation Principle for Heavy-Tailed U-Statistics*, arXiv:2301.11563, 2023. Historical claims in broader regular variation remain a risk; neither a uniform growing-\(n\) bound nor exact finite-significance-level error is claimed. The result applies to independent, fully specified uniform sampling on \(\mathbb S^2\) only.

Self-review: passed. Independent audit: not yet performed.
