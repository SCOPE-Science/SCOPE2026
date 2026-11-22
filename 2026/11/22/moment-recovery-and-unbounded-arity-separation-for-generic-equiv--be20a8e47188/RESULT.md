# Moment recovery and unbounded arity separation for generic equivalence-constrained graphs

## Finding
Let \(\mathcal G\) be the countable homogeneous limit of finite structures \((V,E,R)\), where \(E\) is an equivalence relation and \(R\) is a symmetric irreflexive graph relation satisfying \(R(u,v)\Rightarrow\neg E(u,v)\). For a finite individually named base \(A\) of \(n\ge1\) points, write its \(E\)-class sizes as \(a_1,\ldots,a_s\). Let \(t_r(A)\) be the number of complete first-order types of ordered \(r\)-tuples of pairwise distinct new elements over \(A\), with \(t_0(A)=1\). Define \(S_j(A)=\sum_{i=1}^s2^{-j a_i}\) for \(j\ge1\).

**Theorem (exact numerical reconstruction and an unbounded finite-arity hierarchy).** For each \(r\ge1\) there is a universal polynomial \(F_r\in\mathbb Z[S_1,\ldots,S_r]\), of weighted degree at most \(r\) when \(S_j\) has weight \(j\), such that
\[
\boxed{t_r(A)=2^{nr}F_r(S_1(A),\ldots,S_r(A)).}
\]
Its coefficient of the monomial \(S_r\) is the nonzero odd integer
\[
\boxed{c_r=\sum_{\pi\in\Pi_r}(-1)^{|\pi|-1}(|\pi|-1)!\,2^{\sum_{B<C\in\pi}|B||C|}\equiv1\pmod2.}
\]
Thus for bases of **equal known cardinality** \(n\), equality of the first \(k\) numerical counts is equivalent to equality of the first \(k\) moments \(S_1,\ldots,S_k\). The first \(n\) counts determine the entire unordered class-size multiset \(\{a_1,\ldots,a_s\}\), hence determine every later count. Conversely, two such bases have identical complete spectra if and only if their class-size multisets agree. The spectrum deliberately does **not** reconstruct the old graph-edge pattern \(R\) on the base.

No absolute arity cutoff works uniformly across base sizes. For every integer \(k\ge1\) there exist two distinct class-size multisets of the same total size, whose first \(k\) counts agree and whose count at arity \(k+1\) differs. An explicit witness is given by separating positive and negative coefficients of
\[
\boxed{P_k(z)=z(1-z)^2\prod_{j=1}^{k}(2^jz-1).}
\]
The coefficient of \(z^a\) specifies a signed multiplicity of old \(E\)-classes of size \(a\).

The first numerical **one-point** collision between *different class-size multisets* occurs at twelve parameters. It is unique at that size, between \((5,5,1,1)\) and \((4,2,2,2,2)\); both give \(t_1=8448\), but their two-point counts are respectively \(151093248\) and \(155254784\). The finite minimality and uniqueness statement is supported by a complete enumeration of integer partitions of sizes one through twelve, not by any assertion of uniqueness at larger sizes.

## Assumptions and scope
The finite language contains equality, a named binary equivalence predicate \(E\), and a named symmetric irreflexive edge predicate \(R\). The only mixed constraint is that edges connect different equivalence classes. There is no assumption that the old-base graph is complete multipartite: its cross-class edges may be arbitrarily present or absent. Bases are pointwise named and compared only at the same size \(n\). Tuple coordinates are all distinct and are distinct from every named parameter. Logical types are complete types in the countable homogeneous structure, not arbitrary syntactic choices in an unrelated theory. All exponents, probabilities, and polynomial evaluations are exact; no generic randomness on infinite vertices is being sampled.

The age has hereditary and joint-embedding properties. To amalgamate finite structures over a common induced substructure, take the transitive closure of their two equivalence relations on the disjoint union without identifying new points, and put no cross-amalgam graph edges. This is consistent with the side restrictions and gives strong amalgamation. Hence its Fraïssé limit \(\mathcal G\) exists. Since the language is finite relational and the limit is ultrahomogeneous, complete types of finite tuples are precisely realizable atomic diagrams. In particular, the exact counts below require no extra existential conditions.

