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

The exact analytic proof is in `RESULT.md`. The standalone `impulse_benchmark.py` uses only the Python standard library and checks the root formula, synthetic examples, comparative statics and a numerical forward-ODE integration against the exact intervention advantage. Run `python impulse_benchmark.py`. Expected output: `PASS 25556 finite supplementary assertions`.

Numerical grids are supplementary: the infinite family of parameter cases is justified analytically by the strict monotonic derivative comparison. Error from the illustrative Euler integration is bounded empirically by the implemented tolerance, not treated as a formal error certificate.

The 2018 study's full-text manuscript was accessible via its author-uploaded text; the 2024 motivating article was read at the publisher. The 2022 impulsive epidemic paper was accessible by abstract in the retrieved source, and 2023 related modeling full text was inaccessible from its publisher in this check. Historical priority remains provisional. No independent audit is represented.
