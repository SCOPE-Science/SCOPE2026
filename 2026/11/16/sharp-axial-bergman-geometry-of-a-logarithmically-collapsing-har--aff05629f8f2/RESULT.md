# Sharp axial Bergman geometry of a logarithmically collapsing Hartogs cusp

## Finding

Fix a real parameter \(\alpha>1\), and consider the bounded complete Reinhardt domain
\[
\Omega_\alpha=\left\{(z,w)\in\mathbb C^2:\ |z|<1,\quad |w|<\exp\left[-\left(\log\frac{e}{1-|z|^2}\right)^\alpha\right]\right\}.
\]
Equip it with the Bergman metric normalized by \(\beta_\Omega(P;X)^2=\sum_{j,k}\partial_j\bar\partial_k\log K_\Omega(P,P)X_j\overline{X_k}\), with no additional numerical factor. Write \(\delta=1-r^2\) and \(L=\log(e/\delta)\). Then, as \(r\uparrow1\),
\[
\boxed{\ \beta_{\Omega_\alpha}((r,0);(1,0))=\frac{\sqrt{2\alpha}}{\delta}L^{(\alpha-1)/2}(1+o(1)).\ }
\]
Moreover, let \(d_{\mathrm{axis}}\) denote the intrinsic path distance *within the complex axial disk* \(\{(z,0):|z|<1\}\), using the ambient Bergman metric restricted to this disk. Then
\[
\boxed{\ d_{\mathrm{axis}}((0,0),(r,0))=\frac{\sqrt{2\alpha}}{\alpha+1}L^{(\alpha+1)/2}(1+o(1)).\ }
\]
The theorem asserts no asymptotic equality for the unrestricted ambient Bergman distance: the latter permits paths leaving the axis and is bounded above by \(d_{\mathrm{axis}}\).

## Assumptions and scope

The exponent \(\alpha\) is fixed, real and strictly greater than one; \(r\in(0,1)\) tends to one. Kernels are taken with respect to ordinary Euclidean area/volume. The Bergman metric convention is the one displayed above. The second formula concerns intrinsic axis distance, not ambient geodesic distance. Every \(o(1)\) is for the fixed-\(\alpha\) limit. The restriction \(\alpha>1\) matters: the concentration parameter in the proof tends to infinity only in this range. At the excluded endpoint \(\alpha=1\), direct beta-function evaluation gives the different exact metric \(\beta((r,0);(1,0))=2/(1-r^2)\), so the parameter and boundary limits do not commute.

## Proof

**Step 1: exact diagonal kernel and a discrete variance.** Put \(v(s)=\exp[-2(\log(e/(1-s)))^\alpha]\) for \(0\le s<1\), and define
\[
\mu(t)=\int_0^1 s^t v(s)\,ds\qquad(t\ge0).
\]
Rotational orthogonality on the Reinhardt domain shows that every Bergman monomial involving a positive power of \(w\) vanishes on \(w=0\); the squared norm of \(z^n\) equals \(\pi^2\mu(n)\). Thus, for \(s=|z|^2\),
\[
K_{\Omega_\alpha}((z,0),(z,0))=\pi^{-2}\sum_{n\ge0}\frac{s^n}{\mu(n)}.
\]
For \(x=-\log s>0\), set \(a(t)=-\log\mu(t)\), \(Z(x)=\sum_{n\ge0}\exp[a(n)-xn]\), and \(p_x(n)=\exp[a(n)-xn]/Z(x)\). The series and its derivatives converge locally uniformly for \(x>0\), since the interval \(1/(n+1)\le1-s\le2/(n+1)\) gives \(\mu(n)\ge c(n+1)^{-1}\exp[-C(\log(n+2))^\alpha]\), hence \(a(n)=O((\log(n+2))^\alpha)=o(n)\). Direct differentiation yields the **exact identity**
\[
\beta_{\Omega_\alpha}((r,0);(1,0))^2=\frac{\operatorname{Var}_{p_x}(N)}{r^2},\qquad x=-\log(r^2).
\tag{1}
\]
Indeed \(\partial_z\bar\partial_z\log Z(-\log|z|^2)=\operatorname{Var}_{p_x}(N)/|z|^2\).

