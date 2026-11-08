# Graph-isomorphism completeness for perfect and simple evolution algebras over fixed finite fields

## Finding

Fix a prime power \(q\ge 2\). Given two finite-dimensional evolution algebras over the **same fixed field** \(\mathbb F_q\), each specified by its natural-basis structure matrix, deciding whether they are isomorphic as \(\mathbb F_q\)-algebras is graph-isomorphism complete (GI-complete) under deterministic polynomial-time many-one reductions, even if both algebras are promised to be perfect. **The same conclusion holds if both algebras are promised to be simple.**

More explicitly, the following two reductions hold.

1. An arbitrary \(n\)-dimensional perfect evolution algebra can be encoded as a directed graph with two edge colors on exactly \(n(q-1)\) vertices. Two such algebras are isomorphic if and only if their colored directed graphs are isomorphic. For fixed \(q\), the encoding and its conversion to an ordinary undirected graph are polynomial time.
2. For every undirected simple graph \(G\) on \(n\ge 1\) vertices, there is an explicit simple evolution algebra \(E_G\) of dimension \(4n+6\), with structure coefficients all in \(\{0,1\}\), such that \(G\cong G'\) if and only if \(E_G\cong E_{G'}\). These algebras are simple over **every** field; fixed finite fields are used only for the upper reduction.

Here GI-complete means polynomial-time many-one interreducible with the ordinary isomorphism problem for finite undirected simple graphs. The finite field is not part of the input. This is not a claim about the complexity when \(q\) varies and is supplied in a succinct encoding.

## Assumptions and scope

An evolution algebra \(E(A)\) associated with \(A=(a_{ij})\in M_n(K)\) has a designated basis \(e_1,\dots,e_n\), with \(e_ie_j=0\) for \(i\ne j\) and \(e_i^2=\sum_j a_{ij}e_j\). It is perfect when \(A\) is invertible. An algebra is simple when it has no nonzero proper two-sided ideals and has nonzero square; the constructed examples satisfy this in every characteristic.

All isomorphisms are \(K\)-linear algebra isomorphisms, not semilinear or isotopy maps. Graph isomorphisms preserve directions and colors when those are specified. Matrices can have arbitrary entries of the fixed field in the upper reduction. No promise of connectedness or nonzero diagonal entries is made in the upper reduction. The lower reduction uses connected graphs to produce simple algebras.

## Proof

**1. Monomial rigidity and its exact equations.** Let \(E(A),E(B)\) be perfect of the same dimension and let \(\varphi:E(A)\to E(B)\) be an algebra isomorphism. Write \(\varphi(e_i)=\sum_k p_{ik}f_k\). For \(i\ne j\),

\[
0=\varphi(e_ie_j)=\sum_k p_{ik}p_{jk}f_k^2.
\]

Since \(B\) is invertible, the \(f_k^2\) form a basis. Consequently, \(p_{ik}p_{jk}=0\) for every \(k\) and distinct \(i,j\). Each column of the invertible matrix \(P=(p_{ik})\) has exactly one nonzero entry, so each row does also. Thus there are a permutation \(\sigma\in S_n\) and nonzero scalars \(s_i\) with \(\varphi(e_i)=s_i f_{\sigma(i)}\). Comparison of squares yields the necessary and sufficient equations

\[
  a_{ij}s_j=s_i^2 b_{\sigma(i),\sigma(j)}\qquad(1\le i,j\le n).
  \tag{1}
\]

Conversely, any permutation and nonzero scalars satisfying (1) give an algebra isomorphism. This also rederives the standard natural-basis rigidity theorem for perfect evolution algebras.

**2. Reduction to graph isomorphism.** Fix \(K=\mathbb F_q\) and fix a generator \(g\) of the cyclic multiplicative group \(K^\times\). For a structure matrix \(A\), form a directed graph \(\mathcal C(A)\) with two distinct arc colors \(\alpha,\beta\), and vertex set

\[
  V(A)=\{(i,t):1\le i\le n,\ t\in K^\times\}.
\]

Place the \(\alpha\)-arc \((i,t)\to(i,gt)\) for each vertex. For every \(a_{ij}\ne0\), place the \(\beta\)-arc

\[
  (i,t)\longrightarrow (j,t^2a_{ij})
  \quad(t\in K^\times).
\]

