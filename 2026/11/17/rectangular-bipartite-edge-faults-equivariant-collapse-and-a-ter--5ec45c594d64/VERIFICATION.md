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

The file `verify.py` is a standalone Python 3 program using only the standard library. From the graph definition it independently enumerates all faces, tests each domination step for every fault stage, deletes dominated vertices, reconstructs the exact join core, computes full reduced mod-two simplicial boundary ranks and checks Euler characteristics against the closed-form prediction.

The parameter triples are \((s,b,k)=(3,5,4),(4,5,4),(4,6,4),(4,6,5)\), with all \(0\le t\le b\), or 26 stages total. Run `python verify.py`; output is preserved in `verification_output.txt` and terminates in `RECTANGULAR_BLOCK_FINITE_CHECK_PASS`.

The test is finite, does not establish claims for infinitely many values, and does not by itself establish integral torsion or the complete homotopy type. Those results follow from the dominated-vertex retractions, the classical simplex-skeleton matching, and the integral exterior-power basis established in the proof.
