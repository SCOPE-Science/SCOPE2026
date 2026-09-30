# Independent Audit — 2026-09-28

**Record:** `2026/09/10/040`  
**Title:** Claimed two-sided Bilu–Linial datum for canonical LPS X^{3,5}  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `f42e8c897a125babd6eca6fbe1b419bf562ea8ea`  
**Disposition:** **FAILED**

## Independent checks

- Read the filed graph/generator JSON and the exact-certification scripts.
- Performed the determinant-square-class check directly over F5 rather than accepting the repository's graph label.
- Compared the graph identity against the standard LPS quaternionic construction; the failure is prior to and independent of the signed-spectrum calculation.

## Three-axis assessment

- **Correctness — FAIL**: The finite signed-matrix computations may be internally consistent, but the headline identifies the 60-vertex graph as the canonical LPS X^{3,5}. In the standard quaternionic LPS construction a norm-p generator has projective determinant square-class p modulo q. Here p=3 is a nonsquare in F5, so such generators lie in the nontrivial PGL2(F5)/PSL2(F5) coset and cannot define a Cayley graph on the 60-element PSL2(F5). The filed generator matrices have determinant 1 mod 5, confirming they are not projective norm-3 LPS generators. Thus the core object identity and the claimed 'smallest 4-regular LPS cell' interpretation are false.
- **Originality — UNRESOLVED**: The exact spectrum of the filed 60×60 signed matrix could still be a new finite computation, but once the LPS identity fails it is no longer the concrete open-problem instance advertised by the record. Priority for the weaker arbitrary-filed-graph datum was not established.
- **Scientific Value — FAIL**: The record's scientific significance rests on placing the datum in the LPS/Bilu–Linial setting. A spectral certificate for a misidentified finite graph does not validate that claimed example; a meaningful repair would first need a correctly constructed and independently verified base graph, then a fresh signing audit.

## Sources compared

- Repository record 040 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/09/10/040/RESULT.md — Claims the filed 60-vertex PSL2(5) Cayley graph is X^{3,5} and derives open-problem significance from that identity.
- Repository record 040 lps_graph.json: https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/09/10/040/artifacts/lps_graph.json — Files the 60-vertex adjacency and determinant-1 generator matrices used in the record.
- Lubotzky–Phillips–Sarnak, Ramanujan graphs: https://doi.org/10.1007/BF02126799 — Primary source for the quaternionic LPS construction whose norm/determinant square-class distinguishes the PSL and PGL cases.

## Limitations

- This failure does not assert that the filed 60×60 matrix lacks the quoted spectral bound; it rejects the claimed canonical LPS identity and the scientific interpretation built on it.
- A repaired record would need to reconstruct X^{3,5} under a valid convention and prove the filed matrix is isomorphic to it, or else explicitly recast the work as an unrelated finite graph datum and re-audit value/originality.

This audit is independent of the repository's pre-existing `AUDIT.json`. GitHub was read only as evidence; no repository changes were made by this audit run.
