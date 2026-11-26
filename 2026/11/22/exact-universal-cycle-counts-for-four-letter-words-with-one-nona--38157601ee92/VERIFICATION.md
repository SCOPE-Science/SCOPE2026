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

The two overlap vertex types and the three arrows follow from the actual windows. The graph is balanced; rotations, reversal via a two-edge path, and substitution of one letter connect the distinct triples and attach every repeated-endpoint triple. For the outgoing Laplacian the rotation block has determinant (s^3-1)^(n/3). Eliminating it gives the stated pair-space operator: the first term of the inverse sums along a row, the second along a column, and the third transposes the ordered pair. The off-diagonal symmetric row-sum map has rank q (its dual kernel would require y_i+y_j=0 on every pair), and the skew row-sum map has rank q-1 (its dual kernel consists of constants). The constant and centered additive spaces supply the remaining dimensions. On the constant space the eigenvalue simplifies to t(t+q-1)(s^2+s+1); on centered additive arrays the two-by-two block gives determinant 14q(q-2) at t=0. Balanced strong connectivity makes the derivative at zero the number of vertices times the common rooted cofactor. BEST with a fixed initial arc multiplies by the factorials of outdegree minus one, and this uniquely fixes rotation since that arc occurs once. Initial letters of edge labels give the claimed frequencies. An independent exact direct-cofactor computation matched q=3,4,5,6, including both printed integers, and directly checked the q=4 witness windows: `python /workspace/audit-replay.py 1`.

## originality

PASS

The supported distinct content is the exact product for the labeled nonadjacent-repeat edge set at all q>=4. Neither the known ternary boundary nor the use of BEST and the cofactor theorem is credited as new.

## value

PASS

The nonadjacent one-repeat patterns form a natural complement to the adjacent-repeat motif class and a strict restriction of local square-freeness. The exact all-alphabet enumerator distinguishes these combinatorially close problems and supplies a formula beyond an Euler-existence argument or a small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
