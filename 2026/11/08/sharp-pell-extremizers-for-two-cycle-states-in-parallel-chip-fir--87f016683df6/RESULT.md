# Sharp Pell extremizers for two-cycle states in parallel chip-firing on trees

## Finding
For every finite labelled simple tree \(T\) with \(n\ge2\) vertices, the number \(N_2(T)\) of *states already on a primitive two-cycle* of parallel chip-firing satisfies
\[
2(n-1)\le N_2(T)\le2p_{n-1},
\]
where \(p_0=0\), \(p_1=1\), and \(p_{k+1}=2p_k+p_{k-1}\) for \(k\ge1\). At every order \(n\ge4\), the lower bound is attained only by the star and the upper bound only by the path. For \(n=2,3\), the unique tree is both a path and a star, so the bounds coincide. Each two-cycle has two distinct states; the sharp orbit-count bounds are therefore \(n-1\) and \(p_{n-1}\).

For example, the two-cycle *state* counts for path orders \(2,3,4,5,6,7,8\) are \(2,4,10,24,58,140,338\), whereas the star counts are \(2,4,6,8,10,12,14\). The ratio of the extreme orbit counts grows exponentially in the number of vertices, since \(p_{n-1}\sim(1+\sqrt2)^{n-1}/(2\sqrt2)\).

## Assumptions and scope
The graph is finite, undirected, simple, connected, and has at least one edge. A state is a vector \(\sigma\in\mathbb Z_{\ge0}^{V(G)}\) of *indistinguishable* chip counts, with no imposed bound on its total. In one parallel step \(U\), each vertex \(v\) having at least \(d_v=\deg(v)\) chips fires once, distributing one chip along every incident edge. All decisions are made from the old state, before any receipts.

We count only states satisfying \(U^2\sigma=\sigma\ne U\sigma\). This is a finite set even though the full state space and the set of fixed states can be infinite. We do not count trajectories that first enter a two-cycle after a positive transient.

For a vertex subset \(S\), write \(k_v(S)=|\{w\sim v:\mathbf1_{w\in S}\ne\mathbf1_{v\in S}\}|\), the number of neighbors across the cut. The preliminary identity valid on every connected simple graph is
\[
N_2(G)=\sum_{S\subseteq V(G)}\prod_{v\in V(G)}k_v(S).
\]
Terms with some zero factor contribute zero. The theorem concerns the sharp extrema of this dynamic-state count over all trees of a given order, not a general bound for non-trees.

## Proof
**1. Two-step firing constraint.** Put \(f_t(v)=\mathbf1_{\sigma_t(v)\ge d_v}\). Summing two steps gives \(\sigma_2-\sigma_0=-L_Gh\), where \(L_G\) is the ordinary graph Laplacian and \(h(v)=f_0(v)+f_1(v)\in\{0,1,2\}\). If \(U^2\sigma=\sigma\), the connectedness of \(G\) forces \(h\) to be constant. Values zero and two imply no vertex or every vertex fires on both steps, hence \(U\sigma=\sigma\); for a primitive two-cycle necessarily \(h(v)=1\) at each vertex. Conversely, if every vertex fires once in two steps, then the Laplacian identity gives \(U^2\sigma=\sigma\).

Let \(S\) be the vertices firing at the first step. For \(v\in S\), its count after the first step is \(\sigma(v)-k_v(S)\); it must cease firing, giving exactly \(k_v(S)\) choices
\[
d_v\le\sigma(v)\le d_v+k_v(S)-1.
\]
For \(v\notin S\), its count after the first step is \(\sigma(v)+k_v(S)\); it must begin firing, giving exactly \(k_v(S)\) choices
\[
d_v-k_v(S)\le\sigma(v)\le d_v-1.
\]
These intervals are nonnegative and fully specify the two-step firing patterns. All such assignments satisfy \(U^2\sigma=\sigma\), and the first-step firing set is unique. Thus the cut identity above counts every primitive two-cycle state once. In particular, every such state's chip count at each vertex lies between zero and \(2d_v-1\).

