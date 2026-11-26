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

Under the stated commensurate Caputo-delta Volterra recurrence for c>1 and real states, the stationary equations give the origin and all inverse-sine branches with x=±sqrt((c−1)/c). With h=sqrt(c−1) and δ=atan(h)/π, precisely the symmetric pairs ±(h/sqrt(c),(−1)^m(m+δ)), m≥0, have positive determinant. It is D_m=2πh(m+δ) with trace −1, whereas the origin and all other branches have a positive real linear eigenvalue. For the scalar generating function, a unit-circle root occurs at μ=(1−z)^α/z; z=e^(iω) gives modulus (2sin(ω/2))^α and phase −απ/2−(1−α/2)ω, yielding the quoted strict sector/radius criterion. This also settles the Caputo initialization: the curve is simple away from its two endpoints at μ=0, the stable component containing (−2^α,0) has no open-disk denominator zeros, and in the other component there are open-disk zeros (as seen first for μ>0); the number cannot change away from the unit-circle curve. For the negative interval, a nonreal z in the disk cannot map to a negative real μ, and on z=−ρ the magnitude is (1+ρ)^α/ρ≥2^α. Under the strict criterion the matrix generating function, including a possible Jordan block, has integrable boundary values (near z=1 its bound is O(|1−z|^(α−1)) since the matrix is invertible), so its coefficients decay. At nonzero equality the unit-circle denominator zero is simple, since the derivative of (1−z)^α/z is nonzero there, and the numerator is nonzero. Its nonzero radial Abel pole limit rules out decay, including α=1. For D_m≤1/4 the negative real roots lie in the stable interval. For D_m>1/4 the modulus increases while the admissible radial bound decreases with D_m; the comparison changes sign exactly once, at D_α. Evaluation at D=1 yields equality for α=1 and a strictly larger allowed radius for α<1. Counting m below the strict threshold gives the ceiling with no +1 at integer equality. The monotonic equation in h gives unique strictly ordered transition values and h_m∼D_α/(2πm). The independent scalar replay gave D_(1/2)=1.447622986854899 and ceiling arguments 0.0536103 at half order and −0.0315394 at order one for c=1.7, confirming 2 versus 0 equilibria. No nonlinear attraction or bifurcation claim follows.

## originality

PASS

The supported distinct contribution is the all-real, all-branch strict stability census, with a sharp order-dependent determinant cutoff and distinct inverse-square transition sequence. Neither the map nor the general fractional spectral criterion is credited as new.

## value

PASS

Completing the real branch census changes the qualitative picture: near c=1 many distinct linearly stable pairs can coexist, and the thresholds accumulate at a quantifiable inverse-square rate. The exact formula and distinct order-dependent interval also explain when a fractional-order pair remains stable beyond the classical threshold. This is more than applying a stability inequality to a chosen principal branch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
