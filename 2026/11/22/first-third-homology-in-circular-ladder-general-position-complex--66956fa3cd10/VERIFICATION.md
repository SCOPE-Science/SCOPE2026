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

# Verification of the finite homology calculation

Execute `python3 verify.py` with any current Python 3 interpreter. Only Python standard-library modules are used. The program reconstructs all graph distances using the exact Cartesian-product formula, enumerates all forbidden geodesic triples and then all nonempty vertex subsets for \(3\le n\le8\). It constructs integer signed boundaries in the canonical increasing vertex order, applies unit-pivot elimination over \(\mathbb Z\), and asserts that no nonunit residual survives. It asserts the complete face-vector and reduced-homology tables.

**Actual result:** the verifier completed with `PASS: complete face enumeration and primitive integer ranks for n=3..8`. The intermediate boundary-rank lists agree with an additional exact Smith-normal-form calculation. Unit-pivot reductions show each nonzero Smith factor is one, and hence no torsion appears.

**Limit:** Computational exhaustion covers only \(3\le n\le8\). No infinite-range theorem, quotient calculation, or independent audit is claimed.
