# Exact disappearance times under repeated two-agent announcements of ignorance

## Finding

In a finite two-agent \(\mathsf{S5}\) model, repeatedly restrict to the worlds where *neither* agent knows whether a fixed atom \(p\). There is an exact world-by-world time formula in terms of directed walks in a bipartite incidence multigraph. With \(N\ge1\) initial worlds, the **sharp greatest number of strict restriction rounds** is
\[
R_N=\max\{\lceil N/2\rceil,N-2\}.
\]
If the two equivalence-class coordinates jointly distinguish every world (a *proper* frame), the sharp value is instead
\[
R_N^{\mathrm{proper}}=\max\{\lceil N/2\rceil,N-4\}.
\]
The directed walk criterion and constructions below establish both bounds for all \(N\), with no probabilistic or asymptotic assumptions. The terminal directed \((1,1)\)-core interpretation is known prior graph mathematics; the claimed contribution is the **exact synchronous disappearance profile in the stated epistemic model and its two sharp size laws**.

## Assumptions and scope

Let \(M=(W,E_a,E_b,V)\) be a finite nonempty Kripke model, with \(|W|=N\ge1\), \(E_a,E_b\) equivalence relations on \(W\), and \(p\) true precisely at \(V(p)\subseteq W\). For any current nonempty domain \(U\subseteq W\), put
\[
\psi=(\neg K_a p\wedge\neg K_a\neg p)\wedge(\neg K_b p\wedge\neg K_b\neg p).
\]
Starting from \(W_0=W\), define \(W_{t+1}=\{w\in W_t:M\restriction W_t,w\models\psi\}\); once \(W_t=\varnothing\), put all following sets empty. A *strict restriction round* is a step with \(W_{t+1}\subsetneq W_t\); the stabilization time \(r\) is the smallest nonnegative integer with \(W_{r+1}=W_r\). This is ordinary **world-deleting** public-announcement model restriction, not an arrow-deleting believed announcement. After the world containing a designated point disappears, the remaining sequence is understood set-theoretically, not as continued truthful announcements at that vanished point.

Construct a directed bipartite **multigraph** \(D_M\): the vertices on the left are \(E_a\)-classes and on the right are \(E_b\)-classes. Each world is a distinct arc between its classes, left-to-right when \(p\) is true and right-to-left when \(p\) is false. Parallel oppositely oriented arcs are allowed for distinct worlds with both coordinates equal. A frame is *proper* if different worlds never occupy the same class pair; equivalently, \(D_M\) has no parallel arcs even after orientation is forgotten.

For each vertex \(v\), let \(h^-(v)\) be the supremum of lengths of directed walks ending at \(v\), and \(h^+(v)\) the supremum of lengths of directed walks starting at \(v\). Walk length zero is allowed. The values lie in \(\mathbb N\cup\{\infty\}\); \(\infty\) means arbitrarily long walks, equivalently appropriate reachability to or from a directed cycle.

## Proof

**(1) Translation to directed peeling.** In a restricted S5 equivalence class, \(\neg K_i p\wedge\neg K_i\neg p\) holds at every member exactly when the class contains at least one \(p\)-world and one \(\neg p\)-world. In \(D_M\), this is equivalent to the corresponding class vertex having at least one incoming and one outgoing arc. Therefore one restriction round deletes simultaneously all arcs incident with a vertex with zero indegree or zero outdegree, within the current arc set. This includes empty and singleton classes without exception.

**(2) Exact arc-survival law.** For an arc \(e:u\to v\), prove for every integer \(t\ge0\) that
\[
 e\in W_t\quad\Longleftrightarrow\quad h^-(u)\ge t\ \text{and}\ h^+(v)\ge t. \tag{1}
\]
At \(t=0\) this is immediate. Assume (1) at \(t\). If \(e\) survives round \(t+1\), it survived round \(t\) and there is an arc \(f:w\to u\) and an arc \(g:v\to z\), both surviving through round \(t\). By (1), \(f\) extends a directed walk of length \(t\) ending at \(w\), producing length \(t+1\) ending at \(u\). Likewise \(g\) extends a walk of length \(t\) beginning at \(z\), producing length \(t+1\) beginning at \(v\). Conversely, choose directed walks of length \(t+1\) ending at \(u\) and starting at \(v\). Let \(f\) be the final arc in the former and \(g\) the initial arc in the latter. There is a length-\(t\) walk entering the tail of \(f\), and a length-\(t\) walk starting at its head \(u\), supplied by \(e\) followed by a sufficient prefix of the latter walk. Thus \(f\) survives round \(t\) by the induction hypothesis. Symmetrically, \(g\) survives round \(t\), using a suffix of the first walk, then \(e\), and the remaining second walk. The two length-\(t+1\) walks also supply the length-\(t\) conditions for \(e\), so \(e\) survives through \(t\) and both its endpoint vertices have in/out neighbors there. It consequently survives round \(t+1\), proving (1).

