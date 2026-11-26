---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Reconstructed RESULT.md §§1–5 for arbitrary nonnegative individual allocations. On 1⊥ the Laplacian map is injective in edge weights, and the trace Hessian has strictly positive divided differences of f′, including at repeated eigenvalues (f=x^(−p) or −log x). The fixed cost simplex bounds all eigenvalues above, so approaching disconnection makes either objective diverge upward. Uniqueness forces invariance under simultaneous index permutations of the two parts. Their two edge orbits have conductances a,b; b=0 is disconnected and a=0 gives the connected crown graph for m≥3. The symmetric and antisymmetric constant and zero-sum vectors give positive classes 2(a+(m−1)b), mb, and 2a+(m−2)b, with multiplicities 1,m−1,m−1. On the budget line b′=−c/(m−1), the derivative at a=0 has sign opposite to A+TC−c(A+D+C), including for −logdet. Strict convexity gives the exact deletion criterion including equality and a unique interior stationary point otherwise. In the order derivative the sole negative term has magnitude AD log(2(m−1)/m); the positive DCT log(m/(m−2)) dominates since C/A≥m−1 and log(m/(m−2))>2/m. Dividing by C, the term D/C=(1−2/m)^p tends to e^(−2α) for p/m→α, also for α=∞, and A/C≤1/(m−1); expansion at fixed p gives 1+(p+1)/m+O_p(m^−2). Independently expanding the signed stationarity function after multiplying by m^(p+1) gives 2[(p+1)(1−r)−γ] at every fixed r=a/b; bracketing the unique derivative root proves the positive-part limit, including equality γ=p+1. A fresh full crown-Laplacian calculation verified 15 marked/unmarked edge marginal ratios for m=3,4,7 and five orders including 0 and 0.37. Replay with `OPENBLAS_NUM_THREADS=1 python /tmp/opencode/frozen-review-diagnostics.py` (check 3). The supplied checker was inspected but not executed; its deletion test partly branches on the formula itself, so the independent derivative check and analytic argument are the evidence for the exact boundary.

## originality

PASS

Credit p=0, p=1 and spectral-gap support results and the determinant critical-window ratio as earlier coverage. The exact real-order frontier, strict order hierarchy, fixed-order ratio extension and joint logistic law pass on the inspected evidence; no inspected stronger result was shown to imply that package. Closest full-text access limitations are retained.

## value

PASS

The exact threshold predicts whether every marked edge is purchased or removed under an interpretable family of objectives. Strict nesting answers a discrete support question that separate endpoint results leave open. The logistic law identifies the joint scaling at which the large-size and high-order limits diverge; the fixed-order window additionally resolves the relative conductance near deletion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
