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

# Reproducibility and checked scope

Run `python3 verify.py` using Python 3 and only its standard library. The program enumerates every map \([n]\to[n]\) at \(1\le n\le6\), independently forms vacancy masks and their Walsh transform, and checks the resulting coefficients against the character formula and the Stirling surjection counts. It then checks each degree multiplier and the claimed integer valuations for \(1\le n\le120\), with 15,137 exact assertions in total.

The general nonvanishing and valuation conclusions follow from the proof in `RESULT.md`: no finite search establishes them by itself. A bounded comparison with existing occupancy and mapping research was performed. Neither historical originality nor an independent audit has been certified.
