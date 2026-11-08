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

Run `python3 verify.py` using Python 3.9+ and the standard library. The recorded output is `verification_output.txt`. The code constructs translated supports, replays parallel binary firing until the first repeated configuration, enumerates all edges and triangles, verifies free-edge collapse certificates and surviving graph components, and independently evaluates simplicial boundary ranks over the field of two elements for smaller cases. It computes the predicted homotopy invariants from the theorem and checks agreement in all cases.

The verifier checks all 9,139 normalized supports with cycle length from 3 through 39. A subset of 1,140 supports is compared with direct sandpile dynamics. A subset of 816 supports is checked by mod-two matrix reduction. The proof in `RESULT.md` is required for the unrestricted assertion and for integral coefficients; mod-two checks cannot by themselves detect odd torsion, while the explicit graph collapses prove integral torsion-freeness.

Limits: This verification does not assess publication priority, does not independently audit the mathematical proof, and does not test cycles beyond length 39. The proof does not depend on extrapolation beyond this bound.
