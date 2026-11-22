# Mathematical review: Three placement regimes versus universal balanced coverage in a two-crop pollination model

## Correctness

**PASS.** Global optimality follows from strict exterior monotonicity and the strictly decreasing stationary ratio \(t/\sinh t\). All three cases, equalities, and the symmetric pair of noncentral maxima are covered by the analytic sign argument. A separate log-concavity proof gives the unique midpoint maximum for both-crop service. The proof also independently establishes the strictly ordered fixed-strength spacing thresholds and the square-root bifurcation. The exact \(\log2\) construction and `python3 check.py` (482428 supplementary assertions) support reproducibility; no numerical enumeration substitutes for the proof.

## Originality

**PASS on inspected material, with a priority limitation.** The inspected 2021 InVEST study supplies exponential distance-based pollinator visitation and a simulation-based placement problem; the 2018 field study supplies empirical distance trends; the 2023 individual-based work emphasizes effective rather than merely observed visitation. The 2004 Oikos paper already derives the Poisson one-hit service response, which is **not** claimed as novel. None of the inspected accessible results states or implies the complete combined two-crop expected-versus-joint-coverage optimizer classification. Public mathematical research records on sensor placement, pollinator-network reliability, and landscape trapping use differing objectives/kernels. Equivalence searches do not prove priority, and the 2004 full-document visual comparison was limited by access.

## Value

**PASS.** This is an exact phase diagram for an ecologically motivated placement decision. It isolates the substantial distinction between serving as many crop units as possible *on average* and requiring that both units be served: the latter is always centrally optimized, while the former undergoes two sharp, physically interpretable placement transitions. The fixed-strength separation law makes the boundary meaningful without a fitted downstream prediction. The mathematical fact stands independently of field calibration.

## Closest literature and limitations

Desaegher, Sheeren and Ouin (2021), https://doi.org/10.1111/1365-2664.13949, is the closest field-informed spatial optimization paper. Ganser and colleagues (2018), https://doi.org/10.1002/ece3.4631, report observational distance effects. Kortsch and colleagues (2023), https://doi.org/10.1111/1365-2435.14353, demonstrate why visits are not automatically effective pollination. Feldman, Morris and Wilson (2004), https://doi.org/10.1111/j.0030-1299.2004.12845.x, establish the pre-existing Poisson success transform. Full historical priority remains unverified; a broader facility-location theorem might subsume the exact model. Both-source coupling, crop heterogeneity and real yield are outside scope. Numerical checks supplement but do not replace the proof.

Self-review: passed. Independent audit: not yet performed.
