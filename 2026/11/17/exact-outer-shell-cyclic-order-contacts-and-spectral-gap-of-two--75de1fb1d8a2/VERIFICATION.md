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

The actual simplicial triangle-edge boundary B and tetrahedron-triangle boundary D satisfy B^T B+DD^T=nI by edge/tetrahedron incidence cancellation. Thus every zonotope endpoint p_sigma=B sigma/2 has 4||p||^2=n C(n,3)-||D^T sigma||^2. Vanishing tetrahedron coboundary enforces transitive tournament labels on n-1 nonzero vertices, precisely (n-1)! oriented circular-order signings; the vector u=B sigma/n strictly exposes each and gives uniqueness. Central symmetry gives the unique origin circumcenter and antipodal diametral pairs. For any nonzero tetrahedron defect t, parity forces |t_T|>=2 and 5-vertex boundary-of-boundary incidence forces at least n-3 distinct nonzero entries, hence squared gap >=n-3. Flipping one triangle in an outer signing produces exactly n-3 defect entries of size 2, and u'=u-(sigma_j/2)Be_j strictly exposes the new signing; so sharp second shell is real vertex. An independent Gray-code exhaustive enumeration of all 1,049,618 signings across n=3..6 reproduced (n,R^2,contacts,next)=(3,3/4,2,none),(4,4,6,3),(5,25/2,24,21/2),(6,30,120,27). These finite tests are corroboration; the chain/cocycle proof covers all n. RESULT.md blob a718af84ea74b803ceb13c5b0a52f5956c7bc4b7 and acyclohedron_verify.py blob 8b6c05ed46ac31121834f242afe284cd820daa12 inspected.

## originality

PASS

The full fixed-d=2 Euclidean outer-contact enumeration and sharp next squared-radius shell for all n, especially n>=6, is not implied by known combinatorial acyclohedron face counts or the near-top n-3 result, except the explicitly conceded n=5 overlap.

## value

PASS

This is a natural metric invariant of the canonical two-dimensional acyclohedron with a specified orthonormal simplicial metric: exact minimal enclosing ball, factorial contact orientations, antipodal diameter pairs and a sharp nonzero gap to the next vertex shell. The cocycle-defect structure explains a full infinite family and supplies exact extremal geometry, not a numerology exercise or arbitrary low-dimensional slice. The n>=6 and gap portions survive previously solved n=5 special cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
