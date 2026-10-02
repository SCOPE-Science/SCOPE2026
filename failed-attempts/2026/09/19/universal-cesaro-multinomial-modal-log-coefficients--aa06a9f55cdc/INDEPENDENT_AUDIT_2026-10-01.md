# Independent mathematical audit — 2026-10-01

## Final claim assessed

For rationally independent multinomial probabilities, every fixed logarithmic local-expansion coefficient at the actual multinomial mode has a universal Cesaro mean given by the displayed Bernoulli--Stirling formula; more generally polynomial functions of the modal displacement converge in Cesaro mean to expectations under Janson’s Jefferson seat-excess limit law.

## Correctness — PASS

The proof reconstructs correctly. Elezovic identifies the mode with Jefferson allocation and supplies the Bernoulli-polynomial coefficient formula. Janson supplies the random-house-size Jefferson seat-excess limit, and bounded displacement upgrades weak convergence to polynomial moment convergence. Independently expanding e to the power w((e to the power w-1)/w) to the power (n-2) for n=2..5 and m=0..5 reproduced the stated Stirling coefficient identity exactly. The p_i to the power (k+1) factor cancels p_i to the power (-k), leaving sum p_i=1.

## Originality — FAIL

The final theorem is already contained in earlier published SCOPE records. The 2026-09-18 record proves the polynomial transfer law and all-order universal logarithmic means, and the earlier 2026-09-19 record gives the same Bernoulli--Stirling closed form. This later record’s own RESULT acknowledges that chronology. It is therefore covered, not independently original.

## Value — FAIL

The theorem is mathematically useful, but this record does not fill an unknown gap: its final claim is a later restatement of already published SCOPE results. The alternate verifier is reproducibility evidence, not a new mathematical contribution under the value bar.

## Source inspections and risks

- **Multinomial probabilities near the mode: integer modes and the complete local expansion** (arXiv:2609.20229): Full arXiv HTML introduction, mode theorem, and coefficient context; primary abstract/HTML. Assessment: COVERING_MACHINERY.
- **Asymptotic bias of some election methods** (arXiv:1110.6369): Primary arXiv abstract and paper metadata; exact limit representation cross-checked against the audited derivation and earlier SCOPE proof. Assessment: COVERING_MACHINERY.
- **On-slice Cesaro laws for multinomial modes** (SCOPE 2026/09/18/multinomial-mode-cesaro-universality--a66b1067c370): Complete RESULT.md from the audited Git snapshot. Assessment: COVERING.
- **Universal Cesaro law for all logarithmic coefficients at multinomial modes** (SCOPE 2026/09/19/multinomial-mode-cesaro-log-coefficients--69879bbdb548): Complete RESULT.md from the audited Git snapshot. Assessment: COVERING.

Residual risks: No correctness issue was found; originality failure is decisive from exact earlier repository records.
