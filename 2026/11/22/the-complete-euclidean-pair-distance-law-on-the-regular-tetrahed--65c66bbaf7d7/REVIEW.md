# Review of the tetrahedral wireframe distance law

## Correctness
PASS. All ordered edge pairs are classified exhaustively into coincident (6), vertex-adjacent (24) and disjoint (6); their squared-distance forms are determined by the regular tetrahedral Gram matrix. The two nontrivial CDF components follow from explicitly integrated circular sectors clipped by the unit parameter square. The local expansions at both interior thresholds and the diameter are derived from cap integrals and first-order corner cones. The proof establishes all values, including transition and endpoint cases. The accompanying `check.py` additionally uses 18 independent one-dimensional quadratures and exact-moment checks.

## Originality
PASS under best-knowledge comparison, with unresolved historical-priority risk. The sources inspected cover random direction widths of tetrahedra (Finch), interior point distance laws for regular planar polygons (Bäsel), and random circumscribed-polytope volume errors (Fodor–Hug–Ziebarth); none supplies the distribution for two independently arclength-uniform points on the full tetrahedral 1-skeleton. Related prior mathematical records concern 2D surface or 3D volume sampling, intrinsic geodesic networks, or variable random polytopes rather than this fixed three-dimensional embedded wireframe. General geometric probability permits a double integral, but neither the complete three-phase formula nor its coalescing clipping-contact coefficient follows as a stated or stronger prior theorem. Searches cannot rule out preexisting work under other terminology.

## Mathematical value
PASS. The full distance law is the canonical two-point Euclidean metric invariant of a highly symmetric, nonplanar finite-length graph embedded in space. It distinguishes effects invisible to a mean alone: a density jump at the positive opposite-edge separation and an independent curvature-contact three-halves singularity where adjacent- and opposite-edge squares both clip. The exact quadratic near-diameter tail and second moment provide interpretable benchmarks for random geometric networks and skeletal sampling. This is not an arbitrary parameter slice or a numerical table.

## Limits and literature
The result does not cover intrinsic path distance, surfaces or volumes, nonsymmetric tetrahedra or nonuniform edge measures. See the references in `RESULT.md` for primary comparative literature and `AUDIT.json` for searches and remaining priority risks.

Self-review: passed. Independent audit: not yet performed.
