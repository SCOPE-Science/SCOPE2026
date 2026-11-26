---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The formula is correct for the ordered pair of rows on the fixed-zero binary path. Independently, put q=n+1 and represent u_i(t)=z_(t+i)+z_(t-i) using indices modulo 2q. This solves the update with both boundaries zero. The kernel of the map to rows at times 0 and -1 consists exactly of sequences invariant under the two reflections centered at 0 and -1, hence of sequences constant on each parity class. The kernel has dimension 2, so the paired-row map is onto and conjugate to shift on that quotient. For the t-shift, let d=gcd(2q,t). Its difference map has kernel dimension d and image characterized by a zero mod-two sum on each of its d cycles. Intersect that image with the two-dimensional parity subspace and subtract 2 for the quotient. For even t, each cycle has constant parity; the intersection has dimension 2 if 2q/d is even and 0 otherwise. For odd t, each cycle alternates parity, so the intersection has dimension 2 if q/d is even and 1 otherwise. These cases give D_n(t). Full nullity first occurs at t=2q: for u>1 all odd roots and full 2-adic multiplicity are needed; for u=1 the multiplicity 2^(a+1)-2 exceeds 2^a since n>=2. Period counts follow by Möbius inversion. A separate direct basis-evolution check (python3 /workspace/audit_evidence/waves.py) matched 1,357 nullities and checked exact orders for n=2..24; the proof, not the tests, covers unbounded n and t. No formal or expert certification is asserted.

## originality

FAIL

Exact statement-level coverage in the distinct indexed two-defect-tree result. Its theorem contains the same cyclic path-wave component and the full fixed-point, order and orbit formulas. A tree realizing the entire scoped family is obtained by adding one leaf to every vertex of P_n: the two spine endpoints are its only even-degree vertices, at distance n-1, and in spine/leaf coordinates its parity update is exactly the paired-row matrix. Thus m=n and q=2 give the frozen theorem for every n>=2, not just an upper bound or one example. The records share an indexed date; no inference of chronological priority is made. The failure is exact non-distinctness within the compared results, not a proof of historical priority or an access failure.

## value

FAIL

The complete orbit census is a natural, useful invariant rather than a random test or period bound. However, as a standalone finding it adds no supported new invariant to the indexed theorem: the same permutation and census are given explicitly and specialize through the spine-leaf construction. The alternative proof used for correctness verification is not a new standalone claim in the frozen result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
