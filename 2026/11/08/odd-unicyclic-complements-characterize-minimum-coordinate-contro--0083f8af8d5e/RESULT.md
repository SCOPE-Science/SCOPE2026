# Odd-unicyclic complements characterize minimum coordinate control of two-subset Kneser graphs

## Finding

**Theorem.** For every integer \(n\ge 5\), let \(G=KG(n,2)\) be the graph on the \(N=\binom n2\) unordered pairs of \([n]\), where two pairs are adjacent exactly when disjoint. Let \(L\) be its unweighted combinatorial Laplacian. For any \(S\subseteq V(G)\), let \(B_S\) have the distinct standard-coordinate columns indexed by \(S\). The real continuous-time system
\[
\dot z=-Lz+B_Su
\]
can be controlled with as few as \(N-n\) independently actuated pair-vertices, and never with fewer.

For \(|S|=N-n\), regard the unactuated complement \(U=V(G)\setminus S\), consisting of \(n\) unordered pairs, as the edges of a simple graph \(H_U\) on the ground set \([n]\). Then \((-L,B_S)\) is controllable **if and only if** each connected component of \(H_U\) has exactly one cycle and that cycle has odd length, **except** that when \(n=6\), the graph \(H_U=K_3\sqcup K_3\) is not controllable.

Thus the number of labeled minimum-cardinality controlling sets is
\[
\boxed{\mathcal A_n=n!\,[z^n]\exp\!\left(\frac{\operatorname{arctanh}T(z)-T(z)}2\right)-10\mathbf 1_{\{n=6\}}},
\qquad T(z)=z\exp(T(z)),\quad T(0)=0.
\]
For \(n=5,6,7,8,9\), these counts are respectively \(162,2520,45615,937440,21685132\). In particular, the Petersen graph requires five independent coordinate inputs, and has exactly \(162\) optimal five-vertex input sets. A constructive optimal placement in every dimension is obtained by leaving unactuated the edges of a triangle with a path on the other \(n-3\) vertices attached to one triangle vertex.

## Assumptions and scope

All graphs are finite, simple, unweighted and undirected. Each actuated pair-vertex receives one *independent* scalar control; sharing an input across several vertices is not covered. Controllability refers to the full state space over \(\mathbb R\) of the *fixed* Laplacian system, not to a family of arbitrary edge-weighted matrices. The parameter is every integer \(n\ge5\), and the characterization is only for sets of minimum cardinality \(N-n\). The formal series defining \(T\) is uniquely determined coefficient by coefficient, so the enumeration does not depend on choices of analytic branches.

## Proof

