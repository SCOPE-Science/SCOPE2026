# Two order transitions in endpoint positivity for four-site fractional graph heat

## Finding
Consider the four-vertex unweighted path with vertex order \(1,2,3,4\), combinatorial Laplacian \(L\), and spectral fractional-power heat family \(H_\alpha(t)=\exp(-tL^\alpha)\), where \(\alpha>0\) and \(t>0\). Write \(h_\alpha(t)=[H_\alpha(t)]_{1,4}\). Its sign as a function of positive time has the following **complete classification**:

1. For \(0<\alpha\le1\), \(h_\alpha(t)>0\) for all \(t>0\).
2. For \(1<\alpha\le2\), there is exactly one positive zero \(T_+(\alpha)\). The kernel entry is negative for \(0<t<T_+(\alpha)\) and positive for \(t>T_+(\alpha)\).
3. For \(\alpha>2\), there are exactly two positive zeros \(0<T_-(\alpha)<T_+(\alpha)\). The sign is positive on \((0,T_-(\alpha))\) and \((T_+(\alpha),\infty)\), and negative on \((T_-(\alpha),T_+(\alpha))\). Both zeros are simple.

All zeros in items 2 and 3 are precisely the positive solutions of the explicit four-exponential equation
\[
1+e^{-2^\alpha t}-\left(1+\frac1{\sqrt2}\right)e^{-(2-\sqrt2)^\alpha t}-\left(1-\frac1{\sqrt2}\right)e^{-(2+\sqrt2)^\alpha t}=0.
\]
The singular onsets at the two power thresholds are
\[
\lim_{\alpha\downarrow1}\frac{T_+(\alpha)}{\sqrt{\alpha-1}}=\sqrt{\frac{3\log2}{2}},
\qquad
\lim_{\alpha\downarrow2}\frac{T_-(\alpha)}{\alpha-2}
=\frac{(2-\sqrt2)\log(2-\sqrt2)+(2+\sqrt2)\log(2+\sqrt2)-4\log2}{12}>0.
\]
The second limit is taken from \(\alpha>2\); the first from \(\alpha>1\). This statement concerns the **single endpoint-to-endpoint entry**, not the positivity of the entire heat matrix.

## Assumptions and scope
The graph has exactly four labeled vertices in one unweighted path. The operator is the positive-semidefinite combinatorial Laplacian
\[
L=\begin{pmatrix}1&-1&0&0\\-1&2&-1&0\\0&-1&2&-1\\0&0&-1&1\end{pmatrix}.
\]
For every real \(\alpha>0\), the fractional power is defined by the spectral calculus, including \(0^\alpha=0\). Time \(t\) is a positive real number. Only \(h_\alpha(t)\), the kernel entry between the two endpoints, is classified. There are no restrictions that \(\alpha\) be an integer or at most two.

## Proof
**Step 1: exact spectral representation.** The distinct eigenvalues of \(L\) are \(0\), \(a=2-\sqrt2\), \(b=2\), and \(c=2+\sqrt2\). The \((1,4)\) entries of their spectral projections, in the same order, are \(1/4\), \(-q/4\), \(1/4\), and \(-p/4\), where \(q=1+1/\sqrt2\), \(p=1-1/\sqrt2\). Thus, for every \(\alpha>0\),
\[
4h_\alpha(t)=\Phi_\alpha(t):=1+e^{-Bt}-q e^{-At}-p e^{-Ct},\quad A=a^\alpha,\ B=b^\alpha,\ C=c^\alpha.
\]
In particular \(0<A<B<C\), \(\Phi_\alpha(0)=0\), and \(\Phi_\alpha(t)\to1\) as \(t\to\infty\).

