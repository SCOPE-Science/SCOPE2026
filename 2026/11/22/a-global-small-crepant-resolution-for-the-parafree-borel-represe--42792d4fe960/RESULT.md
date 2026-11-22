# A global small crepant resolution for the parafree Borel representation fourfolds

## Finding
For every integer \(m\ge2\), the fourfold \(X_m=\operatorname{Hom}(G_m,B)\), where \(G_m=\langle x,y,z\mid x^2y^3=z^{2m+1}\rangle\) and \(B\subset\operatorname{SL}_2(\mathbb C)\) is the upper-triangular Borel subgroup, admits an explicitly constructed smooth **projective-over-\(X_m\)** small crepant resolution \(f_m:\widetilde X_m\to X_m\). It is the total space of a rank-two algebraic vector bundle on the blow-up of a two-dimensional algebraic torus at \(16m\) reduced points. The exceptional locus of \(f_m\) is the disjoint union of \(16m\) surfaces \(\mathbb P^1\times\mathbb A^1\), contracted onto the respective singular lines.

Its ordinary integral homology is torsion-free and has ranks \((1,2,16m+1)\) in degrees \(0,1,2\), and zero in all other degrees. Moreover \(\operatorname{Pic}(\widetilde X_m)\cong\mathbb Z^{16m}\), and, writing \(\mathbb L=[\mathbb A^1]\) in the Grothendieck ring of complex varieties,
\[
[\widetilde X_m]=\mathbb L^2\bigl((\mathbb L-1)^2+16m\mathbb L\bigr),\quad
[\widetilde X_m]-[X_m]=16m\mathbb L^2,\quad
\chi(\widetilde X_m)=16m.
\]
Consequently the compactly supported Hodge–Deligne polynomial is \((uv)^2((uv-1)^2+16muv)\).

## Assumptions and scope
Work over \(\mathbb C\) and take \(m\) to be any integer at least two; set \(n=2m+1\). Define \(\sigma_r(w)=\sum_{j=0}^{r-1}w^{r-1-2j}\). Let
\[
T_m=\{(\lambda,\mu,\nu)\in(\mathbb C^*)^3:\lambda^2\mu^3=\nu^n\}\cong(\mathbb C^*)^2.
\]
The established trace/representation equations [1, §3] identify \(X_m\) with the hypersurface in \(T_m\times\mathbb A^3_{a,b,c}\) cut out by
\[
F=f_1a+f_2b+f_3c=0,\quad
(f_1,f_2,f_3)=(\mu^{-3}\sigma_2(\lambda),\lambda^2\sigma_3(\mu),-\sigma_n(\nu)).
\]
Let \(E_m=V_{T_m}(f_1,f_2,f_3)\). The source proves that \(E_m\) has \(16m\) distinct geometric points and that the singular locus is a disjoint union of \(16m\) lines [1, §4]. The multiplicities and blow-up construction below are checked independently. No compactification and no statement about positive characteristic is claimed.

## Proof
**1. The coefficient ideal is a reduced set of regular points.** The torus is smooth since the derivative of \(\lambda^2\mu^3-\nu^n\) with respect to \(\nu\) is nonzero; \(\lambda,\mu\) are local coordinates. At a common zero of \(f_1,f_2,f_3\), the simple roots of \(\sigma_2(\lambda)\) and \(\sigma_3(\mu)\) imply that \(f_1,f_2\) are regular parameters. Therefore \(I=(f_1,f_2,f_3)\) equals the maximal ideal locally at every point of \(E_m\), and its global zero scheme is reduced. The source's root count can also be recovered directly: two choices for \(\lambda\), four for \(\mu\), and \(n-1=2m\) admissible roots of \(\nu\) for each pair, giving \(16m\) points.

**2. An algebraic rank-two kernel on a point blow-up.** Put \(p:Z_m=\operatorname{Bl}_{E_m}T_m\to T_m\), and denote by \(D=\sum_{e\in E_m}D_e\) the exceptional divisor. Since \(I\mathcal O_{Z_m}=\mathcal O_{Z_m}(-D)\), the three coefficients induce an everywhere surjective sheaf map
\[
\mathcal O_{Z_m}^{\oplus3}\longrightarrow\mathcal O_{Z_m}(-D),\quad (a,b,c)\longmapsto f_1a+f_2b+f_3c.
\]
The map is surjective off \(D\) because its coefficients have no common zero there. On \(D\), the leading forms of the regular system \(f_1,f_2\) generate \(\mathcal O_{\mathbb P^1}(1)\), proving surjectivity also there. Thus its kernel \(\mathcal K_m\) is a locally free sheaf of rank two. Set \(\widetilde X_m=\operatorname{Tot}(\mathcal K_m)\). Its defining equation is the strict transform of \(F\); it is closed in \(Z_m\times\mathbb A^3\), so the induced map \(f_m:\widetilde X_m\to X_m\) is projective (as \(Z_m\to T_m\) is projective). It is an isomorphism away from \(E_m\).

