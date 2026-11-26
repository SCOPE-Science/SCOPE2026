# Hamiltonian irreducibility and exponential rarity of length-two free-semigroup endomorphisms

## Finding
Let \(\Sigma\) be a labelled alphabet of \(n\ge2\) symbols. A 2-uniform endomorphism \(\varphi:\Sigma^+\to\Sigma^+\) sends every letter to a word of length exactly two. A rank-preserving endomorphism has no generating set for its images with fewer than \(n\) nonempty words; an irreducible rank-preserving endomorphism has no factorization into two nonautomorphic endomorphisms.

**Graph criterion.** Form a labelled multigraph \(G_\varphi\) whose \(n\) edges are the ordered two-letter images, with orientations forgotten but loops retained; opposite words give distinct parallel edges. The endomorphism is rank-preserving exactly when the images are distinct and \(G_\varphi\) is a disjoint union of unicyclic components. Among these, it is irreducible exactly when \(G_\varphi\) is a single spanning cycle without attached trees. For \(n=2\), a spanning cycle means the pair of opposite words.

Let \(A_n\) count all rank-preserving 2-uniform endomorphisms and \(B_n\) count irreducible ones, with domain letters and alphabet symbols labelled. Define \(T(z)\) as the unique formal solution \(T(z)=z\exp(2T(z))\). Then
\[
A_n=(n!)^2[z^n]\,\frac{\exp(-T(z)^2/2)}{\sqrt{1-2T(z)}}.
\]
For \(n=2\), \(B_2=2\); for every \(n\ge3\),
\[
B_n=2^{n-1}n!(n-1)!.
\]
In particular, the conditional proportion of irreducibles among rank-preserving 2-uniform endomorphisms obeys
\[
\frac{B_n}{A_n}\sim\frac{2^{-3/4}e^{1/8}\Gamma(1/4)}{n^{1/4}e^n}
\qquad(n\to\infty).
\]
The constant \(2^{-3/4}e^{1/8}\Gamma(1/4)\) is approximately \(2.44\). This is an exponential rarity theorem within the rank-preserving family, not within all endomorphisms.

## Assumptions and scope
Words are nonempty; generator images have length exactly two; all labels are distinguished. Irreducibility is understood **only for rank-preserving endomorphisms**, with the same intermediate alphabet and composition notion as in Bell–Foster–Reidenbach. A graph loop represents an image \(aa\); the two edges \(ab\) and \(ba\) are different but become a parallel pair on forgetting their orientations. A unicyclic connected multigraph has as many edges as vertices, counting loops and parallel edges. Only the two oppositely directed words can realize a length-two cycle on two vertices.

## Proof
**1. Basis-size lemma.** Write \(W=\{\varphi(a):a\in\Sigma\}\), initially as a set of distinct words when rank preservation is possible. Any factor basis \(V\) generating \(W\) can be stripped of unused elements. Every used element has length at most two. Let \(S=V\cap\Sigma\). A two-letter word in \(W\) can be represented as a concatenation of members of \(V\) either by its own length-two generator, or by its two individual letters, both in \(S\). Hence the least possible basis cardinality is
\[
\min_{S\subseteq\Sigma}\left(|S|+n-e(S)\right),
\quad e(S)=|\{uv\in W:u,v\in S\}|.
\]
Indeed the candidate consisting of all letters in \(S\) and the words of \(W\) not contained in \(SS\) always generates \(W\). Repeated images immediately violate rank preservation. With distinct images, rank preservation is therefore equivalent to \(e(S)\le|S|\) for every \(S\subseteq\Sigma\).

**2. Graph structure.** The inequalities \(e(S)\le|S|\) are the standard pseudoforest criterion: each connected component contains at most one cycle, allowing loops or a parallel-edge 2-cycle. Since there are globally exactly \(n\) edges on \(n\) vertices, every component has exactly one cycle. Thus the rank-preserving image sets correspond bijectively to labelled oriented unicyclic pseudoforests subject to the convention that opposite orientations of a pair form two distinct edges.

**3. Reducibility.** By Theorem 1 of Bell–Foster–Reidenbach, a rank-preserving endomorphism is reducible precisely when \(W\) has a nontrivial factor basis of cardinality \(n\). In the length-two case any such basis has the canonical form \(V_S=S\cup\{uv\in W:(u,v)\notin S\times S\}\) for some \(S\). It has size \(n\) exactly when \(e(S)=|S|\). The cases \(S=\varnothing\) and \(S=\Sigma\) are the two trivial bases, and a nonempty proper \(S\) with equality yields a nontrivial basis (every member is used because the original system is rank preserving). Conversely, any nontrivial basis forces such a proper \(S\). If \(e(S)=|S|\) for a nonempty proper \(S\), every connected component of the induced graph on \(S\) is unicyclic, so \(S\) contains a cycle. Conversely, whenever a cycle does not span all vertices of the full graph, choosing \(S\) to consist precisely of the vertices on that cycle gives \(e(S)=|S|\). Thus such a subset exists unless the only component is a spanning simple cycle, with the parallel-edge cycle allowed at order two. This proves the graph criterion.

