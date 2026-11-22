# Complete ideal-dimension polynomials for three-block nilpotent radicals with a nontrivial middle layer

## Finding
Let \(q\) be any prime power and \(a,c\geq1\), \(b\geq2\) integers. Let \(J_{a,b,c}(q)\) be the nonunital associative algebra of strictly upper three-block matrices over \(\mathbb F_q\), with diagonal block sizes \((a,b,c)\). Its elements are triples \((X,Y,Z)\), with \(X\in\operatorname{Mat}_{a\times b}\), \(Y\in\operatorname{Mat}_{b\times c}\), \(Z\in\operatorname{Mat}_{a\times c}\), and multiplication
\[
(X,Y,Z)(X',Y',Z')=(0,0,XY').
\]
All ideals below are \(\mathbb F_q\)-linear **two-sided ideals of this nonunital radical**, not ideals of the encompassing unital parabolic algebra.

The polynomial \(F_{a,b,c;q}(t)=\sum_{I\triangleleft J_{a,b,c}(q)}t^{\dim_{\mathbb F_q} I}\) has the following complete explicit expression. Let \(\genfrac{[}{]}{0pt}{}{n}{j}_q\) be the Gaussian coefficient (zero for inadmissible \(j\)) and put
\[
\begin{aligned}
 M_d(\ell,r;q)
 &=\sum_{i=0}^{\ell}\sum_{j=0}^{r}
 (-1)^{\ell-i+r-j}q^{\binom{\ell-i}{2}+\binom{r-j}{2}}
 \genfrac{[}{]}{0pt}{}{\ell}{i}_q
 \genfrac{[}{]}{0pt}{}{r}{j}_q
 \genfrac{[}{]}{0pt}{}{b(i+j)}{d}_q,\\
 h(\ell,r)&=c\ell+ar-\ell r.
\end{aligned}
\]
Then
\[
\boxed{\begin{aligned}
F_{a,b,c;q}(t)
={}&\sum_{\ell=0}^{a}\sum_{r=0}^{c}
\genfrac{[}{]}{0pt}{}{a}{\ell}_q
\genfrac{[}{]}{0pt}{}{c}{r}_q
\sum_{d=0}^{b(\ell+r)}M_d(\ell,r;q)\\
&\qquad\cdot\sum_{e=h(\ell,r)}^{ac}
\genfrac{[}{]}{0pt}{}{ac-h(\ell,r)}{e-h(\ell,r)}_q
q^{d(ac-e)}t^{d+e}.
\end{aligned}}
\]
For every admissible choice of parameters, each coefficient is exactly the number of embedded two-sided ideals of that dimension; no classification up to automorphisms or restriction to coordinate-supported ideals is imposed. The formula is valid in all characteristics.

For instance, at \((a,b,c,q)=(2,2,1,2)\) the radical has dimension \(8\) and
\[
F_{2,2,1;2}(t)=1+3t+19t^2+75t^3+651t^4+1395t^5+651t^6+63t^7+t^8,
\]
so it has exactly \(2859\) two-sided ideals. At field order \(3\), the same block shape has exactly \(56721\) ideals.

## Assumptions and scope
The ground field is any \(\mathbb F_q\), including fields of characteristic \(2\). The outer sizes satisfy \(a,c\geq1\) and the middle size satisfies \(b\geq2\). The formula also holds formally at \(b=1\), where the associated commutator Lie algebra is the already studied complete-bipartite graph Lie algebra; that covered special case is not proposed as the new contribution. Zero and full ideals are included. All dimensions are vector-space dimensions over the indicated field. The polynomial is not an integral-order or local-ring ideal zeta function.

## Proof
Put \(U=\mathbb F_q^a\), \(V=\mathbb F_q^b\), \(W=\mathbb F_q^c\), \(E=\operatorname{Hom}(V,U)\oplus\operatorname{Hom}(W,V)\) and \(Z=\operatorname{Hom}(W,U)=U\otimes W^*\). Then \(J=E\oplus Z\), the square \(J^2\) equals \(Z\) because \(b\geq1\), and \(JZ=ZJ=0\).

