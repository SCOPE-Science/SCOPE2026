# Scientific review

## Correctness

PASS. The binary Rule-57 truth table makes an unchanged bit during a two-sweep return force both neighboring bits unchanged. On a connected ring, this would force a prohibited fixed point; hence all bits toggle. Checking the precise old/new neighbor order at each interior and boundary site gives a four-step spatial recurrence together with two boundary equalities. Their solutions exist only for ring lengths congruent to two modulo four and number exactly four. The proof covers every integer length at least three. Independent exhaustive and symbolic programs support, but do not replace, the proof.

## Originality

PASS, with an unindexed-literature residual risk. The closest inspected original paper, Vielhaber (2012), describes Rule 57 under varying temporal schedules, not the fixed-order temporal two-cycle census. Donoso-Leiva et al. (2025, sequential convergence) explicitly address absence of fixed points, but do not derive the nontrivial two-cycle classification. The schedule-sensitivity study of de Oliveira et al. (2020) addresses how updates differ rather than period-two states. A more recent 2025 study of maximum cycle periods was available at abstract level only. Searches for Rule-57 two-cycles, complements and ring-size congruences did not expose equivalent or stronger coverage; this is evidence of noncoverage among inspected materials, not absolute priority proof.

## Mathematical value

PASS. Rule 57 is a canonical center-permutive nonlinear elementary automaton with highly expressive schedule-dependent permutations. The theorem reveals a rigid and surprising arithmetic obstruction in its smallest possible nontrivial recurrent period: despite every state being recurrent under the fixed scan, exactly four states have period two when the circumference is two modulo four, and none otherwise. The sitewise unchanged-or-everywhere-changed dichotomy is a structural mechanism, not a numerical list. The claim is a natural complete classification for the first nontrivial temporal period, without asserting a wider cycle-spectrum result.

## Risks and limits

The classification concerns one fixed site order and temporal periods at most two. Unindexed priority or a stronger all-period theorem elsewhere could change the novelty assessment. External independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
