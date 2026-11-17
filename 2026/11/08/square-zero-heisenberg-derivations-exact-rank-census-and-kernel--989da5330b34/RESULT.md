# Kernel-bracket conservation and rank-stratum geometry for square-zero Heisenberg derivations

## Finding

Let \(k\) be any field, \(n\ge1\), and \(H_n=V\oplus kz\) the \((2n+1)\)-dimensional Heisenberg Lie algebra, where \(\omega:V\times V\to k\) is a nondegenerate alternating form and \([v,w]=\omega(v,w)z\). Let \(\mathscr D_d\) denote the locus of **ordinary** derivations \(D\) with \(D^2=0\) and \(\operatorname{rank}_kD=d\).

**Theorem (kernel conservation and two rank mechanisms).** For any such derivation, \(kz\subseteq\ker D\), and the induced bracket form \(\omega_D\) on \(\ker D/kz\) satisfies
\[
\boxed{\operatorname{rank}\omega_D+2\operatorname{rank}D=2n.}
\]
For each \(1\le d\le n\), \(\mathscr D_d\) has a canonical disjoint partition into **two nonempty smooth, geometrically irreducible locally closed strata**:
\[
\mathscr D_d^{\mathrm{in}}=\{D:\operatorname{rank}(D\bmod kz)=d\},\qquad
\mathscr D_d^{\mathrm{out}}=\{D:\operatorname{rank}(D\bmod kz)=d-1\}.
\]
Their respective dimensions over \(k\) are
\[
\boxed{d(2n-d+2),\qquad d(2n-d+2)-1.}
\]
Here \(D\bmod kz\) denotes the induced linear map \(V\to V\); the two strata are not claimed to be irreducible components of the whole rank locus or of any nonreduced defining scheme. Rank zero consists only of the zero derivation, and no ranks above \(n\) occur.

This theorem makes no novelty claim for the already published exact finite-field rank polynomial or the isotropic-image/symmetric-form parametrization; those are recalled as ingredients below. The new statements concern the induced bracket on each kernel and the geometric decomposition of a *fixed full derivation rank*.

## Proof

**1. Block equations, in every characteristic.** As \(kz=[H_n,H_n]\), a derivation has blocks \(D(z)=az\), \(D(v)=Tv+f(v)z\), with \(T\in\operatorname{End}(V)\), \(f\in V^*\), and
\[
\omega(Tu,v)+\omega(u,Tv)=a\omega(u,v).
\]
The condition \(D^2=0\) forces \(a=0\) over a field, followed by \(T^2=0\) and \(fT=0\). Conversely these conditions suffice for an ordinary square-zero derivation. In particular \(z\in\ker D\), and the quotient \(\ker D/kz\) identifies with the subspace \(\{v\in V:Tv=0,\ f(v)=0\}\). These statements remain valid in characteristic two.

**2. The established isotropic-image parametrization.** Set \(W=\operatorname{im}T\), \(r=\dim W\), and \(U=\ker T\). The symplectic skew-adjointness identity yields \(U=W^\perp\). Because \(T^2=0\), \(W\subseteq U\), so \(W\) is isotropic and \(0\le r\le n\). The map induced by \(T\) on \(V/U\cong W^*\) is a nonsingular symmetric linear isomorphism \(B:W^*\to W\). Conversely such a pair \((W,B)\) uniquely determines \(T\), and the allowed central functionals form \(\operatorname{Ann}(W)\). This familiar classification and its finite-field counting consequences are established in the earlier *Exact rank spectra of square-zero derivations of finite Heisenberg Lie algebras* (2026-10-18); the present theorem uses, but does not reclaim, them.

**3. Conservation law.** The subspace \(U=W^\perp\) has radical \(W\) for the restricted alternating form, and \(U/W\) is a nondegenerate symplectic space of dimension \(2(n-r)\). If \(f|_U=0\), then the full derivation has rank \(d=r\), its kernel quotient is \(U\), and the restricted bracket rank is \(2(n-r)=2(n-d)\).

