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

The included `verify.py` uses only the Python standard library. Execute `python3 verify.py` in the directory containing it; the observed output is `VERIFIED 3955 exact assertions, 1286 weight multisets`.

The script independently computes lattice-point counts by a signed-coordinate recurrence, compares small cases with direct coordinate enumeration, examines root-of-unity pole orders, and tests minimum quasiperiods by finite differences on all integer residue classes for a finite set of parameters. It verifies the unique sharp weight multisets through the denominator \(32\) and their exact binomial counts for dilations through \(70\). All numerical assertions use exact integer arithmetic. The analytic proof in RESULT.md, not these finite checks, establishes the unrestricted theorem.

The code is a finite reproducibility check, not an independent audit or a formal proof of the infinite-dimensional assertions. General historical priority also remains provisional.
