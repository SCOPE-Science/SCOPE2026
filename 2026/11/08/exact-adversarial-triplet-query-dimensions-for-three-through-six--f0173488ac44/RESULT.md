# Exact adversarial triplet-query dimensions for three through six rooted taxa

## Finding

For an integer \(n\in\{3,4,5,6\}\), let \(X_n=\{0,\ldots,n-1\}\), and let \(\mathcal T_n\) be the set of rooted, non-plane, strictly binary phylogenetic trees with leaf set \(X_n\). A binary query is a rooted triple \(ab\mid c\), where \(a,b,c\in X_n\) are distinct, \(a<b\), and the answer is one precisely when the restriction of the unknown tree to \(\{a,b,c\}\) has \(a,b\) as its cherry. Let \(\mathcal H_n\subseteq\{0,1\}^{Q_n}\) be the resulting class of query-response functions.

The exact Littlestone dimensions are

\[
\big(\operatorname{Ldim}(\mathcal H_3),\operatorname{Ldim}(\mathcal H_4),\operatorname{Ldim}(\mathcal H_5),\operatorname{Ldim}(\mathcal H_6)\big)=(1,3,5,9).
\]

In particular, \(\mathcal H_6\) attains the sharp information bound \(\lfloor\log_2 945\rfloor=9\), whereas \(\mathcal H_5\) falls one short of its cardinality bound \(\lfloor\log_2 105\rfloor=6\). The finding concerns adversarial, adaptive *binary yes/no rooted-triplet incidence* queries, not a three-way oracle that reveals the entire induced triple topology.

## Assumptions and scope

All labels are distinct and trees are rooted and fully binary, with no edge lengths or plane orientations. Every leaf labeling is allowed. There are exactly \((2n-3)!!\) such trees, giving \(3,15,105,945\) for \(n=3,4,5,6\). The query set contains \(3\binom n3\) distinct binary predicates. A complete adversarial query tree of depth \(d\) has a query at each internal binary node, chosen as a function of preceding answers, and requires at least one tree consistent with every length-\(d\) answer string. The Littlestone dimension is the maximum such \(d\). Queries may be reused on different branches but not effectively repeated on a single branch of a complete witness.

## Proof

**Upper bounds by the number of concepts.** Distinct leaves of a complete depth-\(d\) adversarial query tree have incompatible answer histories, hence require at least \(2^d\) distinct tree concepts. Since the class sizes are \(3,15,105,945\), this gives the respective bounds \(1,3,6,9\). For \(n=3,4,6\) these bounds are sharp, as certified constructively below.

**The exceptional upper bound at five taxa.** Fix any first query \(q=ab\mid c\). Exactly 35 of the 105 rooted binary trees answer yes: the 105 trees restrict equally often to each of the three topologies on \(\{a,b,c\}\), by relabeling symmetry. Call this 35-tree subfamily \(P_q\). If a complete depth-six query tree existed on all 105 trees, its yes branch would have to support depth five. A depth-five tree on a 35-element class requires its first query to split that class into two children of cardinality at least 16. Direct enumeration of the 30 admissible queries reveals **exactly one** query satisfying this necessary condition for \(P_q\), and it produces children of sizes 17 and 18. In its 17-tree child, every one of the 30 possible queries produces a smaller child of size at most seven. A complete depth-four tree on 17 hypotheses would instead require a first split into two groups of at least eight hypotheses, a contradiction. This establishes \(\operatorname{Ldim}(\mathcal H_5)\le5\). The stated exhaustive inequalities are replayed for *every* choice of the first query in the supplied verifier, rather than relying on a single unverified symmetry representative.

**Constructive lower bounds.** The file `rooted_triplet_strategy.json` supplies four fully explicit, complete binary adversarial query trees of depths \(1,3,5,9\), respectively. The query at heap-indexed internal node \(i\) is its listed integer triple \([a,b,c]\); its negative and positive successors have indices \(2i+1\) and \(2i+2\). The independent checker builds every tree by inserting each new leaf above each existing subtree (including the root), calculates least-common-ancestor depths, and follows every branch of each certificate. At every leaf, its remaining concept set is nonempty; the sets at all leaves are disjoint and cover all concepts. In the six-taxon certificate, exactly 511 query nodes yield 512 nonempty answer histories. Thus the certified depths are lower bounds. Combining them with the preceding upper bounds proves the displayed formula.

**Justification of the enumeration.** Starting with the unique two-leaf rooted tree, insertion of the next taxon above any one of the \(2k-1\) subtrees of a rooted binary \(k\)-leaf tree generates every rooted binary \((k+1)\)-leaf tree exactly once: delete the newest leaf and suppress its now-degree-two parent to recover the unique predecessor and insertion position. Therefore the enumeration is exhaustive, not sampled. For each tree, the query \(ab\mid c\) is true precisely when the depth of the least common ancestor of \(a,b\) strictly exceeds that of \(a,c\). The verifier derives these depths independently of the recursive split construction that produced the certificate.

## Verification

Use Python 3, standard library only, in a directory containing the two accompanying files:

```bash
python3 verify_rooted_triplet_online.py rooted_triplet_strategy.json
```

The verifier prints `ROOTED_TRIPLET_ONLINE_PASS` and reports the counts of trees, queries, internal certificate nodes, and remaining concepts at the leaves for each \(n\). It checks every rooted binary tree through six taxa, every branch of each strategy, and the exceptional five-taxon upper-bound inequalities over all 30 possible first queries. The certificate-generating calculation additionally compared an independent recursive-root-split enumeration against a successive-leaf-insertion enumeration; each gave the same trees and query-response data.

## Relationship to prior work

Huber, Moulton, and Steel (first arXiv version 2017) characterize *static phylogenetic flexibility*: when arbitrary choices of rooted triple topologies on given three-element taxon subsets can be jointly displayed. Their thin-set criterion is a prior structural result, not a new assertion here. Hellmuth and Seemann (2017 preprint; 2018 journal article) study closure and a matroid of representative positive rooted-triple constraints. Walker (2022) gives general combinatorial results about tree and Littlestone dimensions. Semple and Toft (2020) discuss the fact that a complete set of rooted triples encodes a rooted binary tree. None of those statements alone yields a nine-level adaptive *binary incidence* mistake tree for six taxa or the exceptional non-saturation at five taxa. These works concern different invariants and are not asserted to prove the present exact online profile.

## Limitations

The theorem and certificates concern only \(3\le n\le6\). No extrapolation to larger \(n\), nonbinary trees, networks, three-way triplet answers, random instances, or online algorithms with computational constraints is made. The finite certificates provide ordinary exhaustive mathematical evidence, not an independently audited proof. Historical priority of an exactly equivalent finite online-query result under specialized terminology cannot be ruled out solely by literature search.

## References

1. M. Hellmuth and C. R. Seemann, *The Matroid Structure of Representative Triple Sets and Triple-Closure Computation*, arXiv:1707.01667, first posted 2017-07-06; *European Journal of Combinatorics* 70 (2018), 384–407. https://arxiv.org/abs/1707.01667
2. K. T. Huber, V. Moulton, and M. Steel, *Phylogenetic Flexibility via Hall-Type Inequalities and Submodularity*, arXiv:1710.08946, first posted 2017-10-24; *Bulletin of Mathematical Biology* 81 (2019), 598–617. https://arxiv.org/abs/1710.08946
3. R. Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211, first posted 2022-03-23. https://arxiv.org/abs/2203.12211
4. C. Semple and G. Toft, *Trinets Encode Orchard Phylogenetic Networks*, arXiv:2012.02231, first posted 2020-12-03. https://arxiv.org/abs/2012.02231
