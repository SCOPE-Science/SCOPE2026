# Four optimal binary three-message variable-length non-overlapping codes

## Finding

For exactly three binary source messages represented by a **strong variable-length non-overlapping code**, the minimum total codeword length is \(16\), or mean \(16/3\) under a uniform message distribution. Exactly four unordered codebooks attain it. The two optimal codebooks whose words start in \(0\) and end in \(1\) are

- `00011`, `01011`, `010011`;
- `00101`, `00111`, `001101`.

The other two are their bitwise complements. All four belong to one symmetry orbit under reversal and complementation, and have length multiset \(\{5,5,6\}\). A fixed-length three-word binary non-overlapping code exists at length \(6\), so this exact result saves \(2/3\) of a bit per uniformly chosen message compared with using three equal-length-six codewords.

## Assumptions and scope

A code is a set \(S\subseteq\bigcup_{\ell\ge2}\{0,1\}^{\ell}\) with three **distinct** words. For every pair \(u,v\in S\), possibly equal, and every \(1\le k<\min\{|u|,|v|\}\), their length-\(k\) prefix/suffix comparisons never agree crosswise; when distinct lengths occur, full-length prefix/suffix agreement is already excluded by the factor condition. For any distinct \(u,v\in S\), neither is a contiguous factor (substring) of the other. These are the two conditions in the strong variable-length non-overlapping convention of Wang and Wang. In particular, the factor prohibition is **essential**: Bilotta's weaker cross-fix-free definition alone does not imply this theorem. Codewords are labeled only by their binary content; the three messages are equiprobable for the average-length interpretation.

## Proof

1. **Common orientation.** An unbordered binary word of length at least two begins and ends with different bits. If two codewords had different start bits, the first bit of either would equal the last bit of the other, violating the one-bit prefix/suffix condition. Therefore every word has the same orientation. Complement the alphabet, if necessary, so that all words begin in \(0\) and end in \(1\).

2. **No word shorter than four can occur.** The only oriented length-two word is `01`; every word beginning in `0` and ending in `1` contains `01` as a factor. The length-three words are `001` and `011`. If `001` belongs to a code, another word cannot start `01` (it would overlap the suffix `01` of `001`); hence it must start `00`, and its first transition to `1` contains `001` as a factor. If `011` belongs to a code, another word cannot end `01` (overlap with the prefix `01` of `011`); hence it must end `11`, and its last transition from `0` contains `011` as a factor. Therefore no code of three words can contain a word of length at most three.

3. **Length-four obstruction.** There are three oriented unbordered length-four words, `0001`, `0011`, `0111`. The first and last cannot coexist with any second oriented word: the first forces the second word to begin with at least `000`, yielding a `0001` factor at its first transition; the last follows by reverse-complement symmetry. Thus if a code contains length four, that word is `0011`. Exhaustive comparisons over the only oriented unbordered words of lengths five, six, and seven yield precisely these compatible candidates:

   - length five: `00101`, `01011`;
   - length six: `000101`, `001011`, `010111`;
   - length seven: `0000101`, `0001011`, `0010101`, `0010111`, `0101011`, `0101111`.

   The two length-five candidates conflict with each other and with **each** of the three length-six and six length-seven candidates; the three length-six candidates conflict pairwise. Hence no length profile \((4,5,5)\), \((4,5,6)\), \((4,5,7)\), or \((4,6,6)\) is feasible. No profile with two length-four words is feasible either. These are all possibilities with a length-four word and total length at most \(16\).

4. **Length-five boundary and enumeration.** When all word lengths are at least five and the total is at most \(16\), only \((5,5,5)\) and \((5,5,6)\) are possible. Of the six oriented unbordered length-five words, the compatible pairs are exactly

   `00011`–`00101`, `00011`–`01011`, `00101`–`00111`, `00111`–`01011`.

   They form a four-cycle, so no three length-five words are compatible. Testing the ten oriented unbordered length-six words against the four pairs yields exactly two triples, the two listed in the Finding. Each passes all comparisons and the factor-free test. Complementation doubles the count to four; reversal takes one oriented optimum to the complement of the other, establishing one symmetry orbit.

This proves the lower bound, attainability, and complete equality classification; no bounded-length assumption is needed, since shorter configurations are excluded by an exhaustive list of all possible length profiles up to total \(16\).

## Verification

Run `python3 verify.py` and `python3 crosscheck.py` using only the Python 3 standard library. The first regenerates oriented unbordered words of lengths four through seven, independently checks every pair and every feasible short length profile, and obtains two oriented and four total equality codebooks. The second directly enumerates **all** binary length triples with sum at most \(16\), including lengths as large as \(12\), with a separate conflict predicate, and produces precisely four solutions of profile \((5,5,6)\). Both scripts run without random inputs or external downloads. Output from the packaged scripts was `PASS` in both cases.

## Relationship to prior work

Bilotta (2016) introduces variable-length cross-fix-free codes and distinguishes the stronger factor-free subclass, but gives constructions and cardinality recurrences rather than this three-message minimum total length. Blackburn (2013/2015) studies fixed-length maximum cardinality, exhibiting a three-word code of length six; this proves an upper bound of \(18\) for our objective, not the exact value \(16\). Wang and Wang (2021) analyze non-overlapping codes with the explicit factor restriction, including binary fixed-length-six examples, but do not determine this exact average-length invariant. Wang and Wang (2024), Section 4, explicitly pose minimization of average word length and establish broad bounds; their lower bound does not imply \(16/3\). Existing public finite maximum-code tables for binary length five show only that no three-codeword code fits entirely at length five; they do not classify mixed-length equality.

## Limitations

This exact threshold is confined to three equiprobable binary messages and the strong factor-free definition. It does not apply to the weaker cross-fix-free convention if factors are allowed, nonuniform message distributions, four or more messages, or higher alphabets. Source comparisons support but cannot guarantee historical novelty; no independent mathematical audit has been performed.

## References

- S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026 (first posted 2013-03-05), https://arxiv.org/abs/1303.1026.
- S. Bilotta, *Variable-length Non-overlapping Codes*, arXiv:1605.03785 (first posted 2016-05-12), https://arxiv.org/abs/1605.03785.
- G. Wang and Q. Wang, *Q-ary non-overlapping codes: a generating function approach*, arXiv:2108.06934 (2021), https://arxiv.org/html/2108.06934v1.
- G. Wang and Q. Wang, *On the maximum size of variable-length non-overlapping codes*, arXiv:2402.18896 (2024), especially Section 4, https://arxiv.org/abs/2402.18896.

