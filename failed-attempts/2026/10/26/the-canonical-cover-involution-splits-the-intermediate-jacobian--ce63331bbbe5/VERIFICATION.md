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

For Sarikyan's smooth complex (2,2,2) canonical cover, the source gives the eight isolated fixed points. Expanding the normal-bundle formula gives the cubic Chern coefficient 35-126+168-80=-3; the degree is eight, so the Euler characteristic is -24. Weak Lefschetz and duality leave four one-dimensional even groups and no odd groups except H^3, so b3=28. A finite-order holomorphic action linearizes at a fixed point; isolatedness excludes a +1 direction and the real Lefschetz index is +1. The traces on the even groups are +1. Thus the odd trace is 4-8=-4 and the ordered multiplicities are (12,16). Adjunction gives K_V=O_V(-1); the only pieces in H^3 are conjugate H^{2,1} and H^{1,2}, giving (6,8) on either. The images of 1±sigma on the abelian intermediate Jacobian have these dimensions and their addition has invertible differential, hence is an isogeny. This makes no integral or polarization assertion. The supplied script checks only exact arithmetic; the geometric inputs and the universal argument were checked separately, not certified by the script.

## originality

PASS

No matching statement of this cover's evaluated eigenspace dimensions or intermediate-Jacobian isogeny was found in the inspected sources. This is narrowly credit for a distinct stated evaluation, not for the construction, the fixed-point count, the fixed-point formula, or the general isogeny construction. Its mechanical derivation is a separate reason not to accept it as a research contribution.

## value

FAIL

The cover and equivariant Jacobian are natural objects, but the specific numerical decomposition is a routine consequence of the already known eight fixed points, the standard complete-intersection Betti calculation and Lefschetz. Passing to the images of 1±sigma is formal. The record adds no factor identification, polarization information or nonroutine invariant beyond this mechanical deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
