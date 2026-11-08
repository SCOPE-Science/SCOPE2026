# Four quantifier-rank-three theories of finite Grassmann adjacency graphs

## Finding
Let \(q\) be any prime power, \(n\geq1\), and \(1\leq k\leq n\). The finite Grassmann adjacency graph \(\operatorname{PGJ}(n,k,q)\) has the \(k\)-dimensional subspaces of \(\mathbb F_q^n\) as vertices, with two distinct vertices adjacent exactly when their intersection has dimension \(k-1\). All such graphs, considered in the pure graph language, realize exactly **four** elementary-equivalence classes at quantifier rank at most three:

1. \(k=n\): the singleton class.
2. \(\min(k,n-k)=1\): the finite complete-graph class (all orders at least three).
3. \(\min(k,n-k)=2\): the two-point-extension class, whose members are rank-three equivalent to the countable Rado graph.
4. \(\min(k,n-k)\geq3\): the diameter-at-least-three class, different from the previous three.

For distinct vertices \(U,V\), let \(d=k-\dim(U\cap V)\). If \(\min(k,n-k)\geq2\), then the **complete adjacency-extension profile** for a third distinct vertex \(Z\), with \((a,b)=(\mathbf 1_{Z\sim U},\mathbf 1_{Z\sim V})\), is
\[
\mathcal E(U,V)=\begin{cases}
\{(0,0),(0,1),(1,0),(1,1)\},&d=1\text{ or }2,\\
\{(0,0),(0,1),(1,0)\},&d\geq3.
\end{cases}
\]
In particular, the **sharp** Rado rank-three threshold is \(\min(k,n-k)=2\). The smallest Grassmann representatives of the extension and generic classes have, respectively, \(35\) and \(1395\) vertices: \(\operatorname{PGJ}(4,2,2)\) and \(\operatorname{PGJ}(6,3,2)\). These minima apply within the Grassmann family only.

## Assumptions and scope
Here \(q\) ranges over prime powers \(\geq2\), and all subspaces are linear, not affine. The graph is finite, simple, and undirected. The graph language has equality and one irreflexive adjacency relation, with no named field elements, dimensions, or parameters. Rank-three equivalence means agreement on all **first-order sentences** of quantifier rank at most three; it does not mean isomorphism or full elementary equivalence. The countable Rado graph is invoked only for this bounded-rank comparison. The first public motivating source appeared on 2026-10-29 UTC.

## Proof
**1. Duality and distance.** Choose a nondegenerate bilinear pairing on \(\mathbb F_q^n\). Orthogonal complement induces a graph isomorphism between \(\operatorname{PGJ}(n,k,q)\) and \(\operatorname{PGJ}(n,n-k,q)\), because \(\dim(U^\perp\cap V^\perp)=n-2k+\dim(U\cap V)\). We may assume \(k\leq n/2\). The graph distance of \(U,V\) is \(d=k-\dim(U\cap V)\). The lower bound follows because one adjacency step changes the intersection dimension by at most one; the upper bound follows by successively replacing a basis vector of a complement of \(U\cap V\) in \(U\) with a corresponding vector from \(V\). All distances \(1,\ldots,k\) occur.

**2. A common-complement lemma.** Let \(I=U\cap V\) have dimension \(t\) and write \(U=I\oplus A\), \(V=I\oplus B\), with \(\dim A=\dim B=k-t\) and \(A\cap B=0\). Let \(H\) be any \(t\)-dimensional subspace disjoint from \(U+V\) (possible because \(n\geq2k\)). Choose bases \(a_i\) of \(A\) and \(b_i\) of \(B\). Then
\[
Z=H\oplus\operatorname{span}\{a_i+b_i:1\leq i\leq k-t\}
\]
has dimension \(k\) and is disjoint from both \(U\) and \(V\). When \(k\geq2\), it is nonadjacent to each, giving extension pattern \((0,0)\).

**3. Adjacent and distance-two pairs.** If \(d=1\), put \(I=U\cap V\) of dimension \(k-1\). There are at least three \(k\)-subspaces through \(I\), so some third one \(Z\) meets both in dimension \(k-1\), giving \((1,1)\). For \((1,0)\), choose a hyperplane \(H<U\) different from \(I\), and choose a vector \(x\notin U+V\), possible because \(\dim(U+V)=k+1<n\). Then \(Z=H\oplus\langle x\rangle\) meets \(U\) in dimension \(k-1\) and \(V\) in dimension \(k-2\). Reversing \(U,V\) gives \((0,1)\).