If \(f|_U\ne0\), then \(f(W)=0\) implies \(f\) descends to a nonzero covector on the symplectic quotient \(U/W\). The full rank is \(d=r+1\), and \(\ker D/kz=U\cap\ker f\) maps to a hyperplane in \(U/W\). In a nondegenerate alternating space of dimension \(2s\ge2\), any hyperplane has a one-dimensional radical, so its alternating restriction has rank \(2s-2\). Thus the rank here is \(2(n-r)-2=2(n-d)\). (If \(r=n\), the quotient is zero and this case cannot occur.) Both possibilities prove the claimed conservation law for every field, including characteristic two.

**4. Smooth geometrically irreducible strata and dimensions.** Let \(\mathrm{IGr}(r,2n)\) be the isotropic Grassmannian. It is smooth and geometrically irreducible, of dimension
\[
 r(2n-r)-\frac{r(r-1)}2.
\]
Over this base, the nonsingular symmetric maps \(B:W^*\to W\) form an open subbundle of the symmetric-vector-bundle of rank \(r(r+1)/2\). The choice of \(f\in\operatorname{Ann}(W)\) is a vector bundle of rank \(2n-r\); the condition \(f|_{U}=0\) cuts out a vector subbundle \(\operatorname{Ann}(U)\) of rank \(r\). All these descriptions are algebraic and apply after extension to an algebraic closure. Hence the inside locus, \(r=d\) and \(f\in\operatorname{Ann}(U)\), is smooth and geometrically irreducible of dimension
\[
\left[r(2n-r)-\frac{r(r-1)}2\right]+\frac{r(r+1)}2+r=d(2n-d+2).
\]
The outside locus has \(r=d-1\), with \(f\) in the complement of \(\operatorname{Ann}(U)\) inside \(\operatorname{Ann}(W)\). This is a nonempty open subbundle exactly when \(r<n\), and is smooth and geometrically irreducible of dimension
\[
 r(2n-r+1)+(2n-r)=d(2n-d+2)-1.
\]
In particular, both loci exist for \(1\le d\le n\). The rank-zero case has \(r=0\) and \(f=0\), i.e. the zero derivation; the rank bounds follow from \(r\le n\) and exclusion of the outside case at \(r=n\).

## Scope, verification and limitations

The assertions describe ordinary square-zero derivations of standard nondegenerate Heisenberg Lie algebras over **arbitrary fields**, including characteristic two. They concern the induced kernel-bracket form and two locally closed *set-theoretic geometric strata*. They do not classify arbitrary nilpotent derivations, conjugacy orbits, restricted derivations, or irreducible components of the full possibly nonreduced rank scheme. The formula for the total rank polynomial is prior work and is deliberately not restated as a new theorem. The existing `checker.py` independently checks the original derivation equations and kernel-bracket ranks in the finite cases \((n,q)=(1,2),(1,3),(1,4),(2,2)\). Such bounded checks corroborate the conservation identity but do not prove the all-field statements or the geometric irreducibility; those follow from the block and bundle arguments above.

## Mathematical context and priority boundary

The published 2026-10-18 *Exact rank spectra of square-zero derivations of finite Heisenberg Lie algebras* already gives the full isotropic-image parametrization and the **complete** all-prime-power rank polynomial. The same-day 2026-11-08 *Exact rank counts and a discrete corank limit for square-zero derivations of finite Heisenberg Lie algebras* gives that same rank distribution and an additional asymptotic law. Neither inspected proof states the kernel-bracket conservation identity or the two smooth geometrically irreducible fixed-full-rank strata, although their parametrization is a substantial prerequisite. These two geometric properties are the precise surviving claims; a broader general theorem on symplectic nilpotent orbit strata remains a priority risk.

For related background, see J. Feldvoss, S. Siciliano and T. Weigel, *Outer restricted derivations of nilpotent restricted Lie algebras*, arXiv:1102.2629; and A. E. Brouwer, R. Gow and J. Sheekey, *Counting Symmetric Nilpotent Matrices*, *Electronic Journal of Combinatorics* **21** (2014), P2.4, https://doi.org/10.37236/3810. These do not establish an identical ordinary-derivation kernel-bracket theorem in the inspected material.
