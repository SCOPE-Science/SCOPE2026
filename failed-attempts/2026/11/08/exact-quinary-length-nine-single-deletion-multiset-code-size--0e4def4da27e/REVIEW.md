# Independent mathematical audit

## correctness

PASS

The coding problem is exactly the binary packing of 715 weight-nine 5-vectors, imposing one five-term ≤1 inequality for each of 495 weight-eight received vectors; the equivalent unit-transfer conflict graph has 4950 unordered edges. The checksum ≡0 mod 5 gives 143 valid codewords by cyclic symbol relabeling. The source two complete HiGHS MILP models report global dual upper bounds below 144; independently reconstructed all 715 vertices,495 output cliques,4950 conflict pairs and checksum validity. More importantly, an earlier published complete n=9 exact theorem gives the same conclusion. Numerical solver reports without a rational search certificate have a reproducibility/soundness limitation, not proof that the 143 bound is new.

## originality

FAIL

FAIL: a published 2026-11-02 result already states S₅(9,1)=143 with the IDENTICAL 715-vertex/495-extension-clique and 4950-edge integer models, together with n=10 value 201. Its complete theorem and proof were read. Moreover Zabokritskiy (arXiv 2607.13733, first posted July 15, 2026) establishes all-degree α(G₅(n))=ceil(C(n+4,4)/5) according to a later November 2 full mathematical theorem explicitly using it, making n=9 a direct corollary. Full Zabokritskiy text inaccessible, but the fully inspected Nov2 exact theorem is independently decisive.

## value

FAIL

FAIL as a distinct mathematical result: the integer 143 and checksum optimizer are already recorded and proved by earlier complete n=9+n=10 work and covered by the earlier general all-degree independence statement. No new structure, rational certificate, or nontrivial classification remains in this submitted result; copying two equivalent numerical MILPs does not create an independently valuable unknown exact fact.

The dated certificate retains the supplied scientific assessment, sources and limitations.
