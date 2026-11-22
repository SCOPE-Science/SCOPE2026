# Review of the graph-indexed co-clustering theorem

## Correctness (PASS)
Pitman's two-parameter EPPF supplies the exact two-, three-, and four-label probabilities. The incident-versus-disjoint two-edge gap is strictly positive throughout the stated open parameter domain, giving necessity of the three graph families; vertex relabeling supplies sufficiency. For triangles, an exchangeable binary extension cannot have between two and \(N-1\) ones because its random triple would have a forbidden two-one pattern. Consequently the complete count distribution is forced onto \(\{0,1,N\}\), giving the explicit sharp length ceiling, constructive sufficiency and uniqueness. Every boundary case (\(n=3\), one-edge graphs, \(\alpha=0\), admissible negative \(\theta\), integer-valued ceiling) is included. A supplementary exact finite program passed 2,063 assertions; the mathematical argument, not the computations, covers the continuous parameter domain and arbitrary graph order.

## Originality (PASS, priority qualified)
The necessary EPPF is classical (Pitman 1995); the parameter \(\alpha=0\) construction is classical (Gnedin–Pitman 2006); general finite-exchangeability criteria are classical (Konstantopoulos–Yuan 2015). The graph lemma that pairwise-intersecting edges form a star or triangle is not being claimed as new. The inspected primary text and broader searches did not locate the *combined specific graph-edge indicator* classification nor the exact two-parameter sharp triangle ceiling. General finite-extension criteria may specialize to this case and no search proves historical uniqueness. The closest accessible earlier local result addresses the different **uniform Bell set-partition** model, whose graph-indicator exchangeability shapes and extension ceilings are not those of the Ewens–Pitman family. Historical priority is qualified, not certified.

## Value (PASS)
This is a natural complete classification for how vertex exchangeability transfers—or fails to transfer—to edge-coordinate exchangeability, distinguishing infinitely extendible star and matching observations from a three-observation triangle which cannot be extended past an exact finite parameter-controlled horizon. The ceiling is not merely a numeric finite search; it is a universal answer over all graph sizes and a two-dimensional parameter family, with a unique explicit witness. This informs the limits of latent Bernoulli-mixture approximations for co-clustering observations.

## Limits
The evidence does not assert an independent mathematical audit or exhaustive historical priority. The code is a finite test harness, and historical comparisons may miss an equivalent specialization in the broad exchangeability/partition literature.

Self-review: passed. Independent audit: not yet performed.
