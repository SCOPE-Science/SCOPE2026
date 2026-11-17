---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

PASS: Normalize target p by y_i=x_i/p_i; A_ij=S_ij p_j. If Q_i is homogeneous quadratic, the target equilibrium fixes Q_i(1)=-r_i-sum_jA_ij; Euler homogeneity forces every Jacobian H to obey H1=w with w_i=-2r_i-sum_jA_ij. Conversely any such H is realizable by a partner-symmetric real tensor, for example the submitted quadratic formula Q_i(y)=(sum_j y_j)(g_i dot y)/n-q_i(sum_j y_j)^2/n^2, with g_i=H_i-A_i and sum g_i=2q_i. If w is constant c>=0, H has eigenvalue c and is not Hurwitz; if c<0, H=cI works. If w is nonconstant, choose f^T1=1, f^T(w+1)=0 and H=-I+(w+1)f^T. The rank-one correction squares to zero, so every eigenvalue is -1 and the construction realizes H at p. Independent exact arithmetic checked this square-zero identity and prescribed row sums for several nonconstant rational vectors. The proof covers n=1 and all real unrestricted tensors, not sign constraints.

## originality

FAIL

FAIL: complete direct prior coverage in the full October 27 published Resultary theorem. Set its h_i=2r_i+sum_j S_ij z_j=-w_i and z=p. Its necessary-and-sufficient criterion h nonconstant or a positive constant is precisely the current w nonconstant or a negative constant. Both exhibit a compatible square-zero rank-one Jacobian with eigenvalues all -1 and show constant nonnegative obstruction. The earlier construction uses only repeated-partner T_ijj terms, a stronger restriction. This paper is not new.

## value

FAIL

FAIL for the submitted final result, despite the underlying sharp ecological design classification being mathematically meaningful: identical universal criterion and sharp constructive/obstructed cases were proved previously. Alternate quadratic implementation and a different illustrative matrix are not a distinct valuable scientific claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
