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

# Verification of the exact two-part diameter law

The proof in `RESULT.md` is analytic for every integer ring size and real height in the stated domain. The central logical checks are (i) the exhaustive distance classes; (ii) nonbipartiteness of the union of the two maximal classes in the even case; (iii) the strict second-largest same-ring comparison; (iv) the explicit three-coloring at the tie; and (v) the odd-cycle obstruction within one ring for odd ring sizes. The parity of \(n\) matters at each step.

Run `python3 verify_antiprism.py` using only the Python 3 standard library. This independently builds 3D point coordinates and tests graph bipartiteness of strict and inclusive pair-distance threshold graphs, all pairwise Euclidean diameters and all predicted diameter-edge counts across 253 parameter configurations and 303,178 pairs. It also tests equality-height cases to numerical tolerance. Recorded output is provided in `verification_output.txt`. These finite computations are independent checks of special cases, not exhaustive validation of unbounded integers or real heights.
