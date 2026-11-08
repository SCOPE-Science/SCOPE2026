# Scientific review: exact majority basins on balanced tripartite graphs

## Correctness — PASS

The proof reduces every vertex-level synchronous update to a three-coordinate count map while explicitly preserving individual opinions on ties. Exhaustive cases according to the number of part counts equal to the shifted total \(T=S-n\) show a stationary configuration or an exact primitive two-cycle by time two. The strict-middle criterion is necessary and sufficient. The basin census weights all labelled states with binomial coefficients, checks the three frozen-part choices do not overlap, and separates the already-periodic states and the balanced fixed states. The central-limit argument uses the conditional hypergeometric law and a Gaussian cone with null boundary. Both verification programs were replayed and agree with the formulas. Limits: finite exhaustive checks through five vertices per part, quotient checks through 30; the all-size theorem uses proof, not those finite bounds.

## Originality — PASS, qualified

The finite undirected symmetric threshold period-two theorem is classical, so the universal period bound alone is not a new contribution. The 2014 majority paper's scope concerns infinite unimodular and random graphs and does not supply the exact three-part eventual basin. The claim differs from counts of initially recurrent/periodic states: the exact basin is polynomially likely while the initially periodic set is exponentially rare. Searching for the exact strict-middle criterion, complete tripartite majority basins, alternative count-map formulations, and stronger multipartite statements produced no claim implying the basin formula together with its asymptotic constant. Generalized threshold-function full text from 1980 was not inspected, leaving a historical-priority risk; the available abstract only establishes a general finite period bound. Search absence is not a novelty proof.

## Mathematical value — PASS

The result classifies the fate of every initial configuration in an infinite graph family, and quantifies the difference between the number of periodic configurations and the size of their attraction basins. The explicit square-root probability and its Gaussian angular constant supply a meaningful asymptotic invariant not determined by the classical period-two theorem. It is not merely a computation of a few small cases.

## Limits and closest literature

The model assumes equal-size tripartition, synchronous open-neighborhood majority and tie retention. A general 1980 threshold-period theorem and a 2014 general majority dynamics study are closest. No claim of absolute historical priority or independent certification is made.

Self-review: passed. Independent audit: not yet performed.
