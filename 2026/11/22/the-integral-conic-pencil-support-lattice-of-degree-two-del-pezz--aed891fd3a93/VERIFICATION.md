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

In the seven-point marking, the equations E²=K·E=−1 for a nonexceptional image of degree d give sum(m_i)=3d−1 and sum(m_i²)=d²+1; Cauchy gives 0≤d≤3. With r²=−2 and K·r=0 the same bound calculation gives |d|≤2. Independent finite enumeration of the norm-and-sum constraints recovers the 56 exceptional and 126 root patterns, with the exceptional types effective by the standard classification for seven points in general position. For F=−K+r all intersections with the exceptional classes are nonnegative; the independent enumeration finds 12 zeros, 32 ones and 12 twos, and verifies that each zero E has an exceptional partner F−E of intersection one. Distinct partner pairs are mutually disjoint, so two of their effective divisors give a basepoint-free pencil of class F. If its generic fiber were disconnected, the Stein factorization would make F a multiple of a fiber class, necessarily twice one with square zero and anticanonical degree one, contrary to the adjunction parity. Thus |F| gives a conic fibration and those six pairs are reducible fibers; conversely any conic bundle gives a root by adding K. Zero intersections characterize the supporting exceptional components and the matrix represents the unsigned formal labels, not Picard classes. A fresh 56×126 construction and exact integer Smith reduction gives 1^28,2^6,6,0^21, with rank 35. The inspected package's operation replay verifies unimodular row or column additions/swaps, including its row negation case, and checks a diagonal with the claimed divisibility. The transpose in the package preserves nonzero Smith factors, but the free cokernel rank comes from the 56-row map and is 21. The saturation quotient has order 384 and torsion exponent six.

## originality

PASS

The 56-vertex Gosset geometry with 126 twelve-vertex D6 supports is explicitly known. The strongest checked source uses these supports for signed quadratic equations, not for the integral cokernel of the unsigned support incidence. The closest checked catalogue records change the degree and incidence dimensions, use the same exceptional labels with a graph Laplacian instead, or treat Frobenius arithmetic. The bounded literature and catalogue comparisons did not produce a distinct exact Smith table or a theorem implying these unsigned factors.

## value

PASS

The support vectors are fixed by all conic fibrations of a standard del Pezzo surface, and the exceptional-curve labels carry canonical incidence data before one computes a matrix. The full invariant answers a precise reconstruction question: in what rank-35 rational subspace can integer support combinations fail to generate all integral labels in that subspace, and what obstructions remain there? The exact answer gives the index 384 and a genuine order-three class as well as seven independent 2-primary factors. This is potentially useful in comparing formal support relations or integral incidence lattices; neither a rank nor the older signed equations determines it. The conclusion does not assert a geometric Picard torsion phenomenon.

The dated certificate retains the supplied scientific assessment, sources and limitations.