## Proof
**1. Exact block expansion.** Fix a set partition \(\pi\) of the new coordinate labels \([r]\); its blocks are the new \(E\)-classes. A subset \(D\subseteq\pi\) is designated to join distinct old \(E\)-classes. Every block outside \(D\) creates a distinct new class; the restriction of a block in \(D\) to an old class is encoded by an injection \(f:D\hookrightarrow[s]\). The number of free \(R\)-choices for the old/new edges is
\[2^{rn-\sum_{B\in D}|B|a_{f(B)}},\]
whereas free edges between new coordinates belonging to different blocks contribute the factor
\[2^{q(\pi)},\qquad q(\pi)=\sum_{B<C\in\pi}|B||C|.\]
Edges inside an \(E\)-block are forced absent. Here \(B<C\) simply denotes one choice of each unordered pair of distinct blocks, without imposing any meaningful order on the blocks. Therefore the exact finite sum is
\[
\boxed{2^{-nr}t_r(A)=\sum_{\pi\in\Pi_r}2^{q(\pi)}\sum_{D\subseteq\pi}\sum_{f:D\hookrightarrow[s]}\prod_{B\in D}(2^{-a_{f(B)}})^{|B|}.}\tag{1}
\]
Every admissible atomic diagram is represented once, and every represented diagram is realizable by homogeneity. The old \(R\)-edges never occur in this sum.

**2. Polynomial and odd diagonal.** Put \(x_i=2^{-a_i}\). For a collection of block sizes \(d_1,\ldots,d_b\), the injection sum \(\sum_{i_1,\ldots,i_b\text{ distinct}}x_{i_1}^{d_1}\cdots x_{i_b}^{d_b}\) is, by Möbius inversion on the partition lattice of \([b]\), an integer polynomial in the power sums \(S_j=\sum_i x_i^j\). More explicitly it equals
\[
\sum_{\sigma\in\Pi_b}\prod_{C\in\sigma}\bigl((-1)^{|C|-1}(|C|-1)!\,S_{\sum_{j\in C}d_j}\bigr).
\]
This proves (1) is the asserted integer polynomial of weighted degree at most \(r\). A monomial \(S_r\) can arise only when every new block joins an old class and all these old-class labels are identified in the Möbius inversion. For a partition \(\pi\) with \(b\) blocks, its contribution to that coefficient is \((-1)^{b-1}(b-1)!2^{q(\pi)}\). If \(b=1\), the contribution is one; if \(b\ge2\), then \(q(\pi)\ge1\), so the contribution is even. Hence the coefficient \(c_r\) is odd and nonzero. All other terms of \(F_r\) use only \(S_1,\ldots,S_{r-1}\) or products of them. For illustration,
\[
\begin{aligned}
2^{-n}t_1&=1+S_1,\\
2^{-2n}t_2&=3+4S_1+2S_1^2-S_2,\\
2^{-3n}t_3&=21+36S_1+24S_1^2+8S_1^3-12S_2-12S_1S_2+5S_3.
\end{aligned}
\]
For equal \(n\), induction on \(r\) yields equivalence of equality of the first \(k\) type counts and equality of \(S_1,\ldots,S_k\).

**3. Complete reconstruction from at most \(n\) arities.** There are at most \(n\) positive numbers \(x_i\). Pad their multiset with zeros to length \(n\). Newton's identities reconstruct the elementary symmetric functions of the padded \(n\)-tuple from its first \(n\) power sums. The resulting monic polynomial of degree \(n\) has roots equal to that multiset. Its positive roots are exactly the \(x_i=2^{-a_i}\), so the class sizes and their multiplicities are uniquely recovered. The converse, identical class-size multisets imply identical spectra, is immediate from (1).

