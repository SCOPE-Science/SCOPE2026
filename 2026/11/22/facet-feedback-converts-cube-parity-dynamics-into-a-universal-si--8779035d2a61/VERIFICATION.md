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

The mathematical proof derives the block operator directly from the simultaneous update and computes its rational canonical form. Direct successor enumeration and independent bit-matrix rank checks provide finite, reproducible cross-checks only.

Run `python verify_direct.py` to reproduce `verify_direct_output.txt`. This exhaustively checks all initial states for dimensions one through four over the binary field, and dimensions one through three over the field of four elements. Run `python verify_algebra.py` to reproduce `verify_algebra_output.txt`; this constructs binary matrices independently and checks dimensions one through eight, including the proposed order, ranks and polynomial identities.

The checks do not exhaust every dimension or field, and do not constitute an independent audit. The all-size statement is supported by the tensor decomposition and rank argument in RESULT.md.
