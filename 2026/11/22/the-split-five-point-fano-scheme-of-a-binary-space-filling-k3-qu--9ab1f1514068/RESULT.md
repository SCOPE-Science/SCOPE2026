# The split five-point Fano scheme of a binary space-filling K3 quartic

## Finding
Let \(k=\mathbb F_2\), let \(\phi_{ij}=X_i^2X_j+X_iX_j^2\), and let the smooth quartic \(X\subset\mathbb P^3_k\) be defined by
\[
F=X_1\phi_{01}+X_2\phi_{12}+X_3\phi_{23}+(X_0+X_3)\phi_{30}=0.
\]
The **complete scheme of projective lines** on \(X\) is the finite étale, split scheme
\[
\boxed{F_1(X)\cong\coprod_{j=1}^{5}\operatorname{Spec}(\mathbb F_2).}
\]
Thus all five geometric lines are defined over \(\mathbb F_2\); in particular, **there are no additional lines over any extension**. For every integer \(r\ge1\),
\[
\#F_1(X)(\mathbb F_{2^r})=5,
\qquad Z(F_1(X),T)=(1-T)^{-5}.
\]
In the original homogeneous coordinates the five lines are
\[
\begin{aligned}
&X_2=0,\ X_3=X_0+X_1;\qquad
X_2=X_0+X_1,\ X_3=X_1;\\
&X_2=X_0+X_1,\ X_3=X_0;\qquad
X_1=X_3=0;\qquad X_0=X_2=0.
\end{aligned}
\]
These are equations of five distinct embedded lines, not merely a point count on the Grassmannian.

## Assumptions and scope
All scheme statements are over \(\mathbb F_2\); geometric points are taken over \(\overline{\mathbb F}_2\). The quartic is the \(q=2,b=1\) specialization of the smooth characteristic-two surface in Bourgeois-Conti–Moon–Perez–Warren, Section 9, Lemma 9.2. We use the usual Grassmannian \(\operatorname{Gr}(2,4)\) and its six disjoint row-reduced echelon (RREF) **Schubert cells**. These cells enumerate geometric lines, but are not all open neighborhoods in the Grassmannian; reducedness of the complete line scheme will be proved separately by adjunction. Smoothness is established by that source; the line-scheme computation below does not use smoothness as a shortcut to counting points.

## Proof
A two-dimensional vector subspace of \(k^4\) has a unique RREF \(2\times4\) matrix with ordered pivot columns \((a,b)\), where \(0\le a<b\le3\). In the RREF cell \((a,b)\), put \(1\) at positions \((0,a),(1,b)\) and free variables at the non-pivot positions strictly to the right of the pivot in each row. The admissible free positions are therefore
\[
\bigl\{(i,j):i\in\{0,1\},\ j>p_i,\ j\notin\{a,b\}\bigr\},\qquad (p_0,p_1)=(a,b).
\]
Write the two RREF rows \(A,B\). The corresponding line is contained in \(X\) if and only if all five coefficients of the binary quartic \(F(sA+tB)\) vanish identically in characteristic two. The five coefficient polynomials cut out the line condition on this RREF cell. The cells classify all geometric lines; we do not identify them with open Grassmannian charts.

Use variable order \(v_0>\cdots>v_{h-1}\) for the \(h\) free entries, and lexicographic Gröbner reduction over \(\mathbb F_2\). Direct coefficient extraction and reduction give the following **full chart ideals**, written by their reduced Gröbner generators:

| RREF pivot chart | Free variables | Reduced Gröbner generators |
|---|---|---|
| \((0,1)\) | \(v_0,v_1,v_2,v_3\) | \(v_0+v_2,\ v_1+v_2+v_3,\ v_2^2+v_2,\ v_2v_3+v_2+v_3+1,\ v_3^2+v_3\) |
| \((0,2)\) | \(v_0,v_1,v_2\) | \(v_0,v_1,v_2\) |
| \((0,3)\) | \(v_0,v_1\) | \(1\) |
| \((1,2)\) | \(v_0,v_1\) | \(1\) |
| \((1,3)\) | \(v_0\) | \(v_0\) |
| \((2,3)\) | none | \(1\) |

