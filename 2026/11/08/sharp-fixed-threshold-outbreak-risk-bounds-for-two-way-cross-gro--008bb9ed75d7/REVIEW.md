# Scientific review: fixed-threshold two-way outbreak risk

## Correctness — PASS

The two-type Poisson offspring generating functions give the exact survival equations \(x=1-e^{-ay}\), \(y=1-e^{-bx}\) and the next-generation eigenvalue \(R=\sqrt{ab}\). The scalar composite fixed point is strictly increasing and strictly concave and therefore has a unique positive solution precisely for \(R>1\). The key analytic step establishes strict convexity of \(F(u)=\log[-\log(1-u)/u]\) for the **whole** interval \(0<u<1\). In the non-immediate case, the inequality is converted to a positive-coefficient comparison of the exponential series, with all powers from degree four having strictly negative remainder coefficients. Its inverse is strictly concave, giving the sharp Jensen upper bound, strict chord lower bound, equality conditions and monotone directional asymmetry comparison. The explicit subcritical mean-matrix inverse and AM–GM provide the complete expectation classification. Critical extinction and infinite expected progeny are addressed. The standard-library checker passed 1,664 finite exact/numerical assertions; the universal inequalities rely on the analytic argument rather than finite tests.

## Originality — PASS within available evidence; priority provisional

The author-hosted 2004 full text by Ball, Britton and Lyne studies multitype household epidemic reproduction thresholds and vaccination coverage optimization, not the sharp nonextinction interval at a **fixed** Perron root. Rao and Bauch (2006) address branching extinction and vaccination without this two-type rate-product optimization; Alexander and Day (2010) address pathogen emergence with mutation. Aravinda et al. (2024) derive general multitype Poisson extinction fixed points and a series expansion (especially Theorem 5.3), but not the global strict extremal bound. The accessible published research records concerning coupled SEIR reproduction-number bracketing, household reproduction-number rank reversal, and matrix-splitting thresholds neither state nor imply the present risk inequality. The 2014 zoonotic multitype outbreak paper was accessible only at abstract level. Missing historical monographs and uninspected full papers remain a priority risk; search absence is not a novelty proof. The supported conclusion is best-knowledge non-coverage, not independent historical certification.

## Value — PASS

At fixed \(R\), outbreak nonextinction can range over a strict, sharp interval, with equal directional rates maximizing outbreak risk above the threshold; the same balance minimizes the mean outbreak burden below threshold. A threshold-only risk comparison thus hides a large structural difference. The exact endpoint, nonattainment, equality and monotonicity classification answer a motivated two-group epidemic question, rather than an arbitrary numerical slice. Interpretation is confined to an idealized early-phase branching model; there is no claim about finite SIR interventions or fixed-total-contact budgets.

## Limitations and reproducibility

All reproductive rates are strictly positive, offspring are Poisson and purely cross-type, and the founder type is equiprobable. No inference is made for arbitrary multitype networks, unequal seed types or susceptible depletion. Run `python3 verification.py` to reproduce the recorded deterministic checks. The complete proof and exact assumptions appear in `RESULT.md`; finite sample diagnostics do not prove the all-parameter theorem. Relevant accessible literature and outstanding historical-priority risks are documented in `AUDIT.json`.

Self-review: passed. Independent audit: not yet performed.
