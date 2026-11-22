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

# Reproducibility and checks

The exact proof in `RESULT.md` applies to every integer \(n\ge5\). Execute `python3 check.py` in the extracted directory using Python 3 standard library only. The checker computes exact rational dynamic-programming terminal-size distributions for \(n=5,6,7,8\), enumerates all reachable first-three success geometries, verifies the star and triangle forms, and verifies Laplace factors and moments. It prints `PASS: 16 independent grouped exact checks` after the exact small-case results. All probability identities were reconstructed from exponential race memorylessness; no Monte Carlo result or failed search is used as an infinite proof. The retained historical-priority risk and scope exclusions are discussed in the result and review.
