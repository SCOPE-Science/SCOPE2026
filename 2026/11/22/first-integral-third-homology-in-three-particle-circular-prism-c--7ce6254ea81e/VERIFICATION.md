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

# Computation and proof checks

Run `python3 verify_prism_top3.py` (Python 3.10+). All cells and signed generators are constructed from the defining graphs, without downloaded input data. The checker enumerates 432, 1296, 2880 and 5400 three-cells respectively for circumferences 3–6; computes all columns of the boundary over F2; obtains nullities 0,0,0,2; checks two 512-cell signed product three-tori as full integral cycles; and verifies a determinant-one 2x2 coordinate minor.

These finite checks prove the upper bound on rational top homology for each of the four cases. The two explicit integral generators and coordinate unimodularity separately prove the lower bound and integral primitivity. They do not compute lower-degree integral homology and cannot be extrapolated beyond n=6.

The topological equivalence with the continuous configuration space uses the Prue–Scrimshaw sufficiently subdivided graph condition with three particles and one subdivision per original prism edge. No independent audit has been performed.
