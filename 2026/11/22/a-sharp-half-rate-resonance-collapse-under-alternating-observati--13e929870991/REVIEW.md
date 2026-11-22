# Scientific review

## Correctness (C): PASS

The claim concerns a deterministic constant-input threshold/reset system on an exact two-phase periodic time set. The existing forward-projection theorem supplies the event recursion, and the proof explicitly computes both phase arrows with the inclusive threshold convention. Case analysis covers the boundary \(r=0\), the equalities \(r=a\) and \(r=b\), and all remaining positive parameters. The exact rational checker independently exercises the computed transition table, but correctness rests on the analytic proof. No finite enumeration is mistaken for an all-real proof.

## Originality (O): PASS within inspected evidence

The 2026 primary source proves the general forward-projection recurrence and the uniform-grid rate, but identifies periodic-time-scale spike arithmetic as future work. The new contribution is the two-gap phase diagram and the exact, discontinuous half-rate collapse under arbitrarily small alternating jitter at a resonance. Published literature on regular-grid exact numerical propagation, periodic forcing, and generic spike-train quantization has overlapping motivation but does not imply the exact event-opportunity result in the inspected material. The closest available historical comparisons include Rotter–Diesmann (1999) and Pakdaman (2001); only the latter's abstract was accessible for the full-claim comparison, so unindexed or inaccessible priority remains a risk. published-finding corpus and accessible prior claims were searched for alternate wording, resets, period-two sampling, and equivalent rate laws.

## Mathematical value (V): PASS

A discontinuous factor-of-two loss in physical spike frequency despite vanishing timing jitter, identical mean sampling density, and unchanged membrane parameters is a structurally meaningful sampling-resonance effect. The theorem also characterizes every positive two-gap clock and every possible travel time, including the exact robust high-rate interval. It supplies a sharp design boundary rather than a single numerical counterexample. Its intentionally minimal periodic clock does not claim to resolve the general multi-opportunity problem.

## Literature and limitations

Primary source: https://arxiv.org/html/2611.17219v1 (Sections 5–8; first public 2026-11-12). Related older exact digital integration: https://brainworks.biologie.uni-freiburg.de/1999/journal%20papers/RotterDiesmann99.pdf. Different periodic-drive framework: https://doi.org/10.1103/PhysRevE.63.041907 (abstract inspected; full text not available). Related spike-train quantization: https://arxiv.org/abs/2402.07954 (abstract inspected). The conclusion applies only to on-time-scale threshold opportunities, constant input, and deterministic alternating clocks. Independent priority and mathematical validation remain unperformed.

Self-review: passed. Independent audit: not yet performed.