If \(d=2\), let \(I=U\cap V\) have dimension \(k-2\). Choose independent \(u,u'\) in a complement of \(I\) in \(U\) and independent \(v,v'\) in a complement in \(V\). Then \(Z=I\oplus\langle u,v\rangle\) meets each in dimension \(k-1\), giving \((1,1)\). For \((1,0)\) when \(k\geq3\), take a hyperplane \(H<U\) containing \(I\), then take \(x\notin U+V\) (possible since \(\dim(U+V)=k+2<2k\leq n\)); \(Z=H\oplus\langle x\rangle\) meets \(V\) in dimension \(k-2\). When \(k=2\), \(U\cap V=0\), and \(Z=\langle u,u'+v\rangle\) instead meets \(U\) in dimension one and \(V\) trivially, including the boundary \(n=4\). Swapping the two vertices gives \((0,1)\).

**4. Pairs farther apart.** For \(d\geq3\), a common adjacent neighbor cannot exist, by the graph-distance triangle inequality. The lemma from step 2 supplies \((0,0)\), and choosing any neighbor of either endpoint supplies \((1,0)\) and \((0,1)\). These and steps 2–3 prove all profiles for all prime powers, not merely for tested fields.

**5. Exactly four rank-three theories.** The symmetric group of subspace-coordinate changes acts transitively on vertices and on ordered pairs at any fixed distance. In a three-round Ehrenfeucht–Fraïssé game between two graphs from the same proposed class, Duplicator first matches any vertex. At round two she matches equality or the distance category \(d=1\), \(d=2\), or \(d\geq3\), as needed; each available category occurs in both structures. Round three is won by matching equality or the requested \((a,b)\) extension profile, which agrees by steps 2–4. Thus same-class graphs satisfy precisely the same rank-three sentences. Singletons and complete graphs are elementary easy cases. For \(k=2\), every pair admits all four patterns, giving the two-point extension property of rank three, also possessed by the Rado graph. Conversely, when \(k\geq3\), distance-three pairs exist and have no common neighbor, so the rank-three sentence
\[
\forall x\,\forall y\,\bigl(x\ne y\to\exists z\,(z\ne x\wedge z\ne y\wedge E(x,z)\wedge E(y,z))\bigr)
\]
is true at diameter two but false at larger diameter. The singleton class is separated by existence of two distinct vertices, and the complete class is separated from the others by existence of nonadjacent vertices. Thus all four classes differ.

**6. Sharp representative sizes.** For prime power \(q\), the order of \(\operatorname{PGJ}(n,k,q)\) is the Gaussian binomial coefficient \(\begin{bmatrix}n\\k\end{bmatrix}_q\). Its interpretation as a subspace count makes it nondecreasing in \(n\); the standard recurrence and positive-coefficient polynomial expression make it increasing in \(q\geq2\). Complement symmetry and unimodality in \(k\) give the smallest diameter-two case at \((n,k,q)=(4,2,2)\), with \(35\) vertices. For diameter at least three the minimum ambient dimension is six and the minimum dimension pair is \((6,3)\), whose binary subspace count is \(1395\). This proves the claimed minima.

## Verification
Run `python checker.py` with standard Python 3. It constructs every reduced-row-echelon \(k\)-subspace over \(\mathbb F_2\) and \(\mathbb F_3\) in the listed cases, checks Gaussian-binomial vertex totals, builds adjacency directly from intersection dimensions, and exhaustively checks all ordered pair-extension masks. It includes the complete and diameter-three boundaries. Expected concluding line: `GRASSMANN_RANK_THREE_CHECKS_OK`. The finite checker does **not** certify the theorem for arbitrary prime powers: the linear-algebraic argument above supplies that proof.

## Relationship to prior work
Benediktsson–Macpherson–Adler (2026), Section 6, explicitly proposes first-order investigation of finite-field Grassmann adjacency graphs \(\operatorname{PGJ}\), but their theorems concern set-based Johnson graphs and their infinite limit theory, not this rank-three Grassmann classification. Gavrilyuk–Koolen (2018), especially Sections 1–2, develops the classical finite Grassmann scheme and its intersection numbers; those numerical intersection parameters underpin local graph geometry but the paper studies distance-regular characterization, not a four-class rank-three model-theoretic classification. Existing finite Grassmann diameter and graph-endomorphism literature concerns different invariants. Exact rank-three logical equivalence and smallest representatives are the contribution claimed here, **not** the basic Grassmann distance or intersection formulas.

## Limitations
This result is only about quantifier rank at most three, the pure graph language, finite fields, and the full Grassmann adjacency graph family. It does not determine higher-rank theories, model-theoretic limit completeness, or stability. The finite calculation handles only two small prime fields, not extension fields. Historical priority risk remains: a general theorem translating distance-regular intersection arrays into bounded-rank elementary equivalence could subsume the result, and older specialized mathematical-logic literature may not have been located. No independent mathematical audit has been performed.

## References
- B. G. Benediktsson, D. Macpherson, I. Adler, *Model theory of Johnson Graphs*, arXiv:2610.40054v1 (first public 2026-10-29), Section 6, https://arxiv.org/html/2610.40054v1.
- A. L. Gavrilyuk, J. H. Koolen, *On a characterization of the Grassmann graphs*, arXiv:1806.02652v1 (2018), especially Sections 1–2, https://arxiv.org/html/1806.02652v1.
- L.-P. Huang, B. Lv, K. Wang, *The endomorphism of Grassmann graphs*, arXiv:1404.7578 (2014), https://arxiv.org/abs/1404.7578.
- A. Ehrenfeucht, *An application of games to the completeness problem for formalized theories*, Fundamenta Mathematicae 49 (1961), 129–141.
