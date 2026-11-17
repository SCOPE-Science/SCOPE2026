# Sharp bounded-variation gain of the cardinal linear-spline orthoprojector

## Finding
Let \(\phi_j(x)=(1-|x-j|)_+\), \(j\in\mathbb Z\), and let \(P\) denote the \(L^2(\mathbb R)\)-orthogonal projection onto the closed span of these unit-grid hat functions, with its canonical bounded-kernel extension to bounded measurable inputs. Write \(\operatorname{Var}(f)=|Df|(\mathbb R)\) for functions with finite distributional variation. Then
\[
\boxed{\sup_{\operatorname{Var}(f)>0}\frac{\operatorname{Var}(Pf)}{\operatorname{Var}(f)}=\sqrt3.}
\]
The supremum is attained by a single jump at any integer knot, \(f(x)=\mathbf1_{\{x\ge k\}}\). For a single jump in the interior of a unit cell, the gain is strictly below \(\sqrt3\). More precisely, for \(0\le u\le1\), let
\[
\rho=\frac{\sqrt3-\sqrt{6-3\sqrt3}}{3(\sqrt3-1)}=0.3804268441\ldots.
\]
The sharp profile for a jump at \(u\) is
\[
F(u):=\operatorname{Var}(P\mathbf1_{\{x\ge u\}})=
\begin{cases}
\sqrt3-3(\sqrt3-1)u^2,&0\le u\le\rho,\\
6u(1-u),&\rho\le u\le1-\rho,\\
\sqrt3-3(\sqrt3-1)(1-u)^2,&1-\rho\le u\le1.
\end{cases}
\]
The same sharp coefficient holds if inputs are restricted to compactly supported \(BV(\mathbb R)\cap L^2(\mathbb R)\): long interval indicators approach \(\sqrt3\), even though the one-sided jump itself is not in \(L^2(\mathbb R)\).

## Assumptions and scope
The knot spacing is one (any fixed positive common spacing is equivalent by dilation). The signal is real-valued and represented up to a.e. equality. The homogeneous variation domain consists of bounded real measurable functions \(f\) whose distributional derivative \(Df\) is a finite signed measure. This permits functions with nonzero limits at infinity; no \(L^1\) requirement is imposed on this homogeneous domain. The ordinary \(L^2\) projector agrees with the stated kernel extension on bounded \(L^2\) functions. Both input and output variation are distributional total variation on the whole real line, not periodic variation or an \(L^\infty\) norm.

## Proof
**1. Orthogonal projection and an absolutely summable inverse.** The Gram operator \(G=(\langle\phi_i,\phi_j\rangle)_{i,j\in\mathbb Z}\) has \(G_{ii}=2/3\), \(G_{i,i\pm1}=1/6\), and all other entries zero. Put \(s=\sqrt3\) and \(q=s-2\in(-1,0)\). Because \(q+q^{-1}=-4\), the exact convolution inverse is
\[
(G^{-1})_{ij}=s q^{|i-j|}.
\]
Indeed \((4g_j+g_{j-1}+g_{j+1})/6=\delta_{j0}\) for \(g_j=s q^{|j|}\). The series is absolutely summable, so for any bounded measurable input the coefficient sequence
\[
c_j(f)=\sum_{k\in\mathbb Z}s q^{|j-k|}\int_{\mathbb R}f(x)\phi_k(x)\,dx
\]
is well defined and uniformly bounded. Define \(Pf=\sum_jc_j(f)\phi_j\), a locally finite, continuous piecewise-affine spline. The Gram equations establish its agreement with the Hilbert-space orthogonal projection on \(L^2\cap L^\infty\). Since \(G\mathbf1=\mathbf1\), this extension reproduces constants.

**2. Exact step projection.** Put \(H_u(x)=\mathbf1_{\{x\ge u\}}\) for \(0\le u\le1\). Its hat moments are zero at indices \(j\le-1\), equal to \((1-u)^2/2\) at \(j=0\), equal to \(1-u^2/2\) at \(j=1\), and equal to one at indices \(j\ge2\). Define
\[
A(u)=\frac{1-2su+3(s-1)u^2}{2},\qquad B(u)=A(1-u).
\]
Direct substitution in the Gram equations gives all its projected nodal values:
\[
c_j(H_u)=\begin{cases}
A(u)q^{-j},&j\le0,\\
1-B(u)q^{j-1},&j\ge1.
\end{cases}
\]
The central difference is \(c_1-c_0=1-A-B>0\). The other differences form two alternating geometric tails. Since \((1-q)/(1-|q|)=s\), their total absolute sum is \(s(|A|+|B|)\). Hence
\[
F(u)=1-A(u)-B(u)+s\bigl(|A(u)|+|B(u)|\bigr).
\]

