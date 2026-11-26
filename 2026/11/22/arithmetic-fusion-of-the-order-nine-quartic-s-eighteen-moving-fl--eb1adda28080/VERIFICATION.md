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

The three partials cannot vanish together in characteristic zero or seven: off infinity F_Z forces Y=0 and then F_Y is nonzero; at infinity F_Y forces X or Y to vanish and then F_X is nonzero. The Hessian determinant expands to 54Z(8X³Y²−2X²Z³−Y⁵). Its second factor is nonzero at the four transverse infinity intersections, which split over Q as two rational points and a conjugate pair. At the affine origin the tangent is y=0 with contact four; the local equation has y of order four in x, so the Hessian has order two from −2x². At a nonzero affine intersection set t=xy² and s=x⁴/y. The two equations give s=−(t+1) and (8t−2)s=t², hence 9t²+6t−2=0 and x⁹=t(t+1)²=(9t+8)/27. Conversely t=3x⁹−8/9 and y=−x⁴/(t+1)=27x¹³−11x⁴ recover both equations from P(x)=0 over either field. Thus this recovers the affine support without relying on the packaged Gröbner basis. The 18 roots are simple, and the 18 affine points, the four infinity points and the weight-two origin exhaust degree 24. Independently modulo 7, u=x⁹ satisfies u²+3u+5=0 with nonsquare discriminant 3, so u is in F_49 and its norm 5 has order six. Since the norm is u^8 and order(u) divides 48, u has order 48. Every x above it has order 432; ord_432(7)=lcm(ord_16(7),ord_27(7))=lcm(2,9)=18 (7³≡19 mod 27). This proves irreducibility mod 7, hence over Q; a separate bounded modular computation also reproduced the three Frobenius congruences and both gcds. The affine automorphism multiplies x by ζ_9², acts freely on the 18 roots and preserves x⁹. The infinity polynomial x³+1 splits in F_7 and the origin remains rational, giving Frobenius 1^5·18. The packaged script was inspected, not run.

## originality

PASS

The supported distinct claim is the arithmetic descent and the explicit good-reduction cycle for the reduced canonical flex support of this rational model. The equation, cyclic automorphism type and geometric orbit structure are not claimed new. The closest inspected primary and indexed same-model statements give automorphisms, twists, bitangents or their incidence and level-two data, none of which supplies this flex descent. The cited geometric Weierstrass source could not be inspected in full; this is an access risk, not negative evidence or a reason to defer.

## value

PASS

For a canonical genus-three quartic with an exceptional automorphism group, the descent of known geometric flex orbits to rational closed points is a natural and independently useful arithmetic invariant. The fusion of two geometric automorphism orbits into a single degree-18 closed point determines the rational decomposition, not merely a geometric count. The good-prime 18-cycle is a concrete reproducible witness. This is distinct from the established bitangent and level-two invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
