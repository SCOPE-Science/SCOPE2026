# Independent audit — Every prescribed finite Nakayama order detects the Auslander-Reiten conjecture

Audit date: 2026-10-01 (UTC) UTC

Final disposition: **FAILED**

## Correctness — PASS

The corner transfer is mathematically sound: the hypothesis on \({}_Ae\Gamma\) converts ARC vanishing into the Tor vanishing required for the induction Ext comparison, and induction reflects projectivity. Standard cyclic \(r\)-fold trivial extensions satisfy the corner hypothesis.

## Originality — FAIL

A separately published SCOPE record from the same date, “Tachikawa reduction at every Nakayama cycle length”, was inspected in full. It proves the same all-\(r\) TC2-to-ARC transfer using the same corner and Ext argument, proves exact Nakayama outer order \(r\), and derives the fixed-cycle-length universal equivalence. The present broader Frobenius exact-order formulation is mechanically implied by that equivalence together with universal ARC implying TC2 for every self-injective algebra.

### equivalent_formulations

Direct equivalent coverage.

Evidence: 524bc75cb4fb states the same all-r reduction and fixed-cycle equivalence.

### broader_coverage

The present broader Frobenius formulation is mechanically implied.

Evidence: The prior record covers every r>=2 and a sufficient self-injective test class.

### exact_database_or_table

Decisive exact database hit with full text inspected.

Evidence: Exact prior record 2026/9/18/SCOPE-tachikawa-reduction-every-nakayama-cycle-length--524bc75cb4fb.

### claim_vs_prior_implication

The principal claim is covered.

Evidence: Same corner, same Tor/Ext mechanism, same all-r transfer, same exact-order consequence.

## Source inspections


- **Tachikawa reduction at every Nakayama cycle length** (Resultary 2026/9/18/SCOPE-tachikawa-reduction-every-nakayama-cycle-length--524bc75cb4fb): DECISIVE_COVERAGE. Material read: complete RESULT.md. Evidence: Contains the same all-r corner/Ext transfer and fixed Nakayama cycle-length universal equivalence.

- **Tachikawa's second conjecture implies the Auslander-Reiten conjecture** (arXiv:2609.19172): PRIOR_R2_INGREDIENT. Material read: arXiv abstract; direct full-text and institutional fallback attempts failed. Evidence: Abstract proves the two-fold TC2-to-ARC reduction.


## Scientific value — FAIL

After that prior all-\(r\) reduction and fixed cycle-length test class, the remaining broader-class wording is a formal implication rather than a distinct motivated mathematical gap.

## Residual risks and limitations


- No correctness defect was found; rejection is scientific prior coverage, not an access failure.
