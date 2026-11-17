---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The assumptions lambda_n->lambda in (0,infinity), maximal individual edge probability eps_n->0 and weak convergence nu_n on compact [0,1] are adequate. For fixed m tags, hyperedges intersecting tags in exact subsets S give independent Poisson-binomial counts with mean sum_r binom(n-m,r-|S|)p_nr. The uniform O_m(1/n) hypergeometric ratio yields mu_S=int x^(|S|-1)(1-x)^(m-|S|) nu(dx). Le Cam error <=eps_n*m*lambda_n goes to zero and yields the correlated subset-shock limit. Construct PPP of intensity nu(dx)/x on (0,1] with independent Bernoulli marks and independent singleton dust of intensity nu({0}); finite intensity of sum_x x ensures almost-sure product. Tagged mixed moments identify the random conditional-iid empirical degree masses; a uniform expected-degree tail bound ensures l1 tightness. The Poisson exponential formula gives E P(0)=exp(-lambda), Var P(0)=exp(-2lambda)(exp(int x nu(dx))-1), and log E P(0)^k= sum_{j=1}^k (-1)^j binom(k,j) M_{j-1}; Hausdorff determinacy recovers nu. Rounded/clipped rank construction makes all finite measures attainable even with atoms at 0 or 1. Inspected actual check.py: finite tagged-pattern and rational-moment verifications do not replace these limit arguments.

## originality

PASS

Primary November 3 2026 Zhu–Xu–Reinert paper treats a fixed vector of vertex degrees via approximation by INDEPENDENT multivariate Poisson or normal distributions, explicitly with error terms controlled by shared hyperedges, and does not analyze non-concentrating empirical histograms under macroscopic ranks. Pal–Makowski distinguish nodal and empirical graph degree laws, but their general counterexample does not give this hypergraph PPP paintbox or isolate-moment spectral inversion. Bergman–Leskela target connectivity/isolation estimates, and Goldschmidt–Norris study collapse of Poisson hyperedges; no checked full text implies the complete random histogram law plus injective inversion. Originality remains best of knowledge subject to general exchangeable hypergraph paintbox theory.

## value

PASS

The deterministic-versus-random empirical-degree threshold at positive macroscopic hyperedge fractions is a natural and precise structural phase boundary. The explicit correlated common-shock law and nontrivial recovery of the whole hyperedge-size intensity from one isolate-fraction distribution answer measurable questions not settled by a marginal Pois(lambda) law; they are motivated by the distinction between one-vertex degree and empirical histogram and do not simply rename de Finetti.

The dated certificate retains the supplied scientific assessment, sources and limitations.
