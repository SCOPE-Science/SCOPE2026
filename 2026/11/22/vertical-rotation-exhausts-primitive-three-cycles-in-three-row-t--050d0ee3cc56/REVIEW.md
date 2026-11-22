# Scientific review: three-row Toom temporal three-cycles

## Correctness — PASS

The claim is a theorem for every integer horizontal circumference \(n\ge3\), with synchronous deterministic binary north-east-center majority and three distinct vertical rows. The 512 temporal-history states encode all possible triples of three-bit columns; their 262144 directed candidate pairs are evaluated by the original local rule. Closed directed walks, and only closed directed walks, correspond bijectively to states returning after three steps. The exhaustive and replayable graph certificate identifies 14 vertices on cycles: two spatially uniform stationary histories, six nonuniform stationary histories, and six nonuniform histories of the form \((a,Ra,R^2a)\). The other 498 history vertices have no directed return path. The third component yields all least-period-three states and is counted by the trace of a printed six-by-six integer adjacency matrix. Its exact determinant factorization and elementary two- and three-edge closed walks prove the claimed formula and existence for all circumferences. The direct simulator independently checks all states at circumferences three through six, but these finite direct tests alone do not prove the infinite statement. The correctness proof is computer-assisted through a small, exhaustively specified Boolean graph certificate; neither external certification nor a hand-enumerated component list is claimed.

## Originality — PASS, with historical risk

Actual database searches included Toom north-east-center three-row temporal period three, vertical rotation waves, finite strip zeta, and equivalent cellular-automaton period-three configurations. The closest published finite-strip manuscript, *Two coexisting fixed-state phases in the three-row Toom automaton*, explicitly classifies only one-step fixed states; it does not establish primitive three-cycles, their vertical rotation rigidity, or their orbit spectrum. *Exact attraction basins and an emergent Ising law for two-row Toom dynamics* concerns two rows and a distinct propagation mechanism. Jen (1988) establishes a general transfer-matrix framework for temporal cycles, but does not evaluate the present six-state rotating component, derive its exact spectrum, or prove the exhaustive vertical-rotation classification. Makowiec (1997, 1998) concerns stationary patterns and noise, and Gács (2001) concerns deterministic erosion, not this all-circumference nonstationary census. These are statement-level distinctions, not conclusions from title matching. The 1997 ground-state primary article could be read only at abstract level, leaving a genuine historical-priority risk. An unindexed equivalent treatment is possible; originality is not independently certified.

## Value — PASS

The three-row periodic strip is a natural smallest width in which vertical columns have a nontrivial cyclic order-three rotation, in contrast to the previously studied two-row absorbing versus translating dynamics. A complete exact classification of every primitive three-cycle, including a rigidity theorem and the all-length asymptotic orbit count, identifies the first nonstationary temporal-period-three sector of a canonical nonlinear cellular automaton. This is a motivated structural dynamical invariant, not an arbitrary finite ring enumeration or a routine restatement of the previously known one-step fixed-point formula. Its limitation to period three is explicit.

## Closest sources and limitations

- E. Jen, *Cylindrical Cellular Automata* (1988), DOI:10.1007/BF01221109; general method, full primary text reviewed.
- *Two coexisting fixed-state phases in the three-row Toom automaton* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-two-coexisting-fixed-state-phases-in-the-three-row-toom-automato--ba0ec0595c40; complete RESULT manuscript reviewed.
- *Exact attraction basins and an emergent Ising law for two-row Toom dynamics* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-exact-attraction-basins-and-an-emergent-ising-law-for-two-row-to--c044dc7d101f; complete RESULT manuscript reviewed.
- D. Makowiec, *Critical properties of Toom cellular automata* (1998), arXiv:cond-mat/9808247v1; full arXiv text reviewed.
- P. Gács, *A Toom rule that increases the thickness of sets* (2001), arXiv:math-ph/0102009v1; accessible primary text reviewed.
- D. Makowiec, *Ground-state configurations for Toom cellular automata: Experimental hints* (1997), DOI:10.1103/PhysRevE.56.5195; abstract read, full material unavailable. This is the principal residual source-access risk.

Self-review: passed. Independent audit: not yet performed.
