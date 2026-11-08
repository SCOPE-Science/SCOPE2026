# Scientific review

## Correctness — PASS

The model, injection convention, positivity conditions and expectation normalization are explicit in RESULT.md. For each right label, vacancy restricts every independently sampled row to a uniformly chosen subset of one fewer label; since every right motif vertex is incident, none can map to the vacant label. Comparing the exact falling-factorial expectation sums gives a multiplier independent of the actual row sizes. Summing indicator covariances proves the identity. Strict concavity of \(1-\prod(1-t_jx)\) proves the exhaustive sign trichotomy, and direct substitution gives the integer square threshold. The extracted standalone exact checker verifies seven exhaustive finite parameter cases and 638 additional double-star identities. Finite evidence is not used to justify the all-order statements.

## Originality — PASS, qualified

The most closely related primary model is Blackburn–Gerke (arXiv:0805.2814v1, 2008), which establishes connectivity thresholds of projected random intersection graphs, not dependence between vacant attributes and underlying bipartite incidence-motif embeddings. The accessible Bloznelis–Jaworski–Kurauskas (arXiv:1209.4675v1, 2012) concerns assortativity and clustering in the projected graph. Karoński–Scheinerman–Singer-Cohen (1999) studies induced projected-graph motifs, but only abstract-level material could be inspected; implicit coverage remains possible and is not claimed absent. A previous exact isolation–motif covariance in \(G(n,m)\) does not imply this formula: global fixed-edge conditioning differs from independent row sums, its motif count is induced and undirected, and its transition parameter is the number of edges rather than the right-attribute universe. No direct equivalent or dominating result was identified in the performed comparisons; this is not a definitive historical uniqueness assertion.

## Value — PASS

The all-finite-size covariance law identifies a natural statistical relation between unused attributes and motif occurrences in random incidence structures, separates the dependence on motif shape from its left degree profile, and exposes a sharp transition controlled solely by the attribute universe size. The entire heterogeneous-row family collapses to one rational expression, while the two-star-overlap family exhibits a transparent nontrivial square threshold \(n=d^2\). This is a structural all-parameter result, not an arbitrary finite example or a recalculation of a known table.

## Remaining risks and scope

Historical implicit coverage in the inaccessible full 1999 article or other older incidence-pattern literature has not been excluded. No result is claimed for induced projected-graph motifs, for fixed-total-edge sampling, or with right-isolated motif roles. The computational replay tests finitely many parameter sets but the proof is algebraic for every admissible model.

Self-review: passed. Independent audit: not yet performed.
