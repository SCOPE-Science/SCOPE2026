# Thirteen singularities and a geometric-genus-\(45\) vertex on a normal degree-nine abelian model

## Finding
For the normal projective surface \(S_Q\subset\mathbb P^3_{\mathbb C}\) given by
\[
W^3Q(X,Y,Z)^3=(X^3-Y^3)(Y^3-Z^3)(Z^3-X^3),
\]
the complete singular-point basket consists of twelve simple elliptic \(\widetilde E_6\) points, each with local geometric genus \(1\), and one additional vertex of multiplicity \(6\) and local geometric genus exactly \(45\). In particular the sum of the geometric genera of the singularities is \(57\). The vertex tangent cone is three times a smooth conic.

## Assumptions and scope
Work over \(\mathbb C\). Put \(P=(X^3-Y^3)(Y^3-Z^3)(Z^3-X^3)\). Assume \(Q\) is a homogeneous quadratic defining a smooth plane conic, with \(Q(p)\ne0\) for each singular point \(p\) of \(P=0\). These conditions form a nonempty Zariski-open set. For a normal isolated surface singularity \((S,p)\), the local geometric genus is \(p_g(S,p)=\dim_\mathbb C (R^1\pi_*\mathcal O_{\widetilde S})_p\) for a resolution \(\pi\). The result concerns singularities of the displayed degree-nine projective model, not the smooth abelian surface birational to it.

## Proof
**1. Nine lines and twelve triple points.** Fix \(\zeta\) with \(\zeta^3=1\), \(\zeta\ne1\). The reduced branch divisor \(P=0\) consists of the three lines \(X=\zeta^a Y\), the three \(Y=\zeta^b Z\), and the three \(Z=\zeta^c X\), with \(a,b,c\in\mathbb Z/3\mathbb Z\). Lines within each pencil meet at one of the three coordinate vertices. Between distinct pencils, every intersection lies on a unique line of the third pencil: \(a+b+c=0\) modulo \(3\). Thus there are nine further triple points, altogether precisely twelve ordinary triple crossings, and no double crossings. Each pair of the nine lines is accounted for: \(12\binom{3}{2}=\binom{9}{2}=36\).

**2. Exactly thirteen singular points.** Write \(F=W^3Q^3-P\). Then \(F_W=3W^2Q^3\). Wherever \(WQ\ne0\) the surface is smooth. On \(W=0\), a point is singular precisely if \(P=P_X=P_Y=P_Z=0\), hence at the twelve arrangement triple points. Their \(Q\)-values are nonzero. On \(Q=0\), the equation and remaining derivatives again force \(P=\nabla P=0\), impossible for a nonvertex projective \([X:Y:Z]\) because \(Q\) avoids these points. The projective vertex \(v=[1:0:0:0]\) is singular by the degree-six leading term \(Q^3\). Thus these are all thirteen singularities. The hypersurface is Cohen–Macaulay and is regular in codimension one; by Serre's criterion it is normal.

**3. Twelve local simple elliptic singularities.** Near any triple point of the branch curve, the three vanishing linear factors are independent tangent directions and the six other factors are units. Since \(Q\) is a unit, multiplying the local cube coordinate by a holomorphic cube root of the nonzero units gives an analytic germ of the form
\[
 t^3=u\,v\,(u+v).
\]
Its homogeneous exceptional cubic is smooth in \(\mathbb P^2\). One blowup resolves the isolated cone singularity, leaving a smooth elliptic curve \(E\) with normal bundle \(\mathcal O_E(-1)\) and \(E^2=-3\). Its local geometric genus is \(\sum_{k\ge0}h^1(E,\mathcal O_E(k))=1\), by genus one and vanishing for positive-degree twists. This is the simple elliptic \(\widetilde E_6\) type.

