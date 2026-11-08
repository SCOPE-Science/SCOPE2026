# Simultaneously extremal prefix-normal rearrangements of periodic binary run profiles

## Finding

Fix an integer \(k\ge1\), and two multisets of positive integers \(\mathcal A=\{a_1,\ldots,a_k\}\) and \(\mathcal B=\{b_1,\ldots,b_k\}\). For any independent permutations \(\sigma,\tau\) define the infinite binary word

\[
X_{\sigma,\tau}=\bigl(1^{a_{\sigma(1)}}0^{b_{\tau(1)}}\cdots1^{a_{\sigma(k)}}0^{b_{\tau(k)}}\bigr)^\omega.
\]

Write \(a_1^\downarrow\ge\cdots\ge a_k^\downarrow\) for the decreasing rearrangement of \(\mathcal A\), and \(b_1^\uparrow\le\cdots\le b_k^\uparrow\) for the increasing rearrangement of \(\mathcal B\). Define

\[
Y=\bigl(1^{a_1^\downarrow}0^{b_1^\uparrow}\cdots1^{a_k^\downarrow}0^{b_k^\uparrow}\bigr)^\omega.
\]

For any infinite binary word \(U\), let \(F_U(n)=\max_{i\ge0}\#_1(U[i:i+n])\), where factors are contiguous, length \(n\), and positions start at zero. **For every integer \(n\ge0\) and every pair of independent permutations**, the simultaneous inequality

\[
\boxed{F_{X_{\sigma,\tau}}(n)\le\#_1(Y[0:n])=F_Y(n)}
\]

holds. In particular, \(Y\) is a \(1\)-prefix-normal infinite word, and its prefix realizes the largest possible one-count at each window length among all cyclic rearrangements that preserve both individual run-length multisets.

With \(T=\sum_i(a_i+b_i)\) and \(A=\sum_i a_i\), writing \(n=qT+r\) with \(q\ge0\) and \(0\le r<T\), the exact global maximum is

\[
\boxed{\max_{\sigma,\tau}F_{X_{\sigma,\tau}}(n)=qA+\#_1(Y[0:r]).}
\]

## Assumptions and scope

Every run length is a strictly positive integer. A period begins with a maximal \(1\)-run, alternates between \(1\)-runs and \(0\)-runs, and ends with a maximal \(0\)-run. Equal run lengths are allowed; permutations are independent. There are precisely \(k\) runs of each kind per displayed period, including \(k=1\). The theorem concerns infinite periodic words and all finite factors, including factors crossing arbitrarily many period boundaries. It makes no claim that the maximizing arrangement is unique.

## Proof

**Multiset window lemma.** Let \(c_1,\ldots,c_k\) be positive integers, let \(c_1^\downarrow\ge\cdots\ge c_k^\downarrow\) and \(c_1^\uparrow\le\cdots\le c_k^\uparrow\) be sorted versions, and extend all sequences periodically to positive indices. For each integer \(h\ge0\), every consecutive length-\(h\) segment in any periodic permutation of the \(c_i\) has sum at most \(\sum_{j=1}^{h}c_j^\downarrow\) and at least \(\sum_{j=1}^{h}c_j^\uparrow\). Indeed, write \(h=uk+v\), where \(0\le v<k\). Any such segment consists of \(u\) complete cycles plus \(v\) distinct members of the multiset. The largest possible remaining \(v\)-sum consists of the \(v\) largest entries, and the smallest consists of the \(v\) smallest entries. The same formulas hold for \(h=0\) as empty sums.

**Span dominance.** Fix a pair \(\sigma,\tau\), put \(X=X_{\sigma,\tau}\), and take any \(t\ge1\) *consecutive occurrences* of the symbol \(1\) in \(X\). Suppose there are exactly \(h\ge0\) complete \(0\)-runs strictly between the first and last of these occurrences. Then those \(t\) one-symbols lie in (parts of) \(h+1\) consecutive \(1\)-runs; their count is therefore bounded by the sum of those \(h+1\) full run lengths. The multiset window lemma gives

\[
t\le\sum_{j=1}^{h+1}a_j^\downarrow.
\]

For the first \(t\) occurrences of \(1\) in \(Y\), let \(h_0\) be the number of complete \(0\)-runs strictly between first and last. Since the first \(h+1\) sorted \(1\)-runs contain at least \(t\) ones, \(h_0\le h\). The inclusive span of these first \(t\) ones in \(Y\) is exactly

\[
t+\sum_{j=1}^{h_0}b_j^\uparrow.
\]

The span of the chosen \(t\) consecutive ones in \(X\) is \(t\) plus the lengths of its \(h\) intervening complete \(0\)-runs. Their total is at least \(\sum_{j=1}^{h}b_j^\uparrow\), again by the multiset window lemma. Positivity and \(h_0\le h\) imply

\[
t+\sum_{j=1}^{h_0}b_j^\uparrow\le t+\sum_{j=1}^{h}b_j^\uparrow\le\text{the span of the selected ones in }X.
\]

The case \(t=1\) is included: both spans are one.

**All-length extremality.** Let a length-\(n\) factor of \(X\) contain \(t>0\) ones. Its first and last \(1\) form a span of length at most \(n\) enclosing exactly \(t\) consecutive \(1\)-occurrences of \(X\). Span dominance says that the first \(t\) ones of \(Y\) also fit within its first \(n\) positions. Hence this factor has at most \(\#_1(Y[0:n])\) ones. When \(t=0\), the same bound is immediate; when \(n=0\), all counts are zero. Taking the maximum over all factors and the arbitrary permutations yields \(F_X(n)\le\#_1(Y[0:n])\). Choosing \(X=Y\), its prefix is itself an available factor, so \(F_Y(n)\ge\#_1(Y[0:n])\); together the two inequalities yield equality. Finally, \(Y\) has \(A\) ones per period \(T\), so division of \(n\) by \(T\) gives the explicit formula. This completes the proof for all \(k\ge1\) and all \(n\ge0\).

## Verification

The accompanying standalone Python program `verify.py` directly enumerates every distinct independent arrangement of two run-length multisets for \(k=1,2,3\) with each run length between \(1\) and \(4\), checking every cyclic factor length through one full period. There are \(516\) multiset-pair profiles and \(4{,}368\) arrangement pairs. Independent occurrence-span checks cover \(2{,}896\) sampled/structured profiles; further randomized tests cover \(1{,}440\) larger profiles with \(4\le k\le9\). It prints `PASS profiles 516 all_permutation_pairs 4368 position_profiles 2896 random_large_profiles 1440`. Execute `python3 verify.py` in a directory containing the extracted file. These finite checks test the implementation and boundary conventions; the infinite theorem follows from the proof, not from exhaustive computation.

For strictness, the multisets \(\mathcal A=\{3,2,1\}\), \(\mathcal B=\{1,2,4\}\) give the canonical period `1110110010000`, whose length-five prefix has four ones. The rearranged period `1001110000110` has at most three ones in any cyclic length-five window.

## Relationship to prior work

Prefix normal words and their relation to binary jumbled indexing are defined and studied by Burcsi et al. (2016) and Cicalese, Lipták, and Rossi (2018). The 2018 paper studies infinite prefix-normal words, including structural examples and connections to abelian complexity, but the inspected text did not supply simultaneous run-multiset rearrangement extremality. Cunha et al. (2017) provide algorithms for indexing run-length-encoded binary strings with general fixed runs; their stated result does not compare every permutation of two run-length multisets or provide a universal maximizing arrangement. The present theorem instead is an explicit extremal rearrangement over *all independently permuted run orders*, realized by the same prefix-normal word for every window length. No equivalence or dominating formulation was established in the examined sources or semantic research searches; this is not a claim that all literature has been exhausted.

## Limitations

The theorem is confined to two-symbol periodic words with positive alternating run lengths. It does not classify all maximizing permutations or address three-letter alphabets, arbitrary finite words with incomplete boundary runs, nonperiodic run sequences, or minimum-one window extrema beyond what follows by separate symbol complementation. No publication priority or independent review is asserted. The possibility of an equivalent rearrangement theorem in unindexed literature remains.

## References

- Burcsi, Fici, Lipták, Ruskey, Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017 (first publicly available 2016-11-28). https://arxiv.org/abs/1611.09017
- Cunha, Dantas, Gagie, Wittler, Kowada, Stoye, *Fast and Simple Jumbled Indexing for Binary RLE Strings*, arXiv:1702.01280 (first publicly available 2017-02-04). https://arxiv.org/abs/1702.01280
- Cicalese, Lipták, Rossi, *On Infinite Prefix Normal Words*, arXiv:1811.06273 (first publicly available 2018-11-15). https://arxiv.org/abs/1811.06273
