# Review status

Independent mathematical audit completed on 2026-10-01 UTC.

Disposition: **failed**.

Correctness: **PASS**. The arbitrary-Hadamard transfer uses only normalized-column data and the fact that two distinct Hadamard rows agree and differ in exactly half the positions; the four pair types therefore reproduce Xiong's distance equations. The threshold condition \(m>1/\Delta(p)\) yields a solution to the scalar equation by continuity. Independent symbolic differentiation reproduces \(c_4=\sqrt2\log(1+\sqrt2)-	frac74\log2=0.0334429143005567\ldots\) and \(8/c_4=239.2136022627\ldots\). The dense-Hadamard-order argument then gives the stated near-\(4\) upper scale, while Swanepoel's published stability inequality gives the lower scale by contraposition and asymptotic inversion. The large-\(p\) expansion of the same explicit \(\Delta(p)\) is consistent with the displayed linear upper bound. These arguments prove construction-dependent upper bounds, not optimality of the true threshold.

Originality: **FAIL**. A published 17 September record, one day earlier, already states and proves the same arbitrary-Hadamard transfer for Xiong's construction and the same sharp near-\(4\) template scale with the identical constant \(c=\sqrt2\log(1+\sqrt2)-	frac74\log2\), including the resulting global upper bound. The 18 September record's added lower estimate is a direct contraposition/asymptotic inversion of Swanepoel's existing stability interval, and its large-\(p\) estimate is a routine expansion of the already-defined threshold function. Those additions do not create an original final claim under the required implication standard.

Scientific value: **PASS**. Quantifying the onset dimension at the now-sharp \(p=4\) transition is mathematically well motivated, and combining construction upper bounds with stability lower bounds is useful. The value failure is not the reason for rejection: the problem and estimates are worthwhile. The record fails because the core Hadamard amplification and leading near-\(4\) constant were already published, while the remaining additions are straightforward consequences of prior formulas.

Detailed evidence, source inspections, originality comparisons, checked sources and residual risks are in `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json`.

The original same-model review remains historical evidence and is not relabeled as independent.
