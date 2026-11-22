# Scientific review: sharp one-substitution dinucleotide-profile capacity

## Correctness (C): PASS
The local matrix identity for replacing one interior symbol accounts for both deleted and newly created adjacent edges. Row and column sums distinguish ordered replacements and boundary mutations; a support argument shows precisely one pair of interior contexts collide for each replacement. For \(q\ge3\) every triple has a mutation change vector unique to that triple, so maximality forces all \(q^3\) trigrams and length at least \(q^3+2\). De Bruijn linearizations meet the bound, and the directed Matrix-Tree/BEST calculation counts the indexed maximizers. Three separate executable checks corroborate local collisions, direct word-level substitution, and the de Bruijn count. The checker outputs cannot independently certify arbitrary parameters; those rely on the explicit proof.

## Originality (O): PASS against inspected literature, with residual priority risk
The 2013 context-dependent dinucleotide mutation study already provides the elementary local mutation accounting, which is expressly credited. En Gad (2026) treats substring-count hashes for error-correcting codes, not a sharp local substitution-profile sphere formula. Kiah–Puleo–Milenkovic (2015) treat global sequence profiles and coding. He–Kari–Millan Arias (2025) treat profile/Eulerian correspondences. Three relevant published exact enumerations (binary one-deletion, binary one-insertion, ternary global bigram profiles) were inspected in full and distinguish different operations or different quantifier order. The searches did not reveal the claimed q-ary substitution bound, de Bruijn first-attainment rigidity or maximizer count; unindexed Markov-type or histogram calculations cannot be excluded.

## Value (V): PASS
The precise object is the one-substitution observation ball of a fixed word under full oriented two-gram multiplicities, which is a natural noisy-read channel. Knowing its maximum alone does not identify when it can be achieved: the first-attainment theorem links a source length cutoff to complete coverage of trigrams, and the extremizer count describes all optimally diverse shortest sources. The result is an exact infinite-alphabet-family capacity and a sharp structural classification, not a routine recomputation of the global number of profiles.

## Boundaries and independent validation
The all-length bound and sharp saturation apply to \(q\ge3\), with no claim of all shorter-length spectra or coding-capacity improvement. Historical priority remains subject to independent literature review; the scripts are finite corroboration rather than proof of the infinite theorem.

Self-review: passed. Independent audit: not yet performed.
