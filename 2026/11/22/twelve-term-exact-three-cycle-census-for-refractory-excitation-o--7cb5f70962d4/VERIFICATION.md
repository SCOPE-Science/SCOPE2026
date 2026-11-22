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

The independent literal-update checker in `proof/verify_rook_gh.py` exhaustively evaluated all labelled states for widths one through four and found exactly 6, 72, 2562, and 119880 primitive three-periodic states. The symbolic coefficient procedure separately aggregated all 6859 nonempty palette/subpalette triples and asserted the full twelve-base coefficient table using integer arithmetic. Recorded output is provided in `proof/check.out`.

The infinite-family result relies on the proven inclusion–exclusion identity and the fixed finite symbolic coefficient certificate, not on extrapolation from four enumerated sizes. Other periods, attraction basins, spatial symmetry orbits and historical priority are not certified. Independent external review has not been performed.
