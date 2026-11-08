# Zariski-chamber support polynomial of the maximally nodal cubic resolution

## Finding
Let \(X\) be the blow-up of \(\mathbb P^2_{\mathbb C}\) in the six distinct intersection points of four projective lines in general position (no three concurrent). Equivalently, \(X\) is the minimal resolution of the four-nodal Cayley cubic surface, whose singularity configuration is \(4A_1\). The Zariski-chamber polynomial, in which the exponent counts the number of irreducible components supporting the negative part, is exactly
\[
Z_X(t)=1+13t+69t^2+186t^3+260t^4+168t^5+29t^6.
\]
Thus \(X\) has exactly \(726\) Zariski chambers, and precisely \(29\) have the maximum possible support size of six. Of these \(726\) chambers, exactly \(393\) have a negative support containing one of the three strict transforms of the diagonal lines of the complete quadrilateral; the remaining \(333\) do not.

A more structural statement gives the polynomial without matrix enumeration. Let \(K_4\) denote the graph on four vertices, let \(G\) range over all its labeled spanning subgraphs, and put \(e(G)=|E(G)|\). Let \(b(G)\) be the number of isolated-edge components of \(G\), and let \(f(G)\) be the number of vertices of degree at most one which are not endpoints of such isolated-edge components. Let \(r(G)\) be the number of perfect matchings of \(K_4\) having no edge in \(G\). Then
\[
Z_X(t)=\sum_{G\subseteq K_4}t^{e(G)}(1+r(G)t)(1+t)^{f(G)}(1+2t)^{b(G)}.
\]
Both equalities are exact over \(\mathbb C\).

## Assumptions and scope
Choose four distinct complex projective lines \(L_0,L_1,L_2,L_3\) such that no three pass through one point. Denote their intersections by \(p_{ij}=L_i\cap L_j\) for \(0\le i<j\le3\). Let \(\pi:X\to\mathbb P^2\) be the simultaneous blow-up of these six distinct points. Write \(H\) for the pulled-back class of a line and \(E_{ij}\) for the six exceptional curves. The intersection form is \(H^2=1\), \(H\cdot E_{ij}=0\), \(E_{ij}^2=-1\) and \(E_{ij}\cdot E_{kl}=0\) for distinct pairs.

For each \(i\), the strict transform \(D_i=H-\sum_{j\ne i}E_{\min(i,j),\max(i,j)}\) has self-intersection \(-2\). The three diagonal strict transforms are \(R_{01|23}=H-E_{01}-E_{23}\), \(R_{02|13}=H-E_{02}-E_{13}\), and \(R_{03|12}=H-E_{03}-E_{12}\); each has self-intersection \(-1\). The reduced negative curves are exactly these thirteen curves: the six \(E_{ij}\), three \(R\), and four \(D_i\).

A Zariski chamber means a chamber of the big cone classified by the support of the negative part of the Zariski decomposition. The empty support is counted once (the nef chamber). The result is about the smooth resolution, not the Weil-divisor cone of the singular cubic itself; no claim is made about chamber volumes, walls, or Cox-ring presentations.

## Proof
**1. Exhaustiveness of the negative curves.** The anticanonical class is \(-K_X=3H-\sum_{i<j}E_{ij}\), and the strict transforms of the four initial lines satisfy \(\sum_iD_i=4H-2\sum_{i<j}E_{ij}\). Consequently \(-K_X=H+\frac12\sum_iD_i\). For an irreducible curve other than one of the \(D_i\), intersection with \(H\) and with each \(D_i\) is nonnegative; each \(D_i\) has \((-K_X)\cdot D_i=0\). Thus \(-K_X\) is nef and \((-K_X)^2=3\).

If \(C\) is irreducible with \(C^2<0\), adjunction gives \(C^2+K_X\cdot C=2p_a(C)-2\ge-2\), while \(-K_X\cdot C\ge0\). Parity and integrality force either \((C^2,-K_X\cdot C)=(-1,1)\) or \((-2,0)\). If \(C\) is not exceptional, its plane image has degree \(d\ge1\) and nonnegative point multiplicities \(m_{ij}\). For a \((-1)\)-curve, the equations are
\[
\sum m_{ij}=3d-1,\qquad\sum m_{ij}^2=d^2+1.
\]
The Cauchy inequality \((3d-1)^2\le6(d^2+1)\) forces \(d\le2\). When \(d=1\), precisely two multiplicities are one: there are fifteen pair-lines, but twelve pairs share one of the four original lines, whose strict transform is a \((-2)\)-curve. Only the three pairs of disjoint edges of \(K_4\) yield new irreducible \((-1)\)-curves. When \(d=2\), five multiplicities are one; any five edges of \(K_4\) contain three edges incident to a common vertex, so five base points include three collinear points. An irreducible conic cannot pass through these three points by Bezout. The six exceptional curves account for the \(d=0\) case.

For a \((-2)\)-curve, the equations become \(\sum m_{ij}=3d\) and \(\sum m_{ij}^2=d^2+2\), hence \(9d^2\le6(d^2+2)\) and \(d\le2\). Degree one requires exactly three base points on a line, yielding the four \(D_i\). Degree two requires a conic through all six vertices of the complete quadrilateral, but any such conic would contain each initial line (it passes through its three nodes), which is impossible for degree two. This proves the asserted list of thirteen.

