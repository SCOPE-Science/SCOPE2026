---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and limits

The derivation is analytic: substitute the two three-by-three skew-symmetric matrices into the worst-case margin against each pure opponent, minimize the affine group-weight expression at its interval endpoints, and maximize the lower envelope after showing that any asymmetry incurs a strict penalty. Check both full-radius boundary equalities and the strictly positive critical-radius conditions.

Run `python robust_lottery_verify.py` from the directory containing the extracted files. The checker evaluates 625 exact rational choices of four parameters by independently enumerating feasible linear-program vertices and comparing optimal values with the analytic envelope; it also recomputes margins from three concrete strict-ballot profiles and tests the rational critical radius. Expected output: `PASS: 625 exact rational LP/analytic comparisons; 3 exact ballot profiles; radius switch 1/5`.

Finite parameter enumeration is corroboration, not proof for all positive real margins. No external proof certification or independent scientific audit has been performed.
