# Two exact cusps and a sharp three-preimage region in a planar rational map

## Finding
For the rational planar map
\[
F_{a,b,c,d}(x,y)=\left(x+\frac{ax}{1+y^2}+b,\;y+cx+d\right),
\]
assume \(a>-1\), \(a\ne0\), \(c\ne0\), and \(b,d\in\mathbb R\). Put
\[
B=1+a,\quad s=\sqrt{B/3},\quad U_*=\frac{8\sqrt3 B^{3/2}}{9|a|},\qquad U=c(X-b),\quad V=Y-d.
\]
Here \((X,Y)\) denotes a target point. The number of **distinct real** preimages of \((X,Y)\) is exactly one for every \(|U|\le U_*\). At \((U,V)=(\sigma U_*,\sigma U_*-3\sigma\operatorname{sgn}(a)s)\), \(\sigma=\pm1\), this sole preimage is cubic (algebraic multiplicity three), and these are the only cusp values.

For \(|U|>U_*\), set \(\phi_U(y)=y+U-Ua/(B+y^2)\). Its derivative has exactly two distinct real roots \(y_1<y_2\); set \(V_-(U)=\min_i\phi_U(y_i)\) and \(V_+(U)=\max_i\phi_U(y_i)\). There are exactly three preimages for \(V_-(U)<V<V_+(U)\), exactly two distinct preimages on either boundary, and exactly one otherwise. The critical points over noncusp boundaries are ordinary folds. Thus the map has two unbounded, oppositely directed three-preimage tongues, with no zero-preimage region. The two cusp tips are the only cusps of its critical-value set.

The vertical separation of the two fold values, measured in the normalized \(V\) coordinate (equivalently in the target \(Y\) coordinate), has the sharp onset
\[
V_+(\sigma(U_*+\varepsilon))-V_-(\sigma(U_*+\varepsilon))
=\frac89\sqrt B\left(\frac{\varepsilon}{U_*}\right)^{3/2}
+O_a(\varepsilon^2),\qquad\varepsilon\downarrow0,
\]
for either \(\sigma=\pm1\). The map is proper, has Brouwer degree \(+1\), and its three inverse sheets have Jacobian signs \(+,-,+\). At the excluded parameter \(a=0\), the map is an affine homeomorphism; in the stated range \(a>-1\), any \(a\ne0\) gives genuine triple-preimage regions.

## Assumptions and scope
All coordinates and parameters are real. The inequality \(a>-1\) ensures \(A(y)=1+a/(1+y^2)=(B+y^2)/(1+y^2)>0\), so division by \(A(y)\) is legitimate on the whole real plane. The result classifies first inverse images only; it makes no assertion about periodic orbit counts, Lyapunov spectra, existence of attractors, or forward global convergence. For \(c<0\), the physical \(X\)-direction of the cusps is reversed, but the normalized formulas are unchanged.

## Proof
**1. A global inverse reduction.** Set \(u=cx\). Affine source and target changes turn the map into \((u,y)\mapsto(U,V)=(uA(y),y+u)\). Since \(A(y)>0\), fixing \(U\) gives the exact bijection between real preimages and real roots of
\[
V=\phi_U(y):=y+U-\frac{Ua}{B+y^2},\qquad
u=\frac{U}{A(y)},\quad x=\frac{U}{cA(y)}.
\]
The corresponding cubic inverse equation, with no extraneous real roots, is
\[
(V-U-y)(B+y^2)+Ua=0.
\]
In particular every target has at least one preimage because \(\phi_U(y)=y+U+O(y^{-2})\) at both ends.

**2. The sharp inverse-fiber threshold.** Direct differentiation gives
\[
\phi_U'(y)=1+\frac{2Ua y}{(B+y^2)^2}.
\]
For \(B>0\), \(h(r)=r/(B+r^2)^2\), \(r\ge0\), increases up to the unique maximum at \(r=s=\sqrt{B/3}\) and then decreases. That maximum is \(9/(16\sqrt3 B^{3/2})\). Consequently \(\phi_U'\) is everywhere positive if \(|U|<U_*\). At equality it is nonnegative, with one isolated double zero, so \(\phi_U\) is still strictly increasing. Above threshold, exactly two simple derivative zeros occur on the half-line of sign \(-\operatorname{sgn}(Ua)\), with the sign pattern \(+,-,+\) along the real line. Three monotonicity intervals prove the complete one/two/three-real-preimage census and the claimed exact fold boundaries. The positivity or negativity of the two outer and middle inverse Jacobians follows from \(\det DF=A(y)\phi_U'(y)\).

