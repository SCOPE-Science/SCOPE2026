# Independent Audit — 2026-09-30

**Record:** `2026/09/19/second-order-tail-trichotomy-weighted-porous-medium--17326eed1bba`  
**Title:** Second-order tail trichotomy for weighted porous-medium self-similarity  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `e04315afaff6b057d04a08e31a82fb3244e12f85`  
**Disposition:** **FAILED**

## Three-axis assessment

- **Correctness — PASS**: The exponent ordering, universal forced coefficient, resonant logarithmic coefficient, free-mode regime, and harmonic cancellation all rederive correctly from the profile ODE and the source center-manifold rates.
- **Originality — FAIL**: The same repository already contains the accepted record `2026/09/19/far-field-resonance-weighted-porous-medium--7d98f252f0ca`, which states the same three-regime theorem with the same threshold m=2p-1, the same coefficients after notation changes, the same profile-dependent free mode, and the same harmonic exceptional surface. The present record therefore does not supply an independent new finding.
- **Scientific value — FAIL**: Although mathematically sound, the package is redundant as a standalone citable finding because its substantive theorem is already preserved in an accepted, independently audited SCOPE record that is at least as strong and includes the same mechanism.

## Independent checks

- Re-derived the relative-error linearization and resonance coefficient independently.
- Checked the current Iagar–Munteanu v1 source for the leading tail and the two stable far-field rates.
- Compared the complete filed theorem line-by-line with the earlier accepted SCOPE record.

## Findings

- Direct algebra gives δ=D/(p−1), h=D/(m−p), and βδ−1=(m−2p+1)/(p−1).
- Substitution yields B*=(p−1)c*^(m−1)λ(λ−N+2)/(2p−1−m) and at resonance B_log=d/β, exactly as filed.
- The earlier accepted record `far-field-resonance-weighted-porous-medium--7d98f252f0ca` contains the same theorem and additionally states the eventual side of approach in the forced regime.

## Sources

- https://arxiv.org/abs/2609.20397 — Current v1 source for the common leading tail and center-manifold rates.
- https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/09/19/far-field-resonance-weighted-porous-medium--7d98f252f0ca/RESULT.md — Earlier accepted SCOPE record containing the same second-order trichotomy and coefficients.

## Limitations

- The failure is about originality and standalone value, not mathematical correctness.
- Older homogeneous absorption literature remains a background originality risk but is not needed for this failure decision because repository-level duplication is decisive.

Repository evidence was checked against current main commit `eff2c6312cec5b0dee5115e5f42211a853092dfb`; the assigned source-tree SHA still matches the current record tree. GitHub was used only as read-only evidence; no repository writes were made.
