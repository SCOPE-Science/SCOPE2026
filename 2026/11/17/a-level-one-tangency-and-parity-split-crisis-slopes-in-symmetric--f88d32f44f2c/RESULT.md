# A level-one tangency and parity-split crisis slopes in symmetric Lozi renormalisation

## Finding

Consider the orientation-preserving two-dimensional border-collision normal form restricted to the symmetric Lozi parameter plane \(\xi(s,d)=(s,d,-s,d)\), where \(s>1+d\) and \(d>0\). Let the renormalisation \(g\) and homoclinic-corner function \(\phi\) be as defined below. For every **fixed** integer \(n\ge1\), the equation \(\phi(g^n(\xi(s,d)))=0\) has a unique real-analytic local solution \(s=s_n(d)\) near \((s,d)=(2^{1/2^n},0)\), and

\[
s_n(d)=2^{1/2^n}-\frac{1+(-1)^n2^{1-n}}{3\,2^{1/2^n}}d+O_n(d^2).
\]

The first curve is exceptional: its entire linear displacement cancels, and the sharp first nonzero term is

\[
s_1(d)=\sqrt2+\frac{3\sqrt2}{8}d^2+O(d^3).
\]

For every fixed \(n\ge2\), the linear coefficient is strictly negative, while \(s_1(d)>\sqrt2\) for sufficiently small positive \(d\). Thus the first component-doubling boundary moves to larger slope with a quadratic onset, whereas every deeper boundary moves to smaller slope with a linear onset. The all-depth coefficient contains an explicit alternating parity correction. At each such local crossing, the previously established component theorem assigns \(2^n\) chaotic Milnor-attractor components to parameters on the lower-slope side and \(2^{n-1}\) to the higher-slope side (at strictly positive sufficiently small \(d\)).

## Assumptions and scope

The map is

\[
f_{s,d}(x,y)=\begin{cases}(sx+y+1,-dx),&x\le0,\\(-sx+y+1,-dx),&x\ge0,\end{cases}
\]

with \(s>1+d\) and \(0<d<1\). This is the positive-determinant Lozi subfamily of the border-collision normal form. Write a parameter four-tuple as \(\xi=(u,p,v,q)\). We use the **published** renormalisation and corner function, not new definitions of their underlying dynamical significance:

\[
g(u,p,v,q)=(v^2-2q,q^2,uv-p-q,pq),
\]

\[
\ell(u,p)=\frac{u+\sqrt{u^2-4p}}2,\quad
\phi(u,p,v,q)=q-\bigl(v+p+q-(1+v)\ell(u,p)\bigr)\ell(u,p).
\]

The square root is the positive real branch near the stated points. The conclusion is **pointwise in depth**: for each \(n\) there is a possibly different neighborhood of \(d=0\). It does not assert bounds uniform in \(n\) as \(d\to0\), nor interchange the limits. The parameter plane is studied only near the specified crisis curves, not over all values of \(s,d\).

## Proof

**Zero-determinant starting points.** Let \(F_n(s,d)=\phi(g^n(\xi(s,d)))\). For \(d=0\), the \(n\)-th renormalised four-tuple is \((S_n,0,-S_n,0)\), where \(S_n=s^{2^n}\). Hence

\[
F_n(s,0)=S_n^2(2-S_n).
\]

At \(s_{n,0}=2^{1/2^n}\), this vanishes and

\[
\partial_s F_n(s_{n,0},0)=-\frac{2^{n+3}}{s_{n,0}}\ne0.
\]

The real-analytic implicit function theorem gives a unique analytic curve \(s_n(d)\) for each fixed depth.

**Linear response of the renormalised traces.** Write the first and third entries of \(g^n(\xi(s,d))\) as \(U_n(s,d)\) and \(V_n(s,d)\); at \(d=0\) these are respectively \(S_n\) and \(-S_n\). The two determinant entries coincide and equal \(d^{2^n}\), so for \(n\ge1\) their first derivatives at \(d=0\) vanish. Let \(A_n=\partial_dU_n(s,0)\) and \(B_n=\partial_dV_n(s,0)\). Direct differentiation of the renormalisation gives

\[
A_1=B_1=-2,\qquad A_{n+1}=-2S_nB_n,\qquad B_{n+1}=S_n(B_n-A_n).
\]

Normalize \(a_n=s^2A_n/S_n\) and \(b_n=s^2B_n/S_n\). The recursion is constant-coefficient, \(a_{n+1}=-2b_n\), \(b_{n+1}=b_n-a_n\), with eigenvalues \(2\) and \(-1\). Solving it gives

\[
a_n=\frac{2^n+8(-1)^n}{3},\qquad
b_n=\frac{-2^n+4(-1)^n}{3}.
\]

