# Scientific review

## Correctness (C): PASS

The theorem quantifies over all nonempty ternary words. Run contraction preserves all shortest covers because the latter have no equal consecutive letters; the original s-cover literature supplies the bound \(\gamma(3)=8\). Every remaining candidate is in a 255-word finite pool. The described two-variable candidate membership automaton represents both a greedily matched candidate prefix and the largest suffix pending for a host position. This transition is justified by the nesting of suffix obligations. Exhaustive reachability over normalized run-free hosts closes after 84,725 states, checking both outgoing edges of every state and comparing the full set of minimum-length accepting candidates with an independent regex recognizer. It establishes the all-length result rather than extrapolating a finite host-length census. A separate positional-mask implementation checks 2,047 normalized words through length twelve, and additionally checks greedy earliest/latest embeddings; this bounded test is corroboration, not the all-length argument. The run-expansion generating function follows from a positive-run substitution and the denominator's dominant pole. Sources, proof code and outputs are in the package.

## Originality (O): PASS against inspected literature

The most directly relevant earlier public claim, *First ambiguity of shortest ternary subsequence covers* (dated 2026-10-18), completely classifies the first exceptions at length eleven but expressly stops there. The present theorem recovers that classification as its first case yet settles the entire infinite ternary ambiguity language, exact maximum multiplicity two, and generating function. The original 2022 and revised 2025 Charalampopoulos et al. papers supply the general algorithm, transitivity and primitive bound but not the fixed-ternary global classification; larger-alphabet multiplicity examples are not contrary evidence. Searches compared shortest covers, equivalent run contraction forms, shortest-cover multiplicity, and published finite tables as substantive implications rather than title matches. The detailed four named comparisons and material-read scope are recorded in AUDIT.json. An undiscovered unindexed all-length equivalent remains a historical priority risk; this is not an independent priority certification.

## Value (V): PASS

The previous exact ternary problem was a finite first-ambiguity boundary. The natural question whether multiplicity can grow at fixed alphabet size, and which hosts attain it, is answered at every length, including host words with repeated runs. The complete regular normal form plus a rational enumerator and asymptotic density are mathematically informative and usable for testing symbolic algorithms. The result is neither a mere finite-table recomputation nor an arbitrary isolated parameter increment.

## Limits

The proof is computer-assisted and depends on the established \(\gamma(3)=8\) bound. The direct positional-check program covers only its stated finite range; the exact all-length part is the complete reachable-state graph. Independent external review has not occurred. The global result is for overlapping scattered occurrences and alphabet size at most three.

Self-review: passed. Independent audit: not yet performed.
