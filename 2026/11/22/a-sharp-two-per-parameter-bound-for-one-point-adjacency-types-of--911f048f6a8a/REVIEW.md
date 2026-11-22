# Scientific review

## Correctness: PASS

The proposition is quantified over all finite simple undirected cographs and all nonempty parameter sets. The strengthened inductive potential \(t+(1-e)+(1-f)\) handles both the disjoint-union and join steps and parameter-free child components. The child trace overlaps are exactly the empty trace (for disjoint union) and full trace (for join), respectively, so the rank-zero bound follows without extrapolating from computations. Full binary tree leaf clusters give exactly \(2m\) distinct external traces; counting their required distinct witnesses proves the sharp minimum \(3m\) vertices. All boundaries, particularly \(m=1\), are included. The supplied verifier exhaustively tests 362,227 parameter cases on 6,039 cographs through six vertices, plus the stated constructed and randomized cases. These are checks, not the infinite proof.

## Originality: PASS within inspected evidence

Primary comparisons use theorem implication rather than headline matching. Bonnet et al. give the more general twin-width upper bound \(4m\) at twin-width zero, not this exact \(2m\) estimate. Dreier et al.'s recent general parameter-type theorem provides only polynomial growth, while Berthe et al. study sharp constants for bounded treewidth/pathwidth; neither theorem gives the exact cograph coefficient or the external minimum-order construction. The published-finding corpus database searches for adjacency traces, \(P_4\)-free graphs, cotrees, sharp neighborhood complexity and type counts returned adjacent but distinct records. The most relevant primary paper sections were materially inspected, with the availability and residual-priority limits recorded in the structured audit. A hidden or historically unindexed equivalent may still exist, so priority is not independently certified.

## Value: PASS

Neighborhood complexity measures the number of possible one-point observations over named parameters and is central to finite model theory, graph algorithms and kernelization. Replacing a known general \(4m\) upper bound by a universal **sharp** \(2m\) bound, together with an optimal \(3m\)-vertex external-type witness family, gives an exact natural invariant, not an arbitrary finite census or a parameter substitution. The strengthened induction exposes the mechanism by which join/union operations control realizable types. No downstream algorithmic theorem is claimed.

## Scope and residual risks

Only finite \(P_4\)-free simple graphs, open neighborhoods and nonempty parameter sets are covered. Possible older cograph-specific neighborhood-complexity observations not returned by searches could establish historical priority. Closed neighborhoods, arbitrary first-order ranks and independent audit are not covered.

Self-review: passed. Independent audit: not yet performed.
