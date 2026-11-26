# Opposite-extremum covariance signs reconstruct every graph from random rankings

## Finding

Let \(G=(V,E)\) be any finite simple labelled graph. Assign independent and identically distributed atomless random priorities \(U_v\) to the vertices; only the ranking matters. Let \(P_u\) indicate that the priority at \(u\) is strictly greater than every priority at its neighbors, and let \(V_v\) indicate that the priority at \(v\) is strictly smaller than every priority at its neighbors. An isolated vertex is both a peak and a valley.

For distinct \(u,v\in V\), the covariance has a complete three-way sign law:

\[
\operatorname{sgn}\operatorname{Cov}(P_u,V_v)=
\begin{cases}
+1,&uv\in E,\\
-1,&uv\notin E\ \text{and}\ N(u)\cap N(v)\ne\varnothing,\\
0,&uv\notin E\ \text{and}\ N(u)\cap N(v)=\varnothing.
\end{cases}
\]

Thus the signs of the opposite-extremum cross-covariance matrix identify every edge, every pair at graph distance two, and every more distant pair, without observing priorities or edges. The sign is insensitive to the continuous priority distribution.

More quantitatively, for an edge \(uv\in E\), with \(d_u=|N(u)|\) and \(d_v=|N(v)|\),

\[
\operatorname{Cov}(P_u,V_v)\ge \frac{1}{(d_u+1)d_v(d_v+1)}>0.
\]

If a bound \(\Delta\ge\max_v d_v\ge1\) is known, define \(\gamma=1/[\Delta(\Delta+1)^2]\). Observe \(N\) independent random rankings and their full labelled peak/valley indicator vectors. Declare \(uv\) an edge precisely when the empirical cross-covariance \(\widehat C_{uv}\) exceeds \(\gamma/2\). For \(n=|V|\ge2\) and \(0<\delta<1\), the full graph is recovered with probability at least \(1-\delta\) provided

\[
N\ge72\,\Delta^2(\Delta+1)^4\log\left(\frac{2n(n+1)}{\delta}\right).
\]

This is a sufficient sample bound, not an optimal one.

An exact finite-size formula is also available. Put \(e=\mathbf 1_{uv\in E}\), \(c=|N(u)\cap N(v)|\), \(a=d_u-c-e\), and \(b=d_v-c-e\). If \(e=1\) or \(c\ge1\), then

\[
\mathbb P(P_u=V_v=1)=\int_0^1\int_0^x x^a(1-y)^b(x-y)^c\,dy\,dx
=\sum_{j=0}^b\frac{(-1)^j\binom bj j!c!}{(j+c+1)!(a+j+c+2)}.
\]

For \(e=c=0\), joint probability factors into \(1/[(d_u+1)(d_v+1)]\). In every case \(\mathbb P(P_u=1)=1/(d_u+1)\) and \(\mathbb P(V_v=1)=1/(d_v+1)\).

## Assumptions and scope

The graph is finite, undirected, loopless, simple, and its vertices are individually labelled. Priority draws are independent and identically distributed with an atomless distribution. Distinct vertices are considered for the covariance sign law. The empirical recovery theorem assumes independent repeats of the complete ranking experiment, observed only through peak/valley indicators, a supplied maximum-degree upper bound, and no observation error. The degree-zero case is the immediately identifiable edgeless graph.

## Proof

Probability integral transformation reduces the priority distribution to independent \(\operatorname{Uniform}(0,1)\) variables without changing peaks or valleys. For any vertex \(w\), exchangeability among the priorities of \(w\) and its neighbors gives probability \(1/(d_w+1)\) of being a strict maximum, and likewise a strict minimum.

**Adjacent pairs.** Suppose \(uv\in E\), and let \(c\) count their common neighbors. Condition on \(P_u=1\) and \(U_u=x\). Since \(v\) is a neighbor of \(u\), write \(U_v=xt\) with conditional \(t\) uniform on \((0,1)\); the other \(c\) common-neighbor priorities are independent uniform \((0,x)\), and the \(b=d_v-1-c\) private neighbors of \(v\) have independent uniform \((0,1)\) priorities. Thus

\[
\mathbb P(V_v=1\mid P_u,U_u=x)
=\int_0^1(1-t)^c(1-xt)^b\,dt
\ge\int_0^1(1-t)^{c+b}\,dt=\frac1{d_v}.
\]

After averaging in \(x\), the joint probability is at least \(1/[(d_u+1)d_v]\). Subtract the product of marginals to obtain the claimed strictly positive covariance and degree-dependent lower bound. This argument is also valid when \(b=0\) or \(c=0\).

**Nonadjacent pairs.** Suppose \(uv\notin E\). If they have no common neighbor, their peak and valley events depend on disjoint independent priorities, hence are independent. Otherwise let \(W=N(u)\cap N(v)\) have size \(c\ge1\), with \(M=\max_{w\in W}U_w\) and \(m=\min_{w\in W}U_w\). Conditional on all common-neighbor priorities, the remaining variables involved in the two events are disjoint. With \(a=d_u-c\) and \(b=d_v-c\), their conditional success probabilities are

\[
f(M)=\frac{1-M^{a+1}}{a+1},\qquad
g(m)=\frac{1-(1-m)^{b+1}}{b+1}.
\]

