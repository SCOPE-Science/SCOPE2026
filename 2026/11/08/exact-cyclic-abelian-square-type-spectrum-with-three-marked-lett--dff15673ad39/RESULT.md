# Exact cyclic Abelian-square type spectrum with three marked letters

## Finding

Let \(w\) be a binary circular word of **odd** length \(n\ge 3\), with exactly three symbols \(0\). Write \(g_1,g_2,g_3\ge 1\) for the positive distances from each zero to the next zero in cyclic order, so \(g_1+g_2+g_3=n\). Set \(K=(n-1)/2\), and order the three distances as \(a\le b\le c\). For each half-length \(1\le m\le K\), let \(z_m(w)\) be the number of equivalence classes of cyclic Abelian-square factors of length \(2m\), where the class of a square is determined by \(m\) and the number of zeros in either length-\(m\) half. Put \(N(w)=\sum_{m=1}^Kz_m(w)\).

**Exact type classification.** All possible types have zero-count \(j\in\{0,1\}\). Type \((m,0)\) occurs exactly when \(2m\le c-1\). Type \((m,1)\) occurs exactly when at least one cyclic index \(i\in\{1,2,3\}\) satisfies
\[
\left\lfloor\frac{g_i}{2}\right\rfloor+1\le m\le
\min\bigl(K,\,g_i+\min(g_{i+1},g_{i+2})-1\bigr),
\]
where the subscripts on \(g\) are read modulo three.

**Closed cardinality formula.** For every such word,
\[
\boxed{N(w)=K-\mathbf 1_{\{2\mid c\}}+
\max\left(0,\min\left(K,a+b-1,\left\lfloor\frac c2\right\rfloor\right)-\left\lfloor\frac a2\right\rfloor\right).}
\]
Here the indicator is one when \(c\) is even and zero otherwise.

**Every prefix inequality.** For each \(1\le k\le K\),
\[
\boxed{\sum_{m=1}^{k}z_m(w)\ge k.}
\]
By exchanging the two letters, both results hold identically for binary circular words with exactly three ones. In particular, these infinite families satisfy the full prefix-strengthened odd-length conjecture about non-equivalent Abelian squares.

## Assumptions and scope

A *circular factor* of length \(L\le n\) means \(L\) consecutive symbols read cyclically, without reusing a position. An *Abelian square* of half-length \(m\) is a factor of length \(2m\) whose first and second halves have the same number of each letter. Two Abelian squares are equivalent exactly when their half-length and their common half-Parikh vector agree; the count is of types, not distinct factor strings or individual occurrences. The three zeros may be adjacent; all cyclic gaps remain positive. No condition is imposed on the three positive gaps beyond having odd sum. We use one-based half-lengths and zero-based positions in the checker.

## Proof

**1. Only two types are possible.** Since \(2m\le n-1\) and the circle contains exactly three zeros, an Abelian square can contain either zero or two zeros, never four. Equal half-counts therefore force the number of zeros in each half to be \(j=0\) or \(j=1\). A type \((m,0)\) requires \(2m\) consecutive ones. The longest run of ones has length \(c-1\), giving the first criterion.

**2. A necessary and sufficient interval for each ordered pair of zeros.** For a type \((m,1)\), choose the zero belonging to the first half and the next zero in the forward direction belonging to the second half. They are consecutive among the three circular zeros. Lift their coordinates to \(0\) and \(g\), and write the preceding and following zero positions as \(-j\) and \(g+h\) respectively, with \(g,j,h\ge1\) and \(g+j+h=n\). The start position \(s\) of an admissible factor must satisfy: the first chosen zero is in its first half, the second in its second half, and neither other zero belongs to the factor. These conditions are precisely
\[
\max\{1-j,1-m,g-2m+1\}\le s\le
\min\{0,g-m,g+h-2m\}.
\]
All six endpoints are integers, so such an \(s\) exists if and only if every lower endpoint is at most every upper endpoint. The nonautomatic comparisons reduce to
\[
2m\ge g+1,\qquad m\le g+j-1,\qquad m\le g+h-1,\qquad 2m\le n-1.
\]
For positive integer \(m\), these are equivalent to
\[
\left\lfloor\frac g2\right\rfloor+1\le m\le
\min\bigl(K,g+\min(j,h)-1\bigr).
\]
Applying this to each of the three ordered pairs of consecutive zeros proves the exact criterion for type \((m,1)\). Conversely, every square with one zero in each half selects just such a consecutive pair, so the criterion is exhaustive.

