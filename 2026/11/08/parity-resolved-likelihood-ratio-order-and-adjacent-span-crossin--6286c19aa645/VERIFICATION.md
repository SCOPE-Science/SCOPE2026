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

The included `verify.py` is a standalone standard-library Python 3 program. It enumerates all perfect matchings of the non-distinguished endpoints for every permitted span when \(2\le n\le7\) and compares the resulting counts with the closed formula. Additional exact rational calculations test normalized distributions, means, likelihood ratios, tail domination, and adjacent-span tail reversals for \(3\le n\le41\). One replay passed **24,290 exact assertions**.

Command: `python3 verify.py`.

The proof for arbitrary \(n\) rests instead on exhaustive symbolic matching counts and inequalities given in RESULT.md. Finite enumeration and rational tests are diagnostic; they are not a proof of infinitely many cases. This package contains no independent audit or formal prover certificate.
