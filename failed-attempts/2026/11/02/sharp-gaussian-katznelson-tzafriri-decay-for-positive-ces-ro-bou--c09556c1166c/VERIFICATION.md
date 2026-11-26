---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For fixed interior α and θ the shift powers telescope, and taking absolute column sums on ℓ¹ gives the exact weight θ(j/(j-k))^α multiplying |p_n(k-1)-p_n(k)|. The binomial ratio and local limit give σ_n² times this gradient tending to |x|φ(x); the ratio on k≤n(1+θ)/2 and a Chernoff bound on its complement give a uniform Gaussian envelope, including the support endpoints. The near-cutoff sum is bounded by a constant times ε^(1-α), and the envelope makes off-window normalized columns negligible. Thus the localized Riemann sum converges and yields the same supremum as the continuous profile; the scale is θ(nθ)^α n^((1-α)/2)/σ_n^(1+α)=(θ/(1-θ))^((1+α)/2). In the far-right bound the displayed constant 2^α for j>2n is slightly too small at k=n+1; 3^α is a uniform bound and suffices for the stated limit. The continuous profile is positive and tends to zero at both ends, so its maximum is attained. The spectrum follows from the explicit eigenvectors in the open disk and spectral radius 1, and replacing the gradient by p_n in the same central argument proves non-power-boundedness. The positive Cesàro property also follows directly from Σ_(m≥k) p_m(k)=1/θ and the Cesàro bound for W. The supporting check.py was inspected, not run; its finite checks are not the proof.

## originality

FAIL

A distinct, earlier indexed finding has the same fixed-parameter operator, both the exact global limit and the full central profile, as well as an additional sharp power-norm limit. The failure is based on exact statement-level coverage, not unavailable literature.

## value

FAIL

A sharp norm constant and a localization theorem for this natural non-power-bounded example would be useful invariants if unknown. Both are already established by the exact indexed theorem, with no distinct surviving extension; repeating the computation does not supply another mathematical contribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