**4. Irreducible count.** For \(n\ge3\), the number of undirected Hamiltonian cycles on \(n\) labelled vertices is \((n-1)!/2\). Independently orienting each of the \(n\) edges produces \(2^n\) permitted ordered word sets. Assigning those distinct words bijectively to the \(n\) source generators introduces a factor \(n!\). Therefore \(B_n=2^{n-1}n!(n-1)!\). For \(n=2\), there is only the word set \(\{ab,ba\}\), and its two source assignments give \(B_2=2\).

**5. All rank-preserving endomorphisms.** The exponential generating function for a rooted labelled tree with each away-from-root edge admitting two possible word orientations is \(T=z\exp(2T)\). A connected unicyclic component consists of a cycle with independent such trees attached. The cycle may be (i) one loop, contributing \(T\); (ii) two opposite word-edges, contributing \(T^2/2\); or (iii) a simple cycle of length \(k\ge3\), contributing \(2^{k-1}T^k/k\). Thus its connected-component EGF is
\[
C(z)=T+\frac{T^2}{2}+\sum_{k\ge3}\frac{2^{k-1}T^k}{k}
=-\frac12\log(1-2T)-\frac{T^2}{2}.
\]
The labelled exponential formula gives \(P(z)=\exp C(z)=\exp(-T^2/2)/\sqrt{1-2T}\). Each edge set can be assigned to the ordered source generators in \(n!\) ways, whence \(A_n=(n!)^2[z^n]P(z)\).

**6. Asymptotics.** The inverse equation \(z=T\exp(-2T)\) has its first positive critical point at \(T=1/2\), \(\rho=1/(2e)\), and
\[
1-2T(z)\sim\sqrt{2(1-z/\rho)}.
\]
Consequently \(P(z)\sim 2^{-1/4}e^{-1/8}(1-z/\rho)^{-1/4}\). Standard singularity transfer gives
\[
[z^n]P(z)\sim
\frac{2^{-1/4}e^{-1/8}}{\Gamma(1/4)}(2e)^n n^{-3/4}.
\]
Dividing the exact \(B_n\) by \(A_n\) gives the displayed ratio. The nonnegative aperiodic combinatorial series excludes competing dominant singularities.

## Verification
Run \(\texttt{python3 verify.py}\) with Python 3. The program independently enumerates all allowed length-two image tuples on two and three generators, exhaustively constructs all possible nonautomorphic factor pairs whose compositions can have length two, and compares the result with the graph criterion. For four and five generators it exhaustively enumerates distinct sets of length-two images and checks the induced-subgraph inequalities and cycle criterion. It independently computes unicyclic-component counts by the labelled rooted-forest formula and checks the first seven coefficients of the EGF through the combinatorial recurrence.

Direct factor tests: \(A_2=12\), \(B_2=2\); \(A_3=432\), \(B_3=48\). Distinct rank-preserving image sets: \(1274\) at \(n=4\) with \(48\) irreducible sets, and \(29610\) at \(n=5\) with \(384\) irreducible sets. The coefficient counts for \(n=2,3,4,5,6,7,8\) are \(6,72,1274,29610,850692,29086624,1153013052\). These finite checks do not establish the arbitrary-alphabet theorem; the proof above does.

## Relationship to prior work
Bell, Foster and Reidenbach introduce rank-preserving endomorphisms and prove the general factor-basis criterion for irreducibility (their Theorem 1). Their full 2026 manuscript additionally studies factorization ambiguity and incidence matrices, and gives smaller examples, including the binary opposite-word example. The present result applies their criterion to an entire new, length-two subclass and proves the **graph equivalence, all-size exact enumeration, and sharp conditional rarity law**. It does not claim to originate the factor-basis criterion or the classical rooted-tree/labelled-exponential formulas. The count uses word order, so incidence matrices alone do not provide this census.

## Limitations
This result concerns words of length exactly two and does not classify morphisms of lengths three or higher. It counts labelled generators, not isomorphism classes modulo alphabet permutation. The asymptotic is conditional on rank preservation and does not describe every random 2-uniform endomorphism. Known general factor-basis results subsume the decision problem in principle, although they do not state the closed-form enumerative consequences. Older elementary-morphism or oriented-graph literature may contain an equivalent counting statement; a targeted search and inspection of the closest full primary text found none, but exhaustive bibliographic novelty is not proved. No external independent mathematical audit has been performed.

## References
1. P. C. Bell, E. Foster, D. Reidenbach, *Irreducibility of Endomorphisms of Finitely Generated Free Semigroups*, first made public March 16, 2026, arXiv:2603.15177. Full text (version 3): https://arxiv.org/html/2603.15177v3 ; public-date record: https://arxiv.org/abs/2603.15177 .
2. P. C. Bell, E. Foster, D. Reidenbach, *Irreducibility of Endomorphisms of Finitely Generated Free Semigroups*, proceedings version, arXiv:2610.07122v1, https://arxiv.org/html/2610.07122v1 .
3. The rooted-forest enumeration and the labelled exponential formula are standard consequences of Cayley's tree formula and the labelled combinatorial-species construction; singularity transfer is used in its standard analytic-combinatorics form.
