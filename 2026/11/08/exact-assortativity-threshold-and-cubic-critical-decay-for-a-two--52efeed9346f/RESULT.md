# Exact assortativity threshold and cubic critical decay for a two-degree synergistic SIS system

## Finding

For the correlated two-degree synergistic susceptible–infected–susceptible (SIS) mean-field model with degrees \(20,5\), frequencies \(1/5,4/5\), unit recovery, and assortativity \(-1\le r<1\), there is a **unique exact synergy threshold** \(\alpha_*(r)\) at which the local disease-free onset changes from forward to backward. It is strictly decreasing in assortativity, with endpoint values \(\alpha_*(-1)=1/9\) and \(\lim_{r\uparrow1}\alpha_*(r)=1/19\). At zero assortativity it equals \(17/200\), resolving the numerical transition near \(0.086\) for these network parameters.

Precisely, let \(z\in(0,1/2]\) be the unique solution of
\[
\frac{1+r}{2}=\frac{1-4z^2}{(1-z)(1+4z)}.
\]
The disease-free invasion threshold and the synergy threshold are
\[
\lambda_c(r)=\frac{1+4z}{20(1+z)},\qquad
\alpha_*(r)=\frac{(1+4z)(1+4z^3)}{(1+z)(19+64z^3)}.
\]
For fixed \(r<1\) and \(\alpha\ne\alpha_*(r)\), a branch of small strictly positive equilibria leaves the origin as \(\lambda\) crosses \(\lambda_c\), existing on the \(\lambda>\lambda_c\) side if \(\alpha<\alpha_*\), and on the \(\lambda<\lambda_c\) side if \(\alpha>\alpha_*\). The former equilibria are locally asymptotically stable; the latter are saddles. These assertions are local: a backward branch does not, by itself, prove a distant stable endemic branch or global hysteresis.

At the exact double-critical point \((\lambda,\alpha)=(\lambda_c,\alpha_*)\), the cubic center-manifold coefficient is strictly negative at **every** allowed assortativity. Small strictly positive trajectories satisfy
\[
\lim_{t\to\infty}\sqrt t\,(i_1(t),i_2(t))
=\frac{(1,z)}{\sqrt{-2C(z)}},
\]
with \(C(z)<0\) defined explicitly below. For \(r=0\), the limiting vector is \((20,5)/\sqrt{659}\). This law concerns the deterministic two-class mean-field ODE and not stochastic extinction on a finite network.

## Assumptions and scope

Let \(i_1,i_2\in[0,1]\) be the infected fractions among degree-\(20\) and degree-\(5\) nodes. The degree-weighted stub totals are equal because \((1/5)20=(4/5)5=4\). Thus a feasible reversible mixing matrix with assortativity \(r\in[-1,1]\) is
\[
P=\begin{pmatrix}a&b\\b&a\end{pmatrix},\qquad a=\frac{1+r}{2},\quad b=\frac{1-r}{2}.
\]
For \(r<1\), the mixing matrix is irreducible. We analyze exactly the mean-field equations of the cited model (its mean-field equations (10)–(11)) with recovery scaled to one:
\[
\dot i_j=-i_j+(1-i_j)\lambda k_j m_j\bigl(1+\alpha(k_j-1)m_j\bigr),
\qquad m_j=\sum_{\ell=1}^2P_{j\ell}i_\ell,
\]
where \((k_1,k_2)=(20,5)\), \(\lambda>0\), \(\alpha\ge0\). The biological square is forward-invariant. All equilibria and trajectories asserted near zero are in an unspecified but sufficiently small neighborhood (depending on fixed \(r\) and parameter choices). There is no statement of global convergence or uniqueness of all endemic equilibria.

## Proof

