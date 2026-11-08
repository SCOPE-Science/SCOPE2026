# Affine strict-peak profiles under random relabeling of finite mappings

## Finding

**Theorem.** Let \(n\ge4\), let \(f:[n]\to[n]\) be any deterministic map, let \(\tau\) be uniform on the symmetric group \(S_n\), and put \(F=\tau\circ f\circ\tau^{-1}\). For \(2\le i\le n-1\), define the *strict-peak probability*
\[
p_i=\mathbb P\bigl(F(i-1)<F(i)>F(i+1)\bigr).
\]
Write \(T=\binom n3\) and \(d_v=|f^{-1}(v)|\). Define
\[
Z=\sum_{v\in[n]}\binom{d_v}{3},\qquad
M=\sum_{v\in[n]}\binom{d_v}{2}(n-d_v).
\]
Let \(c_1\) count fixed points of \(f\), and let \(c_3\) count its directed 3-cycles (each cycle counted once). Consider each unordered source triple \(S\subset[n]\) for which its three successor images consist of a *double* image \(u\) and a different *single* image \(v\). Let \(M_+\) count these source triples for which \(v\in S\) and \(u\notin S\); let \(M_-\) count those for which \(u\in S\) and \(v\notin S\).

Then, **simultaneously for all interior positions**,
\[
\boxed{\displaystyle
p_i=\frac13-\frac{2Z+M+2\binom{c_1}{3}-c_3}{6T}
+\frac{M_+-M_-}{3T(n-3)}\left(i-\frac{n+1}{2}\right).}
\]
Consequently all position-resolved peak probabilities form an exact arithmetic progression, with slope \((M_+-M_-)/(3T(n-3))\). Its sign has the complete combinatorial classification \(\operatorname{sgn}(M_+-M_-)\). The mean across interior positions depends only on the indegree histogram and the fixed-point and 3-cycle counts:
\[
\frac1{n-2}\sum_{i=2}^{n-1}p_i
=\frac13-\frac{2Z+M+2\binom{c_1}{3}-c_3}{6T}.
\]

Both nonzero slope signs occur. For \(n=4\), representing \(f\) by its values on \(0,1,2,3\) rather than \([4]\) merely for these examples, \(f=(0,0,0,3)\) yields \((p_2,p_3)=(1/12,1/6)\), whereas \(f=(0,0,1,2)\) yields \((7/24,5/24)\).

## Assumptions and scope

The vertex set has \(n\ge4\) elements, and the only randomness is a uniformly random simultaneous relabeling of *both* the domain and codomain of a fixed map. The map need not be injective, surjective, connected, or random under a uniform mapping law. The comparisons are strict; repeated outputs cannot constitute a peak. Binomial coefficients \(\binom ab\) vanish when \(a<b\). The ordered word \(F(1),\ldots,F(n)\) is a word with possible ties, not generally a permutation.

## Proof

Choose a uniform ordering \(x_1,\ldots,x_n\) of the original vertices and give \(x_j\) new label \(j\). Then \(F(j)\) is the new label of \(f(x_j)\). At positions \(i-1,i,i+1\), the *unordered* set \(S=\{x_{i-1},x_i,x_{i+1}\}\) is uniform among \(T\) triples, and its six orders are equiprobable. Every successor outside \(S\) has its new label strictly below \(i-1\) or above \(i+1\); there are \(i-2\) available lower labels and \(n-i-1\) upper labels, among \(n-3\) outside labels.

We compute the peak probability conditionally on \(S\). There are three mutually exclusive kinds of successor multisets.

**One successor image.** If all three images are identical, a strict peak is impossible, yielding conditional probability zero. Exactly \(Z\) source triples have this property.

**Two successor images.** Suppose \(f(S)\) consists of a repeated target \(u\) and a unique target \(v\). The source having image \(v\) must occupy the central position, an event of conditional probability \(1/3\); it is then necessary and sufficient that the new label of \(v\) exceed that of \(u\). When both targets lie inside \(S\), their relative order is symmetric and gives probability \(1/6\); when both lie outside, their relative order is also symmetric and gives \(1/6\). If \(v\in S\) and \(u\notin S\), the target \(v\) exceeds \(u\) exactly when the outside target \(u\) receives one of the \(i-2\) lower outside labels. The conditional peak probability is therefore \((i-2)/(3(n-3))\). If \(u\in S\) and \(v\notin S\), the outside target \(v\) must receive an upper outside label, giving \((n-i-1)/(3(n-3))\). Thus all \(M\) two-image source triples contribute a baseline \(1/6\), and the \(M_+\) and \(M_-\) exceptional triples contribute, relative to that baseline, respectively
\[
+\frac{i-(n+1)/2}{3(n-3)},\qquad
-\frac{i-(n+1)/2}{3(n-3)}.
\]

