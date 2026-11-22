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

Run `python3 verify_honeycomb_symmetry.py` alongside this file with standard Python 3; the exact output is `verification_output.txt`. The standalone code constructs all 50 plane-partition facets, all 41 lozenge labels and 2,517,787 nonempty faces. It checks a complete ordered-pivot discrete-Morse matching with one zero-dimensional and two four-dimensional critical cells. It verifies the geometric group action, calculates Lefschetz traces from vertex-orbit complexes and independently from the signed fixed original simplices.

The proof uses a standard tiling–plane-partition bijection and the ordered-pivot acyclicity argument, so the executable finite enumeration alone is not being treated as an infinite theorem. The asserted classification is limited to this one finite graph. Independent third-party audit has not been performed.