The function \(f\) is strictly decreasing, and \(g\) is strictly increasing. For \(c=1\), \(M=m\) and opposite strict monotonicity implies \(\operatorname{Cov}(f(M),g(m))<0\). For \(c\ge2\), condition on \(M=t\). The other \(c-1\) priorities divided by \(t\) are independent uniform variables; therefore \(m=tZ\), where \(Z\) is the strictly positive minimum of \(c-1\) independent uniforms, independent of \(M\). Hence \(h(t)=\mathbb E[g(tZ)]\) is strictly increasing. It follows that \(\operatorname{Cov}(f(M),g(m))=\operatorname{Cov}(f(M),h(M))<0\). Strict negativity is justified by taking two independent copies of nondegenerate \(M\) and applying the identity \(2\operatorname{Cov}(f(M),h(M))=\mathbb E[(f(M)-f(M'))(h(M)-h(M'))]\). The conditional-independence law identifies this covariance with \(\operatorname{Cov}(P_u,V_v)\).

**Exact joint probability.** When adjacency or a common neighbor forces \(U_u=x>U_v=y\), the \(a\) private neighbors of \(u\) have to be below \(x\), the \(b\) private neighbors of \(v\) above \(y\), and the \(c\) common neighbors strictly between \(y\) and \(x\). Their conditional probabilities multiply to \(x^a(1-y)^b(x-y)^c\). Integration over \(0<y<x<1\) gives the double integral; expanding \((1-y)^b\) and integrating yields the displayed rational sum. When the two neighborhoods are disjoint and the vertices nonadjacent, the two indicator events are independent.

**Recovery from observations.** For each ordered distinct pair define \(\widehat C_{uv}=\overline{P_u V_v}-\overline{P_u}\,\overline{V_v}\). Hoeffding's bound guarantees for each bounded empirical mean \(Z\) that \(\mathbb P(|\overline Z-\mathbb EZ|>\varepsilon)\le2e^{-2N\varepsilon^2}\). There are at most \(n(n+1)\) relevant means, including both marginals, so with \(\varepsilon=\gamma/12\), their simultaneous deviation probability is bounded by \(2n(n+1)e^{-N\gamma^2/72}\). On the complementary event, the covariance error is at most \(3\varepsilon=\gamma/4\), since products of numbers in \([0,1]\) are \(1\)-Lipschitz in each factor. True edges have covariance at least \(\gamma\); all nonedges have covariance at most zero. The \(\gamma/2\) threshold therefore classifies every pair correctly. The stated sample bound makes the failure probability at most \(\delta\).

## Verification

The companion standalone `checker.py` enumerates every labelled simple graph with two through five vertices, every permutation of its vertex priorities, and every ordered distinct pair. With exact rational arithmetic it compares the enumerated joint probabilities against the finite-sum integral, the marginal identities, the three sign cases, and the adjacent-edge quantitative bound. Executing `python3 checker.py` returned `PASS: 1098 labeled graphs, 74708 exact assertions; all rank orders n<=5`. The complete-graph proof above, rather than this finite census, establishes the infinite family of cases.

Two transparent examples: on a three-vertex path, the endpoint peak and other endpoint valley have covariance \(-1/12\); on a triangle, opposite extrema at distinct vertices have covariance \(+1/18\).

## Relationship to prior work

The combinatorics of peak sets in uniformly random permutations is classical. Billey, Burdzy and Sagan (2012) study prescribed peaks of permutations, including valleys of paths. Billey, Burdzy, Pal and Sagan (2013) examine peak and valley configurations on cycles in a probabilistic model. Diaz-Lopez and collaborators (2017) study how to enumerate peak sets on general graphs (under a convention excluding vertices of low degree). These directions overlap in the underlying local-extremum notion, but the checked texts do not state the three-way opposite-extremum *pair covariance* classification on arbitrary finite graphs, the universal edge lower bound, or reconstruction from extremum-only observations. General graph-covariance recovery results using thresholded vertex labels concern different observables and do not imply this exact sign law. The result is not a claim of first-ever use of local extrema or of covariance-based inference.

## Limitations

The inference bound is polynomial but not minimax-optimal and assumes independently redrawn, complete noiseless extrema vectors and a known degree bound. It does not apply automatically to partially observed samples, dependent ranking repetitions, directed graphs, tied priorities, or general vertex-score dependence. The scientific priority assessment is best-knowledge rather than an exhaustive historical uniqueness certificate. A specialist search of older random-rankings and graph-shape reconstruction literature could uncover equivalent formulations. Independent external validation has not been performed.

## References

1. S. C. Billey, K. Burdzy and B. E. Sagan, *Permutations with given peak set*, arXiv:1209.0693, initially publicly posted 2012-09-04. https://arxiv.org/abs/1209.0693
2. S. C. Billey, K. Burdzy, S. Pal and B. E. Sagan, *On meteors, earthworms and WIMPs*, arXiv:1308.2183, initially posted 2013-08-09. https://arxiv.org/abs/1308.2183
3. A. Diaz-Lopez et al., *Counting peaks on graphs*, arXiv:1708.08493, initially posted 2017-08-28. https://arxiv.org/abs/1708.08493
