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

# Scientific verification

The proof establishes aperiodic-word shattering and the homotopy type for every \(n\ge2\) and \(1\le k<n\). Its nonstandard critical obstruction is the first complex cyclic moment: all periodic subsets have moment zero, while a one-swap change moves the moment by two distinct roots of unity. Every non-forced trace fiber contains a pair related by a one-swap, and every missing rank-\(r\) face can be filled along its boundary by the remaining faces of a single rank-\((r+1)\) simplex. These are exact all-order arguments, not computational extrapolations.

The independently written pure-Python `checker.py` was executed successfully from the actual scientific package source. It exhaustively enumerated all \((n,k)\) with \(2\le n\le12\), tested every support for shattering, and checked all Möbius counts and forbidden Johnson adjacencies. It additionally checked the mod-two top boundary ranks for all \(2\le n\le10\). Reported totals: 81,924 support decisions, 680 periodic-pair checks, and 45 homology-rank instances; all passed. These finite ranges do not constitute an infinite proof, nor do mod-two ranks alone certify integral homotopy. The integral homotopy claim is justified by the explicit nullhomotopic cell attachments and connectivity in the written proof.

The result is not independently validated, and no formal proof assistant or external mathematical certification is asserted.