**Step 2: concentration of the continuous moment integral.** Change variables \(q=1-s\). Then \(\mu(t)=\int_0^1e^{H_t(q)}\,dq\) with
\[
H_t(q)=t\log(1-q)-2\left(\log\frac e q\right)^\alpha.
\]
Its second derivative is strictly negative, so \(H_t\) has a unique maximum \(q_t\in(0,1)\), determined by
\[
\frac{tq_t}{1-q_t}=B_t,\qquad B_t=2\alpha\left(\log\frac e{q_t}\right)^{\alpha-1}.
\tag{2}
\]
Equation (2) implies \(q_t\sim B_t/t\), \(\log(e/q_t)\sim\log t\), and \(B_t\sim2\alpha(\log t)^{\alpha-1}\to\infty\). The second-derivative identity at the mode gives
\[
-\frac{q_t^2H_t''(q_t)}{B_t}=1+O\!\left(\frac1{\log t}+\frac{B_t}t\right)\longrightarrow1.
\tag{3}
\]
We record the standard one-dimensional Laplace conclusion *with the necessary moment control*. If \(Q_t\) has density proportional to \(e^{H_t(q)}\), then
\[
Y_t=\sqrt{B_t}\left(\frac{Q_t}{q_t}-1\right)\Longrightarrow\mathcal N(0,1),\quad \mathbb E Y_t\to0,\quad\mathbb E Y_t^2\to1.
\tag{4}
\]
Here is an explicit justification of the tails, not only a pointwise quadratic expansion. On \(q=q_t(1+y/\sqrt{B_t})\) with \(y\) in a fixed compact set, Taylor's formula and (3) give \(H_t(q)-H_t(q_t)=-y^2/2+o(1)\), uniformly. On each fixed interval \(q/q_t\in[\eta,\eta^{-1}]\), where \(0<\eta<1\), the normalized logarithmic profile obeys
\[
\frac{H_t(q_ty)-H_t(q_t)}{B_t}=1-y+\log y+o(1)\quad(\eta\le y\le\eta^{-1}),
\]
uniformly. This function is strictly negative away from one. Outside such a central interval, strict concavity gives an exponentially decaying one-sided tangent bound at the interval endpoints, with slopes of magnitude comparable to \(B_t/q_t\); the original \(t\log(1-q)\) term controls the far endpoint \(q\uparrow1\). These bounds make every fixed polynomial moment of \(Y_t\) uniformly integrable and prove (4) by dominated convergence. Since \(q_t\to0\), the same estimates justify the Taylor expansion \(-\log(1-Q_t)=Q_t+O(Q_t^2)\), including its second centered moment. Differentiating \(a=-\log\mu\) under the integral gives
\[
 a'(t)=\mathbb E[-\log(1-Q_t)],\qquad a''(t)=-\operatorname{Var}[-\log(1-Q_t)].
\]
By (2)–(4),
\[
 a'(t)\sim\frac{2\alpha(\log t)^{\alpha-1}}t,\qquad
 a''(t)\sim-\frac{2\alpha(\log t)^{\alpha-1}}{t^2}.
\tag{5}
\]
In particular \(a\) is strictly concave and \(a'(t)\searrow0\).

**Step 3: concentration of the discrete reciprocal-moment series.** For sufficiently small \(x>0\), let \(t_x>0\) be the unique solution of \(a'(t_x)=x\). From (5),
\[
 t_x\sim\frac{2\alpha}{x}(\log(1/x))^{\alpha-1},\quad
 \sigma_x^2:=\frac1{-a''(t_x)}\sim\frac{2\alpha}{x^2}(\log(1/x))^{\alpha-1},\quad
 \frac{\sigma_x}{t_x}\to0.
\tag{6}
\]
On each compact set of real \(y\), (5) gives \(a''(t_x+\sigma_xy)/a''(t_x)\to1\) uniformly, since \(\sigma_x/t_x\to0\). Twice integrating the second derivative therefore gives
\[
 a(t_x+\sigma_xy)-x(t_x+\sigma_xy)
 -[a(t_x)-xt_x]=-y^2/2+o(1).
\tag{7}
\]
The mesh of integers in the \(y\)-scale tends to zero because \(\sigma_x\to\infty\). Concavity of \(a(t)-xt\) gives the required tails: beyond each \(t_x\pm R\sigma_x\), tangent-line majorants have slopes with magnitude at least \((R+o(1))/\sigma_x\), while (7) bounds the value at the tangency points by \(-R^2/2+o(1)\) relative to the maximum. The resulting geometric tails, after normalization by the central sum of order \(\sigma_x\), make the second centered moments uniformly integrable as \(R\to\infty\). Consequently the discrete law obeys
\[
 (N-t_x)/\sigma_x\Longrightarrow\mathcal N(0,1),\qquad
 \operatorname{Var}_{p_x}(N)\sim\sigma_x^2.
\tag{8}
\]
This proves a genuine infinite-series asymptotic; no finite truncation has been used as proof.

**Step 4: geometric conclusions.** Combine (1), (6) and (8), and use \(x=-\log r^2\sim1-r^2=\delta\) together with \(\log(1/x)=\log(e/\delta)+O(1)\). This yields the first boxed formula. Rotational symmetry makes the induced metric on the axis radial. Every piecewise smooth path in the axis from zero to radius \(r\) has length at least the radial integral \(\int_0^r\beta_{\Omega_\alpha}((t,0);(1,0))\,dt\), attained by the straight radial segment. As \(dL/dt=2t/(1-t^2)\), the first formula and integration of a regularly varying power give
\[
\int_0^r\beta_{\Omega_\alpha}((t,0);(1,0))\,dt
\sim\frac{\sqrt{2\alpha}}2\int^L y^{(\alpha-1)/2}\,dy
=\frac{\sqrt{2\alpha}}{\alpha+1}L^{(\alpha+1)/2}.
\]
This completes the proof.

## Verification

The exact identity (1), the mode equation (2), the curvature computation (3), and the double concentration mechanism (4)–(8) provide independently checkable analytic proof steps. `CHECK.py` reproduces finite quadrature and discrete variance consistency tests for selected fixed parameters. Numerical tests illustrate the slowly converging limit, not its validity for every parameter or arbitrarily small boundary scale. Run `python CHECK.py` with NumPy and SciPy as specified in `requirements.txt`.

## Relationship to prior work

Chen and Xiong's 2026 Hartogs-cusp paper introduces **exactly the domain above** and proves the upper comparison for the axial Bergman metric in Lemma 7.3, together with an upper bound for the ambient distance in Theorem 1.4. Its section 7 does not assert the asymptotic coefficient or a matching lower estimate for the axial metric. The present theorem strengthens that **metric estimate** to a sharp asymptotic, and obtains an intrinsic-axis path-length equivalent; it does not upgrade their ambient-distance bound to an ambient asymptotic. Byun–Cho–Lee (2021) studies comparability of the Bergman metric for exponentially weighted disk spaces, not a reported exact coefficient for this logarithmically flat weight. Arroussi (2021) develops reproducing-kernel and operator bounds for exponential-type weights. Jaiswal (2023 preprint, 2025 publication) proves exact metric scaling for *smooth exponentially flat boundary points* with a different local defining-function geometry; his theorem's hypotheses do not include the nonsmooth collapsed Hartogs rim considered here.

## Limitations

The parameter \(\alpha\) must stay fixed above one. The rate of the remainder is not quantified. The result concerns the axial restriction, not arbitrary tangent directions or the full ambient Bergman distance. Existing broad weighted-kernel theorems might permit an alternative proof. A 2021 article on the exponentially weighted disk metric was accessible through metadata and its comparability abstract, not full primary text; an exact specialized coefficient there or in differently indexed literature remains a priority risk. No external independent mathematical audit is claimed.

## References

1. Bo-Yong Chen and Yuanpu Xiong, *Quantitative hyperconvexity and the Bergman distance*, arXiv:2610.34339v1, first public 2026-10-25, especially Theorem 1.4 and §7, https://arxiv.org/html/2610.34339v1.
2. Ravi Shankar Jaiswal, *Asymptotic behaviour of the Bergman kernel and metric*, arXiv:2311.01097v1 (2023-11-02), https://arxiv.org/pdf/2311.01097, published as *Asymptotic Behavior of the Bergman Metric at Infinite Type Points*, Bull. London Math. Soc. 57 (2025), doi:10.1112/blms.70100.
3. Hicham Arroussi, *Bergman spaces with exponential type weights*, J. Inequal. Appl. 2021:193, doi:10.1186/s13660-021-02726-4.
4. Jisoo Byun, Hong Rae Cho and Han-Wool Lee, *The Bergman Metric and Related Bloch Spaces on the Exponentially Weighted Bergman Space*, East Asian Math. J. 37 (2021), 19–32, https://www.kci.go.kr/kciportal/landing/article.kci?arti_id=ART002682204.
