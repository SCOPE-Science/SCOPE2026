# Singular strata and canonical-index obstruction of the weight-12 motivic MZV toric base

## Finding
Let \(Y=\mathcal R^{0}_{12}(\mathcal Z^{\mathfrak m})\subset\mathbb P^6_{\mathbb C}\) denote the weight-12 base toric threefold of the motivic multiple-zeta-value relation variety. In the seven coordinates \([a:b:c:d:e:f:g]\) of Example 3.8 of Burmester–Charlton–Kidambi–Lotter–Preiß, the homogeneous ideal is
\[
I_Y=(af-b^2,\;be-c^2,\;bg-cd,\;cg-de).
\]
Write \(p_a,p_f,p_g\) for the corresponding coordinate points and set
\[
L_{dg}=\{a=b=c=e=f=0\},\qquad
L_{eg}=\{a=b=c=d=f=0\}.
\]
Then the **entire reduced singular locus** is
\[
\operatorname{Sing}(Y)_{\mathrm{red}}=L_{dg}\cup L_{eg}\cup\{p_a,p_f\}.
\]
The two lines meet only at \(p_g\); the two additional singular points are isolated. The generic transverse singularity along \(L_{dg}\) is \(A_1\) and along \(L_{eg}\) is \(A_3\). At \(p_g\), a complete affine local chart is the hypersurface \(af=d^4e^2\). Each isolated point has the analytic germ of the vertex of the affine cone over the smooth cubic rational normal scroll \(S(1,2)\subset\mathbb P^4\). Moreover, \(Y\) is \(\mathbb Q\)-Gorenstein precisely on \(Y\setminus\{p_a,p_f\}\).

The full weight-12 variety \(X=\mathcal R_{12}(\mathcal Z^{\mathfrak m})\subset\mathbb P^{11}\) is the projective cone over \(Y\) with vertex \(V\cong\mathbb P^4\). Its reduced singular locus is the join \(\operatorname{Join}(V,\operatorname{Sing}(Y)_{\mathrm{red}})\), including the vertex itself.

## Assumptions and scope
The ground field is \(\mathbb C\). All singular-locus equalities are *set-theoretic/reduced*, not claims of equality with the possibly nonreduced Jacobian singular scheme. The input that these four quadrics generate the prime ideal of the three-dimensional toric base, and the projective-cone decomposition for the full weight-12 variety, comes from Example 3.8 of arXiv:2610.37351v1. Coordinate lines and points always refer to the specified embedding; no statement concerns arbitrary weight or actual numerical MZV relations beyond the motivic toric construction.

## Proof
The five principal opens \(D(a),D(f),D(d),D(e),D(g)\) cover \(Y\): if these five coordinates were all zero, \(af=b^2\) forces \(b=0\), and \(be=c^2\) then forces \(c=0\), contradicting projective nonvanishing. We compute each affine coordinate ring, eliminating variables using the four defining quadrics.

1. On \(D(d)\), put \(d=1\). The equations \(bg=cd\) and \(cg=de\) yield \(c=bg\) and \(e=bg^2\); the equation \(be=c^2\) then holds identically. Hence
\[
Y\cap D(d)\cong\operatorname{Spec}\mathbb C[a,b,f,g]/(af-b^2).
\]
Its Jacobian vanishes exactly where \(a=b=f=0\), i.e. the segment of \(L_{dg}\) in this chart. The transverse singularity is \(A_1\) at every such point, including \(p_d\).

2. On \(D(e)\), put \(e=1\). The equations give \(b=c^2\) and \(d=cg\); the remaining nontrivial equation is \(af=c^4\). Thus
\[
Y\cap D(e)\cong\operatorname{Spec}\mathbb C[a,c,f,g]/(af-c^4).
\]
Its singular locus is \(a=c=f=0\), the segment of \(L_{eg}\), with transverse type \(A_3\), including \(p_e\).

3. On \(D(g)\), put \(g=1\). Now \(c=de\) and \(b=cd=d^2e\), giving
\[
Y\cap D(g)\cong\operatorname{Spec}\mathbb C[a,d,e,f]/(af-d^4e^2).
\]
The hypersurface gradient is \((f,-4d^3e^2,-2d^4e,a)\) in coordinates \((a,d,e,f)\). Over \(\mathbb C\), its common zero set on the hypersurface is exactly \(a=f=0\) and \(de=0\), i.e. the portions of the two lines meeting at \(p_g\). This chart also explicitly describes the crossing germ.

