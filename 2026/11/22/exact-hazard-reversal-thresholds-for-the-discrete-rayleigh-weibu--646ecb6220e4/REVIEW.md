# Self-review of the Rayleigh–Weibull hazard theorem

## Correctness — PASS

The full domain is \(0<q<1\), \(t>0\), \(\beta>0\), all ages \(n\in\mathbb N_0\). The survival is normalized at zero, strictly decreases, and tends to zero. The sign of the difference of consecutive hazards is exactly the sign of a second difference of the squared-odds cumulative hazard, not an approximate continuous derivative. The power-series proof separates finitely many negative powers from all later positive powers to establish one and only one positive root for every index when \(0<\beta<1/2\). The triangular-kernel monotone-likelihood-ratio argument proves strict ordering of these roots across all integers; it includes the delicate \(n=0\) singular endpoint through an integrable weighted limit. Rescaling the central second difference proves the asymptotic constant. The symbolic factorization and numerical root checks in `check_hazard.py` were rerun successfully; numerical checks are supplementary only. The critical domain limit \(\beta=1/2\) is covered explicitly, with strict hazard increase for all \(t>0\).

## Originality — PASS (qualified best-knowledge comparison)

The original 2020 discrete Rayleigh-G paper already defines the squared-odds law and its Weibull subfamily. Its Section 3 and Figure 2 give graphical hazard descriptions rather than a necessary-and-sufficient global phase boundary. The 2023 generated Rayleigh-G article generalizes odds powers but also gives qualitative shapes. The related 2022 discrete Weibull-Rayleigh model uses a fixed quadratic inner argument; it does not imply the variable-inner-Weibull exponent threshold staircase here. The 2024 general discrete Weibull generated-G family contains the present distribution as a nested case, but its formula and graphical shapes do not entail the claimed exact global agewise monotonicity theorem. Related general Weibull-G generation from 2014 explains the construction, not the integer second-difference geometry. Published-result semantic searches found analogous hazard phase theorems for **different probability laws**, not this statement or a dominating equivalent. A relevant unindexed or otherwise undiscovered theorem remains possible; absence from search results is not proof of absolute novelty.

## Value — PASS

A discrete reliability model previously assessed through parameter plots has a sharp global division between increasing and bathtub hazard, a unique possible flat transition, exact monotone integer-age boundaries and a universal rescaled threshold limit. The complete classification rules out complicated reversals within this natural Weibull-baseline Rayleigh generator and makes the time of the minimum interpretable from the model's shape and scale, independently of the generator's \(q\) parameter. It addresses reliability-shape calibration across infinitely many ages rather than evaluating an arbitrary finite slice or making a simple substitution.

## Closest literature and scientific limits

Sources: Aboraya et al. (2020), https://doi.org/10.3390/math8101648; Emam et al. (2023), https://doi.org/10.3390/math11051125; Ma and Yan (2022), https://doi.org/10.2298/TSCI2203627M; Yousof et al. (2024), https://doi.org/10.18187/pjsor.v20i4.4616. The theorem does not extend automatically to the full generalized-odds generator or arbitrary outer Weibull powers. Some older continuous Weibull-G literature was checked through the references of these sources rather than exhaustively through every edition; historical-priority risk persists. No external mathematical audit was requested or performed.

Self-review: passed. Independent audit: not yet performed.
