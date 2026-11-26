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

Reconstructed RESULT.md §§1–5. For z0 z1 nonzero the ambient gradient forces t^3=4 and t^6=1; the zero-coordinate cases are nonsingular. A fiber critical point has w≠0; on w=1 its squared coordinates are (-1/3,-t/3,-t²/3,0). Neither endpoint is bad. Writing x2=δ t x0 gives the two coprime squarefree sextics and exactly two solutions at each root. The Hessian is nondegenerate in the three nonzero coordinates and x3 enters only cubically, giving A2. For the plane section the binary cubic has one double root and not a triple root (b²−3ac=9t^5 at every bad t); the binary leading coefficient cannot vanish there, and the x3³ term gives the cusp. The parameter derivative is nonzero at each critical point, so the local cubic discriminant has order two at each point. Independently, in the homogeneous gradient resultant, the x3² derivative gives the square of the resultant on x3=0, and the factor w in the w-derivative contributes only a nonzero constant. The other factor is the linear form L=x0+t x1+t² x2; evaluating it on the eight solutions of the three diagonal quadratics on w=1 gives, up to constant, D_+²D_-²: pairing the ±sqrt(t) choices gives (1±t³)²−t³. Squaring gives D^4, and the projective endpoints are smooth. Both sextics reduce to the irreducible Phi_9 modulo 2. A plus-field contains sqrt(−3) from a primitive cube root; a minus-field has a real embedding, so the quadratic point extension is nontrivial. This gives exactly the point orbits 6,6,12. Inspected VERIFICATION.md and verify.py, including the extent of the symbolic assertions; did not run the frozen script.

## originality

PASS

The explicit fourfold, pencil and tangency criterion are prior. The exact exceptional cusp census and arithmetic point-field partition are distinct from both the original construction and the closely matching generic discriminant calculation. No assessed distinct source establishes the full special calculation; this is a bounded best-of-knowledge decision, not a priority guarantee.

## value

PASS

The pencil is fixed by a prior geometric construction rather than manufactured for the census. Its boundary is genuinely different from the generic paired-node boundary: it has only twelve reduced parameters, all with paired cusps, and the two rational components of the parameter divisor behave differently in the singular-point cover. The exact multiplicities and fields give usable local and arithmetic data for studying this particular degeneration; no stable reduction or monodromy is inferred.

The dated certificate retains the supplied scientific assessment, sources and limitations.
