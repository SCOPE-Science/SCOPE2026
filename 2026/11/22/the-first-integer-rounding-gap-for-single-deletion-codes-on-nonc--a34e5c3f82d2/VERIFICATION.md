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

# Verification record

The provided `verify.py` reads the adjacent `certificate.json` and uses Python 3 standard-library integer arithmetic alone. Execute `python3 verify.py` in a directory containing both files. It regenerates all restricted-growth words through order six, rejects exactly crossing set partitions, canonicalizes all one-position deletion outputs, and constructs the full induced compatibility graph for each order. Complete clique search with proper-color pruning establishes each integer upper bound; each stored code meets it. The script separately checks every exact rational primal and dual LP inequality, nonnegativity, and matching objective totals.

Expected output has six summary rows with input counts 1, 2, 5, 14, 42, 132, maximum code sizes 1, 1, 2, 3, 5, 12, fractional optima 1, 1, 2, 3, 95/16, 32021/2390, and final marker `VERIFY_OK`. The length-six enumeration checks 34,913 recursive nodes in the exhaustive clique search. The rational certificate arrays are indexed by lexicographically sorted canonical input words and then by sorted distinct output words; this convention is reconstructed independently from the channel definition.

All finite searches have complete stated ranges. No random sample, numerical floating-point status, or infeasible-timeout inference is used as a proof. Nothing in the package certifies all larger orders, publication priority, or an independent mathematical audit.
