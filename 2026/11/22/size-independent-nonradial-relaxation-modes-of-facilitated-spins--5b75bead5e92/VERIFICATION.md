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

With unit-rate refresh, minus the generator is D_A tensor P_B + P_A tensor D_B. Every centered linear B-shore contrast with zero coefficient sum is killed by evaluation at the all-occupied B configuration and has independent-refresh eigenvalue one. These n-1 contrasts therefore carry copies of D_A+P_A, and their products vanish at the isolated state. In the product Bernoulli scalar product, P_A removes the normalized all-occupied projector. The squared Fourier weights of that vector in Walsh degree k are binomial(m,q), giving the stated secular equation by a rank-one determinant; its left side increases from less than one to infinity on (0,1). Strict binomial stochastic comparison gives both monotonicities. The simple analytic root at q=0 has derivative m/2. Writing epsilon=1-lambda, the k>=1 sum in the secular equation stays bounded away from 1 as q tends to 1 for m>=2 (the mass is concentrated at m), which first forces epsilon to zero and then gives the limit of that sum as 1/m. At fixed q and growing m the same sum tends to zero by binomial concentration. At m=1 the equation gives epsilon squared equal to 1-q. Independent full-matrix diagonalization for five selected triples confirmed at least n-1 eigenvalues matching the secular root within 4.8e-15; replay: OPENBLAS_NUM_THREADS=1 python3 /workspace/reproductions/one_biclique_spectrum.py. The computation is finite and the general statement is about a branch and a gap upper bound, not an exact gap or exact multiplicity.

## originality

PASS

The leaf-contrast mechanism and exact m=1 gap are credited prior overlap. The evidence does not establish the m>=2 binomial-root branch over the entire biclique family, its multiplicity lower bound, and its change in high-vacancy exponent. Best-of-knowledge judgment on that distinct claim, not on priority of the contrast construction or rank-one lemma.

## value

PASS

This gives a concrete exact nonradial relaxation obstruction for a natural graph family at all vacancy densities, including many independent directions and a qualitative change from the star's high-vacancy exponent. It is informative even without identifying the full gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
