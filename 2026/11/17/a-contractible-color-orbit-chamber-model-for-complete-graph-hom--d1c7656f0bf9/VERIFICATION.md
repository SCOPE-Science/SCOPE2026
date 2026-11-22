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

Every point of Hom(K_m,K_n) is uniquely an m-by-n stochastic row array with disjoint positive column supports. Sorting each row preserves all support cardinalities and is continuous. Equality of separately sorted row multisets allows the rowwise column bijections to assemble into a single target permutation, exactly classifying orbits. The sorted length-k row simplex has barycentric coordinates lambda_j=j(a_j-a_{j+1})>=0 summing to 1, with vertices v_j=(1/j,...,1/j,0,..). Positive support total <=n gives exactly the stated chamber union; the compact Hausdorff quotient therefore is homeomorphic. The nested simplices D_k intersect in common faces; positive compositions of n into m parts index maximal chambers of dimension n-m. Straight-line interpolation of each row toward v_1 stays in its original D_k and fixes the common vertex, proving strong contractibility for all integers in range. Independent m=3,n=5 check found 10 vertices and 6 maximal chambers.

## originality

PASS

Babson–Kozlov prove the unreduced complex is a wedge of spheres, and published target-color character studies prove only rational acyclicity of its quotient. An explicit sorted row-orbit homeomorphism and integral strong deformation retraction are strictly stronger. The 1997 deleted-join model and Pfeifle canonical projections have related ordered-block geometry, and could have an equivalent under alternate naming, but no read theorem asserts this target-color quotient contraction.

## value

PASS

The full-color quotient topology was only rationally resolved in the closest comparison; an integral strong deformation retraction, explicit orbit space and chamber/vertex structure settle a natural exact topological question for all m,n. The m-armed star boundary illustrates why an acyclic-orbit argument or ball guess is inadequate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