Put \(d(e)=\min\{h^-(u),h^+(v)\}\). Thus an arc with finite \(d(e)\) disappears **exactly in restriction round \(d(e)+1\)**, and an arc with infinite \(d(e)\) survives all rounds. In particular,
\[
 r=\max\bigl(\{d(e)+1:d(e)<\infty\}\cup\{0\}\bigr). \tag{2}
\]
Equation (1) is a complete stage-by-stage description, not merely a bound on eventual stabilization.

**(3) Sharp maxima when the initial digraph is acyclic.** An acyclic graph with \(N\) arcs has no directed walk longer than \(N\). If \(e:u\to v\) has a predecessor walk of length \(a=h^-(u)\) and a successor walk of length \(b=h^+(v)\), concatenation through \(e\) gives a directed walk of length \(a+1+b\le N\). Hence
\[
 d(e)+1\le\left\lceil\frac{N}{2}\right\rceil.
\]
A directed path of exactly \(N\) arcs, with alternating bipartition classes, attains this bound: the middle arc(s) have \(d(e)+1=\lceil N/2\rceil\). Its incidence graph is simple, so this also works for proper frames. Every directed bipartite graph constructed here is realized by an S5 model by taking arcs as worlds and endpoints as equivalence-class labels.

**(4) Sharp maxima when a directed cycle exists.** Any directed cycle survives every peeling round, by (1), and every strict restriction round deletes at least one other arc. In a bipartite multigraph a directed cycle uses at least two distinct arcs, so \(r\le N-2\); if the underlying bipartite graph is simple, a directed cycle uses at least four arcs, giving \(r\le N-4\). Both bounds are attained where applicable: orient a directed two-cycle of antiparallel parallel arcs (ordinary case), or a directed four-cycle (proper case), and attach a directed path consisting of every remaining arc **outward** from one cycle vertex, using fresh vertices alternately on the opposite sides. The terminal path arc disappears at the first round and successive path arcs disappear one per later round; the cycle survives. For \(N=2\) or \(N=4\), the cycle itself is already stable, giving zero rounds, but the path construction from (3) attains the overall maximum. Taking the greater of the acyclic and cyclic bounds gives the two advertised formulas for each \(N\ge1\).

## Verification

The accompanying standard-library Python program `verify_ignorance.py` independently computes successive restrictions directly from equivalence-class color mixtures and, separately, the directed-walk survival criterion. It exhaustively compares them for every pair of partitions and Boolean valuation for \(1\le N\le5\), a deterministic stratified selection for \(N=6\), and explicit extremal constructions for \(1\le N\le40\). The exhaustive case counts are \(2,16,200,3600,86528\) for \(N=1,2,3,4,5\), respectively; the stratified six-world sample contains \(13888\) models. The maximum strict round counts seen through six worlds are \(1,1,2,2,3,4\) for arbitrary frames, and \(1,1,2,2,3,3\) for proper frames. Finite checks corroborate rather than replace the all-size proof.

## Relationship to prior work

Yamada (2026) studies repeated and transfinite announcement phenomena, especially **believed** announcement semantics and eventual success/refutation, but does not state the exact per-world time formula or the two sharp size laws for ordinary repeated announcement of both agents' ignorance. Fan, Wang and van Ditmarsch (2013) study knowing-whether modalities and public announcement, including iterated epistemic puzzles, but not this exact extremal question. Pittel and Poole (2014) identify and analyze the **directed \((1,1)\)-core** and randomized sequential deletions: the eventual surviving-core characterization and cycle/connecting-path interpretation are **not claimed as new**. What is quantified here is synchronous removal of individual worlds and the sharp epistemic finite-model convergence bounds, distinguishing proper and nonproper incidence relations. The simultaneous peeling framework and standard graph facts are acknowledged as antecedents.

## Limitations

The theorem needs exactly two S5 agents, one fixed unmodified Boolean atom, and repeated ordinary world-deleting restriction by the specified common-ignorance formula. It makes no claim about arbitrary announcement formulas, pointed truthfulness after the designated point disappears, more agents, believed arrow-deleting updates, or general dynamic-epistemic bisimulation classes. No assertion of priority over possible earlier results stated in the language of synchronous directed-core peeling is made; those are a residual literature-coverage risk. The proof applies to finite models. Independent historical-priority and mathematical audits have not been conducted.

## References

1. Eiji Yamada, *Eventual and Strong Eventual Notions in Public Announcements*, arXiv:2609.24006v1 (first posted 2026-09-21), https://arxiv.org/abs/2609.24006.
2. Jie Fan, Yanjing Wang, and Hans van Ditmarsch, *Knowing Whether*, arXiv:1312.0144v1 (first posted 2013-11-30), https://arxiv.org/abs/1312.0144.
3. Boris Pittel and Daniel Poole, *Asymptotic distribution of the numbers of vertices and arcs of the giant strong component in sparse random digraphs*, arXiv:1405.4022v1 (first posted 2014-05-15), https://arxiv.org/abs/1405.4022.
