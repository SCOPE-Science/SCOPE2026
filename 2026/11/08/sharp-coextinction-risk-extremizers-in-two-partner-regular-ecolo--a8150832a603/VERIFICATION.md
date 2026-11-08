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

# Verification of the cycle-coextinction extremal theorem

Run `python verify.py` using Python 3 and its standard library. The script checks the signed \(C_a\)-\(C_b\) merge identity for all \(3\le a,b\le24\), every one of the nine exceptional local replacement identities, and all 5,666 cycle partitions across \(3\le n\le36\). It verifies both coefficientwise inequalities and distinct extremal polynomials. It also directly enumerates all deleted-vertex subsets for 25 graph types through 11 patches to confirm that the independent-set coefficients exactly count configurations with no secondary loss, and recomputes the nine-patch witness counts \(27,30\) out of \(84\).

Expected output starts `VERIFIED` and reports integer counts `merge_identities: 484`, `exceptional_rewrites: 9`, `orders: 34`, `cycle_partitions: 5666`, and `direct_subset_distributions: 25`.

The script is an executable finite cross-check, not a certificate for infinitely many orders. The universal result follows from the exact recurrence and the monotone finite sequence of local substitutions given in `RESULT.md`. Some coefficients can tie for different networks, especially the low-degree terms; strictly better scalar Bernoulli no-loss probabilities distinguish all non-extremal cycle partitions for every deletion probability strictly between zero and one.
