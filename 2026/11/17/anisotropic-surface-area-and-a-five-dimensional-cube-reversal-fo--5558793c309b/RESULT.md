# Anisotropic surface area and a five-dimensional cube reversal for positive-pair signed-order polytopes

## Finding
For every integer \(n\ge2\), consider the Euclidean polytope
\[
P_n=\{x\in[-1,1]^n:x_i+x_j\ge0\ \text{for all }1\le i<j\le n\}.
\]
It is a special positive-pair signed-order polytope; the change of variables \(y_i=(1-x_i)/2\) also identifies it isometrically up to the common scale factor \(2\) with the complete-graph fractional stable-set polytope \(\operatorname{FRAC}(K_n)\). This equivalence and the volume are not new.

Its complete Euclidean facet-area spectrum consists of \(n\) facets of area \(2\) and \(\binom n2\) facets of area \(2\sqrt2/(n-1)\). In particular,
\[
\operatorname{Vol}_n(P_n)=2,\qquad S(P_n)=n(2+\sqrt2).
\]
For arbitrary positive coordinate scalings \(a_1,\ldots,a_n\), with \(D=\operatorname{diag}(a_1,\ldots,a_n)\),
\[
\boxed{\ S(DP_n)=\Bigl(\prod_{i=1}^n a_i\Bigr)\left(2\sum_{i=1}^n\frac1{a_i}+\frac2{n-1}\sum_{i<j}\sqrt{\frac1{a_i^2}+\frac1{a_j^2}}\right).\ }
\]
At any prescribed positive volume, the unique minimum of \(S(DP_n)\) among positive diagonal scalings occurs when all \(a_i\) are equal. For an equal-volume Euclidean cube \(C_n\),
\[
\frac{S(P_n)}{S(C_n)}=\frac{1+1/\sqrt2}{2^{(n-1)/n}},
\]
so \(S(P_n)>S(C_n)\) exactly for \(2\le n\le4\), whereas \(S(P_n)<S(C_n)\) exactly for \(n\ge5\). There are no equality cases. This gives a sharp dimension-five change in isoperimetric efficiency relative to the cube.

An additional facet-area concentration consequence is that the coordinate facets represent only \(2/(n+1)\) of all facets by number, but exactly \(2/(2+\sqrt2)\) of the boundary area, independent of dimension.

## Assumptions and scope
All volumes and facet measures are ordinary Euclidean Hausdorff measures in the displayed coordinate realization. The surface area is the sum of \((n-1)\)-dimensional facet areas. The dimension is any integer \(n\ge2\); diagonal scalings are strictly positive and are compared at fixed determinant. The cube is compared at exactly equal \(n\)-dimensional volume, not at fixed diameter, circumsphere, or affine-invariant position. No optimality among all volume-preserving linear maps or arbitrary convex bodies is asserted.

## Proof
**1. Facets and volume.** The inequalities \(x_i\le1\), together with \(x_i+x_j\ge0\) for \(i<j\), already describe \(P_n\): indeed, for each \(i\), any other \(j\) gives \(x_i\ge-x_j\ge-1\). All displayed inequalities support genuine facets, because each admits points satisfying all other defining inequalities strictly. The full-dimensional point with all coordinates \(1/2\) establishes nonempty interior.

At most one coordinate of a point of \(P_n\) can be negative. The nonnegative cube has volume \(1\). In the region with the \(i\)-th coordinate equal to \(-t\), with \(0<t<1\), all other coordinates independently range over \([t,1]\). Its volume is
\[
\int_0^1(1-t)^{n-1}\,dt=\frac1n.
\]
Summing these disjoint regions gives \(\operatorname{Vol}_n(P_n)=1+n/n=2\). The same sector argument is part of previously published literature and is included to fix the normalization.

**2. Exact facet areas.** At \(x_i=1\), the remaining coordinates satisfy precisely the same positive-pair constraints in dimension \(n-1\). Hence the corresponding facet has area \(2\) by the previous volume calculation, interpreting the one-dimensional base case \(P_1=[-1,1]\) as length \(2\). For the pair facet \(x_i+x_j=0\), set \(x_i=t\), \(x_j=-t\), with \(-1\le t\le1\). Every other coordinate lies independently in \([|t|,1]\), and constraints between those coordinates hold automatically. The induced Euclidean line element along \((t,-t)\) is \(\sqrt2\,dt\); consequently, the facet area is
\[
\sqrt2\int_{-1}^1(1-|t|)^{n-2}\,dt=\frac{2\sqrt2}{n-1}.
\]
All \(n+\binom n2\) facets have thus been counted once. Summing yields \(S(P_n)=2n+\binom n2\frac{2\sqrt2}{n-1}=n(2+\sqrt2)\).

**3. Anisotropic metric law.** For any facet with outward unit normal \(u\), the \((n-1)\)-dimensional area multiplier under the invertible diagonal map \(D\) is \(\det(D)\|D^{-\mathsf T}u\|_2\). A coordinate facet has normal \(e_i\), while a pair facet has normal \(-(e_i+e_j)/\sqrt2\). Multiplying their already computed areas by these factors and summing gives the stated scaled formula. The volume is \(2\det D\).

