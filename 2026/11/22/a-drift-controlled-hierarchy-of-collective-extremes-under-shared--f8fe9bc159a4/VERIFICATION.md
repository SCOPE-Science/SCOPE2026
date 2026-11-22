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

The included `verify.py` is executable using Python 3.9 or newer with SciPy. With SciPy installed, run `python3 verify.py` in the directory containing the script. It reports `PASS: 128 assertions including renewal integral, saddle asymptotics, and strict exponent hierarchy`.

The program independently integrates the exact renewal mixture \(r\int_0^\infty e^{-rt}\overline\Phi((y-at)/(\sigma\sqrt{t}))^n\,dt\), after a positive time rescaling for numerical stability. Its comparison against an analytical saddle prefactor is numerical and uses finitely many parameter choices. An exact one-coordinate survival formula and the closed exponent identities are additionally tested. The proof, not this checker, is the basis of the claimed arbitrary-parameter and unbounded-threshold results. In particular, no simultaneous growing-particle-number limit is claimed. Independent audit has not been performed.
