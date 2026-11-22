# Sharp quadratic small-area law for the third radial Fock localization eigenvalue

## Finding
Let \(\mathcal F\) be the analytic Fock space with norm \(\|F\|^2=\int_{\mathbb C}|F(z)|^2e^{-\pi|z|^2}\,dA(z)\), and let \(T_\Omega=P\mathbf1_\Omega\) be the positive localization Toeplitz operator for a circularly symmetric measurable set \(\Omega\subset\mathbb C\) of area \(s>0\). Denote its third largest eigenvalue, with multiplicity, by \(\lambda_3(T_\Omega)\), and set
\[
M_3(s)=\sup_{\Omega\text{ circularly symmetric},\ |\Omega|=s}\lambda_3(T_\Omega).
\]
Let \(\tau\in(1,2)\) be the unique solution of \((2-\tau)e^\tau=2\), and define
\[
A=e^{-\tau},\quad B=\tfrac12\tau^2 e^{-\tau},\quad
c=\frac{B}{1+B-A},\quad p=\frac{B-A}{1+B-A}.
\]
Then \(c=0.2446018030\ldots\), \(p=0.0519745263\ldots\), and
\[
\boxed{M_3(s)=c\,s-\frac{cp^2}{2}s^2+o(s^2)\qquad(s\downarrow0).}
\]
The positive sharp quadratic deficit coefficient is \(cp^2/2=0.0003303777101\ldots\). An explicit asymptotically second-order optimal set consists of a disk and a disjoint concentric annulus. In squared-radius coordinates \(t=\pi|z|^2\), it has radial set
\[
E_s=[0,p_s s]\cup[\tau-\tfrac12(1-p_s)s,\ \tau+\tfrac12(1-p_s)s],\qquad
p_s=p+\frac{p^2s}{2(1-A+B)}.
\]
For every positive \(s\), one has the global sharp linear envelope \(M_3(s)<cs\), and the displayed family attains the quadratic expansion. Moreover, if radial sets \(E_s\) satisfy \(|E_s|=s\) and \(\lambda_3(T_{E_s})=M_3(s)+o(s^2)\), then for every fixed \(\delta\in(0,\tau/3)\),
\[
\frac1s\left|\left(E_s\cap[0,\delta]\right)\mathbin{\triangle}[0,ps]\right|\longrightarrow0.
\]
Thus the second-order optimality criterion forces an asymptotically filled central disk of precisely the prescribed first-order area fraction. This latter assertion is stronger than mere weak concentration of radii at zero.

## Assumptions and scope
The supremum is over all measurable radial sets (including disconnected sets), centered at any point by unitary translation. The radial coordinate \(t=\pi|z|^2\) turns Euclidean area into Lebesgue length: \(|\Omega|=|E|\). On the normalized monomial basis, the operator is diagonal with values
\[
L_j(E)=\int_E f_j(t)\,dt,\qquad f_j(t)=e^{-t}t^j/j!,\quad j=0,1,\ldots,
\]
and \(\lambda_3\) means the third largest of these values, not the third basis coefficient by definition. The expansion is at fixed Fock scale and \(s\downarrow0\); it is not a claim about arbitrary nonradial observation masks or exact finite-area optimizer uniqueness.

