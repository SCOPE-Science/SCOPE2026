# Scientific review

**Finding:** A sharp golden-ratio shape barrier for monotone edge-averaged convection–diffusion on parallelogram meshes

## Correctness — PASS

Six signed edge weights are computed by exact reference-square integration with the physical metric. Each off-diagonal edge entry has sign opposite to its weight for any positive edge diffusion and real Péclet label; a violating pair survives assembly in the 3-by-3 Dirichlet tiling. At equality, positive-edge connectivity yields a nonsingular column-diagonally-dominant M-matrix. Maximization of the exact 2-by-2 metric eigenvalue ratio yields the sharp Jacobian barrier, realized by a stated affine cell. A standalone symbolic/numeric script passed 2,233 supplementary finite checks; the general result is supported by the analytical proof, not the checks alone.

## Originality — PASS, qualified

Adler–Hu–Lee–O'Keefe (arXiv:2611.01175, 2026), the motivating complete-graph IBEAM source, **owns the edge-weight definition and strict-positive-weight sufficient M-matrix result**. The novelty claim is limited to the exact affine-parallelogram if-and-only-if geometric domain, including zero-weight boundaries and sharp Jacobian conditioning. Cao–Chen–Lee (arXiv:2402.13347, 2024) addresses different virtual-element operators and Voronoi/Delaunay conditions. Li–Zhang (arXiv:2310.16274; 2025 publication) handles a modified-quadrature Q1 scheme and explicitly documents existing Q1 aspect-ratio obstructions. Xu–Zikatanov (1999) originates simplex edge averaging. Searches of these materials and mathematical records did not identify this combined claim. Unindexed prior Q1 geometry analysis may still cover it; the 1999 full paper was not verified read. No search establishes absolute novelty.

## Value — PASS

The result is a complete and sharp practical geometry screening condition for the smallest nonsimplicial element class in the newly introduced polytopal IBEAM method, independent of convection intensity. It identifies when skew and aspect ratio make the sufficient M-matrix framework valid or invalid and proves the sharp admissible affine-condition-number ceiling of \( (3+\sqrt5)/2\), with a realizable extremizer and an example showing that the ceiling is not sufficient. This is more informative than a finite illustrative calculation and gives a precise meshing constraint.

## Scope and outstanding risks

Only uniform affine parallelogram tilings with the six-edge complete-graph operator and Dirichlet boundary are classified. Arbitrary real edgewise Péclet labels are allowed at the matrix level; no PDE-consistency claim is made for arbitrary edge data. Failure of the M-matrix property does not prove failure of all inverse-positivity or maximum-principle notions. Full scholarly priority and independent audit remain unresolved.

Self-review: passed. Independent audit: not yet performed.
