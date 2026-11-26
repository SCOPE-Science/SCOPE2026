# Independent mathematical audit

## correctness

PASS

The two connected level-zero graphs have integral cycle rank m=(2m+1)−(m+2)+1. The book retracts to its shared edge; deleting an open facet from the bipyramid sphere leaves a disk, and the n−1 leaf additions do not change contractibility. The leaf additions give the disk the same vertex and edge counts as the book. Thus the integral modules are one essential degree-zero interval and m degree-one intervals [0,1), with identical face vectors at each level. Keeping the entire edge space makes the persistent up-Laplacian BBᵀ, with nonzero spectrum given by BᵀB. The book Gram matrix is 2I+11ᵀ; the disk Gram matrix is the vertex-pinned principal submatrix of the prism graph Laplacian, as seen by orienting the sphere coherently. This includes n=3 (both rings are simple triangles). Paths from pinned to surviving vertices have length at most n, so the path energy bound gives μ≥1/[n(2n−1)]. Using sin(πi/n) on both rings vanishes at the pinned vertex; rung energies vanish and each ring's quotient is that of the Dirichlet n-edge path. Thus μ≤2(1−cos(π/n))≤π²/n². The disk's largest eigenvalue lies between 3 (test a coordinate vector) and 6 (Gershgorin), so both stated ratios have the claimed orders. Independent replay for 3≤n≤12 checked both Gram constructions and full column rank modulo a prime with floating-point eigenvalue checks. The supplied checker uses floating-point rank and omits zero leaf rows in its disk spectra; exact ranks, leaf-adjusted counts and all-n bounds follow from the proof, not that finite code.

## originality

PASS

The claim surviving comparison is an explicit quantitative extreme-eigenvalue separation for pairs matching both integral persistence and levelwise face vectors. Spectral information beyond the barcode, the definition of the operator and graph-Laplacian estimates are not new. The closest available statements do not give the paired construction or imply its gap ratios with these controls.

## value

PASS

The witness rules out recovering even the asymptotic order of this gap from the barcode augmented by levelwise face counts. Exact simplex counts and ranks make the growing disparity attributable to incidence geometry, not unequal size or homology. It gives both a quadratic lower-end contrast and a linear upper-end contrast in explicit complexes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
