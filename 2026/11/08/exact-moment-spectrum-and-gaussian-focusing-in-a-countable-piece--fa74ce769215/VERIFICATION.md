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

The analytical proof in RESULT.md establishes the all-positive-moment recurrence, exact Wasserstein equality for times at least two, the almost-sure exponential rate and Gaussian fluctuation variance. No independent audit has been performed.

The self-contained standard-library test `verify_focusing.py` computes the motion of rational starting points using exactly the dyadic strip translations, integrates the resulting piecewise translations exactly over every binary cylinder of depth \(t\), and sums the geometrically scaled starting strips. Run `python3 verify_focusing.py` from the package directory.

The test compares the independent integral against the claimed recurrence for \(s\in\{1,2,3,4\}\) and \(0\le t\le10\); it also checks the Bernoulli digit waiting times at rational samples and the right-half-torus condition needed in the Wasserstein proof. The expected output is `PASS: 599 exact-rational checks (finite corroboration, not an infinite proof).` These finite tests cannot themselves certify the real-parameter theorem or limiting distribution.

The numerical constants in the closed-form formula are algebraically evaluated from the exact first two moments and the quadratic characteristic equation; no floating-point certificate is required. The mathematical limitation is that the initial distribution is normalized Lebesgue measure and the exceptional boundary extension must move \(x=0\) away to make the weak limit non-invariant.
