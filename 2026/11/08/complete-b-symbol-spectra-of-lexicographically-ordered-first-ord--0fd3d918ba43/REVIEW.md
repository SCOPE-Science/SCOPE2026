# Self-review

## Correctness — PASS

The claim concerns every integer \(m\ge2\), every cyclic window size \(1\le b\le 2^m\), and all \(2^{m+1}\) affine evaluation words in the fixed increasing-binary coordinate order. The proof checks normalization and constants, counts cyclic transitions by binary carries, uses an invertible prefix-parity change of variables to establish exact run multiplicities, proves that the zero-run multiset is forced by the transition count, and sums all-zero windows over those runs. The dyadic splitting argument proves that nonfull weights are strictly distinct, rather than inferring this from experiments. The separate \(b=1\) formula and saturation at the greatest dyadic \(K\) with \(Kb\le n\) handle the boundaries. Direct word-bit verification passed 2,280 configurations, 1,067,680 individual cyclic-window weights, and 1,020 complete enumerator comparisons. It does not replace the infinite proof.

## Originality — PASS, with bibliographic limitations

Pan–Ling–Liu's arXiv:2309.08920v1, Theorem 4.6, gives the minimum \(b\)-symbol distance, which is a consequence of the smallest nonzero exponent here, not the full distribution. Ma–Luo's arXiv:1911.02184, Section 4, gives complete window-weight results for cyclic/modified simplex codes with different lengths and coordinate orderings; they identify order sensitivity, not the present affine ordered full-length spectrum. Vega's 2023 Theorems 3–4 cover semiprimitive irreducible cyclic codes of lengths coprime to their field sizes; they do not contain the binary power-of-two length code. Zhu–Shi's arXiv:2112.04019 treats Kasami codes. Relevant mathematical-record searches for Reed–Muller, affine Boolean truth tables, Hadamard and symbol-pair enumerators returned no equivalent all-window theorem; the closest records concerned the PIR multiplicity of \(\mathrm{RM}_2(1,m)\), individual cyclic symbol-pair code constructions, and unrelated rank profiles. These comparisons do not prove that an unindexed or differently expressed identity is absent. The established Hamming enumerator and known minimum distances are attributed, not claimed as novel.

## Mathematical value — PASS

The exact all-window weight enumerators of a classical code provide complete pair- and window-read error spectra, refining literature that primarily obtains minimum distances. A structural theorem unexpectedly shows that a single transition count fixes the entire zero-run length multiset, and all nonsaturated nonzero weights have uniform multiplicity four. The result covers an unbounded natural family and all window widths, not an arbitrary finite slice or a standard Hamming-weight substitution. Sensitivity to coordinate order is explicit.

## Limitations and further checks

The analysis does not extend to other coordinate permutations, nonbinary alphabets, higher-order Reed–Muller codes or arbitrary simplex codes. It has not undergone independent mathematical validation. The residual originality risk is an equivalent run-length statement in the literature on binary affine truth tables or Walsh/Hadamard sequences under another name.

Self-review: passed. Independent audit: not yet performed.
