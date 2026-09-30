# Independent Audit — 2026-09-30

**Record:** `2026/09/19/self-similar-rate-largest-dihedral-bisection--ee1438dc8cb0`  
**Title:** A universal self-similar degeneration rate for largest-dihedral-angle bisection  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `8d175bc51ff70f503b1f93e8898f258b628d45c9`  
**Disposition:** **FAILED**

## Three-axis assessment

- **Correctness — PASS**: The limiting map has the stated unique fixed point τ, its derivative is −1/2, the b^2 forcing gives the filed second-order coefficient, and numerical iteration reproduces τ≈0.7835533375134631 and the quality-growth base 1/τ≈1.276237305265537.
- **Originality — FAIL**: The accepted earlier record `2026/09/18/lab-boundary-attractor-degeneration-rates--2604f6e90e43` is strictly stronger: it treats the full parameter family c∈(1/√2,1), proves the general cubic, the universal −1/2 multiplier, second-order law, continuum of rates, geometric asymptotics and angle-doubling relation, and then specializes explicitly to c=7/8 with the same numerical constants as this record.
- **Scientific value — FAIL**: As a standalone package this is only a specialization of an already accepted stronger result, so it adds no independent scientific content despite being correct and clearly presented.

## Independent checks

- Re-differentiated the limiting recurrence at the fixed point and recovered F0′(τ)=−1/2.
- Checked the b^2 Taylor forcing and asymptotic balance.
- Compared the complete current RESULT.md with the earlier general-c SCOPE RESULT.md.

## Findings

- The current record’s cubic 7τ^3−12τ^2+4=0 is exactly the c=7/8 specialization of 2cτ^3−3τ^2+1=0 in the earlier record.
- The filed K, inradius limit, quality ratio, amplitude C and limiting dihedral identity all appear in the earlier stronger record’s c=7/8 specialization.
- Independent symbolic/numerical checks confirm the formulas; duplication, not correctness, is decisive.

## Sources

- https://arxiv.org/abs/2609.18788 — Korotov–Michaud source of the LAB recurrence and coarse degeneration bounds.
- https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/09/18/lab-boundary-attractor-degeneration-rates--2604f6e90e43/RESULT.md — Earlier accepted stronger SCOPE theorem containing this record as the c=7/8 specialization.

## Limitations

- The failure is for originality and standalone value only; the formulas themselves check.
- No claim is made that the underlying Korotov–Michaud recurrence or degeneration phenomenon is unimportant.

Repository evidence was checked against current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the assigned source-tree SHA still matches the current record tree. GitHub was used only as read-only evidence; no repository writes were made.
