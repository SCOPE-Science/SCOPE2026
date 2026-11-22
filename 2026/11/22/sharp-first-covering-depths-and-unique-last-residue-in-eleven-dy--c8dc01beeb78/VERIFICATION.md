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

## Reproduction

Run `python3 check.py` alongside `census.json` using Python 3.9 or later. The only imports are standard-library modules. It completes a full finite breadth-first traversal for every modulus \(2^k\), \(1\le k\le11\), then explicitly tests the reachable/unreachable status of every residue pair in the ambient state square, checks the exact histogram endpoint, and independently validates small-depth results. The program prints `EXACT_CENSUS_AND_INDEPENDENT_CROSSCHECKS_PASSED` after all assertions succeed. The `census.json` output is regenerated from the recurrence rather than used as an input to the proof.

The exhaustive check reaches \(3\,145\,728\) primitive states at the largest modulus, and the ambient grid there has \(4\,194\,304\) pairs. All finite state-distances are checked. This is an exhaustive finite computation for the claimed domain, not a verification of an infinite conjecture. The mathematical identification of the finite graph with the indexed Stern sequence and its binary-order first occurrences is given in the proof.

## Limits

No exponents beyond eleven have been examined or accepted as part of the claim. No independently audited certification is represented. General published asymptotic results establish eventual coverage but not these finite sharp thresholds.
