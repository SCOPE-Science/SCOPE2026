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

For synchronous OR, the relevant support comes from exact-length walks, not automatically from distance balls. Johnson distance is k−|A∩B|; replacing an edge by a two-edge path around a triangle, then inserting backtracks as needed, reaches either parity at all lengths at least the positive distance. Closed walks of lengths 2 and 3 handle distance zero for times ≥2. Thus at t=k−r the zero sites are exactly the k-cliques of uncovered r-faces. For a fixed tuple of h distinct sites, its e distinct faces have e·m_n+O(n^(k−r−1)) forbidden seed blocks by the union bound and the pairwise containment-family inclusion–exclusion bound. For fixed h the Bernoulli vacancy probability is uniformly n^(−ke/b)exp(−ce)(1+o(1)), since p²m_n and the overlap correction multiplied by p vanish. An overlap type on v labels has O(n^v) copies. Within each connected component of the site intersection graph, order the sites by a connected traversal. A new site with s labels already seen adds k−s labels and at least b−binom(s,r) faces, so the exponent v−ke/b changes by at most −s+(k/b)binom(s,r), strictly negative when 1≤s<k for r≥2 and nonpositive for s=k. The second site in a nonsingleton component is distinct and enforces strict negativity. Disjoint tuples alone contribute (exp(−bc)/k!)^h, giving Poisson convergence by factorial moments. By absorption of the all-ones state, earlier consensus would require a fixed site to be active at t−1, bounded by O(log n/n) from its candidate seed blocks even when t−1=1. Complete (r−1)-coverage follows by a union bound with vacancy exp(−Θ(n log n)); full r-coverage fails with high probability by a diverging mean and uniform pair-probability factor 1+o(1). At r=1, the uncovered-label Poisson law and the identity Y=binom(X,k) give a lower tail, not a Poisson zero count at the site level. All nonempty states fill by k and a singleton seed has a disjoint site not reached earlier. The two frozen scripts were inspected, not run. The nominal 26,180 figure counts update iterations, including time one where no ball assertion is made; the asymptotic proof does not use these diagnostics.

## originality

PASS

The original part is the sequence of interior vacancy-clique thresholds and their precise two-time consensus law. Ordinary Johnson geometry, general OR-network propagation tools and the r=1 uncovered-label Poisson law do not themselves constitute novel contributions. The earlier full-coverage results count a different obstruction at a strictly later scale; the usual independent-edge clique theorem does not apply to this dependent shadow without the additional joint vacancy argument.

## value

PASS

The exact-length network reduction poses a natural random coverage question that full coverage does not answer. For every intermediate update the theorem identifies a distinct scale and a sharp nondegenerate probability profile while showing that many faces remain uncovered. The failure of the same clique-count Poisson mechanism at the first-shadow boundary explains why the final pair of times has a different probability law. This is useful beyond a deterministic diameter bound or a first-moment threshold estimate, within the fixed-k scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
