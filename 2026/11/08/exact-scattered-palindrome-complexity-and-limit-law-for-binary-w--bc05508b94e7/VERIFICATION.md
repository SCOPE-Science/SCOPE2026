---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python3 verify.py` using Python 3. The script checks the previously known deterministic gap identity on all 3,876 words of lengths 3–18 and evaluates rational exponential-integral expressions for the limiting moments. Expected final line: `RATIONAL_MOMENTS_OK 7/80 2299/1209600`. The probabilistic limit and the integral identities for its moments are justified in `RESULT.md`; the finite enumeration only supplements the proof.
