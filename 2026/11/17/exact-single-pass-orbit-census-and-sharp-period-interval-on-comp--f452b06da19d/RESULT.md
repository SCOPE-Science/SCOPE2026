# Exact single-pass orbit census and sharp period interval on complete multipartite chip-firing graphs

## Finding
Let \(r\ge3\), let \(n_1,\ldots,n_r\) be arbitrary positive integers, and let \(G=K_{n_1,\ldots,n_r}\) be the labelled complete multipartite graph. Put \(N=\sum_{i=1}^r n_i\), \(M=\max_i n_i\), and \(E=|E(G)|=\sum_{i<j}n_in_j\). In synchronous parallel chip firing, a vertex holding at least its degree in nonnegative integer chips sends one chip to each neighbor at every update. Restrict attention to configurations with exactly \(E\) chips which **are already periodic** and for which **every vertex fires exactly once in its least temporal period** (the critical-mass single-pass sector).

For a positive integer \(T\), let \(C_G(T)\) count the labelled configurations of this kind having least temporal period \(T\). Let \(\left\{\begin{smallmatrix}n\\k\end{smallmatrix}\right\}\) be the Stirling number of the second kind, with the usual zero convention outside \(1\le k\le n\). Define \(A_T(k_1,\ldots,k_r)\) as the number of cyclic words \((s_0,\ldots,s_{T-1})\in\{1,\ldots,r\}^T\) with exactly \(k_i\) copies of letter \(i\) and \(s_t\ne s_{t-1}\) for every \(t\) modulo \(T\). Then

\[
C_G(T)=\sum_{\substack{k_1+\cdots+k_r=T\\1\le k_i\le n_i}}
 A_T(k_1,\ldots,k_r)\prod_{i=1}^r k_i!\left\{\begin{matrix}n_i\\k_i\end{matrix}\right\}.
\]

Equivalently, if \(B(\mathbf z)\) is the \(r\)-by-\(r\) matrix \(B_{ij}=z_j\) for \(i\ne j\) and \(B_{ii}=0\), then \(A_T(\mathbf k)=[z_1^{k_1}\cdots z_r^{k_r}]\operatorname{tr}(B(\mathbf z)^T)\). The number of distinct time-translation orbits is \(C_G(T)/T\).

**Sharp period interval:**
\[
C_G(T)>0\quad\Longleftrightarrow\quad r\le T\le \min\{N,\,2(N-M)\}.
\]
There are no gaps in this interval, including odd periods. In particular, for \(G=K_{2,2,1}\), the respective counts at periods \(3,4,5\) are \(6,16,40\), giving \(2,4,8\) distinct orbits. The period-five sector consists of **40 labelled configurations**, not merely a single example.

## Assumptions and scope
The graph is finite, simple, undirected, loopless, connected and complete \(r\)-partite with \(r\ge3\) nonempty labelled parts. All vertices and chips are otherwise indistinguishable only in the sense that vertices are labelled while chips are not. The state contains nonnegative integers summing to \(E\). Updates are simultaneous, with firing determined from the start-of-round chip counts. The objects counted are configurations already on a cycle; transient states, fixed states and periodic states with a vertex firing more than once in its least period are **excluded**. Each orbit is counted once per initial time origin in \(C_G(T)\), and once in \(C_G(T)/T\).

