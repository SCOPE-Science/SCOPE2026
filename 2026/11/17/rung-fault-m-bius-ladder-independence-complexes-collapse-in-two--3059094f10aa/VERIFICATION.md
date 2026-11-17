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
The exact standalone `verify.py` checks the graph's twisted wrap edges and the absent rung, selects the prescribed even columns, enumerates **every** nonempty independent exterior set, and checks the existence of a free fiber cone vertex.

Verified counts (all passed): \(n=3:6\); \(4:8\); \(7:62\); \(8:80\); \(11:566\); \(12:728\); \(15:5102\); \(16:6560\).

Reproduce with `python3 verify.py`. The finite checks are not a proof for every size; the two modular parity contradictions in `RESULT.md` provide that proof. No third-party certification or independent audit has been performed.