**1. Perron mode and its parametrization.** Write \(K=\operatorname{diag}(20,5)P\). Its Perron eigenvalue \(p\) defines \(\lambda_c=1/p\). Choose right and left Perron vectors \(v=(1,z)^\mathsf T\) and \(u=(1,4z)^\mathsf T\). The two eigenvector equations imply
\[
a=\frac{1-4z^2}{(1-z)(1+4z)},\qquad p=\frac{20(1+z)}{1+4z}.
\]
Here \(0<z\le1/2\), with \(z=1/2\) at \(r=-1\), and \(z\downarrow0\) as \(r\uparrow1\). Differentiation gives
\[
\frac{da}{dz}=-\frac{3(1+4z^2)}{(1-z)^2(1+4z)^2}<0.
\]
Consequently \(z\mapsto r\) is strictly decreasing and its range is \([-1,1)\). At \(\lambda_c\), the Jacobian \(L=-I+\lambda_cK\) has one zero eigenvalue and one strictly negative eigenvalue \(-\kappa\), where
\[
\kappa=\frac{3(1+4z^2)}{4(1-z^2)}>0.
\]
The Perron coordinate is \(s=(u^\mathsf T i)/(u^\mathsf T v)=(i_1+4zi_2)/(1+4z^2)\).

**2. The exact quadratic transition.** At \(\lambda=\lambda_c\), expand the vector field as \(Li+Q(i)+R(i)\), with homogeneous quadratic and cubic terms
\[
Q_j(i)=\lambda_c k_j\bigl[\alpha(k_j-1)m_j^2-i_jm_j\bigr],\qquad
R_j(i)=-\lambda_c k_j\alpha(k_j-1)i_jm_j^2.
\]
The reduced quadratic center coefficient is \(u^\mathsf TQ(v)/(u^\mathsf T v)\). Since \(m_j(v)=v_j/(\lambda_ck_j)\), direct substitution yields
\[
\frac{u^\mathsf TQ(v)}{u^\mathsf T v}=B(z)[\alpha-\alpha_*(z)],\qquad
B(z)=\frac{(1+z)(19+64z^3)}{(1+4z)(1+4z^2)}>0.
\]
Thus the direction of the local transcritical equilibrium branch switches at exactly the displayed \(\alpha_*(z)\). Its dependence on assortativity is strict because
\[
\frac{d\alpha_*}{dz}=\frac{3(256z^6+48z^4+200z^3+12z^2+19)}{(1+z)^2(19+64z^3)^2}>0,
\]
while \(dr/dz<0\). Substitution at \(z=1/2,1/4,0\) gives \(1/9,17/200,1/19\), respectively. The last is an endpoint limit, not a claim of irreducibility at \(r=1\).

**3. The cubic coefficient does not vanish.** Set \(\alpha=\alpha_*\). The quadratic vector satisfies \(u^\mathsf TQ(v)=0\). The center-manifold graph can be written \(i=sv+s^2w+O(s^3)\), with \(u^\mathsf Tw=0\) and \(Lw+Q(v)=0\). Therefore \(w=Q(v)/\kappa\), which simplifies to
\[
w=\frac{(1-z^2)(16z^3,-4z^2)^\mathsf T}{(1+4z^2)(19+64z^3)}.
\]
Writing \(m_j(v)= (Pv)_j\), \(m_j(w)=(Pw)_j\), the reduced cubic coefficient is
\[
C(z)=\frac{u^\mathsf T}{u^\mathsf Tv}
\left(\left[\lambda_ck_j\{2\alpha_*(k_j-1)m_j(v)m_j(w)-v_jm_j(w)-w_jm_j(v)\}\right]_{j=1}^2+R(v)\right).
\]
Exact reduction gives
\[
C(z)=-\frac{16384z^{10}+8192z^7+6016z^6+964z^4+2888z^3+361}{(1+4z^2)(19+64z^3)^2}<0.
\]
Every coefficient in the numerator is nonnegative and the constant term is positive, proving strict negativity for the full interval. In particular, at \(z=1/4\), \(C=-659/800\).

**4. Equilibrium branches and critical dynamics.** The simple zero eigenvalue and smooth center reduction give, for \(\delta=\lambda/\lambda_c-1\) near zero,
\[
\dot s=\delta s+B(z)(\alpha-\alpha_*)s^2+\text{higher-order terms}.
\]
When \(\alpha\ne\alpha_*\), the nonzero branch has
\[
s_*=-\frac{\delta}{B(z)(\alpha-\alpha_*)}+O(\delta^2).
\]
Its center eigenvalue is \(-\delta+O(\delta^2)\), and the transverse eigenvalue remains negative. This establishes both existence side and stability type. At \(\alpha=\alpha_*\), a more precise center equation is \(\dot s=\delta s+C(z)s^3+O(s^4+|\delta|s^2)\), so a stable small positive branch exists for \(\delta>0\) with amplitude \(s_*\sim\sqrt{\delta/(-C)}\). At \(\delta=0\), the positive center dynamics obey \(\dot s=C s^3+O(s^4)\), hence \(t s(t)^2\to1/(-2C)\). The stable transverse mode decays exponentially relative to the center amplitude. For \(r<1\), the strong-stable eigenvector has mixed signs, so the local strong-stable manifold has no nonzero point in the nonnegative quadrant; thus every sufficiently small strictly positive initial state follows the stated algebraic profile.

