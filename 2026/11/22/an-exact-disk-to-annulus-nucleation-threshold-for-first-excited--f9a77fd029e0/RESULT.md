# An exact disk-to-annulus nucleation threshold for first-excited hyperbolic wavelet observation

## Finding

Fix \(\alpha>0\), and let \(\psi_1^\alpha\) denote the **unit-\(L^2\)-norm first excited Laguerre wavelet** on the positive-frequency Hardy space, in the normalization of Abreu--Speckbacher [1]. A measurable observation mask \(0\le q\le1\) on the upper half-plane has the hyperbolic budget \(\int q\,d\mu_h=H\), where \(d\mu_h=dx\,ds/s^2\). We maximize the fraction of the **fixed signal's** squared self-wavelet transform collected by the mask:
\[
\mathcal Q_\alpha(H)=\sup_{\substack{0\le q\le1\\\int q\,d\mu_h=H}}\frac{\int q(z)|W_{\psi_1^\alpha}\psi_1^\alpha(z)|^2\,d\mu_h(z)}{\int |W_{\psi_1^\alpha}\psi_1^\alpha(z)|^2\,d\mu_h(z)}.
\]
There is one finite critical area \(H_*(\alpha)>0\). For \(0<H\le H_*(\alpha)\), the unique optimal mask, up to null sets, is a pseudohyperbolic disk centered at \(i\). For \(H>H_*(\alpha)\), the unique optimum is that disk **together with a disjoint centered pseudohyperbolic annulus**. The new annulus nucleates continuously, but the disk boundary advances only quadratically in excess area. The exact optimal concentration curve and its one-sided curvatures are given below.

