# Scientific review: two sharp degree-rule failure thresholds

## Correctness

PASS. The claim concerns only finite, simple, connected, undirected equal-weight graphs of orders two through six. The exhaustive checker iterates all labelled edge masks, determines connectivity exactly, forms every vertex-deleted adjacency matrix, computes its characteristic polynomial with exact integers and compares Perron roots by certified rational isolation or shared polynomial factors. Canonical labeling uses all vertex permutations. The 150 five-node tie failures and 540 six-node complete failures are exhaustively partitioned into three and two isomorphism classes, respectively; explicit witnesses are additionally checked. The two six-node residual polynomial factorizations agree with direct symbolic calculations. The checker is a finite proof of this finite claim, not a claim about infinite networks.

## Originality

PASS relative to accessible evidence, with recorded historical-priority uncertainty. The source of the metapopulation-capacity objective is Hanski–Ovaskainen (2000), the general patch-removal eigenvalue framework is Ovaskainen (2003), and the closest accessible whole-document network intervention treatment is Saha et al. (2015), whose Sections 6–7 and appendices address spectral-node removal and poor general degree heuristics rather than the exact smallest failure orders and complete 5/6-vertex classes. Semantic searches for smallest spectral node-deletion failures, habitat capacity and degree tie-breaking, and closely related archival findings found no explicit same classification. This is not a claim that earlier work lacks all counterexamples or general algorithms. The full 2000 and 2003 papers were not accessible, so there remains a plausible priority risk.

## Value

PASS. The minimal-order boundaries clarify what a degree-only habitat protection proxy can and cannot guarantee even in small landscapes: tie-breaking first matters at five patches, and the best possible maximum-degree tie-breaking first fails at six. The complete exceptional structures and exact gaps form usable deterministic benchmarks for conservation-network intervention algorithms. It does not infer actual extinction probabilities or a universal real-world conservation strategy.

## Verification and remaining limits

The executable `checker.py` was replayed against `COUNTS.json` using exact symbolic calculations. Model simplifications (uniform symmetric exchange and zero self-exchange), the finite-order restriction and the lack of independent historical review are explicit. The 2000 and 2003 relevant manuscripts were inaccessible beyond public material, but the nearest 2015 whole-paper result was read.

Self-review: passed. Independent audit: not yet performed.
