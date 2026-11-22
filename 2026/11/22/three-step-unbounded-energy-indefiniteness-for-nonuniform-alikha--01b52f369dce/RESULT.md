# Three-step unbounded energy indefiniteness for nonuniform Alikhanov fractional differentiation

## Finding

For every fractional order \(0<\alpha<1\), the standard nonuniform \(L2\!-\!1_{\sigma}\) Alikhanov Caputo difference operator has a **negative three-step increment-energy form** on meshes with successive lengths \((1,\varepsilon,1)\) for every sufficiently small \(\varepsilon>0\), where \(\sigma=1-\alpha/2\). More precisely, define

\[
A_{\alpha}=\frac{\alpha}{(1-\alpha)(2-\alpha)},\qquad
B_{\alpha}=\int_0^1\frac{2t-1}{(2-\alpha/2-t)^\alpha}\,dt>0.
\]

The fixed (for each \(\alpha\)) increments \((\delta_1u,\delta_2u,\delta_3u)=(0,-B_{\alpha}/(2A_{\alpha}),1)\) satisfy the **exact asymptotic energy law**

\[
\boxed{\lim_{\varepsilon\downarrow0}\varepsilon\Gamma(1-\alpha)\mathcal B_3(u,u)
=-\frac{B_{\alpha}^{2}}{4A_{\alpha}}<0.}
\]

Consequently the unrestricted-mesh bilinear form is not positive semidefinite, and its negative energy diverges at rate \(\varepsilon^{-1}\) for this explicit fixed-increment witness. The result concerns the fractional-difference energy form, not a claim that every associated numerical solution is unstable.

## Assumptions and scope

Let \(t_0=0\), \(t_1=1\), \(t_2=1+\varepsilon\), \(t_3=2+\varepsilon\), with \(\varepsilon>0\). Write \(\tau_j=t_j-t_{j-1}\), \(\delta_ju=u^j-u^{j-1}\), and \(s_k=t_{k-1}+\sigma\tau_k\). For the standard nonuniform Alikhanov definition, \(H_2^j\) is the quadratic interpolant through \((t_{j-1},u^{j-1})\), \((t_j,u^j)\), \((t_{j+1},u^{j+1})\), and \(H_1^k\) is the line through the final pair. Set

