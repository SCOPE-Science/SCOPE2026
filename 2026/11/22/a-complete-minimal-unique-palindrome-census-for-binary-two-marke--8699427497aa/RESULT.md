# A complete minimal-unique-palindrome census for binary two-marker words

## Finding

For each \(a,b,c\in\mathbb Z_{>0}\), put \(W(a,b,c)=0^a1\,0^b1\,0^c\) and let \(K(a,b,c)\) count its **minimal unique palindromic substrings** (MUPS). An occurrence of a palindrome is unique when its string appears exactly once as a contiguous substring; it is minimal unique palindromic when deleting its outer two letters produces a nonunique palindrome (with the empty interior allowed for lengths one and two).

**Complete list.** Set \(L=\max\{a,b,c\}\), \(u=\min(a,b)\), and \(v=\min(b,c)\). The complete set contains exactly the applicable members of:

1. \(0^L\), if the largest of \(a,b,c\) is attained exactly once;
2. \(0^{v+1}1 0^{v+1}\), centered at the first \(1\), if \(u>v\), or \(0^{u+1}1 0^{u+1}\), centered at the second \(1\), if \(v>u\);
3. \(1 0^b1\), if \(\max(a,c)\ge b\).

Thus, for every positive triple,
\[
K(a,b,c)=\mathbf 1_{\{L\text{ unique among }a,b,c\}}+\mathbf 1_{\{u\ne v\}}+\mathbf 1_{\{\max(a,c)\ge b\}}.
\]
Equivalently,
\[
K(a,b,c)=\begin{cases}1,&a=c,\\3,&a<b<c\text{ or }c<b<a,\\2,&\text{otherwise}.\end{cases}
\]
The sharp maximum is three; its earliest source length is eight, with exactly the two witnesses \((a,b,c)=(1,2,3)\) and \((3,2,1)\).

Let \(g_j(n)\) count the positive triples of word length \(n=a+b+c+2\) with \(K=j\), and \(G_j(z)=\sum_{n\ge5}g_j(n)z^n\). Their exact rational series are
\[
G_1(z)=\frac{z^5}{(1-z)(1-z^2)},\qquad
G_3(z)=\frac{2z^8}{(1-z)(1-z^2)(1-z^3)},
\]
\[
G_2(z)=\frac{z^5}{(1-z)^3}-G_1(z)-G_3(z).
\]
For a uniformly chosen positive triple at length \(n\), the limiting probabilities of \(K=1,2,3\) are respectively \(0,2/3,1/3\), and \(\mathbb E[K]\to7/3\).

## Assumptions and scope

The alphabet is the labeled binary alphabet \(\{0,1\}\), the two occurrences of \(1\) are separated by a nonempty zero run, and both exterior zero runs are nonempty. Substrings are **contiguous**, not scattered. Distinct MUPS strings correspond to distinct occurrences because each occurs once. We count all globally minimal unique palindromes, not just shortest unique palindromes covering a particular interval query. The empty word is conventionally nonunique in any nonempty text, so trimming a length-one or length-two unique palindrome satisfies minimality automatically.

A palindrome \(p\) of length at least three is MUPS exactly when \(p\) occurs once but \(p[2..|p|-1]\), its centrally trimmed palindrome, occurs at least twice. This criterion is equivalent to demanding that no proper palindromic factor be unique: any palindrome proper factor not inside the central trim has its distinct reflection within \(p\).

## Proof

**Exhausting palindrome shapes.** Since \(W\) has exactly two \(1\)-symbols, every nonempty palindromic factor has one of three types: \(0^t\), \(0^t1 0^t\), or \(0^t1 0^b1 0^t\), with \(t\ge0\). In the third case both marked symbols are used, forcing the entire middle gap \(0^b\). There are no further forms.

**Zero-only factors.** A positive \(0^t\) has \(\sum_{r\in\{a,b,c\}}\max(0,r-t+1)\) occurrences. It is unique precisely when \(t=L\) and exactly one run attains \(L\). Under that condition \(L\ge2\), and its shorter central trim \(0^{L-2}\) occurs at least twice (for \(L=2\), the trim is empty). This gives the first member.

**Single-marker factors.** The first \(1\) supports \(0^t1 0^t\) for exactly \(0\le t\le u\), and the second supports it for exactly \(0\le t\le v\). For \(t\ge0\), the factor is unique exactly if \(\min(u,v)<t\le\max(u,v)\). If \(u\ne v\), the unique factor with \(t=\min(u,v)+1\) has an interior that occurs at both markers; every greater \(t\) has a unique interior, so is not minimal. If \(u=v\), none qualifies.

