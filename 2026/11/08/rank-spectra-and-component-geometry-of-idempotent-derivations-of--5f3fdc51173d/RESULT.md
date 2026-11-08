# Rank spectra and component geometry of idempotent derivations of Heisenberg Lie algebras

## Finding
Let \(H_{2n+1}(k)=V\oplus kz\) be the Heisenberg Lie algebra attached to a nondegenerate alternating form \(\omega\) on a \(2n\)-dimensional vector space, with \(n\ge1\), over any field \(k\). An idempotent derivation is a \(k\)-linear map \(D\) satisfying \(D[x,y]=[Dx,y]+[x,Dy]\) and \(D^2=D\). Write \(\mathcal E_n(k)\) for their set, and \(\mathcal E_n^{\mathrm{red}}\) for the reduced algebraic solution variety.

For a finite field \(k=\mathbb F_q\), put
\[
S_j(q)=q^{j^2}\prod_{i=1}^{j}(q^{2i}-1),\qquad
G_j(q)=\prod_{i=0}^{j-1}(q^j-q^i),\qquad S_0(q)=G_0(q)=1.
\]
Thus \(S_j(q)=|\operatorname{Sp}_{2j}(\mathbb F_q)|\) and \(G_j(q)=|\operatorname{GL}_{j}(\mathbb F_q)|\). The **full rank-generating polynomial** for labeled idempotent derivations is
\[
\sum_{D\in\mathcal E_n(\mathbb F_q)} t^{\operatorname{rank}D}
=\begin{cases}
\displaystyle \sum_{r=0}^{n} q^{2r}\frac{S_n(q)}{S_r(q)S_{n-r}(q)}t^{2r}
+q^n\frac{S_n(q)}{G_n(q)}t^{n+1},&q\text{ even},\\[2mm]
\displaystyle 1+q^n\frac{S_n(q)}{G_n(q)}t^{n+1},&q\text{ odd}.
\end{cases}
\]
Terms of equal exponent are added: when \(n\) is odd and \(q\) is even, the \(t^{n+1}\) coefficient receives contributions from both families.

The associated **reduced** idempotent-derivation variety has exactly \(n+2\) smooth geometrically irreducible connected components in characteristic two: one of dimension \(4r(n-r)+2r\) for each \(r=0,\ldots,n\), and an additional component of dimension \(n^2+2n\). In characteristic different from two, there are exactly two such components, namely the isolated zero derivation and a component of dimension \(n^2+2n\). No statement is made about possible nilpotents in the unreduced defining equation scheme.

## Assumptions and scope
Here \(\omega\colon V\times V\to k\) is alternating and nondegenerate; the Lie bracket on \(H=V\oplus kz\) is \([u+az,v+bz]=\omega(u,v)z\). This defines an alternating Lie bracket also in characteristic two. The theorem concerns **all** ordinary linear derivations which are idempotent as endomorphisms, not arbitrary projections or idempotent Lie algebra homomorphisms. All component statements are geometric statements after extension to an algebraic closure, about the reduced solution variety; finite-field counts concern distinct linear maps, without quotient by automorphisms.

## Proof
**1. Normal form and original defining equations.** The center and derived ideal of \(H\) both equal \(kz\), so any derivation preserves \(kz\). There are unique \(a\in k\), \(T\in\operatorname{End}(V)\), and \(f\in V^*\) such that
\[
D(z)=az,\qquad D(v)=Tv+f(v)z.
\]
The original derivation identity on all pairs of elements is equivalent, by bilinearity, to
\[
\omega(Tu,v)+\omega(u,Tv)=a\,\omega(u,v)\quad (u,v\in V).\tag{1}
\]
Direct multiplication of the displayed linear map gives
\[
D^2=D\iff a^2=a,\quad T^2=T,\quad f\circ T=(1-a)f.\tag{2}
\]
Consequently \(a=0\) or \(a=1\) over every field. Set \(U=\operatorname{im}T\), \(W=\ker T\); then \(V=U\oplus W\), \(T|_U=1\), and \(T|_W=0\).

**2. Complete dichotomy.** Evaluate (1) on \(U\times U\), \(W\times W\), and \(U\times W\). The resulting necessary and sufficient conditions are
\[
(2-a)\omega(U,U)=0,\qquad a\omega(W,W)=0,\qquad(1-a)\omega(U,W)=0.\tag{3}
\]
When \(a=1\), (3) says that \(U\) and \(W\) are complementary totally isotropic subspaces. Nondegeneracy forces both to have dimension \(n\): they are an **ordered transverse Lagrangian pair**. Equation (2) says \(f|_U=0\), with arbitrary values on \(W\). The resulting derivation has rank \(n+1\), because its image contains \(z\) and projects onto \(U\).

When \(a=0\) and \(\operatorname{char}k\ne2\), (3) says that \(U\) is isotropic and orthogonal to \(W\), hence orthogonal to all of \(V\). Thus \(U=0\); (2) then forces \(f=0\), giving only the zero derivation in this sector.

When \(a=0\) and \(\operatorname{char}k=2\), conditions (3) reduce to \(\omega(U,W)=0\), so \(U\) is a nondegenerate symplectic subspace and \(W=U^\perp\). Write \(\dim U=2r\), where \(0\le r\le n\). The projection \(T\) is uniquely determined by \(U\), and (2) permits exactly the functionals \(f\) vanishing on \(W\), a space canonically isomorphic to \(U^*\). The image is a graph over \(U\), hence has dimension \(2r\). Conversely, every datum just described satisfies (1) and (2), proving completeness without a classification assumption.

