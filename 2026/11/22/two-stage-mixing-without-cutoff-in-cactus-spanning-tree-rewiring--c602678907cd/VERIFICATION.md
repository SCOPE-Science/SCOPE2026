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

Each tree omits one edge per cycle. If a retained edge in a cycle is cut, exactly the retained edge just cut and the previously omitted edge in that cycle cross the resulting partition. This makes every single-coordinate off-diagonal probability 1/(2q_L), so the refresh coefficients are ell_i/(2q_L); irreducibility, symmetry, holding, and symbol permutations give uniform stationarity and start-independent distance. In continuous time the stationarity likelihood factors independently. In the specified window the long-coordinate amplitudes satisfy c_L(L-1)ε²→e^(-s) and max|εB|→0 for B=L·1_match−1. The linear sum satisfies Lindeberg, the sum of squares converges in probability to e^(-s) (variance bounded by O(L/c_L)), and the expected cubic remainder is O(sqrt(L/c_L)). This yields the claimed lognormal factor, with uniformly bounded second moments for each fixed s. The triangle retains amplitude exp(-3/(2α)), independently. For discrete time the loss versus continuous time on each fixed tensor degree tends to zero as tδ²→0, with δ=(kL+3z)/(2q_L), and the squared L² contributions are dominated by a constant times C^k/k! in the window and for u>1/α. At late times the long-block chi-square vanishes. At early times the count of matches separates the laws: covariances are nonpositive and the squared mean gap dominates both variance bounds, including by order L relative to c_L/L at u=1/α. The limiting profile is strictly monotone by multiplying the likelihood by an independent mean-one lognormal increment when its variance parameter increases, and applying strict Jensen to |x−1|. For s→−∞ the likelihood tends to zero in probability under stationarity and one uses the bounded overlap E min(1,likelihood)→0, not a moment bound uniform in s. For s→+∞ the long factor tends to 1 in L². The piecewise limits and monotonicity give the two stated mixing-time branches and rule out cutoff. The frozen checker was inspected, not run; its finite spectral and numerical tests are corroboration, not proofs of the limits.

## originality

PASS

The exact mixed Gaussian–triangle likelihood, macroscopic jump and plateau and their translation to this cut-first cactus family remain distinct in the compared literature. Homogeneous Gaussian Hamming profiles, coordinate productization and related product-chain examples of non-cutoff are prior ingredients, not new general phenomena claimed here.

## value

PASS

This specifies an exact example where one fast collective transition drops total variation only to a positive plateau, and resolves the profile while the two scales interact. The full product likelihood gives information that cannot be read off from separate marginal TV curves or a no-cutoff criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
