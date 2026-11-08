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

The standalone `verify_parking.py` was executed directly from its final source file and returned `PASS: 6154 exact identities and controlled numerical mean checks`. It includes independent rational enumeration of attempted subsets and arrival orders, pointwise checks of the finite edge-availability formula for paths through eight sites, all-priority-order checks of the jamming equivalence through seven sites, and numerical first-moment checks up to twenty thousand sites. The code uses no external dependencies. Exact finite enumeration is not an infinite-parameter proof: the proof in `RESULT.md` establishes the locality bound, limiting factorial moments, saturation-time equivalence, and passage to the number of attempts.

The source literature was checked for the exact mean and the earlier first-order scaling; the Gumbel law and its centering are not asserted to have been independently externally audited.
