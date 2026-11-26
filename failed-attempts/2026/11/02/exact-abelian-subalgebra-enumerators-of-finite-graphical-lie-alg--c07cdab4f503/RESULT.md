# Exact abelian-subalgebra enumerators of finite graphical Lie algebras

## Finding

For every finite simple graph \(G=(V,E)\), every prime power \(q\), and every dimension \(d\), the number of \(d\)-dimensional abelian subalgebras of its graph Lie algebra over \(\mathbb F_q\) is given by an explicit finite expression involving only the connected-component counts of induced subgraphs and Gaussian binomial coefficients. The expression uniformly counts subalgebras that do or do not contain the whole derived algebra.

Write \(n=|V|\), \(m=|E|\), and let \(c(S)\) be the number of connected components of the induced graph \(G[S]\); set \(c(\varnothing)=0\). Define the *commuting-frame enumerator*

\[
F_r(G,q)=\sum_{S\subseteq V}(q^r-1)^{c(S)}(q-1)^{|S|-c(S)}\qquad(r\geq0).
\]

Put \(\genfrac{[}{]}{0pt}{}{a}{b}_q={a\brack b}_q\) for the Gaussian binomial coefficient, and use the convention \(|\operatorname{GL}_0(q)|=1\). The exact number of commuting \(k\)-dimensional subspaces of the vertex space is

\[
A_k(G,q)=\frac{1}{|\operatorname{GL}_k(q)|}
\sum_{j=0}^{k}(-1)^{k-j}q^{\binom{k-j}{2}}
{k\brack j}_q F_j(G,q),\qquad 0\leq k\leq n.
\]

The exact number of \(d\)-dimensional abelian Lie subalgebras is

\[
\boxed{B_d(G,q)=\sum_{\substack{0\leq k\leq n,\ 0\leq t\leq m\\k+t=d}}
A_k(G,q){m\brack t}_q q^{k(m-t)}.}
\]

In particular, with \(\alpha(G)\) the ordinary independence number, the largest possible dimension is \(m+\alpha(G)\), and the number of subalgebras attaining it equals

\[
\boxed{B_{m+\alpha(G)}(G,q)=
\sum_{\substack{S\subseteq V\\c(S)=\alpha(G)}}(q-1)^{|S|-\alpha(G)}.}
\]

The maximal *dimension* itself is already implied by earlier results on independent sets and abelian subalgebras; its exact multiplicity and the complete distribution \(B_d\) are the enumerative claims assessed here.

## Assumptions and scope

The graph is finite, simple, undirected, and may contain disconnected components and isolated vertices. An empty graph is allowed by the same formulas, with the usual empty-product conventions. The field \(\mathbb F_q\) can have any characteristic, including characteristic two, and \(q\) can be any prime power. All subalgebras are linear subspaces closed under the given Lie bracket; an *abelian* subalgebra has identically zero bracket.

The graph Lie algebra is \(\mathfrak g_G=U\oplus Z\), where \(U\) has basis \((x_v)_{v\in V}\) and \(Z\) has basis \((z_e)_{e\in E}\). With a fixed ordering on the vertices, \([x_u,x_v]=z_{\{u,v\}}\) when \(u<v\) are adjacent, the reverse bracket has the opposite sign, every other vertex bracket vanishes, and \([\mathfrak g_G,Z]=0\). In characteristic two this is understood as an alternating bracket; antisymmetry does not require a nonzero sign distinction. The displayed formulas are valid when \(Z\) is larger than the full center because of isolated vertices.

For \(a\geq b\geq0\), \({a\brack b}_q\) denotes the number of \(b\)-dimensional subspaces of \(\mathbb F_q^a\). In particular \({a\brack0}_q=1\), and \(|\operatorname{GL}_k(q)|=\prod_{i=0}^{k-1}(q^k-q^i)\). The power \(0^0\) is taken as one.

## Proof

**1. Edgewise determinants.** Let \(u_1,\ldots,u_r\in U\), expressed in the vertex basis. At each vertex \(v\) their coordinates form a column \(b_v\in\mathbb F_q^r\). Because the central basis vectors attached to distinct graph edges are independent,

