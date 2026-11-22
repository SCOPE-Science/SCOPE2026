# Scientific review

## Correctness — PASS
The mathematical object is the probability that a uniformly timed emigrant released during an active source interval reaches an equally long destination active interval after exactly two independent exponential transit stages. The domain explicitly covers every positive rate and active duration and every real opening date. Equations (1)–(4) classify the derivative throughout the real line; the unique positive zero of \(e^x=1+2x\) determines the single touch transition. Implicit differentiation and the exact tail expression prove the strict monotonicity and sharp mode-to-median limits. The CDF antiderivative checks the small-window success asymptotic, and the one-stage comparison is derived separately. A standard-library checker independently exercises the resulting formulas at 39,007 finite comparisons. This is a mathematical self-review, not independent certification or proof by sampling.

## Originality — PASS on the inspected record
The closest motivating article, Moisset de Espanés and Ramos-Jiliberto (2024), makes dispersal events conditional on simultaneous habitat availability and reports numerical metacommunity sensitivity. It does not optimize a delayed arrival-window success probability. Karnatak and Wollrab (2020) study probabilistic network dispersal, not the finite uniform-emission/Erlang arrival calendar; Hockaday and colleagues (2024) measure hydroperiod-dependent responses experimentally. Related mathematical research on exponential presence-episode monitoring, exponential spatial dispersal between bands, and Gamma-conditioned travel currents was also compared at the level of object, constraints, and logical implication. The inspected results do not imply the sharp gap-to-overlap threshold or the short-window synchronization penalty. Classical gamma calculus is acknowledged rather than presented as novel. **Risk:** an older, differently named queueing or coverage-interval result not indexed by the searches may establish an equivalent statement; historical priority is provisional.

## Value — PASS
Temporary habitat availability and arrival delay are biologically motivated by the cited studies. The result distinguishes a delayed-reception design that has **no simultaneous active period** from one requiring overlap, with one exact nondimensional cutoff rather than a numerical or heuristic boundary. It also proves that synchronous short windows can lose an arbitrarily large multiplicative factor relative to optimal scheduling. The first-versus-second transport-stage contrast isolates when this phenomenon becomes possible and supplies an exact benchmark for mechanistic model refinement.

## Closest literature and scientific limitations
- Moisset de Espanés and Ramos-Jiliberto (2024), https://doi.org/10.1038/s41598-024-56632-y: stochastic dispersal with asynchronous sites, no delayed in-transit population in the model used.
- Hockaday et al. (2024), https://doi.org/10.1371/journal.pone.0306578: controlled wetland hydroperiods and community responses; no arrival-window optimizer.
- Karnatak and Wollrab (2020), https://doi.org/10.1038/s41598-020-79162-9: probabilistic network coupling, not a two-stage travel-time receiving window.

Limitations include prescribed independent equal-rate transport stages, uniform source departures, equal fixed habitat durations, unconstrained destination opening, immediate establishment, and omission of environmental feedback, mortality and ecological interactions. The probability optimized is a single-propagule event; it must not be read as a population persistence prediction.

Self-review: passed. Independent audit: not yet performed.
