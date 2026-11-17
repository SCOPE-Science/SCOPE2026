# Two geometric criticalities of cubic Darboux escape trajectories

## Finding
Consider the cubic planar differential system
\[
\dot x=x-x^2y+pxy^2+y^3,\qquad \dot y=y+py^3,
\]
where \(p>0\). Fix \(b>0\) and \(a>-b\), with \(a\ne b\), and start at \((a,b)\). Set
\[
q_0=\frac{a-b}{a+b}\ne0,\qquad A_p=\left(\frac{1+pb^2}{p}\right)^{1/p}.
\]
Every such orbit remains a graph \(x=X_p(Y)\) over \(Y=y\ge b\) until its finite forward escape time \(t_b=\tfrac12\log(1+1/(pb^2))\). There is the **exact** representation
\[
q_p(Y)=q_0\left(\frac{1+pb^2}{1+pY^2}\right)^{1/p},\qquad
X_p(Y)=Y\frac{1+q_p(Y)}{1-q_p(Y)}.
\tag{1}
\]
Consequently \(X_p(Y)/Y\to1\), but the stronger Euclidean transverse behavior has a sharp threshold at \(p=2\):
\[
X_p(Y)-Y\sim 2q_0A_pY^{1-2/p}.
\tag{2}
\]
For \(0<p<2\) the orbit approaches the invariant diagonal \(x=y\) in absolute distance. At \(p=2\), it has the generally **distinct parallel affine asymptote** \(x=y+c\), where
\[
c=q_0\sqrt{2(1+2b^2)}\ne0,
\]
and its signed transverse gap has the second term
\[
X_2(Y)-Y=c+\frac{c^2}{2Y}+O(Y^{-2}).
\tag{3}
\]
For \(p>2\) the transverse gap diverges in absolute value even though its ratio to \(Y\) tends to zero: no finite affine-line asymptote exists.

A second, different geometric threshold occurs at \(p=1\). Define the **signed strip area** between the orbit, the invariant diagonal, and the two horizontal sections \(y=b\) and \(y=Y\):
\[
D_p(Y)=\int_b^Y[X_p(s)-s]\,ds.
\tag{4}
\]
Its absolute value is exactly the corresponding unsigned Euclidean area, since the curves never cross. The limit \(D_p(\infty)\) is finite **if and only if** \(0<p<1\). In that region it is given exactly by
\[
D_p(\infty)=\frac{(1+pb^2)q_0}{1-p}\,
{}_2F_1(1,1-p;2-p;q_0).
\tag{5}
\]
At the critical value \(p=1\), writing \(C=q_0(1+b^2)\), the area is exactly
\[
D_1(Y)=C\log\!\frac{1+Y^2-C}{1+b^2-C}
=2C\log Y+O(1).
\tag{6}
\]
For \(p>1\), the sharp growth law is
\[
D_p(Y)\sim \frac{p q_0A_p}{p-1}\,Y^{2-2/p}.
\tag{7}
\]
At the second critical point this refines to
\[
D_2(Y)=cY+\frac{c^2}{2}\log Y+O(1).
\tag{8}
\]
In particular, for \(1\le p<2\) the orbit's transverse gap vanishes but its strip area is infinite: projective alignment, absolute alignment, and finite-area alignment are genuinely different geometric properties.

Both thresholds have explicit **parameter–observation-scale crossover functions**. With \(a,b\) fixed and \(Y\to\infty\), uniformly for \(\lambda\) in any fixed compact subset of \(\mathbb R\):
\[
\frac{D_{\,1+\lambda/(2\log Y)}(Y)}{2q_0(1+b^2)\log Y}
\longrightarrow \frac{e^\lambda-1}{\lambda},
\qquad\left.\frac{e^\lambda-1}{\lambda}\right|_{\lambda=0}=1,
\tag{9}
\]
\[
X_{\,2+\lambda/\log Y}(Y)-Y\longrightarrow c e^{\lambda/2}.
\tag{10}
\]
These are *joint* limits, not fixed-parameter expansions substituted without uniform control. The two thresholds are absent from the topological phase-portrait classification and concern natural metric invariants of the complete \(p>0\) escaping-side orbit family.

