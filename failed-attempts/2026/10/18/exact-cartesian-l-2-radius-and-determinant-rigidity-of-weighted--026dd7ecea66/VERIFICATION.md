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

The factor 1/2 in H_theta gives tr(H_theta^2)=S/2 and det(H_theta)=Re(e^(3i theta)abc)/4, by the two oriented three-cycles in the determinant. Thus the characteristic cubic is lambda^3−S lambda/4−Re(e^(3i theta)abc)/4. Reflecting all roots changes the sign of the product term but not the norm. For positive product the trace-zero real roots consist of one positive and two negative roots, and the positive one has largest modulus by the zero sum; at zero product the roots are 0 and ±sqrt(S)/2. The largest-root branch becomes sqrt(S/3) cos(arccos(eta |cos(3 theta+arg abc)|)/3). Averaging folds the absolute cosine to [0,pi/2] with density 2/pi; the phase and triple frequency do not affect that distribution. The integrand increases strictly in eta except at the measure-zero endpoint pi/2. The endpoint integrals are S/4 and S(1/6+sqrt(3)/(4 pi)). AM–GM gives their stated equality cases; continuity along a normalized path from (sqrt(S),0,0) to equal positive magnitudes realizes the entire interval. S=0 is separate and eta is not defined there. This analytical check covers all allowed phases and degeneracies. CHECK.py was inspected, not run.

## originality

FAIL

The exact angular formula and its scalar consequences are a mechanical specialization of the previously published weighted-shift Kippenhahn polynomial combined with the pre-existing Cartesian L2 definition. The decisive prior theorem describes the characteristic polynomial of every angular Hermitian part, not merely eigenvalues of W or a bound on the classical numerical radius. No earlier printed identical L2 formula or chronology between nearby catalogue items is asserted.

## value

FAIL

The sharp range and determinant interpretation are useful ways to present this L2 invariant, but no distinct mathematical obstacle remains after the old general pencil is substituted into the defining average. The further scalar monotonicity and endpoint computations are routine and do not provide an independently valuable unknown exact fact at the stated scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
