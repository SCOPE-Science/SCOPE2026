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

# Reproducible checks

The supplied `checker.py` uses the Python standard library only. Running `python checker.py` in the folder containing it checks the two-stage threshold, the Erlang-2 median, both optimal-phase formulas, derivative vanishing at the candidate optima, derivative direction on randomly chosen competitors, consistency of exact probability formulas, monotonicity on a duration grid, and the first terms of the short-duration asymptotics. It prints parameter examples and the number of supplementary assertions.

The actual completed execution reported `PASS; 39007 assertions; threshold=1.256431208626170; Erlang2 median=1.678346990016661`.

The script is evidence for implementation and numerical consistency only. Global uniqueness, all-duration comparative statics, exact equality cases and asymptotic limits are proved analytically in RESULT.md. All random sampling uses a fixed seed. The scientific model is idealized; no empirical calibration, external replication or independent validation is claimed.
