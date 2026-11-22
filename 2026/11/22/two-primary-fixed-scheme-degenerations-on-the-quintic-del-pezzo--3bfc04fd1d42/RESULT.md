# Two-primary fixed-scheme degenerations on the quintic del Pezzo surface

## Finding

**Theorem.** Let \(S\) be the smooth integral degree-five del Pezzo surface \(\overline{M}_{0,5}\), equivalently the blow-up of \(\mathbb P^1_{\mathbb Z}\times\mathbb P^1_{\mathbb Z}\) at its disjoint sections \((0,0)\), \((1,1)\), and \((\infty,\infty)\). Its five markings are \((\infty,0,1,x,y)\). Let \(g=(1234)\) and \(h=(12)(34)\) act by relabelling the markings.

1. The scheme-theoretic fixed locus of \(g\) is finite flat of degree three over the integers, and
   \[
   \operatorname{Fix}_S(g)\simeq\operatorname{Spec}\mathbb Z[u]/\bigl(u(u^2-2u+2)\bigr).
   \]
   It consists of a rational boundary section and a quadratic horizontal component. In characteristic two all three geometric points coalesce to a single curvilinear point of length three.
2. The fixed scheme of \(h\) is the scheme-theoretic union of a smooth rational curve \(\Gamma\simeq\mathbb P^1_{\mathbb Z}\), the strict transform of \(x=y^2\), and a boundary section \(s\simeq\operatorname{Spec}\mathbb Z\). They are disjoint over every odd-characteristic field. In coordinates \(x=1+ab,\ y=1+b\) near the section, its **actual scheme-theoretic ideal** is
   \[
   I_h=\bigl(a(a-2-b),\ b(a-2-b)\bigr)=(a,b)(a-2-b).
   \]
   In characteristic two the section meets \(\Gamma\), and the fixed scheme has an embedded square-zero nilpotent at the intersection: the class of \(a+b\) is nonzero but its square vanishes.

For every finite field of order \(q\), the rational fixed-point count is
\[
\#\operatorname{Fix}_S(g)(\mathbb F_q)=
\begin{cases}
3,&q\text{ odd and }q\equiv1\pmod4,\\
1,&q\text{ even or }q\equiv3\pmod4;
\end{cases}\qquad
\#\operatorname{Fix}_S(h)(\mathbb F_q)=
\begin{cases}q+2,&q\text{ odd},\\q+1,&q\text{ even}.\end{cases}
\]
In odd characteristic, the reduced four-cycle fixed scheme has zeta function \((1-T)^{-3}\) when \(-1\) is a square and \((1-T)^{-1}(1-T^2)^{-1}\) otherwise; in characteristic two its finite-field zeta function is \((1-T)^{-1}\). Scheme length is always three in the four-cycle family.

## Assumptions and scope

All constructions take place over \(\mathbb Z\) and hence specialize to every characteristic. The fixed scheme is the equalizer of the identity and the specified automorphism, not merely the set of fixed geometric points. The labels designate the five marked sections, so cycle notation is unambiguous. No assertion is made about arbitrary twists of \(S\) or about fixed schemes of other permutations.

## Proof

The open moduli chart has \(x,y\not\in\{0,1\}\), \(x\ne y\). Relabeling and renormalizing the first three marked points gives
\[
g:(x,y)\longmapsto \left(\frac{x}{x-1},\frac{x}{x-y}\right),\qquad
h:(x,y)\longmapsto\left(x,\frac{x}{y}\right).
\]
These transformations extend to automorphisms of the standard three-point blow-up, since they are permutations of the marked stable curves.

**Four-cycle.** On the blow-up chart above \((0,0)\) write \(x=uv,\ y=v\). The automorphism acts as
\[
(u,v)\longmapsto\left(\frac{v(u-1)}{uv-1},\frac{u}{u-1}\right).
\]
Setting the two outputs equal to the inputs, eliminating \(v\) via \(v=u/(u-1)\), and retaining the invertible denominators gives precisely
\[
P(u)=u(u^2-2u+2)=0.
\]
The denominators \(u-1\) and \(u^2-u+1\) are units modulo \(P\): their integer resultants with \(P\) have absolute value one. Thus the displayed affine algebra is defined integrally without omitted exceptional fibers. Its three generic geometric fixed points are the boundary crossing \(u=0\) and the interior solutions \(u=1\pm i\), corresponding to \(x=2\) and \(y^2-2y+2=0\). In characteristic two the algebra becomes \(k[u]/(u^3)\).

