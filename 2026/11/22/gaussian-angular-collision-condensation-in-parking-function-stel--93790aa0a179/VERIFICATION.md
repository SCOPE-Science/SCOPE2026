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

# Reproducibility and scope

Run `python3 checker.py` using the Python standard library. The program creates the vertices directly from the parking-bound definition, iterates over every sign assignment and objective-magnitude order for dimensions two through five, chooses a unique maximizer by an independently evaluated dot product, compares each cone's exact rational mass with the claimed expression, and checks the Laguerre coincidence formula for both merged and unmerged vertex families. The exact weighted rank means and variances are additionally evaluated in dimensions 10, 25, 50, 100, 400 and 1600, with a large-order normalization diagnostic.

Observed output concluded with `PARKING_ANGLE_LAGUERRE_EXACT_PASS 16` for sixteen distinct parameter cases. Enumeration is finite, so it does not certify the asymptotic theorem. The analytic proof in RESULT.md separately establishes the all-dimensional angular law, the Gaussian conditional limit and the sharp leading constant. No independent verification or audit has been conducted.
