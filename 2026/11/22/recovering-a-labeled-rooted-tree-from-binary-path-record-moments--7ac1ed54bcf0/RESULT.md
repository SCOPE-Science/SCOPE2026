# Recovering a labeled rooted tree from binary path-record moments

## Finding
Let \(T\) be an unknown finite rooted tree whose \(n\ge 2\) vertices have distinct, persistent observed identities. Independently assign continuous iid marks to all vertices; observe only the binary vector whose entry at \(v\) reports whether its mark is a strict minimum along the root-to-\(v\) path. The full rooted, vertex-labeled tree is uniquely identified by the vector's first and pairwise second moments. In particular, if \(p_v\) is the marginal record probability and \(c_{uv}\) is the covariance, then

\[
p_v=\frac1{d_v+1},\qquad
c_{uv}=\begin{cases}
0,&u,v\text{ ancestor-comparable},\\
\displaystyle\frac{k}{(k+a)(k+b)(k+a+b)},&u,v\text{ incomparable},
\end{cases}
\]

where \(d_v\) is depth (root depth zero); for incomparable vertices, \(k\) is the number of vertices on their shared root-to-lowest-common-ancestor path, and \(a,b\ge1\) are the numbers of vertices on the respective paths beyond that ancestor. Thus the unique parent of any nonroot \(v\) is the unique vertex at depth \(d_v-1\) with zero covariance with its record indicator.

For \(N\) independent repetitions of the entire observation vector, a concrete empirical-moment reconstruction rule succeeds with probability at least \(1-\delta\) whenever

\[
N\ge 288n^6\log\!\left(\frac{2n^2}{\delta}\right),\qquad 0<\delta<1.
\]

The finite-sample bound is a sufficient bound, not a claim of optimal sample complexity.

## Assumptions and scope
The tree is fixed but unknown, with every vertex individually labeled and observed in each repetition. It is connected, finite and rooted, and its root identity need not be supplied. Each repetition uses fresh independent iid real marks with a common atomless distribution, allowing no ties almost surely. The data in each repetition comprise one bit per vertex, not the marks or any edges. No branching-degree restriction or random-tree prior is imposed. All results hold for every such tree with \(n\ge2\).

## Proof
**One-point probabilities.** Let \(P_v\) be the set of the \(d_v+1\) vertices on the root-to-\(v\) path. Iid continuity and exchangeability make each vertex of \(P_v\) equally likely to have its smallest mark. Hence \(p_v=1/(d_v+1)\), identifying each depth exactly and the unique root at depth zero.

**Ancestor-comparable pairs.** When one vertex lies on the root path of the other, restrict the iid marks to that single path. Relative insertion ranks in a uniformly random permutation are independent, and the events that the latest mark is a new minimum are independent Bernoulli events with reciprocal-index means. Thus the two record indicators have covariance zero, even for the root (whose indicator is constant one).

**Incomparable pairs.** Write the shared prefix of \(P_u,P_v\) as \(k\ge1\) vertices, with disjoint exclusive tails of lengths \(a,b\ge1\). Apply the common continuous CDF to normalize marks to independent uniforms. Conditional on the two terminal marks having survival values \(t,s\in[0,1]\), both records occur precisely when every common-prefix mark is greater than both terminal marks, and all other exclusive-path marks exceed their own terminal marks. The conditional probability is \(\min(t,s)^k t^{a-1}s^{b-1}\). Splitting the unit square along \(t=s\) and integrating gives

\[
\Pr(I_u=I_v=1)
=\frac{1/(k+a)+1/(k+b)}{k+a+b}.
\]

Subtracting \(\Pr(I_u=1)\Pr(I_v=1)=1/((k+a)(k+b))\) yields the stated strictly positive covariance. The implication therefore holds both ways: zero covariance is equivalent to ancestor comparability for distinct vertices.

**Population reconstruction.** Recover each depth from its marginal. For each nonroot \(v\), there is exactly one ancestor with depth \(d_v-1\), namely its parent. All other vertices at that depth are incomparable with \(v\), so their covariances with \(I_v\) are positive. The parent is uniquely determined, proving injectivity of the full moment map on rooted labeled trees.

