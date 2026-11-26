# Endpoint-degree law for cycle–adjacency covariance in uniform permutations

## Finding

Let \(n\ge2\), let \(\Pi\) be uniformly distributed on permutations of \([n]=\{1,\ldots,n\}\), and let \(K(\Pi)\) be its number of disjoint cycles, including fixed points. For an arbitrary deterministic simple undirected graph \(H\) on \([n]\), define the count of allowed neighboring **values** in one-line notation by
\[
B_H(\Pi)=\sum_{i=1}^{n-1}\mathbf1_{\{\Pi(i),\Pi(i+1)\}\in E(H)}.
\]
Write \(e=|E(H)|\), \(d_j=\deg_H(j)\), and let \(P_n\) be the reference path with edges \(\{i,i+1\}\) for \(1\le i<n\). Put \(c=|E(H)\cap E(P_n)|\). Then the **exact all-graph covariance identity** is
\[
\boxed{\operatorname{Cov}(K(\Pi),B_H(\Pi))
=\frac{c+2e/n-d_1-d_n}{n(n-1)}.}
\]
Thus the sign is completely classified by the graph quantity \(c+\overline d-d_1-d_n\), where \(\overline d=2e/n\) is the mean degree. Complementing \(H\) reverses the covariance sign.

In particular, for every \(n\ge3\), the reference path gives strictly positive covariance,
\[
\operatorname{Cov}(K,B_{P_n})=\frac{(n-2)(n+1)}{n^2(n-1)}>0.
\]
Let \(S_{n,j}\) denote the star whose central vertex is labeled \(j\). Two *isomorphic stars* have opposite signs:
\[
\operatorname{Cov}(K,B_{S_{n,1}})=-\frac{n-2}{n^2}<0,
\qquad
\operatorname{Cov}(K,B_{S_{n,2}})=\frac{2}{n^2}>0.
\]
At \(n=2\), every such covariance is zero.

## Assumptions and scope

The randomness is uniform over all \(n!\) permutations and is not a random ordering independent of a separate permutation. The cycle statistic and the value-adjacency statistic are measured on the **same** permutation, in its functional and one-line representations respectively. Graph \(H\) may be empty, complete, disconnected, or arbitrary; there are no degree, sparsity, or asymptotic assumptions. Edges are unordered and simple. The reference path depends on the fixed numerical labeling of vertices; graph relabeling need not preserve this joint law.

## Proof

For \(m\ge0\), write \(h_m=\sum_{r=1}^m1/r\), with \(h_0=0\). Uniform cycle insertion shows \(\mathbb E K(\Pi)=h_n\): in passing from a uniform permutation on \([n-1]\) to one on \([n]\), the new element forms a singleton cycle with probability \(1/n\) and is otherwise inserted immediately after one of the previous elements, each with probability \(1/n\).

**Contraction lemma.** Fix \(1\le i<n\), and distinct \(a,b\in[n]\). Then
\[
\mathbb E\bigl[K(\Pi)\mid \Pi(i)=a,\ \Pi(i+1)=b\bigr]
=h_{n-2}+\mathbf1_{a=i}+\mathbf1_{b=i+1}
+\mathbf1_{a=i+1,\ b=i}.
\]
To verify the lemma, draw the two forced functional arrows \(i\to a\) and \(i+1\to b\). Because the tails and heads are distinct, their directed components consist of closed cycles and directed paths. Exactly two arrows are fixed, so after removing any already closed forced cycles, there are exactly \(n-2\) (possibly singleton) open directed paths. Every uniform completion of the partial permutation pairs their terminal vertices bijectively with their initial vertices; this is a uniform permutation of those \(n-2\) paths. Its expected cycle count is \(h_{n-2}\). The only closed forced cycles are the loop \(i\to i\), the loop \(i+1\to i+1\), and the two-cycle \(i\to i+1\to i\), as encoded by the three indicators. This also covers \(n=2\) with zero remaining paths.

