# Fredholm indices and compactly stable crescents of a real-variable Cesàro operator

## Finding
Let \(1<p<\infty\), \(q=p/(p-1)\), and define on complex \(L^p(0,1)\) the bounded operator
\[
(C_pf)(x)=\frac1x\int_0^x\frac{f(t)}{1-t}\,dt.
\]
For \(r>0\), let \(\Gamma_r=\{\lambda\in\mathbb C:|\lambda-r/2|=r/2\}\). With the *Fredholm essential spectrum* defined by \(\sigma_{\mathrm{ess}}^{\mathrm F}(C_p)=\{\lambda:C_p-\lambda I\text{ is not Fredholm}\}\), the exact equality is
\[
\sigma_{\mathrm{ess}}^{\mathrm F}(C_p)=\Gamma_p\cup\Gamma_q.
\]
For \(\lambda\notin\Gamma_p\cup\Gamma_q\), put
\[
\Omega_p=\left\{\lambda\ne0:\min\{1/p,1/q\}<\operatorname{Re}(1/\lambda)<\max\{1/p,1/q\}\right\}.
\]
The complete Fredholm-index classification is
\[
\operatorname{ind}(C_p-\lambda I)=
\begin{cases}
+1,&1<p<2\ \text{and }\lambda\in\Omega_p,\\
-1,&2<p<\infty\ \text{and }\lambda\in\Omega_p,\\
0,&\lambda\notin\Gamma_p\cup\Gamma_q\cup\Omega_p.
\end{cases}
\]
For \(1<p<2\), \(C_p-\lambda I\) is onto, with a one-dimensional kernel, whenever \(\lambda\in\Omega_p\). For \(2<p<\infty\), it is one-to-one with closed codimension-one range there. For \(p=2\), the circles coincide and the index vanishes at every Fredholm point.

Consequently, for every compact \(K:L^p(0,1)\to L^p(0,1)\), the open crescent \(\Omega_p\) lies in \(\sigma(C_p+K)\), and the above nonzero indices are unchanged. In particular, \(2\) is a persistent spectral value for every \(p\ne2\), while \(C_2-2I\) is non-Fredholm.

## Assumptions and scope
All spaces are complex. Fredholm means closed range and finite-dimensional kernel and cokernel; \(\operatorname{ind}T=\dim\ker T-\operatorname{codim}\operatorname{ran}T\). The parameter range is precisely \(1<p<\infty\). The open set \(\Omega_p\) is the region inside the larger of the two disks bounded by \(\Gamma_p,\Gamma_q\), but outside the closure of the smaller; it is empty when \(p=2\). The two circles meet at \(0\), which is included in the non-Fredholm set. No assertion is made for \(p=1\) or \(p=\infty\).

