# Scientific review

## Correctness — PASS

The proof explicitly constructs the 15-by-15 edge–matching incidence matrix, derives its singular-space decomposition from \(TT^{\mathsf T}=4I+J\), obtains the 30-vertex Laplacian spectrum \((0^1,1^9,3^{10},5^9,6^1)\), and applies the PBH criterion to each eigenspace. The lower bound ten and forced five-plus-five split are analytic. The eligible five-edge sets are counted analytically by the unsigned \(K_6\) incidence kernel, and the matching-side and mixed constraints receive a full finite certificate. The standalone verifier uses bounded-determinant exact modular tests; all 720 label automorphisms, eight candidate orbits, and 1518 matching choices per representative are explicitly covered. It confirms 1518 admissible sets of each type, 36 exceptional pairs, 2,304,288 successes, and full-rank positive and negative example comparisons. No floating-point spectrum, randomized search, or incomplete sample substitutes for the proof.

## Originality — PASS, subject to publication-priority risk

Burgarth et al. (arXiv:1111.1475, complete rendered article) establish zero forcing as a sufficient condition; Monshizadeh et al. (arXiv:1403.4868, complete rendered article) primarily classify graph-qualitative strong structural controllability. Neither gives a census of ten-coordinate placements for this fixed unweighted graph. Yuan et al. (2013, open full text) establish general maximum-multiplicity exact controllability, so the spectral lower bound itself is not claimed as independently novel. Zhang, Camlibel and Cao (CDC-ECC 2011, complete six-page full text inspected) provide distance-regular necessary/sufficient conditions, giving only eight-or-more leaders by their diameter bound and a 26-leader generic construction here, not the ten-leader census. Prior incidence classifications on affine/projective planes are on other graphs and do not imply the exact 36 ovoid–spread exceptions. Actual semantic searches of relevant records found no equal or stronger claim; this is evidence of noncoverage among inspected sources, not a proof of global novelty.

## Value — PASS

The Tutte–Coxeter graph is the smallest thick generalized-quadrangle incidence graph and a canonical distance-regular cubic network. The exact count of all optimal coordinate placements is useful for enumerating actuator designs and clarifies a sharp obstruction invisible to checking just the largest repeated eigenspace: 36 star–spread pairs pass the two separate incidence tests but fail on the nine-dimensional eigenmodes. The result is a natural complete classification, not an arbitrarily chosen numerical slice. Its boundaries are fixed graph structure, independent coordinate inputs, and no energy criterion.

## Closest literature and limitations

Reviewed primary sources: Burgarth et al. 2011 (arXiv:1111.1475), Zhang–Camlibel–Cao 2011 (DOI:10.1109/CDC.2011.6160658), Yuan et al. 2013 (DOI:10.1038/ncomms3447), Monshizadeh–Zhang–Camlibel 2014 (arXiv:1403.4868). The exact finite computation has a separately inspectable Python 3 certificate but is not a symbolic all-order generalized-quadrangle theorem. Specialist indexing gaps or other previously unnoticed priority claims remain possible. Independent mathematical verification remains to be carried out.

Self-review: passed. Independent audit: not yet performed.