**2. Tree-edge and functional-map interpretations.** On a tree, the indicator \(e_a\in\{0,1\}\) that an edge \(a\) crosses the cut can be prescribed independently, and every edge-indicator assignment comes from exactly two vertex bicolorings. Hence
\[
N_2(T)=2\sum_{e\in\{0,1\}^{E(T)}}\prod_{v\in V(T)}\Big(\sum_{a\ni v}e_a\Big).\tag{1}
\]
For each positive product choose, independently at every vertex, one incident edge labelled one. This is a function \(f:V(T)\to V(T)\) with \(f(v)\sim v\). The selected functional digraph has one directed two-cycle in every weak component: a longer directed cycle would induce an undirected cycle in the tree. If it has \(c(f)\) components, exactly \(n-c(f)\) undirected edges are selected at least once (one doubled edge per component). The other \(c(f)-1\) edges are free to carry either indicator. Reversing the order of summation in (1) gives
\[
N_2(T)=\sum_{f: f(v)\sim v}2^{c(f)}.\tag{2}
\]
For each of the \(n-1\) edges, orient every other vertex toward that edge and make its endpoints point to each other. This is the unique neighbor map whose sole directed two-cycle uses that edge. These maps give exactly \(2(n-1)\) contributions to (2). If \(T\) is not a star, it has two vertex-disjoint edges. Delete an edge between them and orient each resulting component toward its chosen edge, producing a neighbor map with at least two directed two-cycles and a strictly positive additional contribution. Conversely, a star cannot contain two disjoint edges, and every neighbor map has only one two-cycle. This proves the sharp lower bound and its equality cases.

**3. Rooted-tree recursion for the upper bound.** Root a tree at \(v\), regard the edge to its (possibly fictitious) parent as bearing an externally prescribed crossing bit \(t\in\{0,1\}\), and sum the product of the vertex factors in the rooted subtree. Let \(A(T,v)\) be the sum for \(t=0\), and \(B(T,v)\) the sum for \(t=1\). A leaf has pair \((A,B)=(0,1)\). If the children have pairs \((a_i,b_i)\), define \(s_i=a_i+b_i\); independence of child-edge bits gives
\[
A=\sum_i b_i\prod_{j\ne i}s_j,\qquad
B=A+\prod_i s_i.\tag{3}
\]
The formulas are monotone in every nonnegative child parameter; the empty-product convention handles leaves.

For a path of \(m\) vertices rooted at an endpoint, (3) reduces to \((a_{m+1},b_{m+1})=(b_m,a_m+2b_m)\). It follows by induction that
\[
(a_m,b_m)=(p_{m-1},p_m),\qquad s_m=p_{m-1}+p_m.\tag{4}
\]
The Pell addition identities, valid for all positive integers \(m,k\), are
\[
p_m s_k+p_k s_m=p_{m+k},\qquad
s_{m+k}=s_m s_k+2p_mp_k.\tag{5}
\]
They follow directly from the recurrence in (4), for example by induction in \(k\) with both sides matching at the first two indices.

Inductively replace each rooted child subtree of size \(m\) by an endpoint-rooted path of size \(m\). The two coordinates in (3) cannot decrease. If the root now has at least two path children of sizes \(m,k\), merge them into one path child of size \(m+k\). By (5), their contribution \(p_m s_k+p_k s_m\) to the first sum in (3) stays *exactly* the same, while their product factor strictly increases by \(2p_mp_k>0\). All other child contributions are nonnegative. Thus the new root pair has no smaller first coordinate and a strictly larger second coordinate. Repeat until the root has a single path child. This proves
\[
A(T,v)\le p_{|T|-1},\qquad B(T,v)\le p_{|T|},\tag{6}
\]
and equality in the second coordinate occurs only when the rooted tree is a path rooted at an endpoint. For a leaf root, the second coordinate is exactly the first coordinate of the whole tree after adjoining the leaf edge with bit one; every tree has a leaf \(u\) with neighbor \(v\), and (3) yields \(N_2(T)=2B(T-u,v)\). Applying (6) to the \(n-1\)-vertex rooted subtree gives \(N_2(T)\le2p_{n-1}\). Equality forces \(T-u\) to be a path with \(v\) an endpoint, hence \(T\) itself is a path. Conversely, for a path equality follows from (4). The upper bound and its equality cases are proved.

