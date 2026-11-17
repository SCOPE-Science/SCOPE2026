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

# Reproduction and boundaries

Run `python verify.py` (standard-library-only). The output in `verification_output.txt` is from this concrete package. Verify integer flow conservation, rotor-arrow placement and candidate times for all sizes \(3\le n\le500\). Independent microscopic iteration matches the analytic first-entry formula for \(3\le n\le60\), checking no unicycle occurs earlier. A separate exhaustive loop checks all \(3^n\) labelled rim-rotor initial conditions with the chip initially at rim zero for \(3\le n\le8\). The count of all configurations tested in this finite census is \(3^3+\cdots+3^8\), not an all-size exhaustive proof.

The all-parameter argument is given in `RESULT.md`: conservation of a proposed firing odometer at every vertex; least action for the walk stopped at the first visit to the opposite rim site; final rotor arrows funnel to a unique two-cycle at that site; and the standard rotor unicycle recurrence theorem. These are the sufficient analytic ingredients independent of computation. No exact global maximum beyond the enumerated sizes is established.