**4. Computing the genus of the vertex.** Consider the normal cyclic triple plane \(V\to\mathbb P^2\) defined by \(T^3=P\), with \(T\) of weight \(3\). Because \(P\) is square-free, its finite direct image is
\[
\mathcal O_{\mathbb P}^2}\oplus\mathcal O_{\mathbb P}^2}(-3)\oplus\mathcal O_{\mathbb P}^2}(-6).
\]
Consequently \(\chi(\mathcal O_V)=1+1+10=12\). Its only twelve singularities are precisely the simple elliptic cones just analyzed; hence a smooth resolution \(\widetilde V\) has \(\chi(\mathcal O_{\widetilde V})=12-12=0\). The rational function-field substitution \(T=WQ\) identifies \(V\) and \(S_Q\) birationally, so smooth resolutions of both have equal \(\chi(\mathcal O)\) by birational invariance of the arithmetic genus of smooth projective surfaces. For a degree-nine hypersurface \(S_Q\subset\mathbb P^3\), the hypersurface sequence gives
\[
\chi(\mathcal O_{S_Q})=1+\binom{8}{3}=57.
\]
The Leray spectral sequence of the resolution and the vanishing of \(R^2\pi_*\mathcal O\) for a surface resolution imply \(\chi(\mathcal O_{S_Q})-\chi(\mathcal O_{\widetilde S_Q})=\sum_{p\in\operatorname{Sing}S_Q}p_g(S_Q,p)\). Thus \(57=12\cdot1+p_g(S_Q,v)\), yielding \(p_g(S_Q,v)=45\). In the chart \(W=1\), the local equation is \(Q^3-P=0\) with terms of degrees six and nine. Hence the vertex multiplicity is six and its tangent cone is \(Q^3=0\), three times the assumed smooth conic.

## Verification
The accompanying `verify.py` independently enumerates the nine dual-Hesse lines over \(\mathbb F_7\), where a primitive cube root is \(2\), checks all \(36\) line-pair intersections condense to twelve triple points, and recomputes \(\chi(\mathcal O_{S_Q})=57\), \(\chi(\mathcal O_V)=12\), and the resulting \(p_g(S_Q,v)=45\). It also verifies that the explicit smooth quadratic \(Q=X^2+Y^2+Z^2+YZ+XZ\) avoids all twelve triple points by reduction modulo seven; its integer Hessian determinant is \(4\). The genus computation itself is a general cohomological proof and does not rely on finite enumeration of analytic invariants.

## Relationship to prior work
Chen–Lazarsfeld–Moretti (2026), Proposition A and Proposition 1.6, construct this normal degree-nine model of a self-product of an elliptic curve and establish normality. Their Remark 1.10 recalls the dual-Hesse configuration and related earlier work by Roulleau–Urzúa (2015). The branch configuration and existence of a high-multiplicity projective vertex are therefore prior ingredients. The additional statement here is the complete local singularity basket for the specific displayed model, especially the exact \(45\)-dimensional vertex cohomological defect. The earlier dual-Hesse arrangement does not by itself state this model's vertex invariant. Searches of accessible indexed mathematical findings and targeted literature did not locate the same local invariant; this is evidence of noncoverage, not a guarantee of absolute publication priority.

## Limitations
Only the singularity **geometric genus** and multiplicity/tangent cone at the vertex are computed; its full minimal-resolution graph, analytic equivalence class and deformation theory are not determined. This does not assert all surfaces of degree nine birational to abelian surfaces have this basket. No independent mathematical validation has been performed; the proof and checker are suitable for such validation. The historical-priority comparison is limited by unindexed or uninspected literature.

## References
1. N. Chen, R. Lazarsfeld, F. Moretti, *Some normal abelian surfaces in \(\mathbf P^3\)*, arXiv:2611.09613v1 (first public 2026-11-06), Proposition A, Proposition 1.6, Remark 1.10. https://arxiv.org/html/2611.09613v1
2. X. Roulleau, G. Urzúa, *Chern slopes of simply connected complex surfaces of general type are dense in \([2,3]\)*, Ann. of Math. 182 (2015), 287–306, especially the dual-Hesse arrangement construction. https://doi.org/10.4007/annals.2015.182.1.6
