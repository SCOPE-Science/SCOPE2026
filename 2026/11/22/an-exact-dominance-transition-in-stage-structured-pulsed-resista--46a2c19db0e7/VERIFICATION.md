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

# Verification of analytical claim

The proof explicitly derives allele-density pulses from three Hardy–Weinberg genotype survivals, establishes monotonic stagewide convergence by positive mixing, identifies the positive Perron eigenpairs, and takes a quadratic projection at exactly zero dominance. Every limit is within the assumptions stated in `RESULT.md`; no simulated trajectory is offered as proof of an infinite-dimensional or infinite-time result.

Run `python3 verify.py` with standard Python 3. The script executes exact Fraction checks of the allele-density identities at multiple rational frequencies and dominance coefficients, then computes a two-stage matrix exponential from the generator's explicitly known eigenvalues, and numerically compares the quadratic asymptotic and exponential spectral exponent. The checker is finite and numerical in its asymptotic comparisons; this is evidence of internal consistency only, not exhaustive certification.

The reduction to strictly positive period matrices uses irreducibility and a positive time interval. The parameter bounds ensure all genotype survival factors are strictly positive, preventing zero-denominator or missing-stage failures. Independent audit: not yet performed.
