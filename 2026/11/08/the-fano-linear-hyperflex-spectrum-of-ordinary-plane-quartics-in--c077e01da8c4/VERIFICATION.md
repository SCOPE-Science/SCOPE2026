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

# Exact checks and scope

Run `python3 verify_hyperflex.py` to reproduce the included `verification_output.txt`. The script enumerates the \(512\) Fano-normalized triples \((d,e,f)\) over the exact finite field \(\mathbb F_8\), checks the seven contact equations against rank, verifies expected rank distribution \((1,49,294,168)\), and locates one smooth representative of each of the four ranks using the exact seven gradient exclusions. It checks concurrency for a three-line hyperflex set. The mathematical proof of classification over every algebraically closed characteristic-two field is in RESULT.md, independent of sampling.

No exact checks of nonordinary quartics, characteristic-zero limits, or historical priority are asserted. Independent audit has not been performed.
