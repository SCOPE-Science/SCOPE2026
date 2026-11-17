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

The update rule, vertex indexing, exact state count, and boundary conventions are defined in `RESULT.md`. Run `python3 verify_direct.py` and `python3 verify_faces.py` with Python 3 standard-library modules only. Their complete expected outputs are `direct_output.txt` and `face_output.txt`.

`verify_direct.py` constructs each graph edge from one corner coordinate and its corresponding face, verifies 24 edges and degrees eight times three and six times four, computes all \(2^{14}\) updates, and checks the pointwise identity \(F^7=F^5\) together with a sharp witness against \(F^6=F^4\). It checks period, first-entry histogram, whole-basin partitions, per-orbit basin sizes, the 48-element coordinate symmetry group and its geometric orbit classes.

`verify_faces.py` uses a separate six-bit face-symbol construction. It enumerates every one of the \(64^2\) ordered pairs of face words satisfying necessary and sufficient two-period equations. It independently iterates all \(256\cdot64\) mixed-radix configurations for first-entry and basin statistics and checks orbit-size histograms. Its calculations share neither transition tables nor imported function definitions with the direct checker.

The symbolic equations and 14-bit exhaustive loop provide finite proofs of these *finite* claims. They do not settle corresponding dynamics on other polyhedra; all time and orbit quantifiers refer only to the specified graph. No external, independent audit or formal proof assistant has been performed.
