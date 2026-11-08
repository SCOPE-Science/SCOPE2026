# Scientific review

## Correctness — PASS

For any prescribed quadruple the fourth-order character indicator expands into the exactly counted supports of size one to four. The complete sums obey the standard non-fourth-power multiplicative-character bound \((r-1)\sqrt p\), the single-factor sum vanishes, and at most \(4-r\) omitted non-root terms need correction. The resulting bound is \(256N_p\ge p-513\sqrt p-256\). Its right side is positive from \(p=263681\), by the exact inequality \((263681-256)^2-513^2\cdot263681=65536>0\). The remaining finite interval is **exhaustively** checked by standard-library C++17 for every one of the \(11538\) eligible primes, with exact full-word bitmaps. A second construction directly from fourth powers checks all \(269\) eligible primes through \(4000\). Exact verification depends on the bundled replayable code and source-theory bound; finite testing is not substituted for the latter.

## Originality — PASS within inspected evidence

The 2020 Su–Zhang paper (DOI 10.3390/math8081337) treats special quartic conditions built from \(a\pm a^{-1}\); the full article's theorems and argument do not classify all four consecutive coset labels. Graham's 1964 theorem describes unbounded least starting positions for four identical power-residue labels as the prime varies, not eventual simultaneous occurrence of all 256 patterns. Rabung–Jordan's 1970 full article studies earliest monochromatic runs in one power class (explicit \(A^*(8,2)\) and \(A^*(3,3)\)). An earlier complete *three*-label quartic classification does not imply four-label coverage, and the mixed last exception here is genuinely different from the three-label final all-zero exception. Targeted mathematical-index, original-literature, and actual research-record queries identified no covering statement. **Risk:** the 1983 Lehmer article concerns prescribed residue patterns and its full text could not be inspected; a secondary review points to least all-residue occurrences rather than the mixed-pattern cutoff, but unindexed or inaccessible prior work might still cover part of this claim. A failed search is not treated as proof of novelty.

## Mathematical value — PASS

Simultaneous realization of all quartic-coset words is a canonical finite-word invariant, not a free choice of parameters: four successive positions give the full natural \(4^4\)-word spectrum. The exact sharp prime threshold and exceptional-prime census answer a meaningful finite cut-off question. A structural contrast occurs at the terminal exception: the length-three theorem's last defect is all-residue, whereas the length-four theorem's last defect is mixed, persisting after four consecutive quartic residues are already guaranteed. The explicit finite cutoff is not supplied by general asymptotic existence theorems or by the known length-three result. The contribution is the complete exact classification and new terminal mixed obstruction, not the underlying classical Weil method.

## Limits and closest literature

No least starting-position bound, counts for every individual word, or statement on lengths five and above is claimed. Graham (1964), Rabung–Jordan (1970), Su–Zhang (2020), and the inaccessible Lehmer (1983) are compared in `RESULT.md` and `AUDIT.json`. The exhaustive finite computation is reproducible but has not received an independent external scientific audit.

Self-review: passed. Independent audit: not yet performed.
