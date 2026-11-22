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

# Verification scope

The core analytical checks are: (1) a subnormal weighted shift cannot have a strictly decreasing positive weight sequence; (2) the small-Schur-exponent derivative of the Hausdorff moment inequalities yields complete monotonicity of the logarithmic weight deficit; (3) the unique finite signed Hausdorff measure for this deficit has explicitly computable coefficients whose second coefficient fixes the sharp boundary; and (4) the Poisson probability generating function reproduces every powered moment. These checks are fully reasoned in `RESULT.md`.

Reproducible supplementary computation: `python check.py` (Python standard library, version 3.11 or later) produces `PASS: 1081 supplementary finite tests`. It tests coefficient positivity and logarithmic finite differences in permitted parameter examples, a strict negative finite difference outside the permitted wedge, boundary parity, and truncated Poisson-versus-direct moment agreement. Series tails, not checked by finite enumeration, are bounded analytically by the geometric coefficient estimate in the proof. Numeric tests are examples, not proof of the universally quantified theorem.

No external independent audit, formal proof assistant, or third-party mathematical validation is claimed. Historical novelty remains provisional pending independent literature review; there is no assertion that the cited known MID sufficiency results are new.
