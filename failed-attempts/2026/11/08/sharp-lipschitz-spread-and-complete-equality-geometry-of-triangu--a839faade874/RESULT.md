# Sharp Lipschitz spread and complete equality geometry of triangular graphs

## Finding
For every integer \(n\ge 4\), let \(T_n=J(n,2)=L(K_n)\), the graph whose vertices are the two-element subsets of \([n]\), with two vertices adjacent exactly when the subsets intersect. Give the \(N=\binom n2\) vertices equal probability and use unit graph-edge lengths. For real functions on its vertices, set
\[
\operatorname{spr}(T_n)=\max_{\lvert f(v)-f(w)\rvert\le1\ (vw\in E(T_n))}\operatorname{Var}_{v\in V(T_n)} f(v).
\]
Then the sharp constant is
\[
\boxed{\operatorname{spr}(T_n)=
\begin{cases}
\dfrac{n-2}{2(n-1)},&n\text{ even},\\
\dfrac{(n-2)(n+1)}{2n^2},&n\text{ odd}.
\end{cases}}
\]
Every maximizer, and only a maximizer, has the following form up to adding a constant. Choose a partition \([n]=X\sqcup Y\) with \(\{|X|,|Y|\}=\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\). Put \(f(e)=0\) if \(e\subset X\), \(f(e)=2\) if \(e\subset Y\), and \(f(e)=1\) if \(e\) meets both parts. Interchanging the parts includes sign reversal. Modulo addition of constants, there are exactly \(\binom{n}{n/2}\) maximizers for even \(n\) and \(2\binom{n}{\lfloor n/2\rfloor}\) for odd \(n\). The spread tends to \(1/2\) as \(n\to\infty\).

Equivalently, the square root of the displayed constant is the exact norm of the canonical linear inclusion from real Lipschitz functions modulo constants (with graph Lipschitz norm) into centered \(L^2(V(T_n))\). The result is an equality classification, not merely an existence assertion.

## Assumptions and scope
The graph is simple and unweighted, \(n\) is an integer at least four, the probability measure is uniform on its \(N\) vertices, the scalar field is real, and the Lipschitz inequality is imposed on every pair of incident edges of \(K_n\) (equivalently every edge of \(T_n\)). Variance means \(N^{-1}\sum_e(f(e)-N^{-1}\sum_h f(h))^2\). Translating \(f\) does not affect its Lipschitz seminorm or variance. The graph has diameter two.

## Proof
**1. Integral extremizers and the three-level reduction.** Anchor one vertex value to zero. The resulting Lipschitz polytope is compact because the graph is connected. Variance is strictly convex on the anchored vector space: its quadratic part is zero only on constant vectors, and an anchored constant is zero. Therefore every maximizing point is a vertex of the anchored polytope. If the subgraph consisting of edges \(vw\) with \(|f(v)-f(w)|=1\) were disconnected, a connected component could be perturbed by both sufficiently small positive and negative constants, keeping the anchor fixed by choosing a component not containing it. This contradicts extremality. A spanning tree of tight edges thus determines every anchored value as an integer. After subtracting the minimum, the values belong to \(\{0,1,2\}\), since \(T_n\) has diameter two. If the range is at most one, the integer values are binary and the variance is at most \(\lfloor N^2/4\rfloor/N^2\le1/4\).

**2. Separation of the extreme levels.** Suppose both levels zero and two occur, and let \(a\) and \(b\) be their numbers of vertices. A vertex of \(T_n\) is an edge of \(K_n\). A level-zero edge and a level-two edge cannot share an endpoint, since they would be adjacent in \(T_n\) but have value difference two. Consequently the unions of endpoints of the level-zero and level-two families are disjoint subsets of \([n]\). Extend these subsets to a partition with parts of sizes \(n-t\) and \(t\), where \(2\le t\le\lfloor n/2\rfloor\). Write
\[
A=\binom{n-t}{2},\qquad B=\binom t2,\qquad D=A-B\ge0.
\]
The two extreme-level counts can be assigned to the two capacities \(A,B\). Since the objective is symmetric in \(a,b\), we may optimize over \(0\le b\le B\), \(b\le a\le A\). To justify this even if the original larger count occupied the smaller capacity: if \(a<b\) with \(a\le A,b\le B\), interchange the numerical counts; then \(b\le B\le A\) and \(a<b\le B\) ensure the swapped pair remains feasible. The variance identity is
\[
N^2\operatorname{Var} f=N(a+b)-(a-b)^2=:Q(a,b).
\]
Put \(v=a-b\ge0\) and \(u=a+b\). The capacity inequalities imply
\[
u\le\min(2A-v,2B+v),\qquad
Q\le N\min(2A-v,2B+v)-v^2.
\]
For \(0\le v\le D\) the second bound is \(N(2B+v)-v^2\); for \(v\ge D\) it is \(N(2A-v)-v^2\). The latter is strictly decreasing. Hence if \(D\le N/2\), the unique maximum is at \(v=D\), \(u=A+B\), namely \(a=A,b=B\), with value
\[
Q_t=N(A+B)-D^2.
\]
If \(D>N/2\), the upper bound is instead
\[
Q(a,b)\le N^2/4+2NB.
\]
These continuous upper bounds apply a fortiori to the required integer counts.