The \((0,1)\) RREF-cell algebra is therefore
\[
\frac{\mathbb F_2[v_2,v_3]}
{(v_2^2+v_2,\ v_3^2+v_3,\ (v_2+1)(v_3+1))}
\cong\mathbb F_2\times\mathbb F_2\times\mathbb F_2,
\]
because the admissible ordered pairs are precisely \((v_2,v_3)=(0,1),(1,0),(1,1)\). The \((0,2)\) and \((1,3)\) RREF cells each have one point, and the other three cells have no points. Unique RREF matrices cover the lines over **every field extension**, including the algebraic closure. Hence the complete Fano scheme has exactly five geometric points, all with field of definition \(\mathbb F_2\).

In cell \((0,1)\), the two rows are \((1,0,v_0,v_1)\) and \((0,1,v_2,v_3)\). The Gröbner equations therefore give \(X_2=v_2(X_0+X_1)\) and \(X_3=(v_2+v_3)X_0+v_3X_1\). The first three lines displayed above correspond respectively to \((v_2,v_3)=(0,1),(1,1),(1,0)\). The other two have all free entries zero in cells \((0,2)\) and \((1,3)\).

It remains essential to prove that the **full** Grassmannian line scheme has no nilpotent thickening near these points: RREF cells alone do not suffice for that. Let \(L\) be any of these lines. Since \(X\) is smooth of degree four, adjunction gives \(K_X\cong\mathcal O_X\), so on the smooth rational curve \(L\) we have \(L^2=-2\). Thus its normal bundle in \(X\) is \(N_{L/X}\cong\mathcal O_{\mathbb P^1}(-2)\). The Zariski tangent space to \(F_1(X)\) at \([L]\) is \(H^0(L,N_{L/X})=0\). A finite-type scheme over a perfect field whose geometric points are finite and whose tangent spaces vanish at every geometric point is finite étale. This proves reducedness and the split scheme assertion. The listed line equations come from the five RREF matrices.

Since the scheme is the constant union of five rational points, extension-field counts are five for every degree and the displayed zeta function follows directly from its definition.

## Verification
The complete standalone file `check_fano.py` independently constructs \(F\), enumerates **all six** pivot charts, extracts the five coefficient polynomials of \(F(sA+tB)\), computes exact characteristic-two lexicographic Gröbner bases, and asserts agreement with every displayed generator. Running `python check_fano.py` with SymPy prints five RREF-cell points and terminates with `PASS`. This is exact symbolic elimination over \(\mathbb F_2\), not finite-field point sampling. The geometric-point census comes from the cell ideals; reducedness of the **entire line Hilbert scheme** follows from the normal-bundle tangent-space argument above.

## Relationship to prior work
Bourgeois-Conti, Moon, Perez and Warren [1] establish this explicit quartic and its geometric smoothness. Related calculations establish the five \(\mathbb F_2\)-rational lines and their incidence on this same quartic [3], or its rational-line count in coordinate-equivalent form [4]. Those rational counts do not rule out lines appearing over larger fields. The distinct assertion here is geometric exhaustion; together with rigidity of lines on a smooth quartic, it gives the split finite étale line scheme. The general coefficient-vanishing construction [2] does not by itself supply this census. These comparisons do not establish publication priority.

## Limitations
This statement is for this one explicit smooth space-filling quartic, not for all quartics over \(\mathbb F_2\) or the higher-dimensional inductive family. It does not determine the full geometric Picard group, the saturation of the known line lattice, or the behavior of curves of higher degree. A priority check cannot exhaust unindexed or unpublished calculations. The computational certificate depends on a correct implementation of exact Gröbner reduction, and the precise six displayed chart ideals make this independently reproducible.

## References
1. V. Bourgeois-Conti, H.-B. Moon, E. Perez and A. Warren, *Space-Filling Hypersurfaces*, arXiv:2611.15768v1 (first posted November 11, 2026), especially Sections 2, 7 and 9, https://arxiv.org/html/2611.15768v1.
2. Macaulay2 Documentation, *Tutorial: Fano varieties*, general scheme-theoretic method by coefficient vanishing, https://macaulay2.com/doc/Macaulay2/share/doc/Macaulay2/Macaulay2Doc/html/___Tutorial_co_sp__Fano_spvarieties.html.
3. *The five rational lines and their Picard lattice on a binary space-filling quartic*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-the-five-rational-lines-and-their-picard-lattice-on-a-binary-spa--7fca5e0ad7be.
4. *Exact rational-line counts for an inductive family of smooth binary space-filling hypersurfaces*, https://github.com/Resultary/2026/tree/main/2026/11/22/SCOPE-exact-rational-line-counts-for-an-inductive-family-of-smooth-bin--d08a7f779e4e.
