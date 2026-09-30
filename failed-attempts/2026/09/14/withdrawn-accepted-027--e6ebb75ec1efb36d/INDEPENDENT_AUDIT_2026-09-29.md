# Independent Audit — 2026/09/14/027

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `07f0bcef6f2e9a3db1ee2725827d85c5c9be4aac`  
**Audited current source tree:** `07f0bcef6f2e9a3db1ee2725827d85c5c9be4aac`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** failed

The current `main` directory tree SHA exactly matches the assignment tree SHA, and the designated failed destination was verified absent.

## Correctness — FAIL

FAIL. The claimed universal O(δ) convergence rate is not implied by the stated hypotheses. They assume only α(δ)→α0, with no O(δ) control. For an admissible real tangent direction v, α(δ)=α0+√δ v still satisfies the hypothesis; because the limiting theta reconstruction is nonconstant in phase, at a point where the directional derivative is nonzero the field error is generically Θ(√δ), contradicting sup_K|uδ−u0|≤C(K)δ. Independently, the branch conditions E2,E3→Es and |E2−E3|∼δ allow their midpoint to drift as √δ, e.g. E2=Es+√δ+δ/2 and E3=Es+√δ−δ/2, so the asserted O(δ) period/phase expansions do not follow either. The archived scripts use arbitrary toy period matrices and a proxy 4 atan|theta-ratio|, not the actual sine-Gordon Baker–Akhiezer family, and therefore do not repair the missing hypotheses.

## Originality — FAIL

FAIL AS A VALIDATED CLAIM. Qualitative soliton-on-cnoidal and nodal finite-gap degeneration mechanisms are established in the literature, while the record's purported new contribution is the quantitative O(δ) theorem and exhaustive σ-classification. That quantitative theorem is false under the record's own assumptions, so no original validated result survives in the stated form.

## Scientific value — FAIL

FAIL. A corrected theorem could be valuable, but it would need explicit rate assumptions on the divisor phase and degenerating branch-point data, plus a genuine sine-Gordon reconstruction estimate. As archived, the central rate statement overclaims what the assumptions and artifacts support, so the package cannot be retained as a validated finding.

## Independent checks

- constructed a √δ divisor-phase perturbation allowed by α(δ)→α0
- constructed a √δ midpoint drift with gap size exactly δ satisfying the stated branch assumptions
- inspected both numerical scripts and verified they are toy theta/proxy calculations rather than the claimed spectral family
- checked current record tree equals the assigned tree and failed destination is vacant

## Limitations

- The decisive correctness failure is internal to the theorem statement and does not depend on establishing historical priority.
- A narrower theorem with quantitative O(δ) hypotheses may be salvageable, but supplying and proving that theorem would be a substantive new research package rather than a guarded repair of the present claim.
- Open-access sources were sufficient; Oxford Download was not needed.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/14/027
- https://arxiv.org/abs/nlin/0410065
- https://arxiv.org/abs/2210.01350

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain exactly as previously recorded.
