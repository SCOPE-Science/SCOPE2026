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

At a rational projective point the Frobenius minors vanish, and differentiating the minors gives the three displayed gradient equations. Vanishing excludes zero coordinates and gives Z=X³ in Y=1, then t⁷+kt³−1=0. Independently expanding the frozen-Frobenius part at (t,t³), the constant factor Z²+kX² there is 1/t, so the linear terms cancel. The quadratic in increments u,v is −2t⁸u²+(4t⁶−2/t)uv−2t⁴v², of discriminant 4(1−4t⁷)/t². Distinct tangents give a geometric ordinary node and their fields of definition distinguish split from nonsplit. At 4t⁷=1 the quadratic is −2t⁴(v+t²u)². For q≥5 the degree-three coefficient on v=−t²u is −1+2t³(t⁴+k)=1 by the singularity equation. For q=3, t=1,k=0; in F_3 the three summands on (1+u,1,1−u) add to u³+2u⁵, so the contact is again cubic. After shifting the transverse variable to the formal critical point (possible since 2 is invertible), the equation is a unit times w² plus u³ times a unit. Divide by the latter unit and absorb the square coefficient by a formal square root over the algebraic closure. This gives the stated cusp even in characteristic three, without assuming a cube root of a unit there. In the cyclic multiplicative group, t⁷=1 gives gcd(7,q−1) points at k=0, with the stated types and square class −3. The order of 3 mod 7 is six. The cusp locus t⁷=1/4 gives k=3/(4t³), injective on the solution set when p≠3 because gcd(7,3)=1, and all k=0 when p=3.

## originality

FAIL

The October 13 published record 7205bf0bad87 covers the same rational local classification, nodal splitting, and cusp-bearing parameters of the exact same pencil in reciprocal coordinates, and also provides local jets. The rational singular set already occurs in the Asgarli–Ghioca primary paper. The later and same-day neighbors do not decide this rejection; the earlier complete local result does.

## value

FAIL

Local types and splitting for a rationally singular member are natural invariants, but the substantive classification here is already available, with jets. The k=0 arithmetic instances and counts specialize those tests by elementary cyclic-group arithmetic; no independently useful unresolved invariant remains in the frozen finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
