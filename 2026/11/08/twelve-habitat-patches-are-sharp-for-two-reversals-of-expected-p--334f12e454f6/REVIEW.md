# Scientific review: twelve-site expected pair-connectivity onset

## Correctness

PASS. On a tree, a connected retained pair requires survival of each vertex of its unique path, giving \(\mathbb E[Z_T(p)]=\sum_j a_j(T)p^{j+1}\). The center-rooted canonical encoding, exhaustive leaf-extension argument, and integer Möbius coefficients cover every equal-order tree comparison through eleven vertices. Of the 215 distance profiles at eleven sites, exactly one pair has two transformed sign variations; its difference is proportional to \(p^3(p-1)(3p^3+p^2-3p+1)\), and the cubic discriminant is \(-76\), with its only real zero negative. For twelve sites, the explicit edge lists yield exact profiles and \(p^3(p-1)(2p-1)(p^3+p^2-1)\), with exactly two simple interior roots. Standalone standard-library checks pass. The general result is only the *least* order allowing two reversals, not an all-larger-orders existence claim.

## Originality

PASS on the inspected evidence, with historical priority provisional. The distance polynomial and ecological network connectivity are old, and are expressly not claimed as new. Keitt et al. (1997) treat landscape percolation scales; Saura et al. (2013 online) analyze dispersal and stepping-stone connectivity; Mowshowitz and Dehmer (2015) analyze the local Hosoya polynomial and entropy. Brown, Oellermann and Mol (2018) already identify the *edge-survival* pair-resilience function on a tree exactly with the Wiener polynomial, and investigate roots of each single polynomial. The vertex-survival score here is therefore transparently equivalent to that old edge-resilience polynomial up to a positive factor. Their inspected relevant sections do not present the minimum twelve-vertex onset for two sign reversals of the difference of Wiener/Hosoya polynomials. Nearby indexed results about different graph spectra, two-terminal edge reliability and phylogenetic diversity do not imply this exact site-percolation pair-connectivity cutoff. Residual risk: older graph-polynomial ordering literature not fully indexed may contain an equivalent theorem.

## Value

PASS. The expected number of mutually reachable surviving patch pairs is an immediately interpretable functional-connectivity score on a simple landscape network. The theorem fixes the smallest network complexity at which connectivity-based ranking can switch twice as homogeneous patch viability improves: comparing a landscape at one survival probability need not predict its relative standing at intermediate or high viability. The exact finite onset makes the limitation identifiable without fitted parameters. Applications to actual landscapes need separate model validation.

## Closest literature and scope

Keitt, Urban and Milne (1997); Saura, Bodin and Fortin (2013 online/2014 print); Mowshowitz and Dehmer (2015); Brown, Oellermann and Mol (2018). The result concerns only tree graphs, independent identically distributed patch survival, equal site weights and expected connected unordered pairs; it does not characterize arbitrary larger trees, general graphs or ecological persistence.

Self-review: passed. Independent audit: not yet performed.
