# Scientific review

## Correctness (C): PASS

The residual graph after each accepted edge is another complete-graph corona on the unmatched core vertices, plus isolated leaves. There are exactly \(k\) remaining pendant and \(\binom{k}{2}\) clique edges, which proves the first-step recurrence without assuming independent choices across stages. The ordinary generating function solves its differential equation with the correct initial condition. Singularity analysis at \(t=1\), with the \(t=-1\) contribution smaller for \(z\) near one, proves the uniform asymptotic moment-generating function, hence the central limit theorem and moment constants. The exact labeled-state checker and independent permutation enumeration passed. Finite numerical checks are corroborating evidence, not an infinite proof.

## Originality (O): PASS (qualified)

Arnosti (2021) introduces the RANDOM-EDGE algorithm and gives stochastic comparisons averaged over random **bipartite** graphs, not a law on fixed non-bipartite clique coronas. Bernstein (2020) proves algorithmic approximation guarantees for random-order streams but supplies neither the displayed distribution nor the logarithmic correction for this graph family. The nearest public mathematical index hit concerning the *same corona graph* deals with general-position polynomial log-concavity, not the random greedy matching process. Multiple keyword and equivalent-formulation searches, including the exact hyperbolic-function form, found no dominating theorem; this is not a proof of absolute priority. The inaccessible full text of the same-graph general-position record is a residual source-access risk, although its summarized invariant is mathematically distinct.

## Value (V): PASS

A graph with a readily visible perfect matching can nevertheless cause the most elementary random-edge greedy algorithm to saturate its one-half guarantee asymptotically. The exact distribution reveals the nontrivial \(\log n\) correction and \(\sqrt{\log n}\) fluctuations, and identifies a connection with weighted odd-cycle permutation generating functions. These are structural probabilistic facts about a natural extremal matching example, not just a restatement of the universal one-half bound.

## Scope and limitations

The claim is for one pendant neighbor per clique vertex and uniformly random edge ordering. It does not imply universality across all dense graphs or certify historical priority. The analytic proof gives the infinite asymptotics; the checker tests only listed finite sizes. No independent review has been performed.

Self-review: passed. Independent audit: not yet performed.
