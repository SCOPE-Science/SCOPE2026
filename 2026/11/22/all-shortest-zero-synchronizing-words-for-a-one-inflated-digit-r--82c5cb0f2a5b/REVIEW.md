# Scientific review: optimal zero-synchronizing words for a radix family

## Correctness — PASS
The theorem uses the exact interval characterization of simultaneous zero carry, an explicit forbidden residue class for the lower bound, and a signed-digit decomposition of all represented integers at the candidate length. The disjoint successful blocks are characterized by interior base-\(b\) digits; non-interior blocks cannot contain a run long enough to reset. This proves both shortest length and a complete optimal-word count for every integer \(b\ge3\), \(k\ge2\). The standalone `verify.py` passes 32 direct representation-set and independent subset-automaton BFS checks. Computation is corroborating, not an infinite proof. Boundary cases and the last partial digit block are handled explicitly.

## Originality — PASS, qualified
Zhou's 2026 preprint gives a qualitative criterion and asks for quantitative shortest-length bounds. A directly relevant published ternary predecessor already proves \(2k-1\) in the ternary subfamily and constructs at least \((3^{k-1}+1)/2\) minimum words; its explicit limitations decline to count them exhaustively. The new exact *classification of every minimum word* and extension to every radix \(b\ge3\), including the exact closed count, are not implied by that predecessor. Public claim-search records, the precursor's full result, and the motivating paper's relevant sections were compared. A possible unindexed full classification remains a priority risk. The ternary minimal-length formula alone is not claimed as novel.

## Mathematical value — PASS
This is a natural exact quantitative answer to a recent finite-state numeration question. It identifies all extremal words, not just one witness or an upper bound; it settles the known ternary optimal-word multiplicity lower bound with equality and exhibits structured new bands of shortest words for higher bases. The result supplies a reusable signed-digit interval method and sharp dependence on base and exponent.

## Scope and limitations
The theorem covers the particular complete-residue scalar digit family and zero-target carry automata only. No general all-digit-system bound, universal maximal reset-length theorem, or independent audit is asserted. Finite checks do not certify the proof.

Self-review: passed. Independent audit: not yet performed.
