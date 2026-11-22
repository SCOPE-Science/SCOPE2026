# Eight Hasse components and 25 reduced superspecial parameters in a characteristic-eleven Ciani quartic surface

## Finding
Let \(k=\overline{\mathbb F}_{11}\). The coefficient-marked Ciani plane quartic
\[
C_{r,s}:\ X^4+Y^4+Z^4+rX^2Y^2+s(X^2Z^2+Y^2Z^2)=0
\]
is smooth of genus three exactly when \(r\ne\pm2\), \(s\ne\pm2\), and \(s^2\ne r+2\). Over this smooth two-dimensional base its Hasse determinant is \(A(r,s)^2B(r,s)\), where the nonordinary divisor has precisely eight reduced irreducible geometric components: three components of multiplicity two and five components of multiplicity one. The two groups meet transversely in exactly 25 reduced points; these are all and only the superspecial fibers. All 25 are defined over \(\mathbb F_{121}\), and nine are defined over \(\mathbb F_{11}\).

For coefficient-marked smooth fibers over \(\mathbb F_{11}\), the numbers of geometric Jacobian \(11\)-ranks \(0,1,2,3\), respectively, are \(9,14,18,32\), totaling \(73\). Over \(\mathbb F_{121}\) the corresponding counts are \(25,326,560,13132\), totaling \(14043\). These count coefficient pairs, not abstract curve isomorphism classes.

## Assumptions and scope
All assertions about components and intersections are on the geometrically smooth open parameter surface in characteristic \(11\). Put \(t=s^2\), and define, in \(\mathbb F_{11}[r,s]\),
\[
\begin{aligned}
D&=r^2-4,&E&=2s(r-2),&F&=s^2-4,\\
U&=s^2-4,&V&=2(s^2-2r),\\
L_1&=5s^2(r+1)-4(r+2),\\
L_2&=s^2(r+8)+(r+2),\\
A&=E(E^2+DF)(E^2+8DF)=2s(r-2)^3L_1L_2,\\
B&=V(V^2+U^2)(V^2+8U^2).
\end{aligned}
\]
Choose \(\omega\in\mathbb F_{121}\) satisfying \(\omega^2=-1\). The five irreducible geometric \(B\)-components are the lines in \((r,t)\) specified by \(2(t-2r)=c(t-4)\), where \(c\in\{0,5,-5,\omega,-\omega\}\). Their preimages in \((r,s)\) are irreducible parabola graphs. The three \(A\)-components are \(s=0\), \(L_1=0\), and \(L_2=0\).

## Proof
**Smoothness and genus.** The standard Ciani quartic smoothness criterion (Ohashi, Lemma 2.1) for coefficients \((r,s,s)\) gives the exclusions \(r,s\ne\pm2\) and \((r-2)(r+2-s^2)\ne0\). Thus the displayed conditions are necessary and sufficient. A smooth plane quartic has genus three.

**Cartier and stable rank.** For the standard adjoint-monomial basis of holomorphic differentials indexed by \(X,Y,Z\), the plane-quartic Hasse–Witt coefficient rule extracts coefficients of \(C_{r,s}^{10}\). Because the equation has even monomial exponents, all off-diagonal entries vanish. Interchanging \(X,Y\) preserves the quartic, so the first two diagonal entries agree. Direct multinomial extraction gives
\[
H_{r,s}=\operatorname{diag}(A,A,B),
\quad A=[X^{20}Y^{10}Z^{10}]C_{r,s}^{10},
\quad B=[X^{10}Y^{10}Z^{20}]C_{r,s}^{10}.
\]
The identities in the preceding section are polynomial identities over \(\mathbb F_{11}\), verified again by coefficient enumeration in the attached program. Semilinear Frobenius iterates of this diagonal matrix retain precisely its nonzero diagonal positions. Therefore the geometric Jacobian \(11\)-rank is \(2\mathbf1_{A\ne0}+\mathbf1_{B\ne0}\) and its Cartier \(a\)-number is \(3-\operatorname{rank}H\). In particular \(A=B=0\) is equivalent to Cartier rank zero, hence superspeciality.

**Components.** The factor \((r-2)^3\) never vanishes on the smooth base. The factorization of \(B\), using \(\omega^2=-1\) and \(5^2=3=-8\) in characteristic eleven, gives the five distinct factors \(V-cU\) indexed by the displayed values of \(c\). Each yields the graph \(r=((2-c)s^2+4c)/4\), irreducible in \(k[r,s]\). The three \(A\)-factors are similarly irreducible: \(s\), and the two primitive polynomials linear in \(r\), \(L_1,L_2\). They are reduced. The three \(A\)-components meet one another only at excluded boundary parameters, as do the five \(B\)-components. Thus the Hasse determinant has exactly these eight components, with multiplicities two on \(A\)-components and one on \(B\)-components.

