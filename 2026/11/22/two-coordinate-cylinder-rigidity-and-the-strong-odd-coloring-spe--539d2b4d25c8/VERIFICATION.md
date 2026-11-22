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

The theorem is supported by a complete direct structural argument and two standalone finite verification programs.

- `verify_direct.py` enumerates all nonempty vertex masks of the Clebsch graph, tests adjacency and odd-neighborhood conditions, and counts unlabelled partitions by color number. It reports \(16\) singleton classes, \(40\) four-element classes and strong odd partition coefficients \(70,360,300,40,1\) at color counts \(4,7,10,13,16\).
- `verify_affine.cpp` independently generates forty two-coordinate cylinders and enumerates pairwise disjoint families of sizes \(0\) through \(4\), returning \(1,40,300,360,70\). It also confirms that all four-cylinder partitions use either one coordinate pair (ten cases) or two coordinate pairs (sixty cases).
- The direct program additionally enumerates \(1190\) ordinary proper four-color partitions, giving \(28560\) named proper four-colorings against \(1680\) named optimal strong odd colorings.

To replay, run `python3 verify_direct.py`, followed by `g++ -O2 -std=c++17 verify_affine.cpp -o verify_affine && ./verify_affine` in the directory containing these files. There are no external library dependencies. The finite checks are cross-checks; the proof of exhaustiveness is in `RESULT.md`. The results do not extend to other strongly regular graphs without additional arguments.
