---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Use the established logarithmic-time finite-small-cycle functional limit for Ewens CRP, at fixed θ>0 and fixed integer k≥1, to identify L=∫_0^1 1_{Y(log t)=0}dt where Y is stationary M/G/∞ tandem stages rates 1,...,k. The total service duration S_k equals the maximum of k independent unit exponentials, with survival 1−(1−e^{-u})^k, mean H_k and integrated survival φ_k(e^{-d}). For ordered times, the Poisson forbidden intervals have total intensity θH_k+θΣ_{i=2}^s φ_k(exp(−gap_i)), yielding exact multitime zero probabilities. Order and ratio-change the s integrals (Jacobian u^{s−1}∏r_j^{j−1}) to get E L^s=e^{-θH_k}∏_{j=1}^{s−1}j∫_0^1r^{j−1}e^{-θφ_k(r)}dr. Taylor/Beta estimates give q_j=1−θ/j+O(j^-2), positive convergent renormalized product and moments ~C_{θ,k}s^{−θ}; monotone interpolation and Karamata for W=−log L give P(L>1−ε)~C_{θ,k}ε^θ/Γ(1+θ). Correct derivation of k=1 variance. Independent numerical quadrature corroborated first two moments at θ=1,k=1,2,3, and φ_k identities; no finite check is presented as proof of functional convergence or Tauberian theorem.

## originality

PASS

The prior November 2 Resultary publication gives the ENTIRE k=1 derangement singleton-cycle moment-product and sharp ε^θ endpoint law, including the same constant: that specialization is expressly known, not the independent novelty. The audited contribution is the complete fixed arbitrary cutoff k≥2, where avoiding every cycle size 1,...,k creates a non-Markovian total-service void process with a different φ_k and prefactor; the proof derives exact joint-void factorization and every moment. Gnedin–Stark and Galganov–Ilienko establish limiting count processes, not these evaluated integrated laws in inspected relevant sections. This is a qualified best-of-knowledge result subject to older M/G/∞ occupation theory.

## value

PASS

The chronological fraction of stages without cycles up to cutoff k is a natural permutation-growth observable. Determining its complete limit distribution by moments and precise rare near-one probability for every fixed k≥2 yields a useful non-Poisson invariant and cutoff-dependent constants, beyond the existing k=1 calculation and mere process convergence. The exponent universality across all cutoffs is a specific structural statement motivated by the underlying queue tail, not an arbitrary reparameterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
