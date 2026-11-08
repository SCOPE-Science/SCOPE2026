# Scientific review

## Correctness (C): PASS
The theorem reduces block Parikh vectors to the continuous piecewise-affine zero-prefix function. Its only slope breakpoints are shifted run boundaries. On each interval every pairwise equality is either an identity or a single explicitly computed integer root, so the count is exact with the stated polynomial-in-order bound. For three blocks, the proof separately disposes of single-letter runs, two finite exceptional short-run hosts, constructive sharp threshold witnesses, and the six exhaustive two-letter-block arrangements. The packaged verifier cross-checks 16,642 direct counts, 2,500 threshold/multiplicity cases and seeded longer tests. Complexity counts arithmetic operations and does not pretend that bit operations cost one.

## Originality (O): PASS, with residual bibliographic risk
Fici–Postic–Silva, arXiv:1810.12275, develops Abelian-antipower existence for infinite sequences, especially paperfolding words; its relevant definitions, theorem statements, proof material and references were inspected. Kociumaka et al., arXiv:1812.08101, counts ordinary antipowers in arbitrary finite words, which is not the same as Parikh-distinct antipowers. Peltomäki–Whiteland, arXiv:2006.06307, concerns cyclic Abelian **power** avoidance (equal Parikh vectors) rather than Abelian **antipowers** (pairwise distinct vectors). Searches also considered synonyms `anti-cube`, `anti-power`, periodic binary hosts, cyclic windows, run-length encoding, and fast phase counting. No inspected source or recovered prior statement implies the simultaneous sharp onset, phase multiplicities, and period-independent census. This is a best-knowledge comparison, not a proof of worldwide uniqueness.

## Mathematical value (V): PASS
The order-three threshold is a complete classification for an infinite two-run periodic family, with a sharp 1/3-period obstruction, two isolated exceptional avoidance profiles and exact phase multiplicities. The general count avoids scanning a period of arbitrary size: at most \(2(q+1)+2\) breakpoints suffice even when the period and block length are enormous. These facts give the precise onset and efficient occurrence statistics of a natural Abelian-antipower invariant, not an arbitrary finite slice.

## Limits
The result counts periodic starting phases; it does not classify distinct antipower factor strings. It does not assert any faster general algorithm or independence from earlier unknown unpublished work. Finite tests support but do not establish the infinite proofs.

Self-review: passed. Independent audit: not yet performed.
