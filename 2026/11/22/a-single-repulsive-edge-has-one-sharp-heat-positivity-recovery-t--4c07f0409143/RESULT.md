# A single repulsive edge has one sharp heat-positivity recovery time on square bicliques

## Finding
Let \(K_{m,m}\), \(m\ge2\), have a distinguished crossing edge \(\{u,v\}\) of conductance \(-a\) and all other crossing edges of conductance \(1\). Use the signed row-sum Laplacian \(L\), i.e. \(L_{ij}=-w_{ij}\) for \(i\ne j\) and \(L_{ii}=\sum_{j\ne i}w_{ij}\). Write \(H(t)=e^{-tL}\), \(a_c=(m-1)^2/(2m-1)\), and \(F(t)=H(t)_{uv}\).

For \(0<a<a_c\), \(H(t)\) is positive definite and has every off-diagonal entry strictly positive for \(t>0\), except possibly \(H(t)_{uv}=H(t)_{vu}\). There is exactly one \(T>0\) such that
\[
F(t)<0\ (0<t<T),\qquad F(T)=0,\qquad F(t)>0\ (t>T).
\]
Consequently, its **exact whole-matrix entrywise positivity horizon** is \(T\), and
\[
\|H(t)\|_{\ell^\infty\to\ell^\infty}=\|H(t)\|_{\ell^1\to\ell^1}=1+2[-F(t)]_+.
\]
Define \(\tau=1+a\), \(\Delta=\sqrt{(m-2+2\tau)^2+4(m-1)}\),
\[
\lambda_\pm=\frac{3m-2\tau\pm\Delta}{2},\qquad w=\frac{\lambda_+-(m+1-2\tau)}{\Delta}.
\]
The unique horizon \(T\) is the positive root of the explicit four-exponential equation
\[
\frac1m+\left(1-\frac1m\right)e^{-mT}
=w e^{-\lambda_-T}+(1-w)e^{-\lambda_+T}.
\]
Writing \(w_c=(2m-1)^2/[m(4m-3)]\), its two sharp parameter endpoints are
\[
T\sim\frac{\sqrt{6a}}{m-1}\quad(a\downarrow0),\qquad
\lim_{a\uparrow a_c}(a_c-a)T=\frac{\log(mw_c)}{2w_c}>0.
\]
For \(a\ge a_c\), the distinguished transition \(F(t)\) is strictly negative for every \(t>0\), so no recovery occurs. These statements include \(m=2\).

## Assumptions and scope
All matrices act on the finite-dimensional real Hilbert space \(\ell^2(V)\) of the \(2m\) vertices. The graph and the semigroup use signed conductances in the *row-sum* Laplacian convention, not the unsigned signless or twisted-signed Laplacian. Time \(t\) is strictly positive except where \(t=0\) is stated. The sharp positive recovery horizon is asserted for each integer \(m\ge2\) and real \(0<a<a_c\); the no-recovery statement is for all \(a\ge a_c\).

