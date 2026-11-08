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

# Verification and reproducibility

Run `python3 artifacts/verify.py` using Python 3.10 or later. The self-contained script imports only the Python standard library. It enumerates every partition of each integer from 3 through 22, independently constructs the full graph by indexed row transfers and distinct-value transfers, compares their adjacency exactly, and performs breadth-first component and membership tests for the induced support-two graph. For integers from 23 through 150 it independently enumerates all two-size partitions from their multiplicities and verifies the closed family, component equality, cardinality, and disconnection witness.

A successful replay prints `VERIFY_OK` after the checks. The finite tests corroborate the infinite theorem; the mathematical justification is the exhaustive donor–recipient case argument in `RESULT.md`. There is no claim of independent mathematical certification, completeness of the historical literature search, or characterization of components other than the distinguished one.
