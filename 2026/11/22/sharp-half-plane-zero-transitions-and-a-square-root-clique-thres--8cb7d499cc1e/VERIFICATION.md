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

# Verification

Run `python3 verify_cycle_clique.py` from the extracted package directory. The program checks all independence-set masks on cycles of orders \(3\) through \(12\); confirms the derived coefficient list; computes the phase crossings numerically and independently checks sample right-half-plane counts with exact rational Routh arrays; verifies the two integer cases straddling the eight-cycle threshold; and checks representative large-cycle square-root scales. Zero-pivot Routh sample parameters are excluded explicitly rather than treated as a proof of any sign.

The theorem for all \(n\), all real \(u>0\), and the asymptotic constant are proved analytically in `RESULT.md`. Numerical root checks cannot establish those infinite claims. The phase comparisons are numerical, and the exact Routh comparisons are limited to reported sample instances. The exact boundary value is derived symbolically in the proof; no certified interval arithmetic is claimed. No independent scientific audit has been performed.
