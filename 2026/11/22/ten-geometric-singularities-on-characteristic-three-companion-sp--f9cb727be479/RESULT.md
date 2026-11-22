# Ten geometric singularities on characteristic-three companion space-filling quintics

## Finding

Let \(k=\mathbb F_3\), let \(\phi_{ij}=X_i^3X_j-X_iX_j^3\), and for each \(b\in k^\times=\{1,-1\}\) define the quintic surface \(S_b\subset\mathbb P^3_k\) by
\[
F_b=X_1\phi_{01}+X_2\phi_{12}+X_3\phi_{23}+(bX_0+X_3)\phi_{30}=0.
\]
Then \(S_b\) contains every \(k\)-rational point of \(\mathbb P^3\), is geometrically integral, and is smooth at every \(k\)-rational point. Nevertheless, its geometric singular locus consists of exactly ten points, with Frobenius orbit lengths \(2,2,6\). The projective Jacobian singular subscheme has total length \(22\): the two quadratic orbits are four reduced ordinary double points, and the sextic orbit consists of six Hessian-corank-one points, each with curvilinear Jacobian local algebra \(\overline{k}[\varepsilon]/(\varepsilon^3)\). At each of the latter points the cubic Taylor coefficient along the Hessian null line is nonzero; they are not ordinary double points.

In particular, for each integer \(m\geq1\), the number of geometric singular points defined over \(\mathbb F_{3^m}\) is \(4\) if \(2\mid m\) but \(6\nmid m\), \(10\) if \(6\mid m\), and \(0\) otherwise. These are counts of reduced singular points, not counts with scheme-theoretic multiplicity.

## Assumptions and scope

All schemes and singularities are considered over \(\mathbb F_3\) or its algebraic closure, with the explicitly given homogeneous polynomial (not arbitrary smooth space-filling surfaces). The two values of \(b\) give isomorphic surfaces by the coordinate change \(X_3\mapsto-X_3\); hence it suffices to prove the statements for \(b=1\). The Jacobian singular scheme means the closed projective subscheme defined by all four homogeneous partial derivatives of \(F_b\); Euler's identity is applicable because the degree \(5\) is nonzero in characteristic three.

## Proof

**Eliminating the hyperplane at infinity.** Write \((x,s,t,u)=(X_0,X_1,X_2,X_3)\). Direct substitution of \(x=0\) into the four partial derivatives, followed by dehomogenization successively at \(s=1\), \(t=1\), and \(u=1\), gives the unit ideal in all three charts over \(\mathbb F_3\). Thus every geometric singular point lies in \(x\ne0\).

**The complete affine Jacobian algebra.** Set \(x=1\), and take lexicographic order \(s>t>u\). Exact Buchberger reduction of the four partial derivatives gives the monic three-element Gröbner basis
\[
\{s+\alpha(u),\;t+\beta(u),\;P(u)\},
\]
where all coefficients are reduced modulo three and
\[
\begin{aligned}
\alpha(u)={}&u^{21}-u^{20}+u^{19}+u^{17}+u^{16}-u^{15}-u^{14}-u^{13}\\
&-u^{12}-u^{11}+u^7+u^6+u^5+u^4-u^2+u,\\
\beta(u)={}&u^{19}+u^{18}-u^{16}+u^{15}-u^{13}-u^{12}-u^{10}\\
&-u^7-u^6+u^4-u^3+1.
\end{aligned}
\]
The elimination polynomial has the factorization
\[
\begin{aligned}
P(u)={}&(u^2+1)(u^2-u-1)h(u)^3,\\
h(u)={}&u^6-u^5+u^4+u^3-u+1.
\end{aligned}
\]
The two displayed quadratic factors and \(h\) are pairwise coprime and irreducible over \(\mathbb F_3\). Since the first two Gröbner polynomials are linear in \(s,t\), the entire affine Jacobian algebra is isomorphic to \(\mathbb F_3[u]/(P(u))\). Thus the global singular scheme has length \(2+2+3\cdot6=22\), geometric support size \(2+2+6=10\), and exactly the stated Frobenius orbits. At each sextic point the local algebra is \(\bar k[\varepsilon]/(\varepsilon^3)\); the quadratic points are reduced.

