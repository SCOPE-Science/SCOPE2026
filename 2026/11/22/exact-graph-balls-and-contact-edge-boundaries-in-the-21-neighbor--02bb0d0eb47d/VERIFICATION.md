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

# Actual verification and limits

Run `python3 verify_contact_growth.py` from the same directory after extraction. The program uses only standard-library exact rational/integer arithmetic. It checks 11,175 geometric pairs among 150 central-subdivision tiles; 61 exact lattice-ball and incident-edge enumerations; and contact-graph BFS balls (radius through 8) and their edge boundaries (radius through 7). Output in the preparation environment: `PASS` on all three independent check groups.

The computational ranges are finite. The all-radius conclusion follows instead from the explicitly proved base-edge incidence, integer-hexagon counts, and crossing-edge formula in `RESULT.md`. The exact equality tiling itself follows from Yang–Wang's cited published preprint; no new proof of the classification of all 21-neighbor tilings is claimed. The original 1975 historical construction has not been fully read. No independent audit has been performed.
