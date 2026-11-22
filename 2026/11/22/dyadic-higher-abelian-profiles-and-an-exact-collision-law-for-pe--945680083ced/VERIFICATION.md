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

# Computational and symbolic verification

The full proof is in `RESULT.md`; the supplied programs check independent finite instances and are not claimed as proofs for unbounded parameters.

Run `python3 verification/check_direct.py` to enumerate all rotations for substitution scales \(k=4,5,6,7,8,9\), compute every overlapping occurrence count through length three, and verify exact rational collision probabilities and all twelve context multiplicities. The required output terminates in `DIRECT_OK`.

Run `python3 verification/check_general.py` to compare complete overlapping \(\ell\)-Abelian signatures and circular bridges with actual length-\(m\) factors for \(\ell=2,3,4,5,6\) and both of the tested substitution scales for each order. The output terminates in `GENERAL_OK`.

Independently checked corner conditions: the two substitution-block one-counts always differ by exactly one; the context classes are disjoint; the stated probabilities are positive and sum to one for the range \(k\ge4\). The all-order theorem depends on the symbolic common-prefix, bridge, and context-coverage lemmas, not these finite experiments.

No independent mathematical audit has been performed.
