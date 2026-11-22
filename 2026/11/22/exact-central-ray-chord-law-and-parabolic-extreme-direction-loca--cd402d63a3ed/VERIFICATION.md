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
# Reproducibility and scope

Run `python verify_central_bicylinder.py` using Python 3 standard library only. The successful output from the executed file is stored verbatim in `verification_output.txt`; it reports 440,041 deterministic assertions, including 220,000 seeded uniform directions. The checker derives a polar-area integral separately from the closed arctangent formula, compares numerical derivatives and endpoint asymptotics, independently integrates shrinking parabolic neighborhoods, and checks exact radial geometry for each sampled direction.

The mathematical proof is in `RESULT.md`. It covers all thresholds in the support and a conditional total-variation limit; random samples, quadrature and finite assertions do not prove these universal claims. The verified primary source was publicly dated 2008-01-19. Historical priority remains provisional owing to inaccessible portions of older cylinder literature. There is no independent mathematical audit or external certification in this package.
