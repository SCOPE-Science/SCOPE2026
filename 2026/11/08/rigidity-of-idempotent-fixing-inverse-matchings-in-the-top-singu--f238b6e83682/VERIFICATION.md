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

# Verification of the coatom matching

Run `python3 verify.py` with Python 3.9 or newer and no third-party packages. `verification_output.txt` is the expected stdout from a complete execution. All groupings are over genuine order-preserving transformations on \([n]\); multiplication is implemented as function composition, not through the theorem's inverse condition.

The checker tests every ordered pair of coatom transformations for \(n=4,5,6,7,8,9,10\). It checks actual mutual-inverse compositions against the claimed index criterion, tests all specified partners and their involution identities, verifies fixed idempotents, counts two-cycles, and confirms chain-reflection equivariance. In addition it enumerates **all** perfect matchings of the nonidempotent bipartite inverse relation using exact integer dynamic programming for \(n=4,5,6,7,8\), recovering precisely one each time.

The output reports the number of ordered inverse pairs, which includes loops and both orientations of each nonloop edge. The exhaustive dynamic program checks only the displayed finite parameter values. The mathematical proof of uniqueness for every \(n\ge4\) is the finite-set coordinate-sum argument in `RESULT.md`; finite checks are independent corroboration, not an infinite proof.

No external mathematical verification, proof-assistant certification, or independent audit is claimed.
