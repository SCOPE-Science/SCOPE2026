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

Incidence walks of length three give s+t+1 on flags and α on antiflags, yielding A³=cA+aK in characteristic two, where K is the all-ones cross-shore matrix. The row and column sums give AK=KA and A²K=(s+1)(t+1)K. For even α the cases are A³=A (T⁶=I with T²,T³ not identity) and A³=0≠A² (order 8). For odd α and both parameters odd, A³=K≠0=A⁴ gives a zero block of length four and order 8. The other odd-α cases give A⁵=A³ with a nonzero one-primary component; A⁴+A² detects exactly whether any zero block has length three. It is nonzero for mixed parity. For both parameters even, its vanishing is precisely A²=diag(J,J); uniqueness of joins and meets and the nontrivial degrees make this an even-order projective plane. Two distinct point basis vectors sum to a vector in ker A² but not ker A there, and the exchanged constant vectors give a size-two one block, yielding order 12; otherwise the zero block of length three and a one block give order 24. On a size-j adjacency block the wave characteristic polynomial is (X+1)^{2j} or (X²+X+1)^j depending on eigenvalue 0 or 1. The primary-factor kernel dimensions 1 and 2 respectively show there is one cyclic block over F2 in each case. Intersecting with X^k−1 gives the stated minima and factor of two; scalar extension preserves nullities, and Möbius inversion counts labelled primitive orbits. The inverse exists and the state space is finite, so no state has a transient. An independent binary matrix check on the triangle, affine planes of orders two and three, and Fano plane confirmed the four orders and all 96 fixed-space nullities for k=1,…,24 on those samples.

## originality

PASS

The generic reversible update and block/census method are established machinery; existing projective-plane, generalized-quadrangle and affine-plane results give exact proper subcases. The surviving distinct result is the parity and plane-exception classification for all realized partial-geometry incidence graphs, with a single six-nullity formula. The inspected graph/design statements do not supply this general classification by substitution.

## value

PASS

The complete order law isolates a recognizable geometric exception to the 24-step behavior, and explains why a non-plane may have a different period from a plane of the same parity. The six small adjacency nullities give every orbit population without enumerating a state space of exponential size. This goes beyond listing a few example periods or transferring a generic reversible recurrence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
