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

Run `python3 verify.py` using the standard library. It exhaustively constructs represented-digit sets for \(k=1,2,3,4\) through the claimed minimum lengths, checks no earlier represented interval can synchronize, and enumerates the exact optimal counts \(2,5,14,41\) for those small parameters. Direct carry transitions verify constructed words through \(k=8\). The Python checks are finite and do not constitute a proof of the universal theorem; the symbolic proof is in RESULT.md. Independent mathematical audit has not been performed.
