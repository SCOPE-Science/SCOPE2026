---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

Exact FK component count k(omega)=N_0+kappa(H_n) gives Z=W_n^n E_{nu^n}[q^{kappa(H_n)}] with W=1+(q-1)prod_i(1-p_i), nu(S) proportional to q^{1_{S empty}} Bernoulli column mass. The finite-core tilt lies between min(q,q^r) and max(q,q^r). Singleton probabilities a_i/(q sqrt(n))+O(n^-1), pair probabilities a_i a_j/(qn)+O(n^-3/2), higher connectors O(n^-3/2). Multinomial log-mgf yields independent pair Poisson means a_i a_j/q and independent n^(1/4) singleton Gaussian variance a_i/q. Tilt only depends on limiting finite pair graph; rare multi-hub vertices are tight and contribution O_P(1). This proves joint finite FK projected graph and component-selected Gaussian, with correct 2-hub connectivity (exp(a1 a2/q)-1)/(q+exp(a1 a2/q)-1). Independent rational enumeration matched unnormalized exact FK/column reductions for K_{2,3} and q=1,2,3/2. All fixed r>=2, q>0, a_i>0, n large enough; not growing r or uniform rate.

## originality

PASS

Against full submitted theorem and inspected sources: Natural specific formula distinct from checked prior claims, with clear residual priority risks. Exact fixed-hub crossover at edge scale n^-1/2 in FK model yields a finite dependent random-cluster core and n^1/4 conditional Gaussian fluctuations. It identifies why q≠1 cannot be replaced by independent bond thinning;

## value

PASS

Exact fixed-hub crossover at edge scale n^-1/2 in FK model yields a finite dependent random-cluster core and n^1/4 conditional Gaussian fluctuations. It identifies why q≠1 cannot be replaced by independent bond thinning; the exact partition reduction and finite-core transition are independently useful, not a trivial q=1 substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