**Step 2: sharp small-time signs.** For any scalar function \(f\) on the four eigenvalues, the \((1,4)\) entry of \(f(L)\) equals \(-f[0,a,b,c]\), the negative third divided difference. To see this, interpolate \(f\) by a cubic \(P\) on the spectrum: the cubic leading coefficient is \(f[0,a,b,c]\), while \((L^3)_{1,4}=-1\) and all smaller nonnegative powers have zero \((1,4)\) entry. For \(f(s)=s^\alpha\), the third derivative has the sign of \(\alpha(\alpha-1)(\alpha-2)\) on \(s>0\). The divided-difference sign is strict on each open order interval; for \(1<\alpha<2\), passage through the endpoint \(s=0\) is justified by the smooth approximation \(f_\delta(s)=(s+\delta)^\alpha\) and the integral divided-difference formula. Therefore
\[
(L^\alpha)_{1,4}>0\quad(1<\alpha<2),\qquad
(L^\alpha)_{1,4}<0\quad(\alpha>2).
\]
Since \(h_\alpha'(0)=-(L^\alpha)_{1,4}\), the endpoint entry is initially negative for \(1<\alpha<2\) and initially positive for \(\alpha>2\). At \(\alpha=2\), \((L^2)_{1,4}=0\) and \((L^4)_{1,4}=-6\), hence \(h_2(t)=-3t^2+O(t^3)<0\) for small \(t>0\).

**Step 3: all-time positivity below order one.** For \(0<\alpha<1\), the scalar function \(e^{-t s^\alpha}\) is a Laplace transform of a positive probability measure on \([0,\infty)\), assigning positive mass to positive \(s\). Hence \(H_\alpha(t)\) is a positive average of ordinary path heat matrices \(e^{-sL}\); their entries are all strictly positive for \(s>0\), because the graph is connected. The case \(\alpha=1\) is ordinary heat and also strictly positive.

**Step 4: no extra zeros.** A nonzero linear combination of \(m+1\) exponentials with distinct real rates has at most \(m\) real zeros counted with multiplicity: multiply by the slowest inverse exponential, differentiate, and apply Rolle's theorem inductively. Here the four rates \(0,A,B,C\) are strictly ordered; \(\Phi_\alpha\) has at most three real zeros counting multiplicities, and one is \(t=0\). For \(1<\alpha<2\), negativity near zero and positivity at infinity force at least one positive crossing, and the zero bound forces precisely one, simple. For \(\alpha=2\), the zero at the origin has multiplicity two; the same reasoning gives precisely one simple positive zero.

For every \(\alpha\ge2\), evaluating at \(t=1/B\) yields
\[
\Phi_\alpha(1/B)=1+e^{-1}-q e^{-(a/b)^\alpha}-p e^{-(c/b)^\alpha}<0.
\]
Indeed \((a/b)^\alpha\le(a/b)^2=(1-1/\sqrt2)^2\), and \(e^{-x}\ge1-x\), so \(q e^{-(a/b)^\alpha}\ge q[1-(a/b)^2]=\tfrac12+3\sqrt2/4>3/2>1+e^{-1}\). For \(\alpha>2\), strict positivity close to zero, negativity at \(1/B\), and positivity at infinity now force two positive crossings. The three-zero bound (including the zero at the origin) proves that these are the only ones and both are simple. The \(\alpha=2\) case was already covered. This proves the complete sign classification.

**Step 5: the two onset laws.** Put \(\varepsilon=\alpha-1>0\). The spectral formula is analytic in \(\alpha\) near one and \(t\) near zero. Directly from the matrix powers, \((L^3)_{1,4}=-1\). Moreover, writing \(q a=p c=1\) and \(ac=2\),
\[
\left.\partial_\alpha(L^\alpha)_{1,4}\right|_{\alpha=1}
=\frac{2\log2-\log a-\log c}{4}=\frac{\log2}{4}.
\]
Consequently
\[
h_{1+\varepsilon}(t)=-\frac{\log2}{4}\varepsilon t+\frac{t^3}{6}+O(\varepsilon^2t+\varepsilon t^2+t^4).
\]
At \(t=u\sqrt\varepsilon\), the normalized leading expression is \(-u\log2/4+u^3/6\). For \(u\) just below and above its strictly positive zero, the signs differ for sufficiently small \(\varepsilon\). Uniqueness of the positive zero forces the claimed square-root limit.

Next put \(\varepsilon=\alpha-2>0\). As \(q a^2=a\), \(p c^2=c\),
\[
D_2:=\left.\partial_\alpha(L^\alpha)_{1,4}\right|_{\alpha=2}
=\frac{4\log2-a\log a-c\log c}{4}<0.
\]
The strict inequality follows from strict convexity of \(s\mapsto s\log s\) and \((a+c)/2=2\). Since \((L^4)_{1,4}=-6\),
\[
h_{2+\varepsilon}(t)=(-D_2)\varepsilon t-3t^2+O(\varepsilon^2t+\varepsilon t^2+t^3).
\]
At \(t=u\varepsilon\) the normalized leading expression is \((-D_2)u-3u^2\). Its positive root is \((-D_2)/3\), and the first positive crossing lies between any two nearby positive test values, by the two-crossing classification. This yields the second limit.

## Verification
The self-contained analytic argument proves all signs, uniqueness, multiplicity, and asymptotics for the entire stated parameter range. The supplementary script `check.py` checks all spectral projection coefficients symbolically, verifies the relevant low powers and derivatives, and numerically tests representative power regimes and both scaling limits using high precision. Run `python check.py` with Python 3, SymPy and mpmath. Numerical experiments provide only independent consistency checks, not a substitute for the continuum argument.

## Relationship to prior work
Gregorio and Mugnolo's study of bi-Laplacians on graphs proves nonpositivity at short times and eventual positivity on finite connected graphs and displays the three-vertex path, but does not specify the four-vertex endpoint's all-power phase portrait or either critical onset coefficient. Benzi and Simunec's study of fractional graph diffusion focuses on power exponents below one and numerical computation, not the higher-order sign bifurcations here. Related published classifications for complete multipartite graphs do not cover the four-path (which is not complete multipartite), while results on rational heat-step approximants do not imply an exact exponential-semigroup classification. This proof works directly in the two-parameter spectral semigroup, without relying on such implications.

## Limitations
Only the endpoint-to-endpoint kernel entry of the **unweighted four-path** is classified. No all-entry positivity threshold, weighted-path extension, arbitrary-graph result, or analytic closed form for the positive roots is asserted. The numerical check tests finitely many parameters, whereas the proof is uniform in all positive real powers and times. Exhaustive priority over all obscure or inaccessible literature is not claimed, and independent review remains outstanding.

## References
- F. Gregorio and D. Mugnolo, *Bi-Laplacians on graphs and networks*, arXiv:1712.07370, initially posted 20 December 2017. https://arxiv.org/html/1712.07370v3
- M. Benzi and I. Simunec, *Rational Krylov methods for fractional diffusion problems on graphs*, arXiv:2012.08389, initially posted 15 December 2020. https://arxiv.org/abs/2012.08389
- J. Glück and D. Mugnolo, *Eventual domination for linear evolution equations*, Mathematische Zeitschrift (2021). https://doi.org/10.1007/s00209-021-02721-x
