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

## Verification performed

Run `python3 check.py` in the package directory, using Python 3.10 or newer and no third-party dependencies. The checker independently enumerates acyclic orientations by topological sorting and by nested column sets, uses an exact-integer butterfly Walsh transform, and evaluates the thirteen-product formula independently. It verifies the frequency histogram in `spectrum_n2_n5.csv` for \(2\le n\le5\), including all 37,440 frequencies and their Parseval energy. It also verifies the two symbolic witness substitutions and the zero-frequency formula with arbitrary-precision integers through \(n=100\).

## What the computation does not establish

Finite exhaustive verification does not prove the all-order claim. The proof in `RESULT.md` supplies the chain inclusion-exclusion identity, reversal-pair congruence, explicit parity-dependent multiplier witnesses, and the spectral norm deductions for every integer \(n\ge2\). Independent mathematical verification has not been performed.
