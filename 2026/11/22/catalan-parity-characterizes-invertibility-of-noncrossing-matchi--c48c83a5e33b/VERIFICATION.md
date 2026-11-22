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

# Reproduction and scientific limits

Run `python3 verify_noncrossing_walsh.py` from the folder containing this file. The Python-standard-library checker enumerates all frequencies for orders one through four and checks the recursive explicit zero witness by an independent signed-Catalan interval recurrence for every size one through thirty. The observed full zero counts at orders one through four are 0, 8, 0, and 15104, respectively. Orders five and beyond are not exhaustively Fourier-scanned.

The infinite theorem is proved in RESULT.md: a polygon reflection cancels noncentral root-partner classes, and at odd orders the central class factors as the square of a smaller signed Fourier coefficient. Odd Catalan cardinality is sufficient for universal nonvanishing. The finite computation is corroboration, not infinite certification.

The work has not received an independent mathematical audit; scientific priority is bounded by the listed source inspections and residual historical literature risks.
