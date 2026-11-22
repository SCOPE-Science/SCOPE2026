# The five rational lines and their Picard lattice on a binary space-filling K3 quartic

## Finding

For the smooth quartic \(X\subset\mathbb P^3_{\mathbb F_2}\) defined by \(X_1\phi_{01}+X_2\phi_{12}+X_3\phi_{23}+(X_0+X_3)\phi_{30}=0\), with \(\phi_{ij}=X_i^2X_j+X_iX_j^2\), its five \(\mathbb F_2\)-rational lines have incidence graph \(A_3\sqcup A_2\), with exactly three intersecting pairs. Their divisor classes together with the hyperplane class span a rank-six integral sublattice of \(\operatorname{NS}(X_{\overline{\mathbb F}_2})\) of discriminant \(-132\). Each of the five rational lines determines a basepoint-free pencil of residual plane cubics of arithmetic genus one, and each such pencil has a rational section furnished by a skew rational line (with respectively \(3,2,3,3,3\) available skew lines). These are refinements of an already known five-line count and do not assert saturation of the lattice or smoothness of generic fibers.

## Assumptions and scope

Work over \(k=\mathbb F_2\) in \(\mathbb P^3_k\), and set \(\phi_{ij}=X_i^2X_j+X_iX_j^2\). The surface \(X\) is the quartic \(F=0\), with
\[
F=X_1\phi_{01}+X_2\phi_{12}+X_3\phi_{23}+(X_0+X_3)\phi_{30}.
\]
The reference proves that \(X\) is geometrically smooth; alternatively this can be checked by the four projective Jacobian charts. Thus \(X\) is a K3 surface; its hyperplane class has square four, and every geometric line is a smooth rational \((-2)\)-curve by adjunction. All lines counted below are defined over \(\mathbb F_2\), not all geometric lines over its algebraic closure.

## Proof

**Exhaustive line classification.** For independent \(u,v\in k^4\), put \(p_{ij}=u_iv_j+u_jv_i\). In characteristic two, substituting \(su+tv\) gives
\[
F(su+tv)=(s^2t+st^2)\bigl(sA+tB\bigr),
\]
where
\[
A=u_1p_{01}+u_2p_{12}+u_3p_{23}+(u_0+u_3)p_{30},
\]
and \(B\) is the same expression with \(v\) in place of \(u\). Since this is a polynomial identity over the field (not merely a three-point evaluation), the entire projective line lies on \(X\) exactly when \(A=B=0\).

There are \(\binom{4}{2}\) reduced-row-echelon pivot patterns. Enumerating their free binary entries gives exactly 35 distinct two-dimensional subspaces of \(k^4\). The six pivot patterns, in lexicographic order, contribute \(3,1,0,0,1,0\) contained lines. The five resulting lines are precisely:

Let \(L_0,\ldots,L_4\) be the \(\mathbb F_2\)-lines spanned by the following pairs of points, using coordinates in order \(X_0X_1X_2X_3\):

| Line | Two spanning points |
|---|---|
| \(L_0\) | `1001`, `0101` |
| \(L_1\) | `1010`, `0111` |
| \(L_2\) | `1011`, `0110` |
| \(L_3\) | `1000`, `0010` |
| \(L_4\) | `0100`, `0001` |

The only intersecting pairs are \((L_0,L_4)\), \((L_1,L_2)\), and \((L_1,L_3)\). Their intersection points are respectively `0101`, `1101`, and `1010`. The intersection graph is thus the disjoint union of a two-vertex chain and a three-vertex chain, conventionally \(A_2\sqcup A_3\).

**Intersection lattice.** Any two distinct projective lines on smooth \(X\) have intersection product one if they meet and zero otherwise. On the smooth quartic, \(H^2=4\), \(H\cdot L_i=1\), and \(L_i^2=-2\) by adjunction (\(K_X=0\)). Consequently:

Writing \(H\) for a hyperplane section, the Gram matrix of \((H,L_0,L_1,L_2,L_3,L_4)\) is
\[
\begin{pmatrix}
4&1&1&1&1&1\\
1&-2&0&0&0&1\\
1&0&-2&1&1&0\\
1&0&1&-2&0&0\\
1&0&1&0&-2&0\\
1&1&0&0&0&-2
\end{pmatrix}.
\]
Its exact determinant is \(-132\), hence the six classes are independent and generate the asserted integral sublattice. No assertion of primitivity is made.

**Residual cubic pencils and rational sections.** For each \(L_i\), planes through \(L_i\) form a rational pencil, and their divisors on \(X\) are \(L_i+C_\lambda\), where \(C_\lambda\sim H-L_i\) has degree three and arithmetic genus one because \((H-L_i)^2=0\). There are no base points outside \(L_i\). A point on \(L_i\) is a common base point of the residual divisors only if both normal derivatives of \(F\) vanish there; the tangent derivative along \(L_i\) vanishes identically as \(F\) vanishes along the line. That would make \(X\) singular, a contradiction. Thus \(|H-L_i|\) is basepoint-free and defines a morphism \(X\to\mathbb P^1\). A skew line \(L_j\) satisfies \((H-L_i)\cdot L_j=1\), so its restriction to the base has degree one, giving a section defined over \(\mathbb F_2\). The incidence list gives respectively \(3,2,3,3,3\) skew rational lines for \(L_0,\ldots,L_4\). We do not claim the generic cubics are smooth; in characteristic two a quasi-elliptic phenomenon must be excluded separately if required.

## Verification

The companion `verify.py` uses only the Python standard library. Running `python verify.py` enumerates all 35 lines independently in unique reduced-row-echelon form, tests the two polynomial coefficients \(A,B\), checks every pairwise intersection and the lattice determinant exactly, and checks each section count. This exhausts only rational lines; it is not a geometric Fano-scheme enumeration.

## Relationship to prior work

Bourgeois-Conti, Moon, Perez and Warren construct this smooth space-filling binary quartic. Earlier work on the same source already counted five rational lines and independently computed arithmetic Picard rank six and geometric Picard rank ten. Neither numerical statement determines their incidence graph or the integral intersection matrix: for five rational \((-2)\)-curves, distinct graphs produce distinct Gram matrices and determinants. The contribution here is the explicit configuration, its discriminant and the associated rational-section pencils, not the five-line count, K3 smoothness or the Picard-rank computation.

## Limitations

Only \(\mathbb F_2\)-rational lines have been exhaustively enumerated. The rank-six lattice is not proved saturated in the full Néron-Severi group, its discriminant must not be misidentified with the full Néron-Severi discriminant, and no explicit Mordell-Weil rank, singular-fiber classification, or generic smoothness claim is made. The arithmetic Picard ranks cited as context are not re-proved here. An unindexed earlier geometric description remains a possible priority risk.

## References

- Bourgeois-Conti, Moon, Perez and Warren, *Space-Filling Hypersurfaces*, arXiv:2611.15768v1 (first public 2026-11-11), especially construction and smoothness arguments in §§3 and 9. https://arxiv.org/abs/2611.15768
- Veniani, *Lines on K3 quartic surfaces in characteristic 2*, arXiv:1606.02135 (2016), background on positive-characteristic line configurations. https://arxiv.org/abs/1606.02135