## Proof
**1. Symmetry reduction and exact exceptional entry.** Let \(P_0\) and \(Q_0\) be the remaining \(m-1\) vertices on the two sides. In the orthonormal basis consisting of
\[
x=(e_u+e_v)/\sqrt2,\quad y=(e_u-e_v)/\sqrt2,\quad
p=(\mathbf1_{P_0}+\mathbf1_{Q_0})/\sqrt{2(m-1)},\quad
q=(\mathbf1_{P_0}-\mathbf1_{Q_0})/\sqrt{2(m-1)},
\]
the compressed Laplacian is the direct sum
\[
L_+=\begin{pmatrix}m-1&-\sqrt{m-1}\\-\sqrt{m-1}&1\end{pmatrix},\qquad
L_-=\begin{pmatrix}m+1-2\tau&\sqrt{m-1}\\\sqrt{m-1}&2m-1\end{pmatrix},
\]
and on the orthogonal complement it equals \(mI\). The eigenvalues of \(L_+\) are \(0,m\), while those of \(L_-\) are \(\lambda_-<\lambda_+\) above. Since
\[
\lambda_-\lambda_+=2[m^2-\tau(2m-1)],
\]
one has \(0<\lambda_-<m<\lambda_+\) exactly when \(0<a<a_c\). The \(yy\)-entry of \(e^{-tL_-}\) is \(w e^{-\lambda_-t}+(1-w)e^{-\lambda_+t}\), with \(0<w<1\); the \(xx\)-entry of \(e^{-tL_+}\) is \(m^{-1}+(1-m^{-1})e^{-mt}\). Therefore
\[
2F(t)=m^{-1}+(1-m^{-1})e^{-mt}-w e^{-\lambda_-t}-(1-w)e^{-\lambda_+t}.\tag{1}
\]
Here \(F(0)=0\), \(F'(0)=-a\), and in the stable region \(\lim_{t\to\infty}F(t)=1/(2m)\).

**2. The unique sign recovery.** In the stable region, differentiating (1) and multiplying by \(2e^{mt}\) gives
\[
h(t)=w\lambda_-e^{(m-\lambda_-)t}+(1-w)\lambda_+e^{-(\lambda_+-m)t}-(m-1).
\]
The function \(h\) is strictly convex on \([0,\infty)\), satisfies \(h(0)=-2a<0\), and tends to \(+\infty\). Therefore its nonpositive sublevel set is exactly an initial bounded interval, and \(F'\) has one and only one positive zero: the unique strict minimum of \(F\). Since \(F(0)=0>F\) at that minimum and \(F(\infty)>0\), equation (1) has exactly one positive root \(T\), and the sign assertions follow. If \(a=a_c\), then \(\lambda_-=0\) and \(F'(t)<0\) for every positive \(t\): the remaining positive derivative term decays more rapidly than the negative \(e^{-mt}\) term and already loses at \(t=0\). For \(a>a_c\), use strict monotonicity in the antagonism parameter. Since \(\partial_a L=-(e_u-e_v)(e_u-e_v)^T\), the Duhamel formula gives
\[
\partial_a F(t)=\int_0^t[H(t-s)(e_u-e_v)]_u[H(s)(e_u-e_v)]_v\,ds<0.
\]
Indeed the involution exchanging the two sides sends \(u\) to \(v\), so the second factor equals \(-[H(s)(e_u-e_v)]_u\); the first factor is positive, because \(2[H(s)(e_u-e_v)]_u=(e_u-e_v)^TH(s)(e_u-e_v)>0\) for every \(s>0\). Hence \(F(t,a)<F(t,a_c)<0\) for all \(t>0\) and all \(a>a_c\), independently of spectral instability. This proves no recovery beyond the threshold.

**3. The remaining entries are strictly positive.** For the stable region, the \(xp\)-entry of \(e^{-tL_+}\) is \(\sqrt{m-1}(1-e^{-mt})/m\), whereas the \(yq\)-entry of \(e^{-tL_-}\) is \(-\sqrt{m-1}(e^{-\lambda_-t}-e^{-\lambda_+t})/(\lambda_+-\lambda_-)\). Thus the entries joining \(u\) to a vertex of \(P_0\) equal one half of
\[
W(t)=\frac{1-e^{-mt}}m-\frac{e^{-\lambda_-t}-e^{-\lambda_+t}}{\lambda_+-\lambda_-}.
\]
Its Laplace transform is
\[
\widehat W(s)=\frac{(\lambda_-+\lambda_+-m)s+\lambda_-\lambda_+}{s(s+m)(s+\lambda_-)(s+\lambda_+)}.
\]
Both coefficients in the numerator are strictly positive, because \(\lambda_-\lambda_+>0\) and \(\lambda_-+\lambda_+-m=2(m-\tau)>0\). The two terms are positive multiples of convolutions of positive exponential functions, so \(W(t)>0\) for every \(t>0\). Entries joining \(u\) to \(Q_0\) are the corresponding *sum* of two positive quantities and are strictly positive. Symmetry handles \(v\).

For a vertex in \(P_0\) and one in \(Q_0\), the entry equals
\[
\frac{(e^{-tL_+})_{pp}-(e^{-tL_-})_{qq}}{2(m-1)}.
\]
The first numerator term is \((m-1)/m+e^{-mt}/m\). Writing \((e^{-tL_-})_{qq}=\rho e^{-\lambda_-t}+(1-\rho)e^{-\lambda_+t}\), the slow-mode weight is
\[
\rho=\frac{m-1}{(2m-1-\lambda_-)^2+(m-1)}\le\frac1m\le\frac{m-1}{m}.
\]
Since \(\lambda_+>m\) and \(\lambda_->0\), this is at most \(\rho+(1-\rho)e^{-mt}\), strictly smaller than \((m-1)/m+e^{-mt}/m\) for positive \(t\). Hence these cross-group entries are positive.

For two distinct vertices in the same group \(P_0\) or \(Q_0\), the entry equals
\[
\frac{(e^{-tL_+})_{pp}+(e^{-tL_-})_{qq}-2e^{-mt}}{2(m-1)}.
\]
It is positive when \(\tau=0\), because that is the ordinary connected positive-conductance biclique. Moreover its derivative in \(\tau\) is strictly positive: the Duhamel formula gives
\[
\frac{\partial}{\partial\tau}(e^{-tL_-})_{qq}=2\int_0^t(e^{-(t-s)L_-})_{qy}(e^{-sL_-})_{yq}\,ds>0,
\]
as both off-diagonal factors are strictly negative. This establishes positivity for every \(\tau=1+a>0\), including the case where a given group has no two distinct vertices. All diagonal entries are positive because \(e^{-tL}\) is positive definite. Thus the **only** possibly negative entries of the entire matrix are the two distinguished ones.

**4. Exact endpoint norms and scaling.** As \(L\mathbf1=0\), every row and column of \(H(t)\) sums to one; all off-diagonal entries except the two distinguished ones are nonnegative. Absolute row/column sums therefore equal one outside the distinguished endpoints and equal \(1+2[-F(t)]_+\) at them, proving the norm formula. The norm has one strict maximum, at the unique minimum time of \(F\), for \(0<a<a_c\).

When \(a\downarrow0\), the distinguished edge is deleted, so the shortest paths from \(u\) to \(v\) have length three, and there are exactly \((m-1)^2\) such paths. Consequently the jointly analytic expansion at \((t,a)=(0,0)\) is
\[
F(t)=-at+O(at^2)+\frac{(m-1)^2}{6}t^3+O(at^3+t^4).
\]
The unique positive root hence has \(T\sim\sqrt{6a}/(m-1)\). At the opposite boundary, let \(\varepsilon=a_c-a\downarrow0\). The small eigenvalue and its spectral weight satisfy
\[
\lambda_-=2w_c\varepsilon+O(\varepsilon^2),\qquad w=w_c+O(\varepsilon),\qquad m w_c>1.
\]
At the unique root \(T\), the terms containing \(e^{-mT}\) and \(e^{-\lambda_+T}\) are negligible; thus \(e^{-\lambda_-T}\to1/(mw_c)\) and \(\varepsilon T\to\log(mw_c)/(2w_c)\). This proves both sharp asymptotics.

## Verification
The reproducible file `check_signed.py` builds the full signed Laplacians, diagonalizes them, checks the four-dimensional reduction, the unique recovery root, all other transition signs, the exact endpoint norms and both scaling limits for several sizes and parameter regimes. It reports **60,817 successful supplementary assertions** in the captured run. The analytical proof above, not finite enumeration, establishes the infinite family of sizes, all positive real times and all allowed real parameters.

## Relationship to prior work
Chen et al. (2020 preprint; 2021 journal) establish the equivalence of signed-Laplacian spectral stability and eventual exponential positivity, including general conductance-based conditions. Song, Hill and Liu (2019 preprint) study effective-resistance conditions and signed Laplacian definiteness. Fontan and Altafini (2021) develop related eventual-positivity structure. These works support qualitative eventual positivity and the known stability boundary; they do not directly give the present **all-entry sign census**, the **one-crossing recovery equation**, the **exact transient induced norm**, or the **square-root and inverse-distance endpoint laws** on the signed biclique family. The signed-triangle analogue and fractional signed-cycle/complete-network results treat nonidentical graph families or different semigroups and do not imply the biclique formula. Broad historical priority beyond inspected sources remains unverified.

## Limitations
The family is restricted to a square biclique with one negative crossing edge and all other crossing weights exactly one. The theorem does not classify rectangular bicliques, multiple negative edges or nonsymmetric generators. The recovery time is defined by a unique transcendental root rather than generally expressible in elementary closed form. Supplementary numerical checks cannot certify the continuum of parameters; they are separate from the analytical proof. No independent mathematical audit has been performed.

## References
- Y. Song, D. J. Hill, T. Liu, *On Extension of Effective Resistance with Application to Graph Laplacian Definiteness and Power Network Stability* (first public 18 June 2019), https://arxiv.org/abs/1906.07632.
- W. Chen et al., *On Spectral Properties of Signed Laplacians with Connections to Eventual Positivity* (first public 8 September 2020), https://arxiv.org/abs/2009.03581.
- A. Fontan, C. Altafini, *On the properties of Laplacian pseudoinverses* (first public 29 September 2021), https://arxiv.org/abs/2109.14587.
