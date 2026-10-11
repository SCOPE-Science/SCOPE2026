# Projective rigidity and the rank-three spectrum of elementary-abelian join graphs

## Finding

Let \(p\) be a prime, let \(d\ge3\), and put
\[
E_{p,d}=C_p^d.
\]
Use Lucchini's convention for the join graph \(\Delta(E_{p,d})\): every proper subgroup is a vertex, and two distinct proper subgroups are adjacent exactly when together they generate \(E_{p,d}\).

Then
\[
\boxed{\operatorname{Aut}(\Delta(E_{p,d}))\cong \operatorname{PGL}(d,p).}
\]

Moreover, within the elementary-abelian family of ranks at least three,
\[
\boxed{
\Delta(C_p^d)\cong\Delta(C_r^e)
\quad\Longleftrightarrow\quad
p=r\ \text{and}\ d=e.
}
\]

The first noncomplete rank has an explicit spectrum. For \(d=3\), set
\[
N=p^2+p+1.
\]
The nonisolated vertices split into the \(N\) one-dimensional subspaces and the \(N\) two-dimensional subspaces of \(\mathbf F_p^3\). The one-dimensional vertices form an independent set, the two-dimensional vertices form a clique, and a point vertex is adjacent to a plane vertex exactly when the point is not contained in the plane.

Consequently the characteristic polynomial of the full join graph, including its isolated identity subgroup, is
\[
\boxed{
\chi_{\Delta(C_p^3)}(x)
=
x\bigl(x^2-(p^2+p)x-p^4\bigr)
\bigl(x^2+x-p\bigr)^{p^2+p}.
}
\]

Equivalently, its nonzero spectral data are the two roots of
\[
x^2-(p^2+p)x-p^4
\]
with multiplicity one, and the two roots of
\[
x^2+x-p
\]
with multiplicity \(p^2+p\). Its graph energy is
\[
\boxed{
\mathcal E(\Delta(C_p^3))
=
p\sqrt{5p^2+2p+1}
+
(p^2+p)\sqrt{4p+1}.
}
\]

The rank-two case is a sharp boundary:
\[
\Delta(C_p^2)\cong K_1\sqcup K_{p+1},
\]
so
\[
\operatorname{Aut}(\Delta(C_p^2))\cong S_{p+1},
\]
which is generally larger than the projective linear group.

## Assumptions and scope

The group \(E_{p,d}\) is identified with the additive group of the vector space
\[
V=\mathbf F_p^d.
\]
Thus its subgroups are exactly the linear subspaces of \(V\), and generation of two subgroups is their vector-space sum.

Lucchini's join graph includes subgroups contained in the Frattini subgroup. For an elementary-abelian group the Frattini subgroup is \(0\), so this adds exactly the identity subgroup as an isolated vertex. The earlier reduced convention omits that one isolated vertex.

The automorphism theorem uses \(d\ge3\), precisely the range in which the fundamental theorem of projective geometry applies to the full subspace lattice without the rank-two complete-graph collapse.

## Proof

Identify a vertex with a proper subspace of
\[
V=\mathbf F_p^d.
\]
The zero subspace is isolated. Every nonzero proper subspace \(U\) has a linear complement \(X\), so
\[
U+X=V;
\]
therefore \(0\) is the unique isolated vertex.

For any proper subspaces \(U,W\),
\[
\boxed{
U\le W
\quad\Longleftrightarrow\quad
N(U)\subseteq N(W),
}
\]
where \(N(U)\) denotes the open graph neighborhood.

If \(U\le W\) and \(X\in N(U)\), then
\[
V=U+X\le W+X\le V,
\]
so \(X\in N(W)\).

Conversely, assume
\[
U\not\le W.
\]
Choose
\[
u\in U\setminus W.
\]
There is a linear functional
\[
\varphi:V\to\mathbf F_p
\]
that vanishes on \(W\) but not on \(u\). Its kernel
\[
H=\ker\varphi
\]
is a hyperplane containing \(W\) and not containing \(u\). Hence
\[
U+H=V,
\]
so \(H\in N(U)\), while
\[
W+H=H\ne V,
\]
so \(H\notin N(W)\). This proves the equivalence.