4. On \(D(a)\), put \(a=1\). Eliminate \(f=b^2\), obtaining
\[
\mathbb C[b,c,d,e,g]/(be-c^2,\ bg-cd,\ cg-de),
\]
the affine rank-one locus for the \(2\times3\) matrix
\[
\begin{pmatrix}b&c&d\\c&e&g\end{pmatrix}.
\]
Its projectivization is the smooth rational normal scroll \(S(2,1)\cong S(1,2)\): it is parametrized by \([b:c:e:d:g]=[u s^2:u s t:u t^2:v s:v t]\). Its affine cone is smooth away from its vertex and singular at that vertex (the tangent space there has dimension five, while the cone has dimension three). Thus \(p_a\) is its unique singular point in \(D(a)\).

5. On \(D(f)\), put \(f=1\). Eliminating \(a=b^2\) leaves *the same* three minors, and its unique singular point is \(p_f\).

The five charts cover \(Y\), proving the singular-locus equality and local types without relying on a finite scan. The scroll is \(\mathbb F_1\) with negative section \(C_0\), fiber \(F\), hyperplane class \(H=C_0+2F\), and canonical class \(K=-2C_0-3F\). The class group of its normal affine cone at the vertex is \(\operatorname{Pic}(\mathbb F_1)/\mathbb Z[H]\). As \(K+2H=F\) and \([F]\) has infinite order in that quotient, the canonical class is not torsion in the local divisor class group: the two scroll-cone vertices are not \(\mathbb Q\)-Gorenstein. All other points lie on smooth or hypersurface charts, hence are Gorenstein. This proves the precise \(\mathbb Q\)-Gorenstein locus.

For the full relation variety, the original paper identifies \(X\) as the projective cone over \(Y\) with a linear vertex. Away from the vertex, its local rings are polynomial extensions of those of \(Y\), so exactly the joins over singular points are singular; every point of the vertex is singular because the defining quadrics have vanishing linear terms there and \(X\) is not linear. This proves the final assertion.

## Verification
The standalone `VERIFY.py` symbolically checks all five chart substitutions. It also enumerates the \(21\) projective torus-orbit coordinate supports permitted by the four binomials and calculates ranks of the Jacobian at their \(0/1\) representatives; precisely seven supports are singular: `a`, `f`, `d`, `e`, `g`, `dg`, `eg`. These checks match the proven union of two lines and two isolated points. The geometric argument, not the finite support enumeration, establishes the local normal forms and \(\mathbb Q\)-Gorenstein obstruction. Tested using Python 3 and SymPy 1.14.

## Relationship to prior work
Burmester–Charlton–Kidambi–Lotter–Preiß, Example 3.8, give the four equations of the weight-12 toric variety and its lower-dimensional base; their Table 1 records that this base is normal and nonsmooth, and their Theorem 3.7 states a general polytope smoothness test. Those inputs are explicitly reused. The new calculation is the **complete reduced singular set, the two different transverse ADE strata, the crossing germ, the two isolated scroll-cone singularities, and the exact failure of \(\mathbb Q\)-Gorensteinness**. The general determinantal and toric-cone methods are standard; no foundational criterion is claimed as new. Targeted searches of relevant published mathematical text and indexed findings did not locate the equivalent explicit weight-12 stratification; absence in search results is not a proof of historical priority.

## Limitations
The classification is specific to the weight-12 motivic relation variety over \(\mathbb C\). It does not classify all weights, singular schemes with nilpotent structure, resolutions, discrepancies, or singularities of actual numerical MZV relation varieties. The theorem requires the four equations and cone decomposition from the primary paper, and historical priority may be affected by prior toric-stratification computations not indexed or not inspected. No independent external mathematical audit has been performed.

## References
1. Annika Burmester, Steven Charlton, Abhiram Kidambi, Felix Lotter, Rosa Preiß, *Toric Varieties from Multiple Zeta Values*, arXiv:2610.37351v1 (first public version, 2026-10-27), especially Example 3.8, Theorem 3.7, and Table 1, https://arxiv.org/abs/2610.37351.
2. Standard facts about rational normal scrolls, their determinantal embeddings, and the local divisor class group of a projectively normal affine cone are used with their necessary divisor calculations spelled out above.
