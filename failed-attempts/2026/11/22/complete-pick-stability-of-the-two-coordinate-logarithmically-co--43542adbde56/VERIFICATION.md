---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

On the finite summand the defect is D=B*B−I and the logarithmic-concavity difference is B*WB with B invertible. The two diagonal conditions and det W=(a²−1)(b²−a²)−a²|u|² give the exact stated region, and det D is nonnegative there. Multiplying the proposed basis by q gives q, az and z²,z³,…, which is a bounded invertible finite-coordinate change from the monomial basis; division by q is bounded and invertible because |u|<ab. The model intertwines directly. The cleared two-by-two matrices of R and H are positive on this region, including the degenerate boundaries; their determinant conditions check directly from the stated gamma, eta and x. Thus R is positive with diagonal less than 1, 1−tR is nonvanishing, and the defect decomposition is a sum of positive Schur products. The space has independent evaluations and the kernel is normalized and nowhere zero, so the normalized Pick criterion applies. At (2,3,1), det W=11, det D=23, and the 22 entry of D−A*DA is −18, so failure of ordinary concavity persists on an open subset of strict logarithmic concavity. verify.py was inspected, not run; its real rational examples are consistency checks, not evidence for all complex u.

## originality

FAIL

A distinct indexed result proves complete Pick for the same Hardy-block kernel on a strictly larger coupling range and gives the same exact logarithmic-concavity threshold after parameter relabeling. Disk rotation covers complex phases. The remaining edges are already covered by the equal-diagonal comparison or an elementary uncoupled kernel. The same-day observation is mathematical coverage, not a priority judgment.

## value

FAIL

A sharp operator-defect boundary and a CNP separation in a minimal block model would be meaningful, but the exact boundary and the claimed CNP sufficiency are already available for the same nontrivial model, with strictly more CNP coverage. Phase rotation costs no mathematical restriction, and the elementary uncoupled edges do not supply a distinct valuable remainder. No narrower repair is supported.

The dated certificate retains the supplied scientific assessment, sources and limitations.
