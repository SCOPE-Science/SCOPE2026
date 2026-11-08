# Scientific assessment

## Correctness

**PASS.** The theorem's quantifiers cover every positive integer alphabet size at the fixed input length six, with primitive necklaces counted modulo rotation and a linear (not cyclic) BWT-run condition. The proof reduces the claim to exactly all normalized alphabets of sizes one through six, gives an exhaustive primitive-Lyndon enumeration, and proves the order-preserving binomial lift. A second, independent last-to-first-permutation enumeration reproduces every admissible last column and input-run count. The ten multiplicity-partition histogram cells and all 384 complete census entries are reproducible. The result makes no claim at other word lengths.

## Originality

**PASS, subject to normal historical-priority risk.** Kumallagov's 2026 primary paper establishes the exceptional optimum at length six and supplies witnesses and a nonexistence test for three input runs, but not the complete all-alphabet input-run enumerator or alphabet-support restriction. The 2025/2026 Fici et al. paper proves general existence and lower counting bounds, not these multiplicities. Direct comparisons of claims, exact binomial coefficients, source tables, related records, and equivalent stable-permutation formulations found no result that implies this full six-letter spectrum. The earlier appendix's finite enumeration method could be adapted to recover the coefficients; such a derivability concern is a residual priority/value risk, rather than evidence that the coefficients were already stated.

## Value

**PASS.** Length six is the distinguished exceptional case where the universal half-length BWT run-amplification lower bound is not tight. The theorem completely determines the number of extremizing inputs and the full input-run distribution for every alphabet size, resolves which input multiplicity patterns are possible, and proves that four-run extremizers disappear proportionally as \(7/(2q^2)\). These describe a natural compression-geometry boundary more precisely than the known optimum or example table. The result is a self-contained classification of the exceptional case, not a proposed general-length formula.

## Sources and limitations

- Kumallagov, arXiv:2606.01267v1, §§3, 6 and Appendix A: known minimum, examples, and length-six obstruction.
- Fici, Gabory, Romana and Sciortino, arXiv:2508.20879, CPM 2026: all-length existence and a general lower bound on counts.
- Scope: primitive ordered-alphabet cyclic BWT, input length six only. Independent external audit and definitive historical-priority confirmation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
