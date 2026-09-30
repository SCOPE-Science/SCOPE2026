# Independent Audit — 2026/09/14/029

**Audit date:** 2026-09-29 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `3cbcf94ab598b2c035d0b726b010741ef9e03def`  
**Audited current source tree:** `3cbcf94ab598b2c035d0b726b010741ef9e03def`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** failed

The current `main` directory tree SHA exactly matches the assignment tree SHA, and the designated failed destination was verified absent.

## Correctness — PASS

PASS. I independently rebuilt the 4×4-vertex, 24-edge grid and exhaustively enumerated all 2^24 bond configurations with a separately written multi-source BFS. The result exactly matches the record: N_cross=10,575,744, sum_S=36,373,760, and counts for S=3,…,9 equal 6,942,720; 2,790,784; 697,472; 123,264; 16,896; 4,224; 384. Thus E[S|Cross]=36,373,760/10,575,744=284170/82623≈3.43935707974777, and 5·sum_S<18·N_cross, so the ≥3.6 claim is correctly disproved.

## Originality — PASS

PASS, NARROWLY. Targeted searches for the exact fraction and ledger integers found no covering prior, while the cited percolation literature concerns large-scale/asymptotic chemical distance and does not determine this finite 4×4 enumeration. This is only a narrow originality judgment for the exact finite datum; search non-detection alone is not treated as evidence of importance or broad priority.

## Scientific value — FAIL

FAIL AS A STANDALONE RESEARCH FINDING. The result is a brute-force evaluation of one 4×4 grid at one probability against the arbitrary threshold 3.6. It supplies no new method, structural identity, scaling law, rigorous bridge to asymptotic tortuosity, or reusable classification; two BFS implementations and an inclusion–exclusion spot check strengthen correctness but not scientific significance. The exact datum could serve as a regression test or benchmark, but that is not enough to support the record's research-value framing.

## Independent checks

- independent C/OpenMP exhaustive enumeration over all 16,777,216 masks reproduced every histogram count
- verified fraction reduction and exact 3.6 inequality
- verified S=3 count by inclusion–exclusion on the four disjoint straight rows
- searched exact headline integers/fraction and compared theorem scope with asymptotic chemical-distance literature
- checked current record tree equals the assigned tree and failed destination is vacant

## Limitations

- The failure is scientific-value failure, not a correctness failure.
- The originality pass is deliberately narrow and does not assert exhaustive historical priority.
- A finite-size table embedded in a broader finite-size scaling theory or a reusable exact method could warrant a different value assessment, but that is absent here.
- Open-access sources were sufficient; Oxford Download was not needed.

## Evidence and references

- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/14/029
- https://arxiv.org/abs/1506.03461
- https://doi.org/10.1007/BF01053586

This audit changes only the independent-audit channel in `VERIFICATION.md`; Lean verification and expert attestation remain exactly as previously recorded.
