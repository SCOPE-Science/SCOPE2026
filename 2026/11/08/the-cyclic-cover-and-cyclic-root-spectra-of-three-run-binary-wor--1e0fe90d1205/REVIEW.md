# Scientific review: cyclic covers and roots of three-run binary words

## Correctness (PASS)

The theorem ranges over arbitrary integers \(a,c\ge1\), \(b\ge2\) for the linear word \(0^a1^b0^c\). A cyclic cover necessarily forces the length-matched prefix and suffix to be conjugate, hence to have equal counts of ones. For unequal flanks this gives exactly the stated long-length threshold; for equal flanks, shorter patterns reach at most \(r\) middle-run positions from each end and give the \(2r\ge b\) criterion. The factor census follows from uniqueness of the central run; the cyclic-root restriction follows from equal Parikh vectors in each partition block. The accompanying definition-driven checker passed 1,250 parameter triples and 26,029 candidate-length comparisons. The general proof, not the finite checks, establishes the infinite result.

## Originality (PASS, bounded bibliographic confidence)

The original Grossi–Iliopoulos–Jansson–Lim–Sung–Zuba paper explicitly gives the case \(0^m10^m\), which is acknowledged and excluded. Its general cyclic-cover algorithm, the 2025 open-access revision, and the later Iliopoulos–Kociumaka–Radoszewski–Rytter–Waleń–Zuba linear-time cyclic-cover/cyclic-root algorithm cover computation of instances, not an explicitly stated uniform formula for the remaining three-run family or its length-refined factor counts. Searches of published research records and targeted literature did not identify an equivalent theorem. An unindexed result or an unstated consequence of general algorithmic work could still affect priority; the result does not claim independent bibliographic certification.

## Value (PASS)

The two-transition binary family is a complete natural class for which cover behaviour changes qualitatively at equality of the outer runs. Its full length set, every distinct covering factor count and cyclic-root spectrum have explicit closed forms. A single appended zero can increase the shortest cover length by an unbounded amount, while outside symmetry the total number of covering factors is independent of the middle-run length. These structural facts distinguish the result from merely running a general cyclic-cover algorithm.

## Scope and limits

The singleton-middle-run example is prior work. Neither the theorem nor the verification script addresses words with more than two transitions, cyclic text wraparound, approximate cyclic covers, or independent external validation. The first public guiding source is the 2023 repository entry, not the later journal publication.

Self-review: passed. Independent audit: not yet performed.