## Proof
**1. A critical-mass phase lemma.** Let \(H=(V,E_H)\) be any finite connected simple graph with at least one edge. Suppose a periodic parallel chip-firing configuration has \(|E_H|\) chips, least period \(T\), and each vertex fires once in these \(T\) rounds. Let \(\tau(v)\in\{0,\ldots,T-1\}\) be the unique firing round for \(v\), and let \(d(v)\) be its degree. At the start of the firing round \(\tau(v)\), vertex \(v\) holds its initial chips \(x(v)\) plus one chip for each neighbor fired at an earlier round; hence
\[
x(v)\ge d(v)-\#\{w\sim v:\tau(w)<\tau(v)\}.\]
Summing over vertices, an edge whose endpoints have different phases is counted exactly once among earlier neighbors, whereas an edge with equal endpoints' phases is counted zero times. Therefore
\[
|E_H|=\sum_v x(v)\ge |E_H|+\#\{vw\in E_H:\tau(v)=\tau(w)\}.
\]
Thus adjacent vertices never fire in the same round, and equality forces the **unique** initial chip allocation
\[
x(v)=d(v)-\#\{w\sim v:\tau(w)<\tau(v)\}.\tag{1}\]
For every vertex whose phase is positive, the preceding round must contain a neighbor: otherwise that vertex already has at least \(d(v)\) chips one round before its specified firing. For a vertex whose phase is zero, the same condition with the last round is necessary because otherwise it regains its full \(d(v)\) chips before its scheduled return at the start of the next period. Every round is nonempty (an empty firing round would freeze the game forever).

Conversely, take any surjective map \(\tau:V\to\mathbb Z/T\mathbb Z\) such that (i) adjacent vertices have different phases and (ii) every vertex has a neighbor in the immediately preceding phase, including the phase \(T-1\) predecessor of phase zero. Define \(x\) by (1), where inequalities use the representatives \(0,\ldots,T-1\). All \(x(v)\) are nonnegative and sum to \(|E_H|\). If \(\tau(v)=t>0\), before time \(t\) its chip count is below \(d(v)\) because its predecessor-phase neighbor has not fired before time \(t-1\); at time \(t\) the count becomes exactly \(d(v)\) and it fires. Subsequently its count stays at most \(d(v)-1\) until the next period, since at least one neighbor fired earlier than time \(t\). If \(\tau(v)=0\), it starts with exactly \(d(v)\), fires immediately, and stays below threshold until time \(T\) since a neighbor fires only in the final phase. The graph returns to the identical chip vector after all vertices have fired once, and no earlier time repeats the vector: any shorter period would make the single firing per vertex in \(T\) rounds occur an integer multiple greater than one. Thus \(T\) is the least period. The chip allocation is uniquely determined by the phase assignment, so the correspondence is bijective.

**2. Specialization to complete multipartite graphs.** An independent set in \(G\) lies inside one multipartite part. Therefore a nonempty firing round belongs to exactly one part. Because every vertex needs a neighbor in the preceding round, two consecutive round labels (cyclically) must be different. Conversely, every cyclic part-label word with different consecutive labels, combined with a surjective assignment of the vertices of each part to that part's prescribed rounds, satisfies the phase lemma. If part \(i\) occurs \(k_i\) times, the number of assignments of its \(n_i\) labelled vertices to the \(k_i\) specified nonempty rounds is \(k_i!\left\{\begin{smallmatrix}n_i\\k_i\end{smallmatrix}\right\}\). Multiplication and summation give the formula. The trace expression follows by expanding closed directed walks in the matrix of allowed successive part labels.

**3. Sharp support.** Any proper cyclic word of length \(T\) using \(k_i\) copies of part \(i\) requires \(k_i\le\lfloor T/2\rfloor\). All \(r\) nonempty parts must occur, and no vertex fires twice; hence \(T\ge r\) and \(T\le N\). Applying the multiplicity bound to a largest part selected into the word shows \(T\le2(N-M)\) if \(T\) exceeds the number of vertices outside the largest part: because at most \(N-M\) non-largest-part vertices can separate its occurrences. More precisely, if \(M>N/2\), the word uses at most \(N-M\) letters from the other parts, so its largest-part count cannot exceed the number of these separators and \(T\le2(N-M)\). If \(M\le N/2\), the bound \(T\le2(N-M)\) follows already from \(T\le N\).

Conversely fix an integer \(T\) in the proposed interval and put \(h=\lfloor T/2\rfloor\). There are positive integers \(k_i\le\min\{n_i,h\}\) with sum \(T\): the sum of the upper capacities is at least \(T\). Indeed, if no \(n_i\) reaches \(h\), that sum is \(N\). If exactly one part reaches \(h\), it is a largest part, and the capacity sum is \(h+(N-M)\ge T\). If at least two parts reach \(h\), their capacity contribution is \(2h\) and at least one further nonempty part supplies the extra unit possibly needed when \(T\) is odd. Start with \(k_i=1\) and distribute \(T-r\) additional units up to these capacities. On the selected \(T\) vertices, the complete multipartite graph with part sizes \(k_i\) has minimum degree \(T-\max k_i\ge T/2\). By the classical Dirac Hamilton-cycle criterion, it has a Hamilton cycle; reading its part labels gives a proper cyclic word with the prescribed multiplicities. Every coefficient and Stirling factor in the relevant summand is positive. This establishes all periods in the interval.

## Verification
Independent verification was performed with two standalone Python standard-library programs. `check_dynamics.py` enumerates **every nonnegative critical-mass chip allocation** in nine graphs (20,814 allocations in total), explicitly follows the update map and counts configurations which are initially periodic and fire each vertex once. `check_formula.py` independently enumerates cyclic part words and calculates Stirling-factor census numbers. Their nine per-period distributions agree exactly; for example, \(K_{2,2,1}\) gives \((6,16,40)\) at periods \((3,4,5)\), while \(K_{2,2,2}\) gives \((6,24,120,192)\) at periods \((3,4,5,6)\). Both programs and their actual outputs are embedded; run with Python 3 standard library. These finite tests are corroboration, not an infinite proof.

## Relationship to prior work
Jiang, *On the Period Lengths of the Parallel Chip-Firing Game* (first submitted March 4, 2010, arXiv:1003.0943), establishes attainable periods and constructs configurations on complete multipartite graphs. In its discussion, \(K_{2,2,1}\) appears as an explicit period-five example, without a count of its full critical-mass single-pass period-five sector. The present theorem counts precisely \(40\) labelled states, or eight distinct five-cycles, in that sector, and gives all period counts and sharp possible periods for every complete multipartite graph with at least three parts.

Scully, Jiang and Zhang, *Firing Patterns in the Parallel Chip-Firing Game* (2013 conference paper, extended journal version 2015), characterize possible periodic firing patterns by nonclumpiness; this does not, by itself, enumerate the chip allocations in the present labelled sector. Goles and Prisner, *Source Reversal and Chip Firing on Graphs* (2000), study the closely related source-reversal mechanism. Their full article was not accessible in this examination, so any pre-existing corresponding phase lemma is **not** claimed to be new. The distinguishing candidate contribution here is the multipartite **exact Stirling-weighted temporal-orbit census and the full sharp no-gap interval in the stated critical single-pass sector**, not the existence of source-reversal dynamics or the known complete-bipartite special case.

## Limitations
This does not characterize all periodic chip-firing states at a given chip mass: states with more than one firing per vertex in the least period are excluded. It does not count transients or basins. The critical-mass and single-pass hypotheses are essential to the argument. The source-reversal paper was read only at abstract level and may carry unrecognized related results. Historical originality is therefore subject to further primary-literature review and independent validation; finite tests do not establish novelty or prove the theorem without the analytic argument.

## References
- T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943, first public preprint March 4, 2010. https://arxiv.org/abs/1003.0943
- Z. Scully, T.-Y. Jiang and Y. X. Zhang, *Firing Patterns in the Parallel Chip-Firing Game*, DMTCS Proceedings (FPSAC), 2013/2014. https://dmtcs.episciences.org/en/articles/2421
- E. Goles and E. Prisner, *Source Reversal and Chip Firing on Graphs*, Theoretical Computer Science 233 (2000), 287–295, doi:10.1016/S0304-3975(99)00122-X.
- G. A. Dirac, *Some theorems on abstract graphs*, Proc. London Math. Soc. (1952), 69–81 (Hamilton-cycle minimum-degree criterion).
