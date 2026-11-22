# Review of the curvature-histogram inverse for triaxial ellipsoids

## Correctness (C) — PASS

For strictly ordered semiaxes, the linear sphere parameterization gives the exact induced surface-area weight \(abc\sqrt{Q(u)}\) and positive Gaussian curvature \(C/Q(u)^2\). The two-root transformation of the spherical axial coordinate gives the normalized one-dimensional density. At the four extremal poles the quadratic-sublevel derivative yields finite endpoint-density limits. At the two saddle poles, a one-positive/one-negative Hessian yields the specified logarithmic coefficient. Dividing endpoint densities cancels the unknown surface-area normalization and gives the algebraic inverse. All critical values are explicitly classified. Four independent semiaxis choices passed 124 deterministic diagnostics: area Jacobian, weighted spherical CDF, endpoint limits, exact inversion, and Gauss–Bonnet mean. The proof, not numerical approximation, covers every \(a>b>c>0\).

## Originality (O) — PASS, with a meaningful derivability risk

The exact curvature and surface-area formulas are classical, in particular Poelaert–Schniewind–Janssens [1]. Hillier [2] completely treats the **unweighted** random-sphere quadratic-form density and its eigenvalue singularities. Thus the area-weighted curvature density is derivable by reweighting and a monotone variable substitution, and neither of those general ingredients is claimed as original. The retained new statement is the **three-statistic inversion from only the two curvature-support endpoints and their one-sided density ratio**, independent of total surface area; its explicit cancellation, recovery of all three axes, and complete critical-density characterization were not found in inspected primary material or semantic record searches. This is not the same as the section-diameter and area/perimeter-tomography results returned for triaxial ellipsoids. The strongest residual risk is an unlocated earlier observation that the eigenvalue density endpoint ratio already solves exactly this inverse problem after the known curvature change of variables. Originality is assessed only against actually inspected and retrieved sources, not as a guarantee of global historical priority.

## Value (V) — PASS

A histogram of intrinsic Gaussian curvature under uniform surface sampling is a natural measurable shape descriptor, and inverse recovery from sparse summary statistics is a motivated geometry problem. The finding determines the complete density, distinguishes generic triaxiality via the unique saddle logarithm, and gives an **exact** reconstruction of scale and all axis ratios from exactly three boundary statistics, with no surface-area measurement. This is a structured shape-inference result, not merely a numerical value of a special-case integral. It does not claim stable recovery under noisy sampling or a general theorem for all convex surfaces.

## Closest literature and boundaries

[1] D. Poelaert, J. Schniewind, F. Janssens, *Surface Area and Curvature of the General Ellipsoid*, arXiv:1104.5145, first posted 2011-04-27. Full text equations (5) and (16) provide the input surface element and curvature, but no area-uniform curvature-density inverse.

[2] G. Hillier, *The Density of a Quadratic Form in a Vector Uniformly Distributed on the n-Sphere*, Southampton Discussion Paper 9902 (1999; revised July 1999), *Econometric Theory* 17 (2001), DOI 10.1017/S026646660117101X. Full accessible parsed text discusses general spherical quadratic-form density, not ellipsoid surface-area sampling or an inverse from endpoint density ratios. PDF image screenshot access was blocked; the textual extraction supplied the relevant theorem and preliminary definitions.

Related published records on ellipsoid section perimeter caustics and section-diameter reconstruction concern different observables. Source-access and literature-search incompleteness are retained risks. The statement excludes spheroids and finite-sample statistical error.

Self-review: passed. Independent audit: not yet performed.
