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

# Reproducibility and verification

The exact claim is established by the analytic count and direction of imaginary-axis roots in RESULT.md. Reproduction of optional numerical spot checks:

```bash
python3 -m pip install numpy
python3 verification/check_gamma.py
```

The script evaluates the polynomial \((\lambda^2+a)(1+\tau\lambda/q)^q-b\), the phase-matching frequencies, the signed transverse derivatives, and interval root counts for four parameter pairs, through gamma orders one to six. The recorded execution produced `PASS: 96 characteristic/threshold/crossing and root-count checks`. Numerical samples are not used as proof of spectral stability for every parameter; that follows from explicit crossing enumeration and root continuity. The review did not independently validate the nonlinear neuron model, and no external audit has been performed.
