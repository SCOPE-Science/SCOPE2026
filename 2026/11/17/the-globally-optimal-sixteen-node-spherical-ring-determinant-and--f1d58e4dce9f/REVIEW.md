# Scientific review

## Correctness

**PASS (self-review).** The harmonic evaluation matrix is reduced by independent ring Fourier transforms to derivative-Legendre Vandermonde blocks. The product of block determinants yields the stated positive normalization and height-dependent factor. For each of the six connected height-ordering chambers, the explicit Hessian is uniformly bounded above by \(-4I\), implying a unique interior maximum, a gradient-to-optimum distance bound, and a rational upper bound on the true maximum in terms of one rational test point. The standalone exact-fraction checker verifies all six chamber assignments, the upper bounds, the five strict adjacent chamber comparisons, and the two-sided ratio bound. Thus the finite inequalities imply the claimed global comparison on the continuous domain. The checker was run successfully from the submitted package. The independent numerical sixteen-by-sixteen determinant agreement is a supplementary normalization check only.

## Originality

**PASS against inspected accessible comparisons, with priority risks.** The precise new statement is the six-chamber *global hierarchy* and sharp factor-of-four/ratio law for the minimal sixteen-node degree-three harmonic design. The previously established all-bandwidth determinant and concavity theorem already shows that each chamber has exactly one optimum, but it does not rank those optima. The previous exact nine-node quadratic optimum neither has the same parameters nor implies the cubic ranking. Giacaglia–Lundquist (1972) introduces the same odd-ring node geometry with a prescribed distribution. Khalid–Kennedy–McEwen (2014) establishes the modern iso-latitude one-pole odd-ring sampling analysis and orderwise inversion; Nafees–Khalid–Kennedy–McEwen (2017) studies condition-number-driven placement of that geometry. Neither inspected full text states a determinant hierarchy. Khalid (2026), posted on November 12 after the literature anchor, also analyzes the same rings but optimizes Lagrange interpolation amplification, not this determinant. Dell'Accio–Nudo–Pérez–Piñar (2026) proves general interpolation–regression rank/KKT facts, and Beltrán–Marzo–Ortega-Cerdà (2026) addresses Riesz energy and discrepancy, not the finite-ring determinant. Published related results about two equal rings, one-ring pure harmonics, and continuous-band sampling do not dominate the new result. Search failure is not a uniqueness proof: an earlier unlocated equivalent Fekete/determinant-design computation remains possible.

## Value

**PASS.** The first ring family with three freely ordered nonpolar latitudes is a natural minimal 16-measurement design for 16 harmonic coefficients, and the exact determinant is an information-volume criterion. The six chambers are distinct physical layouts. The result solves the entire finite global layout-choice problem, not just a local or sampled optimization: five exact inequalities give the unique optimal ring arrangement and establish more than a fourfold squared-volume gap to *every* competing ordering. This is actionable for determinant-based sensor layout within the established geometry without claiming numerical-conditioning optimality.

## Closest sources and limits

- G. E. O. Giacaglia, C. A. Lundquist, *Sampling Functions for Geophysics* (1972), https://ntrs.nasa.gov/citations/19730008792; primary report Sections 2.6, 3.1–3.2 and 4.1 compared for ring distributions, Gram determinant conditions, and absence of exact height optimization.
- Z. Khalid, *An \(O(L^3)\) Spherical Harmonic Transform on \(L^2\) Samples* (2026-11-12), https://arxiv.org/html/2611.16441v1; Sections III-B and VI-C and the references compared. This later publication is an overlap comparison, not a motivating source.
- Z. Khalid, R. A. Kennedy, J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms* (2014), https://arxiv.org/html/1403.4661v2; full introduction and Sections III-A, III-E and III-F compared.
- W. Nafees, Z. Khalid, R. A. Kennedy, J. D. McEwen, *Optimal-Dimensionality Sampling on the Sphere: Improvements and Variations* (2017), https://arxiv.org/abs/1709.02497; full mathematical formulation and co-latitude placement sections compared.
- F. Dell'Accio, F. Nudo, T. E. Pérez, M. A. Piñar, *Polynomial interpolation–regression on the sphere* (2026), https://arxiv.org/abs/2605.13124; introduction, definitions, rank hypotheses and main KKT results compared.
- C. Beltrán, J. Marzo, J. Ortega-Cerdà, *A set of points with optimal \(L^2\) spherical cap discrepancy* (2026), https://arxiv.org/abs/2609.27708; introduction, principal Riesz energy/discrepancy and Sobolev error results compared.

No claim is made for arbitrary 16-point Fekete designs, global condition-number minimization, or higher-bandwidth chamber hierarchies.

Self-review: passed. Independent audit: not yet performed.
