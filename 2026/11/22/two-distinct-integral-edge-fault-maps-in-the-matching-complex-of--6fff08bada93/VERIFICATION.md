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

Triangle-parallel edges lie in triangles and square-parallel edges do not; product symmetries act transitively within each class. I independently generated matching faces as edge bitmasks, extracted deletions and links by filtering, and constructed and checked acyclic ordinary face matchings (after unpairing the empty face). In order X, triangle deletion, square deletion, triangle link, square link, the face totals including empty were 2764, 2344, 2308, 420, 456 and the augmented pair counts were 1360, 1154, 1132, 206, 226. The ordinary critical counts besides one vertex were 44, 36, 44 degree-3 cells, then 8 degree-2 cells, then 2 degree-2 and 2 degree-3 cells. Signed integral unit cancellation returned the zero 2-by-2 degree-3 boundary for the mixed link. The Morse 2-skeleton in that case is a wedge of two 2-spheres; Hurewicz identifies its attaching classes in pi_2 with their degree vectors, so both 3-cells attach trivially. The pure cases are wedges directly. The decomposition into deletion plus cone on link gives the suspension of the link as cofiber. The integral exact sequence gives the split rank-36 injection with cokernel Z^8 and, respectively, a rank-42 map of free rank-44 groups with free rank-2 kernel and cokernel, which also fixes the Smith form. No assumption that the link inclusion is null is needed.

## originality

PASS

Pass is for the distinct one-edge deletion and link profiles and their natural maps, not the already published intact wedge or the standard deletion–link cofibration. The closest fault computation is rectangular and has only injective deletion maps. No compared source states or implies the toroidal square-direction rank-42 map, or gives the two toroidal fault profiles together.

## value

PASS

The two edge directions are exhaustive natural perturbations of the same small periodic graph. The square-direction fault preserves both endpoint homotopy types yet loses two independent integral classes under the canonical inclusion, with a free cokernel of the same rank; this provides a concrete counterexample to inferring persistence from the endpoint Betti numbers. The link and cofiber data make it a usable exact comparison with rectangular faults, not just another face count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
