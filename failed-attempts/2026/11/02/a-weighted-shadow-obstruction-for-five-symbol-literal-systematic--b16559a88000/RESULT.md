# A weighted-shadow obstruction for five-symbol literal-systematic two-deletion codes

## Finding

**Theorem (necessary alphabet size at the first two-information-symbol endpoint).** Let \(\Sigma\) be an alphabet of cardinality \(q\ge2\). Suppose a literal-prefix systematic encoder
\[
E:\Sigma^2\longrightarrow\Sigma^5,\qquad E(a,b)=ab\,p(a,b),\quad p(a,b)\in\Sigma^3,
\]
has pairwise disjoint sets of distinct length-three subsequences for distinct messages \((a,b)\). Equivalently, the transmitted code corrects any two deletions. Then
\[
\boxed{q\ge7.}
\]
This is a *necessary condition only*: the theorem does not construct a code when \(q\ge7\), and does not assert that the threshold seven is sufficient.

A stronger quantitative version is the following **weighted-shadow converse**. For *any* code \(\mathcal C\subseteq\Sigma^5\) correcting two deletions, let \(m_{=}\) be the number of codewords whose first two symbols are equal, and \(m_{\ne}\) the number whose first two symbols differ. Then
\[
\boxed{22m_{=}+30m_{\ne}\ \le\ q(3q^2+7q+12).}
\]
The prefix-systematic conclusion follows because its code has exactly \(m_{=}=q\) and \(m_{\ne}=q(q-1)\).

## Assumptions and scope

A deletion removes one symbol without changing the order of the surviving symbols. For \(w=w_1w_2w_3w_4w_5\), let
\[
D_2(w)=\{w_iw_jw_k:1\le i<j<k\le5\}
\]
be a **set** (not a multiset) of distinct three-symbol descendants. Two-deletion correction means \(D_2(u)\cap D_2(v)=\varnothing\) for distinct codewords. The encoder is *literal-prefix*: the message symbols occur unchanged as the first two transmitted symbols, with exactly three appended symbols, all deletion-prone. No algebraic structure on \(\Sigma\), linearity, efficiency or probabilistic assumption is needed. The result holds for every integer \(q\ge2\), not only prime powers.

For a length-three word, let \(\operatorname{type}(v)\) be its equality pattern. The five patterns \(AAA,AAB,ABA,ABB,ABC\) respectively mean: all symbols equal; first two equal; first and last equal; last two equal; all three distinct. Assign the integer weights

| Three-symbol equality pattern | \(AAA\) | \(AAB\) | \(ABA\) | \(ABB\) | \(ABC\) |
|---|---:|---:|---:|---:|---:|
| \(\omega\) | 22 | 5 | 3 | 8 | 3 |

Here distinct letters in these *pattern names* denote unequal alphabet symbols. Set
\[
W(w)=\sum_{v\in D_2(w)}\omega(\operatorname{type}(v)).
\]

## Proof

**1. Finite equality-pattern lemma.** Every five-symbol word \(w\) satisfies
\[
W(w)\ge\begin{cases}
22,&w_1=w_2,\\
30,&w_1\ne w_2.
\end{cases}\tag{1}
\]
To verify the nonstandard numerical lemma without relying on a numerical optimizer, canonically relabel distinct symbols in order of first appearance as \(0,1,2,\ldots\). The resulting *restricted-growth word* is unique, starts with \(0\), and each later entry is at most one greater than the maximum preceding entry. There are exactly \(52\) such words of length five, one for each set partition of five positions. Every possible equality pattern occurs exactly once; relabeling does not change \(W\).

For each canonical word, form the set of outputs at the ten index triples \(1\le i<j<k\le5\), remove duplicates, classify each output into the five types above, and add its weights. The complete finite enumeration has the following independent grouped certificate. Its pattern count sums to \(52\), and the minima in the two prefix categories are exactly the right-hand sides of (1).

| First two equal? | Number of distinct symbols | Canonical patterns | Minimum \(W\) | Maximum \(W\) |
|---|---:|---:|---:|---:|
| Yes | 1 | 1 | 22 | 22 |
| Yes | 2 | 7 | 27 | 43 |
| Yes | 3 | 6 | 26 | 44 |
| Yes | 4 | 1 | 27 | 27 |
| No | 2 | 8 | 30 | 54 |
| No | 3 | 19 | 30 | 50 |
| No | 4 | 9 | 30 | 37 |
| No | 5 | 1 | 30 | 30 |

