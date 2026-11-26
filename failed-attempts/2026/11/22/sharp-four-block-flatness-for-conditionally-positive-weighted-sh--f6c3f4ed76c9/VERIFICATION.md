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

PASS

The frozen statement is mathematically correct. Downsampling the positive second-difference measure with the factor t^κ(1+⋯+t^{p−1})² gives the second-difference moments for the block sequence. If q=d²≠1, the first three of these moments force zero variance at t^p=q. If q=1, the total mass is zero. The original measure can therefore have only the indicated positive atom (no positive atom in the unit case), and it can have a zero atom only for κ>0. Solving the resulting recurrence and matching the geometric subsequence eliminates the affine part in the nonunit case and the slope in the unit case. The equation at n=0 forces c≤1 and gives exactly the stated two-point Berger measure; κ=0 gives c=1. For sharpness, the two positive masses C(u−1)² and D(v−1)² have sum (q−1)² and first moment q(q−1)², so matching γ_0 and γ_p yields γ_{jp}=q^j for j≤3. The positive variance gives γ_{4p}>q⁴. The coefficient limits yield positivity and bounded consecutive ratios for each fixed p. This is an exact check, not a finite test.

## originality

FAIL

The closest distinct prior source does not state the arbitrary-length theorem verbatim, but both halves of the claimed extension follow from it by downsampling and rescaling. In particular its published sharpness witness, not just the p=1 sharpness assertion, transfers to every p. The new choice of coefficients is a different instance of the same two-atom construction, not a distinct sharpness result.

## value

FAIL

Sparse block measurements are a reasonable rigidity question, but the submitted exact threshold is a direct consequence of the published flatness theorem plus the positive moment representation, and its all-length optimality is already obtained by fractional rescaling of the published example. The separate coefficient family does not yield a new obstruction or another independent mathematical guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
