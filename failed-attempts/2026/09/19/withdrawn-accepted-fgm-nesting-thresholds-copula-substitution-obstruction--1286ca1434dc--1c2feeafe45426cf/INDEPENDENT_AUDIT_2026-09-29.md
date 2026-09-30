# Independent Audit — 2026-09-29

**Record:** `2026/09/19/fgm-nesting-thresholds-copula-substitution-obstruction--1286ca1434dc`  
**Disposition:** **FAILED**

## Correctness

**PASS** — The mathematics stated in this record is correct. The Euler-operator identity follows from repeated differentiation through product blocks, and for FGM it reduces to the same density and exact admissibility interval as the companion record. The explicit (m,n,θ)=(2,1,1) value -35/64 and the quadratic entropy coefficient were independently recomputed.

## Originality

**FAIL** — The core research contribution is not original within the same SCOPE corpus: the companion record `2026/09/19/fgm-block-substitution-validity-and-entropy-failure--f5661be14848` contains the same exact FGM/product-block admissibility threshold, the same corrected density mechanism, the same source-specific closure obstruction, and a strictly stronger entropy theorem valid throughout the interior of the admissible window. The only material addition here is an Euler-operator packaging of the chain rule, which is elementary and does not rescue standalone originality.

## Scientific value

**FAIL** — As a standalone validated finding this package is dominated by the companion record: its principal threshold and counterexample are duplicated, while its local O(θ^2) entropy defect is weaker than the companion record's global strict monotonicity theorem. Retaining both as independent findings would overcount one mathematical contribution.

## Disposition rationale
The record is rejected as a separate validated finding because a stronger companion SCOPE record already contains the same core theorem and a stronger entropy result. This is not a claim that the displayed formulas are false. The complete package should be retained as a failed attempt for provenance rather than silently deleted.

## Evidence checked

- X. Lu, Copula Operad and Copula Entropy: https://arxiv.org/abs/2609.20512 — Current source whose unrestricted substitution claims are contradicted.
- Companion SCOPE record with stronger FGM result: https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/fgm-block-substitution-validity-and-entropy-failure--f5661be14848 — Same corpus record containing the same exact threshold and density obstruction plus a stronger global entropy theorem.

Repository evidence was read at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6` / source-check commit `253a0fe5d0217455660a277f9adb940030e567ad`. A later repository-head comparison through `eff2c6312cec5b0dee5115e5f42211a853092dfb` found no changes under this record path, so the assigned source-tree SHA `3607885569db6f52b15e0212d21e2abce2fef456` is the tree audited. GitHub was used only as read-only evidence.

## Limitations

- The formulas are mathematically correct; failure is on originality and standalone scientific value, not correctness.
- The companion record is treated as prior corpus evidence for curation; this does not assert an external historical priority result.

## Audit conclusion

This independent audit is scientifically complete on correctness, originality, and value. The package should be relocated atomically to its designated failed-attempt path, preserving the original evidence and adding a failure note.
