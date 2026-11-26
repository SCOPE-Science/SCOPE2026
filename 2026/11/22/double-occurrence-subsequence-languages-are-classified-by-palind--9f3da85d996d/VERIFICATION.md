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

Coordinatewise min and max preserve strict index increase, so the only two embeddings must be comparable. If different at two indices j<k, splicing the lower prefix through j and the upper suffix after j gives a third embedding. For the one differing coordinate, an occurrence can be altered if either adjacent selected symbol is inserted into its ordinary gap, or if the fork symbol or one of its existing target neighbors is inserted into its fork gap. Conversely the gap exclusions force greedy first and last occurrences to be precisely the designated tuples, which agree off the fork; the interval between them contains exactly two admissible choices at the fork. Thus the restrictions count all hosts once. For each fork there are two exterior gaps with q−1 letters, m−1 ordinary gaps with q−2, and a fork gap with q−2 in exactly 2+t cases and q−3 otherwise. Multiplying their geometric factors gives the full series, including when q=3 and a fork gap has no allowed letters. At length m+2 the coefficient differs by one per unit of t; for m=2 there is only one class. The labeled target count follows by independent choices of copying the penultimate letter or using a letter distinct from the last two. At z=1/(q−1), evaluation after removing the double pole gives (m+2+t)/(2(q−1)); other poles have strictly smaller exponential bases, and only the leading n term is retained. Independent bounded replay enumerated all hosts for (q,m,n)=(3,2,2),(3,2,3),(3,3,5),(3,4,7),(4,4,6),(3,5,7), aggregated each target's complete list of increasing index tuples per host, and matched every target and fork to the coefficient of its gap product. In particular 108 quaternary length-four targets against length-six hosts gave 5904 exact-two target-host pairs. These are finite checks; the greedy argument proves all lengths. The equivalence is equinumerosity, not equality of the labeled languages, and does not extend here to adjacent repeats or other multiplicities.

## originality

PASS

The distinct contribution is the all-length fork-sensitive formula and complete t-classification for nonbinary adjacency-distinct literal targets. An equivalent ternary all-distinct specialization is independently indexed on the same date and is explicitly not claimed as new in the frozen result. Priority between the two catalog entries is not established.

## value

PASS

Fixing multiplicity two exposes a complete statistic that is invisible at multiplicity one and degenerate in the binary case. Fork rigidity plus the gap factorization proves an exact classification across a natural infinite family, determines when classes first separate and their populations, and explains the dominant coefficients. The contribution is not a recomputation of 012 or a selection of small empirical differences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
