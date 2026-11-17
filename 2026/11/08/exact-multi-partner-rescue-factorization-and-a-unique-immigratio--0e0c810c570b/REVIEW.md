# Independent mathematical audit

## correctness

PASS

For reference empty-state hazard D=sum delta_i, couple independent arrivals T_i~Exp(lambda_i) and hazard clocks K_i~Exp(delta_i). The success event is exactly intersection of T_i<K_i for every partner, giving product lambda_i/(lambda_i+delta_i). Changing only the initial empty-state hazard to d0 multiplies success by (B+D)/(B+d0), because fixed budget B fixes total first-arrival rate. For all positive hazards/B, log success has strictly negative second derivative f_i''=-delta_i(2lambda_i+delta_i)/(lambda_i^2(lambda_i+delta_i)^2), so one strictly positive global optimum solves unique KKT multiplier and the displayed quadratic roots. Low/high budget expansions and gain coefficient follow by Taylor; delta_i ordering follows strict monotonicity in hazard at fixed multiplier. Independently compared exact subset CTMC recursion with factorization in 120 heterogeneous rational cases, n=2..5. No finite test substitutes for independent exponential coupling and concavity.

## originality

PASS

The ecological mutualism source Amarasekare (2004) treats spatial two-species metacommunity density and rescue thresholds; its full accessible model and appendices do not have this n-independent arrival-clock product or budgeted allocation. Classical series reliability product law and generic log-concave resource allocation are acknowledged; they motivate, but no inspected primary source specifies the same initial-hazard correction, hazard-ordering and sharp small/large-budget split for this distinct finite establishment model. Originality is best-of-knowledge with particularly substantial generic reliability-theory risk.

## value

PASS

The exact, parameter-uniform solution of a motivated initial establishment problem with arbitrary n independent obligatory partners provides a self-contained baseline for multi-mutualist colonization. The initial-extinction correction, unique interior policy and equal-to-square-root crossover supply a useful benchmark and meaningful allocation boundary, though the clock independence is restrictive and all calculus steps become straightforward after factorization. It is not an empirical policy or a general metacommunity theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
