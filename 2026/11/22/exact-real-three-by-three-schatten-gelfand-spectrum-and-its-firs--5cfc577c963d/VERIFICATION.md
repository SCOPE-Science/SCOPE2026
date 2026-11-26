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

The numerical table survives unchanged in the repaired RESULT.md. In a codimension-at-most-three real space, the 3-by-3 matrix whose rows are u^T B_i for the annihilators has odd determinant on the connected unit sphere. At a zero, a nonzero kernel vector v gives nonzero rank-one uv^T in the space. Thus every test at k<=4 has ratio one. A real matrix two-plane has a nonzero singular matrix by the same antipodal determinant argument on its coefficient circle; no nonzero pencil element is lost because the basis is independent. The finite-dimensional power-mean bound at rank at most two gives 2^(1/q-1/p) from below through k=8. The five-dimensional symmetric traceless witness has spectrum (M,-a,-b) up to sign/permutation, with M=a+b and a,b>=0. Its p-sum is at least 2M^p by subadditivity, its finite q-sum at most 2M^q, and its infinity norm is M. The signed rank-two diagonal realizes equality. The codimension-four witness is admissible at k=5; the bound then holds at every larger index. The scalar line attains the universal rank-three lower bound at k=9. Both endpoints p=1 and q=infinity obey these inequalities. The source's incidental fixed-rank equality sentence was corrected: the upper ratio one occurs at rank one, not at every fixed rank with equal singular values. The two-row restriction and classical skew normal form reductions in the repair were checked separately.

## originality

PASS

The frozen novelty assertion for k=4 fails: the prior exact real 2-by-3 c_4=1 implies the square c_4=1 by zero-row embedding and restriction, even though the prior theorem does not explicitly mention square matrices. This is a demonstrable implication, not a priority conjecture. The repaired claim narrows originality to the sharp real square upper bound at k=5 with a five-dimensional witness and its consequent first-drop classification. It gives the complete table as context, credits k=4,8,9, notes that k=7 is independently recoverable using classical skew normal form and the known c_8, and treats k=6 as a consequence, not a separate novelty claim. No inspected source gives the k=5 matching upper bound.

## value

PASS

The surviving c_5 bound is at the first codimension permitting rank-one avoidance and is exact across the stated exponents; it identifies the five-plane that attains it. At that same index the complex value is one, so the result quantifies a scalar-field difference at the first affected width. This is a motivated exact boundary of the natural measurement invariant, not a recomputation of the credited indices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
