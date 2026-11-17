# Scientific review

## Correctness — PASS

The claim is a finite census over nineteen explicit twelve-vertex graphs and every one of the 4,096 labelled binary configurations on each. Two independently implemented algorithms give identical exact rows: one follows each trajectory using neighbor counts and incumbent ties, while the other constructs the graph from an LCF encoding and peels the complete Boolean-majority functional graph. The local tie/self-substitution lemma is verified algebraically in RESULT.md. All reachable cycles have lengths one or two; all entry times and unanimous basin set differences are computed exactly. The full scripts and exact outputs permit reproduction without any external dependency. Risk: these are finite exhaustive certificates, not a claim about larger graphs; any arithmetic error shared by both scripts would be a residual risk, reduced by their different graph encodings and dynamic algorithms.

## Originality — PASS (best available evidence)

The 2014 majority-dynamics preprint of Benjamini et al. studies general and random networks and establishes no Frucht-specific one-edge basin response. The 2015 voting-time preprint of Kaaser et al. gives general bounds, not the exact labelled Frucht census. A related indexed mathematical finding about Frucht graph edge deletions concerns matching-complex homotopy, not majority dynamics. Another about an edge defect in complete bipartite graphs concerns a different graph family. Published descriptions of the Frucht graph provide its structure but no majority basins. Direct searches for the graph, update, parameters, and candidate cardinalities found no equivalent statement. Residual risk: not all historical or unindexed writing is accessible, and absence of a database match is not proof of novelty.

## Mathematical value — PASS

The Frucht graph is a canonical cubic network with no spatial automorphism allowing edge classes to be merged. Instead of an unmotivated one-edge example, the classification covers every one of its eighteen edge removals, including the full gain/loss decomposition of the consensus basin. Each deletion both creates and destroys successful initial conditions, yet the net sign varies, showing nonlocal dependence not dictated simply by the deleted edge's triangle membership. The sharp, complete relaxation cutoff accompanies the basin data and permits exact comparisons with graph-majority sensitivity models. It is a natural finite dynamical invariant with no asserted extension to arbitrary graphs.

## Source/uncertainty limits

Primary sources actually inspected include arXiv:1405.2486 (definitions, theorem statements, consensus and regular-graph sections) and arXiv:1508.03519 (definitions, voting-time theorem, introduction and relevant result statements). Graph identity checked against the Frucht description in MathWorld. Full scientific result documents for the closest indexed one-edge majority defect theorem on complete bipartite graphs and for the Frucht matching-complex edge-deletion census were also retrieved and inspected: neither implies this different labelled majority-basin census. Unindexed historical priority remains open.

Self-review: passed. Independent audit: not yet performed.