To see that this chart contains the **entire** fixed subscheme, the ten boundary components are labelled by two-element subsets of the five markings, with components intersecting exactly when their labels are disjoint. The four-cycle fixes no boundary component and exchanges exactly one intersecting pair, namely \(D_{13}\) and \(D_{24}\). Their intersection is the displayed boundary point. All remaining fixed points lie on the open chart and are the two interior solutions, which the same affine fixed algebra captures. This also rules out unseen vertical components and ensures the identification in every characteristic.

**Double transposition.** On the open moduli chart, the fixed equation is \(x=y^2\). Its strict transform \(\Gamma\) is a copy of \(\mathbb P^1_{\mathbb Z}\), parametrized by \(y\). At the blown-up center \((1,1)\), use \(x=1+ab,\ y=1+b\), with exceptional divisor \(b=0\). The induced action is
\[
(a,b)\longmapsto\left(\frac{a(1+b)}{a-1},\frac{b(a-1)}{1+b}\right).
\]
Subtracting the identity, with units inverted on this chart, yields the fixed equations
\[
a(a-2-b)=0,\qquad b(a-2-b)=0.
\]
The factor \(a-2-b\) is exactly the strict-transform equation of \(\Gamma\); the factor \((a,b)\) defines the boundary section \(s=D_{12}\cap D_{34}\). The two loci intersect only in characteristic two. In that fiber \(t=a+b\) obeys \(at=bt=0\), so \(t^2=(a+b)t=0\); yet \(t\notin (at,bt)\), proving that the collision has a genuine embedded nilpotent rather than a merely reduced intersection.

For global completeness, the double transposition fixes only boundary components \(D_{12}\) and \(D_{34}\); its two exchanged intersecting component-pairs are \((D_{13},D_{24})\) and \((D_{14},D_{23})\). The latter two crossings are boundary points of \(\Gamma\). The invariant components meet \(\Gamma\) or the section, and on each the restriction is a nonidentity involution (its fixed points are precisely those already listed). In the blow-up chart above \((0,0)\), the involution interchanges \(u,v\), so its fixed ideal there is \((u-v)\), exactly the local equation of \(\Gamma\), including characteristic two. In the reciprocal chart at \((\infty,\infty)\) the same conclusion holds. Thus no omitted boundary or infinitesimal fixed component exists.

Finally, a degree-three algebra with one rational root and a quadratic factor \(u^2-2u+2\) gives the four-cycle counts. For the double transposition, \(\Gamma(\mathbb F_q)\) has \(q+1\) points; the section contributes one more precisely when it is disjoint from the curve, namely in odd characteristic. Nonreduced structure does not change finite-field-valued point counts.

## Verification

The accompanying self-contained symbolic checker confirms the two birational group relations, both blow-up chart formulas, integral four-cycle elimination with unit resultants, the double-transposition fixed ideal, the nonzero square-zero class in characteristic two, and the boundary-incidence exclusions. Direct prime-field counts are checked for ten primes between two and twenty-nine. These finite checks complement, but do not replace, the algebraic arguments for arbitrary fields.

Run `python check_2primary_fixed.py` with Python 3 and SymPy installed. Expected terminal message: `EXACT_TWO_PRIMARY_FIXED_SCHEMES_VERIFIED`.

## Relationship to prior work

The fundamental \(S_5\)-symmetry of the degree-five del Pezzo surface and its forms over general fields are treated in Zaitsev's classification and Boitrel's geometric classification. Dolgachev and Duncan study finite-group fixed points in the plane Cremona group. The contribution here is more specific: integral **scheme structures** for the two primary order-two/order-four types and the different wild collisions at the prime two. Neither classifying automorphism groups nor determining geometric fixed-point sets alone implies these scheme-theoretic equalizer ideals. The analogous fixed schemes for other permutation types are outside this result.

## Limitations

The four-cycle statement is for the split integral surface and the stated relabeling action. It does not prove deformation-invariance under arbitrary integral models or twists. In characteristic two the scheme-theoretic fixed locus need not be reduced; counting rational geometric points cannot recover its embedded structure. The argument does not compute quotient singularities or intersection-theoretic invariants beyond these explicit fixed schemes.

## References

- A. V. Zaitsev, *Forms of del Pezzo surfaces of degree 5 and 6*, first submitted 9 February 2023, https://arxiv.org/abs/2302.04937.
- A. Boitrel, *Del Pezzo surfaces of degree 5 over perfect fields*, first submitted 11 April 2023, https://arxiv.org/abs/2304.05328.
- I. Dolgachev and A. Duncan, *Fixed points of a finite subgroup of the plane Cremona group*, https://arxiv.org/abs/1408.4042.
