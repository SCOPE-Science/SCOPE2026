# Scientific review

## Correctness: PASS

The normalized spherical degree-one reproducing kernel is verified using sphere second moments. The pair mean-square formula is reconstructed from Hilbert-space polarization. A Haar-averaging argument handles every coupling, not only isotropic ones. The resulting constant/linear two-level spectra and Jensen inequality prove the bound with equality **only** for fixed inner product \(-1/d\). The exact symbolic checker verifies the difference factorization and comparison cases. Twenty independent empirical spectral comparisons agree within their declared Monte Carlo tolerance. The proof does not use finite experiments as a substitute for quantification over all dimensions or couplings.

## Originality: PASS (best-knowledge, provisional priority)

The motivating first-public source is Brauchart et al., *Needlets Liberated* (arXiv:2207.12838), primary MSC 42C10, first public July 26, 2022; its actual text was examined through the introduction, generalised cubature setup, Theorem 4.1, proof, Section 4.1 and conclusions. Its multiscale QMC-design needlet error bound does not imply the sharp covariance/minimax coupling formula for **this** first-band random estimator. QMC designs (arXiv:1208.3267) concern deterministic Sobolev cubature asymptotics, not the fixed-\(2m\)-sample paired error operator. The 2025 Monte Carlo spherical quasi-interpolation study is related later context but addresses scaled radial-basis kernels and multilevel concentration; its abstract was checked, not its full theorem text. Multiple semantic searches of the published finding collection returned no same-statement match. Residual priority risk: general optimal antithetics/coupling theory or a specialized spherical sampling paper could imply this precise two-sector minimax result, including after a non-obvious reduction.

## Mathematical value: PASS

The first nonconstant spherical Fourier band is the natural finite-dimensional test case for replacing exact cubature by stochastic measurement. Rather than a generic rate or a routine point estimate, the theorem classifies **all** dependence structures that are minimax-optimal under fixed uniform marginals, identifies a non-antipodal optimal angle in all dimensions, and quantifies why the default antithetic choice can increase error. The distinction between pairwise kernel orthogonality and antipodal geometric symmetry provides a generalizable design principle, though no higher-band theorem is claimed.

## Limitations and comparative literature

The sharp conclusion applies only to the specified real first-band estimator, independent identically distributed pairs, uniform marginals and equal weights. It is not a substitute for deterministic spherical designs, which can be exact on the entire band with more nodes. Historical priority is provisional until expert review and specialized general coupling literature comparison.

Self-review: passed. Independent audit: not yet performed.
