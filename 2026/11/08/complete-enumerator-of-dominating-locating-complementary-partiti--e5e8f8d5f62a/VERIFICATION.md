---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

Run `python3 verify.py` using Python 3.10 or newer. It requires only the standard library. The checker independently constructs each clique corona from the base graph edge list. For every candidate subset, it directly checks that the complementary class dominates the selected class, and that the selected class dominates and distinguishes all vertices outside it. It compares the resulting cardinality histogram against the binomial-subset formula and separately calculates \(\gamma(H)\) from the original domination definition.

The direct tests cover every labelled simple base graph of orders one through three with private clique sizes two and three, all labelled simple base graphs of order four with private clique size two, plus path and complete hosts of order four with private clique size three, and path and cycle hosts of order five with private clique size two. The tests total 90 graph/parameter profiles. On each tested profile, the coefficient histogram and exact minimum agree. Expected output ends with `CHECKS_OK 90`.

The unrestricted assertions for arbitrary finite base graphs and clique sizes at least two are established by the local necessity-and-sufficiency proof in `RESULT.md`, not by exhaustive finite experiments. The checker does not demonstrate novelty, inspect literature, or provide independent mathematical certification. No external audit has been performed.
