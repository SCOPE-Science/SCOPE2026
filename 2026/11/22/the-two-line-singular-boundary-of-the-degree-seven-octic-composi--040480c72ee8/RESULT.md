# The two-line singular boundary of the degree-seven octic composition threefold

## Finding

Let \(k=\mathbb C\), let \(W\) be the seven-dimensional vector space with ordered basis \((t^8,t^6,t^5,t^4,t^3,t^2,t)\), and let \(X\subset\mathbb P(W)=\mathbb P^6\) be the projective closure of the locus of centered monic octics expressible as a quadratic polynomial in a centered monic quartic. Write its homogeneous coordinates as \([A:B:C:D:E:F:G]\), in the stated basis. Then \(X\) has degree \(7\), its normalization is the smooth projective bundle
\[
\nu:\mathbb P_{\mathbb P^2}(\mathcal O(-1)\oplus\mathcal O(-2))\longrightarrow X,
\]
and its entire **reduced singular locus** consists of the two distinct intersecting projective lines
\[
\ell=V(A,B,C,D,E),\qquad m=V(A,B,C,E,G).
\]
The two lines meet at the point representing \(t^2\). In the hyperplane \(A=0\), the **intersection cycle** (not merely the set-theoretic support) is
\[
[X\cdot V(A)]=[\Pi]+2[\Sigma],
\]
where \(\Pi=V(A,B,C,E)\cong\mathbb P^2\) and \(\Sigma\) is the irreducible cubic surface in \(V(A,B,C)\cong\mathbb P^3\) given by
\[
E^3-4DEF+8D^2G=0.
\]
The plane and cubic intersect in the nonreduced plane-section divisor \(2\ell+m\). Here the notation \(\ell,m\) also denotes their natural restrictions to the boundary \(\mathbb P^3\).

More generally, for every pair of integers \(r\ge2\), \(s\ge3\), the projective closure \(X_{r,s}\) of centered normalized degree-\(rs\) compositions with outer degree \(r\) and right factor degree \(s\) has two geometrically distinct irreducible hyperplane-at-infinity components \(A_{r,s}\) and \(B_{r,s}\), and
\[
[X_{r,s}\cdot H_\infty]=[A_{r,s}]+r[B_{r,s}],
\]
with respective degrees \(S(r+s-3,r-1)\) and \(S(r+s-3,r)\), where \(S(n,j)\) denotes a Stirling number of the second kind. This gives the geometric degree recursion \(S(r+s-2,r)=S(r+s-3,r-1)+rS(r+s-3,r)\).

## Assumptions and scope

Everything is over \(\mathbb C\), with scheme-theoretic intersection cycles taken in the irreducible projective varieties. The reduced singular locus is a statement about all complex points of \(X\), not merely rational or coordinate points. The normality assertion concerns the full projective threefold, whereas its dense affine composition chart is smooth. The hyperplane section is generally nonreduced: its cycle multiplicity along \(\Sigma\) is exactly two. No statement is made about the full Jacobian singular scheme or analytic types of the points on the intersecting lines.

## Proof

**1. Parameterization and compactification.** For an arbitrary nonconstant quartic-form parameter \(h=c t^4+u t^2+v t\) and a nonzero pair \((a,b)\), put \(P=ah^2+bh\). The coefficients of \(P\) in the stated basis are
\[
(A,B,C,D,E,F,G)=(ac^2,2acu,2acv,au^2+bc,2auv,av^2+bu,bv).
\tag{1}
\]
The projective-bundle construction of Piene--Shapiro (Theorem 6.2) identifies the source of this map with \(Y=\mathbb P_{\mathbb P^2}(\mathcal O(-1)\oplus\mathcal O(-2))\) and proves that the induced proper morphism \(\nu:Y\to X\) is birational. Its target dimension is three and \(\deg X=S(4,2)=7\).

The map is also **finite**. For any nonzero target polynomial, if \(a=0\) then \(P\) is proportional to \(h\), so the parameter is uniquely determined. If \(a\ne0\), the degree of \(P\) is twice the degree of \(h\); the three possibilities for \(\deg h\) are \(4,2,1\), and for each fixed value a normalized right compositional factor is uniquely recovered by comparing successively its leading coefficients (the standard centered polynomial decomposition algorithm in characteristic zero). The residual outer coefficients are then unique. Thus every geometric fiber is finite. A proper quasi-finite morphism is finite. Since \(Y\) is smooth and normal and \(\nu\) is finite birational, \(\nu\) is the normalization of \(X\).

**2. Boundary cycle and its defining equations.** The leading coefficient in (1) is \(ac^2\), so the pullback of the hyperplane \(A=0\) is the divisor \(V(a)+2V(c)\). The first divisor has a generic point with \(a=0,c\ne0\) and maps birationally onto \(\Pi\); its general polynomial is \(b(ct^4+ut^2+vt)\), characterized by \(A=B=C=E=0\). The second divisor has \(c=0,a\ne0\) and generically maps birationally onto \(\Sigma\); setting \(c=0\) in (1) gives
\[
(D,E,F,G)=(au^2,2auv,av^2+bu,bv).
\]
Elimination yields \(E^3-4DEF+8D^2G=0\). The polynomial is irreducible because it is primitive and linear in \(G\): \(\gcd(D^2,E^3-4DEF)=1\). Conversely, on the dense open \(D\ne0\) the generic inverse is \(v/u=E/(2D)\), with the remaining coefficients reconstructed from \(F,D,G\). Thus the cubic is exactly the irreducible image; pushforward of the pulled-back Cartier divisor gives \([\Pi]+2[\Sigma]\), of degree \(1+2\cdot3=7\). Setting \(E=0\) in the cubic gives \(8D^2G=0\), hence \(\Pi\cap\Sigma=2\ell+m\). Its reduced lines, in the ambient coefficient notation, are \(\ell=V(A,B,C,D,E)\) and \(m=V(A,B,C,E,G)\). The equality \(X\cap V(A)=\Pi\cup\Sigma\) holds set-theoretically.

