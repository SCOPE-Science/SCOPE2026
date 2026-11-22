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

# Reproduction and limits

The complete proof, including the two-cut resistance identity, the strictly convex scalar reduction, the integer identities at adjacent parameter values, and both asymptotics, is in `RESULT.md`. The standard-library `verify.py` supplies independent finite diagnostics and can be executed as `python3 verify.py`. The observed output of this packaged version was:

```
PASS: 1484 exact threshold, row feasibility, direct trace, sampled unrestricted designs and asymptotic diagnostics
```

For the spectral check, the program inverts \(L+\mathbf1\mathbf1^{\mathsf T}/N\) by Gauss–Jordan elimination, subtracts one from its trace, and compares with the cut-resistance expression. The randomized tests construct independently varying feasible edge probabilities and compare their objective values. Their role is diagnostic; the strict-convexity proof certifies optimality for every real feasible design. No exhaustive numerical search over infinitely many parameters is claimed. There is no independent mathematical audit.
