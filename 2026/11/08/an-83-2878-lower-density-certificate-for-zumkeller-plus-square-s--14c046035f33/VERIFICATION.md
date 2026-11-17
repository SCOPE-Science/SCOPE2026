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

Coprime multiplication preserves Zumkeller divisor partitions; seeds 2^a p are Zumkeller when p<=2^(a+1)-1, and 70 has sigma(70)=144 with divisor subset {70,2} of sum 72. For each odd p the exact valuation-one square-lift event G_p mod p^2 has size (p-1)(p+2)/2: either nonzero quadratic-residue r mod p or p|r with p^2∤r. CRT and nested binary square-residue strata give ten-prime density 63520442937841228526/83108492151210387225. Mixed 70 event N mod4∈{2,3}, N mod25∈G_5, N mod49∈G_7 has event density (1/2)*(14/25)*(27/49); its intersection with old C is only p=3 event of probability 5/9, so incremental density is 12/175. Independent exact Fraction recomputation confirmed final 2768772438842683346/3324339686048415489=0.8328789174170931; inspect verify.py counts 6804−3780=3024 classes modulo 44100. CRT chooses positive square root x<=15376 and N>15376^2 ensures z=N−x^2>0; coprime Zumkeller seeds handle both constructions. Thus every large certified residue is representable; finite prefix irrelevant to liminf. No density-one assertion.

## originality

PASS

Published Somu–Kukla–Tran Proposition 4.11 supplies only ten of eighteen mod18 residue classes, lower density 5/9; its further results do not give this 70-support 83.2878% bound. Prior October 18 Resultary ten-prime sieve gives exactly the base 0.764307..., and its construction mostly requires a mod4 square. The new seed 70 exploits complementary nonsquare mod4 2,3, producing an independent provably additional 12/175. No dominating square-summand coverage arose in Resultary searches; results about Zumkeller + prime or cube are mathematically different.

## value

PASS

The motivation is the genuine open density of integers expressible as Zumkeller plus square. A constructive, fully rigorous periodic residue certificate raises the known lower bound by 12/175 (~6.86 percentage points) using a new natural mixed-prime Zumkeller seed 70, rather than merely recomputing the earlier ten-prime table; every certified class has a uniform constructive threshold. This is meaningful quantitative additive-number-theoretic progress short of density one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
