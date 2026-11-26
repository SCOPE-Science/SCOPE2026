---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

FAIL

The frozen hypotheses in RESULT.md line 29 literally permit at most one nonzero coefficient. Under that restriction |g|² is constant, the claimed supremum is R/r rather than (R/r)³, and Γ₂(δ) is 2δ rather than 2((1+δ)³−1). This contradicts both the Finding and the two-active-frequency witness. For the evident intended at-most-two-tone class the proof is sound: centered parity diagonalizes the two energies, and division by the radius cubed reduces to decreasing F±(z)=(z±sin z)/z³. On (0,π] the plus derivative is directly negative and the minus derivative is negative by the displayed half-angle identity; for z≥π both derivative numerators are bounded above by 3−z<0. The verified collision limit is the energy ratio of t−c, giving (R/r)³, unattained for positive gaps, with the shell normalization obtained by subtracting the inner integral and multiplying by two. Inspected VERIFICATION.md and verify_energy.py without executing the uploaded script. No repair is delivered: removing the contradictory sentence would fix the scope but leave the intended theorem fully covered as described below.

## originality

FAIL

The intended full statement is covered mathematically by a distinct indexed broader result's proof: its scalar strict inequality, normalized-energy claim, parity formula, and collision argument already give the one-dimensional interval case. The transfer profile is then arithmetic in the same ratio. This is full equivalent coverage in the available corpus, not a determination of which same-day record was written or posted first. The earlier fixed-gap and pointwise records and Zhang's general bounds alone would not justify this verdict.

## value

FAIL

The exact transfer profile is a meaningful quantity distinct from integrated pointwise bounds. But the strongest distinct indexed record already gives it for this natural interval case by taking the uniform interval law and removing the inner energy; the submitted record adds neither a new extremal regime nor any information beyond that implication. There is no separately useful unresolved invariant to preserve by editing the assumptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
