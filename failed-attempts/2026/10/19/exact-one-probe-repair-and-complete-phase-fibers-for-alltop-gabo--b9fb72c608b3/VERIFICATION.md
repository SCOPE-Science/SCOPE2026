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

For any nontrivial additive character, sums of psi(ct) vanish at c nonzero even over extensions. Distinct h shifts reduce to a planar B; expanding the squared correlation by differences yields q from zero lag and zero from each nonzero lag. Thus the q bases and the coordinate basis form a complete MUB. Their centered projector spans are mutually orthogonal, each of dimension q-1, with the coordinate traceless diagonals exactly the omitted subspace. Consequently equality of data is exactly equality of norm and off-diagonal products. One nonzero off-diagonal pair identifies a two-point support if it is the sole unordered pair; the norm and product give the two roots for squared magnitudes, with phases fixed relatively. On at least three sites the three-product ratio recovers each squared magnitude, and vanishing off-diagonals leaves impulses (or zero). The extra probe sees each nontrivial lifted difference as a nonzero multiple of one squared-weight difference, so distinct weights are necessary and sufficient and add one real rank direction. Sorted unit squared weights satisfy z_j >= j delta for minimum separation delta, including the trivial delta=0 case; equality gives exactly the proposed optimizer, which is valid even with one zero coordinate.

## originality

FAIL

The claimed sharp one-intensity repair and lifting rank are mechanically implied by prior complete-MUB linear inversion and the prior rank-two criterion, applied to the known Alltop MUB completion. This is actual implication, not a keyword match: subtracting the prior inversion formula for two normalized states with the same measured q bases leaves precisely a traceless diagonal difference in the omitted basis. Passing from this known subspace to the repair is just excluding a zero coefficient on each diagonal difference e_i e_i^* - e_j e_j^*. I did not find the full list of fiber sizes and the squared-weight optimizer printed together; that does not restore the claimed distinctness of the central repair theorem. The result is mathematically true.

## value

FAIL

The design motivation (reuse measured chirp bases with little extra acquisition) is sensible, but the claimed contribution does not add a structural phase-retrieval result once the prior omitted-basis reconstruction and rank-two criterion are accounted for. The fiber list just enumerates rank-one factorizations with given off-diagonal entries and trace; its only nontrivial support case reduces to swapping two roots of a quadratic. The remaining optimum is equally spaced weights on a scalar simplex and controls only basis-impulse discrimination, not a stability property of the recovery problem. No valuable distinct remainder has been established by recombining those elementary consequences under the Alltop name.

The dated certificate retains the supplied scientific assessment, sources and limitations.
