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

Execute `python3 verify.py` in this directory. The standard-library checker exhaustively enumerates 8, 64, 1024, and 32768 labeled tournaments of sizes 3–6 and obtains 222 passing exact-integer/rational assertions. Specifically it checks every allowed two-bit endpoint pattern conditioned on a designated covering pair, the exact \(\frac12(3/4)^{n-2}\) covering-event probability and the induced bivariate score law. The finite checker does not prove any limit, exponential relative error or external source priority. Those properties require the independently written mathematical argument in `RESULT.md`. No independent audit has been performed.
