# Independent mathematical audit

## correctness

PASS

For iid atomless observations, all strict rankings of the w+ℓ observations from index −1 through w+ℓ−2 are equally likely. For an upward start surviving ℓ observations, the greatest must be at w−1; this has probability 1/(w+ℓ). For a downward start surviving ℓ, the greatest must be at −1 and the second greatest must lie in the w−ℓ+1 surviving current-window positions. This has probability (w−ℓ+1)/[(w+ℓ)(w+ℓ−1)]. Both conditions are sufficient as well as necessary, since a unique observation cannot reappear after leaving a window. At ℓ=1 both start types have probability 1/(w+1), including w=1. Division, equal mixing, and Bayes' rule give the four tails/posterior. Tail summation gives the harmonic-number upward mean and the telescoping start mean (w+1)/2; the downward mean then follows from the mixture. For the deterministic-time residual, the maximum in the union of the ℓ+1 consecutive windows must be in their common intersection, giving (w−ℓ)/(w+ℓ) for 0≤ℓ≤w. The interior scaled survival functions converge to (1+x)⁻² at starts and (1−x)/(1+x) at a deterministic time. The first gives interior density 2/(1+x)^3 and mass 1/4 at one, also the limit of the exact terminal probability; the second has no endpoint atom and integrates to 2 log 2−1. Frozen replay path: verify_moving_max_plateaus.py, lines 27–74, for w=1 through 4, inspected and not executed. The 368,046 permutations and 56 comparisons are the source's reported finite verification, not the basis of the arbitrary-width proof.

## originality

PASS

The substantive distinction is the exact split by upward and downward plateau start, including its linear type posterior; none of the inspected prior statements supplies or implies that split from the aggregate law. The quarter atom and deterministic-time residual are not independent originality claims: the residual determines the aggregate start tail by stationary differencing. The strongest distinct same-day all-rank result demonstrably covers the aggregate maximum law and quarter atom, and explicitly credits the assigned result for rank one; no within-day priority is inferred from its date. Neither its stated law nor its rank-one specialization determines the two directional tails.

## value

PASS

Repeated equal block maxima are a genuine feature of strongly overlapping samples even for atomless data. The direction-conditioned laws answer a practical mathematical question not answered by the start intensity or untyped survival: an entering record is at the newest position, whereas the maximum revealed by a departure can immediately leave. In particular the maximal-duration mass tends to 1/2 for upward starts and zero for downward starts, explaining the aggregate atom and why sampling a stationary time gives a different tail. This is an exact diagnostic for sliding-block dependence, not a claim about improved inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
