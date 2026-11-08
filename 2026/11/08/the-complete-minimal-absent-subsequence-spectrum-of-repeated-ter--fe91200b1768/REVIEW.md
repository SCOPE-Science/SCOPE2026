# Scientific review

## Correctness — PASS

For every nonempty ternary candidate, greedy matching into the repeated permutation ends at position \(1+v_\ell+3D(v)\). Absent means \(D\ge k\); every single deletion reduces \(D\) by at most one, giving the exact endpoint and triple criteria and proving the all-\(k\) classification. The nine-state transfer construction is bijective. The accompanying exact integer certificate proves \((I-T)H=QB\) and \(AH=N\) as polynomial identities for the displayed rational function. Its standard-library verifier also checks formal-series coefficients, the initial length spectra and 103,784 direct candidate evaluations. A finite test is not used as a substitute for the polynomial identity or the combinatorial proof. Risk: transcription or implementation error was addressed by independent direct enumeration and exact certificate replay; no external audit was performed.

## Originality — PASS, with bibliographic risk

**Closest primary source:** Kosche, Koß, Manea and Siemer (arXiv:2108.13968), §3 and Proposition 3.8, study the same \(B_k\) repeated-increasing-permutation words. They give the short-absence class and show exponential minimal-absence growth through a selected constructed subfamily, but not a complete ternary all-length spectrum. The present theorem fixes the smallest nonbinary alphabet and determines every minimal-absence length by a rational bivariate enumerator. The previously established binary formula and the published number of shortest absent subsequences are not re-claimed. Adamson et al. (arXiv:2407.18599) study counts of all absent (not necessarily minimal) subsequences at fixed length across host words, and Manea et al. (arXiv:2504.21471) give arbitrary-host enumeration algorithms, not this explicit closed form. Semantic research-index searches and accessible earlier mathematical statements found no equivalent. A possibly relevant 2023 chapter could not be inspected in full; its existence and the possibility of unindexed exact equivalents remain risks, not evidence of novelty by themselves.

## Value — PASS

A complete length-resolved enumerator and all-size structural characterization for the canonical ternary family directly sharpen an existing exponential-versus-polynomial phenomenon. Unlike a small finite table or an arbitrary parameter slice, the result solves the natural complete census for every number of repetitions of the smallest alphabet beyond binary. The rational function permits exact arbitrary-\(k\) coefficient extraction and refines the known shortest-absence count. It is not a claimed downstream theorem for unrestricted words.

## Scientific limits

Only words of the form \((012)^k\) are covered. The generated certificate is an exact symbolic finite identity, not independent external validation. Bibliographic novelty is qualified by possible unindexed sources and one inaccessible full text.

Self-review: passed. Independent audit: not yet performed.
