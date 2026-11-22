# Sharp integrated BV error and separated-jump rigidity for quadratic Schoenberg splines

## Finding
For every integer \(n\ge 2\), let \(S_{n,2}\) be the classical positive quadratic Schoenberg spline operator with uniform mesh \(h=1/n\), clamped endpoints, and Greville sampling sites. On the class of real right-continuous bounded-variation functions on \([0,1)\), with the endpoint value fixed by the left limit, its exact sharp approximation coefficient is
\[
\boxed{\displaystyle\sup_{|Df|(0,1)>0}\frac{\|f-S_{n,2}f\|_{L^1(0,1)}}{|Df|(0,1)}=\frac{13}{24n}.}
\]
Equality holds exactly for nonconstant step functions of the form
\[
f(x)=c+\sum_{j\in J}a_j\mathbf1_{[\xi_j,1]}(x),\qquad
\varnothing\ne J\subseteq\{2,\ldots,n\},\quad
|j-k|\ge2\ \text{for distinct }j,k\in J,\quad a_j\ne0,
\]
with arbitrary real \(c\) and arbitrary nonzero real jump sizes \(a_j\). Thus the equality jumps are *locked to nonadjacent interior Greville sites*. By comparison, the ordinary degree-one Schoenberg operator (uniform piecewise-linear interpolation) has sharp coefficient \(1/(2n)\). The quadratic \(C^1\) spline incurs the exact relative worst-case integrated BV penalty \(1/12\).

## Assumptions and scope
Put \(h=1/n\) and define the clamped knots
\[
t_0=t_1=t_2=0,\qquad t_{i+2}=ih\ (1\le i\le n-1),\qquad t_{n+2}=t_{n+3}=t_{n+4}=1.
\]
Write \(N_{i,2}\), \(0\le i\le n+1\), for the normalized nonnegative degree-two B-splines for this knot vector, with \(\sum_iN_{i,2}=1\). Their Greville sites are \(\xi_i=(t_{i+1}+t_{i+2})/2\), namely
\[
\xi_0=0,\quad\xi_1=h/2,\quad\xi_j=(j-1/2)h\ (2\le j\le n),\quad\xi_{n+1}=1.
\]
The operator is \((S_{n,2}f)(x)=\sum_{i=0}^{n+1}f(\xi_i)N_{i,2}(x)\). To remove arbitrary point-representative changes, its input domain is the class of right-continuous functions of finite Jordan variation on \([0,1)\), normalized by \(f(1)=f(1-)\) and \(f(0)=f(0+)\). This is equivalent to choosing \(f(x)=c+\mu((0,x])\) for a finite signed Borel measure \(\mu=Df\) on \((0,1)\), with the obvious interpretation at \(x=1\). The seminorm is \(|Df|(0,1)=|\mu|((0,1))\). All \(L^1\) integrals use unweighted Lebesgue measure. The theorem does not assert boundedness on arbitrary a.e.-equivalence classes without fixing sampling representatives.

## Proof
**1. Reduction to one discontinuity.** Let \(H_s(x)=\mathbf1_{[s,1]}(x)\) for \(0<s<1\). Since \(S_{n,2}\) reproduces constants and the measure representation converges absolutely in the finite-variation norm,
\[
f-S_{n,2}f=\int_{(0,1)}\big(H_s-S_{n,2}H_s\big)\,\mu(ds).
\]
Taking the \(L^1\) norm and using Tonelli yields
\[
\|f-S_{n,2}f\|_1\le\int E_n(s)\,|\mu|(ds),\qquad
E_n(s)=\|H_s-S_{n,2}H_s\|_1.
\]
Hence the exact operator coefficient is \(\sup_{0<s<1}E_n(s)\), and equality forces \(|\mu|\) to be supported on its maximizing points, with no cancellation between the signed jump responses.

**2. All interior step errors.** If \(\xi_{j-1}<s\le\xi_j\) for \(2\le j\le n\), the sampled step spline is \(G_j=\sum_{i=j}^{n+1}N_{i,2}\). Put \(a=t_j\). The B-spline recurrence (including the clamped boundary cases \(j=2,n\)) gives the exact response
\[
G_j(x)=\begin{cases}
0,&x\le a,\\
(x-a)^2/(2h^2),&a\le x\le a+h,\\
1-(a+2h-x)^2/(2h^2),&a+h\le x\le a+2h,\\
1,&x\ge a+2h.
\end{cases}
\]
Its residual \(H_s-G_j\) is negative to the left of \(s\) and positive to the right, and is supported on \([a,a+2h]\). Setting \(v=(s-a-h)/h\in(-1/2,1/2]\) and integrating the two quadratics exactly yields
\[
E_n(s)=h\left(\frac13+v^2-\frac{|v|^3}{3}\right).
\]
The function on the right strictly increases with \(|v|\) on \([0,1/2]\). Its maximum is \(13h/24\). In this half-open interval it is attained only at \(v=1/2\), namely \(s=\xi_j\). The other formal endpoint \(v=-1/2\) is excluded because right-continuous sampling selects the preceding spline at that node.

**3. The two boundary intervals.** For \(0<s\le\xi_1=h/2\), the sampled spline is \(G_1=1-N_{0,2}\), where \(N_{0,2}(x)=(1-x/h)^2\) on \([0,h]\) and vanishes elsewhere. Direct integration gives
\[
E_n(s)=\frac h3-s+\frac{2s^2}{h}-\frac{2s^3}{3h^2}\le\frac h3.
\]
Reflection gives the same upper bound on \(\xi_n<s<1\). Since \(h/3<13h/24\), the complete maximizing-point set is exactly \(\{\xi_2,\ldots,\xi_n\}\).