**Step 1: unique ideal data.** For an arbitrary two-sided ideal \(I\le J\), let \(K=I\cap Z\) and \(T=\pi_E(I)\le E\), with \(e=\dim K\) and \(d=\dim T\). The quotient \(I/K\) projects isomorphically onto \(T\). Hence \(I\) is uniquely a graph of a linear map \(T\to Z/K\), together with \(K\); conversely such a graph gives a linear subspace. Because products with \(Z\) are zero, it is an ideal if and only if
\[
 TJ+JT\subseteq K.
\]
For fixed \(T,K\) satisfying this condition, the number of graph maps is \(q^{d(ac-e)}\), and every resulting ideal has dimension \(d+e\).

**Step 2: product support.** Let \(L\le U\) be the sum of the column images of all first components of vectors in \(T\), and \(R\le W^*\) the sum of the row spaces of their second components. Write \(\dim L=\ell\) and \(\dim R=r\). Multiplying vectors of \(T\) against pure second-block and pure first-block matrices in \(J\), respectively, shows, without assuming the two projections of \(T\) are independent,
\[
 TJ=L\otimes W^*,\qquad JT=U\otimes R.
\]
Their sum \(D(T)\) therefore has dimension
\[
 h(\ell,r)=c\ell+ar-\ell r,
\]
using intersection \((L\otimes W^*)\cap(U\otimes R)=L\otimes R\). Since \(\dim Z=ac\), the admissible \(e\)-subspaces \(K\supseteq D(T)\) number
\[
\genfrac{[}{]}{0pt}{}{ac-h(\ell,r)}{e-h(\ell,r)}_q
\qquad(h(\ell,r)\le e\le ac).
\]

**Step 3: count horizontal spaces by their exact support.** Fix \(L\) and \(R\) of dimensions \(\ell,r\). For arbitrary subspaces \(L'\le L\), \(R'\le R\) of dimensions \(i,j\), the space
\[
\operatorname{Hom}(V,L')\oplus(V\otimes R')
\]
has dimension \(b(i+j)\), and thus contains precisely \(\genfrac{[}{]}{0pt}{}{b(i+j)}{d}_q\) different \(d\)-subspaces. The property of having aggregate image and row support **equal** to \((L,R)\) is obtained by Möbius inversion on the product of the two subspace lattices. The Möbius function on an interval of codimension \(s\) is \((-1)^s q^{\binom{s}{2}}\). Substituting this standard value gives exactly \(M_d(\ell,r;q)\). This inversion counts linked mixed subspaces of \(E\) as well as direct sums; it assumes no splitting of \(T\).

**Step 4: sum unique choices.** There are \(\genfrac{[}{]}{0pt}{}{a}{\ell}_q\genfrac{[}{]}{0pt}{}{c}{r}_q\) choices of the pair \((L,R)\); for each, \(M_d(\ell,r;q)\) choices of \(T\), then the displayed Gaussian number of choices of \(K\), then \(q^{d(ac-e)}\) lifts. Multiply these factors and insert the weight \(t^{d+e}\). Every ideal has exactly one quadruple \((L,R,T,K)\) and one graph map, so there is neither omission nor overcounting. The formula follows. The argument is valid in every characteristic and over every finite field.

## Verification
The standalone script `verify_ideals.py` independently enumerates all row-reduced subspaces of the small matrix spaces and tests two-sided ideal closure by multiplying basis elements **using the original matrix-unit multiplication**. It separately evaluates the closed formula using integer Gaussian coefficients and Möbius inversion. Complete comparisons passed over \(\mathbb F_2\) for block shapes \((1,1,1)\), \((1,2,1)\), \((2,1,1)\), \((1,1,2)\), and over \(\mathbb F_3\) for \((1,1,1)\), \((1,2,1)\), \((2,1,1)\). The check includes the first genuinely nontrivial middle layer \((1,2,1)\). The small boundary cases with middle size one test the unrestricted algebraic identity, but are not claimed as original.