**1. The relevant orthogonal eigenspaces.** Write \(B\) for the unsigned \(n\times N\) vertex-edge incidence matrix of the complete graph on \([n]\), so its column indexed by \(\{i,j\}\) has ones at rows \(i,j\). Then
\[
BB^{\mathsf T}=(n-2)I_n+J_n,
\qquad
A_G=J_N+I_N-B^{\mathsf T}B.
\]
The second identity holds at diagonal positions as well as the off-diagonal positions, since two distinct pairs have disjointness indicator \(1-\#\text{(common endpoints)}\). The graph \(G\) is regular of degree \(k=\binom{n-2}{2}\). Because \(BB^{\mathsf T}\) is positive definite for \(n\ge5\), \(B\) has row rank \(n\), and \(\ker B\) has dimension \(N-n\). Direct application of \(A_G\) gives the pairwise orthogonal Laplacian eigenspaces
\[
E_0=\operatorname{span}\{\mathbf1_N\}\ (0),\qquad
E_1=\ker B\ \bigl(\tfrac{(n-1)(n-4)}2\bigr),\qquad
E_2=\{B^{\mathsf T}x:\mathbf1_n^{\mathsf T}x=0\}\ \bigl(\tfrac{n(n-3)}2\bigr).
\]
Numbers in parentheses are Laplacian eigenvalues. They are distinct for all \(n\ge5\), and the eigenspaces have dimensions \(1,N-n,n-1\), totaling \(N\). Therefore these are all eigenspaces.

**2. The lower bound and first exact condition.** The Popov–Belevitch–Hautus test for a real symmetric matrix says the pair is controllable if and only if no nonzero Laplacian eigenvector vanishes on every coordinate of \(S\). As \(\dim E_1=N-n\), every controlling set has at least \(N-n\) members. If equality holds, then \(U\) has exactly \(n\) edges and an eigenvector in \(\ker B\) vanishes on \(S\) precisely when a nonzero vector in \(\ker B_U\) exists, where \(B_U\) is the square unsigned incidence submatrix indexed by \(U\). Consequently the \(E_1\) requirement is \(\det B_U\ne0\).

We recall and prove the elementary unsigned-incidence criterion. In a connected component with \(v\) vertices and \(e\) edges, the row nullspace of the unsigned incidence matrix consists of assignments \(x_i+x_j=0\) along every edge: it is one-dimensional if the component is bipartite, and zero if the component contains an odd cycle. Thus the unsigned incidence rank is \(v-1\) for a bipartite component and \(v\) otherwise. Because \(\sum e=\sum v=n\), invertibility of the overall \(n\times n\) matrix requires every component to have exactly \(e=v\) and full row rank; equivalently every component is unicyclic with an odd unique cycle. Conversely those conditions give square full-rank blocks. This is a standard signless-incidence fact, not an independently claimed new incidence theorem.

**3. The second eigenspace and the exceptional case.** As \(B^{\mathsf T}\) is injective, an \(E_2\) eigenvector vanishing on \(S\) corresponds exactly to an \(x\in\mathbb R^n\) satisfying
\[
\mathbf1_n^{\mathsf T}x=0,\qquad x_i+x_j=0\quad\text{for all }\{i,j\}\in S.
\]
Let \(H_S=([n],S)\). On a connected nonbipartite component of \(H_S\), these equations force every \(x_i=0\); on a connected bipartite component they allow opposite constant signs on the bipartition.

Since \(|S|=N-n=n(n-3)/2\), a disconnected \(H_S\) cannot have a component of size between \(2\) and \(n-2\): the crossing pairs alone would give \(|U|\ge2(n-2)>n\). Two or more isolated vertices similarly force more than \(n\) missing pairs. Hence the sole disconnected possibility is one isolated vertex and the other \(n-1\) vertices spanning \(K_{n-1}\) with exactly one edge deleted. That large component is connected and contains a triangle for \(n\ge5\), so the edge equations force \(x=0\) there; the zero-sum condition forces its isolated coordinate to zero too. Thus the \(E_2\) requirement always holds in the disconnected case.

For connected \(H_S\), a nonzero solution is possible only if it is bipartite with two equal-size color classes. When \(n\) is odd this is impossible. For even \(n\ge8\), bipartiteness is impossible because the edge count \(n(n-3)/2\) strictly exceeds the complete-bipartite maximum \(n^2/4\). The remaining even case is \(n=6\). Equality holds in the bipartite edge bound: a connected bipartite \(H_S\) can have nine edges and equal classes only when \(H_S=K_{3,3}\). Its complement consists of two disjoint triangles, exactly the stated exception. Conversely those two triangles make \(E_1\) admissible but the balanced sign vector annihilates all controlled \(E_2\) coordinates, so controllability fails. There are \(\binom63/2=10\) such complements. This proves the if-and-only-if classification.

**4. Achievability and enumeration.** A triangle with a tree path attached to one vertex has \(n\) edges on \(n\) ground vertices and one odd cycle; it is connected, and so is not the excluded \(K_3\sqcup K_3\). Its complement achieves the lower bound for every \(n\ge5\).

For the count, the rooted labeled-tree exponential generating series obeys \(T=ze^T\). A connected odd-unicyclic graph is an *unoriented* cycle of odd length \(j\ge3\) with an independent rooted tree attached to each cycle vertex, giving EGF
\[
C(z)=\sum_{\substack{j\ge3\\ j\ \mathrm{odd}}}\frac{T(z)^j}{2j}
=\frac{\operatorname{arctanh}T(z)-T(z)}2.
\]
The class of sets of such components has EGF \(\exp C(z)\). Choosing their labeled edge sets is the same as choosing an unactuated \(U\); subtract the ten balanced-triangle exceptions at \(n=6\). The displayed formula follows.

## Verification

The accompanying `verify_kneser.py` uses only Python's standard library and exact rational elimination. Run `python3 verify_kneser.py` from the extracted package. It checks incidence/adjacency spectral identities for \(5\le n\le8\), all \(252\) candidate unactuated sets for \(n=5\), all \(5005\) candidates for \(n=6\), and a fixed reproducible sample of \(1000\) candidate sets for \(n=7\), comparing direct PBH ranks against the graph criterion. It also independently counts the \(116280\) seven-edge subsets of \(K_7\) by the structural condition, and computes the rational formal-series coefficients through \(n=9\). The output ends with `VERIFY_OK`. The finite verification is supplemental; the proof above covers all \(n\ge5\).

## Relationship to prior work

Monshizadeh–Zhang–Camlibel (2014) establish zero-forcing characterizations for controllability throughout a qualitative matrix class, which uses a stronger, different quantifier than controllability of the single fixed unweighted Laplacian. Brešar–Kos–Torres (2019) determine the zero-forcing number of \(KG(n,2)\) as \(N-6\) for \(n\ge7\), while the fixed-Laplacian minimum here is \(N-n\), strictly less for \(n\ge7\); hence that zero-forcing theorem does not imply this optimum or placement classification. Ducey–Hill–Sin (2017) analyze the Kneser Laplacian spectrum and critical group but do not give the PBH placement classification. Hessert–Mallik (2022) recall the classical odd-unicyclic incidence invertibility criterion, which serves here only as one step in the new control equivalence. General graph-distance leader lower bounds and general perfect-critical-set methods do not specify the exact Kneser minimum-set correspondence or the six-vertex exception.

## Limitations

The result concerns the exact fixed, unweighted \(KG(n,2)\) Laplacian and independent coordinate controls. It does not classify larger controlling sets, weighted Kneser graphs, a single broadcast input, robustness to uncertain weights, or time- and energy-optimal control. The computations cannot alone prove the statement for all \(n\). Unindexed prior exact Kneser leader-placement results could affect publication priority; no independent mathematical audit is represented here.

## References

- N. Monshizadeh, S. Zhang, M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs* (2014), arXiv:1403.4868v1, first posted 2014-03-19. https://arxiv.org/pdf/1403.4868
- A. Y. Yazicioglu, W. Abbas, M. Egerstedt, *Graph Distances and Controllability of Networks* (2016), arXiv:1608.04309. https://arxiv.org/abs/1608.04309
- J. E. Ducey, D. Hill, P. Sin, *The critical group of the Kneser graph on 2-subsets of an n-element set* (2017), arXiv:1707.09115. https://arxiv.org/pdf/1707.09115
- B. Brešar, T. Kos, P. D. Torres, *Grundy domination and zero forcing in Kneser graphs*, Ars Math. Contemp. 17 (2019), 419–430. https://doi.org/10.26493/1855-3974.1881.384
- R. Hessert, S. Mallik, *The Inverse of the Incidence Matrix of a Unicyclic Graph* (2022), arXiv:2201.02580v1. https://arxiv.org/pdf/2201.02580
- L. Dai, *Minimum leader selection for controllability of undirected graphs with leader–follower framework* (2023). https://doi.org/10.1049/cth2.12385