Thus the graph itself reconstructs the order relation on all proper subspaces. A graph automorphism fixes the unique isolated vertex and preserves neighborhood inclusion, hence induces an order automorphism of the full subspace lattice after adjoining \(V\) as its maximum element.

For \(d\ge3\), the fundamental theorem of projective geometry says that every such lattice automorphism is induced by a semilinear automorphism of \(V\). Since the ground field is the prime field \(\mathbf F_p\), it has no nontrivial field automorphisms. Therefore every graph automorphism is induced by an element of
\[
\operatorname{GL}(d,p).
\]
Two invertible linear maps induce the same permutation of all subspaces exactly when they differ by a nonzero scalar. Conversely, every invertible linear map preserves the condition
\[
U+W=V,
\]
so it induces a graph automorphism. Hence
\[
\operatorname{Aut}(\Delta(E_{p,d}))
\cong
\operatorname{GL}(d,p)/\mathbf F_p^\times
=
\operatorname{PGL}(d,p).
\]

The same neighborhood-inclusion reconstruction shows that an isomorphism
\[
\Delta(C_p^d)\cong\Delta(C_r^e)
\]
with \(d,e\ge3\) induces an isomorphism of their subspace lattices. The maximal chain length gives
\[
d=e.
\]
The number of atoms is
\[
1+p+\cdots+p^{d-1},
\]
which is strictly increasing in \(p\), so
\[
p=r.
\]
The converse is immediate.

Now specialize to \(d=3\). There are
\[
N=p^2+p+1
\]
one-dimensional subspaces and the same number of two-dimensional subspaces. Two one-dimensional subspaces cannot generate \(V\), while two distinct planes always sum to \(V\). A point \(P\) and a plane \(H\) generate \(V\) exactly when
\[
P\not\le H.
\]

Let \(M\) be the point-plane incidence matrix of the projective plane
\[
\operatorname{PG}(2,p),
\]
and let
\[
B=J-M
\]
be its nonincidence matrix. Ordering point vertices first and plane vertices second, the adjacency matrix of the nonisolated graph is
\[
A=
\begin{pmatrix}
0&B\\
B^{\mathsf T}&J-I
\end{pmatrix}.
\]

Each projective point lies on \(p+1\) projective lines, and two distinct points lie on a unique common line. Therefore
\[
MM^{\mathsf T}=pI+J.
\]
Since
\[
N=p^2+p+1,
\]
one obtains
\[
BB^{\mathsf T}
=
pI+p(p-1)J.
\]

On the two-dimensional space spanned by the all-ones vectors of the point and plane parts, \(A\) acts by
\[
\begin{pmatrix}
0&p^2\\
p^2&p^2+p
\end{pmatrix},
\]
whose characteristic polynomial is
\[
x^2-(p^2+p)x-p^4.
\]

On the orthogonal complements of the all-ones vectors,
\[
BB^{\mathsf T}=pI
\]
and
\[
(J-I)=-I.
\]
After pairing corresponding singular directions of \(B\), the remaining action is a direct sum of \(N-1=p^2+p\) copies of
\[
\begin{pmatrix}
0&\sqrt p\\
\sqrt p&-1
\end{pmatrix},
\]
whose characteristic polynomial is
\[
x^2+x-p.
\]
Finally the identity subgroup supplies one zero eigenvalue. This proves the displayed characteristic polynomial.

For a quadratic
\[
x^2-sx-t
\]
with \(t>0\), the two real roots have opposite signs and the sum of their absolute values is
\[
\sqrt{s^2+4t}.
\]
Applying this to the two quadratic factors gives
\[
p\sqrt{5p^2+2p+1}
\]
and
\[
(p^2+p)\sqrt{4p+1},
\]
which proves the energy formula.

For \(d=2\), every nonzero proper subgroup is one-dimensional, and any two distinct such subgroups generate the whole space. Hence the nonisolated graph is
\[
K_{p+1},
\]
establishing the stated boundary.

