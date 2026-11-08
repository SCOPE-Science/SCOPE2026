# The complete associative-form rank distribution of radical-square-zero quiver algebras

## Finding

Let \(Q\) be any finite quiver with \(n\ge1\) vertices and \(m\ge0\) arrows, allowing loops, parallel arrows, and disconnected components. Over any finite field \(k=\mathbb F_q\), let \(A=kQ/J^2\), with \(J\) the arrow ideal. The rank enumerator of all associative bilinear forms \(B:A\times A\to k\) is

\[
\mathcal R_{Q,q}(z)=\sum_{F\subseteq Q_1}(q-1)^{|F|}q^{|S_F\cup T_F|}z^{|S_F|+|T_F|}(1+(q-1)z)^{n-|S_F\cup T_F|},
\]
where \(S_F\) is the set of sources of arrows in \(F\), and \(T_F\) is the set of targets. More precisely, if \(B_\lambda(x,y)=\lambda(xy)\), write \(d_v=\lambda(e_v)\) and \(c_a=\lambda(a)\), and set \(F=\{a:c_a\ne0\}\). Then

\[
\operatorname{rank}B_\lambda=|S_F|+|T_F|+|\{v\notin S_F\cup T_F:d_v\ne0\}|.
\]
This is a complete classification of the possible ranks and their exact multiplicities, for every finite quiver and finite field. Each associative bilinear form is uniquely \(B_\lambda\) for one \(\lambda\in A^*\).

The maximal attainable rank is

\[
\max_{\lambda}\operatorname{rank}B_\lambda=n+|S_{Q_1}\cap T_{Q_1}|.
\]
Consequently, a nondegenerate associative form exists precisely when the nonisolated part of \(Q\) is a disjoint union of directed cycles (loops count as one-cycles), with exactly one incoming and one outgoing arrow at every nonisolated vertex. If \(c\) is the number of nonisolated vertices, there are then exactly \(q^c(q-1)^n\) nondegenerate forms; otherwise there are none. The nondegenerate-form enumeration agrees with the standard Frobenius-functional/unit correspondence and is not asserted to be independently new.

## Assumptions and scope

An associative bilinear form means a bilinear \(B\) satisfying \(B(xy,z)=B(x,yz)\) for all \(x,y,z\in A\); symmetry is not assumed. The rank is the rank of its \((n+m)\)-square Gram matrix in the path-length-at-most-one basis of \(A\). The arrow set is labeled: distinct parallel arrows are distinct summands in the support sum. The source and target of a loop coincide. Empty products and empty sets follow their usual conventions.

## Proof

**Reduction to functionals.** For every associative bilinear form \(B\) on the unital algebra \(A\), let \(\lambda(t)=B(1,t)\). Associativity yields \(B(x,y)=B(1,xy)=\lambda(xy)\), uniquely. Conversely any linear \(\lambda\) defines an associative bilinear form. Thus it suffices to count the ranks of \(B_\lambda\) as \(\lambda\) varies through \(A^*\).

**The Gram matrix.** The algebra has basis \(\{e_v:v\in Q_0\}\cup\{a:a\in Q_1\}\); its nonzero products between basis elements are \(e_ve_v=e_v\), \(e_{s(a)}a=a\), and \(ae_{t(a)}=a\). Relative to the ordered vertex-arrow basis,

\[
M_\lambda=\begin{pmatrix}D&U\\V&0\end{pmatrix},\qquad D=\operatorname{diag}(d_v),
\]
where column \(a\) of \(U\) is \(c_a e_{s(a)}\) and row \(a\) of \(V\) is \(c_a e_{t(a)}^{\mathsf T}\). Therefore \(\operatorname{im}U\) is exactly the coordinate subspace supported on \(S_F\). The equations for the right kernel are \(Dx+Uy=0\) and \(Vx=0\). The second equation is equivalent to \(x_v=0\) for every \(v\in T_F\). Modulo \(\operatorname{im}U\), the first equation is equivalent to \(d_vx_v=0\) for every \(v\notin S_F\). Hence there are exactly \(|T_F|+|\{v\notin S_F\cup T_F:d_v\ne0\}|\) independent conditions on \(x\); the adjustment variable \(y\) contributes the additional rank \(\dim\operatorname{im}U=|S_F|\). This proves the rank identity, without assuming any independence among the nonzero \(c_a\)'s beyond their support.

