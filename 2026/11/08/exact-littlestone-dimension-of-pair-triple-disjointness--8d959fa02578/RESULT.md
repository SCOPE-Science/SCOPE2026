# Exact Littlestone dimension of pair–triple disjointness

## Finding
For every integer \(n\ge3\), let the hypothesis set be \(\mathcal H_n=\binom{[n]}{2}\), let the query set be \(\mathcal X_n=\binom{[n]}{3}\), and define the binary concept \(f_P(Q)=1\) if and only if \(P\cap Q=\varnothing\). Then the ordinary realizable Littlestone dimension is exactly
\[
\operatorname{Ldim}(\{f_P:P\in\mathcal H_n\})=
\begin{cases}
0,&3\le n\le4,\\
1,&n=5,\\
2,&n=6,\\
3,&n=7,\\
4,&n\in\{8,9\},\\
5,&n\ge10.
\end{cases}
\]
In particular, \(n=10\) is the smallest ground-set order permitting a complete depth-five mistake tree, and dimension five is a universal ceiling, irrespective of the order. Both parameter sides are essential: centers are *pairs* and queries are *triples*; the result is not a theorem about the symmetric rank-two or rank-three Kneser graphs.

## Assumptions and scope
The ground set \([n]=\{1,\ldots,n\}\) is finite. Hypotheses are all *unordered distinct-element pairs*; queries are all *unordered distinct-element triples*. Membership is strict disjointness, with label 1 meaning disjoint and label 0 meaning intersecting. Queries may be chosen adaptively according to preceding labels. A complete binary query tree of depth \(d\) is shattered if every one of its \(2^d\) root-to-leaf label sequences is realized by some fixed hypothesis. The dimension is the maximum such depth; a nonempty constant class has dimension zero. The result does not classify ordinary VC dimension, randomized mistake bounds, higher-uniformity incidences, or arbitrary set systems.

## Proof
We use two elementary observations. First, a concept class with \(m\) distinct hypotheses cannot shatter a complete tree of depth exceeding \(\lfloor\log_2m\rfloor\), since the \(2^d\) leaves need distinct witnesses. Second, if for every possible root query at least one nonempty branch of a class has Littlestone dimension at most \(t\), then the entire class has dimension at most \(t+1\): a shattered tree of depth \(t+2\) would require both root branches to shatter depth \(t+1\).

**Uniform upper bound.** Fix \(S\subseteq[n]\) and define \(\mathcal F(S)=\{P\in\binom{[n]}2:P\cap S\ne\varnothing\}\), regarded as a restricted version space under triple queries. We prove the three bounds
\[
\operatorname{Ldim}(\mathcal F(S))\le 1+|S|\quad\text{for }|S|\in\{1,2,3\}.
\]
For \(|S|=1\), say \(S=\{a\}\), a query \(Q\) containing \(a\) has an empty positive branch. If \(a\notin Q\), the negative branch has at most three hypotheses \(\{a,q\}\), \(q\in Q\), and therefore has dimension at most one. Every root thus has a branch of dimension at most one, proving dimension at most two.

For \(|S|=2\), if \(Q\cap S\ne\varnothing\), the positive branch is contained in \(\mathcal F(S\setminus Q)\) with at most one marked element and therefore has dimension at most two. If \(Q\cap S=\varnothing\), the negative branch consists only of pairs \(\{s,q\}\) with \(s\in S\), \(q\in Q\), at most six hypotheses, so it has dimension at most \(\lfloor\log_2 6\rfloor=2\). This gives dimension at most three.

For \(|S|=3\), if \(Q\cap S\ne\varnothing\), the positive branch is contained in \(\mathcal F(S\setminus Q)\), now with at most two marked elements, of dimension at most three. If \(Q\cap S=\varnothing\), the negative branch consists of at most nine pairs with one endpoint in each of \(Q\) and \(S\); its dimension is at most \(\lfloor\log_2 9\rfloor=3\). This gives dimension at most four. A query \(Q\) at the root of the **unrestricted** pair class has negative branch exactly \(\mathcal F(Q)\), of dimension at most four. Thus the full dimension is at most five for all \(n\ge3\). Empty positive branches and repeated concepts cause no exception.

