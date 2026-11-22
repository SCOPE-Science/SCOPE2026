# Exponential saturation of the sharp \(BV\)-to-\(L^2\) Hardy-iteration defect

## Finding

Write \(Hf(x)=x^{-1}\int_0^x f(u)\,du\) for ordinary one-sided Hardy (continuous Cesàro) averaging. For each integer \(m\ge1\), define the real variation-to-error norm

\[
C_m=\sup_{f\in BV(0,1),\ V(f)>0}\frac{\|f-H^m f\|_{L^2(0,1)}}{V(f)},\qquad V(f)=|Df|(0,1).
\]

Let \(Q_m(y)=e^{-y}\sum_{k=0}^{m-1}y^k/k!\). There is exactly one positive solution \(L_m\) of

\[
\frac{2}{(m-1)!}\int_0^{L_m}y^{m-1}Q_m(y)\,dy=1.
\]

The **exact sharp constant and all equality cases** are

\[
C_m=Q_m(L_m),\qquad
f(x)=a+b\mathbf1_{(e^{-L_m},1)}(x)\quad\text{a.e.},
\]

where \(a,b\in\mathbb R\) and \(b\ne0\). In particular \(C_1=1/2\), \(L_1=\log2\), and \(C_m\) increases strictly with \(m\).

Define \(b_m=(m!/2)^{1/m}\). There is a numerical \(c>0\) such that

\[
L_m=b_m+O(e^{-cm})
=\frac m e+\frac{\log(2\pi m)-2\log2}{2e}
 +O\!\left(\frac{(\log m)^2}{m}\right).
\]

Thus the unique worst jump moves exponentially toward the left endpoint, and its squared-norm deficit obeys the sharp law

\[
\boxed{1-C_m^2\sim\frac{e}{e-1}
\left(\frac{2}{\sqrt{2\pi m}}\right)^{1/e}e^{-m/e}.}
\]

Equivalently, the location is \(e^{-L_m}\sim(2/\sqrt{2\pi m})^{1/e}e^{-m/e}\).

## Assumptions and scope

All functions are real-valued and understood up to Lebesgue-null changes. The variation is the full distributional variation on the open interval, not an endpoint-augmented variation. The norm is unweighted Lebesgue \(L^2(0,1)\). The averaging operator preserves constants, and the iteration count \(m\) is any positive integer. No smoothness beyond bounded variation is assumed; the assertion is about \(I-H^m\), not the norm of \(H^m\) itself.

## Proof

**1. Step reduction.** The distributional derivative of \(f\in BV(0,1)\) is a finite signed measure \(\mu\) and, up to a constant and null-set changes, \(f(x)=a+\int_{(0,1)}\mathbf1_{(t,1)}(x)\,d\mu(t)\). The constant term is annihilated by \(I-H^m\), and Fubini holds because the kernel is bounded. Let \(g_{m,t}=(I-H^m)\mathbf1_{(t,1)}\). Minkowski's integral inequality gives

\[
\|(I-H^m)f\|_2\le\int\|g_{m,t}\|_2\,d|\mu|(t)
\le\bigl(\sup_{0<t<1}\|g_{m,t}\|_2\bigr)V(f).
\]

Every jump is admissible, so this upper bound is an equality after taking the supremum.

**2. Gamma survival profile.** If \(U_1,\ldots,U_m\) are independent uniform \((0,1)\) variables, then \(H^mf(x)=\mathbb E[f(xU_1\cdots U_m)]\). The random variable \(G_m=-\sum\log U_j\) has Gamma density \(y^{m-1}e^{-y}/(m-1)!\). It follows exactly, for \(x>t\), that \(g_{m,t}(x)=\Pr(G_m>\log(x/t))=Q_m(\log(x/t))\), while \(g_{m,t}(x)=0\) for \(x<t\). Set \(L=\log(1/t)\). Changing variables yields

\[
\|g_{m,t}\|_2^2=R_m(L)=e^{-L}\int_0^Le^yQ_m(y)^2\,dy.
\]