**4. Complete equality classification.** For a maximizing site \(s=\xi_j\), put \(r_j=H_{\xi_j}-G_j\). The residual is strictly negative on \((t_j,\xi_j)\), strictly positive on \((\xi_j,t_{j+2})\), and zero outside \([t_j,t_{j+2}]\). If \(k\ge j+2\), the supports of \(r_j,r_k\) have disjoint interiors, so arbitrary signed coefficients produce no \(L^1\) cancellation and saturate the estimate. But for consecutive indices \(j,j+1\), the overlap \((t_{j+1},t_{j+2})\) contains \(\xi_j\) but lies left of \(\xi_{j+1}\). Therefore \(r_j\) changes sign on the overlap while \(r_{j+1}\) remains negative there. No pair of nonzero signed coefficients can align their signs almost everywhere. Equality in the integral triangle inequality rules out every adjacent pair. Combined with the maximizing-support requirement from Step 1, this proves both necessity and sufficiency of the stated nonadjacent-jump class.

**5. Comparison with degree one.** For the degree-one Schoenberg operator the Greville sites are the knots \(ih\), and the spline is ordinary piecewise-linear interpolation. The response to a single step is the linear ramp spanning the adjacent sampling cell, so its integrated error is at most \(h/2\), attained at interior sampling knots. The same signed-measure reduction proves its sharp \(BV\)-to-\(L^1\) coefficient \(h/2\). Consequently \((13h/24)/(h/2)=13/12\), yielding the stated exact relative penalty \(1/12\).

## Verification
Run `python3 check_quadratic_schoenberg.py` (standard library only). Its independently implemented rational Cox–de Boor recurrence and exact polynomial-by-polynomial Simpson integration check 1,710 strictly submaximal step points for \(2\le n\le21\), every maximizing Greville-node response in those dimensions, and the partition-of-unity and affine-reproduction identities at 560 rational sites. The exact arithmetic checks supplement, rather than replace, the all-degree argument above. The bound and all equality cases follow from the explicit step formula, measure decomposition and support-sign argument, not finite enumeration.

## Relationship to prior work
The 2013 full-text work of Nagler–Kähler defines this uniform Schoenberg operator and proves a lower bound for **continuous-data uniform approximation** in terms of second moduli of smoothness; its statements concern neither the sharp right-continuous \(BV\)-to-\(L^1\) error nor isolated-jump equality. The 2014 full-text Nagler–Cerejeiras–Forster treatment studies spectral properties and inverse inequalities for continuous data. The earlier Beutel–Gonska–Kacsó–Tachev direct inequalities concern moduli of continuity; only the abstract, not its complete 2002 article, was accessible in this comparison. Levin–Gruberger (2025) treat adapted local quasi-interpolation for discontinuities, with a different operator and accuracy criteria. A published result on quadratic cardinal B-spline quasi-interpolation gives sharp **output total-variation amplification** of a corrected bi-infinite spline; that seminorm and sampling scheme do not imply the integrated **identity-defect** norm, finite clamped-boundary formula, or nonadjacent-jump equality classification here. No historical uniqueness beyond the inspected literature is claimed.

## Limitations
The result is exact for real one-dimensional right-continuous \(BV\) representatives and **degree-two uniform clamped Schoenberg splines**; without the sampling representative convention the map is not well-defined on \(BV\) equivalence classes. The coefficient does not classify higher spline degrees, irregular knots, integral-sampling variants, weighted variation or dimensions above one. Earlier unindexed equivalent formulas, particularly in historical monographs, remain a priority risk. Independent review has not yet been performed.

## References
1. J. Nagler and U. Kähler, *A lower bound for the uniform Schoenberg operator*, arXiv:1312.5546v1, first posted 2013-12-19, https://arxiv.org/html/1312.5546v1 (full text, especially Sections 1.1 and 3).
2. J. Nagler, P. Cerejeiras and B. Forster, *Lower bounds for the approximation with variation-diminishing splines*, arXiv:1402.2403v1, first posted 2014-02-11, https://arxiv.org/abs/1402.2403 (full text, Sections 1–3).
3. L. Beutel, H. Gonska, D. Kacsó and G. Tachev, *On variation-diminishing Schoenberg operators: new quantitative statements*, Monografías Academia de Ciencias de Zaragoza 20 (2002), 9–58, https://www.researchgate.net/publication/265713666_On_variation-diminishing_Schoenberg_operators_New_quantitative_statements (abstract/metadata; full text not verified).
4. D. Levin and N. Gruberger, *Adapted B-Spline Quasi-Interpolation for Approximating Piecewise Smooth Functions*, Algorithms 18 (2025), 335, https://doi.org/10.3390/a18060335 (full HTML, Sections 2–4).
5. *Sharp variation–reproduction tradeoff for quadratic cardinal B-spline quasi-interpolation*, published 2026-11-17, https://github.com/published-finding corpus/2026/tree/main/2026/11/17/SCOPE-sharp-variation-reproduction-tradeoff-for-quadratic-cardinal-b-s--8d80fc7ae2c3 (RESULT.md inspected for its operator and norm).