**Explicit finite-sample recovery.** For each vertex compute the empirical mean \(\widehat p_v\), and for each pair the empirical product mean \(\widehat q_{uv}\), using the \(N\) independent observed vectors. Estimate depth by choosing the nearest point to \(\widehat p_v\) in \(\{1,1/2,\ldots,1/n\}\), and set \(\widehat c_{uv}=\widehat q_{uv}-\widehat p_u\widehat p_v\). Choose as parent of each nonroot \(v\) the unique vertex at the preceding recovered depth with \(\widehat c_{uv}<1/(4n^3)\).

Put \(\eta=1/(24n^3)\). There are fewer than \(n^2\) marginal and product means, each an average of independent Bernoulli random variables across repetitions. By Hoeffding's inequality and a union bound, all their errors have absolute value at most \(\eta\), except on an event of probability at most

\[
2n^2\exp\!\left(-\frac{N}{288n^6}\right).
\]

On the good event, successive distinct depth probabilities differ by at least \(1/[n(n-1)]>2\eta\), so all depths are recovered. Since all empirical means are between zero and one, every empirical covariance differs from its population value by at most \(3\eta=1/(8n^3)\). For incomparable pairs, \(k\ge1\), \(k+a\le n\), \(k+b\le n\) and \(k+a+b\le 2n-1\), hence

\[
c_{uv}\ge\frac{1}{n^2(2n-1)}>\frac{1}{2n^3}.
\]

Consequently a true parent has estimated covariance at most \(1/(8n^3)\), while every competing vertex on the immediately preceding level has estimated covariance greater than \(3/(8n^3)\). The proposed threshold separates them strictly. The stated condition on \(N\) makes the failure bound at most \(\delta\), completing the proof.

## Verification
Run `python3 verify.py` using Python's standard library. It independently enumerates every rooted labeled tree with designated root zero on two through five vertices via Prüfer sequences, and for each tree enumerates every ordering of the iid marks. It checks the complete first and second moments against the analytical rational formulas, the signs of all pairwise covariances, and exact reconstruction. It additionally tests 24 deterministically seeded trees on six vertices by exhaustive mark ordering, and 1,060 seeded trees on sizes 2 through 54 with exact symbolic moments. These are finite cross-checks of the algebra; the all-size assertions are proved above. The verifier prints the actual number of checks, not an independent mathematical certification.

## Relationship to prior work
The random tree record/cutting process is classical. In particular, Janson's *Random cutting and records in deterministic and random trees* (preprint dated 27 January 2004, revised 17 May 2005) studies record counts under iid marks. Its introduction explicitly gives independent record indicators on a path and a positive two-sibling dependence example. Those antecedents are credited; neither is presented here as new. The claim assessed here is the **inverse labeled-tree identifiability and quantitative recovery guarantee from a sequence of complete binary record vectors**. Burghart's later work on complete rooted-tree polynomial invariants addresses the distinguishability of unlabeled isomorphism classes using different generating invariants, and does not supply this labeled binary observation rule or a finite-replication error guarantee. These statements do not establish exclusive historical priority; see the risks below.

## Limitations
The theorem requires each vertex to retain a consistent observed identity between experiments and the complete vector of binary record indicators to be measured. It does not reconstruct a tree from the distribution of the total number of records, from unlabeled observations, or from a single draw. Its \(O(n^6\log(n/\delta))\) replication guarantee is intentionally conservative and not minimax-sharp. Other unknown or dependent mark mechanisms are not covered. An exact equivalent inverse theorem in earlier record-process or statistical topology literature has not been ruled out by a comprehensive historical audit.

## References
1. S. Janson, “Random cutting and records in deterministic and random trees,” preprint dated 27 January 2004; *Random Structures & Algorithms* 29 (2006), 139–179, doi:10.1002/rsa.20086. Public preprint first-page transcription: https://doc.xuehai.net/b351d49e3d302aafdd909620d.html.
2. F. Burghart, “Polynomial invariants for rooted trees related to their random destruction,” arXiv:2302.08394, first posted 16 February 2023, https://arxiv.org/abs/2302.08394.
3. C. Holmgren, “Random Records and Cuttings in Binary Search Trees,” *Combinatorics, Probability and Computing* 19 (2010), 391–424, doi:10.1017/S096354830999068X.
