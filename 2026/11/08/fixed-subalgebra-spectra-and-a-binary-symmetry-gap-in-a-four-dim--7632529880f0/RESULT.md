# Fixed-subalgebra spectra and a binary symmetry gap in a four-dimensional monomial algebra

## Finding
For every finite field \(k=\mathbb F_q\) with \(q=2^e\), \(e\ge1\), put
\[
A_q=k[x,y]/(x^2,y^2),\quad z=xy,\quad \mathfrak m=(x,y,z).
\]
For \(\phi\in\operatorname{End}_{k\text{-alg}}(A_q)\), write \(\operatorname{Fix}(\phi)=\{a:\phi(a)=a\}\). Its \(k\)-dimension is between one and four. Define \(E_d(q)\) as the number of unital endomorphisms whose fixed subalgebra has dimension \(d\); define \(G_d(q)\) similarly for automorphisms. Then
\[
\begin{aligned}
E_1(q)&=q^3(q^3-2q^2+2),\\
E_3(q)&=(q^2-1)(q+1),&E_4(q)&=1,\\
E_2(q)&=q^6-E_1(q)-E_3(q)-1;\\
G_1(q)&=q^3(q+1)(q-2)^2,\\
G_3(q)&=(q^2-1)(q+1),&G_4(q)&=1,\\
G_2(q)&=q^3(q-1)^2(q+1)-G_1(q)-G_3(q)-1.
\end{aligned}
\]
Every dimension occurs for endomorphisms. For automorphisms, all dimensions except \(d=1\) occur over \(\mathbb F_2\), whereas all dimensions occur over every larger characteristic-two field. Moreover, each dimension determines the fixed algebra's isomorphism type: for \(d=1\), it is \(k\); for \(d=2\), \(k[t]/(t^2)\); for \(d=3\), \(k[u,v]/(u,v)^2\); and for \(d=4\), \(A_q\).

The common fixed algebra under the entire automorphism group is \(\mathbb F_2\oplus\mathbb F_2z\) when \(q=2\), and the scalars alone when \(q>2\). The natural action of \(\operatorname{Aut}_{k\text{-alg}}(A_q)\) on \(A_q\) has exactly \(3q\) orbits.

## Assumptions and scope
All homomorphisms are unital and \(k\)-linear; \(q\) is any power of two, including nonprime fields. Equivalently, \(A_q\cong k[C_2\times C_2]\) via \(x=g-1\), \(y=h-1\) for commuting involutions \(g,h\). This supplies a canonical modular group-algebra motivation for the invariant problem. The algebra has basis \(1,x,y,z\), with \(x^2=y^2=0\), \(xy=z\), and \(xz=yz=z^2=0\). No semilinear maps, change of coefficient field, or arbitrary multiplicative set maps are counted. Counts refer to labeled endomorphisms, not conjugacy classes.

## Proof
**Normal form.** Every element of \(\mathfrak m\) squares to zero by characteristic two. Conversely an element with a nonzero scalar part has nonzero square. Hence images of \(x\) and \(y\) under any unital endomorphism can be chosen uniquely as
\[
\phi(x)=ax+cy+uz,\qquad \phi(y)=bx+dy+vz
\]
with arbitrary \(a,b,c,d,u,v\in k\). These images satisfy all defining relations, and \(\phi(z)=(ad+bc)z\). Therefore the matrix on \(\mathfrak m\) is
\[
M=\begin{pmatrix}a&b&0\\c&d&0\\u&v&\Delta\end{pmatrix},\qquad \Delta=ad+bc.
\]
In particular there are \(q^6\) endomorphisms, and exactly \(q^2|\mathrm{GL}_2(k)|=q^3(q-1)^2(q+1)\) are automorphisms; the latter formula is background group counting, not a separate novelty claim.

**Fixed-dimension stratification.** Put \(L=\begin{psmallmatrix}a&b\\c&d\end{psmallmatrix}\) and \(t=\dim_k\ker(L-I_2)\). As \(\phi(1)=1\), one has
\[
\dim_k\operatorname{Fix}(\phi)=4-\operatorname{rank}(M-I_3).
\]
If \(\Delta\ne1\), the bottom-right entry of \(M-I_3\) is nonzero and row reduction gives dimension \(1+t\), independent of \(u,v\). If \(\Delta=1\), let \(\ell:k^2\to k\) be \(\ell(s,t)=us+vt\); the dimension becomes
\[
2+t-\operatorname{rank}(\ell|_{\ker(L-I_2)}).
\]

The complete count follows from four disjoint types of \(2\times2\) matrices. For \(\Delta=1\): exactly one matrix \(L=I_2\) has \(t=2\); exactly \(q^2-1\) further matrices are nontrivial unipotents with \(t=1\); the remaining \(q(q^2-1)-q^2\) members of \(\mathrm{SL}_2(q)\) have \(t=0\). The nontrivial unipotents form one conjugacy class, of size \(q^2-1\). For \(\Delta\ne1\), \(t=1\) if and only if \(L\) is conjugate to \(\operatorname{diag}(1,\delta)\) with \(\delta\in k\setminus\{1\}\); there are \(q(q+1)\) such matrices per value \(\delta\). All other such matrices have \(t=0\). These observations also include singular matrices, where \(\delta=0\).