**4. Rigidity at fixed volume.** Fix \(\det(D)=v>0\), set \(c=v^{1/n}\) and \(b_i=c/a_i>0\). Then \(\prod_i b_i=1\), and the surface area equals \(v/c\) times
\[
2\sum_i b_i+\frac2{n-1}\sum_{i<j}\sqrt{b_i^2+b_j^2}.
\]
By the arithmetic–geometric mean inequality, \(\sum_i b_i\ge n\). For each pair, \(\sqrt{b_i^2+b_j^2}\ge\sqrt{2b_ib_j}\). Another application of the arithmetic–geometric mean inequality to the \(\binom n2\) numbers \(\sqrt{b_ib_j}\), whose product is \(1\), yields
\[
\sum_{i<j}\sqrt{b_ib_j}\ge\binom n2.
\]
Therefore the bracket is at least \(2n+n\sqrt2\), attained if all \(b_i=1\). Equality in the first arithmetic–geometric mean inequality forces precisely this case. Thus the equal scaling is the unique minimizer.

**5. The sharp cube comparison.** Since \(\operatorname{Vol}(P_n)=2\), the equal-volume cube has side length \(2^{1/n}\) and surface area \(2n\,2^{(n-1)/n}\). Write \(c_0=1+1/\sqrt2\). The ratio in the finding equals \(c_0/2^{1-1/n}\); its denominator is strictly increasing with \(n\). Direct exact arithmetic gives
\[
c_0^4=\frac{17}4+3\sqrt2>8,
\qquad
c_0^5=\frac{29}4+\frac{41\sqrt2}8<16.
\]
Thus \(c_0>2^{3/4}\), but \(c_0<2^{4/5}\), and strict monotonicity yields the announced threshold and absence of ties.

The coordinate facets represent \(n/(n+\binom n2)=2/(n+1)\) of facet count, and carry area \(2n/S(P_n)=2/(2+\sqrt2)\), proving the final consequence.

## Verification
A standalone numerical convex-hull script `checker.py` independently reconstructs the vertices from the halfspaces, computes Euclidean volume and boundary area using convex hulls, and compares them with the symbolic formulas in dimensions \(2\) through \(5\) under both equal and unequal diagonal scalings. It reports `SIGNED_PAIR_FACET_PASS n=2..5 scales=2` when every test passes. This finite numerical corroboration is not used to prove the all-dimensional result; each formula and strict inequality follows from the analytic derivation above.

## Relationship to prior work
Beck and Hlavacek define the signed-order-polytope setting and its facet systems. An older, equivalent realization is already contained in the fractional stable-set polytope \(\operatorname{FRAC}(K_n)\), studied by Hamano, Hibi and Ohsugi. In fact, \(x=\mathbf1-2y\) sends the latter exactly to the displayed \(P_n\), so these two descriptions are not competing new objects. Previously published work on two-layer signed-order covariance even uses this same body \(P_n\) as an integration base and already proves its volume is \(2\). The volume calculation, equivalence, and facet descriptions are therefore not claimed as discoveries. Another prior result computes inradii of signed order polytopes by weighted longest paths. The contribution claimed here is instead the exact Euclidean facet-area distribution and full positive-diagonal surface-area law, its unique fixed-volume minimizer and the dimension-five cube crossing. The reviewed primary papers and nearby indexed findings do not state these metric conclusions; that comparison does not establish uniqueness against all unindexed sources.

## Limitations
The proof is specific to complete positive-pair constraints; it does not extend the surface formula to arbitrary signed posets or general graphs. The scaled minimality compares only diagonal transformations. The equality classification for cube comparison uses the standard coordinate metric and a cube of exactly equal volume. All-dimensional claims are deductive, while numerical verification covers only dimensions \(2\) through \(5\). An equivalent independent surface-area calculation may exist under fractional vertex packing or signed-graph terminology; historical priority requires external assessment. No independent mathematical audit has been conducted.

## References
1. M. Beck and M. Hlavacek, *Signed Poset Polytopes*, arXiv:2311.04409v1, first public 2023-11-08. https://arxiv.org/abs/2311.04409
2. G. Hamano, T. Hibi, and H. Ohsugi, *Ehrhart series of fractional stable set polytopes of finite graphs*, arXiv:1603.09613v1, first public 2016-03-31. https://arxiv.org/abs/1603.09613
3. *A sharp asymptotic covariance barrier for two-layer signed-order polytopes*, publicly accessible research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/25/SCOPE-a-sharp-asymptotic-covariance-barrier-for-two-layer-signed-order--7e19d7a8fc21
4. *A longest signed path gives the exact Euclidean inradius of every signed order polytope*, publicly accessible research result, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-longest-signed-path-gives-the-exact-euclidean-inradius-of-ever--bd0fdb1bb195
