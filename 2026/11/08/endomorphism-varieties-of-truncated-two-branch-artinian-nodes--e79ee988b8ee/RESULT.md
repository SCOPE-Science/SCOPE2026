# Endomorphism varieties of truncated two-branch Artinian nodes

## Finding
Let \(k\) be any field and let \(m,n\ge 2\). Define the commutative unital \(k\)-algebra
\[
A_{m,n}=k[x,y]/(xy,x^m,y^n).
\]
For the **reduced geometric variety** \(\mathcal E_{m,n}^{\mathrm{red}}\) of unital \(k\)-algebra endomorphisms of \(A_{m,n}\), the following hold simultaneously:

1. Over an algebraic closure of \(k\), the variety has exactly
\[
\boxed{(m-\lceil m/n\rceil)(n-\lceil n/m\rceil)}
\]
   geometrically irreducible components. Every component is a coordinate linear affine space of dimension \(m+n\). Thus the reduced variety is equidimensional over every field.
2. Over every finite field \(\mathbb F_q\), the exact number of unital algebra endomorphisms is
\[
\boxed{q^{m+n-2}\bigl[1+(m-\lceil m/n\rceil)(q-1)\bigr]\bigl[1+(n-\lceil n/m\rceil)(q-1)\bigr].}
\]
3. In the equal-length family \(m=n=d\ge3\), precisely two of the \((d-1)^2\) components contain an open dense set of automorphisms. Every other component has no automorphism. The proportion of endomorphisms that are automorphisms over \(\mathbb F_q\) equals
\[
\boxed{\frac{2(q-1)^2}{((d-1)q-(d-2))^2}},
\]
   with limit \(2/(d-1)^2\) as \(q\) increases. At \(d=2\), by contrast, the reduced variety is a single affine \(4\)-space and the automorphism locus is the dense open group \(\mathrm{GL}_2\).

Here the endomorphism variety is defined by the polynomial equations for unital algebra homomorphisms in the affine coefficient space; the theorem asserts the geometry **after reduction**, not the reducedness of the full equation scheme.

## Assumptions and scope
The algebra is local and Artinian, with maximal ideal \(\mathfrak m=(x,y)\), \(k\)-basis \(1,x,\ldots,x^{m-1},y,\ldots,y^{n-1}\), and length \(m+n-1\). Endomorphisms fix \(k\) and \(1\). They are not assumed injective or surjective. The geometric conclusion is valid over arbitrary fields in all characteristics, and the point-count conclusion holds for every prime power \(q\). All powers are multiplication powers in \(A_{m,n}\), not compositions of endomorphisms.

## Proof
**1. Two independent truncated branches.** The ring is the fiber product of \(k[x]/(x^m)\) and \(k[y]/(y^n)\) over their common residue field \(k\). Every nilpotent element has unique form \(f(x)+g(y)\) with \(f\in xk[x]/(x^m)\) and \(g\in yk[y]/(y^n)\). Images of the two generators of a unital endomorphism must therefore have the unique forms
\[
X=f(x)+g(y),\qquad Y=h(x)+\ell(y).
\]
The defining equations \(X^m=Y^n=XY=0\) split, without cross-branch cancellation, into
\[
 h(x)^n=f(x)h(x)=0\quad\text{in }k[x]/(x^m),
\]
and
\[
 g(y)^m=g(y)\ell(y)=0\quad\text{in }k[y]/(y^n).
\]
The relations \(f(x)^m=0\) and \(\ell(y)^n=0\) are automatic. Conversely, these four displayed constraints give a unique unital algebra homomorphism, since they are precisely the images of the defining relations.

**2. One-branch calculation.** For integers \(M,N\ge2\), put \(R_M=k[t]/(t^M)\), \(b_0=\lceil M/N\rceil\), and let \(\mathcal C_{M,N}\) consist of pairs \((u,v)\in(tR_M)^2\) with \(v^N=uv=0\). Define \(\operatorname{ord}_t(0)=M\). Over every field,
\[
 v^N=0\iff \operatorname{ord}_t(v)\ge b_0,\qquad uv=0\iff\operatorname{ord}_t(u)+\operatorname{ord}_t(v)\ge M.
\]
These equivalences use only the nonvanishing of the product of leading coefficients; no hypothesis on the characteristic is required. The reduced point locus is exactly the union of linear spaces
\[
 L_b=\{(u,v):u\in t^{M-b}R_M,\ v\in t^bR_M\},\qquad b_0\le b\le M-1.
\]
For a pair with \(v\ne0\), its order \(b\) gives membership in \(L_b\). If \(v=0\), the pair belongs to \(L_{M-1}\). The spaces \(L_b\) are pairwise incomparable: the point with exact orders \(M-b\) and \(b\) lies on no other one. Each space has \(b+(M-b)=M\) free coefficients and is therefore a geometrically irreducible affine \(M\)-space. The displayed union consequently gives **all** irreducible components of the reduced one-branch locus, including at zero coordinates.