## Assumptions and scope
The differential equation and \(t\) use original physical time. The parameter \(p\) is real and strictly positive, the starting coordinate \(b\) is positive, and \(a>-b\), \(a\ne b\). The strict inequality \(a>-b\) excludes the different escape sector beyond the invariant line \(x=-y\); \(a=b\) is the invariant diagonal itself and has zero transverse gap. In (2) and (7), signed \(\sim\) means that the ratio tends to one, even if \(q_0<0\). The constants in all fixed-parameter asymptotics may depend on the fixed parameters. The limits (9)–(10) are uniform only over compact sets of \(\lambda\), with \(a,b\) fixed. The hypergeometric function in (5) has its real Euler-integral interpretation for \(q_0<1\), including negative values smaller than \(-1\).

## Proof
**1. Exact orbit graph and physical escape time.** Since \(\dot y=y(1+py^2)>0\) for positive \(y\) and \(p>0\), the scalar equation gives
\[
y(t)^2=\frac{b^2e^{2t}}{1-pb^2(e^{2t}-1)},\qquad
 t_b=\frac12\log\left(1+\frac1{pb^2}\right),
\]
and \(y(t)\uparrow\infty\) exactly at \(t_b\). With \(r=x/y\), direct differentiation gives \(\dot r=y^2(1-r^2)\). Setting \(q=(r-1)/(r+1)\) and eliminating the physical time yields
\[
\frac{dq}{dy}=-\frac{2y}{1+py^2}\,q.
\]
Thus \(q=q_p(y)\) in (1). Because \(q_0<1\) for all \(a>-b\), the denominator \(1-q_p(y)\) is strictly positive for every \(y\ge b\), so no earlier \(x\)-singularity occurs. Formula (1) proves the exact graph through the full maximal forward interval and the projective limit.

**2. Absolute and affine asymptotic geometry.** Put \(A_p=((1+pb^2)/p)^{1/p}\). As \(Y\to\infty\),
\[
q_p(Y)=q_0 A_pY^{-2/p}(1+O_p(Y^{-2})),
\]
so, using \(X_p-Y=2Yq_p/(1-q_p)\),
\[
X_p(Y)-Y=2q_0A_pY^{1-2/p}
\left(1+O_p(Y^{-\min\{2,2/p\}})\right).
\tag{11}
\]
The sign never changes. The exponent \(1-2/p\) changes sign at \(p=2\), establishing the trichotomy. At \(p=2\), expand \(q_2(Y)=q_0\sqrt{1+2b^2}\,(1+2Y^2)^{-1/2}\) and the geometric series \((1-q)^{-1}=1+q+q^2+\cdots\). The constant term of \(2Yq\) is \(c\), its order-\(Y^{-1}\) term vanishes, and that of \(2Yq^2\) is \(c^2/(2Y)\); the remaining terms give \(O(Y^{-2})\). If \(p>2\), projective direction one is necessary for any straight-line asymptote, yet the gap from every line of slope one diverges; no affine-line asymptote exists.

**3. Exact area and the first threshold.** From (1), the derivative of the signed area is \(2Yq_p(Y)/(1-q_p(Y))\), which never changes sign. First set \(u=Y^2\), then \(v=((1+pb^2)/(1+pu))^{1/p}\). Direct Jacobian substitution, with the lower section corresponding to \(v=1\), yields the exact identity
\[
D_p(Y)=(1+pb^2)\int_{v_Y}^{1}
\frac{q_0v^{-p}}{1-q_0v}\,dv,
\qquad v_Y=\left(\frac{1+pb^2}{1+pY^2}\right)^{1/p}.
\tag{12}
\]
Because \(q_0\ne0\) and \(q_0<1\), the only possible divergence of the integral is \(v^{-p}\) at zero. This proves the sharp finite-area criterion \(p<1\). For \(0<p<1\), Euler's hypergeometric integral evaluates (12) as (5). At \(p=1\), substituting the rational \(q_1(Y)=C/(1+Y^2)\) directly into \(D_1'(Y)\) and integrating gives (6), with denominator \(1+b^2-C=(1+b^2)(1-q_0)>0\). For \(p>1\), integrating (11) gives (7), because \(2-2/p>0\). Integrating (3) gives (8), with an \(O(1)\) remainder since \(Y^{-2}\) is integrable on a half-line.