\[
L_k^{\alpha,*}u=\frac1{\Gamma(1-\alpha)}\left[
\sum_{j=1}^{k-1}\int_{t_{j-1}}^{t_j}
\frac{(H_2^j)'(t)}{(s_k-t)^\alpha}\,dt+
\int_{t_{k-1}}^{s_k}\frac{(H_1^k)'(t)}{(s_k-t)^\alpha}\,dt
\right],\quad 1\le k\le3.
\]

The scalar quadratic form under study is \(\mathcal B_3(u,u)=\sum_{k=1}^3 \delta_ku\,L_k^{\alpha,*}u\). Values \(u^0\) and \(u^1\) may both be zero; the remaining values are then determined by the stated increments. There is no additional spatial problem, forcing, or timestep restriction.

## Proof

For a quadratic interpolation panel with adjacent lengths \(a=\tau_j\), \(b=\tau_{j+1}\) and \(y=t-t_{j-1}\), direct differentiation gives

\[
(H_2^j)'(t)=\frac{\delta_ju}{a}+
\frac{2y-a}{a+b}\left(\frac{\delta_{j+1}u}{b}-\frac{\delta_ju}{a}\right).
\]

Let \(W_{kj}\) be the coefficient of \(\delta_ju\) in \(\Gamma(1-\alpha)L_k^{\alpha,*}u\). Only \(W_{22},W_{32},W_{33}\) enter the form when \(\delta_1u=0\). Define \(J_{\alpha}(s)=\int_0^1(2t-1)(s-t)^{-\alpha}\,dt\). Since \(s_2=1+\sigma\varepsilon\), the second panel's final linear segment and the first panel's quadratic segment give exactly

\[
W_{22}=\frac{\sigma^{1-\alpha}}{(1-\alpha)\varepsilon^{\alpha}}
+\frac{J_{\alpha}(1+\sigma\varepsilon)}{\varepsilon(1+\varepsilon)}.
\]

The integral is continuous as its argument decreases to \(1\), because \(\alpha<1\), and substitution \(v=1-t\) gives

\[
J_{\alpha}(1)=\frac1{1-\alpha}-\frac2{2-\alpha}=A_{\alpha}>0.
\]

At the third evaluation point \(s_3=1+\varepsilon+\sigma\), the first quadratic panel contributes \(J_{\alpha}(s_3)/[\varepsilon(1+\varepsilon)]\) to \(W_{32}\). The second quadratic panel contributes a bounded term: its \(\delta_2u\) derivative coefficient is \(O(\varepsilon^{-1})\) and is integrated over a panel of length \(\varepsilon\) against a uniformly bounded kernel. Thus

\[
W_{32}=\frac{J_{\alpha}(1+\varepsilon+\sigma)}{\varepsilon(1+\varepsilon)}+O(1)
=\frac{B_{\alpha}}{\varepsilon}+o(\varepsilon^{-1}).
\]

The current linear panel of length \(1\) contributes \(\sigma^{1-\alpha}/(1-\alpha)\) to \(W_{33}\). Its other contribution, from the preceding quadratic panel, is bounded (indeed, tends to zero). Therefore

\[
W_{22}=A_{\alpha}\varepsilon^{-1}+o(\varepsilon^{-1}),\quad
W_{32}=B_{\alpha}\varepsilon^{-1}+o(\varepsilon^{-1}),\quad
W_{33}=O(1).
\]

For \(s>1\), strict positivity of \(J_{\alpha}(s)\) follows by pairing \(t\) with \(1-t\):

\[
J_{\alpha}(s)=\int_0^{1/2}(1-2t)
\left[(s-1+t)^{-\alpha}-(s-t)^{-\alpha}\right]dt>0.
\]

Thus \(B_{\alpha}=J_{\alpha}(1+\sigma)>0\). With \(q=-B_{\alpha}/(2A_{\alpha})\), the energy is

\[
\Gamma(1-\alpha)\mathcal B_3(u,u)=q^2W_{22}+qW_{32}+W_{33}.
\]

Multiplying by \(\varepsilon\) and taking the limit gives \(A_{\alpha}q^2+B_{\alpha}q=-B_{\alpha}^2/(4A_{\alpha})\), which is strictly negative. This proves both eventual indefiniteness and the stated divergence coefficient. No finite mesh enumeration is used to infer the asymptotic assertion.

## Verification

The standalone standard-library program `checker.py` integrates all polynomial panels exactly at \(\alpha=1/2\), using high-precision decimal square roots. For this order, \(A_{1/2}=2/3\) and \(B_{1/2}=4\sqrt7/3-2\sqrt3\). On the exact mesh \((1,1/10000,1)\), the **integer** increments \((0,-1,16)\) give

\[
\Gamma(1/2)\mathcal B_3(u,u)=-3075.1592734497714868\ldots<0.
\]

The program also compares successively smaller mesh values with the analytic coefficient \(-B_{1/2}^2/(4A_{1/2})=-0.00151527675498665349\ldots\). These calculations check the algebra at a particular order but are not the proof for all orders. Run `python3 checker.py`; see `checker-output.txt` for the captured output.

## Relationship to prior work

Liao, Tang, and Zhou introduced and studied a nonuniform second-order Alikhanov scheme for fractional Allen–Cahn equations, with step-ratio restrictions and maximum-principle results [1]. Quan and Wu proved positivity of precisely this increment-energy form under explicit sufficient mesh-ratio constraints, including a uniform sufficient lower bound near \(0.475329\) [2, Sections 2–3]. Liao, Zhu, and Sun established a related discrete-gradient energy structure under weaker but still positive ratio bounds [3, Sections 2–4]. The present conclusion is logically different from those sufficient results: it gives a constructive, all-fractional-order negative counterexample and a sharp \(\varepsilon^{-1}\) blow-up law when a middle cell collapses. The cited positivity theorems do not apply to this mesh because its second-to-first step ratio tends to zero. No claim is made about the optimal universal positive ratio threshold.

## Limitations

The result concerns the **unmodified** Alikhanov increment-energy form on arbitrary scalar grid data, rather than the actual trajectory of a subdiffusion PDE, a modified discrete energy, or a variable-order derivative. It does not show divergence of the numerical solution, failure of a maximum principle, or necessity of the specific published sufficient ratio constants. A priority search may miss older counterexamples in less easily accessible numerical-analysis literature. The asymptotic is for a fixed fractional order \(0<\alpha<1\); it is not uniform as \(\alpha\) approaches either endpoint.

## References

[1] H.-L. Liao, T. Tang, and T. Zhou, *A second-order and nonuniform time-stepping maximum-principle preserving scheme for time-fractional Allen–Cahn equations*, arXiv:1909.10216, first submitted 2019-09-23. https://arxiv.org/abs/1909.10216

[2] C. Quan and X. Wu, *Global-in-time H1-stability of L2-1sigma method on general nonuniform meshes for subdiffusion equation*, arXiv:2208.01384, first submitted 2022-08-02, specifically formulae (1)–(4), (9) and Theorem 3.1. https://arxiv.org/abs/2208.01384

[3] H.-L. Liao, X. Zhu, and H. Sun, *Asymptotically compatible energy and dissipation law of the nonuniform L2-1sigma scheme for time fractional Allen-Cahn model*, arXiv:2311.13216, first submitted 2023-11-22. https://arxiv.org/abs/2311.13216
