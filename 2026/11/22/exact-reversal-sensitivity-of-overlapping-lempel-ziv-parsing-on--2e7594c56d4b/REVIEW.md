# Scientific review

**Correctness (C): PASS.** The proof fixes the overlapping longest-previous-factor convention, partitions the only nontrivial parsing step into \(c\le a\), \(a<c\le2a\) and \(c>2a\), and explicitly includes all strict and equality boundaries. It derives the reversal and sharp extremizer conditions by two independently bounded functions and proves the limit using independent Dirichlet ratios. Direct parsing and independent lengthwise checks passed, but finite checks are not an infinite proof.

**Originality (O): PASS against inspected sources, with priority risk.** The 2026 Bannai–Fujie–Guo–Inenaga–Nakashima–Puglisi–Urbina article introduces the relevant reversal sensitivity theorems; the August 2026 Shibata–Fujie article strengthens global multiplicative bounds. Neither of their inspected statements implies the present exact four-run formula, first length-12 extremizers or Dirichlet distribution. A published de Bruijn-cycle overlap-cost spectrum concerns another family and another operation. Exact-expression, alternative-description and stronger-coverage searches did not locate an equivalent result. Absence in an index does not prove novelty; unindexed literature remains a residual risk.

**Value (V): PASS.** The theorem resolves a natural run-restricted asymmetry question across all positive parameters, not a one-off computation: its sharp uniform bound and complete equality geometry are combined with a discrete probability law for all long four-run words. It distinguishes structured finite-run inputs from unrestricted worst-case constructions.

**Reproducibility:** `verify_lz.py` (28561 direct parameter tests per orientation), `verify_counts.py` (lengths 4--30 and exact limit-law algebra), and captured outputs are included. The result is limited to overlapping greedy parsing and to the specified run and sampling families. No independent audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
