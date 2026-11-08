# Exact polynomial-time leader placement on arbitrarily weighted tripod networks

## Finding

**Theorem.** Let \(T\) be any weighted tripod: three internally vertex-disjoint, nonempty paths with a common endpoint \(o\), arm lengths \(\ell_1,\ell_2,\ell_3\ge1\), and arbitrary strictly positive real edge conductances. Let \(N=1+\ell_1+\ell_2+\ell_3\), and \(L\) be the conductance Laplacian. For every integer \(1\le k\le N\), the exact optimum

\[
\mathcal R_k(T)=\min_{S\subseteq V(T),\ |S|=k}\operatorname{tr}\bigl((L_{V\setminus S,V\setminus S})^{-1}\bigr)
\]

(with value \(0\) when \(S=V\)) and a minimizing leader set can be computed with at most \(O(N^5)\) arithmetic operations and comparisons in the exact-real arithmetic model. In particular, the number of operations is polynomial in \(k\) and \(N\), rather than in the number of possible size-\(k\) subsets. For positive rational conductances, the algorithm is exact using rational arithmetic.

The minimizing sets for different cardinalities need not be nested. On the unweighted tripod with arm lengths \((1,1,4)\), number vertices by center \(0\), short arms \(1,2\), and long arm \(3,4,5,6\) outward. The unique optimal singleton is \(\{3\}\), with trace \(11\), whereas the unique optimal pair is \(\{0,5\}\), with trace \(13/3\). Thus greedy augmentation cannot always produce optimal leader placements, even on a unit-weight tripod.

## Assumptions and scope

The graph has exactly three arms and no additional edges. Edge conductances are strictly positive and finite; zeros or infinite conductances are excluded. Each leader is perfectly fixed (noise-free), and each follower is governed by the weighted undirected graph Laplacian. The objective is the unnormalized grounded inverse trace. For a conventional uniform-white-noise model the total steady-state variance is one half this trace, which does not change optimal leader sets. No convergence-rate, soft-leader, directed-graph, or general-tree assertion is made. A set of at least one leader is required for invertibility. The operation bound is an algebraic bound, not a bound on binary bit complexity for arbitrary rational inputs.

Write vertices on arm \(i\) as \(v_{i,1},\ldots,v_{i,\ell_i}\), with \(v_{i,0}=o\). If edge \((v_{i,j-1},v_{i,j})\) has conductance \(w_{i,j}>0\), put \(r_{i,j}=1/w_{i,j}\) and \(d_i(j)=\sum_{a=1}^j r_{i,a}\), with \(d_i(0)=0\). All resistance distances below refer to these sums.

## Proof

**1. Electrical identity.** For a nonempty leader set \(S\), wire all leaders to ground. Kirchhoff's equations give the follower potential vector under one unit of injected current at \(v\) as \((L_{FF})^{-1}e_v\), so its voltage at \(v\) is the effective resistance \(R_{\mathrm{eff}}(v,S)\). Therefore

\[
\operatorname{tr}((L_{FF})^{-1})=\sum_{v\notin S}R_{\mathrm{eff}}(v,S).
\]

Deleting all leaders partitions the remaining tree into components; the grounded Laplacian and the above sum split exactly by those components.

**2. Path costs and exact dynamic program.** On one arm, suppose two successive grounded vertices are at indices \(a<b\). For any intervening vertex \(j\), the two resistance paths to ground have lengths \(d_i(j)-d_i(a)\) and \(d_i(b)-d_i(j)\), so its effective resistance is their parallel combination. The cost of the open interval is exactly

\[
B_i(a,b)=\sum_{j=a+1}^{b-1}\frac{(d_i(j)-d_i(a))(d_i(b)-d_i(j))}{d_i(b)-d_i(a)}.
\]

After the last leader at \(a\), an ungrounded free tail costs

\[
Q_i(a)=\sum_{j=a+1}^{\ell_i}(d_i(j)-d_i(a)).
\]

For any fixed grounded index \(t\) and number \(s\) of additional leaders farther out, let \(F_i(t,s)\) be the minimum sum of such open-interval and final-tail costs. An acyclic path dynamic program starts at \(t\), adds a directed arc from index \(a\) to \(b>a\) of weight \(B_i(a,b)\) for each new leader, and ends with tail weight \(Q_i(a)\). Its shortest paths with exactly \(s\) arcs give \(F_i(t,s)\). Store parent pointers to recover actual leader positions. Computing all \(F_i(t,s)\) for all three arms, all \(t\), and all admissible \(s\) costs at most \(O(N^4)\) arithmetic operations after \(O(N^3)\) straightforward interval-cost preprocessing.

**3. Center chosen as leader.** If \(o\in S\), deleting \(o\) separates the arms and leaves their index-zero endpoints grounded. For nonnegative integers \(s_1+s_2+s_3=k-1\), the exact cost is

\[
F_1(0,s_1)+F_2(0,s_2)+F_3(0,s_3).
\]

Minimize over the three budgets. This includes the boundary \(k=N\), for which all followers disappear.

**4. Center remains a follower.** On each arm choose either the first leader index \(t_i\in\{1,\ldots,\ell_i\}\) or \(t_i=\infty\) when no leader is placed there. At least one \(t_i\) must be finite. A leader at \(t_i\) separates all farther vertices of that arm from the center component, so any farther choices affect only the independent path costs \(F_i(t_i,s_i)\). The center component depends *only* on the three first-leader indices, not on any farther leaders.

