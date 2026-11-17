---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Over R=k[epsilon]/(epsilon^2), D=A+epsilon B satisfies D²=0 iff A²=0 and AB+BA=0. Contractible unit pivots of reduction A split off r acyclic rank-two summands, leaving epsilon C on R^h, h=n-2r, with C induced on ker A/im A. With s=rank C, c=dim(ker C cap im C), cycles/boundaries show H(D)≅R^(h-s-c)⊕k^(2c), underlying k-rank(D)=2r+s. Counting square-zero A by kernel/image flags, q^(2r(n-r)) free lift parameters, and the rank-s C subspace intersection c yields N=[n r]_q[n-r r]_q |GL_r| q^(2r(n-r)) [h h-s]_q [h-s c]_q [s s-c]_q q^((h-s-c)(s-c)) |GL_s|, including all boundary cases. An independently implemented direct enumeration of all 2x2 matrices A,B over F_2 and F_3 satisfying original equations reproduced all (r,s,c) counts (F2: 1,6,3,6,12; F3: 1,24,8,48,72). This exhaustive small-size check corroborates the general flag proof, not replaces it.

## originality

PASS

Strongest comparison is earlier published length-two chain-ring Bockstein equidistribution, which counts residue rank and image/Smith shape from rank C, and split-local-algebra square-zero joint rank distribution in all radical dimensions. Neither records the intersection c=dim(ker C cap im C) required to determine R-module homology, and same-rank/Smith example epsilon diag(1,0) vs epsilon J2 has distinct homologies R vs k². Thus earlier broader rank laws do not logically imply the complete homology-type profile. Avramov–Buchweitz–Iyengar gives general differential-module structure without this specific finite-field labeled count. Residual risk of an unlocated general homology type census remains.

## value

PASS

Homology module type is a central intrinsic invariant of a differential, strictly finer than the underlying-field homology dimension and differential Smith shape. Exact joint distribution, parity-even residue torsion multiplicity, and the explicit smallest example separating equal-Smith differentials are meaningful algebraic information for complexes over singular local rings, beyond routine rank recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