**3. Finite-field enumeration.** The symplectic group acts transitively on nondegenerate \(2r\)-subspaces, with stabilizer \(\operatorname{Sp}_{2r}\times\operatorname{Sp}_{2(n-r)}\). Thus there are \(S_n/(S_rS_{n-r})\) possible subspaces \(U\) in the characteristic-two \(a=0\) sector and \(q^{2r}\) choices of \(f\) for each. The symplectic group also acts transitively on ordered pairs of transverse Lagrangians, with stabilizer \(\operatorname{GL}_n\); there are \(S_n/G_n\) such pairs and \(q^n\) choices for \(f\) in the \(a=1\) sector. The sectors are disjoint because they have different values of \(D(z)\). Summing by the ranks established above proves the displayed polynomial, for all finite fields including characteristic two.

**4. Component geometry.** In characteristic two, the \(a=0\), \(\dim U=2r\) locus is the total space of the rank-\(2r\) dual tautological vector bundle over the open subvariety of \(\operatorname{Gr}(2r,2n)\) consisting of nondegenerate subspaces. It is smooth, geometrically irreducible, and has dimension \(2r(2n-2r)+2r=4r(n-r)+2r\). The \(a=1\) locus is the total space of a rank-\(n\) vector bundle over the open variety of transverse pairs in \(\operatorname{LG}(n,2n)\times\operatorname{LG}(n,2n)\), smooth and geometrically irreducible of dimension \(n(n+1)+n=n^2+2n\). Both descriptions also hold in characteristic different from two whenever the corresponding locus exists.

Finally, the polynomial \(a^2-a\) separates the two values of \(a\). Within \(a=0\), the characteristic polynomial of the idempotent \(T\) is \(X^{2n-2r}(X-1)^{2r}\), distinct for every \(r\). Therefore these finitely many disjoint rank loci are each open and closed in the reduced solution variety. Every described irreducible locus is consequently a distinct connected and irreducible component; this proves their number, smoothness, and dimensions. In odd characteristic the only \(a=0\) locus is the zero point.

## Verification
The standalone script `check.py` exhaustively enumerates the center-preserving derivation normal form, tests the original Leibniz identity and \(D^2=D\) on basis elements, computes ranks, and compares with the independent symplectic-group formula. It checks the complete cases \((n,q)=(1,2),(1,3),(1,4),(1,5),(2,2)\). In particular, the full rank distributions are \((1,16)\) at ranks \((0,2)\) for \(n=1,q=2\); \((1,36)\) for \(n=1,q=3\); \((1,96)\) for \(n=1,q=4\); \((1,150)\) for \(n=1,q=5\); and \((1,80,480,16)\) at ranks \((0,2,3,4)\) for \(n=2,q=2\). Actual output is supplied as `check_output.txt`.

Execute from the embedded-file directory with `python3 check.py`. The script's final marker is `HEISENBERG_IDEMPOTENT_DERIVATION_ORIGINAL_LEIBNIZ_AND_RANK_OK`. The \(q=4\) case uses the field \(\mathbb F_2[u]/(u^2+u+1)\); a separate field-table check confirmed associativity and distributivity. Finite enumeration supports, but does not replace, the all-dimensional proof.

## Relationship to prior work
Calderón, Draper, Martín and Sánchez (first posted May 16, 2014) classify group gradings of Heisenberg Lie algebras up to equivalence and derive a homogeneous symplectic basis; Theorem 1 in Section 3 substantially anticipates the **orbit-level symplectic description** used here. That classification is fully credited, and no novelty is claimed for grading equivalence or the existence of a symplectic normal form. Their inspected section does not tabulate the labeled finite-field idempotent-derivation rank spectrum or describe the components and dimensions of this particular reduced projector-derivation variety. The present result makes those quantitative, characteristic-sensitive invariants explicit by working with the derivation and idempotence equations themselves.

Eick and Moede (2022) develop algorithms for finite-field \(\mathbb Z_2\)-gradings of *simple* Lie algebras, a related methodology but a different class of algebras and a different output. Historic research records on Heisenberg subalgebra statistics, square-zero Heisenberg derivations, and local derivations concern other invariants/identities and do not state the present count. A broad, as-yet-unlocated grading-enumeration theorem could nevertheless imply the finite-field formulas; originality is not independently certified.

## Limitations
The theorem counts idempotent **ordinary derivations**, not all derivations, local derivations, square-zero derivations, or algebra automorphisms. The component classification is for the **reduced** solution variety, and does not assert reducedness of the full equation scheme. The proof is complete for every field and the numerical formulas for every finite field, but external historical-priority search cannot establish absolute uniqueness. Independent mathematical review has not been performed.

## References
1. A. Calderón, C. Draper, C. Martín, T. Sánchez, *Gradings and Symmetries on Heisenberg type algebras*, arXiv:1405.4093, first version publicly posted 2014-05-16, particularly Sections 2–3, Theorem 1. https://arxiv.org/abs/1405.4093
2. B. Eick and T. Moede, *Computing subalgebras and \(\mathbb Z_2\)-gradings of simple Lie algebras over finite fields*, arXiv:2205.03155 (2022). https://arxiv.org/abs/2205.03155
