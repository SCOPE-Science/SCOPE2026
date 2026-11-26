# Full-system Abelian sandpile avalanches on complete bipartite graphs: a deletion-tree law and a rare-event activity fraction

## Finding

Let \(a,b\ge2\) be integers. On the simple undirected graph \(G=K_{a,b}\), designate a vertex \(s\) of the \(a\)-vertex part as a sink, and fix a vertex \(t\) of the opposite part as the addition site. Under the uniform recurrent measure, let \(T\) be the total number of nonsink topplings after adding one chip to \(t\). Then

\[
\max T=a+b-1,\qquad
\Pr\{T=a+b-1\}=\frac1b\left(1-\frac1a\right)^{b-1},\qquad
\mathbb E T=\frac{a+b-1}{b}.
\]

There are exactly \(b^{a-2}(a-1)^{b-1}\) maximizing recurrent configurations out of \(a^{b-1}b^{a-1}\). The maximizing configurations are naturally in bijection with recurrent configurations of the smaller bipartite graph \(H=K_{a-1,b}\), now rooted at \(t\). The fraction of total expected toppling activity arising from the maximizing event is exactly
\[
\frac{\mathbb E[T\mathbf1_{\{T=a+b-1\}}]}{\mathbb E T}
=\left(1-\frac1a\right)^{b-1}.
\]
In the balanced family \(a=b=n\to\infty\), this fraction tends to \(e^{-1}\), even though the maximizing event has probability \(\sim 1/(en)\). Thus a vanishingly rare system-spanning avalanche carries a nonvanishing fraction of mean activity.

## Assumptions and scope

All vertices and edges are labeled and unweighted. A nonsink vertex with at least its degree many chips topples by sending one chip across each incident edge, with chips reaching \(s\) discarded. A configuration \(h\) is stable when \(0\le h_v<\deg_G(v)\) at every nonsink vertex; recurrence is in the standard Abelian-sandpile sense, equivalently Dhar's forbidden-subconfiguration or burning criterion. The distribution is uniform over all recurrent stable configurations. The sink \(s\) lies in the \(a\)-part, and the fixed driven vertex \(t\) lies in the \(b\)-part, so \(s\) and \(t\) are adjacent. The result treats finite \(a,b\ge2\), not arbitrary driving sites or random drive protocols.

## Proof

**1. Universal one-toppling upper bound.** Write \(h^{\max}_v=\deg_G(v)-1\). Starting from \(h^{\max}+\mathbf e_t\), topple \(t\) once, then all \(a-1\) other nonsink vertices of the \(a\)-part once, then all \(b-1\) remaining vertices of the \(b\)-part once. Every indicated toppling is legal: \(t\) starts unstable; each nonsink \(a\)-vertex receives one chip from \(t\); each other \(b\)-vertex receives \(a-1\) chips after starting at \(a-1\). All final heights are below their degrees: the \(a\)-vertices finish at \(b-1\), \(t\) at \(a-1\), and other \(b\)-vertices at \(a-2\). Thus the odometer of this configuration is identically one. Monotonicity of the least-action odometer under coordinatewise increase of the initial heights shows that \(h+\mathbf e_t\), for **every** stable \(h\le h^{\max}\), has odometer bounded above by one coordinatewise. Consequently \(T\le a+b-1\).