**Counting.** Fix an arrow support \(F\). Each coefficient \(c_a\) of an arrow in \(F\) has \(q-1\) choices, and all other arrow coefficients are zero. The \(d_v\)'s on \(S_F\cup T_F\) do not affect the rank and have \(q^{|S_F\cup T_F|}\) choices. For each uncovered vertex, \(d_v=0\) has weight \(1\), while the \(q-1\) nonzero possibilities have weight \(z\). Their product is \((1+(q-1)z)^{n-|S_F\cup T_F|}\). Summing over all supports proves the enumerator. Setting \(z=1\) gives \(q^{n+m}\), the number of functionals.

**Maximal rank.** For fixed \(F\), choosing each uncovered \(d_v\ne0\) makes the rank equal to \(n+|S_F\cap T_F|\). This is maximized by activating every arrow, yielding \(n+|S_{Q_1}\cap T_{Q_1}|\), and such activation is possible over every finite field.

**Frobenius boundary.** Full rank requires \(n+m=n+c\), where \(c=|S_{Q_1}\cap T_{Q_1}|\), so \(m=c\). As \(c\le |S_{Q_1}|\le m\) and \(c\le |T_{Q_1}|\le m\), equality forces every nonisolated vertex to have precisely one incoming and one outgoing arrow and no other vertices incident to arrows; this is a disjoint union of directed cycles and isolated vertices. Conversely such a quiver has \(m=c\), and full rank occurs precisely when all \(m\) arrow coefficients are nonzero and all \(n-c\) isolated-vertex coefficients are nonzero. The remaining \(c\) vertex coefficients are arbitrary, giving \(q^c(q-1)^n\). This also covers the zero-arrow semisimple case.

## Verification

The included standalone Python scripts construct the full multiplication-Gram matrix and calculate its row rank by field Gaussian elimination. The expected distribution is computed separately from support masks, without using the matrix-rank routine. `frob_rank_checker.py` exhaustively verifies 26 quiver-field instances over prime fields, including loops, parallel arrows, isolated vertices, chains, forks and cycles. `frob_gf4_checker.py` independently verifies five further instances over \(\mathbb F_4\), implementing multiplication modulo the irreducible polynomial \(t^2+t+1\). All cases passed. The accompanying output files record every comparison. These experiments are finite corroboration, not a substitute for the universal proof.

For example, for a three-vertex chain \(1\to2\to3\) and the outward fork \(1\leftarrow2\to3\), respectively, the polynomials over \(\mathbb F_2\) are

\[
1+3z+11z^2+9z^3+8z^4,\qquad 1+3z+11z^2+17z^3.
\]
These quivers have the same underlying undirected path and the same dimensions, but different maximal pairing ranks. For a directed three-cycle over \(\mathbb F_2\), the coefficient of \(z^6\) is \(8\), as predicted by the Frobenius count.

Reproduce using `python frob_rank_checker.py` and `python frob_gf4_checker.py` from the package's file directory. No external dependencies are required.

## Relationship to prior work

Xiao-Wu Chen's 2011 classification of radical-square-zero algebras addresses self-injectivity and Gorenstein behavior, including the oriented-cycle case. The 2013 work of Artenstein, González and Lanzilotta studies Frobenius and nearly Frobenius structures, particularly coproducts on quiver algebras. The present count concerns the ranks of **all** associative multiplication pairings, including degeneracies on algebras without any nondegenerate pairing; it is not a reproof of the known existence or unit-torsor criteria. Previously recorded exact commutator and ideal-counting invariants of radical-square-zero algebras have different hypotheses and outputs: the commutator statistic can be insensitive to arrow orientations distinguished by the present rank distribution. A general prior theorem giving the same entire rank enumerator has not been located. This is a bounded literature comparison, not proof of historical priority.

## Limitations

The formula assumes the split radical-square-zero path algebra \(kQ/J^2\), not arbitrary finite-dimensional quotients, non-split basic algebras, or higher radical powers. The form is associative but need not be symmetric. The sum over arrow subsets can be exponential in the number of arrows; no general polynomial-time evaluation algorithm is claimed. Full-text access to every historical classification source was not available, so originality remains provisional. Independent audit has not been conducted.

## References

1. Xiao-Wu Chen, *Algebras with radical square zero are either self-injective or CM-free*, Proceedings of the American Mathematical Society 140 (2012), 93–98; electronically published 2011-05-16; DOI: `10.1090/S0002-9939-2011-10921-3`.
2. Dalia Artenstein, Ana González, Marcelo Lanzilotta, *Constructing nearly Frobenius algebras*, first public preprint 2013-06-17, `arXiv:1306.3964`, https://arxiv.org/abs/1306.3964.
