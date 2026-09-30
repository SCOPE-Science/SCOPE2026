# Independent Audit — 2026/09/17/hadamard-order-refinement-of-kusner-counterexamples--61c76de11ba3

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `c808b7df642aacaee9c58408e95ef9a3a60b1dc8`
- Disposition: **FAILED**

## Correctness

**PASS** — The theorem is mathematically correct. The arbitrary-Hadamard replacement preserves Xiong's four distance cases, and m>1/Delta(p) gives a solution of Phi_p(a)=1+1/m by continuity. The expansion Delta(4+delta)=c delta+O(delta^2) has the stated c. For the lower bound, Swanepoel's 2014 quantitative stability near p=4 gives delta >= 4 log(1+2/d)/log(d+2) at the first failure dimension; asymptotic inversion indeed yields d >= (8+o(1))/(delta log(1/delta)). No correctness defect was found.

## Originality

**FAIL** — The principal upper-bound contribution was already public in the earlier SCOPE record 'Hadamard densification and critical dimension scaling in Xiong's Kusner counterexamples', committed at 2026-09-17 14:31:30 UTC. That earlier record already proves the arbitrary-Hadamard extension and the same (8/c+o(1))/delta upper asymptotic. This record was first committed at 17:00:42 UTC. Its additional lower bound is a direct contrapositive/asymptotic inversion of Swanepoel's 2014 p=4 stability estimate. Thus the displayed two-sided bracket is a synthesis of an already-public same-day result and an old published corollary, not an independent new theorem.

## Scientific value

**FAIL** — The two-sided presentation is a useful summary, but it neither improves the already-public upper construction nor introduces a new lower-bound argument; the logarithmic gap remains exactly the one obtained by juxtaposing the earlier upper result with Swanepoel's known estimate. As a research record, the incremental content is too small once publication chronology and the existing 2014 corollary are taken into account.

## Sources

- Hadamard densification and critical dimension scaling in Xiong's Kusner counterexamples (SCOPE-Science/SCOPE2026): https://github.com/SCOPE-Science/SCOPE2026/tree/74497afca5c44c2b08e68e3dc3debb522018666a/2026/09/17/hadamard-densification-kusner-critical-scaling--43b27c183a43 — Earlier public record, committed 2026-09-17 14:31:30 UTC, already containing the arbitrary-Hadamard extension and leading upper constant.
- Equilateral Sets and a Schütte Theorem for the 4-norm (Konrad J. Swanepoel): https://doi.org/10.4153/CMB-2013-031-0 — Gives the quantitative near-p=4 stability estimate whose direct inversion yields the record's lower asymptotic.
- Kusner's conjecture is false for p>4 (Nathan Xiong): https://arxiv.org/abs/2609.14794 — Underlying p>4 construction.

## Limitations

- The audit accepts all displayed asymptotics and the arbitrary-Hadamard construction as correct.
- The failure is driven by publication chronology and prior coverage, not by a mathematical error.
- The failed-attempt destination was checked at the audited inventory snapshot and was vacant.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first. Oxford Download was not needed for this record.
