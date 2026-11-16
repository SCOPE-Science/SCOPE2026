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

The included `verify.py` is a standalone exact-integer checker. Run `python3 verify.py` in its own directory. It derives the admissible-word indicator directly, applies integer Walsh–Hadamard transforms, and independently checks singularity, all-frequency parity, the least positive magnitude, the all-negative witness, and each prescribed resonant sign assignment for the 140 pairs \(1\le n\le14\), \(1\le k\le10\). It also checks integer transfer identities for \(1\le k\le23\) at three resonant multiples and several nonresonant lengths. Its successful completion prints `CYCLIC_WINDOW_FOURIER_EXACT_PASS all-frequency cases=140 k=1..23 resonances`.

The infinite-parameter argument relies on the displayed finite-order transition and rank-one idempotent calculations, not on extrapolating the finite tests. The checker does not certify historical priority or constitute independent mathematical validation. No external packages or downloaded datasets are required.