**2. Exact characterization of equality.** If \(T=a+b-1\), every nonsink vertex topples exactly once. The first toppling must be \(t\), so \(h_t=a-1\). For any other vertex \(v\) of the \(b\)-part, its final height is \(h_v-1\), hence \(h_v\ge1\). Delete the original sink \(s\) and make \(t\) the new sink in \(H=K_{a-1,b}\). Construct a configuration \(h'\) on \(H\setminus\{t\}\) by
\[
h'_u=h_u\quad(u\in A\setminus\{s\}),\qquad
h'_v=h_v-1\quad(v\in B\setminus\{t\}).
\]
It is stable since \(H\)-degrees are \(b\) on \(A\setminus\{s\}\) and \(a-1\) on \(B\setminus\{t\}\). After the initial toppling of \(t\) in \(G\), the remaining legal-toppling test, heights relative to degree, and each remaining toppling are exactly those of the burning test of \(h'\) on \(H\): removing \(s\) decreases both the height and toppling threshold of every \(B\setminus\{t\}\) vertex by one, and \(t\)'s initial firing supplies precisely one chip to each \(A\setminus\{s\}\). By Dhar's burning criterion, all the remaining vertices topple once if and only if \(h'\) is recurrent on \(H\) rooted at \(t\).

Conversely, any recurrent \(h'\) on \(H\) rooted at \(t\) yields a stable \(h\) on \(G\) by \(h_t=a-1\), \(h_u=h'_u\) for \(u\in A\setminus\{s\}\), and \(h_v=h'_v+1\) for \(v\in B\setminus\{t\}\). This reconstructed \(h\) is recurrent on \(G\): for any nonempty subset \(U\) of nonsink vertices, if \(t\in U\), then \(h_t=a-1\ge\deg_U(t)\), so \(U\) is not a forbidden subconfiguration. Otherwise the recurrent \(h'\) on \(H\) supplies a vertex \(v\in U\) with \(h'_v\ge\deg_U(v)\), and \(h_v\ge h'_v\). Therefore no nonempty forbidden subconfiguration exists. Its addition at \(t\) generates one toppling at every nonsink vertex by the burning correspondence. The maps are inverse, hence a bijection.

**3. Counting and probability.** The matrix-tree theorem gives
\[
\#\operatorname{Rec}(G,s)=\tau(K_{a,b})=a^{b-1}b^{a-1},\qquad
\#\operatorname{Rec}(H,t)=\tau(K_{a-1,b})=(a-1)^{b-1}b^{a-2}.
\]
The latter is positive, so the upper bound from Step 1 is achieved. Dividing yields the claimed probability and count.

**4. Mean activity.** Addition at a fixed vertex acts as a permutation of recurrent states. For the unique odometer \(u\), stabilization satisfies \(h^{\mathrm{final}}=h+\mathbf e_t-\Delta u\). Averaging uniformly over the recurrent class gives \(\Delta\,\mathbb E u=\mathbf e_t\), since initial and final heights have the same distribution. With the three symmetric classes \(A\setminus\{s\}\), \(\{t\}\), \(B\setminus\{t\}\), direct solution yields
\[
(\mathbb E u)_A=\frac1b,\qquad
(\mathbb E u)_t=\frac{a+b-1}{ab},\qquad
(\mathbb E u)_{B\setminus\{t\}}=\frac{a-1}{ab}.
\]
Summing over the \(a+b-1\) nonsink vertices gives \(\mathbb E T=(a+b-1)/b\). Since the maximizing event contributes \((a+b-1)\Pr\{T=a+b-1\}\) to the mean, the exact activity fraction and balanced \(e^{-1}\) limit follow. The balanced event probability is \(n^{-1}(1-1/n)^{n-1}\sim1/(en)\).

## Verification

Two independent, standard-library Python programs are included. From the extracted package, run `python3 checks/exhaustive.py` and `python3 checks/structural.py`. The first checks recurrence by the forbidden-subconfiguration criterion, enumerates every stable configuration, performs explicit legal stabilizations, and compares exact event counts, maxima and rational means. The second independently uses the burning test on the smaller auxiliary graph, constructs every maximizing configuration, checks stability and one toppling per vertex, and solves the original reduced Laplacian in exact rational arithmetic. Both pass on ten graph sizes \((a,b)\in\{(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(4,4),(5,3)\}\). These finite verifications check the implementation and representative boundary cases; the general statement is established by the proof, not enumeration.

## Relationship to prior work

Dukes–Le Borgne [1] and Aval–D'Adderio–Dukes–Le Borgne [2] study recurrent configurations on complete bipartite graphs and supply foundational recurrence/parking-function viewpoints. Their inspected results concern recurrent-state characterization and lattice-path structure, rather than the fixed-drive full-avalanche count, the deletion-tree bijection, or its contribution to the mean. Austin–Chambers–Funke–García Puente–Keough [3], Corollary 9, already prove that addition at a neighbor of the sink entails at most one toppling per vertex; this known general fact is used but **not claimed as new**. Their graph-family avalanche-polynomial calculations cover trees, cycles, complete graphs and wheels, not the present bipartite extremal coefficient. Selig–Zhu [4] gives further recurrent-state classifications for the same graph family but does not state the fixed-drive maximal-avalanche count in its inspected results. Known recurrence, burning, Green-function, and matrix-tree ingredients are duly acknowledged. The claimed contribution is their exact combination into the fixed-drive extremal-bijection count and rare-event activity law for the complete bipartite family.

## Limitations

This is a result for finite simple complete bipartite graphs, one sink in the \(a\)-part, a fixed neighboring addition vertex in the \(b\)-part, and the stationary uniform recurrent distribution. No claim is made about full avalanche-size distributions, nonadjacent drive, multiple sinks, nonuniform edges, or scaling on sparse two-dimensional lattices. Historical priority is based on inspected sources rather than an exhaustive literature census; an equivalent specialized statement could be unindexed. No independent scientific audit has been completed.

## References

1. M. Dukes and Y. Le Borgne, *Parallelogram polyominoes, the sandpile model on a complete bipartite graph, and a q,t-Narayana polynomial*, first publicly submitted 2012-07-31, https://arxiv.org/abs/1208.0024.
2. J.-C. Aval, M. D'Adderio, M. Dukes and Y. Le Borgne, *Two operators on sandpile configurations, the sandpile model on the complete bipartite graph, and a Cyclic Lemma*, first publicly submitted 2013-07-29, https://arxiv.org/abs/1307.7740.
3. D. Austin et al., *The Avalanche Polynomial of a Graph*, first publicly submitted 2016-05-09, https://arxiv.org/abs/1605.02713, especially Proposition 8, Corollary 9, and sections on graph families.
4. T. Selig and H. Zhu, *Abelian and stochastic sandpile models on complete bipartite graphs*, first publicly submitted 2024-09-18, https://arxiv.org/abs/2409.11811.
