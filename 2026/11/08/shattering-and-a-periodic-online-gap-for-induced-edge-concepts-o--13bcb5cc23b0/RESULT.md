# Shattering and a periodic online gap for induced-edge concepts on cycles

## Finding
Let \(n\ge3\), and let \(C_n\) be the labeled cycle with vertices \(v_0,\ldots,v_{n-1}\) and edges \(e_i=\{v_i,v_{i+1\bmod n}\}\). Define the binary concept class on its edge set by
\[
\mathcal H_n=\{E(C_n[A]):A\subseteq V(C_n)\}.
\]
A concept answers whether both endpoints of a queried edge belong to \(A\). The following assertions hold.

1. The realized binary edge words are exactly those avoiding the cyclic consecutive pattern \(101\). A query support \(S\subseteq E(C_n)\) is VC-shattered exactly when its cyclic incidence word avoids \(111\).
2. Writing \(s_k(n)\) for the number of shattered supports containing \(k\) edges, the entire polynomial is
\[
\Phi_n(z)=\sum_{k=0}^{\lfloor2n/3\rfloor}s_k(n)z^k,\qquad
s_k(n)=\frac{n}{n-k}\,[t^k](1+t+t^2)^{n-k}.
\]
In particular, \(\operatorname{VCdim}(\mathcal H_n)=\lfloor2n/3\rfloor\). The number of maximum-size shattered supports is \(3\), \(n(n+5)/6\), or \(n\), according as \(n\equiv0,1,2\pmod3\). Equivalently, for \(n=3q+1\) it is \(n(q+2)/2\).
3. For every \(q\ge1\),
\[
\operatorname{VCdim}(\mathcal H_{3q+1})=2q,
\qquad\operatorname{Ldim}(\mathcal H_{3q+1})=2q+1.
\]
For every \(q\ge1\), \(\operatorname{VCdim}(\mathcal H_{3q})=\operatorname{Ldim}(\mathcal H_{3q})=2q\). Thus arbitrarily large cyclic concept classes exhibit a strict one-unit online/static separation, whereas the neighboring divisible-by-three subfamily exhibits equality.

## Assumptions and scope
The vertex subset \(A\) may be empty. Distinct choices of \(A\) producing the same binary edge word are identified as a single concept. Edges are undirected, indexed cyclically, and queried individually. All claims concern arbitrary integers \(n\ge3\); the online equality assertions are deliberately restricted to the two specified congruence classes. The standard realizable Littlestone dimension is the maximum depth of a complete adaptive binary query tree; the VC dimension is maximum cardinality of a nonadaptively shattered edge support. The coefficients count **labeled** supports, not dihedral orbits.

## Proof
**The edge-word image.** For a vertex indicator word \(a_i=\mathbf1[v_i\in A]\), the concept's edge indicators satisfy \(b_i=a_i a_{i+1}\). A cyclic \(101\) centered at edge \(e_i\) is impossible: \(b_{i-1}=b_{i+1}=1\) forces both endpoints of \(e_i\) into \(A\), hence \(b_i=1\). Conversely, for a binary word \(b\) with no cyclic \(101\), choose \(A\) to be the endpoints of all edges whose desired labels are one. Positive edges are then realized. If a desired zero edge had both endpoints selected, then each endpoint would have to belong to a neighboring positive edge, yielding a forbidden cyclic \(101\). Thus the word is realized. This argument also handles \(n=3\) and the all-zero word.

**Exactly which supports shatter.** If \(S\) contains three consecutive cyclic edges, prescribe one on the first and third and zero on the middle. These responses cannot coexist by the preceding obstruction, so \(S\) is not shattered. Conversely, assume \(S\) contains no three consecutive cyclic edges. Its nonisolated components as an edge subgraph of the cycle are pairwise vertex-disjoint single edges or two-edge paths (also when \(n=3\)). Given any subset \(T\subseteq S\), take \(A\) to be the union of the endpoints of edges in \(T\). Every edge of \(T\) is present. Every edge in \(S\setminus T\) has an endpoint of degree one in the graph \((V,S)\), and this endpoint cannot be an endpoint of any edge of \(T\); hence that edge is absent. Thus every labeling of \(S\) is realized.

**Exact coefficients and maxima.** Let \(k\) be the number of chosen edges and \(z=n-k\) the positive number of unchosen edges. Mark one of the \(z\) zero positions. Going forward cyclically from that marked zero, record the numbers of consecutive chosen edges before each next zero. This gives an ordered \(z\)-tuple of elements of \(\{0,1,2\}\) summing to \(k\), and the construction is reversible with a specified position for the marked zero. Double-counting such word/marked-zero pairs gives
\[
z s_k(n)=n[t^k](1+t+t^2)^z.
\]
Necessarily \(k\le2z\), or \(k\le\lfloor2n/3\rfloor\). Equality at this floor is attainable by distributing \(k\) ones into zero-separated runs of length at most two; hence the VC dimension is the stated floor. When \(n=3q\), the unique gap vector has all \(q\) entries two, giving \(3\) labeled rotations. When \(n=3q+1\), \(z=q+1\) and there are two missing ones relative to the all-two vector, either one slot drops to zero or two slots drop to one; this gives \(n(q+2)/2=n(n+5)/6\). When \(n=3q+2\), one slot drops from two to one, giving \(n\).

