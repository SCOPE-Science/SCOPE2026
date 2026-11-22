# A sharp five-letter two-read reconstruction capacity for homopolymer-free words

## Finding

Fix an alphabet \(\Sigma\) of size \(q\geq2\). Let \(K_{q,n}\) be the set of words \(w=w_1\cdots w_n\) satisfying \(w_i\ne w_{i+1}\) at every adjacent pair. Write \(D(w)\) for the **set of distinct words** obtained by deleting exactly one letter from \(w\). Define \(G_{q,n}\) on \(K_{q,n}\), joining distinct \(u,v\) exactly when \(|D(u)\cap D(v)|\geq2\). An independent set is precisely a code uniquely reconstructible from any two **distinct** single-deletion outputs, assuming the transmitted word lies in that code.

For every integer \(q\geq2\), the maximum code sizes at lengths \(2\leq n\leq5\) satisfy
\[
\alpha(G_{q,n})=\begin{cases}
\frac12q(q-1)^{n-1},&2\leq n\leq4,\\[2pt]
\frac12q(q-1)^4-2\binom q3,&n=5.
\end{cases}
\]
Thus five is the **first block length at which** a nonbinary homopolymer-free two-read code falls strictly below half the ambient word space; the exact deficit is \(2\binom q3\).

More generally, for every \(n\geq2\),
\[
|E(G_{q,n})|=\binom q2(q-1)^{n-3}\big((n-1)(q-2)+1\big).
\]
Moreover \(G_{q,n}\) is bipartite if and only if \(q=2\) or \(n\leq4\). For every \(q\geq3\) and \(n\geq5\) it contains a seven-cycle, and for \(n=5\) that exhibited cycle is induced. The exact capacity statement is **not** asserted for \(n>5\).

## Assumptions and scope

The alphabet is a labeled set, not necessarily a field. There is no circular wraparound adjacency, and each noisy read deletes exactly one letter. Multiple deletion positions producing the same string count as **one** output. The receiver is given two distinct outputs; no probabilistic, substitution, insertion, reverse-complement or additional composition observation is assumed. The result holds for all integer alphabet sizes \(q\geq2\), with all finite support classes included in the capacity formula.

## Proof

**Alternating-interval lemma.** In the unrestricted single-deletion reconstruction graph, two different words have at least two distinct common one-deletion outputs precisely when their shortest unequal interval is an opposite-phase two-letter alternating pair. More explicitly, uniquely determined common outside words \(P,S\), letters \(a\ne b\), and length \(L\geq2\) give
\[
\{u,v\}=\{P\,a b a b\cdots\,S,\;P\,b a b a\cdots\,S\}.
\]
The two common outputs arise by deleting at opposite ends of the alternating interval. Necessity follows by aligning the two distinct common one-deletion outputs: after removing the maximal common prefix and suffix, the only possible shift-alignment directions are forward and backward, and the coexistence of both forces each interior symbol to alternate between the two endpoint letters. This unrestricted characterization also appears in the earlier exact two-read edge classification in the references. Importantly, merely having a single shared output is not sufficient.

**Homopolymer restriction and edge count.** Both opposite-phase words are legal precisely when the last letter of a nonempty prefix \(P\), and the first letter of a nonempty suffix \(S\), avoid both \(a\) and \(b\). The internal alternating segments are automatically legal. For each fixed unordered pair \(\{a,b\}\), the ordinary generating function for legal prefixes of length \(i\), with weight \(z^i\), is
\[
B(z)=1+\sum_{i\geq1}(q-2)(q-1)^{i-1}z^i
=\frac{1-z}{1-(q-1)z}.
\]
The same formula counts suffixes; an alternating interval can have any length at least two and uniquely determines one unordered edge. Consequently
\[
\sum_{n\geq2}|E(G_{q,n})|z^n
=\binom q2 B(z)^2\frac{z^2}{1-z}
=\binom q2\frac{z^2(1-z)}{(1-(q-1)z)^2}.
\]
Extracting coefficients gives the displayed edge formula, including the boundary case \(n=2\).

**Support decomposition.** The alternating-interval move changes neither the set of alphabet letters used by a word nor the outer word. Thus \(G_{q,n}\) decomposes into disconnected induced components indexed by the exact support \(T\subseteq\Sigma\), with \(2\leq|T|\leq n\). For a fixed support size \(s\), the component is independent of \(q\) up to renaming symbols. In particular, for \(n\leq5\), it is enough to verify the complete finite basis of exact-support components on \(s\leq5\) named symbols. This is a genuine reduction of the **all-alphabet theorem** to finitely many fully enumerated graphs, not an inference from sampling alphabet sizes.

For lengths \(n=2,3,4\), every nonempty exact-support component is bipartite and has a perfect matching. The accompanying standard-library checker constructs all its words and all deletion edges, performs complete two-coloring, and explicitly finds an augmenting-path perfect matching in each basis graph \((n,s)\) with \(2\leq s\leq n\leq4\). Hence every component has independent-set size exactly half its vertices, proving the first capacity formula.

For \(n=5\), the exact-support component sizes and independence numbers are