**3. Resolve the signs and maximize exactly.** We have
\[
A(u)+B(u)=\frac{s-1}{2}-3(s-1)u(1-u)<1.
\]
The quadratic \(A\) has exactly one zero \(\rho\) in \([0,1]\): \(A(0)=1/2>0\), \(A(1/2)<0\), \(A(1)<0\), and its parabola opens upward with no second zero in this interval. Consequently, for \(0\le u\le\rho\), \(A\ge0\ge B\); for \(\rho\le u\le1-\rho\), both are nonpositive; and the last regime is the reflection of the first. Substituting the corresponding signs yields the displayed three-piece formula. The two outer pieces do not exceed \(s\), with equality there only at \(u=0\) or \(u=1\). The middle piece is at most \(3/2<s\). Translation by an integer treats every other jump location, so \(\sup_{t\in\mathbb R}\operatorname{Var}(PH_t)=s\), with equality for single jumps precisely at knots.

**4. All finite-variation inputs and sharpness in the ordinary \(L^2\) domain.** For any input in the stated homogeneous domain, write \(\mu=Df\). Up to a constant and a.e. equality, \(f(x)=c+\int_{\mathbb R}H_t(x)\,d\mu(t)\). Absolute summability of the inverse Gram row and local finiteness of the hats justify exchanging projection with this finite signed-measure integral. Constants are reproduced; by the variation triangle inequality,
\[
\operatorname{Var}(Pf)\le\int\operatorname{Var}(PH_t)\,d|\mu|(t)
\le s|\mu|(\mathbb R)=s\operatorname{Var}(f).
\]
Equality holds for \(f=H_0\), since \(\operatorname{Var}(H_0)=1\) and \(F(0)=s\). For compactly supported inputs let \(f_N=H_0-H_N=\mathbf1_{[0,N)}\) with positive integer \(N\). Then \(\operatorname{Var}(f_N)=2\). The discrete gradients of \(PH_0\) and \(PH_N\) are identical translated absolutely summable sequences, so their \(\ell^1\)-difference converges to twice the one-sequence norm as \(N\to\infty\). Thus \(\operatorname{Var}(Pf_N)/\operatorname{Var}(f_N)\to s\). No finite-window extrapolation is used in this argument.

## Verification
The standalone `verify.py` symbolically verifies the inverse-Gram recurrence, the sign-resolved quadratic identities and the unique interior sign transition. It additionally assembles independent finite-interval mass matrices using exact rational arithmetic, solves for seven rational jump positions on three growing symmetric grids, and compares their variation to the infinite-grid formula. Exact moment equations are checked at seven rational phases across seventeen nodal indices. The program reports `ALL_CARDINAL_SPLINE_BV_CHECKS_PASS`. The all-input and all-knot statements follow from the proof, not these finite diagnostics.

## Relationship to prior work
Oswald (2006) studies \(L^\infty\) stability of linear-spline \(L^2\) projection, contrasting the one-dimensional uniform bound with higher-dimensional failure; an \(L^\infty\) bound does not control the variation of output slopes. Nochetto–Salgado (2012) construct a different, local averaging interpolant that decreases total variation; their interpolant is not the \(L^2\) orthoprojector and hence does not imply its sharp variation gain. Passenbrunner (2016) proves periodic spline \(L^\infty\) stability and a.e. convergence for arbitrary knots; neither gives a homogeneous \(BV\)-seminorm of the nonperiodic cardinal orthoprojector. Available published exact spline-projector calculations address \(L^\infty\) kernel norms and monotone-input endpoint overshoot, rather than the global total variation of projected one-jump data. The inverse-Gram geometric sequence is classical and is not claimed as new. The additional claim here is its exact sharp variation consequence and knot-versus-subcell extremizer profile.

## Limitations
The result concerns degree-one, equally spaced, real cardinal splines on the whole line. It does not determine sharp \(BV\) constants on finite intervals, unequal meshes, periodic domains, higher spline orders, or higher-dimensional grids. The homogeneous domain admits steps not in ordinary \(L^1\)-based \(BV(\mathbb R)\); the separate compact-support approximation shows that this choice does not change the sharp operator constant. Bibliographic originality remains subject to older unindexed spline-variation results and incomplete access to some historical texts. No independent validation or certification is asserted.

## References
1. P. Oswald, *A counterexample concerning the \(L^2\)-projector onto linear spline spaces*, arXiv:math/0611573v1, first posted 2006-11-19, https://arxiv.org/abs/math/0611573.
2. R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069v1, first posted 2012-11-05, https://arxiv.org/abs/1211.1069.
3. M. Passenbrunner, *Orthogonal projectors onto spaces of periodic splines*, arXiv:1608.06720v1, first posted 2016-08-24, https://arxiv.org/abs/1608.06720.
4. M. Beśka and K. Dziedziul, *Box-splines orthogonal projections*, 2004 (available displayed sections concern \(L^1\)-approximation-error asymptotics in \(BV\), not the present norm), https://www.researchgate.net/publication/268998362_Box-splines_orthogonal_projections.
