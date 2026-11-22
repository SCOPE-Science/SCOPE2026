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

# Reproducibility

Run `python3 verify.py` next to `RESULT.md`. The checker uses only Python 3 standard-library exact `Fraction` arithmetic. It enumerates all block states for up to three glued gadgets and tests their rational path-homology Betti ranks, acyclicity and the unchanged consecutive cover edges. It additionally checks five stages of intervals \([1,3)\) and \([2,4)\).

Expected output: `PASS: 39 exact rational-chain states and 5 timeline stages; arbitrary-parameter integral proof is in RESULT.md`.

The infinite-family claim, the integral saturation of the degree-two boundary lattice, and all inclusion-induced persistence maps are justified in `RESULT.md`; finite test output cannot establish these assertions. No independent audit is represented by this document.
