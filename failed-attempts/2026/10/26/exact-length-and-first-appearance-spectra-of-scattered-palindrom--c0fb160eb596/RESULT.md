# Exact length and first-appearance spectra of scattered palindromes in alternating binary words

## Finding

Let \(A_n=0101\cdots\) denote the length-\(n\) prefix of the one-sided infinite alternating binary word, for each integer \(n\geq0\). Let \(P_{n,k}\) count the **distinct** nonempty binary palindromes of length \(k\) occurring as scattered subsequences of \(A_n\); an occurrence is not counted again when it admits multiple embeddings. Define \(e(p)\) as the least \(n\) for which the palindrome \(p\) occurs in \(A_n\). Then the complete joint generating function for first-appearance position and palindrome length is

\[
H(x,y)=\sum_{\substack{p\in\{0,1\}^{+}\\p=p^R}}x^{e(p)}y^{|p|}
=\frac{(1+x)(xy+x^3y^2)}{1-x^2y^2-x^4y^2}.
\]

Equivalently, the full length-refined prefix spectrum is

\[
\sum_{n\geq0}\sum_{k\geq1}P_{n,k}x^ny^k
=\frac{(1+x)(xy+x^3y^2)}{(1-x)(1-x^2y^2-x^4y^2)}.
\]

Explicitly, for integers \(n\geq0\) and \(h\geq0\),

\[
P_{n,2h+1}=\sum_{b=0}^{1}\sum_{j=0}^{h}\binom hj\mathbf1\{2h+1+2j+b\leq n\},
\]

and for \(h\geq1\),

\[
P_{n,2h}=\sum_{b=0}^{1}\sum_{j=0}^{h-1}\binom{h-1}{j}\mathbf1\{2h+1+2j+b\leq n\}.
\]

These formulas also specify, by replacing each inequality with equality, the exact number of new distinct palindromes of each length when one letter is appended to an alternating prefix. This is the length-resolved and first-appearance claim, not a claim of a new univariate counting sequence or an unconditional extremal theorem for all binary words.

## Assumptions and scope

A scattered subsequence is obtained by deleting zero or more symbols without changing the order of retained symbols. A palindrome is a nonempty finite word equal to its reversal. The first symbol of \(A_n\) is \(0\); switching both binary labels preserves all counts. Formal generating functions have integer coefficients; they are identities in \(\mathbb Z[[x,y]]\). All lengths and prefix positions are integers in the ranges stated; an empty prefix contains no nonempty palindrome.

## Proof

**1. Exact first embedding.** For any nonempty binary word \(u=u_1\cdots u_k\), let \(b=u_1\in\{0,1\}\) and \(r(u)=|\{i:1\leq i<k,\ u_i=u_{i+1}\}|\). Its left-to-right greedy embedding into the infinite alternator begins at position \(1+b\). If consecutive symbols differ, the next symbol is at the very next position; if they agree, the next occurrence of that symbol is two positions later. Therefore its greedy embedding ends at exactly

\[
e(u)=k+r(u)+b.\]

Greedy selection of each next occurrence is pointwise no later than any other embedding, by induction on the symbol index, so this endpoint is the **minimum** prefix length containing \(u\). In particular \(u\) is a scattered subsequence of \(A_n\) if and only if \(e(u)\leq n\).

**2. Palindromic symmetry.** For an odd-length palindrome \(p\) of length \(2h+1\), the \(h\) adjacent-equality flags in the first half are repeated in reverse order after the central symbol. Hence \(r(p)=2j\) when exactly \(j\) of these \(h\) flags indicate equality. Once the initial bit \(b\) and these \(h\) flags are specified, every symbol of \(p\) is uniquely determined; there are \(\binom hj\) choices of flags with \(j\) equalities. Thus

\[
e(p)=2h+1+2j+b\quad\text{with multiplicity }\binom hj.\]

For an even-length palindrome of length \(2h\), the central pair always agrees, and the \(h-1\) flags to its left are mirrored. Consequently \(r(p)=2j+1\), with multiplicity \(\binom{h-1}{j}\), and

\[
e(p)=2h+1+2j+b.\]

The initial bit and the equality-flag pattern are a bijective encoding, so the multiplicities enumerate **different palindromes**, not embeddings. Restricting the exact endpoint to \(e(p)\leq n\) proves both stated binomial sums for \(P_{n,k}\).

