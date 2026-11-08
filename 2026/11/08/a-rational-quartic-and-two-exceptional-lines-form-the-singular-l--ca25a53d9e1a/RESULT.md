# A rational quartic and two exceptional lines form the singular locus of the exponent-seven swept threefold

## Finding

Let \(V=\mathbb C^6\), with standard basis \(e_1,\ldots,e_6\). For \(t\in\mathbb A^1\), let \(U_t\subset V\) be the row span of
\[
R(t)=\begin{pmatrix}
1&t&t^2&t^3&t^4&0\\
0&1&2t&3t^2&4t^3&0\\
0&0&1&3t&6t^2&t
\end{pmatrix}.
\]
This extends to \(t=\infty\) with \(U_\infty=\langle e_4,e_5,e_6\rangle\). Let \(X\subset\mathbb P^5\) be the reduced projective variety swept out by the planes \(\mathbb P(U_t)\), and write \(\operatorname{Sing}(X)_{\mathrm{red}}\) for the reduced singular locus.

**Claim.** The degree-seven threefold \(X\) has exactly three irreducible components in its reduced singular locus:
\[
\boxed{\operatorname{Sing}(X)_{\mathrm{red}}
=\Gamma\cup L_0\cup L_\infty,}
\]
where
\[
\begin{aligned}
\Gamma&=\overline{\{[1:t:t^2:t^3:t^4:0]:t\in\mathbb C\}},\\
L_0&=\mathbb P\langle e_1,e_2\rangle,\\
L_\infty&=\mathbb P\langle e_5,e_4-2e_6\rangle.
\end{aligned}
\]
Thus \(\Gamma\) is a rational normal quartic, \(L_0,L_\infty\) are disjoint lines, each meets \(\Gamma\) at exactly one point (respectively \([e_1]\) and \([e_5]\)), and the reduced singular curve has degree \(6\). Moreover, the critical locus of the normalization map is itself reduced and consists of a section over \(\mathbb P^1\) and the two exceptional lines in the fibers over \(0\) and \(\infty\).

## Assumptions and scope

All varieties and maps are over \(\mathbb C\). The variety \(X\) is the **reduced image** of the complete family of planes, not merely the locus in an affine parameter chart. The singular locus statement is set-theoretic and reduced-scheme-theoretic; it does **not** determine the scheme structure of the Jacobian singular subscheme or the conductor of the normalization. The row-frame family is exactly Example 5.11 of Li, Li and Russo [1], where its two-direct-sum property is established.

## Proof

**1. Normalization and why critical points suffice.** The exact identity
\[
\det\begin{pmatrix}R(s)\\R(t)\end{pmatrix}=-(s-t)^7
\]
shows that \(U_s\cap U_t=0\) whenever \(s\ne t\) are finite. The determinant against \(U_\infty\) is \(1\), so this also holds when one parameter is infinite. The smooth projective-bundle source \(Z=\mathbb P_{\mathbb P^1}(S)\), where \(S\) is the rank-three tautological subbundle pulled back along the Grassmannian curve, maps to \(X\) by \(\nu(t,[v])=[v]\). Distinct fibers have disjoint images. Consequently \(\nu\) is proper, quasi-finite, universally injective, and birational, hence finite and the normalization of \(X\).

A finite universally injective unramified morphism is a closed immersion (Stacks Project, Tag 04XV [2]). At a point where \(d\nu\) is injective, remove the closed image of the non-unramified locus; on the remaining target open, the finite, surjective, universally injective and unramified map is a closed immersion and therefore an isomorphism since the target is reduced. Conversely, if \(X\) is smooth at a point then it is normal there and \(\nu\) is an isomorphism above it, forcing \(d\nu\) to be injective. Hence the reduced singular locus of \(X\) is exactly the image of the critical locus of \(d\nu\).

The degree of \(X\) is \(7\): the Plücker coordinates of the curve have maximal degree \(7\) with nonzero coefficients of both extreme powers, so \(\det S^*\simeq\mathcal O_{\mathbb P^1}(7)\), and the birational scroll map yields \(\deg X=\int_Z c_1(\nu^*\mathcal O(1))^3=7\). This is also a consequence of Theorem A of [1], and is recalled only to identify the threefold.

