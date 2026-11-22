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

# Finite exact verification

Execute `python verify.py` from the directory containing the delivered files, using Python 3.10 or later. The certificate enumerates exactly \(2^n\) binary words for each \(1\le n\le11\) (\(4094\) in all), calculates all contiguous-window weights twice by independent methods, and compares every exact integer signature. It asserts the moment-class counts \((2,3,6,10,20,36,72,135,272,528,1050)\), the complete-observation count \(1052\) at length eleven, precisely two exceptional four-word fibers with the listed members, and repair by one cubic length-three statistic.

The expected final program line is `VERIFY_OK: all 4094 binary sources of lengths 1..11 checked by two methods`. The proof of exhaustiveness is the integer loop `range(1 << n)` with a fixed-width binary encoding; no stochastic testing or extrapolation is involved. The certificate concerns this finite domain only and does not establish that these compression statistics retain full information for larger word lengths.