**Sharper small-order upper bounds.** For any triple query \(Q\), the positive branch comprises precisely \(\binom{n-3}{2}\) pairs. A depth-\(d\) shattered tree would require at least \(2^{d-1}\) hypotheses in *both* root branches, and in particular in this positive branch. For \(n=3,4\) that branch is empty, forcing dimension zero. At \(n=5,6,7,8,9\) it has respectively \(1,3,6,10,15\) hypotheses, yielding ceilings \(1,2,3,4,4\). (These are sharper than the uniform bound wherever needed.)

**Sharp lower bounds.** The accompanying standalone `TREES.json` contains five explicit complete mistake trees, for \((n,d)=(5,1),(6,2),(7,3),(8,4),(10,5)\). Every internal node names a three-element query; its `no` branch is the intersecting response and its `yes` branch is the disjoint response. Every terminal node names an actual two-element witness. In each tree, for all \(2^d\) paths, the named witness yields exactly the path's sequence of answers. This finite certificate is a complete construction: `VERIFY.py` independently reconstructs both branch version spaces, verifies every query is a triple of \([n]\), verifies each witness is a pair still feasible at its leaf, and verifies that all \(2^d\) witnesses are distinct. The five verified leaf counts are \(2,4,8,16,32\). The \(n=8\) tree also works for \(n=9\), and the \(n=10\) tree embeds verbatim into every \(n\ge10\), because all its queries and witnesses use only \([10]\). Combined with the upper bounds, this proves the formula for every \(n\ge3\). The certificates prove finite lower bounds only; the uniform upper bound is proved algebraically above.

## Verification
Place `TREES.json` and `VERIFY.py` in the same folder, then run `python VERIFY.py` using Python 3.9 or later (standard library only). The verifier checks the five full trees without assuming the dimension formula, then independently evaluates the exact minimax recursion
\[
L(V)=\max_{Q\in\mathcal X_n}\left(1+\min\{L(V\cap\{f_P(Q)=0\}),L(V\cap\{f_P(Q)=1\})\}\right),
\]
restricting the maximum to queries splitting \(V\) into two nonempty subsets, and defining \(L(V)=0\) if no such query exists. The independent complete recursion verifies the exact dimensions for \(3\le n\le8\). Its terminal success line is `PAIR_TRIPLE_ALL_CHECKS_PASS`. No finite enumeration or timeout is used to establish the universal upper bound.

## Relationship to prior work
Disjointness and restricted set systems appear centrally in Bhattacharya et al. (2020), whose objectives are communication-complexity bounds for classes controlled by VC dimension. Benediktsson, Macpherson and Adler (2020) investigate VC dimension and density of **symmetric Johnson/Hamming open-neighborhood** families; the present bipartite pair-center/triple-query relation has a different parameter domain and uses *adaptive* shattering. Chase, Freitag and Reyzin (2023) provide broader learning-theoretic uses of Littlestone dimension, not this fixed-uniformity exact computation. Exact all-order adaptive results for pair/pair Kneser disjointness and finite triple/triple Kneser disjointness are also different: neither entails the rank-five sharp threshold for pair/triple incidence. In particular, transposing or complementing the pair/triple incidence relation does not turn it into either symmetric same-rank relation. These are implication comparisons, not claims of global historical priority.

## Limitations
The theorem is restricted to the specified two-uniform hypotheses and three-uniform queries with strict disjointness. It gives deterministic realizable mistake-tree dimension, not a general disjointness communication-complexity classification. Independent mathematical audit and comprehensive historical-priority verification have not been performed; equivalent exact formulas could exist under asymmetric Kneser incidence, sparse Boolean learning, or model-theoretic stability terminology. The certificate verifies the five finite lower-bound trees and finite minimax cases; it does not mechanically verify the general upper-bound proof, which is supplied in full above.

## References
[1] A. Bhattacharya, S. Chakraborty, A. Ghosh, G. Mishra, M. Paraashar, *Disjointness through the Lens of Vapnik-Chervonenkis Dimension: Sparsity and Beyond*. arXiv:2006.13712v1, first public 2020-06-24. https://arxiv.org/abs/2006.13712

[2] B. G. Benediktsson, D. Macpherson, I. Adler, *Vapnik-Chervonenkis Dimension and Density on Johnson and Hamming Graphs*. arXiv:2007.16042v1, first public 2020-07-31. https://arxiv.org/abs/2007.16042

[3] H. Chase, J. Freitag, L. Reyzin, *Applications of Littlestone dimension to query learning and to compression*. arXiv:2310.04812v1, first public 2023-10-07. https://arxiv.org/abs/2310.04812
