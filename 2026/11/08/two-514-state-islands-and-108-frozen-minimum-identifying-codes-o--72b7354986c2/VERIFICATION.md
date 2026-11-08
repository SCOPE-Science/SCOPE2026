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

Run `python3 checker_lcf.py` and `python3 checker_affine.py` from a directory containing the two scripts, with a standard Python 3.9+ installation. No third-party dependencies, input data, or downloads are required. Each prints a JSON dictionary and stops with an assertion error if the target census, component sizes, edge counts, radii or diameters differ. Their exact outputs at preparation time are supplied as `output_lcf.json` and `output_affine.json`.

`checker_lcf.py` builds the 18-vertex LCF graph, tests all 262144 possible vertex subsets by nonzero-distinct trace signatures, builds all legal one-token jumps and neighbor-restricted slides on its 1028 nine-vertex minimum codes, and computes all component eccentricities by breadth-first search from every state.

`checker_affine.py` independently constructs a point-line incidence graph of the affine plane of order three after deletion of one parallel class. Its code test is the equivalent 171-set hitting requirement rather than signature equality. It enumerates all 155382 sets of cardinality at most nine, verifies an explicit graph isomorphism to the LCF model, reconstructs both movement graphs and computes the same exact shortest-path profiles.

This is an exhaustive **finite** certificate. Neither program claims to establish a result for graphs beyond the Pappus graph. Execution outputs must be interpreted together with the stated edge construction, identification condition and transition definitions; output logs alone do not prove a broader statement. No outside assessment was performed.
