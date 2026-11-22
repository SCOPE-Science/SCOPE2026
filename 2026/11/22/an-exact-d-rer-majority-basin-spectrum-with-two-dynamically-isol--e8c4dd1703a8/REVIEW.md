# Review of the Dürer majority basin spectrum

## Correctness — PASS

For each of the exactly \(2^{12}=4096\) labelled binary states, the open-neighbor update is deterministic. The supplied Python implementation builds the generalized Petersen adjacency and classifies the entire functional graph by indegree peeling. The independently written C++17 implementation builds the standard LCF representation, verifies an explicit graph isomorphism and classifies the same full state space by first-repetition path tracing. Both return the complete basin-size-by-period table, the six first-entry populations, fixed/primitive-two-cycle counts and the identical consensus basin sizes. The Python implementation additionally checks all twelve automorphisms and Burnside incidences. The finite functional-graph proof guarantees completeness, not extrapolation from partial tests. The asserted all-size singleton basins have a separate symbolic proof: \(2A+B\ge2n\) and \(A+2B\le n\) force \(B=0,A=n\) for every predecessor of a polarized fixed state. Remaining risk: implementation or specification error shared across the two representations; this is mitigated by explicit graph-isomorphism and two algorithms but is not an independent external audit.

## Originality — PASS, with historical-priority uncertainty

The closest published all-size generalized Petersen majority-transfer result already gives \(14\) fixed states and \(184\) primitive temporal two-cycle orbits at \(GP(6,2)\); **these values are not claimed new**. Its complete available result explicitly excludes attraction basins and transient entry times. The published fixed-sector polynomial result concerns fixed-state populations, not basin multiplicities. The dodecahedral \(GP(10,2)\) dynamical census is for a different circumference, and general period-two theorems do not determine this network's individual attraction basins or sharp five-step entry distribution. Directly checked claims in the accessible current ledger do not contain the Dürer basin table. Searches by Dürer/GP(6,2), aliases, first-entry time, period distributions and individual basin parameters found no equivalent statement. Residual priority risk: inaccessible, unindexed older specialized table or algorithm may cover the same 4096-state census. This is a best-knowledge originality comparison, not a guarantee of global novelty.

## Mathematical value — PASS

Dürer is a canonical cubic planar, dihedrally symmetric graph; its all-state basin census reveals how immediate orbit counts fail to characterize transient dynamics or basin sizes. The sharp five-update layer includes exactly \(96\) states and leads only to fixed points. Its fifteen basin sizes and exact symmetry quotient form a natural finite benchmark against other canonical cubic networks. The symbolically proved singleton-basin result is not arbitrary numerical post-processing: it isolates the two polarized layer equilibria on the entire generalized Petersen family. This is an exact finite classification with a meaningful structural extension, not a proposed general all-size basin formula.

## Close literature and limitations

1. Goles and Olivos (1980), generalized threshold periodicity: period-at-most-two only; article body not fully available in this comparison.
2. Benjamini, Chan, O'Donnell, Tamuz and Tan (2014), arXiv:1405.2486v1: inspected the full available text, which supplies general majority context, not the Dürer basin table.
3. *An equilibrium–oscillation entropy reversal on generalized Petersen graphs*: full available RESULTS text inspected; gives recurrent counts through transfer matrices, explicitly excludes attraction basins and first-entry times.
4. *Ninth-degree spin sectors and an entropy gap in majority dynamics on generalized Petersen graphs*: full available RESULTS text inspected; gives fixed-point population and growth, explicitly excludes transient and two-cycle basin classification.
5. Dodecahedral majority census: relevant published summary checked, but this comparison did not inspect its complete text; different \(GP(10,2)\) graph, no inference of the Dürer basin counts.

Self-review: passed. Independent audit: not yet performed.
