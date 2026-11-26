# Exact length–universality distribution of palindromic words and shortest-host classification

## Finding
Fix a labeled alphabet \(\Sigma\) with \(q\ge2\) letters. Let \(p_{n,j}\) be the number of palindrome words of length \(n\ge0\) having scattered-subsequence universality index exactly \(j\ge0\). The **all-length, all-index distribution** is the rational series
\[
P_q(z,u)=\sum_{n,j\ge0}p_{n,j}z^nu^j
=\frac{(1+qz)R_q(z^2)+z(u-1)S_q(z^2)}{1-u^2A_q(z^2)},
\]
where
\[
A_q(y)=\frac{q!y^q}{\prod_{h=1}^{q-1}(1-hy)},\qquad
S_q(y)=\frac{q!y^{q-1}}{\prod_{h=1}^{q-1}(1-hy)},
\]
\[
R_q(y)=\sum_{h=0}^{q-1}\frac{(-1)^{q-h+1}\binom{q}{h}}{1-hy}.
\]
These are formal power series; \(0^0=1\) is understood when extracting coefficients. In particular, the coefficient \([z^nu^j]P_q(z,u)\) is an **exact integer count**, not an asymptotic estimate.

For every \(k\ge1\), the shortest \(k\)-universal palindrome has length
\[
L(q,k)=\begin{cases}qk,&k\text{ even},\\q(k+1)-1,&k\text{ odd},\end{cases}
\]
and exactly \((q!)^{\lceil k/2\rceil}\) labeled words attain it. All shortest words are precisely
\[
P_1\cdots P_t\,M\,P_t^{\mathrm R}\cdots P_1^{\mathrm R},\quad t=\lfloor k/2\rfloor,
\]
where each \(P_i\) is an arbitrary permutation of \(\Sigma\), and \(M\) is empty for even \(k\), or \(V c V^{\mathrm R}\) for odd \(k\) with \(c\in\Sigma\) and \(V\) a permutation of \(\Sigma\setminus\{c\}\).

## Assumptions and scope
A palindrome is a finite word equal to its reversal; the empty word is included. A word is \(j\)-universal if **every** length-\(j\) word over the fixed full alphabet \(\Sigma\) occurs as a scattered subsequence (not necessarily a contiguous factor). Its index \(\iota(w)\) is the largest such \(j\), and is zero when the word omits an alphabet symbol. Alphabet letters are labeled, so distinct letter permutations count as distinct palindromes. All \(q\ge2\), \(n,j\ge0\), and \(k\ge1\) are covered.

## Proof
**1. Greedy arches.** Scan any half-word \(H\) from left to right and close an arch at the earliest position that has seen every symbol of \(\Sigma\); repeat. This uniquely gives \(H=B_1\cdots B_t R\), where each arch \(B_i\) is a shortest complete-alphabet prefix of its remaining suffix, and the remainder \(R\) omits at least one letter. The standard greedy-arch theorem states \(\iota(H)=t\). Moreover, the known palindrome index characterization of Barker et al. (2020, Proposition 3) states that \(\iota(HH^{\mathrm R})=2t\) and that \(\iota(HcH^{\mathrm R})=2t+1\) precisely when \(\operatorname{alph}(R)\cup\{c\}=\Sigma\), and equals \(2t\) otherwise. This pre-existing index result is used here, **not asserted as a new lemma**. Its boundary case \(t=0\) follows by the same greedy argument, including one-letter palindromes.

**2. Count arch blocks.** To make an arch of length \(m\), choose its final previously missing symbol (\(q\) choices), then put every one of the other \(q-1\) symbols at least once into the preceding \(m-1\) positions. Inclusion-exclusion gives \(q\,\operatorname{onto}_{q-1}(m-1)\) such blocks. The usual onto-word generating function is \(\sum_{m\ge0}\operatorname{onto}_{r}(m)y^m=r!y^r/\prod_{h=1}^{r}(1-hy)\). Therefore the generating function for one arch is \(A_q(y)\) above. The remainder may be any word omitting at least one symbol: by inclusion-exclusion its length generating function is \(R_q(y)\). Among these remainders, those omitting **exactly one** symbol have series \(S_q(y)\), since one chooses the omitted letter and uses each of the other \(q-1\) at least once. Consequently half-words with exactly \(t\) greedy arches have series \(A_q(y)^tR_q(y)\), and those with exactly \(t\) arches and a remainder omitting exactly one letter have series \(A_q(y)^tS_q(y)\).

