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

Run `python3 verify.py` under Python 3; no external packages or input files are needed. The bundled checker compares the analytic negative-binomial generating-function derivative with explicitly accumulated probability masses, tests sample optimizer inequalities and derivative directions, finds pairwise crossover roots, and compares limits with sharp asymptotic formulas.

The completed checker run printed `PASS: 263 deterministic diagnostic assertions` and the reproducible \(z=4\) illustration. The analytical uniqueness and infinite-domain conclusions are established by the proof in `RESULT.md`, **not** by finite numerical experiments. No external empirical data, finite enumeration claim, independent scientific audit or formally certified proof is asserted.
