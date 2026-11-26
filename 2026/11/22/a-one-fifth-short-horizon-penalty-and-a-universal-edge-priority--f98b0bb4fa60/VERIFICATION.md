---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For t>0 the Hessian of the trace exponential in any nonzero symmetric direction is the sum of squared spectral-basis entries times strictly positive integrated exponential factors. The edge-to-Laplacian map is injective, so compactness gives a unique minimizer and uniqueness gives continuity on (0,∞). At fixed B, tr L=2B and the Taylor remainder is uniformly O(t³) on the simplex. The quadratic coefficient has matrix T=tridiag(1,4,1), and solving Ty=1 with y₀=yₙ=0 gives the stated alternating geometric formula. The two boundary terms in its numerator have magnitude at most 2ρ<1−ρⁿ, proving positivity and feasibility of the normalized stationary point; subtracting the first two recurrence equations gives 3(y₁−y₂)=y₃>0, also for n=4. Uniform convergence and uniqueness yield the short limit. For the long limit the centered linear test vector bounds λ₂ even at disconnected allocations. For the proposed wᵢ=c i(n−i), the path polynomial operator has leading action c k(k+1) on degree k: the backward-minus-forward coefficient is linear with leading term 2i, and the sum has leading term −2i². Evaluation on the n vertices triangularizes it through degree n−1, so the gap is exactly 2c. Equality for any other allocation in the fixed-vector Rayleigh bound forces the same weights by summing the node equations. The minimum heat trace bounds its optimizer's gap below by λ*−log(n−1)/t; compactness gives the long limit. Its first two weights have strict reversed order when n>3, hence there is a finite crossing by continuity. For the curvature ratio, Qshort=B²/(sum y) with sum y=n/6+O(1); summing the long design's squared eigenvalues gives Qlong=12B²(3n²−2)/(5n(n²−1)). Their ratio tends to 6/5, not a ratio of heat traces. Independent Fraction computations for n=4 through 10 corroborate the exact linear systems and spectra, and for n=4 give Qshort=7/4 and Qlong=46/25 for a unit budget. The all-size and all-horizon claims rely on the proof, not the frozen numerical execution count.

## originality

PASS

The long allocation is prior, and generic convex optimization of Laplacian spectral objectives is prior. The inspected literature and records do not give the combined finite-time heat-trace endpoint comparison, in particular the exact short profile, all-size ordering reversal, and quantified 6/5 initial-coefficient regret. Priority is limited to inspected evidence.

## value

PASS

On the same graph family and with the same budget, a natural observation objective genuinely switches which boundary edge receives more conductance. This holds for every n≥4, rather than an arbitrary small example, and the explicit short profile gives a mechanism. The asymptotically nonzero 20% excess quantifies the cost of using the familiar gap-optimal design for the first variable short-time coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