The two arc relations are separate: a pair of vertices may carry arcs of both colors, including loops. The \(\alpha\)-arcs form exactly \(n\) disjoint directed cycles of length \(q-1\), including singleton loops if \(q=2\). Any two-color graph isomorphism must permute these cycles and commute with their successor action. Therefore it is necessarily of the form

\[
  (i,t)\longmapsto (\sigma(i),t s_i)
\]

for some permutation \(\sigma\) and \(s_i\in K^\times\). For each \(i,j\), the presence or absence of \(\beta\)-arcs between the corresponding cycles forces \(a_{ij}=0\iff b_{\sigma(i),\sigma(j)}=0\). When these entries are nonzero, preservation of the \(\beta\)-arc at \(t=1\) is precisely equation (1). Conversely, (1) ensures preservation of every \(\beta\)-arc at every \(t\), while the form of the map automatically preserves \(\alpha\)-arcs. Thus

\[
  E(A)\cong E(B)\iff \mathcal C(A)\cong\mathcal C(B).
  \tag{2}
\]

There are exactly \(n(q-1)\) vertices, \(n(q-1)\) \(\alpha\)-arcs and at most \(n^2(q-1)\) \(\beta\)-arcs. For fixed \(q\), this is polynomial in the structure-matrix input length. A finite directed graph with two colored arc relations reduces in polynomial time to an undirected simple graph. First form a vertex-colored undirected incidence graph: keep one vertex of a base color for every original vertex, and for each directed arc \(u\to v\) of color \(c\), add two new vertices of distinct colors \((c,\mathrm{out})\), \((c,\mathrm{in})\), joined along the path \(u-(c,\mathrm{out})-(c,\mathrm{in})-v\). This preserves and reflects source, target, arc color, loops and simultaneous arcs. Then replace the finitely many vertex colors by distinguishable constant-size attached marker gadgets to get an ordinary uncolored simple graph. Thus colored directed graph isomorphism reduces to GI in polynomial time. Therefore perfect evolution-algebra isomorphism reduces to ordinary GI. The simple subclass inherits this reduction.

**3. Connected graph encoding of arbitrary undirected graphs.** Let \(G\) be a finite undirected simple graph on \(n\ge1\) vertices. Make a new graph \(H(G)\) by adjoining one vertex \(h\) adjacent to every old vertex, and \(n+2\) new leaves adjacent only to \(h\). The graph \(H(G)\) has \(m=2n+3\) vertices and is connected. Its hub has degree \(2n+2\), whereas each old vertex has degree at most \(n\) and each new leaf has degree one. Thus the hub is unique. From \(H(G)\), knowing \(m\) and hence \(n\), one canonically recovers the subgraph induced by its non-hub vertices of degree at least two: that is \(G\) with all isolated vertices removed. The number of omitted isolated vertices is \(n\) minus the number of recovered vertices. Therefore

\[
  G\cong G'\iff H(G)\cong H(G').
  \tag{3}
\]

**4. Encoding connected graphs as simple evolution algebras.** Let \(H\) be any connected undirected simple graph on \(m\) vertices, with adjacency matrix \(C\). Over any field \(K\), define an evolution algebra \(E_H\) with natural basis \(x_v,y_v\) indexed by \(v\in V(H)\), with

\[
  x_v^2=x_v+\sum_{w\sim v}x_w+y_v,\qquad
  y_v^2=x_v,
\]

and all mixed products of different basis elements zero. Its structure matrix, in the order \(x_1,\ldots,x_m,y_1,\ldots,y_m\), is

\[
  M_H=\begin{pmatrix}I_m+C&I_m\\ I_m&0\end{pmatrix}.
\]

This matrix is invertible over **any** field: if \(M_H(u,v)=0\), the bottom block gives \(u=0\) and then the top block gives \(v=0\). Hence \(E_H\) is perfect. Its multiplication digraph is strongly connected: the \(x_v\) vertices contain the two-way edges of connected \(H\), and each \(x_v\) and \(y_v\) are joined in both directions. For completeness, strong connectivity and perfection imply simplicity directly: any nonzero ideal contains some \(x_v^2\) or \(y_v^2\) by multiplying a nonzero element by a basis vector; further multiplication along directed edges propagates containment to all squares, which span the algebra. Therefore every nonzero ideal is the whole algebra.