**Three distinct successor images.** If at least one target lies outside \(S\), the conditional peak probability is exactly \(1/3\). To check this without a symmetry assumption on \(f\), condition on the labels of all outside vertices. If the highest among the three image labels belongs to an outside vertex, its uniquely determined source occurs in the central position in exactly two of the six possible orders. Otherwise every outside image is below the block, so the highest image is among the one or two targets *inside* \(S\). With one internal target, its uniquely determined source is central in two of the six orders. With two internal targets \(v,w\), their distinct preimages within \(S\) may coincide with either target or the third vertex. Directly placing the two targets and two source vertices in the three ordered positions shows that in exactly two of the six orders, the source of whichever target has the later position is central. (The six-order statement holds for every injection of two sources into two distinct members of \(S\), including all identifications between sources and targets.) Therefore this entire case has baseline \(1/3\).

The only remaining case is \(f(S)=S\) with three distinct images, i.e. \(f|_S\) permutes \(S\). For a fixed order, \(F(i)\) is a strict peak precisely when the source at the central position maps to the target at the largest of the three labels. For each source \(x\in S\) that is not a fixed point of \(f|_S\), there is exactly one ordering placing \(x\) centrally and \(f(x)\) last; there are no such orderings for a fixed point. Hence the conditional probability is \((3-\#\mathrm{Fix}(f|_S))/6\). Its deviation from the \(1/3\) baseline is zero for a transposition plus a fixed point, \(-1/3\) for three fixed points, and \(+1/6\) for a single directed 3-cycle. There are exactly \(\binom{c_1}{3}\) triples of the first exceptional type and exactly \(c_3\) triples of the second type.

**Assembly.** Start with \(1/3\) for each of the \(T\) source triples. The all-equal triples subtract \(Z/3\), the two-image triples subtract \(M/6\), the all-fixed invariant triples subtract \(\binom{c_1}{3}/3\), and the directed 3-cycle triples add \(c_3/6\). Add the signed position-dependent two-image corrections above and divide by \(T\). This is the displayed formula. Averaging over \(2\le i\le n-1\) cancels its centered linear term. No limiting argument is used. \(\square\)

## Verification

The attached standalone Python 3 program `verify.py` computes the six-order incidence counts via direct independent enumeration of all \(n!\) relabelings and compares them to the closed formula using integer and rational arithmetic. It checks every map on \(4\) and \(5\) vertices, and deterministic-seed samples of maps on \(6\), \(7\), and \(8\) vertices: `VERIFY_OK 10603 exact assertions`. This finite verification is not used as a substitute for the proof above.

## Relationship to prior work

Leckey–Wormald [1] analyze random functional graphs with fixed indegree sequences, specifically orbit/six-length rather than local successor-word peaks. Mutafchiev–Finch [2] analyze the deepest cycle of a uniformly random mapping. Their graph objects motivate this question but their stated theorems do not imply an exact fixed-map, uniformly relabeled local peak profile. Fulman–Kim–Lee [3] develop peak-count results for *bijective* maps in symmetric-group conjugacy classes. Gessel–Zhuang [4] develop broad exact peak and cycle-type generating functions for permutations. Indeed, the bijective specialization of the theorem should be treated as contextual, not an independent novelty assertion; the contribution is the universal noninjective mapping statement and its signed coalescence-motif slope.

## Limitations

The result concerns one-position strict peak probabilities, not joint peak distributions or an algorithm to reconstruct the map from observed peaks. Two nonisomorphic maps can share its stated motif parameters. The specific antecedents inspected do not establish complete historical uniqueness; earlier general pattern-enumeration or functional-digraph labeling identities might imply the formula. Independent mathematical review remains unperformed.

## References

[1] Kevin Leckey and Nicholas Wormald, *A limit theorem for the six-length of random functional graphs with a fixed degree sequence* (arXiv:1803.02667, first posted 2018-03-07). https://arxiv.org/abs/1803.02667

[2] Ljuben Mutafchiev and Steven Finch, *On the Deepest Cycle of a Random Mapping* (arXiv:2301.13829, first posted 2023-01-31). https://arxiv.org/abs/2301.13829

[3] Jason Fulman, Gene B. Kim and Sangchul Lee, *Central limit theorem for peaks of a random permutation in a fixed conjugacy class of \(S_n\)* (arXiv:1902.00978, first posted 2019-02-03). https://arxiv.org/abs/1902.00978

[4] Ira M. Gessel and Yan Zhuang, *Plethystic formulas for permutation enumeration* (arXiv:2001.00654, first posted 2020-01-02). https://arxiv.org/abs/2001.00654
