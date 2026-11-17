# Sharp metric and real \(L^1\) Poincaré constants of complete bipartite graphs

## Finding
For integers \(a\ge b\ge2\), let \(G=K_{a,b}\) be the unit-edge complete bipartite graph, with parts \(A\) and \(B\) of cardinalities \(a,b\). Put \(N=a+b\). For a map \(f:V(G)\to(M,d)\) define
\[
R(f)=\frac{\binom N2^{-1}\sum_{\{u,v\}\subset V(G)}d(f(u),f(v))}{(ab)^{-1}\sum_{uv\in E(G)}d(f(u),f(v))},
\]
when the denominator is positive. The sharp supremum over arbitrary metric spaces is
\[
\boxed{\gamma_{\mathrm{met}}(K_{a,b})=\frac{2(a^2+b^2+ab-a-b)}{N(N-1)}.}
\]
The sharp supremum over real \(L^1\) targets is
\[
\boxed{\gamma_{L^1}(K_{a,b})=\max\left\{\frac{4ab}{N(N-1)},\frac{2a}{N}\right\}.}
\]
Every optimal nontrivial real cut \(S\subset V(G)\) is completely described by the pair \((x,y)=(|S\cap A|,|S\cap B|)\):

* If \(a=b\), exactly \(x=y\in\{1,\ldots,a-1\}\).
* If \(a=b+1\), exactly \(x-y\in\{0,1\}\), with neither the empty nor the full cut permitted.
* If \(a\ge b+2\), exactly \((x,y)=(1,0)\) or \((a-1,b)\).

Every nonconstant real \(L^1\)-valued equality map has almost every nontrivial scalar superlevel cut from this list, and this condition is sufficient. For metric targets, equality holds exactly when for all distinct \(u,v\) in one part and every \(w\) in the opposite part,
\[d(f(u),f(v))=d(f(u),f(w))+d(f(w),f(v)).\]
The shortest-path metric supplies a metric-target extremizer. For balanced graphs \(K_{m,m}\) with \(m\ge2\), the ratio is \(\gamma_{\mathrm{met}}/\gamma_{L^1}=(3m-2)/(2m)\), tending to \(3/2\).

## Assumptions and scope
Every metric target is allowed, without finiteness, geodesicity, or linear structure. Real \(L^1\) means any \(L^1(\Omega,\mu;\mathbb R)\), with no restrictions on the measure space needed beyond the ordinary definition. Zero-edge-energy maps are constant since \(G\) is connected, and they are omitted. The constants use the distinct-unordered-pair normalization. With the ordered-pair normalization \(N^{-2}\sum_{u,v}\), both constants must be multiplied by \((N-1)/N\). No claim is made here about squared distances, other target classes, or arbitrary graphs.

