# Scientific review

## Correctness: PASS

The claim fixes a finite labelled once-subdivided clique and counts minimum **vertex sets**, not matchings. Every minimum set must select exactly \(n-1\) original vertices and \(n-1\) subdivision vertices: otherwise a subdivision vertex between two omitted original vertices has no possible selected matching partner. The remaining matching constraint becomes a bijective edge-to-endpoint assignment. Componentwise edge counts force exactly one rooted tree component and otherwise unicyclic components. The rooted tree has a unique incidence matching; each other component contributes exactly two. Labelled tree enumeration and the labelled cycle-of-rooted-trees construction give the stated generating function. The full proof treats \(n\ge2\), including the smallest boundary cases. The included direct checker compares all candidate selections for \(2\le n\le7\) against the actual domination and induced-matching conditions and exact component-distribution recurrence; recurrences are also checked through \(n=30\). None of the unrestricted claims relies on finite enumeration as a substitute for the proof.

## Originality: PASS (provisional historical priority)

The closest source is Muthukamatchi and Arumugam, *Paired Domination in Subdivision Graphs* (2016), Theorem 2.9. It establishes precisely \(\gamma_{\mathrm{pr}}(S(K_n))=2(n-1)\), which is credited as known here. Its inspected full article does not classify all optimum vertex sets, enumerate them, or quantify how many perfect matchings each induces. Lu and Wu, *Paired Domination in Cubic Bipartite Graphs* (2026), prove sharp bounds using dominating matchings; the graph family here is not cubic, and their introductory and central matching formulations give no such enumeration. Semantic searches for synonymous formulations, subdivisions of cliques, rooted pseudoforests, and related paired-domination polynomials found no covering source. Published paired-domination polynomials for chain graphs and complete multipartite graphs concern graph families that do not include \(S(K_n)\) for \(n\ge3\). The reduction to known labelled tree and unicyclic graph enumeration is acknowledged, so the precise claimed contribution is the new mapping of optimal paired-dominating **sets** and their perfect-matching multiplicities, not a novel formula for arbitrary pseudoforests. Unindexed literature may still contain an equivalent classification.

## Value: PASS

The 2016 work provides only the optimal cardinality, leaving a meaningful graph-enumeration question: how many optimal backup-compatible dominating configurations exist and how redundant are their induced perfect matchings? The result gives a full all-parameter structural bijection, an exact polynomial recording every power-of-two multiplicity class, and a sharp distinction between unique-match minima (exactly \(n^{n-1}\)) and multiple-match minima (which occur first at five original vertices). Rooted forests and unicyclic components provide a natural combinatorial explanation that is not recoverable from the known minimum-cardinality statement alone.

## Literature, limits and risk

The proof is limited to the once-subdivided complete graph and minimum-cardinality paired dominating sets. Exact historical priority remains provisional; hidden or less-indexed work on domination in incidence graphs could cover the enumeration. The published 2016 minimum-cardinality theorem and classical Cayley and unicyclic enumeration are not asserted to be new. The verifier provides extensive finite corroboration, but no independent mathematical audit has been performed.

Self-review: passed. Independent audit: not yet performed.