## Verification

The included checker constructs the projective point-plane geometry and the join graph directly for
\[
p=2,3,5.
\]
For each prime it independently verifies:

- the exact point and plane counts;
- the join-graph adjacency rule;
- the point and plane degrees;
- the projective identity
  \[
  MM^{\mathsf T}=pI+J;
  \]
- the nonincidence identity
  \[
  BB^{\mathsf T}=pI+p(p-1)J;
  \]
- the neighborhood-inclusion reconstruction
  \[
  U\le W\Longleftrightarrow N(U)\subseteq N(W)
  \]
  for every pair of proper subspaces in rank three;
- the annihilating polynomial obtained from the two displayed quadratic spectral factors;
- the dimension and trace-square checks implied by the stated multiplicities.

The checker returns `VERIFY_OK`.

These finite checks are not used as a proof of the universal automorphism theorem or the symbolic spectrum formula.

## Relationship to prior work

Ahmadi and Taeri introduced the join graph and developed its basic structural invariants. Later work treated planarity, regularity, domination, independence, genus, and several distance-based graph polynomials.

Lucchini modified the convention by retaining the Frattini-contained subgroups as isolated vertices and asked how much group structure is forced by an isomorphism of join graphs. He proved that the lattice of maximal intersections can be reconstructed from the graph and classified the Frattini-free groups sharing a join graph with a nilpotent group.

The present result specializes that reconstruction problem to elementary-abelian groups but extracts a sharper self-symmetry statement: in rank at least three, every graph automorphism is geometric, and the entire graph automorphism group is exactly
\[
\operatorname{PGL}(d,p).
\]
The direct neighborhood-inclusion argument also gives elementary-abelian isomorphism rigidity without appealing to a group classification.

For rank three, earlier join-graph papers give adjacency matrices and topological indices for other small abelian families, but the inspected full texts do not supply the projective-plane block decomposition or the characteristic polynomial displayed here. The nearest published projective-nonincidence result concerns the bipartite point-hyperplane nonincidence graph by itself; the join graph has, in addition, a complete graph on the plane vertices, which changes both its spectrum and its automorphism problem.

A 2019 paper titled “Further results on the join graph of a finite group” is highly relevant. Its public abstract states results on domination, independence, solvability, and recognition of \(A_4\), but a full-text copy was not available through the public download path inspected here. It therefore remains a bibliographic residual risk rather than evidence of noncoverage.

## Limitations

The automorphism theorem is stated over prime fields because the group is elementary abelian of exponent \(p\). For vector spaces over a nonprime finite field viewed only as elementary-abelian groups over their prime field, the relevant subgroup lattice is the prime-field lattice.

The exact characteristic polynomial is given only for rank three, the first rank in which the elementary-abelian join graph is not merely an isolated vertex plus a complete graph.

The result does not classify all finite groups having the same join graph as \(C_p^d\); Lucchini's work shows that nonnilpotent groups can share join graphs with nilpotent groups.

A spectral or automorphism statement equivalent to the rank-three formulas may exist under projective-incidence terminology not captured by the searches.

## References

1. A. Lucchini, “Finite groups with the same join graph as a finite nilpotent group,” arXiv:2003.12969v1, first public version 29 March 2020; *Glasgow Mathematical Journal* 63 (2021), 640–650, DOI 10.1017/S0017089520000415.
2. H. Ahmadi and B. Taeri, “A graph related to the join of subgroups of a finite group,” *Rendiconti del Seminario Matematico della Università di Padova* 131 (2014), 281–292, DOI 10.4171/RSMUP/131-17.
3. A. Asrari and B. Tolue, “Some new results on the join graph of given groups,” *Mathematica* 60 (83) (2018), no. 1, 3–11, DOI 10.24193/mathcluj.2018.1.01.
4. Z. Bahrami and B. Taeri, “Further results on the join graph of a finite group,” *Turkish Journal of Mathematics* 43 (2019), 2097–2113, DOI 10.3906/mat-1902-61.