**Quadratic and cubic behavior.** Let \(f(s,t,u)=F_1(1,s,t,u)\) and \(H_f\) be its \(3\times3\) Hessian. Substitution of the Gröbner relations gives
\[
\det(H_f)\equiv-(u^3+u^2-1)h(u)^3\pmod{P(u)}.
\]
This determinant is nonzero at each root of either quadratic factor, proving that those four points are ordinary double points (characteristic three is not two). At any root of \(h\), the Hessian has rank exactly two: a nonzero vector spanning its kernel is obtained from the cross product of the first two rows, represented modulo \(h\) by
\[
v(u)=\bigl(-u^5-u^3-1,\;-u^3,\;-u^4-u^3+u^2-u-1\bigr).
\]
The components are all coprime to \(h\), and the product \(H_fv\) vanishes modulo \(h\). The cubic coefficient of \(f(P+\lambda v)\) along this kernel, reduced modulo \(h\), is
\[
\kappa(u)=u^5-u^4-u^3+1.
\]
Because \(\gcd(\kappa,h)=1\), this coefficient is nonzero at all six points. This verifies their corank-one, cubic-null-direction behavior. No ADE label is asserted in wild characteristic three.

**Integrality and the second parameter.** A nonreduced projective hypersurface in \(\mathbb P^3\), or a union of two positive-degree hypersurface components, has a positive-dimensional singular locus. As the singular support just proved is finite, \(S_1\) is geometrically integral. Direct polynomial substitution gives \(F_1(x,s,t,-u)=F_{-1}(x,s,t,u)\), so everything holds for \(b=-1\) as well. Finally, all \(40\) points of \(\mathbb P^3(\mathbb F_3)\) lie on \(S_b\) because each \(\phi_{ij}\) vanishes at \(\mathbb F_3\)-points. The singular points have residue degrees \(2,2,6\), so no rational point is singular.

## Verification

The accompanying `check_spacefill_F3.py` computes all four derivatives in exact characteristic three, checks the three infinite charts, reconstructs the lexicographic Gröbner basis and irreducible factorization, verifies both Hessian strata and the nonzero cubic coefficient, and checks the coordinate equivalence of the two parameters. Run it with Python 3 and SymPy using `python check_spacefill_F3.py`. All stated computations are finite exact polynomial identities; no numerical approximation, sampling assumption, or infinite extrapolation is used.

## Relationship to prior work

Bourgeois-Conti, Moon, Perez and Warren construct the companion-matrix family and prove the existence of members without rational singular points. Their Remark 7.5 records that their characteristic-three companion examples checked computationally are nonetheless nonsmooth. The calculation above adds the complete geometric singular scheme, its residue-field splitting, and the local quadratic/cubic structure for both parameters over \(\mathbb F_3\). A previously recorded exact determination of rational singular points for the broader odd-characteristic family does not imply any of these nonrational geometric singularity counts. The source's public supporting-code page lists smoothness experiments, but a linked individual output file was not accessible for full comparison; it remains a priority risk.

## Limitations

Only the two nonzero parameters for \(q=3\) in this specific companion family are classified. No assertion is made about all invertible companion matrices, higher powers of three, all space-filling quintics, resolutions, or analytic equivalence classes of the six wild singularities. The computation does not establish publication priority against inaccessible data files or unindexed work. Independent mathematical validation has not been performed.

## References

1. V. Bourgeois-Conti, H.-B. Moon, E. Perez, and A. Warren, *Space-Filling Hypersurfaces*, arXiv:2611.15768v1, first submitted November 11, 2026. https://arxiv.org/html/2611.15768v1
2. Same authors, *Supporting code for space-filling hypersurfaces*, public index and linked run logs. https://www.hanbommoon.net/publications/hypersurface
