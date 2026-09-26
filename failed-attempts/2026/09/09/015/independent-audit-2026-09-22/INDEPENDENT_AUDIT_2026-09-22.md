# Independent audit — 2026-09-22 campaign

**Original record:** `2026/09/09/015`  
**Audited source tree:** `37323471aa1c4763ddc56237d252656528a0a9b8`  
**Date:** 2026-09-26 UTC  
**Disposition:** FAILED; archive full original package

## Correctness

FAIL. Marcus–Spielman–Srivastava define a 3-regular graph as Ramanujan when every nontrivial adjacency eigenvalue lies in [−2√2,2√2], excluding −3 only for bipartite graphs. The committed verifier inspects λ2 alone. Independently decoded all five committed GENREG shortcodes (19,85,509,4060,41301 graphs) and diagonalized both spectral ends. Its claimed counts 19,84,480,3870,39686 are positive-side-only counts; the two-sided counts are 19,80,448,3563,36256. The false positives by order are 0,4,32,307,3430. In the n=12 file graph #8, λ2≈2.655442<2√2 yet λmin≈−2.891220<−2√2, and the graph is nonbipartite. A rigorous counterexample needs no eigensolver: adjacency [[1,2,3],[0,2,3],[0,1,4],[0,1,5],[2,5,6],[3,4,7],[4,8,9],[5,10,11],[6,10,11],[6,10,11],[7,8,9],[7,8,9]] and integer vector x=[0,0,−793,793,2292,−2292,−3541,3541,3974,3974,−3974,−3974] give xᵀAx/xᵀx=−289157520/100012292<−2√2. The stated minimal-λ2 extremals may remain valid for a one-sided objective, but cannot repair the false Ramanujan census.

## Originality

PASS only for a narrower possible contribution. OEIS/Meringer provide graph counts and raw lists, whereas MSS supplies the two-sided definition and existential results; the record's per-order λ2 minima and matrices are not simply copied from those sources. The central purported Ramanujan census, however, has no valid novel numerical conclusion as stated. I have not established a literature-complete novelty claim for a corrected two-sided census.

## Scientific value

FAIL for the published claim. Exact small-order Ramanujan counts would be a useful expander benchmark, but thousands of the record's labels are false. The original raw graph files and one-sided computations are worth preserving for correction; accepting this version would mislead downstream users.

## Prior work

- https://arxiv.org/pdf/1304.4132
- https://www.mathe2.uni-bayreuth.de/markus/reggraphs.html
- https://oeis.org/A002851

## Reproduction and scope

The five raw shortcode files were transferred byte-for-byte from GitHub; their Git blob hashes matched the repository. Independent decoding and `numpy.linalg.eigvalsh` supplied corrected census counts. Counts near the spectral threshold rely on floating-point eigensolvers; the explicit n=12 counterexample is certified exactly by the integer Rayleigh quotient and suffices to refute the original conclusion. The complete original package is retained under `original/` in this archive.