**3. Only two cusps, with exact locations.** On the critical locus \(\phi'_U=0\), the additional equation \(\phi''_U=0\) forces \(y^2=B/3\). Substitution forces \(|U|=U_*\) and \(y=-\operatorname{sgn}(Ua)s\). Thus there are exactly two simultaneous derivative degeneracies, at
\[
(U,V)=\left(\sigma U_*,\sigma U_*-3\sigma\operatorname{sgn}(a)s\right),\quad \sigma\in\{-1,1\}.
\]
At each, \(\phi'''_U=9/(2B)>0\) and \(\partial_U\phi'_U=-1/U\ne0\). The latter is the nonzero transverse unfolding and the former is the nonzero cubic term, proving these are ordinary Whitney cusps; everywhere else on the critical locus \(\phi''_U\ne0\), giving ordinary folds. For reference, the critical source curve is explicitly parametrized by \(y\ne0\):
\[
u=-\frac{(1+y^2)(B+y^2)}{2ay},\qquad
U=-\frac{(B+y^2)^2}{2ay},\quad V=y+u.
\]

**4. Cusp opening.** At either cusp use the outward target displacement \(U=\sigma(U_*+\varepsilon)\), and write \(y=y_*+\eta\). Taylor expansion, after subtracting terms constant in \(\eta\), gives
\[
\phi_U(y)-\phi_U(y_*)
=-\frac{\varepsilon}{U_*}\eta+\frac{3}{4B}\eta^3
+O_a(\varepsilon\eta^2+|\eta|^4).
\]
The two critical branches therefore satisfy
\[
\eta_\pm=\pm\frac23\sqrt{\frac{B\varepsilon}{U_*}}+O_a(\varepsilon).
\]
Substituting in the Taylor formula gives an extremal-value difference of \((8/9)\sqrt B(\varepsilon/U_*)^{3/2}+O_a(\varepsilon^2)\), as asserted. The sign of \(a\) and the sign \(\sigma\) only interchange the two critical branches; their separation is unchanged.

**5. Properness and degree.** Since \(A(y)\ge\min(1,B)>0\), bounded first output coordinate \(X\) bounds \(x\), and then bounded second coordinate \(Y\) bounds \(y\). Thus inverse images of compact sets are compact. A regular target with \(U=0\) has precisely the preimage \((x,y)=(0,V)\) in normalized coordinates, with positive Jacobian determinant \(A(V)\). Its degree is \(+1\), and the three-sheet sign count agrees. For \(a=0\), the map reduces to the globally invertible affine shear \((x+b,y+cx+d)\).

## Verification
Run `python check.py` using Python 3 and its standard library. The script performs 864 exact rational forward/inverse and determinant identities across signed parameters, checks two exact cubic cusp factorizations for \(a=2\), and checks a concrete three-preimage witness. At \(a=2,b=d=0,c=1\), the target \((X,Y)=(5,3/2)\) has the three distinct inverse \(y\)-coordinates \(-1\) and \((-5\pm\sqrt{17})/4\), with \(x=5/A(y)\). The target \((4,1)\) has one triple inverse at \((2,-1)\). Twelve additional numerical checks corroborate the cusp-opening constant. Finite checks are corroboration; the proof above establishes the universal claims.

## Relationship to prior work
Zhang, Liu, Wei, Jiang and Bi introduced the displayed rational family and derived fixed-point and Jacobian information, then studied coexisting attractors and bifurcations numerically. Their complete accessible article does not supply its global inverse-fiber partition, cusp positions or cusp opening coefficient. The classical critical-curve theory for noninvertible planar maps explains why inverse valence matters for global basin geometry, but supplies neither the model-specific threshold nor its exact two-cusp arrangement. Published classifications of other \(Z_1\)-\(Z_3\) planar polynomial maps and a different \(Z_0\)-\(Z_2\) rational map do not imply the present statements: their inverse equations and critical loci are different.

## Limitations
The caustic classification is restricted to \(a>-1\), excluding the sign-changing or vanishing factor \(A(y)\) at \(a\le-1\). It does not claim global nonlinear dynamical consequences of the cusps, or priority over all unindexed literature. The fold and cusp local normal forms are classical; the contribution is their exhaustive exact application, global preimage census and sharp constants for this particular rational family. The journal's historical records disagree on the precise accepted-manuscript release metadata; the earliest dated public-release assertion used here is the publisher's December 5, 2021 entry.

## References
1. L.-P. Zhang, Y. Liu, Z.-C. Wei, H.-B. Jiang, Q.-S. Bi, “A class of two-dimensional rational maps with self-excited and hidden attractors,” *Chinese Physics B* 31 (2022), 030503, DOI: 10.1088/1674-1056/ac4025. Full scientific text: https://cpb.iphy.ac.cn/fileCPB/journal/article/cpb/html/2022/1674-1056/cpb_31_3_030503.shtml ; release metadata: https://cpb.cpsjournals.org/EN/10.1088/1674-1056/ac4025 .
2. C. Mira, L. Gardini and coauthors, “Noninvertible maps,” *Scholarpedia*, https://www.scholarpedia.org/article/Noninvertible_maps (general critical-curve framework).
3. G. I. Bischi, L. Gardini and C. Mira, “Basin fractalizations generated by a two-dimensional family of \(Z_1\)-\(Z_3\)-\(Z_1\) maps,” *International Journal of Bifurcation and Chaos* (2005). Different cubic-polynomial family; model and abstract available at https://www.researchgate.net/publication/228816563_BASIN_FRACTALIZATIONS_GENERATED_BY_A_TWO-DIMENSIONAL_FAMILY_OF_Z1-Z3-Z1_MAPS .
4. W. Tikjha and S. S. Muni, “Explicit 2-cycle solutions and bifurcation structures in a non-invertible planar rational map,” *International Journal of Dynamics and Control* 13 (2025), article 184, DOI: 10.1007/s40435-025-01673-y. This paper studies the different map \((x,y)\mapsto(-ax/(1+y^2),x+by)\).
