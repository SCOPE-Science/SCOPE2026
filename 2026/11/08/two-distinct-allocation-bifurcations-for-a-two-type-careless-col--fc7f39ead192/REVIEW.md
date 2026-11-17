# Independent mathematical audit

## correctness

PASS

The actual four-state post-loss transition kernel has nonnegative normalized rows; one-label stationarity m_i=q_i/(2-q_i) yields Pi=t(s-t)/(4-2s+t). Independent 3-transient-state hitting equations yield H=((5-s)t+4-2s)/(t(s-t)). At fixed s in (1,2), feasible t is [s-1,s^2/4]; exact differentiation gives strictly decreasing D_Pi=(4-2s)(s-2t)-t^2 and increasing D_H=(5-s)t^2+2(4-2s)t-s(4-2s), so clipped unique roots, with four endpoint polynomials, are global optima. Independent SymPy checks verified derivatives and exact budget-half values 27/80,152/27,1/3,11/2. Cubic root intervals in (1,2) follow derivative positivity; boundary one loss probability zero is included. Finite budget meshes do not prove continuum uniqueness.

## originality

PASS

The Cruciani–Dudeja FUN 2026 full HTML paper studies common loss probability p and names type-dependent losses as future research, so it does not imply a fixed total heterogeneous budget two-objective phase diagram. Other Resultary clumsy coupon exact balancing results concern a different replacement/erase model or sampling weights. No stronger published same post-erasure two-type optimization was found; no failed-search novelty guarantee.

## value

PASS

The allocation of a fixed erasure budget is a natural robust-cache design decision; stationary all-held availability and transient recovery time are different mathematically motivated operational objectives. Their sharply separated optimal strategies and four exact thresholds provide nontrivial new information beyond elementary mean-time evaluation, with a strict rational witness at B=1/2.

The dated certificate retains the supplied scientific assessment, sources and limitations.
