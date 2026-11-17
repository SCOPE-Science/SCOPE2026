---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The signed-filter and antichain definitions give the two cube-hull bodies exactly. For enriched order, sections at upper minimum y give an m-cube of radius T=(1+min y)/2 and T~Beta(m+1,n) after weighting by the section volume. Conditional upper coordinate minima and uniforms give the rank-one added covariance bJ_n; lower block has a_m I_m and cross covariance zero by signed symmetry. For enriched chain, cubical free-sum shell radii (R,S,1−R−S) are Dirichlet(m,n,1), giving matching diagonal a_m I_m,a_n I_n. The determinant lemma gives ratio 1+nb/a_n. Independent exact rational spot checks m,n=(1,1),(1,2),(2,1),(2,3),(7,5) matched ratios 4/3,11/8,3/2,8/5,28/13; sharp sup follows from m=t²,n=t. Source triangulation script was inspected, not treated as a universal proof.

## originality

PASS

Primary enriched-order/Ehrhart papers give the geometry and equal volume, not this uniform-volume covariance or sharp affine invariant comparison. A published 2026-10-25 study uses the exact same two hulls but examines widths, Gaussian windows, in/circumradius—not covariance. Another signed-order covariance study concerns a different halfspace body with volume 2m!n!/d!, not the enriched cube-hull pair of volume 2^d m!n!/d!. General Hanner isotropic recursion supplies the chain-half covariance only. No verified dominating formula for the order-half rank-one difference was found.

## value

PASS

An exact affine-invariant isotropic-constant difference between canonical enriched order and chain realizations with equal Ehrhart polynomial distinguishes lattice-equivalent volume combinatorics from second moments. The strict universal sharp bound and layer reversal are motivated geometric invariants for a natural complete two-level poset.

The dated certificate retains the supplied scientific assessment, sources and limitations.
