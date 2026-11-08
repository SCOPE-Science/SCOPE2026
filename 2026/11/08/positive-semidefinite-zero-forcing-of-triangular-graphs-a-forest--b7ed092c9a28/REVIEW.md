# Scientific review: PSD zero forcing of triangular graphs

## Correctness — PASS
For every \(n\ge3\), the white-cycle invariant excludes all cyclic white-edge graphs. A spanning tree fails because each blue edge has at least two white neighbors in the sole white component. For any disconnected forest, a blue cross-component edge from a white leaf to another component forces the unique leaf edge, and induction empties the forest. The equivalence and all boundary cases are complete. A labeled forest on \(n\) vertices with \(k\) edges has \(n-k\) components, making the partition and exponential-formula counts exact. Two genuinely different finite implementations check the PSD rule and Cayley enumeration. Their scripts and outputs are included, and their finite scope is expressly distinguished from the proof for all \(n\).

## Originality — PASS, conditional on historical indexing
Direct statement/implication comparisons were made against full text. Peters (2012, Proposition 3.16) and Fallat–Meagher–Soltani–Yang (2015, Lemma 8.3) prove the scalar minimum \(\binom n2-n+2\), which is prior art. Barioli et al. (2010) introduce the PSD rule generally, not the complete Johnson-graph forcing-set family. Work on **ordinary** triangular-graph zero forcing has a forest criterion requiring an isolated ground label, hence covers only a proper subset of the PSD sets: two disjoint white edges for \(n=4\) distinguish them. Earlier ordinary zero forcing polynomials and PSD results for multipartite rather than triangular graphs do not imply this complete PSD distribution. Neither inspected Johnson-graph section contains a full-set PSD enumerator. Searches in mathematical literature and published mathematical records did not find a matching result; this is evidence of noncoverage in inspected material, not a guarantee of priority. A related thesis and potential unindexed computations were not read in full.

## Value — PASS
The known scalar minimum does not specify which configurations succeed, how many exist at each size, or how the positive and ordinary rules differ despite having equal minima. The new forest criterion removes an algorithmic forcing-process predicate in favor of a natural structural class, yields the full size-generating polynomial for an unbounded graph family, and gives the exact two-component Cayley count for all optimal PSD sets. The nontrivial difference already appears at four ground labels and grows substantially (3, 30, 330 more minimum PSD than ordinary sets for 4, 5, 6 labels).

## Scientific and historical limits
The full theorem rests on the proof, not solely finite enumeration. The complete text of the historically plausible 2013 thesis was not inspected; index incompleteness remains a residual historical-priority risk. No independent expert audit has been performed.

Self-review: passed. Independent audit: not yet performed.
