---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The projective discriminant is the zero divisor of the universal resultant of the five partial derivatives of a cubic in five variables. Its covariance exponent under a coordinate transformation is \(3\cdot2^4=48\). Applying this to \(u\mapsto\sqrt a\,u\) certifies that the specialized discriminant is homogeneous of degree \(24\) in \(\ell\). The support is exactly the irreducible degree-\(12\) dual of the smooth cubic surface by the elementary gradient equations. Thus the polynomial multiplicity is forced to be two; this is a complete argument and not a sampled inference.

At each smooth point of the dual, a unique ordinary tangent-plane node produces exactly two projective singular points of the cubic suspension. Their full Hessians are nondegenerate, since the restricted quadratic tangent form is nondegenerate and the off-diagonal normal-coordinate Hessian entry is nonzero. A transverse Veronese conic has \(12\cdot2=24\) distinct bad parameters; each has two \(A_1\) singularities. The incidence variety is a blow-up along the smooth cubic surface.

`checker.py`, executed with Python 3 and SymPy, reports a rank-three example where the Fermat cubic dual restricts to a squarefree homogeneous binary polynomial of degree \(24\). This exact finite calculation witnesses the nonempty transversality open locus and checks a key concrete instance; it is not a substitute for the general proof. Exceptional parameters, non-generic maps, and actual compactified Prym fibers remain outside the proven census. No independent validation has been carried out.
