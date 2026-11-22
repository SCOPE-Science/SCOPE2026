# Scientific assessment

## Correctness — PASS

The stated object and operation are fully defined. A direct matrix exponential gives surface accumulation and the surface-to-air impulse response; linearity reduces the exposure benefit exactly to a positive coefficient times \(f(\tau)L(T-\tau)\). Strict log-concavity of both factors establishes a unique interior maximizer, not merely a critical point; an implicit-function sign proves strict horizon monotonicity. Short- and long-horizon expansions follow from Taylor series and a nondegenerate peak derivative. The proof specifies endpoints and fixed-positive-rate asymptotic scope. Reproducing the included checker gave 31,536 numerical comparisons, including independent ODE integrations; numerical testing is explicitly not used as the proof of the universal statement.

## Originality — PASS on inspected evidence

The defining 2023 smoke-VOC paper (Li et al., DOI 10.1126/sciadv.adh8263) contains the exact linear gas–surface model, experimental cleaning, and reservoir dynamics; it does not give the exact finite-horizon one-wipe optimizer or its spectral characterization in the material read. The 2017 Lei–Jones–Li cleaning study (DOI 10.1186/s12879-016-2120-z) considers hospital contact transmission and a different cleaning objective. Blanchini et al. (DOI 10.1016/j.automatica.2022.110680) provide strong prior general positive-compartmental optimal control with continuously adjusted arc flows; their allowable interventions and switching theorem do not directly imply the stated fixed-generator instantaneous-reservoir-reset optimization without a separate derivation. Nearby retrieved research concerns aerosol ventilation budgets, contaminant plume sensors, stormwater wash-off order, and optimal sampling of exponential modes. Historical priority remains provisional: another older impulse-control or indoor-air engineering result might already present an equivalent calculation or stronger theorem.

## Value — PASS

The motivating experimental literature explicitly finds that post-smoke surface reservoirs prolong airborne VOC exposure and that physical removal affects persistent levels. A finite deadline creates a nontrivial tradeoff: cleaning immediately removes nothing, while cleaning at the deadline prevents no exposure inside the window. Uniqueness and a two-mode calibration law permit a globally optimal intervention time without separately estimating all adsorption, desorption, and ventilation coefficients. The exact \(1/3\) short-window rule and long-window surface-peak limit reveal mathematically distinct scheduling regimes. This is a useful self-contained benchmark rather than a validated field protocol or universal recommendation.

## Sources and boundaries

Primary open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC10575580/ (especially equations (1)–(2), surface-cleaning findings, and limitations). Closest different-object sources: https://link.springer.com/article/10.1186/s12879-016-2120-z and https://iris.unitn.it/retrieve/cd15dadf-d327-4a44-9014-aac0cddefec4/Automatica_OptimalControl.pdf . Model scope excludes additional pollutant sources, multiple sorbing reservoirs, nonlinear surface chemistry, cleaning-generated VOCs, time-varying rates and uncertain parameters. The proof and numerical checker have not been independently audited.

Self-review: passed. Independent audit: not yet performed.