When \(L=I_2\), the zero functional \(\ell\) gives the identity endomorphism (dimension four), and the other \(q^2-1\) functionals give dimension three. For the \(q^2-1\) nontrivial unipotents, exactly \(q\) functionals annihilate the one-dimensional \(\ker(L-I_2)\); they yield dimension three, while the others yield dimension two. All other determinant-one cases give dimension two. Thus for both endomorphisms and automorphisms the dimension-three count is \((q^2-1)(q+1)\), and the dimension-four count is one.

For \(\Delta\ne1\), the matrices with \(t=0\) number
\[
q^4-q(q^2-1)-q(q+1)(q-1)=q^4-2q^3+2q
\]
when singular matrices are also allowed; multiplying by \(q^2\) choices for \(u,v\) gives \(E_1(q)\). Restricting to invertible matrices instead, the \(\Delta\ne1\), \(t=0\) count becomes \(q(q+1)(q-2)^2\), giving \(G_1(q)\). Subtracting the three known strata from the respective total counts proves the formulas for \(E_2\) and \(G_2\). No case is omitted.

**Algebra types.** Any fixed subalgebra is unital and local with residue field \(k\). Every element of its radical has square zero. In dimension two, this forces the dual-number algebra. Dimension three arises only with \(\Delta=1\) and a fixed radical spanned by \(z\) and a lift of a single line in \(\operatorname{span}(x,y)\), so its radical square vanishes; it is \(k[u,v]/(u,v)^2\). Dimension four means \(\phi\) is the identity. Dimension one is the scalar field.

**Common invariants and orbit count.** Varying \((u,v)\) in automorphisms forces any element fixed by every automorphism to have no \(x\) or \(y\) component. Its \(z\)-coefficient is fixed under all determinants in \(k^\times\) precisely when \(k^\times=\{1\}\), namely \(q=2\). Finally Burnside's lemma yields the element-orbit count
\[
\frac{G_1(q)q+G_2(q)q^2+G_3(q)q^3+G_4(q)q^4}{q^3(q-1)^2(q+1)}=3q.
\]
Equivalently, after fixing the scalar part, there are three orbits: zero radical element, nonzero socle element, and element with nonzero image in \(\mathfrak m/\mathfrak m^2\). This also proves the same count directly.

## Verification
The source programs \(\texttt{verify\_fixed.py}\) and \(\texttt{verify\_direct.py}\) use only the Python standard library. Running them with Python 3 returns \(\texttt{VERIFY\_OK\_FIXED}\) and \(\texttt{VERIFY\_OK\_DIRECT}\). The first exhaustively enumerates every six-parameter map over \(\mathbb F_2\), \(\mathbb F_4\), and \(\mathbb F_8\), computing fixed dimensions by finite-field elimination. The second evaluates the images of every individual algebra element for all maps over \(\mathbb F_2\) and \(\mathbb F_4\), without using matrix-rank formulas. Its census also checks the orbit count via Burnside's identity.

The resulting endomorphism distributions \((E_1,E_2,E_3,E_4)\) are \((16,38,9,1)\), \((2176,1844,75,1)\), and \((197632,63944,567,1)\) at \(q=2,4,8\). The corresponding automorphism distributions are \((0,14,9,1)\), \((1280,1524,75,1)\), and \((165888,59336,567,1)\). These finite experiments corroborate but do not replace the proof for arbitrary \(2^e\).

## Relationship to prior work
Díaz, Liendo, Manzano-Flores, and Regeta explicitly consider the same monomial ideal \((x^2,y^2)\) in Example 4.25 of arXiv:2408.02197, in the paper's characteristic-zero setting. Their theorem concerns automorphism-group structure and does not enumerate fixed subalgebras of individual finite-characteristic automorphisms or endomorphisms. In characteristic two the tangent group differs because every radical element squares to zero.

Díaz and Lucchini Arteche (arXiv:2409.15081) address reconstruction of finite monomial algebras from their automorphism groups, not this fixed-algebra spectrum. Kureš (arXiv:1209.0093) studies elements invariant under *all* automorphisms of selected quotients \(\mathbb F_2[x_1,\ldots,x_n]/\mathfrak m^{r+1}\); this differs both in quotient and in quantifier from counting fixed subalgebras of individual endomorphisms. Standard enumeration of \(\mathrm{GL}_2(\mathbb F_q)\) and its unipotent conjugacy class is used as a lemma, not claimed as new.

## Limitations
The result is restricted to the rank-two, exponent-two monomial algebra in characteristic two and to finite coefficient fields; it does not classify all finite-dimensional monomial rings or all conjugacy classes of their endomorphisms. It counts fixed-algebra dimensions and isomorphism types, not embeddings up to conjugacy. An unidentified general finite-field fixed-space theorem might imply the particular formulas; no independent audit or full literature-exhaustiveness certification is claimed.

## References
- R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197 (first public August 5, 2024), Introduction and Example 4.25. https://arxiv.org/abs/2408.02197
- R. Díaz, G. Lucchini Arteche, *Finite monomial algebras are determined by their automorphism group*, arXiv:2409.15081 (first public September 23, 2024), introduction and main theorem. https://arxiv.org/abs/2409.15081
- M. Kureš, *Finite dimensional factor algebras of \(\mathbb F_2[X_1,\ldots,X_n]\) and their fixed point subalgebras*, arXiv:1209.0093 (2012), Introduction and Propositions 3–5. https://arxiv.org/pdf/1209.0093
