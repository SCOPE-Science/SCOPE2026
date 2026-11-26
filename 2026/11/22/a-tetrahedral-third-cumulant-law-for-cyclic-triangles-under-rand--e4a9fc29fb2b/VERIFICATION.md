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

One triangle has probability 1/4 of being cyclic even conditional on the direction of any one of its edges. Distinct triangles share at most one edge, so all pairs are independent. Among three triangles, if one shares at most one edge with the union of the other two, it is independent of their pair by the same conditioning, giving the full joint law. Otherwise each pair shares a different edge. Starting with abc and abd, the third must contain ac and ad or bc and bd, hence is acd or bcd. The three shared edges are spokes at one vertex. Simultaneous cyclicity would require each pair of spokes to have opposite directions at that vertex, which is impossible. This gives centered mixed moment -1/64 in the exceptional case by pair independence. The all-equal term is 3/32, the two-equal terms vanish, and each exceptional unordered triple contributes six times -1/64. There are exactly four such triples per K4 and they determine the clique uniquely. Mean, variance and inversion for the clique count follow with the stated coefficients. Empty and short families and arbitrary fixed signed weights are covered; no assumption of biased or dependent edge sampling is used. The accompanying finite checker was inspected, not executed.

## originality

PASS

Pass is limited to the arbitrary-host classification of three cyclic-triangle indicators and its weighted third-cumulant consequence. The complete-tournament moment and the local four-vertex obstruction are prior, and are not credited as originality. Neither supplies the independent law for every nonexceptional triple or the arbitrary-weight formula. Related same-day findings were compared as distinct records without assuming ordering.

## value

PASS

This gives a complete structural explanation of where three-way dependence first appears in a natural family of pairwise independent indicators. The same local obstruction has a quantitative weighted law and recovers K4 count from two scalar cumulants, with no host regularity or asymptotic hypothesis. It is not a claim about inference from a bounded sample or about higher joint laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
