# Exact binary language with five scattered copies of \(0011\)

## Finding

For a finite binary word \(w\), let \(c_{0011}(w)\) be the number of strictly increasing quadruples of positions spelling \(0011\); occurrences are counted with multiplicity even when they spell the same word. The full language with exactly five such occurrences is
\[
\{w:c_{0011}(w)=5\}=\{1^u0\,1^v0101\,0^s1\,0^t:u,v,s,t\in\mathbb Z_{\geq0}\}.
\]
In particular, for the number \(B_{0011}(n,5)\) of binary length-\(n\) words in this language,
\[
B_{0011}(n,5)=\begin{cases}0,&0\leq n<6,\\\binom{n-3}{3},&n\geq6,\end{cases}
\qquad\sum_{n\geq0}B_{0011}(n,5)z^n=\frac{z^6}{(1-z)^4}.
\]
The word \(001011\) is the unique primitive core: every one of its six symbols participates in at least one \(0011\) occurrence, and all other letters in an accepted word are of four explicitly irrelevant kinds. The regular expression above is unambiguous.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), words are finite, and scattered occurrences (not contiguous factors and not distinct subsequence strings) are counted. Empty words and words of length less than six have count zero at frequency five. Indices are strictly increasing; no cyclic wraparound is permitted. The integers \(u,v,s,t\) independently range over all nonnegative values.

## Proof

**Step 1: remove exactly four classes of unused letters.** Suppose \(c_{0011}(w)>0\). Let \(z_1<z_2\) be the first two zero positions and \(o_{-2}<o_{-1}\) the last two one positions. Existence of a \(0011\) occurrence implies \(z_2<o_{-2}\). No one before \(z_2\) can participate in a \(0011\) occurrence: fewer than two zeros precede it. No zero after \(o_{-2}\) can participate: fewer than two ones follow it. Thus deleting all ones before \(z_2\) and all zeros after \(o_{-2}\) leaves the value of \(c_{0011}\) unchanged. The deleted letters occupy exactly four disjoint zones: (i) ones before the first zero; (ii) ones between the first two zeros; (iii) zeros between the last two ones; (iv) zeros after the last one.

Write the remaining word \(v\). It begins with \(00\) and ends with \(11\). Moreover every position of \(v\) is used in an occurrence of \(0011\): for any zero, choose it and one of the first two zeros as the pair, followed by the final two ones; for any one, choose the first two zeros, then this one and one of the last two ones, respecting their order. In the endpoint cases use the other member of the corresponding first/last pair. Hence every symbol of \(v\) is *active*.

**Step 2: the core cannot be monotone.** If \(v\) has no inversion (a one followed later by a zero), then \(v=0^a1^b\) for integers \(a,b\geq2\), and
\[
c_{0011}(v)=\binom a2\binom b2.
\]
The positive triangular numbers start \(1,3,6,10,\ldots\), so their product cannot be \(5\). Therefore when \(c_{0011}(v)=5\), the word \(v\) contains an inversion.

**Step 3: five forces the unique core.** Choose any inverted one-zero pair in \(v\). Because \(v\) starts with \(00\) and ends with \(11\), these two letters occur strictly between the first two zeros and the last two ones. Together they exhibit \(001011\) as a scattered subsequence of \(v\). The six-letter word \(001011\) contains exactly five \(0011\) occurrences: the pair of initial zeros admits \(\binom32=3\) choices of later ones, and each of the other two zero pairs admits exactly one, giving \(3+1+1=5\). If \(v\) had any additional position, that position would be active by Step 1, supplying at least one further occurrence not contained in the selected six positions. This would yield at least six occurrences, a contradiction. Hence \(v=001011\).

**Step 4: reconstruct and enumerate.** Reinsert arbitrary initial ones, arbitrary ones between the first two core zeros, arbitrary zeros between the final two core ones, and arbitrary final zeros. Every inserted letter remains unused, so no occurrence count changes. Precisely these insertions produce \(w=1^u0\,1^v0101\,0^s1\,0^t\). The four lengths are uniquely recoverable from the first two zeros and last two ones. For length \(n\geq6\), the equation \(u+v+s+t=n-6\) has \(\binom{n-3}{3}\) solutions. Summing gives the stated generating function. This proves both directions for all finite binary words.

## Verification

Run `python3 checker.py` using Python 3 and no external packages. This independently compares the regular-language parser against a running subsequence-count recurrence for all \(2^{15}-1=32767\) binary words of lengths zero through fourteen, compares with literal quadruple enumeration through length eleven, checks 4096 parameter tuples, and matches the counting formula against an independent truncated-state transfer recurrence for 50 lengths. The executable checks confirm boundary cases but are not used to extrapolate the infinite theorem; Steps 1–4 provide the full proof.

## Relationship to prior work

Bruda (initial arXiv submission June 30, 2026) establishes eventual polynomiality and a degree bound for fixed nonzero binary subsequence frequency, and expressly identifies \(p=0011\), \(k=5\) as an exception to previously proposed sufficient criteria for obtaining the maximal degree. That already covers the *existence of the exceptional maximal degree*, which is not claimed new here. The new object is the complete unambiguous regular-language classification and its exact, all-length binomial count. Menon–Singh give detailed formulas for frequencies up to four, but not this frequency-five language. Tian supplies a general primitive-word framework and an algorithmic expression for arbitrary frequencies; the present proof evaluates the first exceptional case by identifying its unique active core and four free insertion regions. General enumeration mechanisms potentially recover the answer through specialization; this is a priority risk, not an assertion that the general mechanisms are absent. Reversing or complementing the alphabet maps the result to the corresponding pattern \(1100\), and these relabelings are not counted as distinct results.

## Limitations

This is a statement for the single pattern \(0011\) at multiplicity five. It does not classify all frequencies, arbitrary patterns, or contiguous occurrences. The independent scientific audit is not performed. Broader algorithmic methods and an unindexed earlier explicit specialization could diminish novelty, although the exact language/formula was not located in inspected source material.

## References

- G. Bruda, *Enumerating binary words restricted by subsequence frequency*, arXiv:2607.02578 (first submitted June 30, 2026), https://arxiv.org/abs/2607.02578, Theorem 1.4 and Section 4.2.
- K. Menon and A. Singh, *Subsequence frequency in binary words*, arXiv:2306.07870 (first submitted June 13, 2023), https://arxiv.org/abs/2306.07870, Section 3.
- R. Tian, *Counting occurrences of a pattern in a binary word*, arXiv:2507.03205 (first submitted July 3, 2025), https://arxiv.org/html/2507.03205v1, Section 5.2.
