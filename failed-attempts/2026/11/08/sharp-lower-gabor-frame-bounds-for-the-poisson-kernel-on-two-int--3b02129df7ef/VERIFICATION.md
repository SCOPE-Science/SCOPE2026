---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The integer modulation and two translated integer cosets admit scalar Zak-frame symbol |Zg(x,ν)|²+|Zg(x−θ,ν)|². Poisson summation gives an explicit rational Zak modulus; frequency minimization at ν=1/2 followed by a convex increasing rational function of sin²(π(x−1/2)) yields the sharp spatial minimum with equality. The resulting lower-bound expression is positive precisely when θ∉Z, strictly optimized by half-offset and has the stated quadratic collision limit. The prior identical full theorem provides an independent cross-check of normalization and the exact formula; the claim is correct.

## originality

FAIL

Decisive exact prior coverage: the 2026-11-02 published Resultary theorem "Exact staggered-translation Gabor bounds for the Poisson kernel" treats the identical unnormalized Poisson g_w=(t²+w²)⁻¹, integer modulation frequencies and translations Z∪(Z+θ), for every width and nonintegral offset. It proves the same optimal LOWER frame bound, same half-offset optimizer and same quadratic collapse coefficient, and additionally gives optimal upper bound and conditioning. Its formula is algebraically identical under q=e^(−2πw), c=|cos(πθ)|. This is not merely the different older *frequency*-coset result. The submitted theorem is completely covered.

## value

FAIL

FAIL for the exact submitted claim as a distinct contribution: all sharp constants, optimizer, frame criterion and degeneration law are already established in a full theorem for the exact same Gabor atoms, while that theorem additionally calculates upper bounds and condition numbers. Reproducing an established sharp formula and proof in different variables does not fill a new mathematical gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
