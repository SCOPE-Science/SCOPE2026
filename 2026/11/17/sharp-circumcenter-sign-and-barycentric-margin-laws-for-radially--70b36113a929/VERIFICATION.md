---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The regular-direction Gram matrix has all off-diagonal entries -1/d; from equal squared distances to the circumcenter and the relation sum_i v_i=0 one obtains common tau=B/U and 2(c·v_i)=r_i-mu/r_i. Using S=sum lambda_i r_i and sum lambda_i=1 yields lambda_i=[d+kappa w_i-d mu w_i^2]/[2(d+1)] with mu=B/U, kappa=[(d+1)(2-d)+d mu sum w_i^2]/U. This is a downward quadratic with f(0)>0 and a single positive root, giving negative barycentric coordinates exactly for an initial block of smallest radii, including ties. Normalize r_[2]=1 and x=r_[2]/r_[1] to obtain U>=d+x, B<=d+1/x, and V-U>=-x(1-x); substituting gives lambda_[2]>=1/(2d)+[(d-1)(d+1)x^2]/[2d(d+x)^2], with equality if and only if all but the possibly largest radius agree. This forces two positive coordinates; k small radii vs d+1-k very large radii realizes exactly k negative coordinates, k=0,..,d-1. 1,200 independently solved circumcenters in dimensions 2–9 confirm both formula and lower bound; no inference of all-dimension truth from random tests.

## originality

PASS

General circumcenter barycentric formulae and the VanderZee et al determinant conditions for well-centeredness are old. The new restricted regular-ray theorem proves a sharp second-largest-radius barycentric lower bound with equality class, monotone sign threshold and every feasible negative-count realization. The generic determinant criterion does not itself state that sharp family-wide inequality, even though it could be used as starting algebra. Full 2010 dissertation inaccessible, so possible specialized earlier coverage remains a real risk rather than a FAIL.

## value

PASS

The exact sharp lower bound for the circumcenter barycentric margin at the second-longest radius is a motivated geometric invariant in orthogonal dual mesh design, not just evaluating a determinant. Its equality family, ordered sign threshold, and complete negative-facet count spectrum provide a useful all-dimension structural classification with a sharp aspect-ratio control.

The dated certificate retains the supplied scientific assessment, sources and limitations.
