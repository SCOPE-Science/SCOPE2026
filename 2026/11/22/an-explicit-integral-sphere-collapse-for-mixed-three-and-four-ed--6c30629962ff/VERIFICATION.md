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

At each stage the lower faces carry a fixed mandatory marker (both poles, then one pole, then a_i), and every face with that marker pairs along a single pivot b_1, beta_1, alpha_1 or c_i. All remaining competing one-vertex extensions of a lower face also carry the marker and omit the pivot, so have been removed by larger lower faces. Any higher coface would force a competing one-vertex extension. The counts are respectively 2^(m-1), 2 times 3^m 2^(q-1), and the sum of 3^(i-1)5^(m-i)3^q over i=1,...,m. The last stage contracts each interval component a_i c_i to c_i, not to the empty set. The survivor join of m+q two-point factors is precisely the named crosspolytope boundary. The degree hypothesis makes the two poles intrinsic; deleting them identifies the paths by length, proving the automorphism group. The invariant pole-free inclusion is a homology isomorphism even though the chosen elementary collapse is not equivariant. On degree-zero reduced homology reversal preserves the two long-factor components and swaps the two short-factor components. Joining the difference cycles gives a generator; transposition of two factors exchanges two vertices in every joined simplex and contributes minus one. Hence the stated integral character holds.

## originality

PASS

Prior theta results give substantial homotopy-level overlap, especially the three-arm classification, and an earlier all-short family has a closely related character. Neither specifies or entails the mixed-family collapse onto the named subcomplex together with its integral symmetry action. The count is a consequence of the specified collapse/survivor and is not being credited as an independent advance.

## value

PASS

A natural finite graph family tests where the ternary criterion stops applying and where the all-short circle disappears. The fixed simplicial survivor and separate integral symmetry character give usable information about those independence complexes beyond sphere homotopy type. The closed count is useful for replay but is not the primary value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