\[
[u_i,u_j]=0\ \text{ for all }i,j
\quad\Longleftrightarrow\quad
\det\begin{pmatrix}(b_u)_i&(b_v)_i\\(b_u)_j&(b_v)_j\end{pmatrix}=0
\ \text{for every edge }\{u,v\}\text{ and every }i,j.
\]

The determinant system says that the two endpoint columns are linearly dependent, even in characteristic two. Let \(S\subseteq V\) be the set of vertices carrying nonzero columns. On every edge of \(G[S]\), both endpoint columns must lie on the same one-dimensional line. Hence, within each connected component of \(G[S]\), all columns lie on one common nonzero line. Conversely, this condition makes every edge determinant zero, since an edge leaving \(S\) meets a zero column.

For a component with \(s\) vertices there are \((q^r-1)/(q-1)\) choices of a line and \((q-1)^s\) nonzero columns on that line, giving \((q^r-1)(q-1)^{s-1}\). Multiplying over components and summing over all supports gives exactly \(F_r(G,q)\). When \(r=0\), only the zero tuple is counted and \(F_0=1\).

**2. Passing from commuting frames to commuting subspaces.** Every ordered commuting \(r\)-tuple spans a unique commuting subspace of some dimension \(k\). A fixed \(k\)-space is the image of exactly \(\prod_{i=0}^{k-1}(q^r-q^i)\) surjective linear maps \(\mathbb F_q^r\to\mathbb F_q^k\). Thus

\[
F_r(G,q)=\sum_{k=0}^{\min(r,n)} A_k(G,q)
\prod_{i=0}^{k-1}(q^r-q^i).
\tag{1}
\]

For fixed \(k\), every full-rank \(k\times n\) commuting matrix has a unique row space of dimension \(k\), and every such row space has precisely \(|\operatorname{GL}_k(q)|\) ordered bases. Möbius inversion of the lattice of subspaces of \(\mathbb F_q^k\), whose interval Möbius value in codimension \(s\) is \((-1)^s q^{\binom{s}{2}}\), gives the number of full-rank commuting \(k\times n\) matrices as

\[
\sum_{j=0}^k (-1)^{k-j}q^{\binom{k-j}{2}}{k\brack j}_q F_j(G,q).
\]

Dividing by the number of ordered bases proves the formula for \(A_k\). This also proves integrality and nonnegativity of the expression without relying on a symbolic simplification.

**3. Restoring the central part.** Let \(H\leq\mathfrak g_G\) be an abelian Lie subalgebra. Its image \(U_H\) under \(U\oplus Z\to U\) is a commuting subspace of dimension \(k\), and its intersection \(T_H=H\cap Z\) is an arbitrary \(t\)-subspace of \(Z\), where \(k+t=\dim H\). Modulo \(T_H\), the subalgebra is the graph of a unique linear map \(U_H\to Z/T_H\). Conversely, any such map, commuting \(U_H\), and \(T_H\) give an abelian subalgebra, because all commutators depend only on the \(U\)-projections. There are \({m\brack t}_q\) choices for \(T_H\), followed by exactly \(q^{k(m-t)}\) maps. The resulting decomposition is unique and proves the formula for \(B_d\).

**4. Maximum dimension and its multiplicity.** For a commuting subspace of dimension \(k\), choose an ordered basis and let \(S\) denote the nonzero-column support. Each component of \(G[S]\) contributes column span of dimension at most one, so \(k\leq c(S)\). Selecting one vertex from each component gives an independent set, hence \(c(S)\leq\alpha(G)\). An independent set of size \(\alpha(G)\) spans a commuting \(\alpha(G)\)-space, proving the bound is attained.

If the row space has dimension \(\alpha(G)\), necessarily \(c(S)=\alpha(G)\), and its component lines must be linearly independent. For such fixed \(S\), the number of full-rank matrices equals \(|\operatorname{GL}_{\alpha(G)}(q)|(q-1)^{|S|-\alpha(G)}\): choose independent nonzero representatives of component lines, then all remaining nonzero scalar multiples. Dividing by \(|\operatorname{GL}_{\alpha(G)}(q)|\) gives the stated top multiplicity. Any abelian subalgebra of dimension \(m+\alpha(G)\) must contain all of \(Z\), so no extra lifts occur.