## Verification
Two independently written, standard-library-only Python programs are included at `checks/verify_direct.py` and `checks/verify_tree_dp.py`. The first directly enumerates chip vectors in the mathematically justified finite box \(0\le\sigma(v)<2d_v\) and tests \(U^2\sigma=\sigma\ne U\sigma\), then compares with independently enumerated cuts. It tests every nonisomorphic tree of order \(2\) through \(7\), paths and stars through order \(10\), and three additional connected non-trees. The second calculates the exact recursive tree invariant for every nonisomorphic tree of order \(2\) through \(8\), tests 2,200 additional deterministic pseudo-random labelled trees of orders \(9\) through \(30\), and checks both Pell addition identities over 9,801 ordered pairs. Captured outputs are supplied separately. These finite checks corroborate but do not substitute for the all-order proof.

Run `python3 checks/verify_direct.py` and `python3 checks/verify_tree_dp.py` in a standard Python 3 environment. The file outputs were reproduced before packaging and match `checks/direct_output.txt` and `checks/dp_output.txt` byte-for-byte.

## Relationship to prior work
Bitar and Goles established that parallel chip-firing on trees has eventual period at most two. Jiang's Proposition 2.5 (arXiv:1003.0943, Section 2) characterizes periodicity through equal vertex firing totals, and Lemma 2.1 confines nontrivial periodic chip heights. Jiang, Scully and Zhang (arXiv:1211.6786, Sections 6–7) characterize allowed periodic firing patterns and discuss tree-like subgraphs. These are genuine underlying results, not claimed here as new. In particular, the first step of the proof is compatible with, and can be recovered from, Jiang's general periodicity proposition.

The present result concerns a different invariant: the *number of chip configurations already lying on primitive two-cycles* as the underlying tree varies, and its sharp extremizers, with Pell growth for the path. No count or sharp tree-extremal theorem of this form was located in the inspected primary texts or the documented search. The 2020 path enumeration by Mullen, Nowakowski and Cox concerns the distinct parallel-diffusion rule, not parallel chip-firing.

## Limitations
The complete original 1992 Bitar–Goles article could not be inspected; comparison with it is restricted to its published abstract and subsequent primary papers citing it. Institutional full-text access was unavailable, and an earlier unindexed equivalent remains possible. The theorem is an exact mathematical proof for finite *trees*, not an assertion about general-graph extrema, the number of fixed configurations, or the sizes of transient basins. The supplied exhaustive tests end at finite sizes; no independent external audit has been conducted.

## References
1. J. Bitar and E. Goles, *Parallel chip firing games on graphs*, Theoretical Computer Science **92** (1992), 291–300. DOI: 10.1016/0304-3975(92)90316-8.
2. T.-Y. Jiang, *On the period lengths of the parallel chip-firing game*, first posted 2010-03-04, arXiv:1003.0943. Especially Proposition 2.5.
3. T.-Y. Jiang, Z. Scully, and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, first posted 2012-11-29, arXiv:1211.6786; SIAM Journal on Discrete Mathematics **29** (2015), 615–630.
4. T. Mullen, R. Nowakowski, and D. Cox, *Counting Path Configurations in Parallel Diffusion*, first posted 2020-10-09, arXiv:2010.04750 (different dynamical rule).