**3. Bivariate summation.** Summing by initial bit, half-length, and equality flags gives an odd-length contribution

\[
H_{\mathrm{odd}}(x,y)
=(1+x)xy\sum_{h\geq0}\bigl[x^2y^2(1+x^2)\bigr]^h
=\frac{(1+x)xy}{1-x^2y^2(1+x^2)},
\]

and an even-length contribution

\[
H_{\mathrm{even}}(x,y)
=(1+x)x^3y^2\sum_{h\geq1}\bigl[x^2y^2(1+x^2)\bigr]^{h-1}
=\frac{(1+x)x^3y^2}{1-x^2y^2(1+x^2)}.
\]

Adding these series proves the displayed formula for \(H\). Every fixed palindrome enters exactly once, at prefix length \(e(p)\), and remains present in all later prefixes; summing \(\sum_{n\geq e(p)}x^n=x^{e(p)}/(1-x)\) proves the cumulative formula.

**4. A sharp threshold for the complete palindrome language of fixed length.** For every \(k\geq1\), the maximum first-appearance endpoint among all binary length-\(k\) palindromes is \(2k\), attained by \(1^k\). At prefix length \(2k-1\), every such palindrome except \(1^k\) occurs. This follows directly from \(e(p)=k+r(p)+b\), with \(r(p)\leq k-1\); equality in \(e(p)=2k\) forces \(b=1\) and all adjacent letters equal.

## Verification

The standalone standard-library script `verify.py` checks the exact binomial spectrum against independent explicit enumeration of all binary palindromes through prefix length \(21\), obtains the bivariate generating-function coefficients independently from its polynomial recurrence through prefix length \(150\), and compares cumulative totals with a separate dynamic program for distinct palindromic subsequences through length \(150\). Its expected success line is

`ALTERNATING_SCATTERED_PALINDROME_PASS brute_n=1..21 exact_spectrum_n=0..150 independent_interval_dp_n=0..150 rational_2d_coefficients_n=0..150`.

The first ten positive-length cumulative counts are \(1,2,4,6,9,12,17,22,30,38\). Finite checks corroborate but are not used to infer the all-length identities, which follow from the bijective argument above.

## Relationship to prior work

Mahalingam and Pandoh (2021) develop general upper bounds for distinct scattered palindromes and conjecture the maximum over words of a given length and alphabet size (Conjecture 5.6). Their Table 4 gives the binary maxima through length ten, matching the alternating-word totals above, but neither the full length-specific spectrum nor the first-occurrence bivariate formula is stated there. The present theorem **does not establish** that alternating words maximize the count for arbitrary lengths.

Holub and Saari (2009) investigate reconstruction from palindromic scattered subwords, minimal-palindromic words, and shortest minimal-palindromic extensions; their different invariants do not furnish this joint census. OEIS A238374 records exactly the **univariate** scalar sequence and generating function obtained by setting \(y=1\) in the prefix series (up to its index shift). That scalar sequence is prior knowledge and is not claimed as original here: the contribution is the full extra palindrome-length grading, individual first-appearance multiplicities, and the explicit bijective explanation. Related OEIS A204026 has the same row sums but is a Fibonacci matrix antidiagonal, not the present palindrome-length distribution.

## Limitations

This result is restricted to the alternating binary word family and its prefixes. It neither proves the global binary extremal conjecture nor counts occurrence multiplicities, only distinct palindromic subsequence strings. The univariate counts and their rational generating function are already recorded in OEIS; no novelty is claimed for them. Independent mathematical validation has not been carried out. The possibility that the new bivariate refinement has appeared under another terminology remains an originality risk.

## References

- K. Mahalingam and P. Pandoh, *Counting scattered palindromes in a finite word*, arXiv:2108.02729, first posted 5 August 2021, https://arxiv.org/abs/2108.02729 .
- Š. Holub and K. Saari, *On highly palindromic words*, Discrete Applied Mathematics 157 (2009), 953–959, https://www.karlin.mff.cuni.cz/~holub/soubory/subpal.pdf .
- OEIS A238374, row sums of A204026, https://oeis.org/A238374 ; OEIS A204026, https://oeis.org/A204026 .
