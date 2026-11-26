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

Direct invariant-moment rederivation: average over S_n and global inversion on H_n. Odd degrees vanish, the degree-two invariant is p₂, and the quartics are spanned by p₂² and p₄ because p₁=0. On the unit sphere p₂=1. The squared coordinates on a vertex have values (n−k)/(nk) and k/[n(n−k)] with multiplicities k and n−k. Thus p₄(u_S)=n/[k(n−k)]−3/n. The squared norm of the projection of e_i to H_n is (n−1)/n; the sphere fourth projection formula in dimension n−1 yields sphere mean p₄=3(n−1)/[n(n+1)]. Equality is exactly the stated criterion and suffices for real or complex polynomials through degree five. The source tensor expansion is consistent: index partitions give A=3−6c₂+3c₄ and B=−2+8c₂−6c₄ using the zero-sum condition. With t=n−2k the criterion becomes (n−1)²−3t²=1. The positive fundamental unit is 2+√3; excluding j=0,1 gives n≥8 and 0<t<n−2, with n−t even from the Pell equation modulo 2. Complements give the opposite choices of k. At k=n/2 the signed multisample has constant multiplicity two and fails the moment condition for n≥4. Confirmed 2 C(27,6)=592020. Inspected CHECK.py and VERIFICATION.md without running; their recorded finite rational and subset checks supplement the proof.

## originality

FAIL

The central if-and-only-if and entire Pell family are covered by the directly inspected quadratic-harmonic/projective-design Resultary theorem for the same normalized hypersimplex vectors. Antipodal lift makes projective 2-design exactly spherical 5-design here, and the latter's extra endpoints n=4 and k=1 supply no new solutions by the immediate fourth-moment check. The dates do not establish independent priority or misconduct; the decision rests on mathematical coverage together with the short general invariant-cubature deduction. The specific node count is arithmetic on the already listed pair (27,6). No distinct surviving central claim supports a repair.

## value

FAIL

An infinite exact fifth-design family on these orbits is an intrinsically natural question. But the deliverable beyond the stronger exactly classified projective family is only the standard antipodal lift and multiplication of its known node count by two. The explicit projection fourth moment is also obtainable by a two-value coordinate calculation and the general invariant cubature criterion. No new exact invariant or useful range left unresolved by the checked result is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
