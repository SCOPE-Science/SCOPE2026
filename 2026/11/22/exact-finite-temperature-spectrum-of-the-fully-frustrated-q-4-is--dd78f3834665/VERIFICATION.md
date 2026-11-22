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

The attached `verify_ising_q4.py` is a standalone Python 3 program with no external dependencies. Its main routine checks the full 16-by-16 signed adjacency against the Clifford identity, checks all 24 elementary square products, and computes the nine energy multiplicities by two independent complete finite algorithms: direct configuration-to-edge evaluation and two-layer 256-by-256 transfer enumeration. All integer coefficient assertions passed when the program was run on the packaged scientific code prior to handoff. No probabilistic simulations, machine-learning surrogates, or unproved infinite extrapolations are used. The limitations concern historical priority, physical scope, and absence of external independent audit—not missing finite computations.
