# Independent Audit — 2026/09/15/021

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `bc60f6755e54eb483dbff6e5841d033e501c06b5`
- Disposition: **FAILED**

## Correctness

**PASS** — The finite census is internally consistent and agrees with older independent computations. The submitted sieve counts reduced primitive forms with the correct boundary weights and reports 290 fundamental discriminants of class number 125; its largest hit is 2,944,363, so extending the bound to 20,000,000 adds no later hit. The exact class-group verifier distinguishes the three order-125 group types by the number of nonidentity elements killed by 5. The eleven reported C25×C5 discriminants are compatible with the classical noncyclic-class-group tables, and the absence of (C5)^3 through 20 million is consistent with Buell's stronger computation that the first imaginary quadratic discriminants of 5-rank three occur at 11,203,620 and 18,397,407, neither having class number 125. No mathematical error was found in the finite statement.

## Originality

**FAIL** — The census is substantially pre-covered. Buell's 1977 computation tabulated occurrences of every class number up to 125 for all imaginary quadratic discriminants below four million—already beyond the submitted last h=125 hit near 2.94 million—and listed small class-group occurrences. More decisively, Buell's 1987 paper computed all noncyclic imaginary-quadratic class groups for discriminants up to 25,000,000, a range strictly larger than the record's 20,000,000 window. Hence the claimed exclusion of (Z/5)^3 and the noncyclic order-125 classifications do not constitute a new census result.

## Scientific value

**FAIL** — The modern C implementation is a reproducible re-verification of historical tables, but the mathematical output does not extend their range or resolve the admitted global missing-group problem. As research, it is replication rather than a new class-group result; its value is computational validation/benchmarking.

## Sources

- Small class numbers and extreme values of L-functions of quadratic fields (Duncan A. Buell): https://doi.org/10.1090/S0025-5718-1977-0439802-X — Processes the complete computed table for 0<D<4,000,000 to find occurrences of all class numbers up to 125; this already extends past the submitted final h=125 hit.
- Class groups of quadratic fields II (Duncan A. Buell): https://scholarcommons.sc.edu/csce_facpub/92/ — Computes noncyclic class groups of imaginary quadratic fields through discriminant 25,000,000 and identifies the first 5-rank-three discriminants.
- Missing class groups and class number statistics for imaginary quadratic fields (S. Holmin; N. Jones; P. Kurlberg; C. McLeman; K. Petersen): https://arxiv.org/abs/1510.04387 — Places (Z/pZ)^3 missing-group questions in the modern statistical context.

## Limitations

- The audit did not independently rerun the full 20-million sieve in this execution; correctness is checked from the source/logs plus independent historical tables.
- Failure is for originality and scientific value, not because the submitted finite computation is false.

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence. Open-access/preprint sources were checked first; Oxford Download was not needed.
