# Review of the random ellipsoid-shadow caustic inversion

## Correctness (C): PASS
The object is a three-dimensional strictly triaxial ellipsoid under Haar-uniform orthographic planar projection. Squared visible semiaxes are the compression eigenvalues of a diagonal positive form. Their exact joint density follows by an invertible secular map from a Dirichlet(1/2,1/2,1/2) squared-normal vector with explicit Jacobian. Two antipodal saddle pairs, and no other interior critical points, produce the claimed logarithmic coefficients. Their algebraic comparison gives the strictly separated inverse candidates; explicit beta integrals give both endpoint constants. The argument handles the critical equality of the two saddle levels by summing coefficients. The supplied standalone script passed 990 deterministic diagnostic assertions including independent matrix diagonalisations and numerical integrals. Numerical evidence is not treated as a proof.

## Originality (O): PASS with historical priority risk
Binney and de Vaucouleurs (1981, section 2.2, Appendix and figure 1) already derived the triaxial apparent-shape forward law and the two preferred projected axis ratios. These positions, and reexpression of the forward law as a compression integral, are explicitly excluded from the originality claim. Binney (1985, section 2) gives projected-shape geometry. The inspected population-inversion literature (Cappellari et al., 2014, section 3.1) addresses heterogeneous galaxies rather than one fixed ellipsoid reconstructed from exactly three singularity statistics. No inspected comparison states both sharp logarithmic coefficients, their coalescent sum, and the uniquely discriminating coefficient ratio. Closest located related findings address a different paired shadow/section statistic, central sections, or nearly oblate scaling, and do not imply the stated one-distribution fixed-shape inverse formula. Risk remains that a classical ellipsoidal-apparent-axis-ratio analysis (including uninspected earlier work) derived equivalent amplitude identities under a reciprocal/minor-major parameterization. A known forward law does make the new formulas derivable, but does not itself explicitly state the quantitative three-statistic inverse theorem.

## Value (V): PASS
The observed singularity positions alone leave a genuine twofold ambiguity between different middle-axis ratios; one naturally measurable density coefficient resolves it by the sharp, universal separation factor \(p\sqrt q>1\). The coefficients also quantify two distinct caustic mechanisms and their collision. This is a natural, exact inverse geometric-statistics result, not an arbitrary slice of a large table. The results may benchmark inference for controlled, monodisperse populations but do not justify an unqualified noisy observational inversion.

## Closest sources and limitations
1. J. Binney and G. de Vaucouleurs, *The apparent and true ellipticities of galaxies of different Hubble types in the Second Reference Catalogue* (1981), DOI https://doi.org/10.1093/mnras/194.3.679: establishes forward apparent-axis-ratio modeling and recognizes two preferential levels.
2. J. Binney, *Testing for triaxiality with kinematic data* (1985), DOI https://doi.org/10.1093/mnras/212.4.767: projected-ellipse geometry, not the identified three-statistic amplitude inverse classification.
3. M. Cappellari et al., *The ATLAS3D project – XXIV* (2014), DOI https://doi.org/10.1093/mnras/stu1603: relates to galaxy-population shape inversions and selection assumptions.

A precise priority search cannot rule out an older source giving the same singularity amplitudes or inverse in alternate notation. No independent audit is represented as complete.

Self-review: passed. Independent audit: not yet performed.