**3. Unique sharp jump.** Differentiating and integrating once by parts, using \(Q_m'(y)=-y^{m-1}e^{-y}/(m-1)!\), gives the exact derivative identity

\[
R_m'(L)=e^{-L}\left[1-\frac2{(m-1)!}\int_0^Ly^{m-1}Q_m(y)\,dy\right].
\]

The bracket decreases strictly from one and eventually becomes negative: \(Q_m(y)\ge e^{-y}\), so the integral multiplier has limit at least two. Thus \(R_m\) has one and only one global maximizer \(L_m>0\). At that point \(R_m'=Q_m(L_m)^2-R_m(L_m)=0\), proving \(C_m=Q_m(L_m)\). Moreover, equality in the measure bound in Step 1 requires \(|\mu|\) to be supported where \(\|g_{m,t}\|_2=C_m\); this set consists solely of \(t=e^{-L_m}\). Therefore every nonconstant extremizer has precisely the stated single jump. For fixed \(y>0\), \(Q_{m+1}(y)>Q_m(y)\); the squared residual strictly increases at each interior jump, proving \(C_{m+1}>C_m\).

**4. Sharp large-iterate asymptotics.** Set \(b_m=(m!/2)^{1/m}\), so \(2b_m^m/m!=1\). The maximizer equation and \(Q_m\le1\) imply \(L_m\ge b_m\). Stirling gives \(b_m/m\to1/e\). Fix any sufficiently small \(\varepsilon>0\) with \((1+\varepsilon)/e<1\). The Gamma lower-tail Chernoff inequality yields \(1-Q_m((1+\varepsilon)b_m)\le e^{-c_\varepsilon m}\) for some \(c_\varepsilon>0\). Therefore the root-equation left side at \((1+\varepsilon)b_m\) is at least \((1-e^{-c_\varepsilon m})(1+\varepsilon)^m>1\), forcing \(L_m\le(1+\varepsilon)b_m\) for all large \(m\).

Since \(Q_m\) is decreasing, the same root equation implies \(1\ge Q_m(L_m)(L_m/b_m)^m\), whence

\[
0\le m\log(L_m/b_m)\le-\log Q_m(L_m)=O(e^{-c_\varepsilon m}).
\]

This proves \(L_m=b_m+O(e^{-cm})\) (possibly with a smaller positive \(c\)). Stirling expansion then gives the asserted two-term expression for \(L_m\).

To determine the leading deficit, expand the Gamma lower tail exactly:

\[
1-Q_m(L_m)=\frac{e^{-L_m}L_m^m}{m!}
\sum_{j=0}^\infty\prod_{i=1}^j\frac{L_m}{m+i}.
\]

Here the empty product is one. Since \(L_m/m\to1/e<1\), dominated convergence gives convergence of the sum to \(e/(e-1)\), while \(L_m^m/m!\to1/2\). Hence \(1-Q_m(L_m)\sim e^{-L_m}e/[2(e-1)]\). Multiplying by \(1+Q_m(L_m)\to2\) gives \(1-C_m^2\sim e^{-L_m}e/(e-1)\). Finally, Stirling converts \(e^{-L_m}\) to the displayed exponential and power prefactor. This also establishes \(C_m\uparrow1\).

## Verification

The accompanying standalone Python checker uses exact rational polynomials to verify the finite truncations of the derivative identities for \(1\le m\le22\), followed by independent numerical integration and unique-root bracketing through \(m=14\). It passed 188 assertions. For orientation: \((m,L_m,C_m)\) equals approximately \((1,0.69314718056,0.50000000000)\), \((2,1.09982031418,0.69909506974)\), \((5,2.29096922372,0.91730147219)\), and \((10,4.22843554019,0.98838733076)\). The proof of universal sharpness, equality rigidity, and the infinite-iterate asymptotic is analytic, not inferred from these finite checks.

Run \(\texttt{python3 check_hardy.py}\) in a standard Python 3 environment; no nonstandard modules are needed.

## Relationship to prior work

Leśnik and Maligranda's open-access 2014 work studies the optimal domain/range of the Cesàro map and an improved weighted Hardy inequality; the actual theorems concern function-space mapping, not sharp iterated \(BV\)-to-\(L^2\) identity defects. Curbera and Ricker's 2015 preprint develops vector-measure integral representations and structural features of Cesàro function spaces, again for different norms and questions. Alhamzi and coauthors' 2026 work derives transported Hardy \(L^p\) bounds and a resolvent application but does not yield the sharp variation-to-residual constants. A 2026 study of real-variable Cesàro operators treats spectral and invariant-subspace questions. These comparisons do not establish historical uniqueness: older or unindexed variants may exist.

## Limitations

The result uses unweighted real \(BV(0,1)\), ordinary Lebesgue \(L^2\), and positive integer powers of the classical one-sided average. It does not claim an analogous formula for arbitrary \(L^p\), weighted Hardy operators, discrete Cesàro matrices, or mixed forward/backward compositions. The asymptotic concerns the exact sharp norm as iteration increases, not convergence for a fixed input function. No independent verification is claimed.

## References

1. K. Leśnik and L. Maligranda, *Abstract Cesàro Spaces. Optimal Range*, Integral Equations and Operator Theory 81 (2015), 227–235; first online December 20, 2014. https://doi.org/10.1007/s00020-014-2203-4
2. G. P. Curbera and W. J. Ricker, *Abstract Cesàro spaces: Integral representations*, first public arXiv version December 9, 2015. https://arxiv.org/abs/1512.02760
3. G. Alhamzi et al., *Hardy Averaging via Distribution Transport: Sharp Lp Bounds, Power Weights, and a Volterra Resolvent*, Axioms 15 (2026), 391. https://doi.org/10.3390/axioms15060391
4. A. Belli et al., *Crescents and the Real Variable Cesàro Operator*, Integral Equations and Operator Theory 98 (2026), 42. https://doi.org/10.1007/s00020-026-02865-7