Set \(J_i=\mathbf1_{\{\Pi(i),\Pi(i+1)\}\in E(H)}\). The pair \((\Pi(i),\Pi(i+1))\) is uniformly distributed over the \(n(n-1)\) ordered distinct image pairs, so
\[
\mathbb E J_i=\frac{2e}{n(n-1)}.
\]
Sum the contraction-lemma expectation over the two orientations of every edge of \(H\). Terms corresponding to \(a=i\) occur \(d_i\) times, those corresponding to \(b=i+1\) occur \(d_{i+1}\) times, and the exceptional two-cycle term occurs once exactly when \(\{i,i+1\}\in E(H)\). Therefore
\[
\mathbb E[KJ_i]
=\frac{2e h_{n-2}+d_i+d_{i+1}
+\mathbf1_{\{i,i+1\}\in E(H)}}{n(n-1)}.
\]
Summing over \(i=1,\ldots,n-1\) gives
\[
\mathbb E[KB_H]
=\frac{2e(n-1)h_{n-2}+4e-d_1-d_n+c}{n(n-1)},
\qquad
\mathbb E B_H=\frac{2e}{n},
\]
because \(\sum_{i=1}^{n-1}(d_i+d_{i+1})=4e-d_1-d_n\). Subtract \(\mathbb E K\,\mathbb E B_H\) and use
\[
h_n-h_{n-2}=\frac1{n-1}+\frac1n.
\]
This simplifies exactly to the asserted graph formula. The sign criterion is immediate from the positive denominator.

For the complement of \(H\), the data become \(e'=\binom n2-e\), \(d'_j=n-1-d_j\), and \(c'=n-1-c\); substitution negates the numerator. For \(P_n\), insert \(e=c=n-1\) and \(d_1=d_n=1\). For \(S_{n,1}\), use \(e=n-1\), \(c=1\), \((d_1,d_n)=(n-1,1)\). For \(S_{n,2}\), use \(e=n-1\), \(c=2\), and \((d_1,d_n)=(1,1)\). The displayed strict inequalities follow whenever \(n\ge3\); for \(n=2\) the only graph-edge indicator is constant under permutation.

## Verification

The included standalone `verify.py` uses only the Python standard library. Run `python3 verify.py` to independently enumerate uniform permutations and compare exact rational covariances against the theorem. It exhausts **all labeled graphs** for \(2\le n\le5\), checks additional sampled graphs for \(n=6,7\), independently checks every admissible forced-two-image conditional expectation for \(2\le n\le6\), and checks path and both star identities for \(3\le n\le23\). The verified output is `VERIFY_OK graph_cases=1352 conditional_cases=280 family_cases=63`. Exact finite enumeration validates those cases; the proof above, not the tests, establishes the full infinite family.

## Relationship to prior work

Xu, Alain, and Sankoff (2008) study the **marginal law**, moments, and Poisson limits of common adjacencies in randomly ordered unsigned linear genomes. This corresponds to the specific adjacency graph \(P_n\), but their result does not state mixed covariance with the disjoint-cycle count of the same permutation, nor the graph-sensitive sign classification here. Deutsch, Kitaev, and Remmel (2009) obtain marginal equidistribution for \((X,Y)\)-adjacencies and place-value statistics in one-line permutations. Marginal equidistribution does not preserve joint covariance with \(K\). Diaconis, Evans, and Graham (2013) show equidistribution of oriented one-line successions and fixed-point sets; it likewise does not assert the joint law with \(K\). Mansour and Shattuck (2016) explicitly count **successions within permutation cycles**, jointly with the number of cycles. Their cycle-successions are directed functional arrows, not neighboring one-line values: even their joint dependence differs. The present claim is restricted to the exact arbitrary-graph mixed covariance, its sign characterization, and the star relabeling reversal. Known marginal laws, insertion formulas, and cycle decompositions are not claimed new.

## Limitations

The law concerns uniform permutations only. It determines a covariance and its sign, not independence or the full joint distribution, and it does not extend without further work to nonuniform permutation models. The graph labeling is essential: invariance under arbitrary relabeling is false. The conditional completion argument is elementary and portions could be implicit in earlier bivariate permutation enumerations. The inspected sources did not explicitly state the all-graph formula or relabeling sign reversal; exhaustive historical priority is not established.

## References

1. W. Xu, B. Alain, and D. Sankoff, *Poisson adjacency distributions in genome comparison: multichromosomal, circular, signed and unsigned cases*, Bioinformatics 24 (2008), i146–i152. DOI: `10.1093/bioinformatics/btn295`.
2. E. Deutsch, S. Kitaev, and J. Remmel, *Equidistribution of (X,Y)-descents, (X,Y)-adjacent pairs, and (X,Y)-place-value pairs on permutations*, arXiv:`0903.2555` (first public version 2009-03-14).
3. P. Diaconis, S. N. Evans, and R. Graham, *Unseparated pairs and fixed points in random permutations*, arXiv:`1308.5459` (first public version 2013-08-25).
4. T. Mansour and M. Shattuck, *Counting permutations by the number of successions within cycles*, Discrete Mathematics 339 (2016), 1368–1376. DOI: `10.1016/j.disc.2015.12.004`.
