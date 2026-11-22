---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-21.md",
      "INDEPENDENT_AUDIT_2026-11-21.json"
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

After similarity normalize f1=x^2+y^2-r1^2, f2=x^2+y^2-r2^2, f3=(x-1)^2+y^2-r3^2, r1>r2>0, and set F=f1f2f3. Independently expanded all three cofactor identities for the proposed V4+eta J grad F at arbitrary symbolic lambda, eta, alpha, beta, gamma, radii. Setting lambda=1, eta=-1, alpha=0, gamma=-(r1^2+r2^2)/2, 0<|beta|<3(r1^2-r2^2)/(2r1) gives the signed speed on each concentric circle and W3=-3f1f2, none zero on the strictly disjoint circles. Pairing sine-reflected phase points gives the same nonzero sign sgn(beta) for all three positive-time cofactor integrals. Independently checked three very different proper disjoint/nested configurations and both signs beta, as diagnostics only. Degree five is exact because eta J grad(f1f2f3) has a noncancelling quintic homogeneous term. Cao–Llibre Theorem B is an exhaustive <=4 normal form; its sign formulas and the ordering r1>r2 forbid three equal exponents, while three feasible sign-pair choices and both beta signs yield all six nonuniform assignments. Those arguments cover arbitrary permitted configurations rather than just the checked sample.

## originality

PASS

PASS in the compared primary literature. Cao–Llibre arXiv:2611.05696 Theorem B and Section 4 already give all quartic systems and the negative lower-bound implication for uniform sign patterns, and are explicitly credited. They do not exhibit the degree-five Hamiltonian perturbation which creates both uniform patterns for every strict geometry. General Christopher and Margalef-Bentabol–Peralta-Salas constructions lack a degree-five all-geometries guarantee; older algebraic-cycle realization literature remains a bounded historical risk.

## value

PASS

PASS: this is the sharp last step in a natural eight-pattern classification of simultaneous stability for an arbitrary prescribed 3-circle geometry with exactly one concentric pair. The novel quintic crossing from mixed-only to uniform stability solves a degree-minimal realization problem, not an incidental polynomial manipulation. Additional cycles and Floquet magnitudes are deliberately outside scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
