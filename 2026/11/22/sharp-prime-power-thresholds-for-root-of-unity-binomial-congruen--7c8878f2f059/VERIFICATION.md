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

# Verification evidence

The supplied `check_miska_band.py` was executed with Python 3 and passed all assertions. For primes 5, 7, 11, 13, 17, 19, it verified the predicted leading residue for 72 parameter pairs (66 inside the claimed range), plus six direct full-product calculations. The direct test cases were (5,6,4), (5,6,5), (5,8,4), (5,9,4), (7,8,4), and (7,12,4) in the order (prime, root count, exponent). The exact outputs for their intermediate degrees and leading residues were respectively (550,2), (2750,2), (500,4), (525,4), (2156,3), and (2058,6).

The complete proof is the exact valuation lower bound, the nonzero finite-field coefficient at the constructed witness, and the Pascal finite-difference implication. Enumeration is not used to infer a universal theorem. No independent audit or separate external certification has been performed.
