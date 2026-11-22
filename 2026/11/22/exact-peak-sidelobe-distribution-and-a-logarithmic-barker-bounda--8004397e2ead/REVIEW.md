# Scientific review

## Correctness — PASS
The three phase differences are independent Haar variables. The first- and second-lag autocorrelations admit a common arcsine amplitude and an independent uniform relative angle, yielding an exact bivariate density and a single-quadrature maximum CDF. The integral at the Barker boundary equals \(5/36\). A uniform boundary-layer Taylor expansion gives the nonanalytic \(\varepsilon\log(1/\varepsilon)/\pi^2\) coefficient, with rigorously controlled \(O(\varepsilon)\) remainder. The executable checker independently evaluates the original complex correlations and compares the predicted CDF with direct sampling; the proof, not simulation, establishes the all-parameter claim.

## Originality — PASS (best-knowledge)
The closest deterministic polyphase Barker literature provides search algorithms, numerical optima and generalized Barker definitions, but the inspected full texts do not give the probability volume of the four-Haar-phase Barker region. The 2021 peak-sidelobe analysis by Katz and van der Linden bounds deterministic recursive binary families, so it does not imply the exact joint iid Haar law. Existing scalar \(L^4\) moment/variance records for random four-term polynomials do not determine the joint squared sidelobes or their maximum. The historical Friese–Zottmann article and a broad survey were not fully accessible/inspected; an uncatalogued equivalent remains a priority risk. Searches and statement-implication comparisons are detailed in AUDIT.json.

## Value — PASS
The peak-sidelobe probability is a natural random-code quality metric for pulse compression, and exactly four phases are the first short case with two nontrivial, jointly coupled sidelobe magnitudes beyond the mandatory endpoint sidelobe. The positive mass at the optimal value, the sharp logarithmic transition and the complete two-dimensional density yield reproducible quantitative baselines for random phase-code generation and near-optimal acceptance, not merely a known deterministic existence example.

## Closest literature and scope
Katz–van der Linden (2021); Borwein–Ferguson (polyphase low autocorrelation); Manda–Kumar (2021); Friese–Zottmann (1994); Schmidt (2016). The theorem is restricted to iid continuous Haar phases of length four; no larger-size or finite-alphabet assertion is implied. Independent mathematical review remains unperformed.

Self-review: passed. Independent audit: not yet performed.
