# Exact Parikh-pair distribution of maximally subsequence-universal binary words

## Finding

Fix integers \(k\ge4\) and \(r\ge0\). A binary word is \(k\)-subsequence universal when every word of length \(k\) over \(\{a,b\}\) appears as a scattered subsequence. Write \(\iota(w)\) for its largest universality index, and \(C(w)\) for the number of scattered occurrences of \(ab\) (pairs of indices, not just distinct patterns). Define
\[
U_{k,r}(q)=\sum_{\substack{|w|_a=k+r,\ |w|_b=k,\\ \iota(w)=k}}q^{C(w)},\qquad T=\binom{k}{2}.
\]
Then the following exact finite-coefficient formula holds:
\[
\boxed{U_{k,r}(q)=q^T[z^r]\frac{1}{1-z}\prod_{j=1}^{k}\left(1+\frac{q}{1-zq^j}\right).}
\]
The rational product is interpreted formally in \(z\); its coefficient is a polynomial in \(q\) with nonnegative integer coefficients. Consequently, for any integer \(C\), the number of words in the binary Parikh-matrix class with parameters \((k+r,k,C)\) whose universality index attains the maximum \(k\) is \([q^C]U_{k,r}(q)\). By reversing and interchanging letters, the same statement covers \((k,k+r,C)\).

The polynomial is palindromic:
\[
q^{k(k+r)}U_{k,r}(q^{-1})=U_{k,r}(q).
\]
Its least exponent is \(T\), its greatest is \(k(k+r)-T\), and both extreme coefficients are one. Its unweighted total and first nonzero coefficients are
\[
U_{k,r}(1)=\sum_{j=0}^{k}\binom{k}{j}\binom{r+j}{j},
\]
\[
[q^{T}]U_{k,r}=1,\quad [q^{T+1}]U_{k,r}=k,\quad
[q^{T+2}]U_{k,r}=\binom{k}{2}+\mathbf{1}_{\{r\ge1\}},
\]
\[
[q^{T+3}]U_{k,r}=\binom{k}{3}+k\mathbf{1}_{\{r\ge1\}}+\mathbf{1}_{\{r\ge2\}}.
\]
These count consecutive exact pair-count layers at the first possible edge of maximal universality.

## Assumptions and scope

Words are finite, ordered left to right, over the labeled alphabet \(a<b\). The notation \(|w|_x\) counts letters, while \(C(w)=|w|_{ab}\) counts embeddings of \(ab\). The index \(\iota(w)\) is defined by scattered rather than contiguous subsequences. Both \(k\) and \(r\) are unrestricted within their stated integer ranges, and \(q,z\) are formal indeterminates; the coefficient extraction is not an analytic convergence assertion. The restriction \(|w|_b=k\) forces \(\iota(w)\le k\), so maximal universality and \(k\)-universality coincide here. Zero coefficients represent empty classes, not an exceptional definition of the probability.

## Proof

**1. The arch criterion.** Greedily split any binary word into the shortest successive prefixes containing both letters, followed by a suffix containing at most one kind of letter. Call the complete pieces arches. If there are \(h\) arches, every target word of length \(h\) is a subsequence by selecting its successive letters from the successive arches. Conversely, let \(y_i\) be the letter at the end of arch \(i\); it is the first occurrence of that letter within arch \(i\). Choose a letter \(x\) missing from the final suffix. Greedy matching of the word \(y_1\cdots y_hx\) is forced to use successive arch endpoints for its first \(h\) letters and then cannot find \(x\). Since greedy matching fails exactly when the subsequence is absent, the universality index is \(h\). This also handles \(h=0\).

**2. A uniquely restricted factorization.** If \(|w|_b=k\) and \(\iota(w)=k\), there are precisely \(k\) complete arches. Each contains at least one \(b\), so each contains exactly one \(b\), all \(b\)'s are consumed, and the remaining suffix consists only of \(a\)'s. The only possible arch shapes are \(ba\) and \(a^{u+1}b\) for a unique integer \(u\ge0\). Thus every counted word has a unique representation as \(k\) ordered arches of these shapes followed by \(a^v\), \(v\ge0\). Conversely, every such representation has exactly \(k\) complete greedy arches and therefore has index \(k\). For arch \(i\), put \(\epsilon_i=0\) for \(ba\), and \(\epsilon_i=1\) for \(a^{u_i+1}b\), setting \(u_i=0\) in the former case. The total number of extra \(a\)'s is \(r=v+\sum_i\epsilon_i u_i\).

**3. Exact pair count.** Select one distinguished \(a\) and the unique \(b\) in every arch. Each distinguished \(a\) precedes the \(b\) of every later arch, contributing \(\binom{k}{2}=T\) pairs. It precedes the \(b\) in its own arch exactly when \(\epsilon_i=1\), contributing \(\sum_i\epsilon_i\). Every extra \(a\) in an \(a^{u_i+1}b\) arch precedes its own \(b\) and all later \(b\)'s, contributing \(k-i+1\) pairs per extra letter. Letters in the final \(a^v\) suffix contribute no \(ab\) pairs. Hence, without double counting,
\[
C(w)=T+\sum_{i=1}^k\epsilon_i\bigl(1+(k-i+1)u_i\bigr).
\]