**3. Why these are exactly the singular points.** In the affine open \(A\ne0\), the normalized composition map is a closed embedding of \(\mathbb A^3\) (Piene--Shapiro, Proposition 5.4), so this open is smooth. At a boundary point with \(E=0\) outside \(\ell\cup m\), one has \(D\ne0\), hence \(a=0,c\ne0,b\ne0\) in the unique normalization preimage; after choosing \(c=b=1\), coordinates \((a,u,v)\) map into the affine target chart \(D\ne0\), and the three target ratios \((A/D,F/D,G/D)\) have Jacobian determinant \(1\) at \(a=0\). At a boundary point with \(E\ne0\), the point lies on \(\Sigma\setminus\Pi\), thus \(c=0,a\ne0,u\ne0,v\ne0\). Normalize \(u=a=1\); in coordinates \((c,v,k=b/a)\) the ratios \((B/D,E/D,F/D)\) have Jacobian determinant \(4\) at \(c=0\). (In the two chart calculations, \(D\) is nonzero.) Every point outside \(\ell\cup m\) therefore has a unique normalization preimage at which the map has full differential rank. Finiteness and the holomorphic inverse-function criterion show \(X\) is smooth there.

For a generic point of \(m\), represented by \(P=\alpha t^4+\beta t^2\) with \(\alpha\ne0\), there are two different normalization preimages: \(a=0,h=P,b=1\) and \(a=\alpha,h=t^2,b=\beta\). For a generic point of \(\ell\), represented by \(P=\alpha t^2+\beta t\) with \(\alpha\ne0\), there are likewise two: \(a=0,h=P,b=1\) and \(a=\alpha,h=t,b=\beta\). A normal point has only one point in its normalization fiber, hence the generic points of both lines are nonnormal, and therefore singular. The singular locus is Zariski closed, so both entire lines are singular. The preceding smoothness argument excludes every other point.

**4. The general boundary recursion.** For \(r,s\) as above, use the Piene--Shapiro bundle \(\mathbb P(\bigoplus_{j=1}^r\mathcal O(-j))\) over \(\mathbb P^{s-2}\). Write the universal polynomial \(\sum_{j=1}^r a_j h^j\) with \(h=c_0t^s+c_{s-2}t^{s-2}+\cdots+c_1t\). The top coefficient is \(a_rc_0^r\), and so the boundary divisor pulls back as \(V(a_r)+rV(c_0)\). The first component maps generically one-to-one to the locus with effective outer degree \(r-1\); the second maps generically one-to-one to the locus with effective right degree \(s-2\), with its next coefficient unrestricted. Generic uniqueness follows by the same leading-coefficient decomposition algorithm. The projective bundle pushforward supplies the stated cycle multiplicities. The degrees are the top powers of the tautological hyperplane class on the respective boundary bundles. Equivalently, their Segre-class coefficients are \(h_{s-2}(1,\ldots,r-1)=S(r+s-3,r-1)\) and \(h_{s-3}(1,\ldots,r)=S(r+s-3,r)\). The two images are distinct. Their generic degrees are \((r-1)s\) and \(r(s-2)\), which differ unless \(s=2r\). In that remaining case, a generic polynomial on the first divisor is centered in its actual highest degree (its penultimate coefficient vanishes), whereas a generic polynomial on the second has a nonzero penultimate coefficient, because the degree-\((s-2)\) inner polynomial has a free next-to-leading term.

## Verification

The accompanying `check.py` is a standalone Python 3/SymPy exact-arithmetic verifier. It checks (1), elimination of the cubic, irreducibility, the plane--cubic intersection, both full-rank chart Jacobians, the degree recursion over a range of parameters, explicit double-fiber witnesses and a finite-field stress test. These finite tests are auxiliary; the proof of the global complex singular locus and general recursion is the algebraic argument above. Execute `python check.py` with SymPy installed.

## Relationship to prior work

Piene--Shapiro (arXiv:2611.16763v1, Sections 5--6 and 9) prove the smoothness of the normalized affine composition locus, the birational projective-bundle parametrization and its degree. Their Section 10 explicitly leaves singularities at infinity as separate questions. The new assertions here are the **finite normalization**, the exact two-line reduced singular locus and the nonreduced plane--cubic boundary cycle for their first nonlinear degree-seven threefold, together with the general geometric boundary multiplicity recursion. Earlier decomposable-polynomial work supplies the underlying recovery algorithm, but not these projective-boundary and singular-locus statements.

## Limitations

No scheme structure is claimed for the Jacobian singular locus of the octic threefold, and no local analytic singularity types are asserted along its two singular lines. The general recursion is an identity of effective cycles, not an identification of the hyperplane section's ideal sheaf. The novelty comparison cannot exclude every unindexed or inaccessible computation; it compares available full texts and relevant mathematical research records. Independent mathematical audit has not been performed.

## References

- R. Piene and B. Shapiro, *Composition loci, invariant Bezoutians, and finite-orbit correspondences*, arXiv:2611.16763v1 (first public November 12, 2026), especially Propositions 5.4 and Theorem 6.2, Sections 9--10. https://arxiv.org/html/2611.16763v1
- J. von zur Gathen and G. Matera, *Density of real and complex decomposable univariate polynomials*, arXiv:1407.0906, in particular the normalized-factor recovery and affine composition setup. https://arxiv.org/abs/1407.0906
