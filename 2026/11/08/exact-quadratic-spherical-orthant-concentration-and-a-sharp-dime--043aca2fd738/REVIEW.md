# Scientific review of exact positive-orthant harmonic concentration

## Correctness — PASS

The final claim is the complete pure-degree-two orthant concentration spectrum in every integer dimension \(d\ge3\), its strict ordering, maximizing harmonic, and sharp dimension-squared conditioning law, with the degree-one comparison. The proof uses a fully normalized Gaussian/Dirichlet fourth-moment identity; the five monomial patterns are sufficient for every quartic product of quadratic harmonics. The trace-free quadratic parametrization is an isometry after multiplication by \(d(d+2)\). The unsigned incidence matrix has rank \(d\) for \(d\ge3\), and its constant, standard, and null sectors exhaust the edge space. The only mixed standard sector is exactly the displayed \(2\times2\) Hermitian matrix. A strict-ordering proof is supplied using \(3<\pi<22/7\). Dimension asymptotics use an explicit Schur-complement limit, not numerical extrapolation. An independent gamma-moment Gram-matrix checker passed 399 assertions and is embedded as `orthant_spectral_check.py`.

The checker does not independently prove the all-dimensional result. The proof covers every claimed dimension, multiplicity and normalization. Degree-zero and mixed low-pass spaces are not included.

## Originality — PASS, provisional

The closest primary literature is Simons, Dahlen and Wieczorek, *Spatiospectral concentration on a sphere* (arXiv:math/0408424), and Michel, Plattner and Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator* (arXiv:2103.14650, first released 2021-03-26). Both establish general spherical concentration matrices; the latter gives commuting operators for polar caps. Those general matrices do not themselves state the orthant eigenvalue values/multiplicities or the dimension-squared sharp constant. Their mathematical approach is foundational and is explicitly credited. Related formulas on hemispheres, lunes, and signed-coordinate cap unions are different observation geometries, and none directly implies the exact orthant moment tensor. Searched publication and mathematical-result records did not locate an equivalent all-dimensional positive-orthant theorem, although negative search evidence alone would not prove uniqueness.

Risk: the evaluated spectrum could have appeared as an implicit special case of a symmetric-group fourth-moment/orthant-design calculation, possibly in literature outside the exact Slepian vocabulary. Therefore historical priority is provisional and independent appraisal is needed.

## Mathematical value — PASS

The positive orthant is a canonical spherical simplex and a fundamental chamber of coordinate sign reflections. It is a stringent non-axisymmetric observation geometry in which full reconstruction remains injective for pure degree one and two. The exact four-sector quadratic spectrum, unexpectedly close separation of the weakest sector from the \(\ker B\) sector, dimensionally persistent multiplicities, and sharp \(d^2\) versus \(d\) concentration-conditioning contrast quantify a mathematically natural restriction-stability barrier. The dimension-squared asymptotic constant is an exact intrinsic invariant of this standard observation family, and the extremizing harmonic and least sector are identified. This is more than a re-expression of the abstract concentration eigenproblem; the strong structure and asymptotic answer require explicit moment calculations and spectral decomposition.

Limitations: no higher-degree, arbitrary-cone, finite-sampling or noise-robustness result is asserted. The result is self-contained, not a claim of general Slepian optimality.

Self-review: passed. Independent audit: not yet performed.
