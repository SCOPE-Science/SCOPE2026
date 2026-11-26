---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1,
  "record_status": "passed"
}
---
# Verification and limits

The proof in `RESULT.md` computes the joint generating function of total incidences and active-catalyst counts. The Pareto rescaling and the integrable bound give a sequential limit for the single-catalyst transform; raising to the power of the catalyst count proves the sharp window. The upper and lower off-window probabilities are checked directly from the probability of no incidence, not from extrapolation of a bounded-offset approximation.

The mathematical comparison with RAF formation is a reindexing of Kim and Sönmez (arXiv:2611.06033v1), Theorem 8 and Section 3.3.4. It uses the fact that an ambient RAF with all members of its food closure in the restricted subsystem is exactly a RAF in that subsystem. No new RAF existence theorem or limiting law in the RAF critical window is claimed.

Run `python3 check.py` (Python standard library only) for finite consistency checks of the ordered-split counts, one exact zero-event formula evaluated numerically at Pareto index one half, the prefactor and a Sibuya series. The script tests neither asymptotic theorem nor the existence of finite RAFs. This is a mathematical random-word model, not a chemical-kinetics calculation.
