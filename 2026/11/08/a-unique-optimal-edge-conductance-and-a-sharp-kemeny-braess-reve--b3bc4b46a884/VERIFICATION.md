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

# Reproducibility and limits

Use Python 3 with only its standard library. Execute `python check_kemeny.py` from the directory containing the checker. Actual output: `PASS: 175 exact full-matrix inversions; 252 rational scaling identities; threshold boundary tests.` The checker uses rational arithmetic and inverts the full labeled fundamental matrix rather than the three-orbit quotient used in the proof. The analytic spectrum and derivative are needed for the claims over all integers and real conductances; the finite replay alone cannot prove them. Independent mathematical audit has not been performed.
