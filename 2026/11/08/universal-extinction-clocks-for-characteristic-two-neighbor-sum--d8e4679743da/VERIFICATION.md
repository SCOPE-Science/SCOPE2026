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

# Verification and reproducibility
The proof uses the characteristic-two identities \(DU=0\), \(U^{h+1}=D^{h+1}=0\), and \(A^k=\sum_{a+b=k}U^aD^b\); these statements justify the infinite family, while the two programs test concrete instances only.

Run `python3 -m pip install -r requirements.txt` followed by `python3 verify_graph.py` and `python3 verify_operators.py` with Python 3.10 or newer (Python with `int.bit_count`). `verify_graph.py` independently constructs unrooted eligible trees and directly evolves parity adjacency matrices. It checks the exact times of all basis impulses, top-two matrix ranks, the deepest-level matrix formula, and all binary initial states for orders up to nine. It includes 409 nonisomorphic eligible trees of sizes through 15 and 30 explicit combs, 439 graph cases in total. `verify_operators.py` constructs 250 independent irregular even-child rooted trees, uses separately implemented operators, verifies \(DU=0\), individual impulse survival, and the word-expansion formula. The recorded outputs are `verification_graph.txt` and `verification_operators.txt`.

Verified maximum observed orders: 15 for enumerated nonisomorphic graphs, 213 for irregular generated trees; comb heights through 30 are structurally checked and comb heights through 7 dynamically checked. No finite test verifies arbitrary heights or unbounded graph sizes; proof steps are supplied in RESULT.md. Characteristic-two extension fields are covered algebraically, while the executable tests use \(\mathbb F_2\).
