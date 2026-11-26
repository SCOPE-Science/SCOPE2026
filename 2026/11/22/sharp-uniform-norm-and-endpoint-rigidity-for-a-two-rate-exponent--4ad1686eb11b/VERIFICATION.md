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

Scale time by a, set R=b/a>1 and w=e^(−(R−1)t), u=e^(−t). The Gram entries 1/2, 1/(R+1), 1/(2R) give determinant (R−1)²/[4R(R+1)²]. Inverting and changing input variable to z=e^(−s) gives the row integral Du∫_0^1|A+Bz^(R−1)|dz, with D=2(R+1)/(R−1)², A=R+1−2Rw, B=R((R+1)w−2). The signed integral inside equals (R−1)(1−w). The endpoint row is 2(R+1)(Re^(−Rs)−e^(−s))/(R−1), with unique zero at log(R)/(R−1) and total signed mass zero. Twice the positive mass yields L(R)=4(R+1)R^(−1−1/(R−1)), and the sign step attains it by continuity up to the boundary even in the open-half-line essential supremum. To exclude later rows, put z_*=R^(−1/(R−1)). In the early mixed-sign region w>(R+1)/(2R), solving for the zero gives z_0≤z_*; integrating below it and bounding by z_* gives J(w)≤uL(R)+2(R+1)u(1−4z_*)(1−w)/(R−1)≤uL(R), with z_*≥1/e. In the nonnegative region 1/R≤w≤(R+1)/(2R), differentiation of w^(1/(R−1))(1−w) gives its maximum at w=1/R and the row bound L(R)/2. In the late region 0<w<1/R, integrating at the zero then bounding z_0≤1 gives J(w)≤[2(R+1)/(R−1)]w^(1/(R−1))((R+2)/R−3w). This bound peaks at (R+2)/(3R²). Its ratio Q to L(R) has log Q≤log((R+2)/(2R))−2/(3R), negative at R=1 and decreasing for R>1. This verifies the strict boundary maximum. The derivative of log L has numerator log R−2(R−1)/(R+1) over (R−1)²; the numerator starts at zero and its derivative is (R−1)²/[R(R+1)²]. The stated limits, R=2 check, and equal-rate rank-one norm 2 then follow directly. The unique zero and the norming step concern the boundary kernel row, not every kernel row.

## originality

PASS

The Gram inversion and sign-of-row arguments are standard. The distinct result supported by the checks is the fixed ordinary-measure, two-real-decay half-line norm, including strict endpoint dominance for every rate ratio and the sharp rate envelope. The inspected primary and local comparators do not entail it.

## value

PASS

The worst amplification of a bounded perturbation by a fixed least-squares projector is a natural stability invariant for decays. Its exact dependence on the ratio, locating the unique worst output and simplest saturating input, resolves questions that a Gram-matrix bound or pointwise endpoint computation alone does not answer. The discontinuity at rank loss is mathematically distinct from coefficient ill-conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
