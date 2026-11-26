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

Reduction splits by constants, and the additive reduction kernel is sl₂(k) because 2 is invertible. Involutions in the residue group are exactly the nonsingular trace-zero projective lines: Cayley–Hamilton proves both directions. The singular locus x²+yz=0 has q+1 projective points (q with y=1, one with y=0), leaving q² involutions. The split ones correspond to unordered pairs of projective-line fixed points. The plus part of the projective centralizer is k[A]×/k×, cyclic of size q−1 or q+1; an eigenspace swap or field conjugation gives the reversing involution, yielding the stated dihedral centralizer and other-involution count, also at q=3. Every lift of exact order two has additive part in the two-dimensional −1 eigenspace. Equal-base lifts commute only when equal. For distinct commuting residue involutions, projective commutation forces anticommutation of the trace-zero representatives A,B, so A,B,AB form the three different simultaneous character lines of the adjoint action. The lift commutation condition matches exactly the AB coefficients, giving q disjoint K_(q,q)'s and exactly q neighbors per commuting fiber. Counting residue pairs and diagonals gives q⁶; the stated degrees and edge counts follow. The reduction kernel has odd order and the residue dihedral centralizers rule out elementary abelian 2-rank three. Thus the product is the unique common neighbor of each commuting pair. Each fixed ordered generating pair of a residue Klein four has q³ commuting lift pairs, one per lifted subgroup. The frozen q=3,5 checker was inspected, not run; those cases do not establish the arbitrary prime-power statement.

## originality

PASS

Standard ingredients include residue involution centralizers, the split congruence kernel, and coprime lifting. The supported distinct claim is the exact local commuting graph across reduction fibers, together with how it accounts for the all-odd-field degrees, triangles and subgroup lifts. Checked field-level results and related finite-ring counts do not describe this projective biclique incidence. This is a bounded best-of-knowledge result.

## value

PASS

Commuting involution graphs are standard group invariants; split dual numbers give a natural first nontrivial congruence extension. The classification gives the local relation above each edge, including complete components, independent fibers and unique triangles. That is more informative than the aggregate count q⁶ or an extrapolation from two small fields and is useful when comparing which features of a residue graph survive congruence lifting. No global isomorphism classification or extension to other rings is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