**3. Union of three integer intervals.** Sort the cyclic gaps as \(a\le b\le c\). The intervals supplied by gaps \(a\) and \(b\) have the same upper endpoint \(\min(K,a+b-1)\), and the one associated to \(b\) has a no-smaller lower endpoint; hence the \(b\)-interval is contained in the \(a\)-interval. The interval supplied by \(c\) reaches \(K\) because
\[
2(c+a-1)-(n-1)=c+a-b-1\ge0.
\]
Thus the complete collection of \((m,1)\) types is the union
\[
I_a=\left[\left\lfloor\frac a2\right\rfloor+1,\ \min(K,a+b-1)\right]\cap\mathbb Z,
\quad
I_c=\left[\left\lfloor\frac c2\right\rfloor+1,\ K\right]\cap\mathbb Z,
\]
with empty intervals permitted. The \((m,0)\) types occupy \(1\le m\le\lfloor(c-1)/2\rfloor\). For odd \(c\), these and \(I_c\) provide exactly one baseline type at every half-length. For even \(c\), they provide exactly one baseline type except at \(m=c/2\), where there is none. In either case, the extra types supplied by \(I_a\) are precisely its indices \(m\le\lfloor c/2\rfloor\). Their number is
\[
\max\left(0,\min\left(K,a+b-1,\left\lfloor\frac c2\right\rfloor\right)-\left\lfloor\frac a2\right\rfloor\right).
\]
Adding this count to the baseline proves the boxed closed formula.

**4. The prefix inequalities.** If \(c\) is odd, the baseline above contributes one type at every \(m\), so every prefix sum is at least its number of half-lengths. Suppose \(c=2t\) is even. The baseline contributes one type for every \(m\ne t\) and none at \(m=t\). Since \(n=a+b+c\) is odd, not all three gaps can equal even \(c\); thus \(a<c=2t\), and
\[
\left\lfloor\frac a2\right\rfloor+1\le t.
\]
Also \(a+b-1\ge\lfloor a/2\rfloor+1\) for all positive \(a,b\), and \(K\ge t\). Consequently the nonempty interval \(I_a\) contains an index \(m\le t\), providing one additional type in the first \(t\) positions. For prefixes ending before \(t\), the baseline already contains one per index. For prefixes ending at or after \(t\), the baseline has lost exactly one type and the extra type from \(I_a\) compensates. Hence \(\sum_{m=1}^{k}z_m(w)\ge k\) for all \(k\). Letter complementation preserves the equal-half condition and type counts, proving the symmetric case. \(\square\)

## Verification

The included dependency-free Python program `verify_threezeros.py` constructs type sets directly from cyclic factors and independently from the three-gap intervals, compares both for every three-zero binary word of every odd length \(3,5,\ldots,29\) (14,665 cases), checks every claimed prefix inequality, tests the closed formula, and performs 250 additional reproducible random positive-gap checks (lengths up to 391). Command: `python3 verify_threezeros.py`. Observed outputs: `EXHAUSTIVE_WORDS_PASS 14665 odd lengths 3..29`, `RANDOM_GAPS_PASS 250 max length 391`, `ALL_TESTS_PASS`. These are finite cross-checks, not an infinite proof; the interval and union arguments above establish the unrestricted statement.

## Relationship to prior work

D. Bhattacharjee, *The minimum number of distinct abelian squares in a binary circular word*, Hexagon preprint hexagon:2610.00473v1 (public October 22, 2026), and expanded version v2 (October 27, 2026), Section 5, define \(z_m\) and conjecture \(\sum_{m=1}^{k}z_m\ge k\) for every odd binary circular word. They verify this computationally through length 27 and prove the first two prefix cases for all odd words. Their Proposition on two runs concerns circular words with a single run of each letter, not three possibly separated isolated zeros; their lower bound for *distinct* squares does not imply the bound for *equivalence classes*. The current classification proves the complete prefix conjecture on an unbounded three-marker family and gives its individual types and closed count.

The earlier circular theorem of Fraenkel, Simpson and Paterson bounds the number of non-equivalent types only by \(\lfloor(n+1)/4\rfloor\) in general; it does not imply the stronger bound proved here for this family. Simpson's 2018 survey distinguishes the various counts. Fazekas, Mammoliti, Mercaş and Simpson study sparse-letter conditions in *linear* words; closing a word into a circle changes its set of eligible factors, and their lower-bound statement does not supply this exact circular spectrum.

## Limitations

No statement is established for arbitrary circular binary words, even lengths, or four or more marked letters. The exact formula depends on **three** cyclic gaps. Historical priority against unindexed proofs of an equivalent gap formula has not been independently settled; general pre-existing interval techniques may shorten the derivation. The finite tests do not certify the infinite theorem. Independent external mathematical review has not been performed.

## References

1. D. Bhattacharjee, *The minimum number of distinct abelian squares in a binary circular word*, Hexagon hexagon:2610.00473v1, October 22, 2026, https://hexagonmath.org/2610.00473v1 ; v2 October 27, 2026, https://hexagonmath.org/2610.00473v2 . The open non-equivalent-type prefix inequality is in Section 5 of v2.
2. J. Simpson, *Solved and unsolved problems about abelian squares*, 2018, arXiv:1802.04481, https://arxiv.org/abs/1802.04481 .
3. A. S. Fraenkel, J. Simpson and M. Paterson, *On weak circular squares in binary words*, CPM 1997, pp. 76–82, https://doi.org/10.1007/3-540-63220-4_51 .
4. S. Z. Fazekas, A. Mammoliti, R. Mercaş and J. Simpson, *Binary words containing few abelian squares*, 2026, arXiv:2604.23188, https://arxiv.org/abs/2604.23188 .
