# Review of complete and maximal EF1 schedules on biclique conflict graphs

## Correctness — PASS

In an incomplete maximal schedule every agent must already hold a chore opposite any omitted chore. This forces the side-complement classification and rules out a second kind of omission. Unit-cost chore EF1 reduces to a load-spread inequality. Counting unique recipient subsets and their factorial multinomial assignments gives the exact census; constructing a full equitable schedule when neither side reaches agent count proves unconditional existence. The sharp family uses divisibility obstruction to full schedules and a balanced incomplete schedule of the larger side. The extracted standalone verifier checks all 726261 assignments across 63 complete finite parameter cells and agrees on both counts and optimum throughput; infinite cases are justified by proof, not enumeration.

## Originality — PASS, with limits

Equbal et al., *Fair Interval Scheduling of Indivisible Chores* (arXiv:2402.04353, public 2024-02-06) establish the conflict-graph/maximal EF1 framework, while Igarashi et al., *Dividing Conflicting Items Fairly* (arXiv:2506.14149), and the later unified work *Fair Allocation under Conflict Constraints* (arXiv:2605.09930), study general existence/algorithms and negative boundaries. Primary full-text material including the tree partial-equitable-coloring appendix was inspected. Yan and Wang's complete multipartite equitable-coloring theory (arXiv:1207.3578) already handles the *complete-colorability subproblem* and is credited. The current distinguishing statement concerns the disjoint structure and exact number of all **incomplete inclusion-maximal EF1** schedules and the sharp throughput loss. No implication of this joint statement from these sources or from the checked mathematical-record matches was found. A possible equivalent outside indexed/inspected work remains a material priority risk; failure to find one is not a uniqueness proof.

## Value — PASS

Inclusion maximality is the economically relevant prohibition against arbitrarily leaving an easy-to-insert chore undone, but does not guarantee that a schedule completes most of the chores. An exact census of all maximal fair schedules, precise conditions for achieving a full schedule, and a sharp nearly-one-half throughput failure on balanced bicliques with four agents are substantively motivated answers within this model. The result covers infinite families and identifies the particular conflict geometry responsible for large loss.

## Scientific limitations

Only identical unit chore costs, two nonempty complete bipartite item-conflict classes and inclusion-maximal allocations are covered. No result is asserted about general conflict graphs, heterogeneity or Pareto optimality. Reproducible finite computations serve as checks; the written general argument supplies the proof. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
