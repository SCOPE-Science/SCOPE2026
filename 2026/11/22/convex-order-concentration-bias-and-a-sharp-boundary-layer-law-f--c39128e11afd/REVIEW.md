# Mathematical review

## Correctness — PASS

The exact Fourier/Parseval objective and differentiated stationarity equation are reconstructed in RESULT.md. The normalized derivative ratio is strictly decreasing for every positive source radius, proving a unique global stationary minimizer; strict Jensen of a rational convex function establishes concentration bias and convex-order monotonicity. A uniform implicit-function expansion gives the small-spread coefficient. Compact-depth scaling of the same equation proves the unique boundary constant and the exact limiting optimized error through the closed rational objective. The included deterministic checker reports 91 passed finite assertions. Continuous and asymptotic conclusions are proved analytically rather than extrapolated from finite checks.

## Originality — PASS, best knowledge, with residual risk

Bailey's 2019 thesis, Appendix C2, equations (6.10)–(6.12), explicitly supplies the two-wrapped-Cauchy Fourier loss and a stationarity equation. Those are prior results and are not claimed new. The present claim additionally proves strict global uniqueness for arbitrary mixing laws, the convex-order comparison and strict bias, and the full boundary-layer depth and sharp positive error constant. These do not follow from the cited formulas without substantive inequality and asymptotic analysis. The separate Bailey–Codling 2020 deposited article compares circular model families for a different underlying mixture; the 2023 Tsagris–Alzeley article concerns directional-model families and likelihood fitting. Indexed mathematical-record searches for equivalent convex-order and Poisson-mixture projection claims found no recorded complete equivalent; these searches cannot prove global priority. Potential equivalence under kernel mean embeddings or old approximation theory remains a real historical risk.

## Value — PASS

Mixed Poisson/wrapped-Cauchy distributions naturally arise from heterogeneous concentration parameters in directional observations and harmonic extensions. The question of replacing a mixture with one kernel is an explicit approximation task in the cited thesis. The result explains why least-squares concentration is systematically biased upward even at fixed first Fourier moment, establishes rigorous ordering under heterogeneity, and quantifies a singular boundary regime where approximation loss becomes unbounded at a sharp rate. Its scope goes materially beyond a stationary equation or a small finite example.

## Evidence and limitations

The proof covers compact radial mixing measures of nonnegative probabilities and a common angular center. The boundary law assumes fixed compactly supported positive source depths. Source material inspected includes Bailey's exact Appendix C2 mathematical equations and surrounding numerical interpretation, the public summaries and accessible text of Tsagris–Alzeley and Bailey–Codling, indexed comparative records and relevant published mathematical-record summaries. Inaccessible/unexamined historical full texts and equivalent formulations remain priority risks; none of the checked statements decisively dominates the new combined theorem. No external proof verification or independent audit is asserted.

Self-review: passed. Independent audit: not yet performed.
