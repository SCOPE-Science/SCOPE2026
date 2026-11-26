---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The formula holds. Three greedy arches are sufficient by matching one bit per arch and necessary because the sequence of arch-terminal bits followed by a bit absent from the remaining suffix fails greedy matching. An independent count for a,b≥3 avoids generating functions: there are two one-arch words, no zero-arch words, and exactly a−1 words with two arches of the form 0^j1 (the suffix must supply the remaining ones), or b−1 with two 1^j0 arches. Each mixed orientation contributes 1+(a−2)+(b−2) by splitting into empty, all-zero and all-one suffix cases. The sum is 3(a+b−2). If either count is below three, 000 or 111 is missing. This covers n=0 and all other boundary cases and justifies the conditional probability by division by the binomial count. The supplied script was inspected, not run; its reported test of every word through length 16 is corroborative only.

## originality

FAIL

The deficit is a short count of six completely specified avoider families already characterized in Fazekas–Huang–Mercaş, arXiv:2610.06717, Lemma 4.3 and proof. This is demonstrable prior implication, not just an algorithmic antecedent or a title match. A separate indexed finer census explicitly contains the exact deficit as a marginal; its later catalogue date and lack of a citation to the frozen finding do not settle historical priority.

## value

FAIL

Fixed-composition universality is a natural census and the flat deficit is a useful simple form. But this record's sole claimed contribution is that invariant, which is already obtainable from the classified length-three avoiders by a short overlap count. The bivariate arch proof is concise but does not establish a further result beyond this mechanically covered census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
