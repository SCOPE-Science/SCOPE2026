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

Run `python3 verify.py`. The checker requires only the Python 3 standard library and passed the following checks when run with the files in this package:

* Five symbolic rational-polynomial first-step identities for the five transient symmetry classes, including all absorbing transitions.
* Full thirty-state rational transition equations generated independently at five rational values of the weak-flip probability.
* Every labeled connected three-uniform hypergraph on three or four vertices (twelve cases) has a path from each nonconstant binary state to unanimity under the limiting strict-majority update.
* The five-vertex two-petal hypergraph has a nonunanimous closed communicating class in the limiting strict-majority dynamics.
* Derivative-sign coefficient inequality, exact sample expectations and sharp limiting coefficient.

The proof relies on finite-state Markov-chain theory, exact algebraic identities, and the explicit reachability argument, not simulations. The checks do not constitute independent audit or external formal certification. The available literature comparison does not exhaust inaccessible primary full texts.
