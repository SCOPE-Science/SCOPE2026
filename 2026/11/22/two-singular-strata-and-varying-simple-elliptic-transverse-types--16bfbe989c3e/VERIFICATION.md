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

The claimed singular locus was derived by differentiating the full Weierstrass-Cox hypersurface and splitting the cases \(z=0\) and \(z\ne0\). Reduced discriminant guarantees the total Weierstrass threefold is nonsingular at all nonzero base vectors. Weights \((1,2,3)\), degree \(6\), yield a genus-one exceptional curve of self-intersection \(-1\) and isolated transverse Milnor number \(10\). Weights \((1,1,2\chi,3\chi)\), degree \(6\chi\), yield the isolated threefold transverse Milnor number \(2(6\chi-1)^2\). These are deductions from a proof, not assertions of exhaustive computer enumeration.

Execute `python checker.py` with SymPy to repeat the exact example checks. They verify a squarefree degree-36 discriminant, different elliptic \(j\)-values at two sample base points, and the stated weight-product calculations. The sample is an algebraic sanity test and does not certify Picard rank or prove the arbitrary-\(\chi\) result.

Only the reduced singular support and the two stated open transverse strata are determined. The Jacobian-scheme thickening, singular fibers in the plane stratum, and the intersection origin are not classified. No independent audit has been performed.