| Exact support size | Vertices | Independence number |
|---|---:|---:|
| \(2\) | \(2\) | \(1\) |
| \(3\) | \(42\) | \(19\) |
| \(4\) | \(144\) | \(72\) |
| \(5\) | \(120\) | \(60\) |

The \(s=2\) component is an edge. The \(s=4,5\) components have explicit two-colorings and perfect matchings computed by the finite verifier. The nontrivial \(s=3\) component has a displayed independent set of nineteen vertices in `verify_direct.py`. Its upper bound is certified without a numerical optimizer: twelve specified edges and six specified seven-cycles carry nonnegative rational weights whose weighted incidence at **each of the 42 vertices** is exactly one, and whose total independent-set capacity is \(39/2\). Every independent set meets an edge in at most one vertex and a seven-cycle in at most three vertices. Thus its cardinality is at most \(\lfloor39/2\rfloor=19\). The verifier checks every graph edge, each seven-cycle, every rational weight (stored doubled as integers), all 42 vertex cover equations, total weight and the nineteen-word construction directly from actual files.

Summing over alphabet supports and choosing which \(s\) letters occur gives the sharp all-alphabet expression
\[
\alpha(G_{q,5})=\binom q2+19\binom q3+72\binom q4+60\binom q5.
\]
The identity
\[
q(q-1)^4=2\binom q2+42\binom q3+144\binom q4+120\binom q5
\]
reduces this to the claimed half-space formula minus \(2\binom q3\).

**Bipartiteness threshold.** For \(q=2\), there are only the two alternating words; they form a single edge at every length \(n\geq2\). The finite support reduction above proves bipartiteness for all \(q\) when \(n\leq4\). For \(q\geq3,n=5\), the seven words, in cyclic order,

`01012`, `01021`, `01201`, `01210`, `10210`, `10120`, `10102`

form an induced seven-cycle. For any larger \(n\), prepend the same alternating prefix over the letters `2` and `0` whose last letter is `2` and whose length is \(n-5\). Every word remains homopolymer-free because its original first letter is `0` or `1`. The original two distinct common deletion descendants for each adjacent cycle pair remain distinct after prepending. This preserves a seven-cycle and proves nonbipartiteness for all \(n\geq5\).

## Verification

Run `python verify_direct.py` and `python verify_structural.py` from the directory containing these files. Both scripts use only the Python standard library and terminate with `VERIFY_DIRECT_OK` and `VERIFY_STRUCTURAL_OK`, respectively. The first constructs deletion-output incidence sets, certifies all small exact-support components, checks matchings, the rational certificate, the nineteen-word witness and the odd cycle. The second independently constructs every edge from alternating intervals and compares against independent deletion enumeration for \(2\leq q\leq5\), \(2\leq n\leq5\). All required finite cases for the general \(n\leq5\) capacity theorem are checked: arbitrary larger \(q\) requires **no new support type**.

## Relationship to prior work

Classical deletion-code bounds and multiread sequence-reconstruction studies motivate the setting. Published unrestricted two-read research already establishes the alternating-interval edge characterization and an unrestricted edge count; the displayed homopolymer-restricted edge count alone is therefore not claimed to constitute the principal new contribution. Earlier published short-length two-read capacities apply to the unrestricted alphabet language, whereas the present sharp support-decomposed capacity is for the constrained Kautz language and shows the first nonbinary failure of a half-space optimum. Work on homopolymer-free codes with Hamming errors does not determine these deletion-reconstruction independent sets.

## Limitations

The capacity theorem is only for lengths two through five. The existence of an induced seven-cycle at length five does not assert that seven is the minimum odd girth at all lengths. A seven-cycle at longer lengths is not asserted induced. No efficient decoder or optimal-length code construction for longer lengths is established. The exact small-support verification is a complete finite proof only because the support-decomposition lemma reduces every required alphabet size to those checked graphs. Unindexed or inaccessible literature may affect priority; the result has not been independently audited.

## References

- D. Cullina and N. Kiyavash, *An Improvement to Levenshtein's Upper Bound on the Cardinality of Deletion Correcting Codes*, arXiv:1302.6562 (first posted 2013-02-26), https://arxiv.org/abs/1302.6562.
- F. Sala, R. Gabrys, C. Schoeny and L. Dolecek, *Exact Reconstruction from Insertions in Synchronization Codes*, arXiv:1604.03000 (first posted 2016-04-11), https://arxiv.org/abs/1604.03000.
- K. Cai, H. M. Kiah, T. T. Nguyen and E. Yaakobi, *Coding for Sequence Reconstruction for Single Edits*, arXiv:2001.01376 (first posted 2020-01-06), https://arxiv.org/abs/2001.01376.
- K. G. Benerjee and A. Banerjee, *Bounds on Size of Homopolymer Free Codes*, arXiv:2305.10741 (first posted 2023-05-18), https://arxiv.org/abs/2305.10741.
- *Exact edge count of the finite-alphabet two-read single-deletion reconstruction graph*, publicly indexed mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-edge-count-of-the-finite-alphabet-two-read-single-deletion--737fed325e91.
