# Review of weighted cactus graphical-zonotope covariance tomography

## Correctness
PASS. The edge-dependence space of a connected cactus splits into disjoint cycle relations, so the block zonotope is a linear image of an actual Cartesian product, preserving normalized uniform measures. An unequal-edge cycle is tiled by maximal-minor parallelotopes with omitted-index weights proportional to inverse lengths; conditional means and covariances reconstruct the claimed Laplacian. The graph support follows from strictly positive off-diagonal edge coefficients. Cycle weights are uniquely recovered because the displayed scalar inverse is continuous and strictly increasing from zero to infinity. Seven exact rational convex-hull moment computations on actual cycle bodies independently verify key instances; finite tests are corroboration, not proof.

## Originality
PASS, with historical-priority risk. The full graphical-zonotope deformation-cone article [1] does not address population covariance. The closest exact unit-incidence cactus calculation [2] supplies only identical edge weights; the closest independently weighted result [3] allows one distinguished cycle edge, not arbitrary lengths and arbitrary cactus blocks. The uniform Lipschitz-polar precision theorem [4] concerns the inverse covariance of a different convex body. Neither the already-known special cases nor the classical zonotope tiling alone states or logically supplies the lossless graph-and-all-weight recovery from a covariance matrix. An unindexed all-weight box-spline moment/inversion identity is possible and independent bibliographic review is needed.

## Mathematical value
PASS. Covariance tomography is a natural inverse problem in geometric probability: the complete labeled weighted graph, not merely a trace or volume, becomes identifiable from second moments of one continuous distribution. The result gives explicit formulas for any number of unequal-length cycles meeting at vertices, plus a practical one-dimensional monotone inversion on each recovered cycle. It resolves a structural information-loss question rather than a mere normalization or parameter replacement.

## Checked prior work and limitations
[1] Padrol, Pilaud and Poullot, *Deformed Graphical Zonotopes*, arXiv:2111.12422, full arXiv HTML sections 1–2 inspected.

[2] *A sharp vertex–volume covariance sandwich for cactus graphical zonotopes*, 2026-11-08, full publicly available RESULT.md inspected.

[3] *Exact covariance and quantitative isotropic profile of one-edge-weighted cycle zonotopes*, 2026-10-25, full publicly available RESULT.md inspected.

[4] *A sparse covariance precision and exact graph recovery for uniform Lipschitz potentials on cactus graphs*, 2026-10-18, full publicly available RESULT.md inspected.

The theorem assumes a connected simple cactus and strictly positive lengths; exact population covariance is necessary for the inverse. Full historical priority and finite-sample stability are not established. Kipp's arXiv:2407.01353 is relevant background on affine-isotropy optimization, not an overlapping inverse theorem; its full primary text was not successfully inspected.

Self-review: passed. Independent audit: not yet performed.
