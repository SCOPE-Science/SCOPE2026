# Scientific assessment

## Correctness (C): PASS
The local identity for a deletion at an interior position is obtained by subtracting the three destroyed trigrams and adding the two newly joined trigrams. The only other deletion positions are the two at each boundary. A support-preserving alphabet collapse makes the five fixed-alphabet exhaustive counts sufficient for all \(q\); the included program enumerates every neighborhood for each support size \(1\) through \(5\), with counts \(1,8,90,192,120\). A de Bruijn linearization realizes all interior changes, while four explicit endpoint changes are outside that set. An independent direct histogram program verifies all deletion outcomes for \(q=2,3,4,5\). The exact first saturation length is *not* proved.

## Originality (O): PASS against inspected evidence
The previously known binary single-deletion trigram bound is a specialization and receives no new priority claim. The neighboring nonbinary dinucleotide-profile capacity concerns length-two rather than length-three oriented factors. The inspected primary paper by Kiah, Puleo and Milenkovic defines q-ary profile vectors and derives global profile and coding bounds without the present local deletion-image count. Literature on unrestricted three-mer profile enumeration studies a global image, not the local deletion fiber above a fixed source. En Gad's 2026 substring-count hashing preprint is closely motivated by the same read-frequency representation but advertises redundancy bounds for deletion-correcting codes, not this exact all-alphabet local capacity. Searches for ternary 121-profile bounds, alphabet-polynomial local change-vector counts, and corresponding de Bruijn saturation did not recover an equivalent statement; these searches are evidence of comparison, not proof of priority. The En Gad full text was inaccessible and remains a residual coverage risk.

## Value (V): PASS
A deletion channel measured only through its oriented three-mer histogram can have dramatically fewer outputs than the number of deletion positions. The theorem supplies its sharp maximal observation capacity as an explicit polynomial in the alphabet size, separating internal and boundary effects; it also supplies universal near-optimal-length saturation witnesses, with a leading-order optimality proof for their length. This is a natural structural capacity invariant for fixed-length readout channels, rather than an arbitrary short numerical census.

## Limitations
The exact smallest saturation length for any fixed nonbinary alphabet is not resolved, and no broader edit model or independent external validation is claimed. The 2026 substring-count hashing source could be checked only via public abstracts/metadata; equivalence hidden in inaccessible full text cannot be ruled out.

Self-review: passed. Independent audit: not yet performed.
