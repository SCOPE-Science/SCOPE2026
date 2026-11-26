---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Frozen Finding 4 fails as stated: take q=2, p=(1,1), d=p. All assumptions hold, σ=0, D_p=I and K_p=0, so 0 is an eigenvalue of infinite multiplicity, not a purely a.c. spectrum without eigenvalues. The corrected RESULT.md and SLOGAN.txt in /workspace/repairs/3 treat that case explicitly and say the residue coefficient has rank two only when σ>0. Re-audit: the exact block entry is i(p_r−p_s)H_a/q with a=(r+s+1)/q; H_a−H is a rank-one integral whose trace-norm majorant behaves as O(x^(a−1)+1) near 0 and O(1) near 1. The coefficient maps the normalized constant and centered vectors by ±iσ as stated and kills their orthogonal complement. The tail summability implies trace-class difference by the bound on each Hilbert column, and Weyl and Kato–Rosenblum give the essential and a.c. claims. At N=qM, the correct residue projection is I⊗P_M; interlacing changes counts by fewer than q for other N. The scalar law applies at t/(πσ) in the normalized Hilbert model: each sign has coefficient π⁻² arcosh(πσ/t) below the edge, zero at or above it. The min–max count sandwich at t±δ has error at most ∥Q_M∥₁/δ; threshold continuity includes the edge. For σ=0 the entire perturbed commutator is trace class (not necessarily zero), so its finite counts are bounded. Complex conjugation gives exact sign pairing. The q=2 shifted block has a=1 and no remainder; nonzero scale preserves pure a.c. spectrum, while zero scale gives the zero operator. These analytic checks, not finite diagnostics, verify the corrected claim.

## originality

PASS

For the repaired claim, the genuinely distinct content is the periodic diagonal commutator's variance-only channel and signed counting classification, with a trace-class weighted-tail criterion. Neither the scalar Hilbert input nor broader scalar Hankel theorems state that operator identification. The corrected constant case is a boundary clarification, not claimed as a new scientific result.

## value

PASS

The repaired theorem identifies one scalar statistic of arbitrary periodic patterns that fixes three nontrivial infinite-dimensional and finite-section spectral invariants, with an explicit stability class and mechanism. It does not claim to classify singular spectrum or general-period outliers. The degenerate-case correction does not remove the substantive nonconstant family or its stability theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