## Verification

The bundled `verify.py` uses only the Python standard library. Run `python verify.py` from the directory containing it. It enumerates every reduced-row-echelon subspace of the vertex space independently, evaluates the native Lie-bracket determinants on each basis, and compares the dimension counts with the closed formulas. It separately enumerates all reduced-row-echelon subspaces of the full Lie algebra and checks the complete central-lift formula. This is independent finite enumeration, not a proof for infinite graph sizes.

The verifier passed 158 quotient graph/prime-field configurations and 44 full-algebra configurations, including every labelled simple graph on at most four vertices over \(\mathbb F_2\) or \(\mathbb F_3\) for the quotient census, plus tested cases over \(\mathbb F_5\). For the path \(P_4\), the quotient-space dimension distributions are \((1,15,5,0,0)\) over \(\mathbb F_2\) and \((1,40,7,0,0)\) over \(\mathbb F_3\). The complete Lie-subalgebra distributions are respectively \((1,127,747,771,155,5,0,0)\) and \((1,1093,9796,8932,859,7,0,0)\). Thus the number of maximal-dimensional abelian subalgebras in this case is \(2q+1\), not merely the number of maximum independent sets.

## Relationship to prior work

Lee's 2020 finite-field Lie-subalgebra zeta-function method gives a general computational framework for counting all subalgebras and examples, but the inspected treatment does not give a graph-uniform enumeration of *abelian* subalgebras. Barrionuevo and Tirao's 2022 graphical Lie-algebra paper studies rigidity; Godoy Molina and Lagos (2023) study subgraph-defined ideals and subalgebras. Rossmann's 2022 graphical-group counting polynomials enumerate conjugacy classes rather than abelian Lie subalgebra Grassmannians.

The closest structural predecessor is Aldi, Gabrielsen, Grandini, Harris and Kelley (2025), who establish bounds on abelian subalgebra dimensions using Lie-algebra independence numbers; specializing to graph algebras identifies the maximal possible dimension already. The present exact all-dimension counting formula is different from their independence-polynomial and maximal-dimension statements. The edge determinant equations are instances of binomial-edge-ideal geometry, so future comparison with comprehensive finite-field point-count results for these ideals remains important. An exhaustive literature uniqueness claim is not made.

## Limitations

The expressions are explicit finite sums over induced subgraphs, not necessarily a polynomial-time algorithm for arbitrary graphs. The theorem counts linear abelian Lie subalgebras, not isomorphism classes under automorphisms, and does not count nonabelian subalgebras. It applies to the standard unweighted simple-graph Lie algebra; repeated or identified edge brackets need a different argument. The verification is finite; the proof establishes all finite graphs and all prime powers. Global publication priority and independent mathematical audit are not established.

## References

1. Seungjai Lee, *Zeta functions of F_p-Lie algebras and finite p-groups*, arXiv:2010.02268, first public October 5, 2020. https://arxiv.org/abs/2010.02268
2. Josefina Barrionuevo and Paulo Tirao, *Rigid 2-step graph Lie algebras*, arXiv:2206.10572, first public June 21, 2022. https://arxiv.org/abs/2206.10572
3. Mauricio Godoy Molina and Diego Lagos, *Lie algebras associated with labeled directed graphs*, arXiv:2308.00272, first public August 6, 2023. https://arxiv.org/abs/2308.00272
4. Marco Aldi, Thor Gabrielsen, Daniele Grandini, Joy Harris, and Kyle Kelley, *Independence Polynomials of 2-step Nilpotent Lie Algebras*, arXiv:2504.19836, first public April 28, 2025. https://arxiv.org/abs/2504.19836
5. Tobias Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, Bulletin of the London Mathematical Society 54 (2022), 1923–1943. https://doi.org/10.1112/blms.12665
