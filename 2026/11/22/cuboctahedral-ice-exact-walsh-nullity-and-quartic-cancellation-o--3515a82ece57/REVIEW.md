# Review of the cuboctahedral-ice Walsh theorem

## Correctness — PASS
A full twenty-four-edge branching enumerator counts 600 balanced orientations and computes all 16,777,216 exact integer Walsh coefficients. An independently programmed thirteen-coordinate affine-parity solver counts 600 states without relying on the branching implementation and computes the 8,192 quotient coefficients. Its 4,639 zeros expand by factor 2,048 to the same full nullity, with minimum nonzero magnitude 4. Separate exact direct signed sums check all two- and four-edge supports, obtaining zero and 864 vanishing instances; cube-symmetry images partition the 864 into 21 orbits. Both Fourier computations agree on the exact endpoint projection norm; translation averaging proves it is minimal even without invariance. The report explains why all configurations and characters are covered, and the standalone code plus outputs document the finite certificates.

## Originality — PASS under bounded comparison
The classical cited ice literature concerns partition functions, lattice sampling/mixing, boundary conditions and graph description; it does not supply binary signed edge-incidence recovery data for this exact finite graph. The closest publicly indexed finite calculations address the octahedral graph's low-degree frame (six vertices rather than twelve) and the 3-by-3 periodic ice torus (nine vertices and eighteen edges), and are not statements of this graph's twenty-four-coordinate rank or endpoint projection norm. Direct aliases, exact numerical claims, equivalent formulations and broader coverage were searched in the available mathematical database and public literature; no covering claim was identified. The remaining risk is an unindexed equivalent calculation and relevant full articles not all inspected.

## Value — PASS
The cuboctahedral graph is a canonical 4-regular Archimedean graph, not a selected toy subcase. The 864 quartic blind characters form 21 full-symmetry orbits, separating the forced reversal-odd nullspace from genuine even-frequency failures; the precise 7,276,544-dimensional recoverable space and sharp 29471/2048 optimal endpoint projection constant quantify how much signed orientation data survives Fourier deconvolution. This is a complete natural finite benchmark, not a minor refinement of a known table or merely a computed unsigned orientation count.

## Scientific limits and comparison risks
The result concerns one finite graph; it does not cover all ice lattices. Coded exact enumeration is part of the proof, not a claim of symbolic closed form. Relevant foundational source bodies were read to the extent specified in the audit, but no global literature search proves uniqueness or priority. External mathematical review is still needed.

Self-review: passed. Independent audit: not yet performed.
