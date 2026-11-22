# Self-review: nested occupancy with one doubly assayed primary sample

## Correctness — PASS

Under site occupancy \(Z\), primary availability \(U_1,U_2\), and conditional independent assays, the proof independently derives the observable moments \(A,B,C,D\). The cross-primary covariance \(V=C-A^2\) and cross-third-moment ratio \(L=(D-AB)/V\) recover \(p+f\); the within-primary moment identifies \(pf=LA-B\). Ordered roots and the remaining cross-primary covariance recover all four parameters. The eight-cell law is reconstructible from these four moments under stated equality and exchangeability constraints. Algebraic invariance proves the two-assay and other three-assay lower bounds. Rational hidden-state enumeration in the bundled checker passed 12,004 assertions, corroborating but not replacing the proof. The restrictions \(0<\psi,\theta<1\), \(0<f<p<1\) and absence of primary contamination are essential.

## Originality — PASS, with residual historical-priority risk

Royle and Link (2006) handle a single-level false-positive occupancy mixture, not the two-level minimal design. Nichols et al. (2008) provide a nested multiscale detection model with no false-positive assay mechanism. Chambert, Miller and Nichols (2015) analyze additional false-positive designs and external truth information. The complete Guillera-Arroita et al. (2017) paper covers a broader, five-parameter two-level model: it explicitly demonstrates label ambiguities and examines calibration but does not state the restricted four-parameter exact 2+1 minimum and four-moment inverse. Its broader generative model includes the present specialized mechanism as a limit, not an implication of the exact minimal identifiability theorem. The inspected published mathematical records concern other occupancy identifiability settings; no exact statement or dominating implication was found. Unexamined latent-class theory and earlier nonindexed literature remain credible priority risks; absence of a search hit is not a novelty proof.

## Value — PASS

Within a realistic hierarchical observation model, a single primary sample cannot distinguish site prevalence from sample availability, and a solitary test on each of several primary samples cannot distinguish sample availability from true assay sensitivity. The identified two-plus-one allocation is therefore a mathematically minimal way to resolve all four unknowns with no gold-standard assay under a known no-contamination condition. The exact attainable-law criterion and Jacobian reveal both statistical feasibility and severe ill-conditioning near low availability. This supplies an interpretable scientific survey-design boundary rather than a mere numerical recomputation. No recommendation for field precision or complex contaminating systems is claimed.

## Closest literature, limitations, and independent status

The most directly relevant later primary source is Guillera-Arroita et al. (2017), DOI 10.1111/2041-210X.12743, which studies the unrestricted two-stage contamination model, including its nonidentifiability. Nichols et al. (2008), DOI 10.1111/j.1365-2664.2008.01509.x, provides the no-false-positive multiscale foundation. Royle and Link (2006), DOI 10.1890/0012-9658(2006)87[835:GSOMAF]2.0.CO;2, establishes single-stage false positive ambiguities (journal abstract and references accessible; entire full text not inspected). Scope excludes upstream contamination and correlated assay errors, and independent historical priority is unresolved.

Self-review: passed. Independent audit: not yet performed.