Put
\[
u(z)=\left|\frac{z-i}{z+i}\right|^2,\qquad b=\alpha+2,\qquad f_\alpha(u)=(1-u)^{\alpha+1}(1-bu)^2.
\]
Define the node and the outer local maximum by
\[
u_0=\frac1{\alpha+2},\qquad u_p=\frac{3\alpha+5}{(\alpha+2)(\alpha+3)},\qquad c_*=f_\alpha(u_p).
\]
There is exactly one \(u_*\in(0,u_0)\) satisfying \(f_\alpha(u_*)=c_*\). Set
\[
H_*(\alpha)=\frac{4\pi u_*}{1-u_*},\qquad
J_\alpha(u)=1-(1-u)^\alpha\bigl[1+\alpha(\alpha+2)u^2\bigr].
\]
For \(H\le H_*\), the optimal disk is \(0\le u(z)<H/(H+4\pi)\) and
\[
\boxed{\mathcal Q_\alpha(H)=J_\alpha\!\left(\frac{H}{H+4\pi}\right).}
\]
For \(H>H_*\), there is a unique \(c\in(0,c_*)\) and unique roots \(0<x<u_0<\ell<u_p<r<1\) of \(f_\alpha(x)=f_\alpha(\ell)=f_\alpha(r)=c\), satisfying
\[
\frac H{4\pi}=\frac{x}{1-x}+\frac{r}{1-r}-\frac{\ell}{1-\ell}.
\]
The unique optimal set is \(\{u<x\}\cup\{\ell<u<r\}\), and its exact captured fraction is
\[
\boxed{\mathcal Q_\alpha(H)=J_\alpha(x)+J_\alpha(r)-J_\alpha(\ell).}
\]
The function \(\mathcal Q_\alpha\) is continuously differentiable, strictly increasing and strictly concave, with
\[
\mathcal Q_\alpha'(H)=\frac{\alpha c(H)}{4\pi},
\]
where \(c(H)=f_\alpha(H/(H+4\pi))\) on the disk branch. Its one-sided **second derivatives at the transition are different**:
\[
\boxed{\mathcal Q_\alpha''(H_*-)=\frac{\alpha f_\alpha'(u_*)(1-u_*)^2}{16\pi^2}<0,\qquad \mathcal Q_\alpha''(H_*+)=0.}
\]
In particular \(\mathcal Q_\alpha\) is not twice differentiable at \(H_*\). Write \(\delta=H-H_*>0\), and \(k_\alpha=-f_\alpha''(u_p)=2(\alpha+1)(\alpha+2)(1-u_p)^\alpha\). Then the new annular width and the disk boundary obey the sharp laws
\[
\boxed{r-\ell=\frac{(1-u_p)^2}{4\pi}\,\delta+O_\alpha(\delta^2),\qquad
x-u_*=\frac{k_\alpha(1-u_p)^4}{128\pi^2|f_\alpha'(u_*)|}\,\delta^2+o_\alpha(\delta^2).}
\]
The critical hyperbolic area has the parameter limits
\[
\lim_{\alpha\downarrow0}H_*(\alpha)=2\pi,\qquad
\lim_{\alpha\to\infty}\alpha H_*(\alpha)=4\pi[1-2W(e^{-1})],
\]
where \(W\) denotes the principal real Lambert function. At \(\alpha=1\), exactly,
\[
\boxed{u_*=(2-\sqrt2)/3,\quad H_*=4\pi(3\sqrt2-4),\quad \mathcal Q_1(H_*)=(8-5\sqrt2)/9.}
\]

## Assumptions and scope

The wavelet convention is \(W_\psi f(x+is)=\langle f,T_xD_s\psi\rangle\), with \(D_s\psi(t)=s^{-1/2}\psi(t/s)\). The wavelet \(\psi_1^\alpha\) is the normalized first Laguerre member of [1], not the analytic \(n=0\) Cauchy wavelet. The fixed input is exactly \(f=\psi_1^\alpha\). All \(H\) are finite and positive. Masks are measurable and may be fractional; ``unique'' means equal almost everywhere for the hyperbolic measure. The result optimizes the mask for this fixed input, **not** the operator norm over arbitrary input signals and observation sets; no higher-Landau-level Faber--Krahn inequality is asserted. Angular orientation is immaterial because the optimal masks are radial in the pseudohyperbolic coordinate about \(i\).

## Proof

**1. The normalized radial wavelet response.** The explicit reproducing-kernel formula for the first excited wavelet in [1, Proposition 1, equation (20)] gives, using \(P_1^{(0,\alpha)}(1-2u)=1-(\alpha+2)u\),
\[
|W_{\psi_1^\alpha}\psi_1^\alpha(z)|^2=f_\alpha(u(z)).
\]
At \(z=i\), both sides are one because \(\|\psi_1^\alpha\|_2=1\). Under \(w=(z-i)/(z+i)\), polar area transformation gives \(d\mu_h=2\,du\,d\theta/(1-u)^2\). Thus each full radial interval \([a,b]\subset[0,1)\) has area \(4\pi[b/(1-b)-a/(1-a)]\), and its **normalized** captured energy is \(J_\alpha(b)-J_\alpha(a)\). Indeed,
\[
\frac{\alpha}{4\pi}\int_{\{u\in[a,b]\}}f_\alpha(u)\,d\mu_h
=\alpha\int_a^b(1-u)^{\alpha-1}(1-(\alpha+2)u)^2\,du
=J_\alpha(b)-J_\alpha(a).
\]
Direct differentiation verifies \(J_\alpha'(u)=\alpha(1-u)^{\alpha-1}(1-(\alpha+2)u)^2\); also \(J_\alpha(0)=0\) and \(J_\alpha(1)=1\). The total wavelet energy is consequently \(4\pi/\alpha\), agreeing with the admissibility constant in [1].

**2. Exactly two radial lobes.** Differentiate the density:
\[
 f_\alpha'(u)=(\alpha+2)(\alpha+3)(1-u)^\alpha [1-(\alpha+2)u](u-u_p).
\]
Therefore \(f_\alpha\) decreases from \(1\) to zero on \([0,u_0]\), increases from zero to \(c_*\) on \([u_0,u_p]\), then decreases to zero on \([u_p,1]\). We have \(0<u_0<u_p<1\). To see that \(c_*<1\), let \(b=\alpha+1>1\). On the outer lobe \(0\le(b+1)u-1\le bu\); therefore its height is at most
\[
\max_{0\le u\le1}b^2u^2(1-u)^b
=\frac{4b^2}{(b+2)^2}\left(\frac b{b+2}\right)^b
\le 4t^2e^{-2t}\le4e^{-2}<1,\quad t=\frac b{b+2}.
\]
The strictly decreasing inner lobe therefore meets \(c_*\) at a unique \(u_*\). The strict lobe monotonicities imply the asserted unique three-root description of every superlevel \(\{f_\alpha>c\}\) with \(0<c<c_*\), and its single-disk description when \(c_*\le c<1\).

**3. Uniqueness and the full optimum.** Hyperbolic superlevel area is a continuous strictly decreasing function of \(c\in(0,1)\): it tends to zero as \(c\uparrow1\), and diverges as \(c\downarrow0\). At \(c=c_*\) the outer peak contributes a single null circle, so its area is exactly \(H_*\). Thus every finite positive budget determines precisely one threshold \(c(H)\). Let \(q_*\) be the indicator of its strict superlevel. For any admissible \(q\),
\[
 \int (q_*-q)f_\alpha\,d\mu_h
 =\int(q_*-q)(f_\alpha-c(H))\,d\mu_h\ge0,
\]
because \(q_*\) is one wherever \(f_\alpha>c\) and zero wherever \(f_\alpha<c\), while the two masks have the same area. Equality forces \(q=q_*\) almost everywhere: all level circles have zero hyperbolic area. This proves the global optimum over **all**, including nonradial and fractional, masks. The radial integral in Step 1 gives the stated exact concentration formulas.

**4. Regularity and nucleation.** The threshold variation identity (or differentiation of the radial formula) gives \(\mathcal Q_\alpha'(H)=\alpha c(H)/(4\pi)\). Strict decrease of \(c(H)\) proves strict concavity. On the disk branch \(x=H/(H+4\pi)\), so the left second derivative at \(H_*\) is the stated negative constant. On the two-component branch, put \(c=c_*-\eta\). Taylor expansion at the nondegenerate outer maximum, whose negative curvature is \(k_\alpha\), yields
\[
 \ell=u_p-\sqrt{2\eta/k_\alpha}+O_\alpha(\eta),\quad
 r=u_p+\sqrt{2\eta/k_\alpha}+O_\alpha(\eta).
\]
The inner root satisfies \(x=u_*+\eta/|f_\alpha'(u_*)|+O_\alpha(\eta^2)\). Therefore
\[
 H-H_*=\frac{8\pi}{(1-u_p)^2}\sqrt{2\eta/k_\alpha}+O_\alpha(\eta).
\]
Inverting this positive expansion shows
\[
 \eta=\frac{k_\alpha(1-u_p)^4}{128\pi^2}(H-H_*)^2+O_\alpha((H-H_*)^3).
\]
Substitution proves both boundary laws. Since \(c(H)=c_*-O_\alpha((H-H_*)^2)\) on the right, the right second derivative of the value is zero. The one-sided curvatures differ, as claimed.

**5. Weight limits.** As \(\alpha\downarrow0\), the density and its outer maximum converge to \((1-u)(1-2u)^2\) and \(2/27\); the inner-level equation has the unique root \(u_*=1/3\), giving \(H_*\to2\pi\). For \(\alpha\to\infty\), \(\alpha u_p\to3\) and \(c_*\to4e^{-3}\). Uniformly for bounded \(v\in[0,1]\), \(f_\alpha(v/\alpha)\to e^{-v}(1-v)^2\), strictly decreasing there. The rescaled inner root therefore converges to the unique \(v_0\in(0,1)\) satisfying \(e^{-v_0}(1-v_0)^2=4e^{-3}\), equivalently \(v_0=1-2W(e^{-1})\). The area formula yields the asserted limit. For \(\alpha=1\), the threshold equation reduces to \((1-u)(1-3u)=1/3\), proving the stated radicals and energy value.

## Verification

The self-contained `check.py` evaluates exact mass-normalization identities and mask endpoints, compares closed-form captured energies to independent numerical quadrature for four positive wavelet parameters and six area regimes each, verifies the two near-transition asymptotics using high precision, and verifies the radical weight-one constants. It passed 104 finite assertions. These tests **do not** establish the infinite-dimensional wavelet identity, global mask optimality, or limiting parameter statements: those are proved analytically above from [1] and the stated scalar calculations.

Reproduce with `python check.py` in an environment containing Python 3, SciPy and mpmath.

## Relationship to prior work

Abreu--Speckbacher [1] establishes the general Laguerre/Jacobi wavelet kernels and local reproducing identities; its explicit kernel is a necessary and credited ingredient here, **not claimed as new**. Ramos--Tilli [2] proves a Faber--Krahn result for analytic Cauchy-wavelet windows and joint optimization over signals and sets. The present fixed-input first-excited-level result neither implies nor extends that unrestricted operator-norm theorem. Abreu--Speckbacher [3] studies invariant higher-level wavelet spaces and density/frame obstructions, not hyperbolic-area masks for one self-ambiguity profile. The elementary measure-theoretic superlevel (bathtub) comparison is standard; the asserted contribution is the complete quantitative two-lobe topology transition for this concrete natural response, including exact area, a non-\(C^2\) optimal energy curve, precise birth coefficients, and the weight limits. Adjacent Gaussian time-frequency localization results concern a different (Euclidean) phase space and do not supply these Jacobi/hyperbolic constants.

## Limitations

The results apply to a single fixed normalized first excited wavelet as both input and window. They do not claim a sharp concentration inequality for all input functions, all higher Laguerre levels, or non-hyperbolic resource budgets. Parameter-dependent constants in remainder terms are not uniform in \(\alpha\). Novelty is assessed relative to the cited inspected literature and accessible mathematical comparisons; historical priority cannot be certified by a finite search.

## References

1. L. D. Abreu and M. Speckbacher, *Donoho--Logan large sieve principles for the wavelet transform*, first publicly available 24 October 2022, arXiv:2210.13056, https://arxiv.org/abs/2210.13056 . Proposition 1, equation (20), and Section 3 provide the normalization and Jacobi kernel.
2. J. P. G. Ramos and P. Tilli, *A Faber--Krahn inequality for wavelet transforms*, arXiv:2205.07998 (16 May 2022), https://arxiv.org/abs/2205.07998 ; Bull. Lond. Math. Soc. 55 (2023), https://doi.org/10.1112/blms.12833 .
3. L. D. Abreu and M. Speckbacher, *Affine density, von Neumann dimension and a problem of Perelomov*, arXiv:2012.11314 (21 December 2020), https://arxiv.org/abs/2012.11314 ; Adv. Math. 407 (2022), Article 108564.
4. L. D. Abreu and M. Dörfler, *An inverse problem for localization operators*, arXiv:1202.5841 (27 February 2012), https://arxiv.org/abs/1202.5841 .
