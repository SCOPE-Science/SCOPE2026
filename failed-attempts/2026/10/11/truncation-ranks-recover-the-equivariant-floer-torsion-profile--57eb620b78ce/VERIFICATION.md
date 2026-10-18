---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Huang Definition 1.1 models equivariant Borel Floer theory by a finite free complex C over the DVR R=F2[[q]]. Its truncated coefficient theory is C⊗R A_N with A_N=R/(q^N), not merely H(C)⊗A_N; thus the universal coefficient theorem contains both a tensor term and an adjacent Tor_1 term. For H(C)≈R^r⊕Σ_j R/(q^{a_j}), both tensor and Tor_1 of each torsion cyclic with A_N have F2-dimension min(a_j,N), while each free R summand contributes N. Therefore h_N=rN+2Σ_j min(N,a_j) and Δ_N=h_N-h_(N-1)=r+2#{j:a_j≥N}; Δ_N-Δ_(N+1)=2#{j:a_j=N}. The localized free rank r=2^(c-1) follows from the published equivariant branched-cover localization input in Huang introduction (for |L|=c). Increments are nonincreasing, have parity r and eventually r; the ungraded module type is reconstructed. This is correct finite-rank homological algebra for each based link and does not recover torsion grading, extension data, or a link-specific numerical spectrum.

## originality

FAIL

FAIL by mathematical implication rather than search silence: general PID/DVR universal coefficients plus elementary-divisor structure already imply every asserted truncation-length identity and the inversion formula for any finite free R-complex. Huang gives precisely the specialization to link Floer theory and its localization rank; the package supplies no nonstandard Floer application or independently computed torsion exponents.

## value

FAIL

FAIL. Although useful as an expository consistency check, the exact numerical formulas are a routine textbook universal-coefficient/elementary-divisor calculation, with no independent link-specific exponent computation, unexpected obstruction, sharpened bound or motivating mathematical gap beyond restating the generic DVR length function. In this form the claimed contribution does not cross the requested substantive-value bar, despite being correct and reproducible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
