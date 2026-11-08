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

# Verification
The analytical proof is in `RESULT.md`. The included `verify.py` is independently runnable with the packages in `requirements.txt` and verifies the characteristic polynomial, resolvent numerator, exact resultant, the cancellation at the critical rate, and the \(c=0\) derivative. It constructs a separate labelled-state continuous-time Markov generator and matches its occupancy-count probabilities against the three-state generator for seven rates and eight times, giving \(56\) vector comparisons, \(168\) count-state values. The replay passed.

**Limits:** Numeric checks sample finitely many times and rates and do not prove the universal theorem. Simple-spectrum and residue-sign arguments, the exact resultant, and the two-exponential zero-count reasoning are needed for the infinite claims. No independent external review or audit has been performed. Full text of certain older hazard-mixture literature was not accessible for historical-priority confirmation.
