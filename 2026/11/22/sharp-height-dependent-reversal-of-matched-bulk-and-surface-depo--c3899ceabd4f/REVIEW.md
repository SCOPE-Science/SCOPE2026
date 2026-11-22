# Scientific review

## Correctness (PASS)

The Robin Green profile satisfies the homogeneous differential equation away from the center, the two endpoint flux laws, and the exact derivative jump at the emitting sheet. Positivity of the Robin energy gives uniqueness. Two strict hyperbolic-function inequalities establish that the local/global ratio starts below one, crosses it exactly once on each half-slab, and peaks above one at the midplane. Direct integration establishes the strict height-mean excess. The semigroup argument proves the limited long-exposure dose implication. The standalone supplementary checker passed the exact elementary case and 504 positive-parameter numerical configurations; numerical checks are not substituted for the infinite-parameter proof.

## Originality (PASS, bounded by inspected literature)

Bansal, Kaouri and Woolley, *Extending indoor airborne infection risk modelling to 3D, with local surface deposition* (arXiv:2611.13372; first public 9 November 2026), motivates this comparison and states model equations and numerical risk comparisons. Its inspected Sections 1–4 and Appendix B do not give the exact surface-to-volume-calibrated planar-source threshold, its all-positive-parameter sign pattern, or the strict mean bias. Xue et al. (arXiv:2408.11772) study the globally removed original VIRIS model. Pretty et al. (arXiv:2309.16332; DOI 10.1017/S0956792526100485) do report locations where a global ventilation approximation over- or underpredicts local ventilation, so generic sign reversal is explicitly **not** claimed as new. Aquino (DOI 10.1017/jfm.2024.294) develops Robin-wall channel-transport profiles but not this point-driven stationary model-pair comparison. Broad historical Robin Green-function methods remain prior art. Equivalent unpublished or unindexed formulas remain a priority risk.

## Value (PASS)

The numerical epidemiological comparison asks whether replacing local wall deposition by a global sink consistently underestimates infection risk. The exact minimal-slab result gives a structural answer that differs by receiver height: the same globally calibrated replacement overestimates near reactive surfaces, underestimates at the emitting plane, and underestimates even the spatial mean. The explicit height threshold exists for every positive transport and deposition choice, with an exact rational-exponential example. It is a benchmark for where a height-averaged approximation can or cannot be conservative, not a disease-outbreak prediction. Its simultaneous mean/local sign pattern and exact threshold are the motivated contribution, not the classical Green formula alone.

## Closest work and remaining risks

The closest scientific source is Bansal et al. (2026), whose full-text numerical study is more realistic spatially but lacks the claimed universal analytic threshold on this reduced geometry. Pretty et al. (2023/2026) already investigate a different local-versus-global removal phenomenon. Aquino (2024) and standard reaction–diffusion theory make the Robin solution technique familiar and leave a credible risk of older equivalent textbook or applied mathematical statements. The actual calibration and horizontal-sheet emitter restrict direct transfer to clinical buildings. These limitations do not alter the stated theorem's quantified domain.

Self-review: passed. Independent audit: not yet performed.
