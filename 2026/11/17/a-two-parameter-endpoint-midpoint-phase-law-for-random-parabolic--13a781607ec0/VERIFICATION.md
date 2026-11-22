---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Recomputed tangent intersection coordinates ((s+t)/2,st) and determinant A=(b-a)(c-b)(c-a)/4; A reaches 1/2 only at (-1,0,1). Deficit expansion gives u+v+y^2 at scales endpoint epsilon, midpoint sqrt epsilon. Checked the density normalization B(q/2,p), the transformed monomial exponent 2p+q/2, the gamma simplex integral and Dirichlet(p,p,q/2,1) mark with independent fair sign; integrable majorant holds for every fixed p,q>0 even with endpoint/midpoint integrable singularities. Independently used SymPy to verify K(1,1)=32sqrt(2)/45 and a nontrivial simplex value p=2,q=3. L1 convergence of rescaled unconditioned densities and positive asymptotic mass gives total-variation convergence; no finite quadrature is treated as limit proof.

## originality

PASS

Best-of-knowledge PASS for full two-exponent beta–Jacobi weighted tail/marked law, while the p=q=1 distribution and deterministic tangent area geometry are explicitly prior. Neither a uniform-sample hull distribution nor deterministic parabola triangle identity implies continuously variable exponents and weighted conditional marks.

## value

PASS

Exact rare-event exponents encode two independent natural singularities of a normalized beta–Jacobi law on a bounded parabola and identify endpoint epsilon versus midpoint sqrt(epsilon) geometry. The conditional Dirichlet TV distribution and normalized deficit mark are independently useful exact probabilistic invariants, not a bare parameter rename of the known uniform hull. Scope restricted to three tangents and fixed p,q>0.

The dated certificate retains the supplied scientific assessment, sources and limitations.
