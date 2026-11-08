# Scientific review: cubic-harmonic latitude E-optimality

## Correctness — PASS

The mathematical claim concerns the unique squared latitude maximizing the **least** restriction-Gram eigenvalue for all complex pure cubic spherical harmonics, in every integer ambient dimension \(d\ge3\). The four orthogonal transverse-harmonic sectors are derived from explicit harmonic polynomials, normalized by spherical moments through order six. On the three intervals separated by the radial nodes \(x=1\) and \(x=3\), the relevant pairs have strict opposite monotonicity and unique crossings. Exact finite-dimensional rational witnesses and envelopes distinguish \(d=3\), \(d=4\), and \(5\le d\le11\); independent high-dimensional positive-coefficient identities establish the \(d\ge12\) regime. At each winning crossing inactive sectors are strictly larger. The full analytical proof is in `RESULT.md`. Direct rational certification passed `CUBIC_LATITUDE_RATIONAL_CERTIFICATE_PASS 201`, and an independently implemented Gaussian-Jacobi spherical-moment check agreed with all four formulas at 140 test values. Exact universal claims are proved algebraically, not extrapolated from those test values.

## Originality — PASS, with historical-priority risk

The cited 2017 Nafees–Khalid–Kennedy–McEwen paper uses multiple finite iso-latitude rings and numerical condition-number optimization for full band-limited spherical-harmonic transforms. The cited 2022 Zandieh–Han–Avron paper constructs randomized whole-sphere reconstruction guarantees. Neither inspected primary account supplies the continuous one-latitude pure-cubic global E-optimum. Earlier pure-cubic antipodal-cap spectra give integrated sector formulas from which the **unoptimized** latitude eigenvalues can be differentiated; these sector formulas are not claimed as new. The nontrivial contribution checked for priority is the *complete four-regime global lower-frame optimum*, with active branch changes exactly between ambient dimensions 3/4, 4/5 and 11/12, strict uniqueness, and the high-dimensional limit. Historical-priority risk persists because older associated-Legendre design and general polynomial E-optimality sources may contain an equivalent optimization. A relevant cubed-sphere interpolation paper was available only as a publisher abstract and bibliography, not full text; its data geometry differs, so this is identified as an access limitation rather than treated as decisive evidence of novelty.

## Mathematical value — PASS

Choosing where to continuously observe a pure spherical harmonic band is a natural E-optimal sensor-design problem. Cubic harmonics are the first odd degree with two interior nodal latitude obstructions and four distinct branching sectors; the problem is not a relabeling of quadratic latitude optimization. The proved changes in the active bottleneck, especially the sharp transition at dimension twelve, explain which type of cubic harmonic dictates worst-case stability. The exact parameterization avoids unsupported claims about condition-number optimality. This is a complete natural classification, not an arbitrary numerical slice.

## Closest comparisons and limits

Nafees et al. (2017), arXiv:1709.02497v1; Zandieh et al. (2022), arXiv:2202.12995v1; Bellet, Brachet and Croisille (2022), DOI 10.1007/s00211-022-01340-w. The result applies only to normalized continuous one-latitude traces of pure degree-three harmonics, not finite samples, mixed degrees, condition-number minimization, or arbitrary sampling measures. Claims of independent confirmation or exhaustive historical priority are not made.

Self-review: passed. Independent audit: not yet performed.
