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
# Verification of finite two-read weight-three capacities

The accompanying `certificates.json` specifies every code and every clique class over lexicographically ordered triples of one-positions for each integer length \(3\le n\le32\). A full partition into cliques is an unconditional upper bound on the independence number; the corresponding independent code is a lower bound. The proof requires no trusted optimization solver.

Run `python3 verify_direct.py` and `python3 verify_structural.py` from the directory containing all three included artifacts. The first verifier passed all thirty lengths, covering 4960 vertices in its largest instance. The second passed direct-set versus alternating-interval graph comparison at all lengths 3–12 and selected larger independent-code checks at 13, 16, 20, 24, 28, 32. The direct verifier alone checks all pairs necessary for the entire certificate.

The matching piecewise cubic evaluations are proven only for length at most 32, since all those integers appear separately in the checked finite certificates. There is no proof for longer lengths. Independent external mathematical audit: not performed.
