---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In barycentric subdivision every simplex is a strict chain, and a setwise stabilizer fixes all its vertices (face cardinalities distinguish them). The geometric quotient has one open cell per orbit, with signed chain deletions; no degree associated to a stabilizer multiplies an incidence. The multiset of directed birth-color words classifies exactly these orbits, including isolated vertices as the remaining label budget. I independently generated actual chains of arc-subsets using one maximal-face representative for each path-size partition and canonicalized by its equal-size-path stabilizer. I computed ranks and integral invariant factors of each original differential separately. Torsion in H_d equals torsion of coker(∂_{d+1}), since the quotient by the embedded H_d is im(∂_d), which is free. The sole nonunit factors were 2 in ∂₂ at n=4 and 2 in ∂₄ at n=6 and 7; the ranks recovered all stated free summands, including the mixed H₃ at n=6. H₀ is Z at every size, and there are no cells beyond dimension n−2.

## originality

PASS

Credit the distinct all-degree integral geometric-quotient calculation, especially lower-degree free and torsion phenomena, not the already covered parity of the top rational quotient homology. No stronger accessible statement or database table was found that supplies the remaining integral groups. The highest-overlap indexed record could not be inspected beyond its statement summary, so this is a bounded decision.

## value

PASS

Geometric quotients of this canonical relabeling action differ from invariant homology of the ordered complex. The finite first-size classification finds integral phenomena invisible to rational top homology: order-two classes appear, disappear, and reappear across the range, with mixed free/torsion H₃ at n=6. This is a concrete benchmark for studying the nonfree quotient action.

The dated certificate retains the supplied scientific assessment, sources and limitations.
