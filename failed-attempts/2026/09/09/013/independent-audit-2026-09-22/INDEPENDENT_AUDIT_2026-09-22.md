# Independent audit — 2026-09-22 campaign

**Original record:** `2026/09/09/013`  
**Audited source tree:** `4803ddb831d393c3164ea378f79702aa71327150`  
**Date:** 2026-09-26 UTC  
**Disposition:** FAILED; archive full original package

## Correctness

PASS. Independently enumerated all 1,024 words from the committed ten systematic 22-bit rows. Weights are {0:1,8:330,12:616,16:77}; nullspace enumeration of 4,096 dual words gives the displayed 11 nonzero coefficients. All 23 integer Krawtchouk sums equal 1,024 times those dual coefficients. An independently built 12-bit syndrome graph has distance layers [1,22,231,1540,1771,484,45,2], giving covering radius 7. These checks support the explicit witness and distance 8; they do not independently certify that the rows arise from the stated parent cyclic construction, although the committed script provides that replay.

## Originality

FAIL. Sven Polak, Semidefinite programming bounds for constant weight codes, arXiv:1703.05171 (2017), p. 2, explicitly states that the twice-shortened extended Golay [22,10,8] code has precisely 1, 330, 616, and 77 words of weights 0, 8, 12, and 16. This is the record's headline enumerator and same object. The dual enumerator is determined mechanically by the standard MacWilliams identity. The record's assertion that the closest bounds tables publish no enumerator overlooks this directly matching preprint. The explicit generator and syndrome-layer tally are useful reproducibility details, but cannot restore originality of the claimed main result.

## Scientific value

FAIL as a new accepted research result. The code's weight enumerator and its classical optimality are already in the cited primary literature; the remaining independently checked dual transform and small 4,096-syndrome layer table can serve as an instructional verification artifact, but the record supplies no distinct new theorem or unresolved classification.

## Prior work

- https://arxiv.org/pdf/1703.05171
- https://www.codetables.de/BKLC/BKLC.php?q=2&n=22&k=10

## Consequence

The accepted claim duplicates the already printed 2017 weight spectrum. The archive preserves the original record and artifacts byte for byte under `original/`; the accepted path is removed in the same commit.
