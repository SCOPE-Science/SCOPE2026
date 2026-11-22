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

# Finite verification record

The supplied `verify.py` uses Python 3 standard library and reads `collapse_pairs.txt` from its own directory. It builds the Petersen graph independently of any certificate; checks all 1,024 subsets with both component/edge counting and union-find forestness; enumerates 785 nonempty forest faces, 120 label automorphisms, 23 face orbits and 15,255 barycentric chain orbits; checks all integral boundary-square identities; and replays 7,627 elementary collapses, testing each live free face. The terminal residual complex consists of one zero-cell.

The proof uses a standard finite simplicial quotient without inversions and the elementary CW-collapse theorem. The computation verifies the finite hypotheses, not a separate infinite generalization. Any independent mathematical audit has not yet been performed.