**2. Reducing negative-definite supports to graphs.** A negative-definite support cannot contain two distinct \((-1)\)-curves meeting once, because their two-by-two intersection matrix would be singular. Distinct diagonal curves \(R\) meet once. Each \(R_{ij|kl}\) meets precisely the exceptional curves \(E_{ij}\) and \(E_{kl}\), and is disjoint from all four \(D_i\). Consequently, for a chosen exceptional subset \(G\subseteq E(K_4)\), a support contains either no diagonal curve or exactly one of the \(r(G)\) diagonals whose endpoints are absent from \(G\). This contributes \(1+r(G)t\).

The four \((-2)\)-curves \(D_i\) are pairwise disjoint. An exceptional curve \(E_{ij}\) meets exactly \(D_i\) and \(D_j\), once each. For a chosen vertex set \(W\subseteq V(K_4)\), the intersection matrix of these selected \(D_i\) together with the selected exceptional curves has block form
\[
\begin{pmatrix}-I&B^{\mathsf T}\\ B&-2I\end{pmatrix},
\]
where \(B\) is the vertex-edge incidence matrix, restricted to \(W\) and \(G\). It is negative definite exactly when \(2I-BB^{\mathsf T}\) is positive definite. Its diagonal entries are \(2-\deg_G(i)\) and, for distinct \(i,j\), its off-diagonal entry is \(-1\) exactly when \(ij\in G\). Hence all selected vertices must have degree zero or one in \(G\), and both endpoints of an isolated edge cannot be selected simultaneously: otherwise their principal two-by-two submatrix is singular. Conversely these two conditions make the Schur complement diagonal and strictly positive, so they are sufficient.

The permitted choices of \(W\) thus give \((1+t)^{f(G)}(1+2t)^{b(G)}\). Multiplying by \(t^{e(G)}\) for the exceptional curves and by \(1+r(G)t\) for the optional diagonal gives the claimed graph sum. No other negative-definite supports exist.

**3. Exact evaluation.** Enumerate the sixty-four labeled subgraphs of \(K_4\) by their eleven isomorphism classes. The ordered triples \((e(G),\text{number of labeled graphs},r(G))\) are
\[
(0,1,3), (1,6,2), (2,12,1), (2,3,2), (3,4,0),
(3,4,0), (3,12,1), (4,12,0), (4,3,1), (5,6,0), (6,1,0).
\]
In the same order, the corresponding permitted-vertex polynomials are
\[
(1+t)^4,\quad (1+t)^2(1+2t),\quad (1+t)^3,\quad(1+2t)^2,
\quad(1+t)^3,\quad1+t,\quad(1+t)^2,\quad1+t,\quad1,\quad1,\quad1.
\]
Inserting these eleven terms in the graph sum gives \(1+13t+69t^2+186t^3+260t^4+168t^5+29t^6\). The coefficients sum to \(726\). Exactly \(393\) supports contain one diagonal, from the terms weighted by \(r(G)t\); the other \(333\) do not. The degree-six coefficient is \(29\), and the degree-seven coefficient vanishes. These arithmetic statements can be reproduced exactly from the standalone certificate.

## Verification
Run the bundled Python files (standard library only) by `python verify_exhaustive.py` and `python verify_graph.py`. The first reconstructs the thirteen divisor classes in the intersection lattice, iterates all \(2^{13}=8192\) subsets, and uses exact rational \(LDL^{\mathsf T}\) elimination to determine negative definiteness. The second independently enumerates the sixty-four graph subsets, groups them into eleven isomorphism classes, and expands the graph formula. Both give the same seven coefficients and total. Their actual outputs are included in `verification_output.txt`.

Finite enumeration is exhaustive here because step 1 proves there are exactly thirteen negative irreducible curves; it does not purport to certify any general claim about arbitrary cubic surfaces.

## Relationship to prior work
Bauer--Funke--Neumann [1, Proposition 1.1] establish the correspondence between chambers and negative-definite reduced supports and [1, Section 3] compute the counts for smooth del Pezzo surfaces. In particular, their smooth cubic count is \(2764\), not the four-nodal result above. Derenthal--Hausen--Heim--Keicher--Laface [2, Theorem 3.1, type \(4A_1\)] give the Cox ring and the classical count of nine lines for the Cayley cubic resolution, but no Zariski-chamber support distribution. Their thirteen Cox-ring generators are not asserted to be a chamber count. The present claim supplies the complete count and the graph-theoretic support formula for the maximally nodal case. No uniqueness of historical priority beyond the consulted evidence is asserted.

## Limitations
The classification uses four lines with no triple intersection over \(\mathbb C\), and concerns their smooth blow-up. It does not transfer automatically to positive characteristic or other ADE configurations, and it does not calculate volumes or wall adjacencies. The finite enumeration is exhaustive conditional on the negative-curve classification, which is proved geometrically here. A specialized older table for weak del Pezzo surfaces could conceivably contain this count, despite the negative targeted searches.

## References
[1] T. Bauer, M. Funke and S. Neumann, *Counting Zariski chambers on Del Pezzo surfaces*, arXiv:0912.0958v1 (public 2009-12-04), https://arxiv.org/abs/0912.0958.

[2] U. Derenthal, J. Hausen, A. Heim, S. Keicher and A. Laface, *Cox rings of cubic surfaces and Fano threefolds*, arXiv:1409.0799 (first public 2014-09-02), https://arxiv.org/abs/1409.0799.