**3. Smallness and exact exceptional fibers.** In a neighborhood of any \(e\in E_m\), write \(s=f_1,t=f_2\); the third coefficient has the form \(f_3=s\alpha+t\beta\). The invertible linear change \(u=a+\alpha c\), \(v=b+\beta c\), \(w=c\) changes the equation to \(su+tv=0\), with singular line \(s=t=u=v=0\). On the blow-up charts \(t=sz\) and \(s=tz\), the strict transform equations are \(u+zv=0\) and \(zu+v=0\). Both charts are nonsingular. Over any point on the singular line, all exceptional directions \([s:t]\in\mathbb P^1\) are permitted. Over all other points, the exceptional direction is unique. Hence the non-isomorphic locus is exactly \(\mathbb P^1\times\mathbb A^1\) above each line. Its dimension is two inside a smooth fourfold; there is no exceptional divisor and the morphism is small. Transversely an exceptional \(\mathbb P^1\) has normal bundle \(\mathcal O(-1)\oplus\mathcal O(-1)\), with a trivial extra line direction from the singular line.

**4. Crepancy.** The ambient \(T_m\times\mathbb A^3\) has trivial canonical bundle and \(X_m\) is a normal hypersurface, hence Gorenstein with \(K_{X_m}\cong\mathcal O_{X_m}\). On the blow-up surface \(K_{Z_m}\cong\mathcal O_{Z_m}(D)\), while the kernel sequence gives \(\det\mathcal K_m\cong\mathcal O_{Z_m}(D)\). The tangent exact sequence of a vector bundle yields
\[
K_{\widetilde X_m}\cong q^*(K_{Z_m}\otimes\det\mathcal K_m^{-1})\cong\mathcal O_{\widetilde X_m}.
\]
Alternatively, smallness gives equality of canonical divisors with the pullback of \(K_{X_m}\), so \(f_m\) is crepant.

**5. Topology, Picard group and motivic identity.** Since a vector-bundle total space deformation-retracts to its base, \(\widetilde X_m\) has the integral homology of \(Z_m\). Blowing up \(16m\) distinct points on \((\mathbb C^*)^2\) adds one free \(H_2\) generator per point, giving ranks \((1,2,16m+1)\). The torus has trivial Picard group, and its point blow-up has \(\operatorname{Pic}(Z_m)\cong\mathbb Z^{16m}\); homotopy invariance of Picard groups for smooth affine-bundle torsors yields the same for \(\widetilde X_m\). In the Grothendieck ring, \([Z_m]=[T_m]+16m([\mathbb P^1]-1)=(\mathbb L-1)^2+16m\mathbb L\), and \([\widetilde X_m]=\mathbb L^2[Z_m]\). Independently, \(X_m\to T_m\) has fiber \(\mathbb A^2\) outside \(E_m\) and \(\mathbb A^3\) over \(E_m\), giving \([X_m]=\mathbb L^2([T_m]-16m)+16m\mathbb L^3\). Subtracting yields the formula and applying Hodge–Deligne realization gives the stated polynomial.

## Verification
The standalone file `CHECK.py` independently tests over the exact rational polynomial ring the simple root and paired-sign conditions for \(n=5,7,\ldots,21\), the \(16m\) count in those instances, and the formal Grothendieck-ring and Euler identities. Execute `python CHECK.py` with SymPy installed. Its finite tests do not prove the universal statement; the five geometric proof steps above do. Key noncomputational verifications are the local regular-sequence criterion for \(I\), the two blow-up charts and the determinant formula for \(\mathcal K_m\).

## Relationship to prior work
Liriano [1] supplies the global representation equations, the number and analytic type of the singular lines, and the integral homology of the smooth locus; it does **not** construct the global algebraic resolution or determine the stated resolution invariants. Standard conifold theory [2] describes two local small resolutions, but local existence does not ensure their compatible algebraic/projective global assembly. The new step here is the simultaneous principalization of the three global coefficients on the smooth character torus, turning the strict transform into a rank-two bundle and yielding the explicit global crepant morphism. Local divisor-class information alone similarly does not determine this global construction or its motive.

## Limitations
This is a relative projective resolution of a nonproper fourfold, not a smooth projective compactification. The construction is specific to the stated odd-exponent Borel representation family in characteristic zero. No uniqueness, classification of other resolutions, or assertion about higher or lower characteristic is made. The motivation and exact all-parameter proof are algebraic; finite checks are supplementary. Novelty is assessed against the inspected accessible literature and records, and priority is not independently certified.

## References
1. S. Liriano, *Exploring the Regular and Singular Loci of Group Representation Varieties*, arXiv:2611.09774v1 (first posted November 6, 2026), https://arxiv.org/html/2611.09774v1, especially Sections 3–6.
2. *Symplectic cohomology of quasihomogeneous \(cA_n\) singularities*, Mathematische Zeitschrift (2026), https://link.springer.com/article/10.1007/s00209-026-03943-7, Definition 2.3 and Example 1 (classical small conifold resolutions).
