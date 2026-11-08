# Truncated-Pareto position scores and a singular location-information transition at a resetting-gas spinodal

## Finding

The spatial location score of the pure-gas stationary branch in the one-dimensional motility-induced phase-separation model with local resetting has an exact truncated-Pareto law of exponent \(3\). As the upper edge of the gas branch is reached, the truncation disappears, its Fisher information diverges logarithmically, and the translated stationary laws acquire an \(h^2\log(1/|h|)\) squared-Hellinger modulus instead of the ordinary quadratic law. The same spatial result holds for finite-speed particle returns when the total (moving plus returning) density is used.

Let \(m=\rho_m>4\), \(M,v_0,\alpha,r>0\), \(\chi=\sqrt{r(r+\alpha)}/v_0\), \(\chi_c=m/(2M)\), and \(\delta=1-\chi/\chi_c\in[0,1)\). With \(p_\delta\) the normalized gas position density, define the absolute spatial score \(W=|\partial_x\log p_\delta(X)|\) for \(X\sim p_\delta\). For \(0<\delta<1\), its density is

\[
 f_\delta(w)=\frac{m\chi}{M}\,w^{-3}\,\mathbf1_{(\chi,\chi/\sqrt\delta)}(w).
\]

At \(\delta=0\), the law is the untruncated Pareto density \(2\chi_c^2w^{-3}\mathbf1_{(\chi_c,\infty)}(w)\). Consequently the positional translation Fisher information is exactly

\[
 I_\delta=\frac{m\chi}{2M}\log\frac1\delta,\qquad 0<\delta<1,
\]

and diverges at the spinodal. With the convention

\[
 H_\delta^2(h)=\frac12\int_{\mathbb R}\bigl(\sqrt{p_\delta(x-h)}-\sqrt{p_\delta(x)}\bigr)^2\,dx,
\]

its local modulus is

\[
 H_\delta^2(h)=\frac{I_\delta}{8}h^2+o(h^2)\quad(\delta>0\ \text{fixed}),\qquad
 H_0^2(h)\sim\frac{\chi_c^2}{8}h^2\log\frac{1}{\chi_c|h|}\quad(h\to0).
\]

This is a pointwise-in-parameter assertion, not a uniform double-scaling claim.

## Assumptions and scope

This is the *continuum stationary mean-field model* with symmetric local Poisson resetting, tumble rate \(\alpha\), free speed \(v_0\), mass \(M\), and the published piecewise density slowdown with \(m>4\). The gas branch exists when \(M\chi\le m/2\). The additional coexistence regime \(M\chi>2\) contains both the dense-droplet stationary profile and the metastable pure-gas profile; this theorem concerns only the latter. At equality \(M\chi=m/2\), the gas solution is taken in the continuous, mass-normalized weak profile sense, despite its non-Lipschitz spatial derivative at the reset origin.

The score is the derivative of the log position density, defined almost everywhere; no derivative value is needed at the single spatial point \(x=0\). The same magnitude is the score for the translated location family \(p_\delta(x-\theta)\) at \(\theta=0\). We consider positive score moments \(q>0\).

## Proof

**1. Flux equation and normalization.**  Write \(u(x)=2\rho(x)/m\) on \(x>0\), where \(\rho\) is the *total* stationary gas density. The published stationary gas flux equation is equivalent to

\[
 (1-u)u'(x)=-\chi u(x),\qquad
 u(x)e^{-u(x)}=u_0e^{-u_0-\chi x}.
\]

Here \(0<u_0\le1\). This also follows directly by substituting the published Lambert-profile formula. Changing variables \(x\mapsto u\) in the two-sided mass gives

\[
 M=m\int_0^\infty u(x)\,dx
 =\frac m\chi\int_0^{u_0}(1-u)\,du
 =\frac m\chi\left(u_0-\frac{u_0^2}{2}\right).
\]

Thus \(u_0=1-\sqrt{\delta}\), where \(\delta=1-2M\chi/m\). The probability density is \(p_\delta(x)=m u(|x|)/(2M)\). At \(\delta=0\), the formula gives the unique monotone continuous weak gas profile with \(u_0=1\) and finite total mass.

**2. Exact score pushforward.**  Differentiating the flux equation away from \(0\),

\[
 \left|\partial_x\log p_\delta(x)\right|=\frac\chi{1-u(|x|)}.
\]

For \(X\sim p_\delta\), the variable \(U=u(|X|)\) has exact density

\[
 f_U(u)=\frac{m}{M\chi}(1-u)\,\mathbf1_{(0,u_0)}(u).
\]

The monotone change of variables \(w=\chi/(1-u)\) has \(du/dw=\chi/w^2\), hence

\[
 f_W(w)=\frac{m\chi}{M}w^{-3}\,\mathbf1_{(\chi,\chi/\sqrt\delta)}(w)
\]

for \(\delta>0\). At \(\delta=0\), \(\chi=\chi_c=m/(2M)\) and the upper endpoint tends to infinity, giving the claimed Pareto limit. The densities integrate to one by the displayed mass identity.

For \(q>0\), \(q\ne2\), exact integration yields

\[
 \mathbb E W^q=\frac{m\chi^{q-1}}{M}\,\frac{1-\delta^{(2-q)/2}}{2-q},\qquad 0<\delta<1,
\]

and for \(q=2\) it yields \(I_\delta=(m\chi/(2M))\log(1/\delta)\). At the spinodal, the critical Pareto law has finite moments exactly for \(0<q<2\). As \(\delta\downarrow0\), the lower moments tend to \(2\chi_c^q/(2-q)\); the second moment is asymptotic to \(\chi_c^2\log(1/\delta)\); for \(q>2\), the moment is asymptotic to \(2\chi_c^q\delta^{-(q-2)/2}/(q-2)\).

