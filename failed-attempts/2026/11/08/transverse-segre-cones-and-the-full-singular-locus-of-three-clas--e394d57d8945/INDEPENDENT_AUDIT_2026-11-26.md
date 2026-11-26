# Independent mathematical audit

## correctness

PASS

The scheme-theoretic nonbasis presentation and a nonzero A–B pivot put its two columns at (1,0) and (0,1). The equations with these pivot columns kill the complementary components of every remaining A and B column; the only surviving equations are the 2×2 minors of the C block. Their ideal is the prime Segre ideal, giving the full chart A^(a+b-2) × D_(2,c). For c=1 the latter cone is affine 2-space. For c≥2 an invertible entry solves c−1 equations, making every rank-one point smooth, and at zero the tangent dimension 2c exceeds c+1. The pivot minors show that the complementary cross support vanishes exactly when the C block vanishes. All points are covered by cross-pair charts, and different pair-support strata cannot meet. The rank-one cross coordinates identify each support stratum with its indicated Segre product. Completing at zero in the C variables and translating the smooth coordinates gives exactly the claimed completed ring. The projective Segre degree, or the Hilbert numerator 1+(c−1)t at 1 from the degree-d dimension (d+1) times binom(d+c−1,c−1), gives multiplicity c; the chart dimension gives codimension c+1. The two-class case is the Segre product by the same coordinate construction without C. I inspected check_charts.py without executing it: it tests the normalized minors, representative Jacobians and truncated Hilbert identities, not global coverage. The scheme argument establishes coverage independently.

## originality

FAIL

The earlier complete-multipartite edge-toric result, Resultary 99655ba7daaa, gives the same strata, transverse charts, multiplicities and codimensions. A cyclic-interval rank-two three-class positroid variety is the same embedded projective edge-toric variety after matching its cross-pair coordinates; the frozen finding is its three-part specialization. This is actual prior coverage, not mere evidence of a similar result or a conclusion from publication-search failure.

## value

FAIL

The local invariants are useful, but the exact fact for this family is already available in the same coordinates from the stronger multipartite theorem. The frozen Grassmann-chart proof gives an alternate presentation, not an additional invariant, extension or consequence that survives this overlap. No supported new claim warrants a repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