**4. No fixed arity cutoff.** Write \(P_k(z)=\sum_{a\ge1}d_a z^a\), whose coefficients are integers and not all zero. Form one partition with \(\max(d_a,0)\) parts of size \(a\), the other with \(\max(-d_a,0)\) such parts. As \(P_k'(1)=0\), their total sizes coincide. Both are nonempty because \(P_k(1)=0\), \(P_k\not\equiv0\), and all coefficients with nonzero exponent have mixed signs. For each \(1\le j\le k\),
\[
S_j(A_k)-S_j(B_k)=\sum_a d_a2^{-ja}=P_k(2^{-j})=0.
\]
But \(P_k(2^{-(k+1)})\ne0\), so their next moments differ; the odd nonzero coefficient \(c_{k+1}\) and Step 2 imply that \(t_{k+1}\) differs. This proves the unbounded strict arity hierarchy with explicitly constructed equal-size witnesses.

**5. First one-point collision in class-size data.** Step 2 gives \(t_1=2^n(1+S_1)\). All integer partitions of \(n\le12\) are generated without omissions by selecting each largest part \(a\) in descending order and recursing on \(n-a\) with parts at most \(a\). Exact rational comparison finds no two distinct profiles with equal \(S_1\) through \(n=11\), and precisely the displayed pair at \(n=12\). For that pair, \(S_1=17/16\) in both cases, while \(S_2\) differs by \(127/512\). Substitution into the two-point identity yields the stated exact counts. The attached independent enumerator records all tested partition counts and checks the two first-type values.

## Verification
Run `python3 verify.py` using only the Python standard library. It compares two independently implemented counts: direct enumeration of set partitions on the entire old-plus-new vertex set, with the old equivalence relation constrained and all legal edge bits counted; and the separate weighted new-block injection formula (1). It checks every integer-partition base through four vertices at arities one through three (36 comparisons). It separately calculates the Möbius coefficient and its parity through arity seven, the polynomial collision witnesses for the first five arity thresholds, and every integer partition through twelve vertices for the first one-point collision. `check_output.txt` stores the exact program output, ending `ALL_CHECKS_PASS`. Only the twelve-vertex minimality claim uses exhaustive finite enumeration; all general claims follow from the displayed proofs.

## Relationship to prior work
Cameron's *Oligomorphic Permutation Groups* (1990) and *Sequences Realized by Oligomorphic Permutation Groups* (2000) establish the established connection of tuple orbits with types and the general language of orbit-counting sequences. The second source explicitly discusses Stirling transforms for unrestricted tuples, which are different from our injective, finite-base marked spectra. Conant's *An axiomatic approach to free amalgamation* (initial arXiv 2015) studies general homogeneity and independence phenomena, not the present constrained equivalence/graph model or the moment-reconstruction claim. Our age is not literally closed under plain disjoint-union amalgamation in the full language because equivalence relations must be transitively completed.

The closest identified finite-structure numerical-profile result concerns parameter-free equivalence-only finite structures and admits all-arity collisions; it does not imply reconstruction for an infinite homogeneous graph enriched by \(E\) and \(R\). A separate countable-grid result with **two** named equivalences finds arity-two saturation, contrasting with the unbounded hierarchy here. A complete-multipartite metric-graph distance-histogram result reconstructs four **positive-integer** part-size moments from a continuous probability density, rather than this family of dyadic moments from injective tuple orbits. These are logical comparisons, not claims that generic power-sum inversion or integer-polynomial root constructions were invented here. See the references for their identifiers and precise scopes.

## Limitations
Complete numerical spectra recover the unordered old \(E\)-class-size profile, **not** the entire old induced structure, including its arbitrary inter-class \(R\)-edges. The recovery bound of \(n\) is not claimed optimal for each fixed \(n\). Unbounded arity is proved only as base size is allowed to grow; no fixed-size infinite hierarchy is possible. The twelve-point uniqueness concerns first **one-point** collisions between differing class-size profiles, not ordinary graph nonisomorphism. The polynomial construction may yield large bases, and no minimality claim is made for those witnesses. Priority among less accessible earlier studies of finite-base orbit growth remains provisional; no independently validated novelty or completeness claim is made.

## References
1. P. J. Cameron, *Oligomorphic Permutation Groups*, Cambridge University Press, first print publication 1990-06-29, DOI 10.1017/CBO9780511549809, https://www.cambridge.org/core/books/oligomorphic-permutation-groups/6800CDD438C175EB8C077DDAA37CCD2B.
2. P. J. Cameron, *Sequences Realized by Oligomorphic Permutation Groups*, Journal of Integer Sequences 3 (2000), Article 00.1.5, https://cs.uwaterloo.ca/journals/JIS/VOL3/groups.html.
3. G. Conant, *An axiomatic approach to free amalgamation*, initial arXiv posting 2015-05-04, arXiv:1505.00762, https://arxiv.org/abs/1505.00762 (inspected current author-corrected 2023 HTML version for foundational distinctions).
4. *Sharp labeled and unlabeled profile collisions in finite equivalence structures*, publicly indexed scientific result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/18/SCOPE-sharp-labeled-and-unlabeled-profile-collisions-in-finite-equival--36357a3c6fd5.
5. *Arity-two saturation and unbounded collisions in finite-base type spectra of the countable grid*, publicly indexed scientific result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/26/SCOPE-arity-two-saturation-and-unbounded-collisions-in-finite-base-typ--801562567ff1.
6. *Four-moment completeness and the sharp five-part collision threshold for metric-graph distance histograms*, publicly indexed scientific result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-four-moment-completeness-and-the-sharp-five-part-collision-thres--eb449f182615.