**3. Balanced parts strictly dominate.** Since \(A+B=N-t(n-t)\) and \(D=(n-1)(n/2-t)\), the full-capacity objective satisfies
\[
Q_t=N^2-\frac{n^2(n-1)^2}{4}+
\left((n-1)^2-N\right)t(n-t).
\]
The coefficient is \((n-1)(n-2)/2>0\). Thus, in the regime \(D\le N/2\), the unique maximum (up to swapping parts) occurs at \(t=\lfloor n/2\rfloor\). Let \(Q_*\) be this balanced objective. Direct evaluation gives
\[
Q_*=\begin{cases}
N\,n(n-2)/4,& n\text{ even},\\
((n-1)/2)^2(N-1),&n\text{ odd}.
\end{cases}
\]
It remains to rule out the other regime. The inequality \(D>N/2\) forces \(t<n/4\), so
\[
B=\binom t2<\frac{n(n-4)}{32},\qquad
Q<N^2/4+\frac{Nn(n-4)}{16}.
\]
For even \(n\), \(Q_*/N\) exceeds the last upper bound divided by \(N\) by \(n(n-2)/16>0\). For odd \(n\), that difference is \((n-2)^2(n+2)/(16n)>0\). Thus no unbalanced capacity allocation can attain \(Q_*\). Finally \(Q_*/N^2\ge1/3>1/4\) for every \(n\ge4\) (immediate from its two explicit formulas), so no binary or constant potential maximizes.

**4. Equality and counting.** Every maximizing pair of families must attain the complete balanced capacities in Step 2. Thus the level-zero and level-two families are exactly the complete edge sets within the two balanced parts, and all cross-part edges have value one. Conversely that assignment is one-Lipschitz because every level-zero edge is disjoint from every level-two edge, and all other differences are at most one. The balanced objective produces the stated formula. Distinct partitions with a distinguished level-zero side yield distinct anchored functions. For even \(n\) there are \(\binom{n}{n/2}\); for odd \(n\), either size can be the level-zero side, yielding \(2\binom{n}{\lfloor n/2\rfloor}\). Strict convexity in Step 1 excludes nonintegral or convex-mixture maximizers. The limiting value follows from the explicit formulas.

## Verification
Run `python3 verify_triangular_spread.py` using Python's standard library. The checker exhaustively enumerates all feasible integer three-level configurations on \(T_4,T_5,T_6\) and obtains sharp numerator/multiplicity pairs \((12,6),(36,20),(90,20)\). It separately checks 22,201 exact capacity inequalities up to \(n=300\) and the closed-form identities through \(n=3000\). These are finite corroborations only; Steps 1–4 establish the theorem for every integer \(n\ge4\).

## Relationship to prior work
Alon, Boppana and Spencer established the graph Lipschitz spread invariant and an integral-extremizer principle, principally to study high-dimensional product isoperimetry. The present proof gives a self-contained version of that integral reduction. Addario-Berry, Janson and McDiarmid studied spread on random graph models and recalled the elementary complete-graph constant and Cartesian-product tensorization; neither of those gives the triangular-graph sharp formula. Yancey analyzed variance-optimal graph functions and various tree-like and cycle families rather than this Johnson graph. The triangular graph is the complement of the Kneser graph on two-subsets, but complementing the adjacency relation changes the Lipschitz admissible set and does not transfer the numerical optimum or equality classification. The new content is the exact complete-family sharp embedding constant, all norming potentials, and their multiplicity. Searches did not uncover a prior exact computation for \(J(n,2)\); this is not a proof of global bibliographic novelty.

## Limitations
The result applies only to the two-subset Johnson graph with its ordinary unit-edge graph metric, uniform vertex probability and real-valued one-Lipschitz functions. It does not determine graph spread for \(J(n,k)\) when \(k\ge3\), for nonuniform measures, weighted edges or higher moments. The comparison with indexed and accessible literature cannot exclude equivalent unindexed calculations. No independent mathematical audit has been performed.

## References
1. N. Alon, R. Boppana and J. Spencer, *An asymptotic isoperimetric inequality*, Geom. Funct. Anal. **8** (1998), 411–436; doi:10.1007/s000390050062. Author-hosted full text: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf (Section 2.1, Theorem 2.1).
2. L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156, initially public 2009-02-06; https://arxiv.org/abs/0902.1156 (especially Section 1 and Section 8).
3. M. P. Yancey, *Probabilistic and Geometrical Applications to Graph Theory*, arXiv:1705.09725, initially public 2017-05-26; https://arxiv.org/abs/1705.09725 (Sections 1 and 2.5).