Any graph isomorphism \(H\to H'\) permutes the \(x\)-basis and the correspondingly indexed \(y\)-basis and gives an algebra isomorphism. Conversely, suppose \(E_H\cong E_{H'}\). By Step 1, every such algebra isomorphism is monomial. The \(x_v\) are exactly the natural basis elements with a nonzero self-coefficient in their square, and the \(y_v\) are exactly those without one; hence each type is preserved. The self-coefficient of each \(x_v^2\) is one, so equation (1) forces its scale factor to be one. Each \(x_v^2\) has exactly one nonzero \(y\)-coefficient, identifying \(y_v\), and comparison of that coefficient forces the scale of \(y_v\) to be one as well. The remaining coefficients of \(x_v^2\) are exactly the adjacency relation in \(H\). Consequently

\[
  E_H\cong E_{H'}\iff H\cong H'.
  \tag{4}
\]

Combining (3) and (4), define \(E_G=E_{H(G)}\). It has dimension \(2m=4n+6\), is simple over any field, and isomorphism of these algebras is equivalent to isomorphism of the input graphs. This is a polynomial-time many-one reduction from GI to the isomorphism problem restricted to simple evolution algebras.

Together with Step 2, this proves GI-completeness for both simple and perfect evolution algebras over every fixed finite field. \(\square\)

## Verification

The accompanying standard-library checker constructs the two-colored graph, computes its graph-isomorphism canonical signature by exhaustive vertex permutations for all invertible two-dimensional structure matrices over \(\mathbb F_2\) and \(\mathbb F_3\), and independently tests the exact monomial algebra-isomorphism equations on every ordered pair. The two methods agree on all \(2{,}340\) comparisons. An additional \(225\) comparisons drawn from the \(180\) invertible two-dimensional matrices over \(\mathbb F_4\) use explicit arithmetic in \(\mathbb F_2[X]/(X^2+X+1)\). The checker also constructs the simple-algebra lower-bound gadget for every simple undirected graph with one through four vertices, checks invertibility over characteristics two and three, checks strong connectivity, and verifies recovery of graph isomorphism classes. This covers \(75\) graphs, with respective numbers of isomorphism classes \(1,2,4,11\).

Execute \(\texttt{python3 checker.py}\). The text file \(\texttt{verification_output.txt}\) records the actual deterministic result. Enumeration confirms the tested finite cases; the proof above, rather than finite checking, establishes arbitrary dimensions and all fixed prime powers.

## Relationship to prior work

Kaygorodov, Martín González and Viruel explicitly ask, in Question 50 of their October 15, 2026 survey, for the complexity of isomorphism of perfect evolution algebras over finite fields relative to graph isomorphism. Their survey also records natural-basis monomial rigidity and contains a graph-to-algebra construction for realizing automorphism groups. Those inputs do not state the pairwise isomorphism-completeness theorem or the linear-sized finite-field upper encoding given here.

Elduque and Labra established the graph-theoretic description and automorphism structure of perfect evolution algebras; monomial rigidity is used here, with a short independent derivation. Falcón, Falcón and Núñez (2019) constructed a total-colored graph functor for evolution algebras and isotopisms using vertices \((x,y)\) from the full vector space. Because that construction ranges over vectors in the algebra, its size can grow exponentially in the natural-basis dimension over a fixed finite field; moreover its described categorical direction concerns isotopisms. It is not the present \(n(q-1)\)-vertex isomorphism-equivalence reduction. The present two-sided polynomial-time complexity classification and the simple-algebra hardness gadget were not identified in the literature compared below.

## Limitations

The field \(\mathbb F_q\) is fixed outside the input. The graph construction has \(n(q-1)\) vertices, so it is not claimed polynomial in \(\log q\) when the field varies. The algebra input is a structure matrix in a supplied natural basis; recognizing such a basis for an arbitrary multiplication table is a different problem. No algorithm for GI itself is claimed, nor any NP-completeness result. The lower-bound algebras have a special form, but the theorem does not classify all simple evolution algebras. Earlier literature could contain a complexity-equivalent graph encoding expressed in other language; historical priority is not independently certified.

## References

1. I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first posted October 15, 2026), especially Theorem 4 and Question 50, https://arxiv.org/html/2610.22248.
2. A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685 (2013), https://arxiv.org/abs/1312.4685.
3. A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191 (2019), https://arxiv.org/abs/1902.02191.
4. R. M. Falcón, Ó. J. Falcón and J. Núñez, *An Application of Total-Colored Graphs to Describe Mutations in Non-Mendelian Genetics*, Mathematics 7 (2019), 1068, https://doi.org/10.3390/math7111068.