**3. Regular translation geometry before the spinodal.**  For fixed \(0<\delta<1\), \(p_\delta\) is strictly positive, continuous, smooth away from the origin, and \(\sqrt{p_\delta}\) is in \(H^1(\mathbb R)\). The ordinary translation differentiability of \(H^1\) functions gives

\[
 H_\delta^2(h)=\frac{h^2}{2}\int_{\mathbb R}|(\sqrt{p_\delta})'|^2\,dx+o(h^2)=\frac{I_\delta h^2}{8}+o(h^2).
\]

The identity \(I_\delta=4\int|\partial_x\sqrt{p_\delta}|^2\) holds almost everywhere.

**4. Sharp nonregular translation geometry at the spinodal.**  For \(\delta=0\), the implicit relation reduces to \(u e^{-u}=e^{-1-\chi_c|x|}\). Expansion at the maximum of \(u e^{-u}\) gives

\[
 u(|x|)=1-\sqrt{2\chi_c|x|}+O(|x|),\qquad
 \sqrt{p_0(x)}=\sqrt{\chi_c}-\frac{\chi_c}{\sqrt2}\sqrt{|x|}+O(|x|).
\]

The remainder after removing the square-root cusp is locally Lipschitz, and outside a small neighborhood the square-root density has an integrable squared derivative. For any function with a single local singularity \(f(x)=a+b\sqrt{|x|}+g(x)\), with this same remainder regularity, direct split of the translation integral into \(|x|\le2|h|\), \(2|h|<|x|<\varepsilon\), and the outside gives

\[
 \int_{\mathbb R}(f(x-h)-f(x))^2dx
 =\frac{b^2}{2}h^2\log\frac1{|h|}+o(h^2\log(1/|h|)).
\]

Indeed, the central interval is \(O(h^2)\); on the intermediate interval \(f'(x)\sim b\operatorname{sgn}(x)/(2\sqrt{|x|})\) and both sides contribute a total \(b^2h^2\log(1/|h|)/2\); the Lipschitz and remote contributions are lower order by Cauchy–Schwarz. Here \(b=-\chi_c/\sqrt2\), and the convention defining \(H^2\) introduces an additional factor \(1/2\). Changing the arbitrary reference length in the logarithm affects only a lower-order \(O(h^2)\) term, giving \(H_0^2(h)\sim\chi_c^2h^2\log(1/(\chi_c|h|))/8\).

**5. Finite-speed return invariance.**  In the source's finite-return-speed extension, with \(\xi=1+\gamma^{-1}\sqrt{r/(r+\alpha)}\), the moving density equals \(\rho_{\mathrm{move}}(x)=-mW_0(-C_0e^{-C_0-\chi|x|})/(2\xi)\), while the returning density equals \((\xi-1)\rho_{\mathrm{move}}\). Therefore the total density \(\rho_{\mathrm{tot}}=\xi\rho_{\mathrm{move}}\) is exactly the same as in instantaneous resetting, at identical \(m,M,\chi\). All position-score, Fisher, and Hellinger assertions apply unchanged to the normalized total density, without asserting they apply to moving particles alone.

## Verification

The accompanying `verify_score.py` uses the independently coded Lambert-profile evaluation and checks numerical normalization, the stationary flux differential equation, all displayed score-moment formulas at multiple parameter values, and direct quadrature of the critical Hellinger modulus. It passed \(47\) deterministic tests. For dimensionless \(m=M=6\), \(\chi_c=1/2\), the Hellinger-leading-term ratios at shifts \(0.025,0.008,0.0025,0.0008\) were approximately \(1.1549,1.1185,1.0958,1.0808\); convergence is logarithmically slow, as expected. The checker is a finite consistency test; the exact claims follow from the above proof.

## Relationship to prior work

Grange's 19 October 2026 preprint, arXiv:2610.26149v1, derives the exact gas profile, its gas-to-droplet coexistence conditions, and finite-return-speed stationary density formulas. These are the premises and are **not** newly derived results. The contribution here is the full score pushforward, sharp score-moment threshold, and exact nonregular Hellinger coefficient at the metastable gas spinodal. A prior exact transport comparison for these two stationary branches concerns radial stochastic order and Wasserstein distances, not the score or translated location-family geometry. General cusp-location asymptotics may explain the logarithmic universality, but do not supply this model's exact score law or coefficient without the specific source-profile analysis. Noninstantaneous-return invariance is already present at the density level in the source; its use for the score law is a consequence, not a newly asserted physical invariance principle.

## Limitations

The gas near the spinodal is metastable within the two-phase coexistence region. The analysis is for a continuum stationary mean-field profile, not a proof of a corresponding many-particle finite-size critical statistic. The endpoint derivative singularity is an admissible weak stationary-profile feature, not a pointwise classical derivative at the origin. The Hellinger asymptotics hold with fixed precritical parameters or exactly at the spinodal; no uniform crossover or local-asymptotic-normality claim is made. The Fisher information concerns hypothetical spatial translation, not a thermodynamic entropy-production rate. The work follows by nontrivial functionals of an already-published exact density; publication-priority and significance require independent assessment.

## References

1. Pascal Grange, *Motility-Induced Phase Separation of Run-and-Tumble Particles under Local Stochastic Resetting*, first public version 19 October 2026, arXiv:2610.26149v1; source equations (39)–(45) and Table 1, https://arxiv.org/abs/2610.26149 and https://arxiv.org/html/2610.26149v2.
2. A. S. Bodrova, A. V. Chechkin and I. M. Sokolov, *Resetting processes with noninstantaneous return*, Physical Review E 101, 052130 (2020), https://doi.org/10.1103/PhysRevE.101.052130. This supplies background on density invariance under finite return speed in other resetting models, not this mean-field score law.
