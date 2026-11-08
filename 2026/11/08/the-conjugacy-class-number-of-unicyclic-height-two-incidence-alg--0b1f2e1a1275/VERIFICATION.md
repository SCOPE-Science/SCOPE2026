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

# Reproducible verification

Run `python verify.py` with Python 3.9 or later and the standard library. A successful run prints `VERIFY_OK`. The program constructs unit-group conjugacy orbits using direct conjugation by generators, with explicit finite-field operations over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\), then makes a separate commuting-pair calculation from componentwise multiplication. It checks multiple attachment configurations and field orders, including characteristic two. On the prepared package, 27 checks passed: eleven exhaustive direct orbit counts and sixteen commuting-pair counts. The program does not depend on any other package or on a separate data file.

The proof of the universal theorem is mathematical, not computational. Finite computations do not establish all dimensions or all prime powers. The formula applies only to connected unicyclic bipartite comparability graphs of height-two posets.