**The 25 intersections.** For each \(c\in\{0,5,-5,\omega,-\omega\}\), the intersection with \(s=0\) is \((r,s)=(c,0)\). The other four points for that \(c\) are obtained by taking both square roots of each of
\[
\begin{array}{lll}
 r=(4c-2)/5, & s^2=-4(c+2)/(5(2-c)), & (L_1=0),\\
 r=(5c+2)/4, & s^2=(c+2)/(2-c), & (L_2=0).
\end{array}
\]
Here denominators are invertible since none of the five values of \(c\) equals \(2\). To establish exhaustion, substitute the parabola equation \(r=((2-c)t+4c)/4\) into \(L_1,L_2\). For each, its roots in \(t\) are the indicated value and \(t=4\). The latter gives the singular boundary point \((r,t)=(2,4)\) and must be discarded. The retained roots are nonzero, distinct from each other and from \(4\), so each gives two distinct \(s\)-values, and each intersection is transverse. For \(s=0\), the gradients of \(s\) and \(V-cU\) are independent since \(\partial(V-cU)/\partial r=-4\ne0\). The five \(B\)-curves are mutually disjoint on the smooth base; hence precisely \(5(1+2+2)=25\) reduced points occur. Direct substitution checks the smoothness conditions at all of them.

All of these parameters lie in \(\mathbb F_{121}\): for \(c\in\{0,5,-5\}\) the two nonzero square arguments are in \(\mathbb F_{11}\) and become squares in \(\mathbb F_{121}\); for \(c=\pm\omega\), the arguments are \(7\pm2\omega\) and \(5\pm3\omega\), whose norms to \(\mathbb F_{11}\) equal \(9\) and \(1\), respectively, so they are squares in \(\mathbb F_{121}\). There are exactly nine rational parameters over \(\mathbb F_{11}\).

**Finite-field stratification.** The exact program `verify_ciani11.py` tests the smoothness predicate and evaluates \(A\) and \(B\) for every coefficient pair in \(\mathbb F_{11}^2\) and \(\mathbb F_{121}^2\), using an explicit quadratic-field representation. It obtains the rank frequencies stated above. The number of smooth marked pairs in either field, of size \(q=11\) or \(q=121\), also equals \(q^2-5q+7\), independently consistent with the enumeration.

## Verification
Run `python3 verify_ciani11.py` using Python 3 and the standard library. The script computes the Hasse polynomials again by direct multinomial coefficient extraction from the defining quartic, checks the factorizations, reconstructs all 25 intersections, proves each proposed parameter is in the smooth locus, and exhaustively enumerates both fields. Its terminal line is `CIANI_F11_25_REDUCED_SUPERSPECIAL_POINTS_VERIFIED`. The program tests all finite-field parameters, while the polynomial identity and component-intersection arguments give the geometric statements over the infinite algebraic closure; enumeration alone is not asserted as a geometric proof.

## Relationship to prior work
Ohashi (2022) supplies the standard Ciani normal form, smoothness criterion and the prime-to-characteristic decomposed Jacobian isogeny; the general fact that superspecial Ciani parameters are defined over the quadratic finite extension is **not** new here. Moriya–Kudo (2022) give arithmetic algorithms and an isomorphism-class census of superspecial genus-three Howe curves; those geometric isomorphism counts are **not** reclassified here. Bouw–Coppola–Lorenzo García–Somoza (2023) study Ciani invariants, reconstruction and conductors rather than this Hasse-divisor geometry. Related characteristic-three, five and seven Ciani rank schemes differ in characteristic and parameter conditions. The assessed claim is restricted to the explicit eight-component characteristic-eleven divisor, its 25 reduced intersections and the two exact coefficient-marked rank censuses.

## Limitations
The two reported censuses are **marked-equation** counts rather than counts of isomorphism classes, principally polarized abelian varieties, or full Weil-polynomial spectra. No Newton polygon classification is claimed away from the superspecial points. The proof and arithmetic checks do not constitute an independent audit. Unindexed earlier parameter calculations could affect historical originality; the enumerated literature does not establish exhaustive global priority.

## References
1. R. Ohashi, *On the maximality of genus-3 nonhyperelliptic curves of Ciani type*, arXiv:2201.12996, first public 2022-01-31. https://arxiv.org/abs/2201.12996
2. T. Moriya and M. Kudo, *Some explicit arithmetic on curves of genus three and their applications*, arXiv:2209.02926, first public 2022-09-07. https://arxiv.org/abs/2209.02926
3. I. Bouw, N. Coppola, E. Lorenzo García, A. Somoza, *On the conductor of Ciani plane quartics*, arXiv:2310.10416, first public 2023-10-16. https://arxiv.org/abs/2310.10416