**Online upper bounds.** A basic disjoint-coordinate lemma states that if a concept class restricts on each of disjoint query blocks to a class of Littlestone dimension at most \(d_j\), then its dimension is at most \(\sum_j d_j\). To prove it, embed the class in the Cartesian product of its block projections and induct on \(\sum_jd_j\): at any query in block \(j\), at least one response branch has a projected dimension at most \(d_j-1\), or the block projection would have dimension exceeding \(d_j\); the other projections stay inside their original classes. A complete tree of depth greater than the sum is therefore impossible. In any three consecutive edge positions, the pattern \(101\) is absent, so the three-coordinate projection contains at most seven hypotheses and has Littlestone dimension at most two (a depth-three tree requires at least eight hypotheses). A singleton-coordinate projection has dimension at most one. Partition the \(3q\) edge indices into \(q\) consecutive triples to get \(\operatorname{Ldim}(\mathcal H_{3q})\le2q\). Partition the \(3q+1\) indices into \(q\) consecutive triples and one singleton to get \(\operatorname{Ldim}(\mathcal H_{3q+1})\le2q+1\). This only uses triples internal to the cyclic edge order, and hence is valid irrespective of further cross-block constraints.

**Matching online lower bounds.** The VC bound already gives depth \(2q\) for \(n=3q\). For \(n=3q+1\), make edge \(e_0\) the root query. On the response-zero branch choose as the next nonadaptive queries the \(2q\) edges \(e_{3j+1},e_{3j+2}\) for \(0\le j<q\). These form \(q\) disjoint two-edge paths using vertices indexed \(1\) through \(3q\); all their binary labels can be independently realized by selecting vertex subsets within each path while leaving vertex \(v_0\) outside \(A\), which keeps \(e_0\) negative. On the response-one branch force \(v_0,v_1\in A\); choose \(e_1,e_{3q}\) and the \(2(q-1)\) edges \(e_{3j},e_{3j+1}\) for \(1\le j<q\). The two outer queries are freely controlled by the distinct vertices \(v_2,v_{3q}\), while every central pair is a two-edge path on a separate group of three vertices; all these controls are independent and avoid \(v_0,v_1\). Thus every one of the \(2^{2q}\) labelings is realized below each response branch. These two depth-\(2q\) complete (nonadaptive) subtrees yield an adaptive tree of depth \(2q+1\). Together with the upper bound this proves the online equality and separation.

## Verification
The included standalone Python checker enumerates the distinct edge concepts from all vertex subsets, independently enumerates every edge support, checks the cyclic forbidden-pattern criterion against explicit shattering, reproduces every coefficient, and calculates the Littlestone recursion for \(3\le n\le9\). It checks static coefficients through \(n=10\). All assertions passed. The unrestricted conclusions above rest on the written proofs, not on the finite computations.

## Relationship to prior work
Guingona, Kolesnikov, Nierwinski and Soucy (first public version September 10, 2021) establish equality of VC and Littlestone dimension for a different class of linear-combination zero sets; their theorem does not apply to these locally conjoined cycle-edge concepts. Ghazi, Golowich, Kumar and Manurangsi (2021) provide general Boolean-aggregation dimension bounds, not the exact cyclic support structure or the adaptive one-unit gap. Classic dissociation-set enumerations provide an alternative expression for the no-\(111\) support coefficients; the enumeration **alone** is not claimed to be a new sequence. The claim here is the model-theoretic identification of the shattered supports together with the sharp online separation for infinitely many cycle sizes. Searches also considered earlier graph VC-dimension literature and related published records; none of the inspected results states or implies the entire theorem.

## Limitations
The exact Littlestone dimension for \(n\equiv2\pmod3\) is not proved here; the present arguments only give \(\lfloor2n/3\rfloor\le\operatorname{Ldim}(\mathcal H_n)\le\lfloor2n/3\rfloor+1\) in this residue class. Finite computations suggest equality with VC dimension in the small examples, but are not an all-order proof. The all-degree support enumeration is a known-type no-\(111\) cyclic-word count, so its intrinsic novelty is limited; the main nontrivial contribution is the precise adaptive separation and its construction. No independent mathematical audit or exhaustive historical priority proof has been performed.

## References
- V. Guingona, A. Kolesnikov, J. Nierwinski, R. Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805 (first posted 2021-09-10), https://arxiv.org/abs/2109.04805.
- B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight Closure Bounds for the Littlestone and Threshold Dimensions*, ALT 2021, PMLR 132, https://proceedings.mlr.press/v132/ghazi21a.html.
- I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik–Chervonenkis dimension and density on Johnson and Hamming graphs*, arXiv:2007.16042, https://arxiv.org/abs/2007.16042 (background on graph-defined concepts, not a source for the theorem).
