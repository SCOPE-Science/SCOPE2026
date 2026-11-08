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

# Reproducibility and scope

The accompanying standalone `verify.py` uses Python's standard library and no downloaded input files. Invoke `python3 verify.py` from this directory. Its recorded stdout is `verification_output.txt`. The checker constructs every four-subset, tests the XOR-zero criterion for the fourteen affine planes, generates all 84 signed suspension cycles, checks their integer simplicial boundaries, checks five- and six-vertex induced subcomplexes, computes an exact 21-by-21 Bareiss determinant and enumerates all 1,344 affine permutations to verify orbit size 84.

The underlying proof uses the augmented simplex chain identity to establish integral rank and homology vanishing; the unimodular minor proves basis saturation. Matrix verification is exhaustive for this eight-vertex complex rather than a probabilistic computation. The verifier does not perform an independent formal proof or establish publication priority. The potentially relevant classical affine Steinberg-module monograph could not be read in full.
