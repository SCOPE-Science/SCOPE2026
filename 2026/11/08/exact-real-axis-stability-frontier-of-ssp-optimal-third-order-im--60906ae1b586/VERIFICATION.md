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

The main universal proof is an analytic reduction: triangular stage elimination gives an exact stability function; strict monotonicity of the associated Möbius ratio establishes both sharp parity-dependent thresholds; \(s\operatorname{artanh}(1/s)\to1\) establishes the stiff-stage limit. No finite test is used to justify quantification over all stages.

Run `python verify.py` from the directory containing the embedded files. With `mpmath`, the prepared checker returned `VERIFY_OK 864`. It independently uses stage-by-stage triangular forward substitution at stages 2 through 35, compares against the closed formula at ten step locations around each boundary, checks the endpoint parity and stiff-limit signs, and checks seven larger stage-count asymptotic instances. The tests use 90 decimal digits and relative equality tolerances, not formal interval enclosures.

Limits: the implementation samples finitely many stages and parameters; it is not a computer-assisted proof of the full theorem. The stability statement is exact arithmetic, scalar real decay only. The 2019 four-stage plotted stability-region endpoint is a comparison, not a numerical certificate for all stages. Independent audit has not been performed.
