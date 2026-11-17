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

# Verification
The exact finite certificate consists of `enumerate_orders.cpp`, `verify_c10.py`, and `gradients.txt`; `verification_output.txt` records the actual local replay. All three are independently embedded files of this finding.

Run from their common directory:
```
g++ -O2 -std=c++17 enumerate_orders.cpp -o enumerate_orders
./enumerate_orders regenerated_gradients.txt
python3 verify_c10.py regenerated_gradients.txt
```
The first program enumerates all 3,628,800 injective orderings of graph vertices. The second enumerates all noncyclic orientations and checks equality of the generated gradient sets. It then constructs all nonempty simplicial faces, performs the exact specified greedy pairing, checks every reversed Hasse edge by global topological sort, computes the signed integral Morse degree matrix, and independently evaluates the original mod-two simplicial homology.

Observed: 1,021 distinct gradients; 6,480 nonempty faces; 3,238 pairs; one critical zero-cell, one critical four-cell, two critical five-cells; 31,840 Hasse covers; 6,480 vertices removed in acyclicity sort; integer Morse boundary \((0\ \ 0)\); reduced mod-two Betti numbers one in degree four and two in degree five. Terminal marker: `FULL_STRONG_C10_WEDGE_PASS`.

The code is a complete finite verification for the specified object, not a proof of an infinite family and not an independent third-party audit. The homotopy inference additionally invokes Forman's discrete-Morse theorem and the degree classification \(\pi_4(S^4)\cong\mathbb Z\). The precomputed gradients file is checked against independently regenerated gradients before it is used.
