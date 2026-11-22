# Scientific review: antipodal six-tap two-channel Gabor tight frames

## Correctness — PASS

The proof reduces all tightness equations to \((1+\chi^s)r_s=0\) for the five distinct positive lags, using the full translation diagonalization and \(N\ge12\) to rule out aliasing. Nonzero endpoint correlation forces character order two or ten. Under order ten, the simultaneous vanishings at lags one, three, and four contradict the unit-modulus constraint through an equilateral-triple argument with incompatible magnitudes \(\sqrt3\) and \(1\). Thus only the antipodal character survives. Two remaining even-lag equations solve completely to two independent \(\mathbb T^3\) families; finite phase groups yield exactly \(2q^3\) solutions precisely for \(4\mid q\). Each implication is bidirectional, and \(\operatorname{tr}S=12N\) establishes the stated bound \(12\).

Verification follows the actual supplied `CHECK_EXACT.py` and `CHECK.py` programs. Exact Gaussian-integer enumeration found \(128\) quaternary antipodal solutions and zero order-ten solutions, consistent with known published counts; full frame-operator sums reproduced \(12I\) for several even cyclic orders. The exact algebraic argument, not finite experimentation, proves the universal quantifiers. Limitations: orders below twelve and nonunimodular windows are not covered.

## Originality — PASS with bounded historical risk

The earliest relevant length-three Golay-pair computations are **not new**. Craigen, Holzmann and Kharaghani (2002), §4.3, explicitly give the \(128\)-pair quaternary census. Parker, Paterson and Tellambura (2003) discuss the primitive quadriphase length-three pair, and Bright et al. (2018) independently recover \(128\) labelled pairs (with one equivalence class). These cover the finite quaternary Golay slice, so the claim expressly excludes its historical priority.

The exact all-order Gabor classification still requires two scientific steps not provided by those tables: deriving and excluding an order-ten modulation candidate for **six consecutive taps**, and solving the complete complex-phase configuration, including sharp divisibility/counts for arbitrary root alphabets. Magsino (2016) provides the general finite Gabor ambiguity-function tightness condition, not the six-tap solution. An indexed public two-modulation/all-translation paper addresses **three** consecutive taps and a quarter-period phenomenon; a separate indexed phase-alphabet result uses **three translations and half the modulation subgroup**, not two modulations with all translations. Full texts of these close results were inspected and the statements compared at the implication level. Specific risk remains that old polyphase Golay literature contains an algebraic length-three all-phase parametrization, or a general Gabor source states this same six-tap corollary without indexing. The comparison does not claim search exhaustiveness or independent novelty certification.

## Value — PASS

This is a complete natural first case in which two interlaced three-site polyphase sequences, rather than a single short correlation, are required to cancel all cyclic Fourier sidelobes. The theorem gives a genuinely different modulation rigidity from the known three-tap quarter-period case: an **antipodal gap is forced in every dimension**, while an apparently feasible order-ten gap is excluded by a nontrivial unimodular obstruction. It also identifies the entire continuous optimal design space and its sharp phase-alphabet threshold, rather than one design or a routine recomputed finite count. These are directly usable when constructing redundant tight time-frequency frames with exactly two modulation channels and six-sample constant-envelope windows. No claim of superior stability under erasures or application-specific performance is made.

## Closest literature and residual limitations

- R. Craigen, W. Holzmann, H. Kharaghani (2002), DOI `10.1016/S0012-365X(01)00162-5`: the \(q=4\) length-three Golay case is covered, not this all-order two-modulation frame classification.
- M. G. Parker, K. G. Paterson, C. Tellambura (2003), DOI `10.1002/0471219282.eot367`: early primitive quadriphase pairs, no exhaustive continuous-phase Gabor classification identified.
- F. Krahmer, G. Pfander, P. Rashkov (2006), arXiv `math/0611493`: finite STFT and Gabor foundations; no identical six-tap design statement found in inspected sections.
- M. Magsino (2016), arXiv `1611.00818`: generic necessary/sufficient tightness criterion, not an all-phase solution at six consecutive taps.
- C. Bright, I. Kotsireas, A. Heinle, V. Ganesh (2018), arXiv `1805.05488`: exact \(128\) quaternary three-term pair count, covered as prior work.
- Public *Exact phase–frequency design and tightness transition for three-tap cyclic Gabor frames* (2026): same modulation architecture but fewer taps; no subsumption.
- Public *Arithmetic existence and exact phase-alphabet counts for three-translate cyclic Gabor tight frames* (2026): different time-frequency lattice and full-support requirement; no subsumption.

Self-review: passed. Independent audit: not yet performed.
