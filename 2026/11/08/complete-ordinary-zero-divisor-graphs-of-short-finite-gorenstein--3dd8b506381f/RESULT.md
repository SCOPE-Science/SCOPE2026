# Complete ordinary zero-divisor graphs of short finite Gorenstein local rings

## Finding

**Theorem.** Let \((R,\mathfrak m,k)\) be a finite commutative local Artinian Gorenstein ring with \(\mathfrak m^3=0\ne\mathfrak m^2\), residue field \(k=\mathbb F_q\), and embedding dimension \(\dim_k(\mathfrak m/\mathfrak m^2)=2\). Write \(\Gamma(R)\) for the simple Anderson–Livingston graph on nonzero zero-divisors, with distinct vertices adjacent exactly when their product is zero.

Multiplication induces a nondegenerate symmetric bilinear form \(B\) on \(V=\mathfrak m/\mathfrak m^2\), valued in the one-dimensional space \(\mathfrak m^2\). Let \(t\) be the number of isotropic lines in the projective line \(\mathbb P(V)\), and put
\[
 u=q-1,\qquad s=q(q-1),\qquad b=\frac{q+1-t}{2}.
\]
Then, with \(\vee\) denoting graph join and \(\sqcup\) disjoint union,
\[
 \boxed{\Gamma(R)\cong K_u\vee\bigl(tK_s\sqcup bK_{s,s}\bigr).}
\]
The possible parameters are exactly
\[
 t=\begin{cases}
 0\text{ or }2,&q\text{ odd (anisotropic or split)},\\
 1\text{ or }q+1,&q\text{ even (nonalternating or alternating)}.
 \end{cases}
\]
Both possibilities in either characteristic are realized by finite local Gorenstein rings. Thus the ordinary zero-divisor graph is classified, within this ring family, by the pair \((q,t)\). More precisely, two such graphs are isomorphic if and only if these parameters agree.

The classification gives the following exact invariants:
\[
 |V(\Gamma)|=q^3-1,\qquad
 |E(\Gamma)|=\binom{u}{2}+u(q+1)s+t\binom{s}{2}+bs^2.
\]
The degree multiset comprises \(u\) vertices of degree \(q^3-2\), \(ts\) vertices of degree \(q^2-2\), and \(2bs\) vertices of degree \(q^2-1\), omitting a class if its multiplicity is zero. The clique number and chromatic number coincide:
\[
 \omega(\Gamma)=\chi(\Gamma)=\begin{cases}q+1,&t=0,\\q^2-1,&t>0.\end{cases}
\]
For an indeterminate \(X\), define the falling factorial \((X)_{\underline r}=X(X-1)\cdots(X-r+1)\), and let \(\left\{\begin{smallmatrix}s\\j\end{smallmatrix}\right\}\) be a Stirling number of the second kind. The entire chromatic polynomial is
\[
 P_\Gamma(X)=(X)_{\underline u}\,\bigl((X-u)_{\underline s}\bigr)^t
 \left(\sum_{j=1}^{s}\left\{\begin{smallmatrix}s\\j\end{smallmatrix}\right\}
 (X-u)_{\underline j}(X-u-j)^s\right)^b.
\]
Its graph automorphism group is the direct product of a symmetric group \(\mathfrak S_u\), the wreath product \(\mathfrak S_s\wr\mathfrak S_t\) when \(t>0\), and the wreath product \(((\mathfrak S_s\times\mathfrak S_s)\rtimes C_2)\wr\mathfrak S_b\) when \(b>0\); factors corresponding to zero component counts are omitted. These formulas describe the **graph** automorphisms, not necessarily automorphisms of the ring.

For completeness, the adjacency characteristic polynomial is equally explicit. Set \(\alpha=1\) when \(t>0\) and \(\alpha=0\) otherwise; set \(\beta=1\) when \(b>0\) and \(\beta=0\) otherwise. Define \(Q\) by starting with the \(1\times1\) entry \(u-1\), adding a row/column for the total clique-component cell when \(\alpha=1\) with entries \(Q_{0,C}=ts\), \(Q_{C,0}=u\), \(Q_{C,C}=s-1\), and adding a row/column for all biclique vertices when \(\beta=1\) with entries \(Q_{0,B}=2bs\), \(Q_{B,0}=u\), \(Q_{B,B}=s\). The two off-diagonal cells, when both present, are zero. Then
\[
 \begin{aligned}
 \det(\lambda I-A_\Gamma)={}&(\lambda+1)^{u-1+t(s-1)}
 (\lambda-(s-1))^{\max(t-1,0)}\\
 &\cdot(\lambda-s)^{\max(b-1,0)}(\lambda+s)^b
 \lambda^{2b(s-1)}\det(\lambda I-Q).
 \end{aligned}
\]

## Assumptions and scope

A finite local ring has precisely \(\mathfrak m\) as its zero-divisor set, so the graph vertices are \(\mathfrak m\setminus\{0\}\). In the hypotheses, Gorenstein means its socle \(\operatorname{ann}_R(\mathfrak m)\) is one-dimensional over \(k\). Since \(0\ne\mathfrak m^2\subseteq\operatorname{ann}_R(\mathfrak m)\), the two are equal; and \(\dim_k\mathfrak m^2=1\). These conditions imply the Hilbert function \((1,2,1)\), not an assumption that \(R\) is an equicharacteristic or graded \(k\)-algebra. All finite prime powers, including characteristic two, are included.

