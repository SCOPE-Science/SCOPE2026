# Sharp threshold-risk containment on blocked cycle contact networks

## Finding

Fix integers \(n\ge3\), \(2\le k<n\) and \(2\le h\le n\). Independently retain each undeleted contact edge of a cycle \(C_n\) with probability \(p\in(0,1)\), delete exactly \(k\) edges in advance, and choose a single uniform epidemic seed independently of edge retention. Let \(S\) be the number of vertices in the seed's open connected component and set \(R_h=\Pr(S\ge h)\). Deletion divides the ring into \(k\) path components with lengths \(\ell_1,\ldots,\ell_k\ge1\), totaling \(n\).

Define the unnormalized path threshold contribution
\[
F_h(\ell)=\begin{cases}0,&\ell<h,\\ p^{h-1}[h+(\ell-h)(h-(h-1)p)],&\ell\ge h.\end{cases}
\]
Then
\[
R_h=\frac1n\sum_{i=1}^k F_h(\ell_i).
\]
The exact global minimum and all equality cases are as follows, for every \(0<p<1\):

* If \(n\le k(h-1)\), the minimum is zero and **all and only** length multisets with \(\max_i\ell_i\le h-1\) attain it.
* If \(n>k(h-1)\), the **unique** minimizing length multiset is
\[
\{n-(k-1)(h-1),\underbrace{h-1,\ldots,h-1}_{k-1}\}.
\]
Its risk is \(n^{-1}F_h(n-(k-1)(h-1))\). Uniqueness here is for the multiset; rotations and reflections and permutations of the physical gaps may represent distinct labeled edge deletions.

A different, sharp phenomenon occurs for the **maximum** risk. The smallest ring allowing a transmissibility-dependent maximizing gap pattern has six vertices. For \(n=6\), \(k=2\), \(h=3\), the three length multisets and their risks are
\[
\begin{array}{c|c}
\{5,1\}&p^2(9-4p)/6\\
\{4,2\}&p^2(6-2p)/6\\
\{3,3\}&p^2
\end{array}
\]
The unique minimizing multiset is \(\{4,2\}\) for all \(p\in(0,1)\); the maximizing multiset is \(\{5,1\}\) for \(p<3/4\), both \(\{5,1\}\) and \(\{3,3\}\) at \(p=3/4\), and \(\{3,3\}\) for \(p>3/4\). By contrast, \(\{3,3\}\) **uniquely minimizes expected outbreak size** for every \(p\in(0,1)\). Thus for \(p>3/4\), the intervention best for expected outbreak size is worst for probability of an outbreak reaching three people.

## Assumptions and scope

The network is one simple ring with \(n\) vertices; exactly \(k\ge2\) distinct edges are removed deterministically before the seed is chosen. Each remaining edge is open independently with common probability \(p\). The epidemic infects exactly the open cluster of the uniformly chosen seed. The result does not assert equivalence with a general Markovian SIR process with correlated transmissions arising from shared random infectious periods. Only length-multiset equivalence, not uniqueness of individual labeled deletion sets, is claimed. All stated strict comparisons require \(0<p<1\).

## Proof

**Path contribution.** Consider one \(\ell\)-vertex path. Let \(W_h\) count consecutive windows of \(h\) vertices all connected by open bonds, and let \(N_h\) count maximal open clusters containing at least \(h\) vertices. For \(\ell\ge h\), each of the \(\ell-h+1\) eligible windows is open with probability \(p^{h-1}\), hence
\[
\mathbb E W_h=(\ell-h+1)p^{h-1}.
\]
One qualifying maximal cluster may start at the path's first vertex, with probability \(p^{h-1}\), or at any of its next \(\ell-h\) candidate vertices, whose preceding bond must be closed, with probability \((1-p)p^{h-1}\). Consequently
\[
\mathbb E N_h=p^{h-1}[1+(\ell-h)(1-p)].
\]
For a maximal cluster of length \(r\ge h\), the identity \(r=(r-h+1)+(h-1)\) expresses its vertex count as the number of qualifying windows plus \(h-1\). Summing over qualifying clusters and averaging yields
\[
\mathbb E[\text{vertices in open clusters of size at least }h]
=\mathbb EW_h+(h-1)\mathbb EN_h
=p^{h-1}[h+(\ell-h)(h-(h-1)p)].
\]
For \(\ell<h\), this expectation is zero. The uniform seed weights every vertex equally, so summing these expectations over the predetermined paths and dividing by \(n\) proves the displayed risk formula.

**All threshold-risk minimizers.** On \(\ell\ge h\), write \(F_h(\ell)=a\ell-b\), where
\[
a=p^{h-1}[h-(h-1)p]>0,\qquad b=h(h-1)(1-p)p^{h-1}.
\]
If two path lengths \(u,v\ge h\) occur, replace them by lengths \(u+v-(h-1)\) and \(h-1\); the first is still at least \(h\), total length and component count are unchanged, and the sum of contributions strictly decreases by
\[
F_h(u)+F_h(v)-F_h(u+v-(h-1))=(h-1)p^h>0.
\]
Therefore every positive-risk minimizer has exactly one path of length at least \(h\). If this sole long path coexists with a short path of length \(j<h-1\), move one vertex from the long path to the short path. Provided \(n>k(h-1)\), the long path has length at least \(h+1\) when some short path is below \(h-1\); hence the move is possible and decreases risk strictly by \(a>0\). Thus every short path has length \(h-1\), fixing the sole long length and proving uniqueness. If \(n\le k(h-1)\), distributing the \(n\) vertices among \(k\) paths of lengths between \(1\) and \(h-1\) is feasible, giving zero risk. Since \(p>0\), \(F_h(\ell)>0\) precisely when \(\ell\ge h\), giving all and only equality cases.

