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

The mathematical proof establishes every dimension \(n\ge2\) by a finite-orbit model, an exhaustive *symbolic* square-support lemma, a common-one-skeleton gluing decomposition, and a homotopy-pushout splitting. The exact integral ranks follow from the cubical two-skeleton Euler characteristic and its simple connectivity, not numerical homology data.

Execute `python3 verify.py` with a standard Python 3 interpreter; the script has no third-party dependencies. It directly recomputes pairwise Hamming distances between all orbit representatives, enumerates every orbit-flag simplex for \(2\le n\le8\), and checks the equality with the square-block union. It independently computes complete mod-two boundary ranks and compares them with the claimed ranks. `verification_output.json` contains the actual replay output; the terminal status must be `WEIGHT_TWO_FIXED_SPACE_CHECKS_OK`.

A finite mod-two calculation alone cannot certify torsion-freeness, higher homotopy groups, or an infinite-parameter statement. Those claims are supported instead by the integral topological splitting in `RESULT.md`. The computational experiment is supplementary. No independent mathematical audit has been performed.
