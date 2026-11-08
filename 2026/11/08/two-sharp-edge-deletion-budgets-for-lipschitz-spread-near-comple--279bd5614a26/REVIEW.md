# Review of the dense-graph deletion theorem

## Correctness — PASS

The new theorem has two independent envelopes. Each admissible graph has diameter at most two; strict convexity and the connected tight-edge argument reduce every variance maximizer to integer values. The three-level formula is exact because opposite levels correspond exactly to a biclique in the missing-edge graph. The total-edge envelope follows from \(a+b\le ab+1\) within the specified budget and a monotone quadratic; its equality conditions force a star. The maximum-lost-degree envelope follows from \(a,b\le r\), with equality forcing a complete biclique component. The root and floor convention is checked at the transition boundary. An embedded exact-integer checker supports, but does not replace, these arguments.

## Originality — PASS (qualified)

Compared by mathematical implication, the source paper of Alon, Boppana, and Spencer, Theorem 2.1, supplies integrality but neither extremal deletion envelope. The 2009 Addario-Berry–Janson–McDiarmid paper analyzes random graph spread and asymptotic high-degree behavior, not the exact adversarial maximum for a prescribed deletion budget. Yancey's 2017 discussion of variance-optimal functions does not supply the two extremal formulas. Published mathematical-record searches for the two budgets found related graph and polytope calculations but no covering statement. A previously recorded complete-multipartite spread formula covers small special cases such as a single missing edge, not general deleted stars and bicliques. Search incompleteness and potential equivalent terminology remain genuine risks; this is not a proof of absolute priority.

## Value — PASS

The question of how much edge loss preserves the smallest possible graph Lipschitz-to-\(L^2\) norm is natural for robust metric constraints. The result gives two *sharp*, different resource profiles: total missing edges force a star extremizer and first increase near \(n/2-\sqrt{2n}\); maximum lost degree forces a complete balanced biclique and first increase near \(n/8\). It handles all dense graphs with the indicated budgets and classifies strict optimizers, rather than computing another isolated small graph invariant. No downstream theorem is needed for the structural cutoff to be meaningful.

## Closest literature and limitations

References and their inspected portions are in `RESULT.md` and `AUDIT.json`. The 1998 integer-extremizer principle and complete-graph baseline are inputs, not discoveries. The graph class must be connected, simple, unweighted, and uniformly measured; total-edge budgets above \(\lfloor(n-2)/2\rfloor\) are outside the stated formula. No independent audit has been performed, and equivalent unindexed results cannot be excluded.

Self-review: passed. Independent audit: not yet performed.