**3. Enumerate even and odd palindromes.** There is a bijection between half-words of length \(h\) and even palindromes of length \(2h\), whose index is \(2t\). Their generating series is
\[
\frac{R_q(z^2)}{1-u^2A_q(z^2)}.
\]
An odd palindrome is uniquely \(HcH^{\mathrm R}\). For each half-word there are \(q\) possible center symbols; the index is normally \(2t\). Exactly one center upgrades the index to \(2t+1\) when, and only when, its greedy remainder omits exactly one letter. Thus the odd series is
\[
\frac{z\{qR_q(z^2)+(u-1)S_q(z^2)\}}{1-u^2A_q(z^2)}.
\]
Summing the even and odd cases proves the displayed rational function. Every factor is an ordinary combinatorial generating series of **unique** decompositions, so there are no multiplicity or overcounting ambiguities.

**4. Extremal length and classification.** Write \(k=2t\) or \(k=2t+1\). An even palindrome of index at least \(2t\) needs a half containing at least \(t\) complete arches; each uses at least \(q\) positions. This forces length \(\ge2qt\), with equality if and only if every half-arch has length exactly \(q\) and the remainder is empty. Thus the half is a concatenation of \(t\) permutations. An odd palindrome of index at least \(2t+1\) must have at least \(t\) complete arches on its left and a remainder that includes all \(q-1\) letters other than the middle symbol; hence left-half length \(\ge qt+q-1\), giving full length \(\ge q(2t+2)-1\). Equality forces all arches to be permutation blocks and the residual half to be a permutation of the noncentral letters. An even palindrome cannot have odd universality index, while an odd palindrome of index at least \(2t\) has total length at least \(2qt+1\); for even \(k=2t\), this exceeds the attainable even length \(2qt\). For odd \(k=2t+1\), an even palindrome of index at least \(k\) must in fact have index at least \(2t+2\), and has length at least \(2q(t+1)\), strictly above the construction. The stated optimal forms are therefore exhaustive, their permutation choices are independent, and their count is \((q!)^{t}\) for even \(k\) or \((q!)^{t+1}\) for odd \(k\).

## Verification
Run the included \(`verify.py`\) using Python 3 with no third-party dependencies. It enumerates shortest palindrome candidates, compares literal scattered-subsequence tests with greedy-arch indices, checks every shorter candidate in bounded cases, verifies the prior palindrome-index lemma and explicit missing-subsequence witnesses, and independently compares integer coefficient convolutions for the rational generating function with all literal palindromes in 52 alphabet/length instances. Output in the packaged replay: \(`VERIFY_OK length_optima=19 construction_words=2648 palindrome_profiles=187229 literal_subsequence_checks=24387 shorter_palindromes=157360`\), \(`ARCH_DOUBLING_OK profiles=160874 absent_witnesses=160874`\), and \(`GENERATING_FUNCTION_OK lengths=52`\). These finite checks corroborate the algebraic proof but are not substitutes for it.

## Relationship to prior work
The **palindrome index lemma is known**: Barker et al., *Scattered Factor-Universality of Words* (2020), Proposition 3, explicitly covers even and odd palindromes. Our claim does **not** repackage this proposition as new; instead it derives the exact two-variable palindrome-counting function with all alphabet sizes and length/index strata, and the classified extremal families with exact counts. Adamson (2023) counts unrestricted universal words; Fleischmann et al. (2023) study alpha-beta decompositions and Simon equivalence. None of the relevant inspected statements gives the above palindrome-restricted generating series or extremizer census. This is a best-knowledge originality comparison, not a claim that all literature has been exhaustively indexed.

## Limitations
The counting model is for reversal-fixed finite words over a **labeled** full alphabet, not rotations, letter-quotient orbits, complement-palindromes, contiguous substrings, or multiplicity-weighted subsequences. Prior work contains the essential palindrome index lemma, and the new enumeration is a consequence of that lemma plus arch-block counting. Equivalent unlocated enumerations or an implicit specialization of a more general transfer-matrix framework remain originality risks. Independent scientific verification has not been performed.

## References
Barker, L., Fleischmann, P., Harwardt, K., Manea, F., Nowotka, D. (2020). *Scattered Factor-Universality of Words*. arXiv:2003.04629v1, 10 March 2020, especially Section 4, Proposition 3. https://arxiv.org/html/2003.04629v1

Adamson, D. (2023). *Ranking and Unranking k-Subsequence Universal Words*. arXiv:2304.04583. https://arxiv.org/abs/2304.04583

Fleischmann, P., Höfer, M., Huch, A., Nowotka, D. (2023). *alpha-beta Factorization and the Binary Case of Simon's Congruence*. arXiv:2306.14192. https://arxiv.org/abs/2306.14192
