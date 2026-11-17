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

The standard-library program `verify_petersen_full_quotient.py` exactly enumerates all fifteen Petersen graph edges, 331 nonempty matching faces, 120 symmetry permutations and the orbit-chain boundary matrices. It verifies a fourteen-edge spanning tree and triangle relations that kill all 61 other edge generators, then checks a fixed vertex for a transposition. The quotient chain complex has ranks (10,32,47,30,6) and undergoes 62 exact unit-boundary cancellations to a single degree-zero generator. Both the unreduced and reduced differentials square to zero.

Run `python3 verify_petersen_full_quotient.py` from this directory; `verification_petersen_output.txt` records the actual checked output. This is an exhaustive finite computation and an ordinary proof using Armstrong, Hurewicz and Whitehead; it does not certify independent verification or equivariant contractibility.
