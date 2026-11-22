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

# Reproduction

Use Python 3 and execute `python3 verify.py` in this directory (no third-party packages). The recorded exact output is `verification_output.txt`. The script exhaustively enumerates every unlabelled tree through ten vertices by leaf attachment, deduplicated with center-rooted isomorphism codes; every oriented bipartition is similarly canonically encoded with fixed lower/upper colours. It computes the complete coefficient polynomial exactly using independent subset counts and the no-four-cycle mixed-cut identity.

The script checks the class and fingerprint counts for each order, verifies precisely two size-two coefficient fibres at ten vertices, checks the four explicitly stated witness posets occur and exhaust those fibres, and independently tests all three-status one-point assignments for every oriented class through eight vertices and all four ten-vertex witnesses. The direct checker rejects assignments violating ideal, filter, or old-order transitivity constraints. No random sampling is used.

Completeness rests on the induction that every tree of order greater than one has a leaf, and on the standard uniqueness of rooted unordered-tree codes after canonical centre rooting. The executable tests are finite and do not assert a reconstruction theorem beyond ten vertices. The source-comparison and historical-priority determination remain subject to independent review.
