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

# Verification record

Run `python checker.py` to reproduce exact-rational checks. The checker passed 4,221 assertions on the exact discrete summation-by-parts and quotient identities, on clock mean-preserving spreads, and on the gambler's-ruin boundary examples with intervals of lengths \(4,6,8,10\), positive rational transition probabilities \(1/3,1/2,3/4\), and all non-midpoint starting sites. The proof of the infinite-clock characterization is analytical, not numerical: it follows from a stop-loss coefficient expansion with summable second differences, a two-endpoint affine test, and a converse local spread. The midpoint case uses reflection of paths and an exact ratio of their probabilities.

The finite checker is a regression certificate, not exhaustive enumeration over all clocks or a substitute for the proof. The source paper arXiv:2611.01756v1 was inspected in its openly available full HTML version. The 2019 Vidmar article was consulted through its accessible abstract and publisher opening sections; other cited comparisons have limited available text, which is not evidence of global absence of an equivalent theorem.
