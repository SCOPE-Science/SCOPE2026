# Scientific review: a sharp palindrome reconstruction threshold

## Correctness — PASS

The claim is exactly that the full contiguous \(k\)-Abelian factor-count fingerprint distinguishes ordinary palindromes at all lengths \(1\le n\le3k\) for every \(k\ge1\), and fails at \(n=3k+1\) over any alphabet containing two letters. For \(n\le k\), the complete word occurs among the counted factors. For longer words, factor incidence recovers the common prefix of length \(k-1\), reversal symmetry makes the centered length-\(k\) or length-\((k-1)\) factor the unique odd-multiplicity palindrome factor of that length, and the bound \(n\le3k\) leaves at most one mirrored letter pair. Single-letter counts recover the last pair. The explicit two-one palindromes at the claimed boundary have identical factors at every length at most \(k\), as proved by a direct positional count. Both independent, executable finite checks passed; the all-parameter conclusion relies on the symbolic proof, not these tests.

## Originality — PASS, qualified

The 2011 and 2013 foundational sources define \(k\)-Abelian equivalence. The 2013 paper's sharp unrestricted length-\(2k\) ambiguity theorem does not claim the palindrome-specific length-\(3k+1\) threshold. The 2016 class-cardinality paper analyzes unrestricted switchings and classes; its inspected sections do not supply the present reversal-fixed reconstruction result. The 2014 palindromic rich/poor article, its related presentation, and the 2018 follow-up concern words equivalent to their own reversal and counts of such factors; those questions do not imply reconstruction injectivity among two different ordinary palindromes. A prior fixed-order result establishes the \(k=3\) first-collision length ten (with a stronger fixed-order fiber census), so that isolated case is not new; the present uniform theorem for **every positive \(k\)** is its substantive extension. The separate published sparse-marker three-mer census concerns only fixed factor length three. Indexed scientific-record searches for the universal threshold, the parity-centered decoder, and the explicit family found no broader covering assertion.

A complete guarantee against unindexed earlier statements is not possible. The full 2014 proceedings text was inaccessible, though its abstract and a related scientific presentation were inspected. The 2018 article's abstract and the related presentation were examined; overlapping content outside those accessible materials remains a residual risk. This qualification is not a claim of formally certified originality.

## Value — PASS

The exact first-ambiguity threshold gives an all-order reconstruction boundary for a natural reflection-symmetric data source, improving the usual unrestricted shortest-ambiguity scale. The parity-of-central-factor argument yields an explicit decoder using only observed multiplicities; the sharpness construction isolates the first genuine information loss. This supplies a reusable structural lemma for palindrome-restricted string reconstruction and a benchmark across all read lengths, rather than a special-case census or routine numerical increment. No statement beyond the palindromic domain is made.

## Sources and limitations

Closest primary sources: Huova–Karhumäki (2011), arXiv:1104.4273; Karhumäki–Saarela–Zamboni (2013), arXiv:1301.5104, particularly its Section 2; Karhumäki–Puzynina–Rao–Whiteland (2016), arXiv:1605.03319, particularly Sections 3–4; Karhumäki–Puzynina (DLT 2014); Cassaigne–Karhumäki–Puzynina (2018) and its related public scientific presentation. For finite verification use `check_exhaustive.py` and `check_decoder.py`. The proof applies to contiguous factor multiplicities, not unordered sets of factors or scattered reads. No claim is made about the complete collision spectrum above the threshold. Research limitations in `RESULT.md` are integral to this assessment.

Self-review: passed. Independent audit: not yet performed.
