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

The mathematical proof is contained in RESULT.md. Execute the included standard-library file with `python3 checker.py` in the same directory. It independently solves the two half-period fixed-point recurrences and checks the stationary integral for sampled positive parameters, both hyperbolic simplifications, strict regime signs away from the theoretical crossover, and the algebraic threshold at quadratic exponent. The deterministic run reports `PASS: 38553 supplementary assertions; quadratic crossover x*=1.061275061905`.

The critical argument is analytic, not empirical: contraction of the affine return map, exact fixed-point integration, strict growth of \(\sinh(z)/z\) for \(z>0\), boundary limits of the comparison ratio, and the quadratic reduction. Finite numerical checks do not establish infinite-domain truth or certify originality. The proof is for positive accumulation, positive rain volume and dose coefficient, and any positive power exponent; its inequalities are strict except at the unique indicated tie.

The road-sediment source date is its 2024-03-14 electronic-article date in PubMed PMID 38492751, not its 2024-04-15 print issue. The motivating source's full text was unavailable and its abstract alone cannot exclude the possibility of prior coverage; closest accessible source material and scientific comparisons are specified in AUDIT.json and REVIEW.md. No field calibration, statistical confidence guarantee, general optimal-control result, or independent external audit is claimed.
