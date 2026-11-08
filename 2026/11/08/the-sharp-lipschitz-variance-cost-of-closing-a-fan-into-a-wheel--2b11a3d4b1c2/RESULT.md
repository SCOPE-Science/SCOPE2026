# The sharp Lipschitz variance cost of closing a fan into a wheel

## Finding
For every integer \(m\ge4\), put \(F_m=K_1\vee P_m\), the graph obtained by joining a new apex to all vertices of a path on \(m\) vertices. Add the edge between its two path ends to obtain the wheel \(W_m=K_1\vee C_m\). There are \(N=m+1\) vertices in both graphs. For a finite connected graph \(G\), define its **Lipschitz spread** by
\[
\operatorname{spr}(G)=\max_{f:V(G)\to\mathbb R,\ |f(u)-f(v)|\le1\ (uv\in E(G))}\left[\frac1{|V(G)|}\sum_v f(v)^2-\left(\frac1{|V(G)|}\sum_v f(v)\right)^2\right].
\]
The same constraint is exactly the unit Lipschitz condition for the unweighted shortest-path metric. Put \(\varepsilon_k=0\) for even \(k\) and \(\varepsilon_k=1\) for odd \(k\). Then
\[
\operatorname{spr}(F_m)=\frac{m-1}{N}-\frac{\varepsilon_{m-1}}{N^2},\qquad
\operatorname{spr}(W_m)=\frac{m-2}{N}-\frac{\varepsilon_{m-2}}{N^2},
\]
and the exact effect of the single new edge is
\[
\boxed{\operatorname{spr}(F_m)-\operatorname{spr}(W_m)=\frac{N-(-1)^m}{N^2}>0.}
\]
The fan formula also holds at \(m=3\), when \(\operatorname{spr}(F_3)=1/2\). The wheel statement starts at \(m=4\): \(W_3\) is the complete graph on four vertices and has spread \(1/4\).

For every maximizing real-valued function, subtract its apex value. For a fan, the path then consists of one contiguous block of \(+1\), one internal \(0\), and one contiguous block of \(-1\), in either order, with block lengths \(\lfloor(m-1)/2\rfloor\) and \(\lceil(m-1)/2\rceil\). For a wheel, the cyclic rim consists of one block of \(+1\), then one \(0\), one block of \(-1\), then one more \(0\); block lengths are \(\lfloor(m-2)/2\rfloor\) and \(\lceil(m-2)/2\rceil\). Conversely every such arrangement is maximizing. The numbers of apex-normalized maximizing configurations are respectively \(2\) and \(4\) for odd and even \(m\) in the fan, and \(2m\) and \(m\) for odd and even \(m\) in the wheel.

## Assumptions and scope
All graphs are finite, simple, undirected, unweighted and have the counting measure normalized to a probability. The inputs are real. Variance uses **all** vertices, including the apex, with equal masses. The apex is an additional vertex, so \(m\) denotes the number of path/cycle vertices, not the total graph order. Every edge has unit Lipschitz budget. The result concerns the variance optimum rather than the difference between extreme adjacency eigenvalues, sometimes also called graph spread.

## Proof
**1. Integral extremality.** Translation lets us fix \(f(h)=0\) at the apex \(h\). The apex edges force \(-1\le f(v)\le1\) on all \(m\) rim vertices. Let \(\mathcal P\) be the compact convex polytope of feasible rim values. The variance quadratic form is strictly convex on the anchored space: for distinct anchored vectors \(f,g\), \(\operatorname{Var}(f-g)>0\), since an anchored constant function must vanish. Consequently a variance maximizer must be a vertex of \(\mathcal P\).

Every vertex of \(\mathcal P\) is integral. Indeed, suppose a feasible vector has a nonintegral rim coordinate. Consider a connected component \(C\) of nonintegral rim vertices linked by **tight** edges \(uv\) with \(|f(u)-f(v)|=1\). No tight edge can connect a nonintegral vertex with an integral one, since their difference would be the integer \(\pm1\). Each bound \(-1\le f(v)\le1\) at a nonintegral coordinate is strict, and every edge from \(C\) to its complement has a slack inequality. A sufficiently small common perturbation \(\pm\delta\) of all coordinates in \(C\) therefore remains feasible in both directions. The vector is a nontrivial midpoint and is not a vertex. Hence every maximizing rim coordinate belongs to \(\{-1,0,1\}\). This establishes integrality for **all** maximizers, not merely the existence of one integral optimum.

