# Independent mathematical audit

## correctness

PASS

The graph is labelled C_n^2 for n>=7, with degree-3 endpoints only at the deleted bond and degree-4 elsewhere; ties on degree four retain the bit. Encode temporal pair (x_i,y_i) by four symbols, and impose both majority equations locally on five-symbol windows. Trace(L1 R1 A^(n-2)) for d=1 or trace(L2 A R2 A^(n-3)) for d=2, with A a 256-state de Bruijn transition, counts every labelled F^2-fixed configuration once; restricting to diagonal pairs gives 16-state fixed configurations, whose subtraction equals twice the number of unordered primitive two-cycles. Since the 256- and 16-state power-traces satisfy degree-at-most-256 and 16 Cayley–Hamilton recurrences, their difference obeys product recurrence of order <=272. The shifted 12-periodicity difference obeys the same order. The inspected source program verifies 272 consecutive zeros for n=7..278, thereby rigorously extending the period 12 formula to ALL n>=7, with 12 initial values. A separately constructed exact sparse 256/16-state transfer implementation (not just saved logs) replicated BOTH defect types for EVERY n=7..290 including 272 zero differences, and independent direct labelled-state enumeration n=7..14 matches. n=7 distance-two witness 0100110 <-> 1011001 checks the new odd-residue orbit.

## originality

PASS

PASS best-of-knowledge: the closely related uniform radius-two majority cellular automaton is not the defective graph: at two endpoints, vertex degree drops from four to three and the tie rule changes; the compared intact-ring classification uses a uniform closed 5-cell majority neighborhood. General symmetric-threshold eventual period<=2 results do not supply primitive orbit counts. The two missing-bond cases have different formulas, and neither is a corollary of the intact-ring periodic configurations or results on chorded ordinary cycles; Resultary record searches found no older exact deleted-bond classification. Risk of other uncatalogued transfer enumerations remains.

## value

PASS

PASS: an exact all-size, bounded and 12-periodic primitive-two-cycle census for a natural local defect in the radius-two cycle is a meaningful classification of how weak symmetry breaking changes recurrent dynamics. Distinguishing bond length one from two and the odd n≡3 mod4 onset is a structural counterexample to naive uniform-ring universality, not an arbitrary small-instance table; the proof supplies an exhaustive finite certificate extended to all n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