**2. The finite-parameter chart.** The first three columns of \(R(t)\) form an invertible matrix \(A(t)\) with determinant \(1\). Thus the planes are graphs of
\[
G(t)=A(t)^{-1}R(t)_{\{4,5,6\}}=
\begin{pmatrix}
t^3&3t^4&t^3\\
-3t^2&-8t^3&-2t^2\\
3t&6t^2&t
\end{pmatrix}
\]
over the first three coordinate axes. The map \(\nu\), using projective row coordinates \([a:b:c]\), is locally \((t,[a:b:c])\mapsto[a:b:c:(a,b,c)G(t)]\). Fiber directions have rank two. The base direction fails to add a third tangent direction precisely when \((a,b,c)G'(t)=0\). Direct multiplication yields the ideal
\[
\left(c-4tb+3t^2a,\ \ t(b-ta)\right).
\]
For \(t\ne0\), this forces \([a:b:c]=[1:t:t^2]\), whose image is \([1:t:t^2:t^3:t^4:0]\), the displayed quartic section. At \(t=0\), the conditions reduce to \(c=0\); their images form \(L_0\). The ideal is reduced: in local affine charts covering its zero locus, eliminating \(c\) leaves the square-free product \(t(b-ta)\), up to multiplication by a unit.

**3. The infinity chart.** For \(t\ne0\), the last-three-column block \(C(t)\) has determinant \(t^7\). Put \(u=1/t\). Using those three coordinates as graph coordinates, the plane family extends to \(u=0\) as
\[
H(u)=\left(C(1/u)^{-1}A(1/u)\right)=
\begin{pmatrix}
4u^3&3u^2&2u\\
-3u^4&-2u^3&-u^2\\
6u^3&3u^2&u
\end{pmatrix}.
\]
Its critical condition \((a,b,c)H'(u)=0\) has ideal
\[
\left(c+2a-2ub,\ \u(a-ub)\right).
\]
For \(u\ne0\) the kernel is \([a:b:c]=[u:1:0]\), giving the same quartic section, because the image is \([u^4:u^3:u^2:u:1:0]\). For \(u=0\) the kernel is \(c=-2a\), giving the additional line \(L_\infty=\mathbb P\langle e_5,e_4-2e_6\rangle\). Again the critical ideal is locally a product of distinct factors after elimination, hence reduced.

The two charts cover \(\mathbb P^1\), proving that there are no further critical points or singular components. Pairwise disjointness of distinct ruling planes shows that the two exceptional lines are disjoint and intersect the quartic only at the respective limiting points; therefore the reduced singular curve has degree \(4+1+1=6\).

## Verification

The accompanying standalone Python 3/SymPy script `verify_exponent7_singular.py` works over \(\mathbb Q\) and independently recomputes the stacked six-by-six determinant, both graph matrices and their derivatives, the exact kernel equations, and their boundary ranks and sections. Run:

```bash
python3 verify_exponent7_singular.py
```

Expected terminal marker: `VERIFY_OK`. All identities involve exact polynomials or rational functions; no numerical sampling is required. The scheme-theoretic conclusion about the critical locus also follows directly from the two displayed local ideals. Smoothness outside their image uses the geometric argument and Tag 04XV, not a finite calculation.

## Relationship to prior work

Li, Li and Russo [1, Example 5.11] introduce this exact rank-three, diagonal-exponent-seven two-direct-sum curve and establish the determinant identity. Their Theorem A gives the normalization and degree of the swept variety; their Theorem C and Section 4 determine singular loci for rank-two swept surfaces. The calculations above instead determine the previously unspecified singular locus of their **rank-three** swept threefold: in particular, the two exceptional singular lines do not follow from the degree or from the rank-two classification alone. Perkinson [3] develops the general derivative-rank theory for curves in Grassmannians, but its cited general framework does not by itself evaluate these two boundary kernels. The finite-radicial-unramified criterion [2] is standard and is not claimed as new.

## Limitations

The theorem concerns the single geometrically distinguished rank-three example and its **reduced** singular locus, not all degree-seven swept threefolds, not the embedded Jacobian scheme, and not transverse analytic singularity types or conductor multiplicities. General derivative/normalization methods are established; the contribution is the exact geometric classification in this model. Wider historical coverage, including possible implicit descriptions in older Grassmannian curve work, remains a priority risk. No independent audit or proof formalization has been performed.

## References

[1] D. Li, Y. Li and F. Russo, *Geometry of m-direct-sum morphisms*, arXiv:2610.38184v1, first submitted 28 October 2026. https://arxiv.org/html/2610.38184v1

[2] The Stacks Project, Lemma 41.7.2, Tag 04XV, *Universally injective, unramified morphisms*. https://stacks.math.columbia.edu/tag/04XV

[3] D. Perkinson, *Curves in Grassmannians*, Transactions of the American Mathematical Society 347 (1995), 3179–3246. DOI: 10.1090/S0002-9947-1995-1308020-2.

[4] J. Jelisiejew and H. Keneshlou, *On construction of k-regular maps to Grassmannians via algebras of socle dimension two*, arXiv:2112.14106.