## Verification

Run `python verify.py` using Python 3 and SymPy. The self-contained checker reconstructs the Perron vectors, the stable eigenvalue, the quadratic center coefficient, the center-manifold correction and the cubic coefficient in exact symbolic arithmetic. It verifies both monotonic derivatives and the endpoint and zero-assortativity rational identities, then prints `VERIFY_OK`. The sign arguments for \(B\), \(C\), and the derivatives are explicit rational-polynomial arguments; the verifier is a reproducibility aid and not a substitute for those proofs.

## Relationship to prior work

Mizutaka, Mori and Hasegawa introduce this exact local-infected-neighbor synergy law and the correlated bimodal mean-field equations. Their phase diagrams show a numerically estimated onset near \(\alpha_c\approx0.086\) for neutral mixing and exhibit complicated global bistability for strongly assortative mixing. The theorem here addresses a different, precisely delimited issue: the **closed all-assortativity local degeneracy curve**, its strict monotonicity, the negative cubic sign throughout the interval, and the physical-time critical infection asymptotic.

Taraskin and Pérez-Reche previously classified bifurcations in regular-graph SIS models with exponential infected- or susceptible-neighbor synergy; their regular-graph theory does not give this two-degree linear-neighbor-rate formula. Pérez-Reche and Taraskin's 2025 heterogeneous model uses exponential **susceptible-neighbor** synergy. Wang and collaborators' 2025 spectral approach uses a **global-prevalence** multiplier \(\lambda_0(1+\sigma\rho)\). These mechanisms are not equivalent to the present infection hazard, and neither paper supplies the displayed cubic for the two-class system. Lin and collaborators' 2023 study emphasizes a changing degree distribution rather than the present fixed two-degree, variable mixing-correlation family. These are statement-level comparisons, not claims that related papers did not study synergy thresholds.

## Limitations

This is a local deterministic mean-field theorem. It does not identify the full global coexistence/hysteresis region, nor does it establish finite-network stochastic thresholds. In the completely assortative limit \(r=1\) the two degree classes decouple, and the strict two-component endemic and positive-orbit assertions have not been extended to that endpoint. The 2023 Lin and collaborators article was only partially accessible, and publication priority is conditional on currently available sources; unindexed equivalent analyses remain possible. No independent external validation has been performed.

## References

1. S. Mizutaka, K. Mori and T. Hasegawa, *Synergistic epidemic spreading in correlated networks*, arXiv:2105.08992 (first public 2021-05-19); Phys. Rev. E **106**, 034305 (2022). https://arxiv.org/abs/2105.08992
2. S. N. Taraskin and F. J. Pérez-Reche, *Bifurcations in synergistic epidemics on random regular graphs*, arXiv:1809.05575 (2018); J. Phys. A **52**, 195101 (2019). https://arxiv.org/abs/1809.05575
3. C. Lin, Z. Yan, J. Gao and J. Xiao, *From heterogeneous network to homogeneous network: the influence of structure on synergistic epidemic spreading*, J. Phys. A **56**, 215001 (2023). https://doi.org/10.1088/1751-8121/accf50
4. F. J. Pérez-Reche and S. N. Taraskin, *Multistability and high codimension bifurcations in synergistic epidemics on heterogeneous networks*, arXiv:2504.13293 (2025). https://arxiv.org/abs/2504.13293
5. Z. Wang, J. Gao, S. Wang, Z. Yan and J. Xiao, *Phase transition predictions of synergistic contagions using spectral approach*, Phys. Rev. E **112**, 014311 (2025). https://doi.org/10.1103/w91q-hm26
