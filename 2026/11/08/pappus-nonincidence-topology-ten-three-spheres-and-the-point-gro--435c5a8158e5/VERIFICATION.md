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

# Verification details

The code `run_verification.py` is standalone Python standard-library code. It explicitly specifies the 18-vertex Pappus graph, verifies a bipartition-exchanging graph automorphism and the incidence triple system, constructs both components by two independently programmed face predicates, and checks the asserted face vectors.

For each component, two deterministic toggle-order matchings are checked, pairing 143 faces and leaving exactly one ordinary critical vertex and ten critical three-simplices. Every one of 1,080 covering relations is oriented and subjected to topological sorting to check acyclicity. The dimension pattern yields the integral homotopy wedge without invoking a field computation. Degree-wise mod-two simplicial boundary ranks corroborate the Betti numbers, but mod-two ranks alone are not used to establish integral torsion-freeness.

The script then enumerates all permutations of nine points, retaining precisely those that preserve the incidence triple set. For all 108 such maps, it computes signed fixed simplices and derives the exact homology character via the Lefschetz trace formula. It checks zero invariant dimension by character averaging.

Execute `python run_verification.py`; the exact recorded output is `verification_output.txt`. These finite checks are exhaustive relative to the explicitly defined graph and complex. They do not certify broader configuration families, exhaustive novelty or external independent validation.
