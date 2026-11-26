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

An eigenvector with purely imaginary eigenvalue must vanish at the endpoints by the dissipative quadratic form, then vanish everywhere by the nearest-neighbor recurrence with J≠0. Thus e^(−Kt) decays, the integrated Gramian is positive definite, and its Lyapunov solution is unique. The same-parity part G of the Dirichlet inverse commutes with A, since the parity sign conjugates A to −A. The inner-path analogue B commutes on interior rows/columns and is zero on endpoints; hence [A,B] is supported on the boundary, with first-row entries B(2,j) and last-row entries B(N−1,j), matching the skew C anticommutator PC+CP (both vanish between opposite endpoints). For same-parity i<j the four affine neighbor terms in [C,A] cancel before truncation, with missing neighbors at i=1 and j=N contributing N+1−j and i respectively, exactly the corresponding copies of G. Opposite-parity entries there are zero. The commutator diagonal is twice the sum of adjacent C entries, giving −4 in the interior and 2(N−2) at either end. These identities, including N=2 where P=I and Q=I/κ, yield K†Q+QK=I with the stated sign of the imaginary term. The survival expectation is Tr(Qρ); the localized diagonal has the form a/κ+bκ, with a,b>0 in the interior and b=0 at an endpoint. Differentiation and strict convexity give the unique interior optimizer and stated minimum; both limiting optimal rates follow directly. An independent diagonal-phase transformation to a real rational Lyapunov equation followed by exact linear solves checked every complex entry for seven paths N=2 through 8 at varied rational couplings and rates.

## originality

PASS

Full survival Gramians and site-dependent localized-source optimization already appear for a single terminal sink, and two-loss scattering is also prior. The distinct contribution supported here is the explicit finite equal-two-end Gramian and the resulting finite-size dependence on distance to both boundaries, not the Lyapunov method or the idea of optimizing a loss rate. The conclusion is bounded by inspected statements.

## value

PASS

The finite coherent path with two terminal absorbers is a natural transport model, and absorption time cannot be recovered from eventual efficiency (which is one). An all-entry formula handles initial relative phases without a matrix solve. The finite-size site dependence of the optimum distinguishes fixed distance from one end from a bulk-scaled start; the exact endpoint case also shows why imposing a universal finite optimal rate would be wrong. This goes beyond solving the routine Lyapunov equation for isolated lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