At the corner point \((u,p,v,q)=(2,0,-2,0)\), \(\partial_u\phi=-2\) and \(\partial_v\phi=2\); the determinants have zero first derivative. Thus at \(s=s_{n,0}\),

\[
\partial_dF_n=2(B_n-A_n)=-\frac8{3s_{n,0}^2}\bigl(2^n+2(-1)^n\bigr).
\]

Implicit differentiation now yields

\[
s_n'(0)=-\frac{\partial_dF_n}{\partial_sF_n}
=-\frac{1+(-1)^n2^{1-n}}{3s_{n,0}}.
\]

For \(n=1\) the numerator is zero; for all \(n\ge2\) it is strictly positive. This proves the entire first-order formula and the opposing signs once the exceptional next term is established.

**The exceptional second derivative.** For \(n=1\), write \(H(s,d)=\phi(s^2-2d,d^2,-s^2-2d,d^2)\). Direct differentiation of its explicit radical expression at \((\sqrt2,0)\) gives

\[
H=0,\qquad H_d=0,\qquad H_{dd}=12,\qquad H_s=-8\sqrt2.
\]

Because \(s_1'(0)=0\), differentiating \(H(s_1(d),d)=0\) twice gives \(s_1''(0)=-H_{dd}/H_s=3/(2\sqrt2)\). Therefore the coefficient of \(d^2\) is \(3\sqrt2/8>0\), as claimed.

**Real component transitions.** At the zero-determinant boundary \(s=s_{n,0}\), one has \(F_{n-1}>0\) and \(F_{n+1}<0\), because their corresponding trace magnitudes are \(\sqrt2\) and \(4\). Both strict signs persist for positive sufficiently small \(d\). Since \(\partial_sF_n<0\) locally, on the lower-slope side \(F_n>0\) and \(F_{n+1}<0\), while on the higher-slope side \(F_{n-1}>0\) and \(F_n<0\). These are exactly the published \(\mathcal R_n\) and \(\mathcal R_{n-1}\) conditions. The orientation-preserving component theorem of Ghosh and Simpson gives \(2^n\) versus \(2^{n-1}\) components. At the equation itself, no new claim about a unique physical attractor is made.

## Verification

The accompanying `verify_crisis.py` performs independent symbolic differentiation of the exact \(n=1\) radical, verifies the closed linear-recurrence solutions through depth eight, and computes 18 high-precision roots of the full, **untruncated** crisis equations at depths one through six. The checker reports `LOZI_CRISIS_TANGENCY_CHECK_OK symbolic_first_levels=8 numerical_root_cases=18`. These tests are corroborating calculations; the analytic recurrence and the implicit-function proof, rather than finite tests, justify the all-depth result.

## Relationship to prior work

Ghosh and Simpson (2021/2022) established the BCNF renormalisation \(g\), the four-dimensional crisis surfaces \(\phi\circ g^n=0\), and the classification of component regions. Ghosh, McLachlan and Simpson (2024) revisited and extended their interpretation of component-doubling bifurcations. These constructions and qualitative classifications are prior results, explicitly used here. Neither inspected work states the **all-depth, closed-form determinant derivative on the symmetric Lozi slice**, nor the exceptional second-order curvature of its first boundary. The result is a new quantitative consequence of the earlier implicit formulas, rather than an independent replacement for them. Ou (2022) studied analytic parameter curves for creation of particular periodic itineraries in the orientation-preserving Lozi family; that distinct orbit-creation question does not provide the present all-depth component-boundary coefficient.

## Limitations

The source's already-known crisis functions determine the boundaries implicitly, so the claimed advance is their explicit quantified perturbation law and exceptional cancellation, not the existence of bifurcation surfaces. The error terms may depend on depth. Neither global attractor uniqueness nor behavior for negative determinant, non-small determinant, or joint limits in \(n,d\) is claimed. Equivalent unpublished or unindexed asymptotics remain possible. Independent mathematical assessment has not been carried out.

## References

1. I. Ghosh and D. J. W. Simpson, *Renormalisation of the two-dimensional border-collision normal form*, arXiv:2109.09242 (first posted 2021-09-19), especially §§2.3–2.6, equations (2.6), (2.10), (2.12)–(2.13), and Theorem 2.3. https://arxiv.org/html/2109.09242v1
2. I. Ghosh, R. I. McLachlan and D. J. W. Simpson, *The bifurcation structure within robust chaos for two-dimensional piecewise-linear maps*, arXiv:2402.05393 (first posted 2024-02-08), especially §§4–5 and equations (4.1), (5.3), (5.5). https://arxiv.org/html/2402.05393v1
3. D.-S. Ou, *Critical points in higher dimensions, I: Reverse order of periodic orbit creations in the Lozi family*, arXiv:2203.02326 (first posted 2022-03-04), §§6–7. https://arxiv.org/html/2203.02326v2
