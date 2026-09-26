# Independent audit — 2026-09-22 campaign

**Original record:** `2026/09/09/019`  
**Audited source tree:** `02af8ec3a8c399f2e214613d4c63f3cf3ec667c8`  
**Date:** 2026-09-26 UTC  
**Disposition:** FAILED; archive full original package

## Correctness

PASS. Independently checked every unordered point pair in the four committed block systems appears once and counted all four-block subsets whose union is six points: the two STS(13) representatives have 13 and 8 Pasch configurations; the STS(15) witnesses have 0 and 105. Re-ran the committed canonical-prefix exact-cover enumeration from its Git-hash-matched Python sources: 138 candidate triples over 57 uncovered pairs gave 14,400 completions, partitioned 1,920 cyclic and 12,480 noncyclic, with automorphism orders 39 and 6. The fixed-prefix lemma supplies coverage of both isomorphism types, and the PG(3,2) witness has the expected 35 blocks and GL(4,2) order 20,160.

## Originality

FAIL. The open 2023 paper A visual representation of the Steiner triple systems of order 13 explicitly says the cyclic system contains thirteen quadrilaterals/Pasch configurations and the noncyclic contains eight, and gives the same automorphism group orders 39 and 6. Grannell et al.'s older original anti-Pasch account states that the 80 STS(15) classes range from 0 to 105 Pasch configurations. The record's anti-Pasch and PG(3,2) witnesses instantiate those known endpoints; its 14,400 completions are for one arbitrary labeled prefix, not a new invariant or classification beyond the known two STS(13) types.

## Scientific value

FAIL as a fresh accepted research result. The reproducible exact-cover implementation and witness JSON are useful teaching or regression data, but the stated census and extrema are already documented, and no new STS(15) distribution or structural theorem is provided.

## Prior work

- https://iris.unipa.it/retrieve/674a8990-dc17-457f-b6b2-f2261c09ebde/Picture%20STS(13)_2023_01_05.pdf
- https://grannell.net/Papers/APasch.pdf

## Consequence

The exact numbers reproduce successfully but the headline census and endpoint examples already occur in the cited literature. The full original record and artifacts are retained under `original/`; the accepted path is removed atomically with this archive.
