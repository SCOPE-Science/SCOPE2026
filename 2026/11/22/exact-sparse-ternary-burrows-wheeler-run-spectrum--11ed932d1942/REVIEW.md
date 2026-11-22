# Scientific review: exact sparse-ternary Burrows–Wheeler run spectrum

**Correctness — PASS.** The rotation-order lemma explicitly describes every zero-starting row and the three remaining marker-starting rows. The nonempty nested active-gap masks give 26 possible chains, and one-level versus repeated-level choices give 111 exhaustive rational-weighted cases. The exact symbolic identity confirms each of the five generating-function numerators and the independent composition count. Direct BWT sorting of every gap triple for lengths 3 through 54 independently reproduces the coefficients. These finite tests alone are not a proof; the case-partition rational identity is the infinite argument.

**Originality — PASS, qualified.** The 1994 BWT algorithm is foundational. Simpson–Puglisi's 2008 ternary theorem characterizes BWT outputs with one consecutive block per symbol in a special descending order, not the entire sparse-content run distribution. The closest explicit binary three-marker census produces only even runs and divides necklace counts by the symmetry of identical markers; that theorem neither counts nor subsumes the mixed ternary three-marker result. Direct searches for sparse ternary BWT run spectra returned no equivalent published table, but an unindexed historical formula remains a concrete residual risk.

**Value — PASS.** Sparse-marker words are a natural test family for run-length-based BWT compression and indexing, and the first nonbinary three-marker composition exposes a qualitative change from the binary parity-restricted run spectrum to both odd and even numbers. The theorem resolves all lengths and exact multiplicities, not an arbitrary finite cutoff.

**Limitations.** The theorem is specific to composition \((n-3,1,2)\) and ordinary linear runs of the sentinel-free BWT. It does not claim general ternary content, circular output runs, or external certification. An older inaccessible or unindexed sparse ternary enumeration might supersede the originality assessment.

Self-review: passed. Independent audit: not yet performed.