**4. Product enumeration.** A \(ba\) arch contributes weight \(1\). An \(a^{u+1}b\) arch in position \(i\) contributes \(q^{1+(k-i+1)u}z^u\). The suffix \(a^v\) contributes \(z^v\). Unique factorization and the geometric series identity in formal power series give
\[
\sum_{r\ge0}z^rq^{-T}U_{k,r}(q)=\frac1{1-z}\prod_{i=1}^k\left(1+\sum_{u\ge0}q^{1+(k-i+1)u}z^u\right)
=\frac1{1-z}\prod_{j=1}^k\left(1+\frac{q}{1-zq^j}\right).
\]
Taking the \(z^r\) coefficient proves the exact formula. There is no convergence or infinite-search assumption: for any fixed \(r\) only finitely many powers of \(z\) contribute.

**5. Symmetry and extremal coefficients.** Reversal preserves the two letter multiplicities and the universality index, while mapping \(C(w)\) to \((k+r)k-C(w)\). This proves reciprocity. The minimum \(T\) occurs only when all arches are \(ba\) and all extra \(a\)'s are in the trailing suffix; the maximum is its reversed counterpart. At \(q=1\), expand \(\prod_i(1+1/(1-z))\), choose \(j\) positive-orientation arches, and extract \([z^r](1-z)^{-j-1}=\binom{r+j}{j}\), giving the stated total. For excesses above \(T\) of zero or one, there are respectively one and \(k\) choices of \(ab\) arch with no extra internal \(a\). At excess two there are \(\binom{k}{2}\) choices of two such arches, plus (if \(r\ge1\)) one extra \(a\) in the last \(ab\) arch. At excess three there are \(\binom{k}{3}\) choices of three \(ab\) arches, plus (if \(r\ge1\)) \(k-1\) choices of one extra \(a\) in the last \(ab\) arch accompanied by one further \(ab\) arch, and one choice of an extra \(a\) in the penultimate \(ab\) arch. A further possibility (if \(r\ge2\)) is two extra \(a\)'s in the last \(ab\) arch. This establishes every displayed edge coefficient. Finally, applying letter interchange followed by reversal preserves both \(C(w)\) and \(\iota(w)\), providing the analogous statement for \(|w|_a=k\).

## Verification

Run `python3 checker.py` from the extracted file directory. The checker independently generates all binary words at \(1\le k\le5\), \(0\le r\le4\) with the required letter counts and tests every length-\(k\) binary target using direct subsequence matching, not arch counting. It compares the resulting exact \(ab\)-pair histogram against the coefficient product, and additionally verifies palindromicity, the unweighted sum and the four stated low-edge coefficients in every applicable test case. A successful replay returned: 25 parameter cases, 6,441 enumerated words, 25 total-count identities, 250 reciprocal coefficient checks and 80 edge coefficient checks. For instance, at \(k=4,r=1\), coefficients for pair counts \(6,7,8,9,10,11,12,13,14\) are exactly \(1,4,7,8,8,8,7,4,1\).

These finite checks are not the proof for arbitrary parameters; steps 1–5 above are.

## Relationship to prior work

Fazekas, Huang and Mercaş (first posted 2026-10-05) give arithmetic conditions for existence and universal validity of subsequence universality within fixed binary Parikh-matrix classes, together with an additive approximation method for containment of a fixed pattern. Their theorem does not state the exact distribution of maximally universal representatives across the pair count \(C\); their bounded-width exact-count procedure does not furnish this closed coefficient product for every \(k\ge4\) and \(r\ge0\). Adamson (2023) counts and ranks \(k\)-universal words of fixed total length, without the joint letter-content and scattered-pair refinement. Richomme (first posted 2025-10-08) identifies binary Parikh classes with bounded partitions, determining class sizes rather than the universality-filtered cardinality. The distinct \(q\)-Parikh deformation studied by Renard, Rigo and Whiteland (2024) refines occurrences of a pattern within one word, rather than counting words by their ordinary \(ab\) statistic.

## Limitations

The exact product relies on a saturated letter multiplicity: one letter occurs exactly \(k\) times. It does not give the corresponding general bivariate refined count when both letter multiplicities exceed \(k\), or a bit-complexity bound for evaluating the coefficient for binary-encoded large inputs. The derivation uses known arch factorization; the asserted new content is the scattered-pair-refined product and its exact Parikh-class counts. The literature comparison is based on the inspected primary text and searches, and cannot rule out an unindexed equivalent identity. No independent mathematical audit has been performed.

## References

1. S. Z. Fazekas, X. Huang and R. Mercaş, *Subsequence Analysis Problems for Binary Parikh Matrices*, arXiv:2610.06717, first submitted 2026-10-05. https://arxiv.org/abs/2610.06717
2. D. Adamson, *Ranking and Unranking k-subsequence universal words*, arXiv:2304.04583, first submitted 2023-04-10. https://arxiv.org/abs/2304.04583
3. G. Richomme, *On some 2-binomial coefficients of binary words: geometrical interpretation, partitions of integers, and fair words*, arXiv:2510.07159, first submitted 2025-10-08. https://arxiv.org/abs/2510.07159
4. A. Renard, M. Rigo and M. A. Whiteland, *q-Parikh Matrices and q-deformed binomial coefficients of words*, arXiv:2402.05657, first submitted 2024-02-08. https://arxiv.org/abs/2402.05657
