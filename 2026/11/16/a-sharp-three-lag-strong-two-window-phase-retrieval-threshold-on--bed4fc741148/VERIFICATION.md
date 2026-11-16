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

The certificate `CHECK.py` uses only exact integer arithmetic modulo the prime 1021. It enumerates all 1,024 subsets of the ten-site cycle, isolates the 60 disconnected supports for lag three, and checks all 3,600 ordered time/frequency support pairs. Each reduced Fourier submatrix has full column rank, certifying nonvanishing of a complex Fourier minor under cyclotomic specialization. Seven rotation classes provide a separate census check.

The sharpness polynomial is algebraically factored in RESULT.md; the script checks the six nonzero coefficient positions, both disconnected support patterns at lag two, and the three surviving Fourier frequencies by exact finite-field evaluation. Its characteristic-zero vanishing is a direct factor identity, not inferred from modular vanishing.

Execution: `python CHECK.py`. Observed output: `CHECK_OK disconnected_supports=60 rotation_orbits=7 exact_modular_ranks=3600 sharp_witness=verified`.

The finite computation exhausts exactly the fixed ten-site domain. It does not test other cycle orders or measurement noise. Independent mathematical audit has not been performed.
