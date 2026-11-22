# Scientific self-review

## Correctness — PASS
The area reduction follows from the projected zonotope formula. The six spherical absolute moments are derived from an explicit Dirichlet integral; multiplying out the raw moments and centralizing cancels the cubic symmetric-sum term. The identity \((x+y+z)(xy+yz+zx)-9xyz=xyz\sum_{i<j}(x_i-x_j)^2/(x_ix_j)\) is exact and yields the stated aspect-ratio law. Both coefficient signs follow from the classical \(\pi<22/7<16/5\); cube equality is immediate. The standalone checker independently tested moment expansions, randomized projected polygon hull areas, and numerical integration diagnostics. No finite sample is used as a proof.

## Originality — PASS (historical-priority risk retained)
Full texts read: Vickers–Brown (2001) cuboid density and silhouette geometry; Finch (2012) cube first/second moments; Yan–Wang (2015) mixed brightness theory; published 2026 orthotope first/second moments and perimeter third moments. Searches of published mathematical findings for random box-shadow third-cumulant signs, skewness, and volume-normalized shape energy found no theorem giving the stated strict sign and exact sharp deficit. The older full distribution for cuboids, attributed to Walters (1947), already determines every moment in principle, and a separately published inverse-tomography result may contain the third *raw* moment. Neither novelty of the cuboid PDF nor new recovery of sides from three raw moments is claimed. An unindexed computation of the sharp central-moment inequality is still possible; the 1947 paper's primary full text could not be inspected.

## Value — PASS
This is a sharp inequality for a natural, experimentally observable integral-geometric statistic; it distinguishes every rectangle-sided noncube from cubes at equal volume and gives an **exact** scale-free anisotropy energy, not a loose bound. The sign is subtle because at the cube the normalized third moment is only about \(-0.00211312\), and its strictness rests on the narrow \(22/7-\pi\) gap. The nonstandard three-way absolute-direction correlation is essential. The scope is limited to positive rectangular boxes and isotropic viewing; statistical sampling stability and general-body extensions are not claimed.

Self-review: passed. Independent audit: not yet performed.
