# First Simon-disagreement spectra of permutation powers and inversion graphs

## Finding

Let \(\Sigma\) be a labelled alphabet of size \(q\ge 2\), and let \(P,Q\) be permutations of its letters, regarded as words of length \(q\). For every integer \(r\ge 1\), put \(X=P^r\) and \(Y=Q^r\). Two words are Simon-congruent through length \(k\) when they have identical sets of scattered subsequences of every length at most \(k\).

Let \(G=G(P,Q)\) be the inversion graph on \(\Sigma\): two different letters are joined when their relative order in \(P\) is opposite to their relative order in \(Q\). Let \(i_j(G)\) be the number of independent \(j\)-element vertex subsets, including \(i_0(G)=1\), and define \(I_G(t)=\sum_{j=0}^{q}i_j(G)t^j\).

**Theorem.** If \(P\ne Q\), then \(X\) and \(Y\) are Simon-congruent through length \(r\), but not through length \(r+1\). The exact number \(D_r(P,Q)\) of length-\(r+1\) words belonging to exactly one of their two scattered-subsequence languages is
\[
D_r(P,Q)=2\left[\binom{r+q}{q-1}-\sum_{j=1}^{\min(q,r+1)}i_j(G)\binom{r}{j-1}\right].
\]
The full generating function and sharp extremal bounds, for distinct \(P,Q\), are
\[
\sum_{r\ge1}D_r(P,Q)z^r
=\frac{2}{z}\left[(1-z)^{-q}-I_G\!\left(\frac{z}{1-z}\right)\right],
\]
\[
2\binom{r+q-2}{q-1}\ \le\ D_r(P,Q)\ \le\ 2\left[\binom{r+q}{q-1}-q\right].
\]
Equality at the lower bound holds precisely when \(Q\) is obtained from \(P\) by interchanging two adjacent letters; equality at the upper bound holds precisely when \(Q\) reverses \(P\). This includes \(q=2\), where the two conditions coincide.

The entire independent-set sequence of \(G\), equivalently the counts of common-order increasing subsequences of every size in the relative permutation, can be recovered from the values \(D_1(P,Q),\ldots,D_{q-1}(P,Q)\) together with \(D_0(P,Q):=0\). In particular, \(D_1(P,Q)\) equals twice the Kendall inversion count of the two orders.

**Exact witness classification.** Fix any multiset \(M\) of \(r+1\) letters of \(\Sigma\). Let \(s_P(M)\) and \(s_Q(M)\) be its two weakly decreasing sorted words in the orders defined by \(P\) and \(Q\). If the support of \(M\) is independent in \(G\), these words coincide and are absent from both powers. If its support contains an edge, they are different: \(s_P(M)\) is absent from \(P^r\) but present in \(Q^r\), and \(s_Q(M)\) is absent from \(Q^r\) but present in \(P^r\). These are all first-length distinguishing words, with no duplicates between different multisets.

## Assumptions and scope

All words are finite, all symbols distinct within each permutation, both powers have the **same** positive repetition exponent, and subsequences are scattered (not necessarily contiguous). The empty subsequence is allowed for congruence, but never contributes to \(D_r\). The graph uses *relative-order inversions*, not adjacent positions in the source words. The cardinality \(D_r\) counts distinct word strings, not choices of embeddings, and the two oriented symmetric-difference classes are counted together. The formulas do not assert anything about unequal exponents, nonpermutation periods, or alphabets with additional unused symbols.

The first-public source dates cited below are arXiv version-one dates, not later publication or revision dates. The source family lies in combinatorics on words, primary MSC2020 \(68R15\).

## Proof

**1. Greedy embedding.** Write \(\rho_P(a)\in\{1,\ldots,q\}\) for the position of letter \(a\) within \(P\). For any nonempty test word \(v=v_1\cdots v_m\), greedy left-to-right matching in the infinite power \(P^\omega\) places \(v_1\) in the first period and moves to a new period between \(v_{h-1}\) and \(v_h\) exactly when \(\rho_P(v_h)\le\rho_P(v_{h-1})\). Thus the minimum period number used equals
\[
1+\sum_{h=2}^{m}\mathbf 1_{\{\rho_P(v_h)\le\rho_P(v_{h-1})\}}.
\]
Greediness is optimal because every letter occurs exactly once per period and choosing any later occurrence cannot improve a subsequent match. Consequently, \(v\preceq P^r\) if and only if this period number is at most \(r\). Every word of length at most \(r\) is therefore embedded in \(P^r\), regardless of \(P\).

**2. The first absent layer.** At length \(m=r+1\), absence holds if and only if all \(r\) adjacent tests contribute one. Equivalently, the ranks of the test word are weakly decreasing. Hence there is exactly one absent length-\(r+1\) word per multiset of \(r+1\) letters: its descending sort \(s_P(M)\). The same argument applies to \(Q\). The number of multisets is \(\binom{r+q}{q-1}\).

**3. Comparing the two absent layers.** The descending orders \(s_P(M)\) and \(s_Q(M)\) agree if and only if no pair of distinct letters in the support of \(M\) is inverted between the two permutations. This is exactly the independent-set condition in \(G\). If they do not agree, \(s_P(M)\) has an adjacent ascent in the \(Q\)-order and so embeds in \(Q^r\), while \(s_Q(M)\) embeds in \(P^r\). Different multisets have different content and cannot duplicate either witness. This proves both the classification and the fact that the symmetric difference is twice the number of multisets whose support contains an edge. For an independent support with \(j\) letters there are \(\binom{r}{j-1}\) strictly positive multiplicity assignments summing to \(r+1\). Summing over \(i_j(G)\) gives the stated exact formula.

