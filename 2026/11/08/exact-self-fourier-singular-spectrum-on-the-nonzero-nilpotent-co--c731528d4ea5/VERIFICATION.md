---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Parameterize every nonzero square-zero X by X_(t,s)=s u_t u_t^T J, t in P¹(F_q),s in F_q×, yielding q²-1 elements and trace pairing tr(X_(t,s)X_(r,v))=-sv det(u_t,u_r)^2. Decompose scalar fibers by unitary multiplicative characters. Trivial character block qI-J has singular 1 once and q (q times). Nontrivial characters give a Gauss sum of modulus sqrt(q) times projective Kχ; if χ²≠1, fractional-linear cross-ratio bijects q-1 off-diagonal points to F_q×, giving KχKχ*=qI. Odd-field quadratic χ gives K=J-I and exceptional sqrt(q) repeated q and q^(3/2) once. This yields exactly q²-1 total levels and universal invertibility; q2 boundary included. Independently assembled finite prime-field matrix and numerical SVD at q=2,3,5,7 (matrix sizes 3,8,24,48) reproducing full multiplicities. All q proof is algebraic, not finite extrapolation.

## originality

PASS

Earlier invariant-function Fourier transforms (Kawanaka/Letellier/Taylor) concern adjoint-invariant subspaces and representation-theoretic transforms, not an arbitrary complex-function square self-restriction with all singular values. A 2026 same-day general rank-one full matrix-cone Fourier result uses the larger *all rank-one* domain and coordinatewise pairing; it does not determine a smaller square-zero cut and trace-paired spectrum. A Veronese half-cone theorem has only square-scalar fibers and demonstrably different q=25 behavior (rank defect), while the current cone has every nonzero scalar and is invertible. Another 3x3 nilpotent **convolution** theorem uses frequencies throughout M3, not 2x2 restricted sampling. Best-of-knowledge O with Kawanaka original full text inaccessible, recorded.

## value

PASS

The punctured minimal nilpotent cone is a natural representation-theoretic variety and finite restricted Fourier sampling is a natural exact inverse problem; sharp singular multiset, universal injectivity and condition number distinguish even vs odd characteristic. The theorem provides a complete all-prime-power boundary, not a table or arbitrary parameter tuning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
