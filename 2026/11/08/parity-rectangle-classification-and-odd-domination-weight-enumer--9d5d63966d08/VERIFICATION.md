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

Over F_2, the closed-neighborhood odd parity equation is x_ij=1+r_i+c_j. Row and column summation yields the necessary and sufficient consistency conditions (n+1)r_i=n+T and (m+1)c_j=m+T. Their four parity regimes classify all feasible labeled patterns uniquely; odd–odd patterns are (A×B)∪(A^c×B^c) with both |A| and |B| odd. Counting produces the complete weight enumerator; minimizing ab+(m-a)(n-b) over odd a,b yields the exact min-cardinality and all min multiplicities. Independent exhaustive neighborhood checks for every 2≤m,n≤4 reproduce every coefficient without using row/column parametrization; submitted two verifier sources were read. The symbolic derivation, not that bounded enumeration, proves the all-size theorem.

## originality

PASS

Peters–Goldwasser–Young (2017) prove universal solvability for Cartesian products and specifically classify whether Kn square Km is solvable, not the full weight polynomial of a single all-on target. Curtis–Earl–Livingston–Shader (2018) give a general Sylvester nullity method, not solution weight data. A published 2026 Hamming-product nullity formula determines only total solution counts, which are explicitly prior, and specifically disclaims minimum weight and weight histogram. Giffen–Parker treats parity domination and complete bipartite hosts, whereas the rook graph is the line graph L(Kmn). No inspected source yields the enumerator and minimizing patterns; historical risk remains from unindexed Lights Out coding theory.

## value

PASS

Beyond the prior kernel nullity and universal-solvability decision, the full weight distribution and exact minimum press patterns for the natural Cartesian rook board provide structurally interpretable parity-rectangle solutions. There is an all-(m,n) sharp parity dichotomy and nontrivial exact counts of minimizers, motivated by minimizing presses, rather than merely re-evaluating a known total. Algebra is elementary but the complete exact combinatorial classification is useful and mathematically natural.

The dated certificate retains the supplied scientific assessment, sources and limitations.