**4. Uniform critical windows.** All constants below are uniform for \(p\) in a fixed small closed neighborhood of the respective threshold. Near \(p=1\), expansion (11) and its integrable error yield
\[
D_p(Y)=2q_0A_p\int_1^Y s^{1-2/p}\,ds+O(1)
=2q_0A_p\frac{Y^{2-2/p}-1}{2-2/p}+O(1),
\tag{13}
\]
where the lower bounded section can be absorbed in \(O(1)\). With \(p=1+\lambda/(2\log Y)\), one has \(A_p\to1+b^2\) and \((2-2/p)\log Y=\lambda/p\to\lambda\). Dividing (13) by \(2q_0(1+b^2)\log Y\) yields (9), with the quotient continuously interpreted at \(\lambda=0\). Uniformity on compact \(\lambda\)-sets follows by the bounded smooth function \((e^z-1)/z\), uniform error in (13), and \(p\to1\) uniformly there. Near \(p=2\), use (11) with \(p=2+\lambda/\log Y\): the exponent obeys \((1-2/p)\log Y=\lambda/p\to\lambda/2\), while \(2q_0A_p\to c\) and the error in (11) decays uniformly. This proves (10), including its uniformity.

## Verification
The standalone `check.py` verifies the coordinate identity symbolically using an independent differential substitution. With SymPy and mpmath available, run `python check.py`. It also compares the finite-area hypergeometric formula with a separate logarithmic-variable quadrature, checks the exact \(p=1\) area identity and the \(p=2\) second-order offset, and tests both crossover functions against exact orbit formulas at very large finite sections. Its success message is `DARBOUX_TWO_GEOMETRIC_THRESHOLDS_CHECK_OK`. These finite numerical evaluations are consistency tests only; the preceding proof supplies the infinite-parameter assertions.

## Relationship to prior work
Volokitin's 2023 paper [1] introduces this exact cubic system, classifies its global phase portraits, establishes the invariant lines, and derives the Darboux first integral \((x-y)^p(x+y)^{-p}(1+py^2)\). The present theorem relies on those established invariants and does **not** claim to rediscover integrability or the phase portraits. Its claim is the two distinct *Euclidean geometric* thresholds, an exact finite-area functional, the second-order affine correction, and their uniform critical crossover laws. These statements are not asserted in the inspected original paper and are not consequences of its qualitative classifications alone, although its first integral makes the necessary exact orbital reduction possible.

A published analysis of the same cubic system [2] computes an escape clock and its crossover near the **other** invariant line, \(x=-y\), on the initial-data side \(a<-b\). It does not provide a finite-area criterion, parallel-affine-asymptote classification, or the two parameter–height crossover functions on the side \(a>-b\) analyzed here. The star-node phase-portrait literature [3] is qualitative, and the 2017 and 2023 related Darboux papers [4,5] were identified but could not be compared in full. Thus priority relative to inaccessible and unindexed full texts remains a real limitation.

## Limitations
This is an exact theorem for one integrable polynomial vector-field family, not a perturbation-stability theorem. It treats only \(p>0\) and one positive-height escaping sector, excludes the invariant diagonal itself, and makes no assertion about arbitrary polynomial flows with the same projective direction. The crossover limits hold for bounded scaling variable, not arbitrarily varying parameters. The first integral already determines individual orbits implicitly, so the novelty asserted here is the derived quantitative geometric classification, not an independent integrability mechanism. Publication priority is not certified by search results or self-review.

## References
1. E. P. Volokitin, *The cubic Darboux systems with a non-elementary singular point at the Poincaré equator*, arXiv:2306.10706v1, first public 2023-06-19. https://arxiv.org/abs/2306.10706
2. *A logarithmic-to-Hölder separatrix escape transition in a cubic Darboux flow*, publicly indexed result (2026). https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-a-logarithmic-to-h-lder-separatrix-escape-transition-in-a-cubic--28d900564546
3. B. Alarcón, S. B. S. D. Castro and I. S. Labouriau, *Qualitative planar dynamics with star nodes and homogeneous nonlinearities: beyond Hilbert's 16th problem*, arXiv:2106.07516, 2021. https://arxiv.org/abs/2106.07516
4. E. P. Volokitin and V. M. Cheresiz, *Dynamics of the cubic Darboux systems*, Siberian Electronic Mathematical Reports 14 (2017), 889–902. https://geodesic.mathdoc.fr/item/SEMR_2017_14_a95/
5. E. P. Volokitin and V. M. Cheresiz, *Algebraic ovals and rational integrals of Darboux-type systems*, Siberian Electronic Mathematical Reports 20 (2023), 1108–1124. https://www.mathnet.ru/eng/semr1632
