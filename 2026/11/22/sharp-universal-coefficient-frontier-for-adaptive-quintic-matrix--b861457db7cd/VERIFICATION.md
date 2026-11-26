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

On each mode r=1−x² the update is F_a(r)=1−(1−r)(1+r/2+ar²)². Differentiation gives its sole positive interior minimum for a>3/8 at r_*=(8a−3)/(10a). At that point (1−r_*)(1+r_*/2+ar_*²)²=(16a−1)²(2a+3)³/(25000a³). Independent polynomial multiplication checked that subtracting 12500a²(2a+1) from the numerator gives (4a+1)²P(a); P(3/8)=−1125/4, P(29/20)<0<P(3/2), and convexity plus positive derivative at 29/20 isolate the relevant root. For 0<r<1 the factorization of F_a−r gives strict descent, and the positive Bernstein expression at a=3/2, together with monotonicity in a, gives F_a>−r below the cap. On the negative side r=−t, 0<t≤1/(2a_*), the multiplier is strictly between 0 and 1 for a≤U<a_*, giving F_a(−t)>−t; its upper bound F_0(−t)=t²(3−t)/4<t gives strict contraction there too. The image of the positive side stays above −1/(2a_*) by the minimum calculation, so a compact invariant interval provides a uniform contraction factor for each fixed input and cap. Writing X_k=J B_k with J=A(A²)^(−1/2) and positive B_k commuting with J handles even the nonnormal square case; in the rectangular case use the initial polar isometry in place of J. This preserves branches and makes the spectral residual norm the maximum of the modal magnitudes. At equality r_* maps to the negative fixed point −1/(2a_*); above equality the same initial-minimum construction crosses the fixed-point barrier, after which the magnitude strictly increases and cannot have a finite limit. Direct rational replay gives F_{3/2}(3/5)=1−(2/5)(46/25)²=−1107/3125<−1/3.

## originality

PASS

The quintic polynomial itself is prior art. The supported distinction is its sharp cap simultaneously for every admissible coefficient schedule, together with the exact boundary trap and divergence witnesses. No inspected source establishes or implies this package.

## value

PASS

The cap supplies a usable exact-arithmetic safeguard even when the coefficient is selected adaptively by an arbitrary procedure. Its value is the precise change from guaranteed contraction to a nonunit trap and then possible divergence, not the approximately 1.5 percent increase over an empirical recommendation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
