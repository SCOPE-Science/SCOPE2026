# Scientific review: Three sharp sowing-date regimes before one random rainfall opportunity

## Correctness — PASS

The proof fixes the conditional-on-rain law and derives the exact inclusion–exclusion objective with all three pairwise terms and the triple term. Moving the earliest planting date to zero strictly improves success. The compact closure analysis excludes the corner and the infinitely delayed third cohort, and shows that no point on the equal-date diagonal except its endpoint can be globally optimal. On the first-date boundary, direct differentiation gives the unique lower threshold. For an interior extremum, the substitution \(y=pv/u\) yields \(u=Z(y)\), a strictly decreasing parametrization; the remaining stationarity function has strictly positive derivative on the entire allowed interval because two explicit quadratic discriminants are negative. Its endpoint sign has exactly the stated second threshold. Existence, uniqueness and all boundary equalities follow; finite randomized computations are corroboration rather than a substitute for this argument.

## Originality — PASS on inspected evidence, subject to historical priority

Farrell et al. (2023), doi:10.1002/eap.2834, motivate timing of dryland seeding relative to rain but the accessible abstract does not contain this probability model or threshold theorem; full text could not be read, so this is a genuine priority risk rather than a claimed full-text exclusion. ten Brink, Gremer and Kokko (2020), doi:10.1111/ele.13461, analyze adaptive germination and dormancy under unpredictable seasons rather than externally timed identical sowing cohorts competing for a single exponential first rain. Agoungbome et al. (2023), doi:10.3390/agronomy13010167, estimate region-dependent sowing windows using simulated rainfall and crop growth, not an analytic three-cohort optimizer. Denton et al. (2024), doi:10.1111/1365-2664.14779, analyze precipitation and ecological restoration empirically. Nearby exact transient-occupancy survey timing and seed-bank diversification statements use different stochastic events, controls and objectives and do not imply the present theorem. More general historical stochastic scheduling and perishable-reliability coverage remains possible.

## Value — PASS

The exact two critical establishment probabilities change the *number of distinct planting times*, not merely the numerical location of an existing optimum. The intermediate two-date regime and third three-date regime demonstrate when independently fading cohorts have a genuine timing-diversification benefit even though all are exposed to a single shared rainfall event. This complete, natural three-cohort classification is a benchmark for restoration timing under uncertainty; it does not claim an empirical schedule or a result for unequal decay rates.

## Reproducibility and limitations

The independent Python 3 standard-library checker tests the exact stationary polynomial identity using rational arithmetic, evaluates the original piecewise event integral independently of the inclusion–exclusion expression, and probes boundary cases and random feasible schedules. The theorem still rests on the analytic proof. Exponential rain, equal-rate viability loss, conditional independence, exactly three cohorts and absence of a final seasonal deadline limit applicability. The motivating full primary text was not accessible through available routes; a complete historical priority audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