**2. Reduction to counts.** Write \(a\), \(b\), \(z\) for the number of rim vertices labeled \(+1\), \(-1\), \(0\). Thus \(a+b+z=m\), and the apex itself has value zero. Exact expansion of the uniform variance gives
\[
N^2\operatorname{Var}(f)=N(a+b)-(a-b)^2.
\]
If both signs occur, no \(+1\) rim vertex can be adjacent to a \(-1\) rim vertex. On the path, this forces \(z\ge1\); on the cycle, it forces \(z\ge2\). For a fixed number \(t=a+b\), the smallest possible \((a-b)^2\) is \(\varepsilon_t\), attained precisely when \(a,b\) are as equal as possible. Consequently for a fan with both signs, the score is bounded by \(N(m-1)-\varepsilon_{m-1}\). If \(z\ge2\), then the score is at most \(N(m-2)\), strictly smaller because \(N>1\). For a wheel with both signs, the analogous bound is \(N(m-2)-\varepsilon_{m-2}\); if \(z\ge3\), the score is at most \(N(m-3)\), again strictly smaller.

Both bounds are attained: use one interior zero between two balanced sign blocks for the path (possible for \(m\ge3\)), or two separating zeros and two balanced sign blocks around the cycle (possible for \(m\ge4\)).

**3. Excluding one-sign competitors.** If the rim contains at most one nonzero sign, write \(t=a+b\). Its score is \(t(N-t)\le N^2/4\). On a fan \(N\ge4\), \(N(N-2)-1>N^2/4\), because \(3N^2/4-2N-1>0\). On a wheel \(N\ge5\), \(N(N-3)-1>N^2/4\), because \(3N(N-4)/4-1>0\). Thus no such function is optimal. The strict count comparisons in Step 2 force exactly the claimed zero counts and balance. Minimal zero count forces the sign-block arrangement: a path has one separator, and a cycle has two. This proves the complete equality classification and formulas for both spreads.

**4. Edge penalty, counting and asymptotics.** Subtracting the two formulas, using \(\varepsilon_{m-1}-\varepsilon_{m-2}=(-1)^m\), gives the boxed gap. The orientation and placement choices give the stated finite counts of normalized extremizers. In particular,
\[
\operatorname{spr}(F_m)=1-\frac2N-\frac{\varepsilon_{m-1}}{N^2},\qquad
\operatorname{spr}(W_m)=1-\frac3N-\frac{\varepsilon_{m-2}}{N^2}.
\]
Both graphs have diameter two, hence the universal diameter-squared variance bound is \(1\), and these formulas quantify approach to it.

## Verification
A standalone standard-library Python program `checker.py` independently enumerates all feasible integer rim vectors for \(3\le m\le10\), separately testing paths and cycles in their stated ranges. It computes exact rational variances, verifies every maximizing profile and checks the predicted parity formula. It further checks the exact algebraic edge-gap identity for \(4\le m<200\). The checker is finite corroboration; the proof above establishes the infinite theorem independently of the enumerated cutoff. Run `python3 checker.py` from the extracted package.

## Relationship to prior work
Alon, Boppana and Spencer [1] introduced graph spread and proved that an integral maximizing potential exists for a finite graph, along with a general distance-to-zero-set structure theorem. Those results make this extremal problem natural, but they do **not** state the two exact fan/wheel constants, enumerate all corresponding optimizers, or quantify the effect of closing exactly one rim edge. Addario-Berry, Janson and McDiarmid [2] used the same variance invariant for random graphs rather than the present deterministic apex-path/apex-cycle comparison. Yancey [3] analyzed variance-optimal Lipschitz functions and applications to concentration and products; his inspected results include trees with hairs and cycles, not these joined apex graphs. The present proof gives the complete comparison, including the parity-sensitive one-edge decrement, directly from the anchored Lipschitz polytope.

## Limitations
The theorem assumes uniform vertex masses, real-valued functions, unit graph edges, and a single apex joined to every rim vertex. It does not determine the spread of weighted fans/wheels, graphs with missing spokes, multiple-apex joins, or arbitrary diameter-two graphs. Exact formulas for one family do not imply a general edge-deletion law. No claim is made that the older general integral-extremizer theorem is new. The originality comparison is literature-based and not a proof that no equivalent result exists outside the inspected sources.

## References
[1] N. Alon, R. Boppana and J. Spencer, *An Asymptotic Isoperimetric Inequality*, Geometric and Functional Analysis 8 (1998), 411–436, DOI: 10.1007/s000390050062. Author-hosted full text: https://web.math.princeton.edu/~nalon/PDFS/iso7.pdf, especially §2.1.

[2] L. Addario-Berry, S. Janson and C. McDiarmid, *On the spread of random graphs*, arXiv:0902.1156, first posted 2009-02-06, https://arxiv.org/abs/0902.1156.

[3] M. Yancey, *Probabilistic and Geometrical Applications to Graph Theory*, arXiv:1705.09725, first posted 2017-05-26, https://arxiv.org/abs/1705.09725.
