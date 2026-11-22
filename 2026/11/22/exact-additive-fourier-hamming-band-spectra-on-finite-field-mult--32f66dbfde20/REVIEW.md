# Scientific assessment: additive-Fourier Hamming sampling on multiplicative varieties

## Correctness — PASS

The result specifies all parameter ranges, the unnormalized row-domain spectral convention, and the complete character-indexing multiplicities. The key calculation is an exact polynomial-valued additive-character Gram kernel \(\prod_i(1+z(q\mathbf1_{x_i=y_i}-1))\). Multiplicative diagonalization on the product-one subgroup then yields the stated occupancy polynomial with no analytic limit or unproved character-sum estimate. Its nonnegative coefficients establish the shell/band rank equivalence and full-row-rank threshold. The final-band endpoint formula follows by removing the top frequency shell from the complete Fourier Gram and minimizing a strictly convex occupancy sum. Both equality eigenspace dimensions are counted by free diagonal-character orbits.

The standalone direct-matrix checker passed 148 shell/band comparisons over five field orders, including the quadratic extension field, plus six nontrivial product-coset checks. This finite evidence is supplementary and does not replace the general proof. No formal or independent validation is claimed.

## Originality — PASS relative to inspected evidence

The most relevant source, Fraser–Rakhmonov (arXiv:2505.09293, Section 5.2), studies exactly the variety \(H_j\) and proves Fourier decay and restriction estimates, but not the complete spectrum of sparse additive-frequency sampling or its last-band conditioning. Published character-band sampling on a single checksum subgroup already gives occupancy rank thresholds; those are **acknowledged as covered** and are not offered as independently novel. That work has unweighted character-orbit Gram blocks, whereas the present additive-frequency matrix has the distinct weighted eigenpolynomial \(F_{[e]}\). The published all-degree Hamming-sphere result samples an additive Hamming **observation shell**, not a multiplicative product-one variety. The coordinate-hyperplane and reciprocal-hyperbola sampling results use other frequency or observation families. Direct statement/implication comparisons with the full texts found none stating or directly implying the complete new additive spectrum and exact sharp last-band eigenvalue extremes without additional calculation.

**Residual risk:** a general weighted code-character, Hecke algebra, or harmonic-analysis formula could encode these values under different terminology. The literature search was bounded; absence of a match is not proof of first discovery.

## Value — PASS

The full frequency-degree family, rather than a single chosen instance, is classified by one finite positive polynomial per character occupancy. This gives exact multiplicities, all sampling ranks, the precise degree threshold for full reconstruction, and exact sharp frame bounds. In particular the final proper band has a simple worst mode and a completely classified balanced family of best modes, permitting exact condition-number design comparisons for finite-field Hamming varieties. These are mathematically natural Fourier-sampling invariants motivated by a recent primary study of the same variety; the result is neither a numerical table recomputation nor an arbitrary finite slice. Its intended application is linear sampling stability, not an asserted improvement of general \(L^p\) extension inequalities.

## Closest literature and limitations

See the exact primary references, full-text material inspected, named comparison checks, and unresolved priority risk in `AUDIT.json`. The scientific claim is confined to full product-one varieties, exact additive-frequency shells and bands, and the unnormalized row Gram spectrum. Boundary cases \(q=2\), \(k=0\), and \(k=d\) are included; deleted observation points and irregular frequency masks are not.

Self-review: passed. Independent audit: not yet performed.
