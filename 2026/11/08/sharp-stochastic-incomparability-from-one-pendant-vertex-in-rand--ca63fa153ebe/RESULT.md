# Sharp stochastic incomparability from one pendant vertex in random-greedy independent sets

## Finding

**Theorem.** For every integer \(m\ge3\), start with the star \(G_m=K_{1,m}\), select one leaf, and attach one further private leaf to it, obtaining \(G_m^+\). On each graph, inspect its vertices in a uniform random order and retain a vertex exactly when none of its earlier retained neighbors is adjacent to it. Let \(I_m\) and \(I_m^+\) count the retained vertices. Their complete probability laws are
\[
\Pr(I_m=1)=\frac1{m+1},\quad \Pr(I_m=m)=\frac m{m+1},
\]
\[
\Pr(I_m^+=2)=\frac{m+1}{m(m+2)},\quad
\Pr(I_m^+=m)=1-\frac{m+1}{m(m+2)}.
\]
All unlisted probabilities are zero. Consequently,
\[
\Pr(I_m^+\ge2)-\Pr(I_m\ge2)=\frac1{m+1}>0,
\]
\[
\Pr(I_m^+\ge m)-\Pr(I_m\ge m)
=-\frac1{m(m+1)(m+2)}<0.
\]
The laws are therefore **incomparable in first-order stochastic order** even though adding the leaf strictly increases the expectation:
\[
\mathbb E I_m^+-\mathbb E I_m
=\frac{m^2+m+2}{m(m+1)(m+2)}>0.
\]
This phenomenon first occurs at original connected graph order four: every connected graph of order at most three has stochastic domination \(I(G)\le_{\mathrm{st}}I(G^+)\) for every single pendant extension \(G^+\).

## Assumptions and scope

Graphs are finite, simple, undirected. The original star has one hub adjacent to \(m\) leaves; its extension adds a new vertex adjacent only to one previously degree-one leaf. The algorithm is **vertex-order random greedy maximal independent set**, not edge-order greedy matching, maximum independent set optimization, or uniform sampling over maximal independent sets. Both graph laws use their respective uniform vertex permutations. For random variables \(X,Y\), \(X\le_{\mathrm{st}}Y\) means \(\Pr(X\ge k)\le\Pr(Y\ge k)\) at every integer \(k\). “Smallest original order” restricts to connected original graphs, irrespective of labels.

## Proof

A uniform random vertex permutation may be exposed by choosing its first vertex uniformly and then ordering the remaining vertices uniformly. Once a vertex is accepted, remove it and all its neighbors; the greedy process on the residual induced graph is an independent uniform-order greedy process.

On \(G_m\), the hub is first with probability \(1/(m+1)\), giving one retained vertex. Otherwise some leaf appears first, forcing the hub to be rejected; every leaf is ultimately retained, so the size is \(m\). This proves the first law.

On \(G_m^+\), write \(c\) for the hub, \(a\) for the distinguished old leaf, and \(w\) for its newly attached leaf. There are \(m+2\) vertices. Partition on the first inspected vertex:

* If it is \(c\), which occurs with probability \(1/(m+2)\), all old leaves are rejected and \(w\) is isolated and accepted, yielding size two.
* If it is \(w\), also with probability \(1/(m+2)\), then \(a\) is rejected and the remaining vertices induce \(K_{1,m-1}\). That star contributes one selected vertex with probability \(1/m\), giving size two in this branch, and contributes \(m-1\) vertices otherwise, giving total size \(m\).
* If it is \(a\), the hub and \(w\) are rejected and the other \(m-1\) leaves are accepted; total size \(m\).
* If it is one of the remaining \(m-1\) old leaves, the hub is rejected and the edge \(aw\) plus the other \(m-2\) isolated leaves remain. The edge contributes exactly one selected vertex; total size \(m\).

Thus the size-two probability is \((1+1/m)/(m+2)=(m+1)/(m(m+2))\) and the complementary probability is supported on size \(m\), proving the second law. Comparing upper tails at the thresholds two and \(m\) gives the displayed strict inequalities. Directly subtracting the exact expectations yields the stated positive rational expression.

For minimality, every connected graph on at most three vertices is isomorphic to one of \(K_1,K_2,P_3,K_3\). For \(K_1\) and \(K_2\), the original greedy size is constantly one and all pendant extensions have size at least one. For \(K_3\), the original greedy size is also constantly one. For \(P_3\), the original size is one with probability \(1/3\) and two with probability \(2/3\). Attaching a pendant at a path endpoint yields \(P_4\), for which every maximal independent set has size two. Attaching at the middle yields \(K_{1,3}\), whose greedy size is one with probability \(1/4\) and three with probability \(3/4\). In either case the extension stochastically dominates the original. Since \(K_{1,3}\) produces incomparability on extension, the four-vertex bound is sharp.

## Verification

The accompanying `verify.py` evaluates the vertex-first decomposition with exact rational arithmetic. It checks every connected labeled graph of order at most three and all possible pendant attachment vertices against every integer stochastic-order threshold, and compares the stated laws and crossing/mean identities on stars with three through eight leaves. It completed `VERIFY_OK 179 exact assertions`. This is supporting finite evidence; the proof above establishes the formulas and all-parameter assertions without relying on finite enumeration.

Run: `python3 verify.py` (standard library only).

## Relationship to prior work

Krivelevich, Mészáros, Michaeli and Shikhelman (first posted July 16, 2019) develop the random-order greedy maximal-independent-set model, including tree extremizers for **expected size**. Their Section 8 states that even natural monotonicity of *expected* greedy independent-set size under edge deletion fails; it does not give the present pendant-extension upper-tail crossing. The general theory and the star's unextended distribution are prior knowledge, not claimed as new. Here the derived full extension law, infinite family of opposing tails, and sharp connected-order boundary are the finite distributional statement.

This contrast differs in both object and implication from random-greedy **edge matching** under private-leaf augmentation, for which pathwise cardinality monotonicity may hold. There is no claim of novelty for the underlying first-vertex recursion.

## Limitations

The theorem concerns this explicit family and establishes the smallest *connected-original-graph* obstruction. It does not classify all pendant extensions, establish that expected greedy independent-set size always increases under a pendant extension, or address independence-number optimization. The first-vertex recursion is elementary; literature priority for the specific distributional crossing has not been independently certified.

## References

1. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy maximal independent sets via local limits*, arXiv:1907.07216 (first posted 2019-07-16), https://arxiv.org/abs/1907.07216 ; *Random Structures & Algorithms*, DOI:10.1002/rsa.21200.
2. M. Krivelevich, T. Mészáros, P. Michaeli, C. Shikhelman, *Greedy Maximal Independent Sets via Local Limits*, AofA 2020, DOI:10.4230/LIPIcs.AofA.2020.20, https://doi.org/10.4230/LIPIcs.AofA.2020.20.