**Two-marker factors.** Each palindrome \(0^t1 0^b1 0^t\) with \(0\le t\le\min(a,c)\) occurs uniquely because it contains both \(1\)-symbols. When \(t\ge1\), the central trim contains both \(1\)-symbols and is itself unique, so these factors are not minimal. When \(t=0\), the trimmed palindrome is \(0^b\): it occurs once in the middle run and additionally in an exterior run exactly if \(\max(a,c)\ge b\). This proves the full list and its three-indicator formula.

**Reducing the indicators.** If \(a=c\), then \(u=v\). When \(b>a\), only the unique largest central zero run contributes; when \(b\le a\), only the two-marker palindrome contributes. Hence \(K=1\). If \(a<c\), the four regimes \(b\le a\), \(a<b<c\), \(b=c\), and \(b>c\) respectively contribute \(2,3,2,2\). Reversing the word exchanges \(a\) and \(c\), completing the case classification.

**Generating functions and limit.** The condition \(K=1\) is \(a=c\), giving \(\sum_{a,b\ge1}z^{2a+b+2}=z^5/((1-z^2)(1-z))\). Each \(K=3\) triple has one of two orientations; the increasing orientation has unique parameters \(a=h\ge1\), \(b=h+s\), \(c=h+s+t\), with \(s,t\ge1\), and length \(3h+2s+t+2\). Summation yields \(G_3\), as claimed. All positive triples give \(\sum_{a,b,c\ge1}z^{a+b+c+2}=z^5/(1-z)^3\), yielding \(G_2\). At each length \(n\), total count is \(\binom{n-3}{2}\); equality \(a=c\) contributes only \(O(n)\) choices. The strict orderings \(a<b<c\) and \(c<b<a\) occupy exactly two of the six ordering regions away from ties, whose contribution is \(O(n)\). Therefore \(g_3(n)/\binom{n-3}{2}\to1/3\) and \(g_2(n)/\binom{n-3}{2}\to2/3\), giving the limiting mean.

## Verification

Two bundled standalone Python 3 checkers use literal occurrence counting and an independently organized palindrome-occurrence index. `verify_mups_bruteforce.py` tested all \(3375\) triples with \(1\le a,b,c\le15\), comparing **every predicted word and interval** against the literal MUPS definition. `verify_mups_census.py` tested all \(17296\) positive triples of lengths \(5\) through \(50\), independently constructing occurrence indices and checking all three generating-function coefficient formulas. Their recorded outputs are supplied as separate text files. These are finite consistency checks only; the all-length theorem is proved above without assuming the computations exhaust infinitely many cases.

## Relationship to prior work

Mieno's *Compact Representation of Maximal Palindromes*, first available as arXiv:2508.14384 on August 20, 2025, and published at CPM 2026, constructs a succinct index for maximal palindromes and internal longest-palindrome queries, rather than enumerating minimal unique palindromic factors for a parametrized sparse family. The full open-access article, including its appendix, was examined for the same combinatorial predicate and parameters. Mieno and Funakoshi's *Data Structures for Computing Unique Palindromes in Static and Non-Static Strings* (arXiv:2204.07327; Algorithmica 2024) treats interval-query SUPS and linear bounds for MUPS; the available abstract does not specify the above sparse-family census. The relevant complete-text comparison for that 2024 article could not be resolved. Earlier enumerations of **ordinary** minimal unique factors for binary two-marker words and of shortest unique palindrome **query answers** use different minimality and output criteria; neither stated result directly implies this complete MUPS list. No priority claim follows from unsuccessful searches alone.

## Limitations

The result requires three positive zero runs and exactly two marked \(1\)-symbols. It does not characterize zero-length exterior gaps, three or more markers, arbitrary alphabets, or interval-specific SUPS answer multiplicities. The novelty comparison is best-knowledge rather than an independent exhaustive publication audit; the full primary text of the 2024 MUPS-related paper was not accessible in this investigation. The proof, not the numerical checks, supports the unbounded-parameter assertion.

## References

1. T. Mieno, *Compact representation of maximal palindromes*, arXiv:2508.14384 (first submitted 2025-08-20); CPM 2026, DOI:10.4230/LIPIcs.CPM.2026.4. https://arxiv.org/abs/2508.14384 and https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.4/LIPIcs.CPM.2026.4.html
2. T. Mieno and M. Funakoshi, *Data Structures for Computing Unique Palindromes in Static and Non-Static Strings*, arXiv:2204.07327 (first submitted 2022-04-15), *Algorithmica* 86 (2024), 852–873, DOI:10.1007/s00453-023-01170-8. https://arxiv.org/abs/2204.07327
3. Published mathematical comparison, *Minimal unique factors of binary words with two marked symbols: exact spectrum*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-minimal-unique-factors-of-binary-words-with-two-marked-symbols-e--82dd9adea10e
4. Published mathematical comparison, *A sharp five-run threshold for three shortest unique palindromic substrings*, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-five-run-threshold-for-three-shortest-unique-palindromic--3513680a544d