## Proof

**1. The multiplication form.** Choose a generator \(z\) of \(\mathfrak m^2\) as a one-dimensional \(k\)-space. For \(x,y\in\mathfrak m\), the product lies in \(\mathfrak m^2\) and depends only on \(\bar x,\bar y\in\mathfrak m/\mathfrak m^2\), because \(\mathfrak m^3=0\). The product is bilinear over \(R/\mathfrak m\), hence yields \(xy=B(\bar x,\bar y)z\) for a symmetric \(k\)-bilinear form \(B\). If \(B(\bar x,-)=0\), then \(x\mathfrak m=0\), so \(x\in\operatorname{Soc}R=\mathfrak m^2\), giving \(\bar x=0\); thus \(B\) is nondegenerate. In particular, \(|\mathfrak m|=q^3\), \(|\mathfrak m^2|=q\), and \(|V|=q^2\).

**2. Exact graph decomposition.** All \(q-1=u\) nonzero elements of \(\mathfrak m^2\) multiply to zero with every element of \(\mathfrak m\). They give the universal clique \(K_u\). Each one-dimensional subspace \(L\le V\) has \(q-1\) nonzero vectors, each with exactly \(q\) lifts through \(\mathfrak m^2\); hence its inverse-image cell \(C_L\subset\mathfrak m\setminus\mathfrak m^2\) has \(s=q(q-1)\) vertices. Cells \(C_L,C_M\) are completely adjacent if and only if \(B(L,M)=0\). The nondegenerate form assigns a unique perpendicular line \(L^\perp\) to each \(L\) and \((L^\perp)^\perp=L\). Each fixed line (an isotropic line) gives a clique \(K_s\). Each two-cycle of the perpendicular involution yields a \(K_{s,s}\): all cross edges exist, and within either of its nonisotropic lines no edge exists. No other edges occur between cells. Since there are \(q+1\) projective lines, there are \(t\) fixed lines and \(b=(q+1-t)/2\) two-cycles, proving the claimed graph decomposition.

**3. Isotropic line counts.** In odd characteristic, a nondegenerate binary symmetric form is either anisotropic, giving no isotropic projective line, or contains an isotropic vector. In the latter case choose a vector paired nontrivially with it, then replace that vector by a suitable scalar multiple of the first to obtain a hyperbolic basis; the two coordinate lines are precisely the isotropic lines. Hence \(t=0\) or \(t=2\). In characteristic two, an alternating form has \(B(v,v)=0\) for every \(v\), hence \(t=q+1\). For a nonalternating form, the function \(v\mapsto B(v,v)\) is a nonzero square of a linear functional on \(k^2\), since finite fields are perfect and cross terms cancel in characteristic two; it therefore vanishes on precisely one projective line, giving \(t=1\). All four possibilities are realized by nonsingular binary Gram matrices: hyperbolic, nonsplit diagonal (odd characteristic), and alternating/nonalternating matrices (even characteristic). The corresponding multiplication table defines the finite split local ring \(k\oplus V\oplus kz\) with \(V\cdot V=B(V,V)z\), \(z\mathfrak m=0\), proving realizability.