The accompanying standalone \(\texttt{verify\_shadow.py}\) implements this exhaustive enumeration directly using Python integer arithmetic and ordered index combinations; it checks every inequality and exactly reproduces all eight rows. It also independently rechecks all actual words for alphabet sizes \(2\) through \(7\). Thus (1) is a finite, fully reproducible lemma, not an inference from partial sampling or an infinite-case experiment.

**2. Total available weight.** There are \(q\) words of type \(AAA\), \(q(q-1)\) words of each of the three two-equal types, and \(q(q-1)(q-2)\) words of type \(ABC\). Therefore
\[
\begin{aligned}
\Omega_q:=\sum_{v\in\Sigma^3}\omega(\operatorname{type}(v))
&=22q+(5+3+8)q(q-1)+3q(q-1)(q-2)\\
&=q(3q^2+7q+12).
\end{aligned}\tag{2}
\]

**3. Shadow packing.** Because the sets \(D_2(w)\), for \(w\in\mathcal C\), are pairwise disjoint and all weights are positive,
\[
\sum_{w\in\mathcal C}W(w)\le\Omega_q.
\]
Combining with (1) gives the weighted-shadow converse in the Finding.

**4. The systematic cutoff.** For the literal-prefix encoder there is exactly one codeword starting with each ordered pair. Hence there are \(q\) codewords starting with two equal symbols and \(q(q-1)\) starting with unequal symbols. The required total shadow weight and the available total obey
\[
22q+30q(q-1)\le q(3q^2+7q+12).
\]
Subtracting the right side from the left gives
\[
q(q-1)(20-3q)\le0.
\]
Since \(q\ge2\), this forces \(q\ge7\), completing the proof.

## Verification

Run \(\texttt{python3 verify\_shadow.py}\) using Python 3 standard-library modules only. The file \(\texttt{verify\_shadow\_output.txt}\) records the output of an actual execution. The verifier enumerates all \(52\) restricted-growth patterns, independently checks all \(q^5\) five-symbol words for each \(2\le q\le7\), and compares the weighted capacity formula to direct enumeration of all \(q^3\) length-three words. The exact excesses of required over available weight for \(q=2,3,4,5,6\) are respectively \(28,66,96,100,60\). No floating-point arithmetic or external optimization solver is used in this certificate.

The universal theorem is proved by the finite equality-pattern reduction and the symbolic packing argument; the finite checker is an executable verification of the critical \(52\)-case lemma, not a substitute for the symbolic quantifiers.

## Relationship to prior work

Grishin and Zabokritskiy (first publicly posted September 29, 2026) study the same literal-prefix systematic deletion model and give the three-symbol optimal redundancy benchmark and an alphabet-size converse in their Section 2.5, Proposition 2.6. Their condition is \(q^{k+1}\ge I_k(n,q)\), with \(I_k(n,q)\) an insertion-ball count. At the present endpoint \(k=n=2\), it becomes only \(q^3\ge q^2\), excluding none of the integer alphabet sizes \(q\ge2\). Their constructions establish existence for sufficiently large alphabets but do not give the stated \(q\ge7\) finite-endpoint exclusion. Their Sections 2.1, 2.5 and 11 and relevant endpoint remarks were compared in the primary full text.

Song and Cai (first posted October 25, 2022) study systematic nonbinary two-deletion-correcting codes with asymptotic bit redundancy. Their primary full text, including Sections II–III and Theorem 2, was inspected: its construction uses a concatenated regular-word encoder and protected check blocks, not an exact five-symbol, three-appended-symbol alphabet converse. The distinction between bit redundancy and three full deletion-prone appended symbols is essential. The new certificate depends on both the exact length-three descendant geometry and the required complete two-symbol prefix message set, rather than a general long-block rate bound.

## Limitations

The proven bound is **necessary, not sufficient**: it leaves the existence of a \(q=7\) encoder unresolved. The finite \(52\)-case lemma applies to words of length five and correction of two arbitrary deletions, not to other lengths or larger deletion radii without new analysis. The certificate verifies the mathematical converse but does not establish uniqueness against unindexed or inaccessible earlier literature. Independent mathematical review has not been performed.

## References

1. V. Grishin and A. L. Zabokritskiy, *Systematic Codes Correcting Two Deletions with Three Redundant Symbols over Large Alphabets*, arXiv:2609.38259, first version September 29, 2026. https://arxiv.org/abs/2609.38259 . In particular, Sections 2.1, 2.5 and 11, and Proposition 2.6.
2. W. Song and K. Cai, *Non-binary Two-Deletion Correcting Codes and Burst-Deletion Correcting Codes*, arXiv:2210.14006, first version October 25, 2022. https://arxiv.org/abs/2210.14006 .