**Six-site phase change.** Substitution of \(h=3\) and the three partitions of six into two positive lengths, modulo ordering, gives the displayed formulas. Their unnormalized differences are
\[
F_3(5)+F_3(1)-F_3(3)-F_3(3)=p^2(3-4p),
\]
\[
F_3(3)+F_3(3)-F_3(4)-F_3(2)=2p^3>0,
\]
\[
F_3(5)+F_3(1)-F_3(4)-F_3(2)=p^2(3-2p)>0.
\]
They establish all strict orders and the unique positive interior crossover \(p=3/4\).

**Sharpness of six sites.** If \(h\ge3\) and \(n\le5\), at most one path can contain \(h\) vertices, since two would require at least six vertices. The nonzero single-path contribution increases strictly with its length, so maximizing configurations can be chosen independently of \(p\), and any ties remain tied for all \(p\). For \(h=2\), if \(t\) of the \(k\) paths have length at least two, the complete unnormalized threshold contribution simplifies to
\[
\sum_i F_2(\ell_i)=p\big[(2-p)(n-k)+pt\big].
\]
Hence the maximizing configurations are exactly those with maximum feasible \(t\), independently of \(p\), for every \(n\). Thus no smaller ring admits a change of maximizing length multiset with transmissibility.

**Mean-risk distinction.** For a path with \(\ell\) vertices, summing connectivity probabilities over all ordered vertex pairs shows that its total mean-size contribution is
\[
M(\ell)=\ell+2\sum_{d=1}^{\ell-1}(\ell-d)p^d.
\]
Thus \(\mathbb E S=n^{-1}\sum_i M(\ell_i)\). Its first discrete difference is \(M(\ell+1)-M(\ell)=1+2\sum_{d=1}^{\ell}p^d\), which increases strictly with \(\ell\) when \(p>0\), since the second difference is \(2p^{\ell+1}>0\). By moving one vertex from a longer path to a shorter path whenever their lengths differ by at least two, one strictly decreases the mean; therefore all mean minimizers have lengths differing by at most one. For six vertices and two paths, this gives only \(\{3,3\}\), yielding the claimed separation.

## Verification

Run `python verify.py` with Python 3.9 or newer; it uses only the Python standard library and exact `fractions.Fraction` arithmetic. It checks the analytic tail formula and mean formula against an independently coded exhaustive open-edge-state enumeration, evaluates the claimed minimizers for all positive-length compositions for \(3\le n\le11\) at three rational transmissibilities and every feasible \(h\), checks the mean extremizers, and verifies the six-site crossover algebra at rational test points. The script reports 990 partition-parameter checks and 2964 independently enumerated threshold probabilities. These are finite cross-checks, not substitutes for the displayed all-size mathematical proof.

## Relationship to prior work

Moore and Newman (2000) analyze exact bond-percolation cluster distributions on small-world networks, including their one-dimensional local-cluster component, but do not classify optimal deterministic multi-edge cuts of finite rings for a uniform-seed threshold objective. Enright and Meeks (2015 preprint) study edge deletion to control the largest possible component under a deterministic worst-case criterion, rather than a probability-weighted random-seed outbreak tail; the zero-risk part of the theorem is compatible with that familiar deterministic idea and is not, by itself, a novelty claim. Enns and Brandeau (2015) compare epidemic link-removal policies using simulation and expected total infections in stochastic SIR systems; their investigated networks and objective do not give the present exact threshold extremizers. Kenah and Robins (2006) explain why undirected independent bond percolation must not be equated with every stochastic SIR specification. Ball, Britton, Leung and Sirl (2018) consider adaptive edge-dropping in large configuration-model SIR epidemics, also a different setting. The contribution claimed here is the complete finite-ring fixed-cut, uniform-seed **risk-minimum classification together with the sharp six-site probability-dependent worst-policy reversal**.

## Limitations

This is an idealized independent-edge transmission model, not a calibrated epidemic forecast or an optimality theorem for generic SIR models, adaptive policies, nonuniform seeding, variable edge probabilities, uncertain contact topology, or other graph classes. Historical-priority certainty is limited by potentially unindexed graph-percolation optimization literature. The minimum rule for zero risk is elementary; the novel-claim focus is the universal positive-risk optimality and sharp objective reversal. The all-size proof is analytic; finite enumeration provides checks rather than independent certification. No independent external scientific audit has been performed.

## References

1. C. Moore and M. E. J. Newman, *Exact solution of site and bond percolation on small-world networks*, first public preprint 2000-01-26, https://arxiv.org/abs/cond-mat/0001393.
2. J. Enright and K. Meeks, *Deleting edges to restrict the size of an epidemic: a new application for treewidth*, preprint 2015-04-22, https://arxiv.org/abs/1504.05773.
3. E. A. Enns and M. L. Brandeau, *Link removal for the control of stochastically evolving epidemics over networks: A comparison of approaches*, *J. Theor. Biol.* 371 (2015), 154–165, https://pmc.ncbi.nlm.nih.gov/articles/PMC4372451/.
4. E. Kenah and J. M. Robins, *Second look at the spread of epidemics on networks*, preprint 2006-10-30, https://arxiv.org/abs/q-bio/0610057.
5. F. Ball, T. Britton, K. Y. Leung and D. Sirl, *A stochastic SIR network epidemic model with preventive dropping of edges*, preprint 2018-08-24, https://arxiv.org/abs/1808.08100.
