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

# Reproducible verification and its limits

Execute `python3 verify.py` with Python 3 and no nonstandard packages. Expected output: `VERIFY_OK: 57 analytic-identity/numerical-consistency groups; m=2 exact tail; m=3 deterministic torus integrals`.

The verifier performs exact rational Gaussian-elimination determinant checks for \(B=I-\mathbf1\mathbf1^\mathsf T/m\) at all integer \(2\le m\le12\); exact integer phase-quadratic identities for two test vectors per sample count; an independent deterministic angular quadrature of the known exact \(m=2\) survival law; deterministic \(640\times640\) torus quadrature for \(m=3\) at two tail thresholds; the local quadratic limit for small phase perturbations; and analytic closed-form checks of the constants for \(m=2,3,4\).

The exact rational tests are identities in sampled finite dimensions; no numerical quadrature proves the asymptotic expansion at every \(t\), nor does finite testing establish the all-\(m\) theorem. The displayed argument in `RESULT.md`, not the code, proves the asymptotic and the moment characterization.
