# Independent mathematical audit — 2026-10-01

## Final claim

Hadamard-order amplification and onset bounds for Kusner counterexamples

## Correctness — PASS

PASS. The arbitrary-Hadamard transfer uses only normalized-column data and the fact that two distinct Hadamard rows agree and differ in exactly half the positions; the four pair types therefore reproduce Xiong's distance equations. The threshold condition \(m>1/\Delta(p)\) yields a solution to the scalar equation by continuity. Independent symbolic differentiation reproduces \(c_4=\sqrt2\log(1+\sqrt2)-	frac74\log2=0.0334429143005567\ldots\) and \(8/c_4=239.2136022627\ldots\). The dense-Hadamard-order argument then gives the stated near-\(4\) upper scale, while Swanepoel's published stability inequality gives the lower scale by contraposition and asymptotic inversion. The large-\(p\) expansion of the same explicit \(\Delta(p)\) is consistent with the displayed linear upper bound. These arguments prove construction-dependent upper bounds, not optimality of the true threshold.

## Originality — FAIL

FAIL. A published 17 September record, one day earlier, already states and proves the same arbitrary-Hadamard transfer for Xiong's construction and the same sharp near-\(4\) template scale with the identical constant \(c=\sqrt2\log(1+\sqrt2)-	frac74\log2\), including the resulting global upper bound. The 18 September record's added lower estimate is a direct contraposition/asymptotic inversion of Swanepoel's existing stability interval, and its large-\(p\) estimate is a routine expansion of the already-defined threshold function. Those additions do not create an original final claim under the required implication standard.

### Equivalent formulations

Its \(D_{m XH}(4+arepsilon)\) formulation is equivalent to the 18 September theorem's near-\(4\) Hadamard-order upper construction.

### Broader coverage

Together with the 17 September SCOPE result, these sources cover the construction and make the added lower-side inversion and threshold expansions routine.

### Exact database or table

This is decisive exact prior coverage, not merely a failed novelty search.

### Claim versus prior implication

The final package is either verbatim-equivalent to the earlier record or mechanically implied by earlier formulas; originality therefore fails.

## Scientific value — PASS

PASS. Quantifying the onset dimension at the now-sharp \(p=4\) transition is mathematically well motivated, and combining construction upper bounds with stability lower bounds is useful. The value failure is not the reason for rejection: the problem and estimates are worthwhile. The record fails because the core Hadamard amplification and leading near-\(4\) constant were already published, while the remaining additions are straightforward consequences of prior formulas.

## Source inspections

- **Hadamard densification and critical dimension scaling in Xiong's Kusner counterexamples** (Resultary/2026, 2026/9/17/SCOPE-hadamard-densification-kusner-critical-scaling--43b27c183a43): DIRECT_PRIOR_COVERAGE. Complete published RESULT.md, including Theorems 1–3, construction, critical expansion and template asymptotic. It proves arbitrary normalized Hadamard orders work and gives \(D_{XH}(4+arepsilon)=(8/c+o(1))/arepsilon\) with the identical constant \(c\), plus the same global upper bound.
- **Kusner's conjecture is false for p>4** (arXiv:2609.14794): BASE_CONSTRUCTION. Primary arXiv abstract. Xiong constructs \(8m\) equilateral points in dimension \(8m-2\) for every \(p>4\).
- **Equilateral Sets and a Schütte Theorem for the 4-norm** (DOI 10.4153/CMB-2013-031-0): IMPLIES_LOWER_SIDE_BY_ROUTINE_INVERSION. Published theorem context and the explicit stability inequality as cited and algebraically inverted in the record. The lower onset estimate is the direct contraposition and asymptotic inversion of the published stability interval.

## Checked sources and replay paths

- Assigned RESULT.md and exact frozen tree
- Independent symbolic differentiation of the near-4 constant
- Resultary semantic search
- Complete earlier 17 September published Resultary record
- Xiong primary arXiv abstract
- Swanepoel stability result

## Residual risks

- No correctness defect was found; rejection is solely scientific originality.
- The large-\(p\) expansion was not found verbatim in the earlier 17 September record, but it is a routine expansion of the same explicit threshold and is insufficient to rescue the covered final claim.

## Disposition

**failed**
