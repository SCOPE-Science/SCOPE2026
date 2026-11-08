# Scientific review

## Correctness — PASS

The update of every peripheral edge follows from its degree-two neighborhood: mixed edges become uniformly equal to the *initial* hub bit in the first synchronous step, and uniform edges never change. At the second step the hub compares the fixed edge population, so all states are fixed by then. With initial hub zero and type counts \((u,m,d)\), the initial hub flip condition is \(2u+m>k\), the second flip condition is \(2u<k<2u+m\), and lasting hub reversal occurs exactly when \(2u>k\) or \(2u=k,m\ge1\). This gives the stated binomial-tail expression, first-entry population, and consensus count, with separate handling of even ties and \(k=1,2\). The displayed asymptotic constants follow from Stirling and consecutive binomial tail ratios; they do not rely on finite experiments. Distinct explicit-adjacency and categorical counting implementations produced the two attached verification outputs. Their finite ranges are identified rather than mistaken for an infinite proof.

## Originality — PASS, qualified

The 2012 Mossel–Neeman–Tamuz information-aggregation paper contains an influential small-social-type construction, but its Section 3.1 uses a different bipartite-and-cliques network with self-loops and proves an aggregation obstruction, not this labelled friendship-graph two-step census. The 2014 Benjamini–Chan–O'Donnell–Tamuz–Tan paper states the finite-graph period-two theorem and studies infinite unimodular graphs and random graphs, without a friendship-graph entry-time/reversal distribution. Closest accessible prior claims about friendship graphs use three-state excitable or asynchronous minority dynamics, synchronous minority dynamics or integer diffusion; another uses larger clique windmills \(K_1\vee(kK_3)\). None logically implies the explicit strict-majority \(K_1\vee(kK_2)\) statement. A targeted database and literature search found no identical or broader covering result. That absence is not a universal priority proof: potential equivalent formulations in uncatalogued literature remain a residual risk.

## Value — PASS

The friendship graph is a canonical triangle windmill with a distinguished high-degree mediator. The exact discrepancy between a limiting \(1/2\) mass of double hub reversals and exponentially rare *lasting* reversals quantifies a non-obvious distinction between transient majority response and final influence. The exact two-round first-entry census and consensus fraction provide natural dynamical invariants for the full infinite family, including sharp parity-dependent decay constants. They are not just a renamed generic period-at-most-two theorem or an arbitrary finite-table entry.

## Boundaries and closest literature

The formulas require synchronous binary open-neighbor strict majority and retaining current opinions on ties. The result is not a characterization of majority dynamics on arbitrary windmills, asynchronous models or biased initial conditions. The two cited full texts were examined in their directly relevant theorem, example and setup sections, with document-level term checks; inaccessible or unindexed possible earlier treatments cannot be ruled out solely by negative searches. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
