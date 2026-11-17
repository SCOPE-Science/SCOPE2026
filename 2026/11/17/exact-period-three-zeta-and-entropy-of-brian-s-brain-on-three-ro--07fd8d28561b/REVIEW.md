# Scientific review: exact temporal-three Brian's Brain census

## Correctness — PASS

The central claim is an exact formula for \(\#\operatorname{Fix}(F_n^3)\) on labelled \(3\times n\) Moore tori for every \(n\ge3\), with the derived primitive temporal three-cycle count, sharp smallest circumference, and entropy. Local histories are exhaustive: a cell either stays resting for three steps or cycles through all three states. For a middle column, checking exactly two firing neighbors at each candidate birth and excluding exactly two neighbors in all three times for each permanently resting cell is necessary and sufficient. Closed walks in the specified pair-of-columns graph therefore correspond bijectively to spatially labelled time-three-fixed configurations. Rebuilding all \(4096\) vertices produces \(12286\) edges, with exactly one cyclic strongly connected component (\(184\) vertices and \(559\) edges); symbolic exact-arithmetic characteristic computation gives the claimed factorization and the zeta. The component is primitive; a supplied strictly positive integer certificate proves the two Perron bounds by rational inequalities. Direct-state evolution, independently coded in C++, exhaustively agrees for \(n=3,4,5\). Risk: the exact polynomial factor and component enumeration are computer-assisted finite claims; all reconstructing code and the integer certificate are included, rather than relying on recorded logs.

## Originality — PASS (qualified)

The fully inspected 2002 primary rule description by Evans explains three-state excitation, refractory delay, and moving patterns but does not give three-row periodic orbit counts. Historical oscillator accounts already contain period-three examples, which are not claimed as novel. Jen's 1988 cylinder transfer method is an explicitly acknowledged general predecessor, not the enumerated degree-\(28\) polynomial, and available related finite graph and elementary automaton results concern different update maps and/or geometries. Searches for all-circumference Brian's Brain B2/S/C3 fixed-third-iterate counts, toroidal-strip zeta functions, and the characteristic-polynomial coefficients found no statement that implies this exact census. Risk: offline/poorly indexed oscillator catalogues and original older full texts are not exhaustively checked. The 1987 Toffoli–Margolus Brian's Brain discussion was visible in an indexed book excerpt but its 34MB full PDF could not be inspected, so whole-document noncoverage is not asserted.

## Mathematical value — PASS

The exact population of the first possible nontrivial temporal period is a natural dynamical invariant of the canonical three-state refractory automaton on the narrowest Moore torus with eight distinct neighbours. The result gives a finite-order rational spatial zeta, the precise first-cylinder onset, and a certified nontrivial growth rate. It determines every labelled period-three orbit count, not merely a sample table or general matrix existence assertion. It does not claim basin or higher-period classifications, or a new generic transfer method.

## Scope and limitations

The claim concerns a labelled periodic three-row torus, not open strips or the infinite lattice. Direct enumeration only tests the first three admissible widths; universal quantification follows from the exhaustive finite transfer graph and its symbolic characteristic identity. Historical priority is qualified; independent external validation is not established.

Self-review: passed. Independent audit: not yet performed.
