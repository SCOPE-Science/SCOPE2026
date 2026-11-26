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

An independent standard-library replay from the frozen edge list and displayed generators gave face counts (12,60,120,60,12), mod-two boundary ranks (11,49,48,12), and group closures of sizes 60 and 120. The augmentation rank is one. The mod-two ranks bound rational ranks below; the augmentation kernel, the preceding boundary kernel and the twelve top columns bound ranks above, including rank ∂3≤60−12. This forces rational homology only in degree 2, of dimension 23. The full group has at most 120 elements: an ordered triangle has only 120 possible images, and fixing its vertices forces the adjacent triangles across their edges and propagates through the connected dual graph. The proper subgroup is the geometric rotation subgroup (order 60, isomorphic to A_5), and the central antipode is outside it. Signed fixed-face enumeration, with the reduced augmentation, gives rotation traces (23,3,−1,3) and the matching antipodal-coset traces (−1,−5,−1,−1) over orders 1,2,3,5 of the rotation factor; both order-five classes agree. Taking half-sum and half-difference gives even (11,−1,−1,1) and odd (12,4,0,2). The A_5 character table gives V_6+V_5 and 2·1+2·V_5, respectively; the two complex threes are Galois conjugates and occur together with multiplicity one in the rational six-dimensional constituent. Barycentric subdivision removes simplex inversions. The quotient chain complex over Q identifies with coinvariants (hence invariants by averaging), and exactness of averaging gives quotient homology equal to homology invariants. This gives degree-two dimensions 2 and 0, with all other reduced degrees zero.

## originality

FAIL

The October 11 Resultary record 5d7e0af98d39 gives the identical rational representation on the same open neighborhood complex and the same rotation/full invariant dimensions. Its wording need not state the Betti numbers of geometric quotients: the standard characteristic-zero finite quotient argument immediately gives them from those dimensions. The October 4 wedge type by itself is not the reason for rejection.

## value

FAIL

The representation of this natural graph complex could be worth knowing, but it is already known with the exact class data. The only change is the routine identification of previously computed fixed dimensions with rational quotient homology. There is no remaining independently useful unknown exact invariant in the frozen claim; independent replay corroborates correctness but does not supply one.

The dated certificate retains the supplied scientific assessment, sources and limitations.
