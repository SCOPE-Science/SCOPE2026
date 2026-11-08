# Scientific review

## Correctness: PASS

The paired-positive-run parameterization is bijective up to simultaneous cyclic rotation, including periodic words. Reversal acts on the two run-composition rows with an index offset of one; hence odd run count gives one fixed coordinate on both rows, and even run count gives two fixed coordinates on exactly one row. The fixed-composition generating functions yield the claimed coefficients. Dihedral Burnside and orbit pairing rigorously give the achiral-orbit count; independent literal enumeration of all binary necklaces through length 17 agrees in 444 feasible parameter profiles. The proof also covers the smallest case and establishes the exact parity boundary. The verification program tests cases but does not constitute the universal proof.

## Originality: PASS, qualified

The full 2013 Zelenyuk–Zelenyuk primary text was inspected: its main formula counts unrestricted symmetric colorings of a cycle, whereas the present theorem conditions jointly on the counts of both letters and both transitions, requiring an offset two-composition reflection calculation. The 2013 Knopfmacher–Robbins abstract treats a single dihedral composition and does not visibly resolve the coupled row action. The 2021/2022 Bianconi–Brugnoli abstract concerns transition-counted necklaces but not their reflection symmetry with fixed content. Semantic comparison with published research records and accessible earlier work found no identical claim. Unread full texts and unindexed weighted-necklace results remain genuine priority risks; a negative search is not a uniqueness certificate.

## Value: PASS

Reversal identifies two physically indistinguishable orientations of a circular two-symbol sequence, while a dinucleotide profile forgets absolute position. An exact count of orientation-fixed reconstructions is a natural missing component of the profile's ambiguity distribution, not a random finite slice. The theorem gives the full infinite-parameter spectrum of achiral and chiral classes and an unexpected if-and-only-if parity obstruction, distinguishing profiles in which every reconstruction is chiral from those where an achiral reconstruction exists. No downstream biological performance is claimed.

## Scope and limitations

The claim treats nonconstant binary circular words only, with cyclic read adjacency and classes modulo rotation. It is not a statement about linear words, multiletter alphabets, or faulty reads. Main historical risks are possible implicit refinements in the inaccessible dihedral-composition and necklace-transition full texts. Correctness is established by proof, with finite computations as a secondary check.

Self-review: passed. Independent audit: not yet performed.
