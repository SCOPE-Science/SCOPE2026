---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible checks and limitations

Run `python3 verify.py` with the standard library to replay the sample graph counts; it uses exact integer square roots for the Beatty coordinates and integer greatest common divisors. At `X=100000`, the recorded counts are `42810`, `28608`, and `11494` for a three-vertex path, a three-vertex complete graph, and a four-vertex complete graph, respectively. The prime-truncated products (primes below `10000`, evaluated in floating point) are approximately `0.428257912679`, `0.286755872147`, and `0.114890809814`. The checker tests that each observed density differs from its truncation by less than `0.003`; it does not test the claimed uniform error estimate or enclose the infinite product.

The power-saving estimate is mathematical. Its main steps are circular spacing for all common divisors, effective residue discrepancy from the algebraic norm and the Erdős–Turán–Koksma inequality, truncation of the product of edgewise Möbius sums, and absolute convergence with a weighted series tail bound. The finite examples are optional illustrations, not hypotheses or certificates for any of these steps.