## Proof
**1. Conjugacy to an invertible first-order operator.** Put \(x(u)=e^u/(1+e^u)\). The isometry \(U:L^p(0,1)\to L^p(\mathbb R)\) is given by
\[
(Uf)(u)=[x(u)(1-x(u))]^{1/p}f(x(u)).
\]
Writing \(h_p(u)=x(u)^{-1/q}(1-x(u))^{1/p}\), a direct change of variables gives
\[
(UC_pU^{-1}g)(u)=h_p(u)\int_{-\infty}^u h_p(v)^{-1}g(v)\,dv.
\]
Set \(b_p=-h_p'/h_p\). Differentiation yields the *exact* coefficient
\[
b_p(u)=\frac1q+\left(\frac1p-\frac1q\right)\frac{e^u}{1+e^u},\qquad b_-:=\lim_{u\to-\infty}b_p(u)=\frac1q,\quad b_+:=\lim_{u\to+\infty}b_p(u)=\frac1p.
\]
Define \(B_p:W^{1,p}(\mathbb R)\to L^p(\mathbb R)\) by \(B_py=y'+b_py\). Because \(b_p(u)\ge\beta:=\min\{1/p,1/q\}>0\), the displayed Volterra integral is bounded in \(L^p\) by Young's inequality with kernel \(e^{-\beta t}\mathbf1_{t\ge0}\); its output has derivative \(g-b_py\in L^p\). It is a right inverse of \(B_p\). A homogeneous solution of \(B_py=0\) is a constant multiple of \(h_p\), which diverges as \(u\to-\infty\) and hence is not in \(L^p(\mathbb R)\). Thus \(B_p\) is an isomorphism \(W^{1,p}\to L^p\), and \(UC_pU^{-1}=B_p^{-1}\) as a bounded operator on \(L^p\).

For \(\lambda\ne0\), put \(z=1/\lambda\). Importantly, the correctly typed factorization on \(L^p\) is
\[
B_p^{-1}-\lambda I=-\lambda(B_p-zI)B_p^{-1},
\]
where \(B_p^{-1}:L^p\to W^{1,p}\) is a Banach-space isomorphism. Hence \(C_p-\lambda I\) and \(B_p-zI:W^{1,p}\to L^p\) have identical Fredholm defect dimensions and index.

**2. Compact reduction to two constant tails.** Let \(b_0(u)=b_-\) for \(u<0\) and \(b_0(u)=b_+\) for \(u\ge0\). Since \(b_p-b_0\to0\) at both ends, multiplication by \(b_p-b_0\) is compact from \(W^{1,p}(\mathbb R)\) into \(L^p(\mathbb R)\): restrict to a finite interval, apply compact one-dimensional Sobolev embedding, then control the two tails by the uniform smallness of the multiplier. Fredholmness and index of \(B_p-zI\) therefore agree with those of
\[
B_0-zI=\frac{d}{du}+b_0(u)-z.
\]
For \(\operatorname{Re}z\notin\{b_-,b_+\}\), solve the inhomogeneous equation separately on the two half-lines, matching the unique continuous trace at \(u=0\). Exponential convolution with decay rate \(|b_\pm-\operatorname{Re}z|\) bounds each half-line solution in \(W^{1,p}\). A homogeneous solution on the negative half-line belongs to \(L^p\) precisely if \(\operatorname{Re}z>b_-\); on the positive half-line it belongs to \(L^p\) precisely if \(\operatorname{Re}z<b_+\). There is a free boundary coefficient on each such side, and the continuity condition imposes one scalar equation. If exactly one side has a free coefficient, matching determines it uniquely and the operator is invertible. If both sides have free coefficients, matching leaves one kernel dimension and no range obstruction. If neither side has a free coefficient, matching imposes exactly one bounded compatibility condition. Explicitly:
\[
\begin{array}{c|c|c}
\text{real part of }z&\dim\ker(B_0-zI)&\operatorname{codim}\operatorname{ran}(B_0-zI)\\\hline
\operatorname{Re}z<\min\{b_-,b_+\}\ \text{or }\operatorname{Re}z>\max\{b_-,b_+\}&0&0\\
b_-<\operatorname{Re}z<b_+&1&0\\
b_+<\operatorname{Re}z<b_-&0&1
\end{array}
\]
The preceding exponential integral constructions prove closed range in all these cases. Consequently the index is \(+1\) when \(b_-<\operatorname{Re}z<b_+\), \(-1\) when \(b_+<\operatorname{Re}z<b_-\), and \(0\) otherwise away from the endpoint lines.

**3. The two non-Fredholm lines.** If \(\operatorname{Re}z=b_\pm\), take normalized smooth packets \(y_R(u)=R^{-1/p}\eta((u-u_R)/R)e^{i(\operatorname{Im}z)u}\), where \(\eta\in C_c^\infty(0,1)\), \(\|\eta\|_p=1\), and the supporting intervals move far into the relevant tail as \(R\to\infty\). Then \(\|y_R\|_{W^{1,p}}\) stays bounded above and below, the supports escape, while \(\|(B_p-zI)y_R\|_p\to0\) by the cutoff derivative estimate and the convergence of \(b_p\) to \(b_\pm\). Since \(1<p<\infty\), the packets converge weakly to zero in \(W^{1,p}\). If \(B_p-zI\) were Fredholm, its bounded left inverse modulo a finite-rank projection would contradict these estimates. Thus neither limiting line consists of Fredholm points.

For \(\lambda=0\), the range of \(UC_pU^{-1}=B_p^{-1}\), viewed inside \(L^p(\mathbb R)\), is exactly \(W^{1,p}(\mathbb R)\); this dense proper subspace is not closed. Therefore \(C_p\) itself is non-Fredholm. Finally \(\operatorname{Re}(1/\lambda)=1/r\) is equivalent for nonzero \(\lambda\) to \(|\lambda-r/2|=r/2\). This proves the entire essential spectrum and index formula, including the zero endpoint.

**4. Exact defects and perturbation protection.** For \(p<2\) and \(\lambda\in\Omega_p\), an eigenvector (already present in the motivating literature) is
\[
f_\lambda(x)=x^{1/\lambda-1}(1-x)^{-1/\lambda}.
\]
For \(p>2\), letting \(z=1/\lambda\), the nonzero bounded linear functional
\[
\ell_z(g)=\int_0^1g(x)x^{-z}(1-x)^{z-1}\,dx
\]
is well defined by Hölder's inequality, since \(1/p<\operatorname{Re}z<1/q\). Direct integration shows that \(\ell_z(C_pg)=\lambda\ell_z(g)\), first on a dense set and then by continuity, so \(\operatorname{ran}(C_p-\lambda I)=\ker\ell_z\) by the codimension-one result. Standard stability of Fredholm index under compact perturbations gives the persistent-crescent assertion. At \(\lambda=2\), the line parameter is \(\operatorname{Re}z=1/2\): it lies strictly between the two endpoints for \(p\ne2\), but is a limiting line when \(p=2\).

## Verification
The proof is analytical and covers every \(1<p<\infty\), all complex spectral parameters and arbitrary compact perturbations. The standalone `checker.py` repeats \(118\) finite algebraic, geometric and quadrature diagnostics for the conjugacy coefficient, reciprocal-circle identity, and the explicit eigenvector or annihilating functional on sample parameters. The checks passed. They are **not** a proof of the Fredholm assertions, and no infinite computation is claimed.

## Relationship to prior work
Belli, Gül, Ross and Siskakis established the exact spectrum, point spectrum, norm, semigroup generator, and a related real-line representation for \(C_p\), but not the Fredholm essential spectrum or its index (their Theorem 1.3, Sections 4 and 8). Their earlier Hilbert-space work already gives the circle and normality at \(p=2\); that endpoint is reproduced as a consistency check, not claimed as new. General Fredholm index theory for asymptotically constant first-order differential operators, including Latushkin–Tomilov's more general dichotomy results, supplies the broad analytical framework. The explicit logistic reduction, complete index/defect classification for this operator and the compactly protected crescents are the particular conclusions established here. The Cesàro–Hardy operators of Abadías, Mahillo and Miana have a different kernel and do not directly identify these defects for \(C_p\).

## Limitations
Only the stated one-variable real-interval operator and \(1<p<\infty\) are treated; no result is claimed for arbitrary weighted Cesàro kernels, compact perturbations outside the open crescent, or essential spectra under non-Fredholm definitions. A broader unexamined special-case consequence of classical dichotomy theory could limit publication priority. The existing literature already gives the complete ordinary spectrum and the \(p=2\) normal representation, and these are not new contributions. Independent validation has not been performed.

## References
1. A. Belli, U. Gül, W. T. Ross, A. G. Siskakis, *Crescents and the real variable Cesàro operator*, arXiv:2606.08600 (first released 2026-06-07); *Integral Equations and Operator Theory* **98** (2026), article 42, https://doi.org/10.1007/s00020-026-02865-7.
2. A. Belli, U. Gül, W. T. Ross, A. G. Siskakis, *The Cesàro operator on \(L^2(0,1)\)*, arXiv:2604.19691 (2026-04-21).
3. Y. Latushkin, Y. Tomilov, *Fredholm Differential Operators with Unbounded Coefficients*, arXiv:math-ph/0308002 (2003).
4. L. Abadías, A. Mahillo, P. J. Miana, *Cesàro-Hardy operators on \(L^p[0,1]\): fine spectrum, weighted Koopman semigroups and invariant subspaces*, arXiv:2604.20408 (2026-04-22).