**4. Isomorphism and numerical invariants.** The decomposition implies the vertex, edge, and degree formulas by counting a universal clique, its cross edges, internal clique edges, and complete-bipartite edges. Every non-socle vertex has degree strictly less than \(q^3-2\); hence the \(u\) universal vertices are identifiable in the graph. From \(|V|=q^3-1\), graph isomorphism recovers \(q\), and from the \(q^2-2\) degree multiplicity it recovers \(t\), since \(s=q(q-1)\). Conversely, equal \((q,t)\) give identical decompositions. Components outside the universal clique are all complete or complete bipartite and hence perfect. Their disjoint union, joined with a clique, is perfect, so \(\chi=\omega\). If \(t>0\), the largest component clique has size \(s\) (a biclique's largest clique has size only \(2\)), giving \(u+s=q^2-1\); for \(t=0\), the largest clique outside the universal part has size two, giving \(u+2=q+1\). Here \(s\ge2\), so boundaries also hold for \(q=2\).

**5. The chromatic polynomial and automorphisms.** Choose distinct colors for the \(u\) universal vertices in \((X)_{\underline u}\) ways, and color each remaining connected component with the other \(X-u\) colors. A clique \(K_s\) has polynomial \((X-u)_{\underline s}\). To color \(K_{s,s}\), choose exactly \(j\) distinct colors on one part: partition that part into \(j\) nonempty color classes in \(\left\{\begin{smallmatrix}s\\j\end{smallmatrix}\right\}\) ways, then injectively assign \(j\) colors in \((X-u)_{\underline j}\) ways, and finally give each vertex in the other part one of the remaining \(X-u-j\) colors. This proves the chromatic polynomial. Any graph automorphism preserves the universal clique and permutes connected components of the residual graph. Cliques \(K_s\) and bicliques \(K_{s,s}\) are distinct connected graph types for \(s\ge2\). Their internal automorphism groups and identical-component permutations give the stated wreath products.

**6. Spectral formula.** Within the universal clique, vectors of coordinate sum zero give eigenvalue \(-1\) with multiplicity \(u-1\); within the \(t\) cliques, internal sum-zero vectors give \(-1\) with total multiplicity \(t(s-1)\). Differences of clique-component constants give eigenvalue \(s-1\), multiplicity \(t-1\) when \(t>0\). Each biclique contributes its anti-constant mode of eigenvalue \(-s\) and \(2(s-1)\) internal zero modes. Differences between its symmetric component constants give eigenvalue \(s\) with multiplicity \(b-1\), when \(b>0\). The remaining subspace consists of constants on the nonempty blocks (the universal vertices, all clique-component vertices, all biclique vertices); the adjacency action on it is the explicitly defined quotient matrix \(Q\). All displayed invariant subspaces form a direct sum of the total vertex space, proving the characteristic-polynomial factorization, including cases \(t=0\) and \(b=0\).

**7. Graphs do not recover the ring.** For any prime \(p\), the two finite local Gorenstein rings \(\mathbb F_p[x,y]/(x^2,y^2)\) and \((\mathbb Z/p^2\mathbb Z)[t]/(t^2)\) have Hilbert function \((1,2,1)\) and split hyperbolic multiplication forms on their two-dimensional radical quotients. Their ordinary zero-divisor graphs are therefore isomorphic by the theorem. They are not isomorphic rings, since their characteristics are \(p\) and \(p^2\), respectively.

## Verification

The included `checker.py` builds the exact nonzero-radical element graph by finite-field bilinear multiplication for all nonsingular symmetric rank-two form types over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8\). It independently counts edges, vertex degrees, and the connected component structures after removing the nonzero socle. Twelve field/form configurations, totaling 2,146 enumerated graph vertices, pass. A separate explicit multiplication check in \((\mathbb Z/p^2\mathbb Z)[t]/(t^2)\), for \(p=2,3\), verifies the mixed-characteristic example. Direct proper-color backtracking over the two seven-vertex binary graphs checks the chromatic polynomial for one through five colors. In four additional graph cases, an exact-integer Faddeev–LeVerrier characteristic-polynomial computation independently verifies the full adjacency characteristic-polynomial factorization (both types over fields of orders two and three). The recorded output ends `VERIFY_COMPLETE_OK`. These finite checks support, but do not replace, the unrestricted proof.

Run `python3 checker.py` with Python 3 standard library only. The complete recorded output is in `checker_output.txt`.

## Relationship to prior work

Kadu's 2021 article (Proposition 3.6) *already establishes* the multiplication/orthogonality criterion for Artinian local rings with principal nonzero square of the maximal ideal and cube zero, including the equivalence between Gorenstein and nondegenerate induced bilinear form. **Neither that criterion nor its proof is claimed as new.** The 2026 paper of Kadu and Tanpure compares ordinary, annihilator-compressed and associate-class graphs of Gorenstein rings and establishes Gorenstein detection by comparing the latter two. Its graph invariants concern a distinct comparison problem. The finding here instead supplies the full **ordinary uncompressed graph isomorphism classification** for the two-generator short local Gorenstein family, together with its exact chromatic polynomial, full graph automorphism group, spectral factorization, and a mixed-characteristic non-reconstruction family.

The 2012 zero-divisor graph survey by Coykendall, Sather-Wagstaff, Sheppardson and Spiroff establishes broad graph-theoretic background. No searched source was found stating the full present classification and its enumerative consequences. These searches do not establish historical uniqueness; an implicit equivalent classification in older local-ring/orthogonal-graph literature remains possible.

## Limitations

The hypotheses \(\dim_k\mathfrak m/\mathfrak m^2=2\), \(\mathfrak m^3=0\ne\mathfrak m^2\), Gorenstein and finite residue field are essential for the stated decomposition. No result is asserted for embedding dimension three or higher, non-Gorenstein rings, infinite residue fields, or other ring-based graphs. The formulas concern **graph** automorphisms, not the ring automorphism group. The prior bilinear-form correspondence is known; independent expert assessment of historical priority and non-routineness is outstanding.

## References

1. G. S. Kadu and V. Tanpure, *Zero Divisors of Gorenstein Rings*, arXiv:2609.36021 (first public 2026-09-28), https://arxiv.org/abs/2609.36021.
2. G. S. Kadu, *On the problem of zero-divisors in Artinian rings*, Communications in Algebra 49 (2021), 4957–4969, DOI:10.1080/00927872.2021.1933998; Proposition 3.6.
3. J. Coykendall, S. Sather-Wagstaff, L. Sheppardson, S. Spiroff, *On Zero Divisor Graphs*, in Progress in Commutative Algebra 2 (2012), 241–299.
4. D. F. Anderson and P. S. Livingston, *The zero-divisor graph of a commutative ring*, Journal of Algebra 217 (1999), 434–447.
