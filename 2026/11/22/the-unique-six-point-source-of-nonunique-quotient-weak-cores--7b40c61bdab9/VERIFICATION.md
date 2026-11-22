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

# Reproducibility and limits

Run `python3 check_weak_core_threshold.py` with a standard Python 3 installation. No external packages, paper downloads, network calls, or private input paths are required.

The checker enumerates all transitive upper-triangular binary partial orders on \(1\) through \(6\) vertices, reduces beat points in each small source, constructs the exact final-topology quotient preorder for all pair identifications at six points, and canonicalizes sources under all vertex permutations. All assertions and the terminal `PASS` were checked on the embedded script. It checks completeness of the six-point combinatorial classification, while the separate spanning-tree argument in the result proves weak equivalence of the two extremal quotient maps. Exhaustiveness is for the stated six-point domain only; finite experiments on larger spaces are not evidence of an infinite classification. Independent mathematical audit has not been performed.