**3. Product geometry.** The first branch contributes \(\mathcal C_{m,n}\) via \((u,v)=(f,h)\); the second contributes \(\mathcal C_{n,m}\) via \((u,v)=(\ell,g)\). Their independent coefficient equations give a product of the corresponding reduced geometric sets. Every product \(L_b\times L_c\) is an affine \((m+n)\)-space and remains irreducible over an algebraic closure. The index ranges have respectively \(m-\lceil m/n\rceil\) and \(n-\lceil n/m\rceil\) values, proving the component count and equidimensionality.

**4. Exact point count.** For \(k=\mathbb F_q\), count \(\mathcal C_{M,N}(k)\) by the order of \(v\). If \(v=0\), there are \(q^{M-1}\) choices for \(u\). For any fixed \(b\in\{b_0,\ldots,M-1\}\), there are \((q-1)q^{M-b-1}\) elements \(v\) of order \(b\), and exactly \(q^b\) choices for \(u\in t^{M-b}R_M\). Hence
\[
 |\mathcal C_{M,N}(\mathbb F_q)|=q^{M-1}\bigl[1+(M-b_0)(q-1)\bigr].
\]
Multiply the two independent branch counts to obtain the stated formula. This counts individual homomorphisms rather than their conjugacy classes.

**5. Automorphisms and the equal-length boundary.** For \(d\ge3\), an endomorphism of \(A_{d,d}\) is an automorphism exactly when it induces an invertible linear map on \(\mathfrak m/\mathfrak m^2\) (the local Nakayama criterion). Since \(xy=0\) and the two classes \(x^2,y^2\) are independent modulo \(\mathfrak m^3\), any invertible tangent matrix must be diagonal or antidiagonal. The diagonal automorphisms are dense precisely in the component indexed by \((b,c)=(d-1,d-1)\) and the antidiagonal ones in \((b,c)=(1,1)\). Each contributes \((q-1)^2q^{2d-2}\) maps: two nonzero tangent coefficients, with the remaining \(2d-2\) coefficients free. The other components have singular tangent matrices throughout. Dividing their total by the endomorphism count proves the displayed proportion. When \(d=2\), the maximal ideal squares to zero, so every \(2\times2\) linear map is an algebra endomorphism and invertible ones form \(\mathrm{GL}_2\).

## Verification
The standalone file `verify.py` constructs the original quotient-ring multiplication on the basis above, enumerates **all** possible images of the two generators in the maximal ideal, tests their powers and product directly, and compares counts with the closed formula. It also checks that each accepted point belongs to at least one predicted product of coordinate components. The checks include unequal branch lengths, equal branch lengths, the boundary \(d=2\), prime fields \(\mathbb F_2,\mathbb F_3\), and an independently implemented extension field \(\mathbb F_4\). The exact captured output is `verification_output.txt`, whose final line is `TRUNCATED_NODE_ENDOMORPHISM_COUNTS_OK`. These finite computations corroborate, but do not prove, the field-uniform and dimension-uniform statements.

## Relationship to prior work
Ananthnarayan, Avramov and Moore develop the structural theory of local fiber products, including their definition and associated homological invariants. Their 2010 preprint provides the archival starting point for the algebra class, not an enumeration of its endomorphisms. Díaz, Liendo, Manzano-Flores and Regeta develop automorphism groups of zero-dimensional monomial algebras in characteristic zero; Díaz and Lucchini Arteche study recovery of monomial algebras from those groups. Those automorphism results do not determine the other full-dimensional components consisting solely of non-invertible endomorphisms. An additional public note titled *Automorphisms of truncated coordinate-cross algebras over arbitrary fields* determines the automorphism group and its finite-field order for the equal-branch family, but does not state the all-endomorphism count or the full reduced component census presented here. The automorphism slice is accordingly credited, not claimed independently new.

## Limitations
The result does not determine nilpotent/nonreduced structure in the full homomorphism equation scheme, intersection multiplicities of the components, composition laws in the endomorphism monoid, or conjugacy classes of endomorphisms. The component claims are for the reduced geometric support. Literature comparisons cannot establish absolute historical priority: a previously unlocated general theorem on homomorphism schemes of fiber products or monomial Artinian algebras could imply these formulas. No independent mathematical audit has been performed.

## References
1. H. Ananthnarayan, L. L. Avramov, W. F. Moore, *Connected sums of Gorenstein local rings*, arXiv:1005.1304v1, first public 2010-05-07, especially the introduction and §1 on fiber products.
2. R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197v1, 2024-08-05; inspected via available complete HTML (v3).
3. R. Díaz, G. Lucchini Arteche, *Finite-dimensional monomial algebras are determined by their automorphism group*, arXiv:2409.15081v1, 2024-09-23; inspected via available complete HTML (v2).
4. *Automorphisms of truncated coordinate-cross algebras over arbitrary fields*, publicly accessible mathematical record (2026); its full result and proof concern the automorphism subgroup.
