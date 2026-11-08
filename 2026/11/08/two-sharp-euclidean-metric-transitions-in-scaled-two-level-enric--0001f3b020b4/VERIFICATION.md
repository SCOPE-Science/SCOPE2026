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

# Reproducibility and scope

The file `verify.py` is a standalone Python 3 exact-rational checker. Invoke it with `python3 verify.py`; its success line begins with `TWOLEVEL_ENRICHED_SCALED_CHECKS_PASSED`.

The code enumerates the explicit generating points of the two coordinate-cube hulls for \(m,n\in\{2,3,4\}\) under six integer scale pairs. It checks their support values, squared diameters, and sharp width inequalities over \(82{,}080\) nonzero ternary normals across \(54\) profiles. It also verifies explicit equality witnesses for both possible width branches and the chain partner.

The irrational boundary \(a=\sqrt2\,b\) is covered by the exact symbolic argument in `RESULT.md`, not the integer-scale finite checker. The proof is all-dimensional for the stated poset family; the checker cannot replace that proof. No independent mathematical audit has been performed.
