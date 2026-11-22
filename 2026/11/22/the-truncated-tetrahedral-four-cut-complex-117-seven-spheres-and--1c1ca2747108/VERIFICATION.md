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

# Verification record

Execute `python3 verify.py` in the same directory as `CERTIFICATE.json`. A successful replay with Python 3 standard-library methods is included in `verification_output.txt`.

The verifier reconstructs the graph from 12 ordered pairs, checks 18 edges, classifies all 495 induced quadruples, enumerates the full cut complex and Alexander dual, verifies the complete six-skeleton, replays 48 individually tested elementary collapse pairs, and tests an eleven-edge spanning tree plus 55 precise triangle relations that kill all fundamental-group generators. It then computes every signed simplex Lefschetz trace for all 24 elements of the full tetrahedral symmetry group, checks the class character \((117,7,1,3,1)\) and the integral irreducible multiplicities \((8,4,16,13,9)\).

The finite certificate supports the combinatorial input, including simple connectivity and the signed action. Hurewicz, Alexander duality and Whitehead's theorem are explicitly invoked in `RESULT.md` for the topological conclusion; no independent external formal verification, independent audit or computational certification of an infinite claim is asserted.