If \(P\ne Q\), their inversion graph has an edge, so a multiset containing its endpoints exists at every size \(r+1\ge2\). This gives a distinguishing word of length \(r+1\); the preceding universality gives no shorter one.

**4. Generating function and reconstruction.** The standard multiset generating identity is
\[
\sum_{r\ge0}\binom{r+q}{q-1}z^r=\frac{(1-z)^{-q}-1}{z}.
\]
For every \(j\ge1\),
\[
\sum_{r\ge0}\binom{r}{j-1}z^r=\frac{z^{j-1}}{(1-z)^j}.
\]
Substituting in the exact formula and observing \(D_0=0\) yields the rational generating function. Defining
\[
J_r=\binom{r+q}{q-1}-\frac{D_r}{2},\qquad r\ge0,
\]
gives the Newton-binomial expansion \(J_r=\sum_{j=1}^{q}i_j(G)\binom{r}{j-1}\). Therefore the \((j-1)\)-fold forward difference at zero satisfies \(\Delta^{j-1}J_0=i_j(G)\). Values through \(r=q-1\) recover every coefficient. Since \(i_2(G)=\binom q2-|E(G)|\), direct substitution at \(r=1\) yields \(D_1=2|E(G)|\).

**5. Extremal bounds and rigidity.** Since \(P\ne Q\), fix an edge \(\{a,b\}\) of \(G\). All multisets containing \(a,b\) contribute to the difference, and stars and bars counts these as \(\binom{r+q-2}{q-1}\), giving the lower bound. If another edge exists, there is an additional multiset supported exactly on its two endpoints, which does not contain both \(a,b\). Thus equality requires exactly one graph edge; a permutation has precisely one inversion relative to another if and only if it is a single swap of adjacent letters in the original order. Conversely one edge attains the bound.

Every monochromatic multiset has independent support; hence at most \(\binom{r+q}{q-1}-q\) multisets contribute. If an unordered pair is not an edge, any multiset supported on precisely that pair is another noncontributing multiset, making the inequality strict. Thus equality requires the complete inversion graph, or equivalently complete reversal of the total order. A reversal attains the bound.

## Verification

Run `python verify_distinguishing_spectrum.py` in a standard Python 3 environment. Its literal subsequence matcher, which is independent of the weak-descent formula, exhausted 488 input-parameter configurations and 127,920 candidate words of the first potentially distinguishing length, checking the exact number and the minimum distinguishing length. A separate combinatorial checker tested independence-polynomial reconstruction and both sharp-bound equality conditions for 5,912 ordered-permutation configurations, including every pair of orderings on at most seven letters after fixing the first order. All checks passed. They are finite cross-checks; the proof above, not the experiments, covers all \(q\), \(r\), and permutations.

For a small example, take \(P=0123\), \(Q=1032\). The inversion graph consists of two disjoint edges, so \(I_G(t)=(1+2t)^2\). The first three values are \(D_1=4\), \(D_2=16\), \(D_3=38\). For a single adjacent transposition instead, the full series is \(2z/(1-z)^q\); for reversal it is \(\frac2z[(1-z)^{-q}-1-qz/(1-z)]\).

## Relationship to prior work

The arXiv papers on repeated-word scattered-factor universality (2021), nearly universal words (2022), and \(\alpha\)-\(\beta\) factorization with Simon congruence (2023) establish general definitions, universality machinery, and congruence characterizations. In particular, the 2022 article gives general methods to characterize and count absent subsequences and compare nearly universal words; the 2023 article's Theorem 3.1 gives a general equivalence criterion by factorization. Those results are substantially broader as algorithms and necessary/sufficient conditions, but the inspected relevant sections do not give the first distinguishing word-set classification for **two equal powers of permutations**, its inversion-graph independence-polynomial transform, or the rigidity of the sharp extremizers. The present result is a closed-form structural specialization requiring the explicit greedy descent and inversion-support argument; it is not a claim to replace or improve their general algorithms.

The associated inversion count, independent-set polynomial, increasing-subsequence statistics, stars-and-bars coefficients, and Newton binomial inversion are standard notions; novelty is claimed only for their precise conjunction as the first Simon-disagreement spectrum of permutation powers. No claim of priority over an unindexed specialized formulation is made.

## Limitations

The result concerns only the first length at which the languages can differ, not the entire higher-length symmetric-difference spectrum. The recovered independence polynomial generally does not determine the relative permutation uniquely. No numerical experiment proves the infinite-parameter theorem, and an unindexed equivalent explicit classification may exist. The first-disagreement theorem is not claimed to settle equivalence for unequal exponents or to characterize higher-length language differences.

## References

1. P. Fleischmann, S. B. Germann, D. Nowotka, *Scattered Factor Universality — The Power of the Remainder*, first arXiv publication 2021-04-19, https://arxiv.org/abs/2104.09063 . Relevant material: Sections 2–4 on powers and universality.
2. P. Fleischmann, L. Haschke, A. Huch, A. Mayrock, D. Nowotka, *m-Nearly k-Universal Words — Investigating Simon Congruence*, first arXiv publication 2022-02-16, https://arxiv.org/abs/2202.07981 . Relevant material: Sections 2–4, especially Proposition 6 and Theorem 4.2.
3. P. Fleischmann, J. Höfer, A. Huch, D. Nowotka, *\(\alpha\)-\(\beta\)-Factorization and the Binary Case of Simon's Congruence*, first arXiv publication 2023-06-25, https://arxiv.org/abs/2306.14192 . Relevant material: Sections 2–3, especially Theorem 3.1, and Sections 4–5.

4. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, first arXiv publication 2021-08-31, https://arxiv.org/abs/2108.13968 . Relevant material: Section 3, especially Propositions 3.8, 3.13, and 3.21 on shortest absent subsequences of individual words.
