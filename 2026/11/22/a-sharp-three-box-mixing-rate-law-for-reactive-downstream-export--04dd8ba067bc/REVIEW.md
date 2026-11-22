# Scientific review: three-box mixing-rate law

## Correctness — PASS

The steady mass-balance matrix is a nonsingular compartmental M-matrix. Explicit cofactor formulas give all three outflow fractions. The middle-input derivative is a quadratic with coefficients whose zeros interlace in a known order; this proves the complete strict classification, including equality boundaries. For the other source locations all derivative coefficients have one strict sign. Two-box derivatives are strict constants over a positive square denominator. A standard-library exact-arithmetic checker re-solves 2,500 random rational instances for each source and passed 25,248 assertions. The proof applies to every positive removal-rate triple and every nonnegative common exchange rate, not just tested instances.

## Originality — PASS, provisional relative to inspected sources

Scientific comparisons covered publicly indexed results on estuarine box dispersion and reactive phosphorus balances, and analogous published mathematical findings on finite-time two-box exchange and serial nutrient removal. Soetaert and Herman (1995) give the conservative tracer transport equations but not a stationary reactive export optimization theorem. Alexander et al. (2002) analyze nutrient transport and first-order retention at watershed scale. Håkanson and Bryhn (2007) study a more detailed lake model, not this exact first-three-compartment exchange classification. The inspected material from Gresch et al. (2009) presents a CFD-to-compartment approximation and mentions backmixing but does not give the stated sharp phase diagram. No checked statement directly implies all three source-location laws plus the threshold classification. This is a best-knowledge originality judgment, not an assertion of priority over inaccessible literature. Residual risk includes older literature on compartment mixing and the inaccessible full 1984 Shanahan–Harleman article.

## Value — PASS

The first occurrence of nonmonotone mixing-rate sensitivity in a directed reactive chain is a structural boundary relevant to water-quality risk assessment. The exact middle-loading classification distinguishes an interior worst-case mixing rate from an interior best-case one using only local attenuation constants, and its exact example makes the effect non-negligible. This is not merely another computed point on a generic curve: it is a full global bifurcation classification for a natural three-compartment water-balance family. It can serve as a benchmark for reactive transport solvers and for deciding when the common assumption that greater dispersion has a monotone effect is safe. It is not a calibrated environmental forecast.

## Limitations and closest literature

Equal volumes, common exchange, fixed throughflow, point-specific loading and strictly first-order reaction are essential restrictions. Full historical coverage is not established. The most relevant accessible primary materials are the 1995 Westerschelde model (transport without reaction), the 2002 Waikato nutrient transport study (reactive losses, spatial watershed model), and the 2007 lake phosphorus model (mixed sediment and water compartments). The full 1984 lake-transport paper and full 2009 reactor paper remain incompletely accessible. The result is self-contained and analytically established under its model assumptions, with no independent audit.

Self-review: passed. Independent audit: not yet performed.