## Proof
**Metric upper bound and equality.** Abbreviate \(d(f(u),f(v))\) to \(d_{uv}\) and let \(E_f=\sum_{u\in A,v\in B}d_{uv}\). For each distinct \(u,u'\in A\) and each \(v\in B\), the triangle inequality says \(d_{uu'}\le d_{uv}+d_{vu'}\). Average over all \(v\in B\), then sum over unordered pairs in \(A\):
\[\sum_{\{u,u'\}\subset A}d_{uu'}\le\frac{a-1}{b}E_f.\]
Similarly, \(\sum_{\{v,v'\}\subset B}d_{vv'}\le\frac{b-1}{a}E_f\). Adding the cross pairs gives
\[
\sum_{\{u,v\}\subset V(G)}d_{uv}\le \left(1+\frac{a-1}{b}+\frac{b-1}{a}\right)E_f.
\]
Multiply by \(ab/\binom N2\) for the claimed constant. Each individual triangle deficit is nonnegative, so equality holds exactly under the stated all-intermediate-vertices condition. The intrinsic graph metric attains equality because same-part vertices are distance two, cross-part vertices distance one, and every opposite-part vertex lies on a shortest same-part path.

**Reduction for real \(L^1\).** For real scalars \(s,t\), the layer-cake identity is \(|s-t|=\int_{\mathbb R}|\mathbf1_{s>h}-\mathbf1_{t>h}|\,dh\). Apply it pointwise over the target measure and integrate over the finitely many vertex pairs and edges. Thus an \(L^1\)-valued map's pair and edge energies are nonnegative integrals of cut energies. The sharp ratio is therefore the largest ratio of a nontrivial Boolean cut; indicator-valued maps attain all cut ratios. Strictness and equality are likewise checked cut by cut.

**Exact cut calculation.** Write \(x=|S\cap A|\), \(y=|S\cap B|\), \(s=x+y\), and \(e=bx+ay-2xy\). The number of unordered pairs separated by the cut is \(s(N-s)\), while \(e>0\) is its edge boundary. The cut ratio is
\[R(\mathbf1_S)=\frac{ab}{\binom N2}\frac{s(N-s)}e.\]
Set \(D=a-b\ge0\) and \(d=x-y\). A direct expansion gives the exact deficit identity
\[\boxed{s(N-s)-2e=d(D-d).}\]
If \(D=0\), integer \(d\) satisfies \(d(D-d)\le0\), with equality exactly at \(d=0\). Nontrivial cuts with \(x=y\) exist because \(a=b\ge2\). If \(D=1\), the same inequality holds for all integer \(d\), and equality holds exactly at \(d\in\{0,1\}\). These two cases have sharp cut ratio \(2ab/\binom N2=4ab/[N(N-1)]\).

Now suppose \(D\ge2\). If \(d\notin\{1,\ldots,D-1\}\), the identity gives \(s(N-s)/e\le2\). Otherwise replace \(S\) by its complement if needed: this transforms \(d\) into \(D-d\), so we may assume \(1\le d\le D/2\). Writing \(x=y+d\) yields
\[e=bd+y(N-2d-2y)\ge bd,\]
since \(0\le y\le b\) and \(N-2d-2y\ge D-2d\ge0\). Hence
\[
\frac{s(N-s)}e=2+\frac{d(D-d)}e\le2+\frac{D-d}{b}\le2+\frac{D-1}{b}=\frac{N-1}{b}.
\]
The cut \((x,y)=(1,0)\) attains equality, proving \(\gamma_{L^1}= (ab/\binom N2)(N-1)/b=2a/N\). Equality in the last inequality forces \(d=1\). Equality in \(e\ge bd\), together with \(D\ge2\), forces \(y=0\) or (only for \(D=2\)) \(y=b\). The latter is the complement of the singleton cut. This proves the full cut classification. For \(D=0\) and \(D=1\), the earlier equality conditions give the respective complete lists. Integrating their level sets proves the claimed classification for every real \(L^1\) map.

## Verification
The proof applies to all integers \(a\ge b\ge2\); no finite enumeration is used to infer this. An accompanying exact-rational checker exhaustively verifies the proposed formula and every equality cut for all \(2\le b\le a\le13\), independently enumerating every cut cardinality pair. This is a supplementary diagnostic and does not replace the cut-identity proof. Both constants are attained, so no approximation or compactness argument is needed.

## Relationship to prior work
Polavarapu's 2026 paper [1] proves general cotype-dependent nonlinear Poincaré bounds for regular scalar expanders. Its theorem controls broad target classes but does not compute complete-bipartite sharp exponent-one constants or their cut equality strata. The balanced complete bipartite family lies in the general regular-graph setting, but the quantitative general bounds do not imply these exact values. The present calculation also addresses arbitrary metric targets, which are outside the bounded-cotype conclusion. The cut integration method is classical; [2] is included as context and is not asserted to be invented here. Earlier published studies of exact constants for other graph families do not imply the formulas here.

## Limitations
The result is a sharp, graph-family-specific benchmark rather than a general nonlinear spectral-gap theorem. The exact constants are stated in a particular normalization and at exponent one only. The full cut classification uses the integer part-size restriction and is not an assertion about weighted or general multipartite graphs. Literature searches cannot prove absolute priority; equivalent older edge-isoperimetric or \(L^1\)-Poincaré formulas may exist under different notation. Independent validation has not been performed.

## References
[1] Achintya Raya Polavarapu, *Linear Cotype Bounds for Nonlinear Spectral Gaps of Scalar Expanders*, arXiv:2611.05649v1, 3 November 2026. https://arxiv.org/html/2611.05649v1

[2] Stefan Steinerberger, *Sharp \(L^1\) Poincaré inequalities correspond to optimal hypersurface cuts*, arXiv:1309.6211, 24 September 2013. https://arxiv.org/abs/1309.6211
