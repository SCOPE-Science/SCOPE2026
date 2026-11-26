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

Compared the triples with Bokowski–Pokora v4 pp. 7–8, independently transcribed them, and reconstructed the three graphs without executing the frozen script. Each ordinary triple blowup separates the strict transforms and gives three distinct transverse nodes on a rational exceptional curve; each unlisted pair leaves one ordinary double point. Thus every pair of line vertices is connected by an edge or a two-edge path, and all exceptional vertices are connected to lines. Degrees are 3 on exceptional curves and 11-r on each line with r incident triples (six on nine lines and seven on three lines); this verifies stability. All components are rational, so the genus is 66-31+1=36. The reduced Laplacian has size 30; independent exact Smith computation gave the ten nonunit factors [2,2,6,6,6,6,6,6,672,37753632] for C2 and [2,6,6,6,42,42,42,210,840,840] for both C6 and C7, with determinants 4734733125943296 and 4742523426816000 respectively. The exact full characteristic polynomial for C6 and C7 is t(t-7)^6(t-3)^7(t-2)^8(t^3-19t^2+107t-155)(t^3-17t^2+85t-120)^2 and the three graphs were distinguished by adjacency-preserving search. The geometry also identifies the line vertices by degree and recovers the triples from the graph, so graph isomorphism would imply isomorphism of the original incidence structures. Replay: /workspace/branches/b449bc6a-4093-4a54-be6d-9dc93493677e/reproduce.py and reproduction.txt. The Schur scalar 3^8 for the independent reduced determinant in the frozen proof follows from eliminating 3I_19 against 11 line coordinates. For the conditional Néron claim, the component-group lattice presentation for a proper regular split semistable model uses the special-fiber intersection matrix on the degree-zero lattice: off-diagonal entries count transverse nodes and the row sums vanish because the whole fiber is reduced and has intersection zero with each component. This is minus the graph Laplacian, hence the same finite cokernel on degree zero. Neither the computation nor the claim asserts existence of a smoothing or handles other thicknesses.

## originality

PASS

The arrangements, their shared incidence profiles and their nonisomorphism are established prior geometry; the distinct contribution supported by the inspection is the comparison of exact integral critical groups for the resolved boundary graphs, together with the precise C6/C7 Laplacian coincidence. No identified source apart from the frozen record stated that comparison. Known graph-component correspondence supplies the interpretation, not the arithmetic of these three matrices. This is a best-of-knowledge finding, not proof of priority; in particular an unproductive literature lookup is not negative evidence.

## value

PASS

These three natural arrangements form a pre-existing controlled incidence comparison, not an arbitrary graph sample. The boundary construction preserves the full incidence data, and the exact invariants show both its greater sensitivity than coarse per-line profiles and its failure to distinguish the nonisomorphic C6/C7 pair even when used with the Laplacian spectrum. In particular the shared full group is stronger than the shared number of spanning trees. The exact torsion factors are directly usable as geometric component-group data in the specified regular smoothings, without claiming anything about the ambient surfaces or more general degenerations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