Put \(A=\{i:t_i<\infty\}\), \(R_i=d_i(t_i)\) for \(i\in A\), and \(G=\sum_{i\in A}1/R_i\). The center effective resistance is \(1/G\). On an arm \(i\notin A\), each vertex \(v_{i,j}\) has effective resistance \(d_i(j)+1/G\), because it connects to ground solely through the center. For \(i\in A\), define \(G_{-i}=G-1/R_i\). If \(G_{-i}=0\), a prefix vertex with \(1\le j<t_i\) has resistance \(R_i-d_i(j)\). Otherwise define \(H_i=1/G_{-i}\); its two paths to the grounded set, one directly to the first leader and one through the center and other grounded arms, have resistances \(R_i-d_i(j)\) and \(d_i(j)+H_i\). Their parallel combination is

\[
\frac{(R_i-d_i(j))(d_i(j)+H_i)}{R_i+H_i}.
\]

Sum these expressions and the center contribution \(1/G\) to obtain an explicit \(O(N)\)-evaluation \(C(t_1,t_2,t_3)\) of the entire center-component trace. It counts the center once and counts no leader vertex.

If \(a=|A|\) is the number of first leaders, the optimal value for this first-leader triple is

\[
C(t_1,t_2,t_3)+\min_{\substack{s_1+s_2+s_3=k-a\\s_i\ge0}}\sum_{i\in A}F_i(t_i,s_i),
\]

where an arm without leaders contributes zero to the distal cost and must have \(s_i=0\). Discard infeasible budgets. There are at most \(\prod_i(\ell_i+1)=O(N^3)\) first-leader triples; three-arm budget convolution costs at most \(O(k^2)\) operations per triple. Together with the center-cost evaluations and the path precomputation, the total is at most \(O(N^4+N^3k^2)=O(N^5)\). Every possible leader set belongs to exactly one of the two center cases and has exactly one first-leader triple in the follower-center case, so the minimization is exhaustive *by decomposition*, not by exponential subset search. Tracing all recorded argmins reconstructs an optimal leader set. This proves the theorem.

**5. Strictly non-nested optimal example.** For the unweighted arms \((1,1,4)\), exact evaluation of the seven singleton placements gives sorted two smallest trace values \(11\) at \(\{3\}\) and \(12\) at both \(\{0\}\) and \(\{4\}\). For the 21 pairs, the best trace is \(13/3\) uniquely at \(\{0,5\}\), and the second best is \(9/2\) at \(\{0,6\}\). Both strict inequalities follow by the same effective-resistance formulas (or by exact inversion of the at-most-six-dimensional grounded matrices). Hence the optimal singleton is absent from the optimal pair.

## Verification

Run `python3 verify_tripod.py` with Python's standard library. It evaluates the decomposition-based dynamic program and *separately* forms and inverts grounded Laplacian matrices in exact rational arithmetic. The self-contained verifier replayed 4,560 complete weighted-tripod/cardinality comparisons with all arm lengths from one to three, total arm length at most six, and conductances drawn from \(\{1,2\}\); 16 further weighted cases and one rational-weight instance were checked. It also verifies the distinct cardinality-optimal sets in the explicit seven-vertex example. The output is `VERIFICATION_OK 4577 total exact comparisons`.

The program is a finite regression and counterexample search, not a proof of the unrestricted theorem. The proof above establishes the infinite family using exact resistor-network identities and a complete case decomposition.

## Relationship to prior work

Patterson, McGlohon and Dyagilev (first public 2014-12-20) developed exact polynomial-time \(k\)-leader algorithms on positively weighted **paths and rings**, and the later journal version explicitly identifies tree topologies as a desired extension. The present graph has a genuine degree-three branch, and the center-follower case introduces a resistance coupling between distinct arms that does not decompose into three independent paths. Fitch and Leonard (first public 2014-07-07) gave general joint-centrality formulas for noisy-network leader sets, including noise-free leaders, but those formulas do not by themselves select an arbitrary-cardinality optimum on a branched weighted tree in polynomial time. This theorem is an exact optimization algorithm, not a re-expression of a given set's score.

Patterson, Yi and Zhang (2017) derive the same grounded-resistance objective identity and optimize two leaders on certain unweighted perfect rooted trees, but do not solve arbitrary leader budgets on arbitrarily weighted tripods. Research on leader-follower coherence in symmetric/asymmetric trees (Sun, Li and Zheng, 2021) considers prescribed leader assignments on particular structured trees. Its accessible abstract does not assert an arbitrary-weight, arbitrary-cardinality polynomial optimizer; the complete paper was not available for a definitive theorem-by-theorem comparison.

## Limitations

The number of arms is fixed at three. Enumerating first leaders on an unrestricted number of arms would not give the stated polynomial bound. The result concerns the grounded inverse-trace coherence objective only, not spectral-gap maximization. It is an exact-real arithmetic-operation bound rather than a bit-complexity bound, and the verifier tests finitely many positive rational conductances. Existing or unindexed structural algorithms for larger tree families may yield overlapping special cases; independent mathematical and publication-priority review remains outstanding.

## References

1. K. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, initial arXiv publication 2014-07-07, https://arxiv.org/abs/1407.1569 .
2. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, initial arXiv publication 2014-12-20, https://arxiv.org/abs/1412.6595 .
3. S. Patterson, N. McGlohon and K. Dyagilev, *Optimal \(k\)-Leader Selection for Coherence and Convergence Rate in One-Dimensional Networks*, IEEE Transactions on Control of Network Systems, doi:10.1109/TCNS.2016.2520201; see https://arxiv.org/abs/1604.07094 .
4. S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873v1, https://arxiv.org/abs/1708.06873 .
5. W. Sun, L. Li and S. Zheng, *Leader selection for coherence in symmetric and asymmetric trees*, Journal of Statistical Mechanics 2021, 073401, doi:10.1088/1742-5468/ac0f66 (full-text comparison unresolved).
