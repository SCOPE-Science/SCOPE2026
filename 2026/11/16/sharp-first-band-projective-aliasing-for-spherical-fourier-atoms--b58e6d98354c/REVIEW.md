# Scientific review

## Correctness (PASS)

The exact projection uses rotational integration and \(\int\omega_i\omega_j\,d\sigma=\delta_{ij}/3\), with Bessel normalization checked directly. No simultaneous zero of \(j_0\) and \(j_1\) occurs. The projective ratio is unique wherever the constant coefficient is nonzero, and the exceptional zero-mean fibers are axial. On each higher complete radial interval, monotonicity explicitly yields **two** solutions for each nonzero ratio, and one whole sphere for the zero ratio; this covers all nonnegative radii. The sharp closed-ball cutoff follows at the first zero of \(j_0\). The Euler sine partial-fraction expansion proves both Jacobian lower bounds globally on the alias-free ball; integration of a symmetric positive Jacobian proves the sharp metric inequality. Gram and affine-rank identities follow from exact four-coordinate algebra. The standard-library `CHECK.py` independently checks 914 finite numerical instances, but proof of the universal assertions is analytic.

## Originality (PASS relative to inspected sources)

Closest primary article: A. Fannjiang, *Spherical ESPRIT by Paired Small Circles and Infinitesimal Rotations*, arXiv:2609.33024 (2026-09-26), whose definitions, continuous injectivity, guard-harmonic construction and generic finite cutoff were compared with the present **unguarded first-band complex-projective fiber theorem**. The article's whole-sphere point-cloud identifiability and guarded finite-cutoff methods do not imply sharp one-atom first-band identifiability or the global two-per-band alias geometry without additional analysis. MathWorld/Abramowitz–Stegun establish the raw spherical Bessel identities, not this sharp first-band inverse geometry. Searches of related published mathematical results showed spherical point-cloud Fourier recovery, two-frequency spherical inversion, harmonic sampling frames and real affine projection norms, but none covered this statement by implication. Publication-priority risk remains in older acoustic monopole/dipole spherical-wave localization literature. A negative search is not evidence of definitive novelty.

## Value (PASS)

Four real low-degree spherical-harmonic coefficients are the smallest natural band containing one scalar and a three-dimensional directional moment. Determining exactly when their projective ratios identify a 3D point, the first inevitable alias radius, all global alias fibers, the sharp inverse geometric constant and the multiatom rank simultaneously resolves an inverse-sampling question directly suggested by recent sphere-based Fourier localization literature. The two-to-one radial aliases and the exact \(\pi\) threshold are substantive structural boundaries, not merely numerical perturbations or restatements of the Bessel formulas. These statements are useful for specifying model geometry and for separating single-atom identifiability from general mixture reconstruction.

## Scientific limitations

No noise stability assertion for raw moments uniformly near \(\kappa R=\pi\). No general nonlinear inverse theorem for mixtures of unknown cardinality. Priority against uninspected historical acoustic literature remains a risk.

Self-review: passed. Independent audit: not yet performed.
