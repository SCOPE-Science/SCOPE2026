# Independent mathematical audit

## correctness

PASS

Each ordered pair of total maps on the four labeled states occurs once. The reachable image subset is propagated exactly by the next input; the preceding symbol suffices to enforce no 00 and the initial sentinel imposes no initial restriction. Thus BFS computes the minimum admissible word length or excludes any admissible reset, terminating on at most 31 nonempty-subset/symbol and start states. The frozen exact-length recurrence was also inspected: repeating the entire ordered pair of reachable families before any singleton guarantees no future singleton. A separately written exact integer enumerator was run on all 65,536 pairs; its bins for 1 through 12 and infinity are (2032, 17088, 15456, 4992, 3696, 1056, 984, 312, 288, 72, 96, 24, 19440), agreeing in every bin. Ordinary synchronization occurs in 51,520 pairs, against 46,096 constrained; containment follows since admissible words are unrestricted words. The length-12 set was compared as a set with all 24 simultaneous state conjugates, keeping letters fixed. The representative has unrestricted minimum 6, constrained minimum 12, and its stated witness ends with singleton mask 4. Replay the separate calculation with python3 /workspace/branches/cf582467-178e-4c4f-a23a-967873f529bf/reproduce_no00.py (no limit); the same directory contains reproduction_full.json. The frozen verify.py was inspected without execution; it offers two exact procedures for this classification. This verifies the specified four-state domain, not any larger automata or arbitrary forbidden patterns.

## originality

PASS

Bounded statement-level comparisons support the exact 4-state, ordered-letter, forbidden-double-zero distribution and extremal orbit as distinct. Ordinary power-automaton BFS and the study of synchronization constrained by a regular language are established. The strongest distinct Resultary overlap is a five-state extremal classification for a different, state-avoidance predicate, not an equivalently encoded census of input-factor avoidance.

## value

PASS

Synchronization with a repeated command prohibited is a simple natural regular constraint whose finite effects are not captured by ordinary reset thresholds. This exhaustive benchmark identifies both qualitative loss of synchronization (5,424 ordinarily synchronizing pairs) and a sharp finite slowdown (an extremal representative from 6 to 12), and classifies every extremizer without imposing artificial reachability assumptions. The exact distribution can be used to test language-constrained reset searches; no arbitrary-state generalization is needed for that use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
