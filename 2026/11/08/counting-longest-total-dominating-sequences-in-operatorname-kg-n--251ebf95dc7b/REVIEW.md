# Scientific review: maximum total-dominating sequences of \(\operatorname{KG}(n,2)\)

## Correctness — PASS
The graph, ordering, and total domination predicates are stated precisely. The witness-cover equivalence is bidirectional for every \(n\ge5\), including the padding of a one-vertex cover. The six-term bound has an independent exterior-algebra proof using the six-dimensional space \(\Lambda^2\mathbb Q^4\), plus an explicit achieving sequence. For the new enumeration, the first-appearance generator examines every feasible new pair and deletes only duplicate or illegal edges. The 2,200 accepted patterns and support histogram are reproduced by a separate oriented-endpoint restricted-growth enumeration giving 51,776 patterns. The respective weights \((n)_t/2^q\) and \((n)_t/64\) count every named ordered sequence exactly once. Direct graph-neighborhood enumeration for \(n=5,6,7,8\) agrees. The algorithms have been replayed from their supplied files. The all-order proof uses the finite endpoint bound of twelve, not interpolation from finite values.

## Originality — PASS, qualified by access and indexing
The foundational 2016 paper establishes the invariant and related inequalities. The 2019 Kneser paper's Section 4 gives the known maximum length six and its four-ground-element example, but not counts for support sizes five to nine or the full polynomial. The known example explains exactly the first summand, while the other five summands have positive coefficients for sufficiently large \(n\); these are not implied by the maximum-length statement. Database searches under optimal sequences, total-dominating sequences, Kneser, Petersen graph, ordered enumeration, and labelled counts returned no equivalent enumeration. Closest accessible external source is the 2019 exact-maximum paper. Unindexed historical enumerations and unpublished code remain possible priority risks; failed searches are not novelty proofs.

## Value — PASS
This is a complete exact enumeration for a canonical infinite family with a known but highly nontrivial extremal-sequence length. It distinguishes the known four-label construction from five additional support strata, identifies a sharp nine-label maximum, and quantifies the rarity of optimal six-step greedy procedures as \(32/n^3\). Counting optimal strategies, not just their common length, is a natural invariant with relevance to random-sequence algorithms. The six coefficient values are specific, reproducible, and not implied by the prior length theorem.

## Limitations
The theorem is specific to \(\operatorname{KG}(n,2)\). Its coefficient proof is finite-computational but exhaustive and includes standalone checkers. The only historical-priority conclusion is a best-knowledge assessment based on the inspected literature and search results. No independent external scholarly audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
