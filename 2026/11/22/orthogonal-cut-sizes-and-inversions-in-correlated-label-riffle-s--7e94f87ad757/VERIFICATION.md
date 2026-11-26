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

For one inverse shuffle from the ordered deck, reversal at fixed cut exchanges I with K(n−K)−I; complement symmetry gives zero covariance from the regression. The constant one-label word forces I=0, while a word starting 1 then all zeros has positive probability and I>0. The signed-word expansion has coefficients a_i=n+1−2i, quadratic term −W²/8 and linear multiplier 1/4. In the many-switch limit, the martingale differences have conditional variance h(1+p). The geometric-tail coefficient replacement yields squared L² errors O(h⁻²) and O(n²/h²+n/h³) for the constant and linear profiles, negligible on scales n/h and n³/h. Omitting j=1 gives a normalized cross-bracket O(1/n), not an exactly zero finite bracket, and the diagonal brackets tend to 1 using the exact sum of squares n(n²−1)/3. The O((nh)⁻¹/²) maximal increments give Lindeberg in every projection. The centered quadratic term is negligible by E[W²]=O(n/h) and nh→∞. This recovers both stated normalizations and independence. In the Poisson regime the word represented by its constant-grid sign path gives exactly the normalized occupation and ordered inversion area; these maps are continuous at distinct interior jumps. The bounded statistics preserve zero covariance, while positive probability of zero occupation forces zero area and a single positive-to-negative switch gives positive area with positive probability.

## originality

PASS

On inspected evidence, the distinct contribution is the named two-statistic joint theorem with its regime change and finite conditional regression. The exact same-model marginal inversion laws, identity, and weighted-martingale setup are existing inputs, not novel here. The evidence does not establish historical priority.

## value

PASS

The natural cut records the two packet sizes and inversions measure reordering in the same shuffle. Exact decorrelation is compatible with dependence for every finite size and in one natural scaling window, yet the coordinates are jointly Gaussian and independent in another. This determines when an independence approximation for the two observables is defensible; the easy symmetry alone or a marginal CLT would not do so.

The dated certificate retains the supplied scientific assessment, sources and limitations.
