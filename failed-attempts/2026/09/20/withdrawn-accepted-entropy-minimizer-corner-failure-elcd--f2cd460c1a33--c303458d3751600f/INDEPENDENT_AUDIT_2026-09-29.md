# Independent audit — Exact entropy minimizer and normalization obstruction for ELCD interface states

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Source path:** `2026/09/20/entropy-minimizer-corner-failure-elcd--f2cd460c1a33`  
**Assigned and audited tree:** `51d3235f39a3cfd6f0ce65980fd363a6d65a1cba`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**FAILED.** The mathematics is retained, but this package fails independent validation as a separate research finding and should be relocated to the assigned failed-attempt path.

## Correctness

PASS. Direct differentiation gives the stated positive-definite Hessian, strict decrease in p, and the unique unconstrained top-edge minimizer rho0=e^{-1}p_+^{1/gamma}; clipping to [rho_-,rho_+] is therefore exact. Adding c rho shifts the stationary density by exp(-(gamma-1)c/gamma), so the normalization dependence is real. The Configuration-3 numerical values were independently recomputed: rho0=0.15567565441316625, corner entropy -0.5412116523249944, continuous minimum -0.5448647904460819, and the reported sound speeds agree. The source preprint abstract confirms entropy-minimizing interface-state selection, although its full PDF body could not be retrieved through the available web endpoint in this run.

## Originality

FAIL. The principal theorem package was already present in SCOPE two days earlier. `2026/09/18/elcd-entropy-rectangle-minimizer-gauge-dependence--f304c0de0856` gives the same closed-form rectangle minimizer, the same strict-interior counterexample family, the same affine/gauge dependence, an exact entropy-excess identity, and even a stronger identric-mean crossover analysis. `2026/09/19/entropy-gauge-corner-obstruction-elcd--8cb75d085d2d` independently repeats the same source-specific obstruction and adds a gauge-invariant diagnostic. The assigned September 20 record therefore does not establish an original finding; its benchmark-specific Configuration-3 calculation is only an illustration of already-published SCOPE results.

## Scientific value

FAIL as a separate validated finding. The mathematics remains useful, and the source-benchmark example is a concrete diagnostic, but the substantive theorem and structural objection had already been published in stronger form inside the same repository. The incremental benchmark substitution does not justify a third research record.

## Independent checks

- Re-derived the continuous minimizer and affine-normalization dependence from the entropy formula.
- Recomputed the Configuration-3 density, entropy values and sound-speed difference numerically.
- Compared the full assigned RESULT.md against the September 18 and September 19 SCOPE records; the earlier records contain the same core theorem and gauge obstruction, with additional formulas.
- Verified the specified failed-path destination and the new audit filenames are absent on current main.

## Literature and evidence

- https://arxiv.org/abs/2609.19838 — Chu, Herty and Kurganov (2026), motivating ELCD preprint; abstract confirms entropy-based interface-state selection.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/18/elcd-entropy-rectangle-minimizer-gauge-dependence--f304c0de0856 — Earlier SCOPE record containing the same exact minimizer and gauge-dependence theorem in stronger form.
- https://github.com/SCOPE-Science/SCOPE2026/tree/main/2026/09/19/entropy-gauge-corner-obstruction-elcd--8cb75d085d2d — Second earlier SCOPE record repeating the same obstruction and adding a gauge-invariant diagnostic.

## Limitations

- The source preprint body was not retrievable through the available arXiv PDF web endpoint during this audit; the audit does not claim to have read inaccessible pages.
- The failure is an originality/scientific-value disposition, not a mathematical-correctness rejection.
- The benchmark-specific Configuration-3 arithmetic may remain useful as example material after relocation, but it must not be presented as a new independent theorem.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `51d3235f39a3cfd6f0ce65980fd363a6d65a1cba`. The publication plan changes only independent-audit materials and `VERIFICATION.md`; the Lean and expert-attestation channels are preserved exactly as `unknown` with null evidence.

The assigned failed destination was checked and is vacant on current `main`; relocation is guarded on the unchanged source tree.
