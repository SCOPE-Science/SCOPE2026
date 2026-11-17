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

The exact source `verify.py` is included in the same package. Executing it on standard Python 3 enumerates every clique from all 32768 vertex subsets. The first finite trace computation sums oriented fixed-face signs, including the empty face; the second groups vertices into cycles of each automorphism, independently sums over invariant unions, and checks equality for all thirty elements. It checks the predicted trace values and the dimension of the representation.

The returned face vector, complete character arrays and success marker are in `verification_output.txt`. Those are finite certificates for the character formula together with the cited published theorem of rational homology concentration. The calculations alone do not prove the cited homotopy equivalence or any family beyond the 15-cycle.