## Proof
**1. Exact dual certificate.** The equation \((2-\tau)e^\tau=2\) has exactly one solution in \((1,2)\): \((2-t)e^t\) rises on \((0,1)\) and falls on \((1,2)\), with values \(2,e,0\) at \(0,1,2\). Put \(h(t)=c f_0(t)+(1-c)f_2(t)\). Then the identities \(c=B/(1+B-A)\) and \((2-\tau)e^\tau=2\) imply
\[
h(0)=h(\tau)=c,\qquad h'(\tau)=0.
\]
In fact \(h(t)\le c\) for every \(t\ge0\), with equality exactly at \(0,\tau\): the sign of \(h'(t)\) is that of the concave quadratic \((1-c)(t-t^2/2)-c\), whose positive roots are \(2-\tau\) and \(\tau\). It is negative, positive, negative on the three consecutive intervals. Thus
\[
g(t):=c-h(t)\ge0,\quad g^{-1}(0)=\{0,\tau\},\quad g(t)=ct+O(t^2)\ (t\downarrow0),\quad\lim_{t\to\infty}g(t)=c.
\]
Consequently \(cL_0(E)+(1-c)L_2(E)\le cs\) for every measurable \(E\) of length \(s\), strictly for \(s>0\).

**2. Excluding other modes near the sharp level.** The peaks of the Poisson densities for \(j\ge3\) obey
\[
\sup_{t\ge0}f_j(t)=e^{-j}j^j/j!\le (9/2)e^{-3}=0.2240418\ldots<c.
\]
The inequality follows because the displayed peak sequence decreases strictly with integer \(j\), as its successive ratio is \(e^{-1}(1+1/j)^j<1\). Thus \(L_j(E)\le(9/2)e^{-3}s\) for all \(j\ge3\). Whenever \(\lambda_3(E)\) is sufficiently close to \(cs\), its three largest eigenvalues must be \(L_0,L_1,L_2\), so \(\lambda_3(E)\le\min(L_0,L_2)\le cL_0+(1-c)L_2\le cs\). If \(\lambda_3\) is below the high-mode bound, it is already strictly below \(cs\). This proves the global strict linear envelope.

**3. Two-band lower expansion.** Write \(p=(B-A)/(1+B-A)\) so that
\[
p+(1-p)A=(1-p)B=c,\qquad (1-p)\tau A=(2/\tau)c>c.
\]
Set \(u=p^2/[2(1-A+B)]\) and \(p_s=p+us\). For sufficiently small positive \(s\), the displayed two disjoint intervals have total length \(s\). Taylor's theorem at \(0\) and symmetry about \(\tau\) give
\[
\begin{aligned}
L_0(E_s)&=cs+[u(1-A)-p^2/2]s^2+O(s^3),\\
L_2(E_s)&=cs-uB s^2+O(s^3),\\
L_1(E_s)&=(2c/\tau)s+O(s^2).
\end{aligned}
\]
Since \(u(1-A+B)=p^2/2\) and \(c=B/(1-A+B)\), both first two displayed expansions equal \(cs-cp^2s^2/2+O(s^3)\). The first-mode gap and the high-mode bound show the third-largest eigenvalue is the smaller of \(L_0,L_2\) for small \(s\). Therefore \(M_3(s)\ge cs-cp^2s^2/2+O(s^3)\).

**4. Second-order upper expansion.** Choose any sequence \(s_n\downarrow0\) and near-maximizers \(E_n\) of length \(s_n\) whose third eigenvalue differs from \(M_3(s_n)\) by \(o(s_n^2)\) (the supremum need not be attained). Step 3 implies \(\lambda_3(E_n)/s_n\to c\). By Step 2, \(L_0(E_n)/s_n,L_2(E_n)/s_n\ge c-o(1)\). Their convex average is \(c-\int_{E_n}g/s_n\le c\), forcing both normalized masses to converge to \(c\) and \(\int_{E_n}g/s_n\to0\). As \(g\) is continuous and strictly positive away from \(\{0,\tau\}\), with positive tail limit, the probability measures \(s_n^{-1}\mathbf1_{E_n}(t)dt\) concentrate on \(\{0,\tau\}\). Their mass at \(\tau\) must be \(c/B=1-p\) because \(f_2(0)=0\), so their mass at \(0\) is \(p\). In particular, for fixed \(\delta\in(0,\tau/3)\),
\[
m_n:=|E_n\cap[0,\delta]|=(p+o(1))s_n.
\]
For each \(\varepsilon>0\), choose \(\delta\) small enough that \(g(t)\ge(c-\varepsilon)t\) on \([0,\delta]\). The one-dimensional bathtub inequality \(\int_F t\,dt\ge|F|^2/2\) for \(F\subset[0,\infty)\) yields
\[
cs_n-\lambda_3(E_n)\ge\int_{E_n}g(t)dt\ge(c-\varepsilon)m_n^2/2.
\]
Divide by \(s_n^2\), pass to a lower limit, then let \(\varepsilon\downarrow0\). This proves \(\liminf_{s\downarrow0}[cs-M_3(s)]/s^2\ge cp^2/2\); the lower construction gives the reverse bound, proving the expansion.

**5. Rigidity of the central disk to second order.** Consider a family achieving the second-order optimum up to \(o(s^2)\). The sharp upper coefficient gives \(\int_{E_s}g=cp^2s^2/2+o(s^2)\): the deficit is at least the sharp value from Step 4 and at most the spectral deficit by the convex-combination inequality. Fix \(\varepsilon>0\) and choose a small \(\delta'>0\) with \(g(t)\ge(c-\varepsilon)t\) on \([0,\delta']\). For \(F_s=E_s\cap[0,\delta']\) and \(m_s=|F_s|=(p+o(1))s\), the preceding upper bound and the bathtub inequality show
\[
0\le\limsup_{s\downarrow0}\frac{\int_{F_s}t\,dt-m_s^2/2}{s^2}
\le\frac{p^2\varepsilon}{2(c-\varepsilon)}.
\]
For every measurable \(F\subset[0,\infty)\) of length \(m\),
\[
\int_Ft\,dt-\frac{m^2}{2}\ge\frac14\big|F\mathbin{\triangle}[0,m]\big|^2.
\]
Indeed, transfer any missing mass \(d\) from the left interval to the right; the least possible transport cost is \(d^2\), and the symmetric difference has length \(2d\). Consequently \(\limsup |F_s\triangle[0,m_s]|/s\le p\sqrt{2\varepsilon/(c-\varepsilon)}\). Sending \(\varepsilon\downarrow0\) proves the scaled symmetric-difference limit for the correspondingly shrinking \(\delta'\). For any larger fixed \(\delta<\tau/3\), the additional area in \(E_s\cap[\delta',\delta]\) is \(o(s)\) by the two-point weak concentration from Step 4. Since \(|m_s-ps|=o(s)\), the result holds with \([0,ps]\) and the stated arbitrary fixed \(\delta\).

## Verification
`check_fock_third.py` is a self-contained standard-library diagnostic. It checks the root and dual identities, samples the dual inequality, evaluates finite monomial eigenvalue lists for the two-band construction using elementary finite gamma sums, and tests the quadratic deficit scaling. Numerical sampling is finite and does not establish the pointwise certificate, infinite-mode bound, or rigidity, all of which have independent arguments above.

## Relationship to prior work
Nicola, Riccardi and Tilli (2025, arXiv:2503.07069, Theorem 1.3 and Remark 4.1) prove the *second*-eigenvalue annulus optimum and show qualitatively that a disk-plus-annulus mask beats the degree-two superlevel annulus for the third eigenvalue. They do not give the sharp optimized third-eigenvalue small-area coefficient or its quadratic term. The publicly available 2026 result *A two-band concentration law for vacuum and excited Gaussian Fock modes* proves a stronger two-fixed-mode first-order statement for every excited index, including the sharp leading constant \(c\), a two-point weak radial limit, and an \(O(s^2)\) remainder. These first-order facts and the origin/ring split are expressly **prior** and not claimed as new. An \(O(s^2)\) remainder, however, does not imply its coefficient, or the stronger rescaled-inner-disk rigidity when the third *ordered* eigenvalue is optimized. The present contribution is exactly those second-order statements, with a proof exploiting the linear boundary zero of the dual deficit rather than first-order concentration alone.

## Limitations
No exact maximizing set at fixed positive area, no unique global maximizing shape, and no analogous nonradial third-eigenvalue law are established. The leading constant and two-point weak concentration were previously established in a two-mode theorem; the new mathematical assertions are the sharp quadratic coefficient for the ordered third eigenvalue and its rescaled central-disk rigidity. Finite diagnostics do not prove continuous inequalities or asymptotics. Bibliographic priority beyond the inspected literature is not independently certified.

## References
1. F. Nicola, F. Riccardi and P. Tilli, *The isoperimetric inequality for partial sums of Toeplitz eigenvalues in the Fock space*, arXiv:2503.07069 (initial public version 2025-03-10), https://arxiv.org/html/2503.07069v2 .
2. *A two-band concentration law for vacuum and excited Gaussian Fock modes*, published-finding corpus mathematical record (2026-11-02), https://github.com/published-finding corpus/2026/tree/main/2026/11/2/SCOPE-a-two-band-concentration-law-for-vacuum-and-excited-gaussian-foc--c54df82037bb .
3. L. D. Abreu, *The isoperimetric inequality for the Ky Fan norm*, arXiv:2607.28376 (initial public version 2026-07-30), https://arxiv.org/abs/2607.28376 .
