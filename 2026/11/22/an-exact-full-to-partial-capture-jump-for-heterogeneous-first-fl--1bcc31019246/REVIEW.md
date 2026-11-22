# Scientific assessment

## Correctness — PASS

The exact continuous-time mass and runoff definitions produce the stated \(F(v)\) under a finite-mean strictly positive initial-stock rate law. The proof controls differentiability away from time zero even for laws without a second rate moment. It then establishes a unique minimum of \(H\), a globally supporting line with precisely two contacts, strict concavity up to the first contact, and all four optimal-cost regimes with exact endpoint equality cases. The first/last-flush single crossing follows from the same strictly convex function. The two-rate example's symbolic extrema and a reproducible standard-library checker independently exercise nondegenerate cases. The checker is finite-support diagnostic evidence, not a substitute for the universal analytical argument.

## Originality — PASS (best-knowledge comparison; priority risk remains)

The specific implication being assessed is a universal **full-to-partial capture discontinuity** and *unique four-regime* cost-optimal storage law for a mixture of positive first-order wash-off stocks driven by exponential-runoff time, plus the unique within-event flush sign crossover. Balistrocchi, Grossi, and Bacchi (2009) examine stochastic storm frequency and power-law mass-volume efficiency curves rather than this stock-mixture objective. Kang (2005) models two physical pollutant sources using flow-dependent mechanics, but the checked section does not derive this capacity phase law. Guo and Urbonas (2002) optimize overflow-risk based runoff capture across many rainfall events, a different random object. The closest indexed stormwater result concerns the temporal order of three pollutant-supply stages, not tank capacity and mixture kinetics. The general technique of taking a concave envelope and drawing a tangent is classical, so no priority is claimed for that technique. Millar (1999) was accessible by its abstract only; related historical design work could contain special cases, so independent priority confirmation is needed. No searched evidence established an equivalent or dominating theorem; nonretrieval alone is not treated as novelty proof.

## Value — PASS

In first-flush assessment the object of interest is not simply pollutant removal at a fixed tank size but whether marginal returns favor capturing a whole event or only an initial fraction. For heterogeneous kinetics, the answer has a discontinuous threshold and two distinct globally optimal choices **at the same cost**, unlike straightforward diminishing-returns mass-volume models. A precise sufficient condition on the rate distribution, a computable threshold, the exact equality/crossing structure, and a closed two-source benchmark can inform mathematical stress tests of storage-design heuristics. The quantitative fact is not a generic numerical slice and is not implied merely by an assumed power-law fit. The idealized assumptions limit transfer to actual stormwater design.

## Closest literature and residual limitations

Relevant works: Balistrocchi, Grossi, and Bacchi (2009), DOI 10.1029/2009WR007822 (full accessible article inspected); Kang (2005), freely available thesis (relevant chapter inspected); Guo and Urbonas (2002), DOI 10.1061/(ASCE)0733-9496(2002)128:3(208) (complete open precursor report and journal abstract); Millar (1999), DOI 10.1061/(ASCE)0733-9372(1999)125:10(989) (abstract only, inaccessible full article). The latter and unindexed historical technical reports remain priority risks. Mathematical validity is restricted to the exactly stated normalized single-event model.

Self-review: passed. Independent audit: not yet performed.