The checker also evaluates the exact nontrivial shape \((2,2,1)\) with \(q=2,3\) and the symmetric shape \((1,2,2)\). These are formula evaluations, **not** exhaustive independent subspace enumerations. The exhaustive tests corroborate, but do not replace, the general proof. Run `python3 verify_ideals.py` with Python 3; the captured output is `verification_output.txt`.

## Relationship to prior work
Meyer, Szigeti and van Wyk (2009) classify ideals of **unital** structural/block-triangular matrix rings (MSC 16S50); their blockwise ideal lattices do not classify the many field-dependent non-coordinate two-sided ideals of the isolated nonunital radical. Chari, Dolbin and Ridenour (arXiv:0809.0245v1, first public 2008-09-01) study **parabolic-stable ad-nilpotent ideals** in the surrounding Lie algebra, rather than ideals of the radical under multiplication by the radical alone.

The complete finite-field ideal polynomials already obtained for the two-step Lie algebras of complete bipartite graphs give the **middle-size-one** instance \(b=1\). Indeed the commutator Lie algebra of \(J_{a,1,c}\) is precisely that of \(K_{a,c}\), and its Lie ideals coincide with associative two-sided ideals by bracketing independently against pure upper-block components. That covered case is explicitly excluded from the novel scope. When \(b\ge2\), the middle basis induces \(b\) copies of the complete-bipartite bracket with their central edge labels identified; the old simple-graph formulas do not by substitution count these amalgamated algebras. The same calculation of independent pure-block brackets shows Lie-ideal and two-sided-ideal conditions still coincide for this family.

Bauer and Schein (arXiv:2202.10865v1, 2022-02-22), Section 1.1, prove general uniform-rationality statements for **local ideal zeta functions** of amalgamated class-two nilpotent rings over compact valuation rings. Those theorems do not give the explicit finite-field degree-by-degree ideal polynomial displayed here, for all \(a,b,c\). A separate published three-block study determines **associative subalgebra** counts in the restricted shape \((1,r,1)\); subalgebras are not required to be two-sided ideals and its formula does not contain the present all-shape ideal census.

## Limitations
This theorem counts only the vector-space dimension of each embedded ideal. It does not classify ideal automorphism orbits, varieties or schemes of ideals, subgroup zeta functions, or ideals of the unital parabolic algebra. The special case \(b=1\) is previously covered. Complete historical priority is not certified; the most relevant published comparisons and outstanding literature-risk qualifications are recorded separately. No independent audit has been performed.

## References
1. V. Chari, R. J. Dolbin, T. Ridenour, *Ideals in Parabolic Subalgebras of Simple Lie Algebras*, arXiv:0809.0245v1 (2008-09-01), https://arxiv.org/abs/0809.0245.
2. J. Meyer, J. Szigeti, L. van Wyk, *On ideals of triangular matrix rings*, Periodica Mathematica Hungarica 59 (2009), 109–115, DOI:10.1007/s10998-009-9109-y.
3. T. Bauer, M. M. Schein, *Ideal growth in amalgamated powers of nilpotent rings of class two and zeta functions of quiver representations*, arXiv:2202.10865v1 (2022-02-22), https://arxiv.org/abs/2202.10865.
4. *Complete ideal-dimension polynomials for complete-bipartite graph Lie algebras*, public research record (2026-10-12), published-finding corpus archive.
5. *Complete ideal census and smooth Goursat strata for bipartite graphical Lie algebras*, public research record (2026-11-02), published-finding corpus archive.
6. *Exact associative-subalgebra spectra in three-block nilpotent radicals*, public research record (2026-11-02), published-finding corpus archive.
