---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

Each matching of size m has the same number of extensions, and each of size m+1 has exactly m+1 predecessors, so adding a uniform free pair preserves the uniform layers. Swapping two fixed entries a<b contributes the new inversion (a,b), and contributes two more for exactly each interior position whose image is between a and b; the other changes cancel. The ratio of class weights at fugacities θ₂>θ₁ is proportional to (θ₂/θ₁)^{n−2m}, strictly decreasing in m, giving usual stochastic order by the coupling and strict decrease in expectation, not strictness at every tail threshold. At fixed f the within-pair, pair/pair and pair/singleton contributions give g_n(f)=(n−f)(3n+f)/12. It is strictly decreasing and F is nonconstant for every positive θ and n≥2, proving strict negative covariance. The successive fixed-point weight ratio has the stated unique crossing in the interior; comparison across a buffer of order n gives vanishing opposite tails, also at the endpoints by choosing thresholds ε/2 or 1−ε/2. Transposing two entries in the random ordering used to generate a uniform partial matching changes at most four permutation images, so the reveal martingale gives conditional variance ≤16n³ uniformly in m. The conditional mean and this bound give the stated inversion LLN. The supplied script was inspected, not executed: its inversion identities, tail probabilities and covariance checks are exact on the stated bounded input, whereas the order-5000 crossover check uses floating-point log weights and approximates finite expectations, not exact numerics or a limit proof.

## originality

FAIL

There is no distinct component left after statement-level comparison. The exact complete-graph monomer density LLN and its curve are already in Alberici–Contucci–Fedele–Mingione; varying the fugacity, including both endpoints, follows by monotone squeezing. The inversion-density limit follows from that LLN, the already encoded conditional inversion mean, and Féray–Kammoun's stronger conditional concentration for classical pattern 21. The distinct November 2 spatial-inversion record also states the identical simultaneous strict matching coupling and increment, and stronger covariance for arbitrary nondegenerate mixtures and every increasing test function of inversions. Mixing the coupled layers using the elementary likelihood ratio in θ gives the stated fugacity order and strict expectation. The November 2 catalogue date is later than the frozen record's date. It demonstrates current equivalent/stronger coverage of the finite claim, not that this finite statement predates the frozen record or that priority is settled. None of this is a claim that the mathematics is false. No novel narrower claim is substantiated by the frozen evidence.

## value

FAIL

The inversion ordering and crossover are mathematically natural. However, the exact finite coupling is already covered as part of a stronger indexed theorem, and the full asymptotic curve including endpoints follows by reparameterizing the known monomer LLN and applying the standard conditional pattern theorem. The elementary self-contained proof is useful exposition, but no additional supported structural result or boundary remains to justify a distinct finding or a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
