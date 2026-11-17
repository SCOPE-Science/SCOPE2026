# Exact coexistence threshold and unavoidable real instability for heterogeneous-delay ineffective phage cocktails

## Finding

For the delayed phage-coinfection equations below with at least two genuinely different positive latent periods and a finite number \(n\ge2\) of phage types, assume each type has a nonproductive expected surviving burst, \(b_i e^{-\mu\tau_i}\le1\). Then **exactly one** strictly positive coexistence equilibrium exists if and only if
\[
\sum_{i=1}^n\frac{k_i^1d_i}{m_i}>\alpha.
\]
When it exists, its full delay characteristic equation has a strictly **positive real** root, so the equilibrium is linearly unstable within the biologically compatible history space. At equality or below there is no strictly positive coexistence equilibrium. The result is valid for arbitrarily unequal positive delays, with no small-delay assumption.

## Assumptions and scope

Write \(S\) for susceptible bacteria, \(I\) for infected bacteria, and \(Q_i\) for free phages of type \(i\). Take \(n\ge2\), \(\alpha,\mu,k_i^1,k_i^2,d_i,m_i,b_i,\tau_i>0\); at least two delays differ, and \(b_i e^{-\mu\tau_i}\le1\) for all \(i\). The deterministic system, with no population cap or saturation, is
\[
\begin{aligned}
\dot S&=\left(\alpha-\sum_i k_i^1 Q_i\right)S,\\
\dot I&=\sum_i k_i^1Q_iS-\mu I-\sum_i k_i^1 e^{-\mu\tau_i}Q_i(t-\tau_i)S(t-\tau_i),\\
\dot Q_i&=d_i-m_iQ_i-k_i^1 Q_iS-k_i^2Q_iI+k_i^1b_i e^{-\mu\tau_i}Q_i(t-\tau_i)S(t-\tau_i).
\end{aligned}
\]
Unlabelled factors in delayed products are evaluated at \(t\); the explicitly delayed factors are evaluated at \(t-\tau_i\). The infected-population compatibility condition is
\[
 I(t)=\sum_i k_i^1\int_0^{\tau_i}e^{-\mu r}Q_i(t-r)S(t-r)\,dr.
\]
Here a *strictly positive equilibrium* has positive values for \(S,I,Q_1,\ldots,Q_n\). Local instability refers to the retarded dynamical system on histories satisfying this integral relation, not to stochastic perturbations.

## Proof

Set \(a_i=k_i^1\), \(\ell_i=k_i^2\), \(e_i=e^{-\mu\tau_i}\), and \(p_i=a_i(1-b_i e_i)\ge0\). For hypothetical equilibrium values \(s=S>0\), \(u=I>0\), its phage coordinates must be
\[
 q_i(s,u)=\frac{d_i}{D_i(s,u)},\qquad D_i(s,u)=m_i+p_i s+\ell_i u>0.
\]
The remaining steady-state equations are precisely
\[
 f(s,u)=\sum_i a_i q_i(s,u)-\alpha=0,\qquad
 g(s,u)=\mu u-s\sum_i a_i(1-e_i)q_i(s,u)=0.
\]
These equations are also sufficient: the phage equations and infected balance then hold, and constant positive histories satisfy the biological compatibility integral.

For each \(s>0\), \(g(s,0)<0\), whereas \(g(s,u)\to\infty\) as \(u\to\infty\). Moreover, with all denominators positive,
\[
 g_u=\mu+s\sum_i\frac{a_i(1-e_i)\ell_i d_i}{D_i^2}>0,
 \qquad
 g_s=-\sum_i\frac{a_i(1-e_i)d_i(m_i+\ell_i u)}{D_i^2}<0.
\]
Hence there is a unique \(u=u(s)>0\) solving \(g=0\), and the implicit-function theorem gives \(u'(s)=-g_s/g_u>0\). It extends continuously to \(u(0)=0\). Define
\[
 H(s)=\sum_i\frac{a_i d_i}{m_i+p_i s+\ell_i u(s)}.
\]
This is strictly decreasing for \(s>0\), since each denominator increases and \(u'(s)>0\); \(H(0)=\sum_i a_i d_i/m_i\). Also \(H(s)\to0\): if every \(p_i>0\), every denominator diverges at least linearly; if some \(p_i=0\), boundedness of the increasing \(u(s)\) would contradict \(\mu u(s)=s\sum_i a_i(1-e_i)q_i(s,u(s))\), because a zero-\(p_i\) summand would grow at least linearly. Thus \(u(s)\to\infty\), forcing every denominator to diverge. Therefore the equation \(H(s)=\alpha\) has exactly one positive solution precisely when \(H(0)>\alpha\). Equality is excluded by strict monotonicity.

For spectral instability, order perturbations as \((\delta S,\delta I,\delta Q_1,\ldots,\delta Q_n)\), and let \(\mathcal M(z)\) be the standard \((n+2)\)-dimensional characteristic matrix of the full linearized retarded system. At \(z=0\), eliminate the phage-coordinate block \(\operatorname{diag}(D_1,\ldots,D_n)\) by a Schur complement. Direct differentiation of the two remaining stationary balances gives the exact identity
\[
\det\mathcal M(0)=s\prod_iD_i\,
\det\begin{pmatrix}f_s&f_u\\g_s&g_u\end{pmatrix}
=s\prod_iD_i\,g_u H'(s)<0.
\]
(The final derivative is evaluated at the unique coexistence root and along \(g(s,u(s))=0\).) For real \(z\ge0\), \(\det\mathcal M(z)\) is continuous, and the delayed terms vanish exponentially as \(z\to+\infty\), so \(\det\mathcal M(z)/z^{n+2}\to1\). The intermediate value theorem provides a real root \(z_*>0\).

For such a root the infected perturbation satisfies
\[
 \delta I=\sum_i a_i\big(q_i\delta S+s\delta Q_i\big)
 \frac{1-e^{-(z_*+\mu)\tau_i}}{z_*+\mu},
\]
which is exactly the linearized infected-population compatibility integral for a growing exponential history. Thus the unstable mode is not an extraneous infected-coordinate mode, proving the claimed linear instability.

## Verification

The supplied `CHECKER.py` independently constructs the instantaneous and delayed Jacobian blocks, solves the steady equations numerically, compares the zero-frequency determinant against the analytical two-dimensional Schur-complement identity, locates a positive real characteristic root, and checks that its eigenvector satisfies infected-population compatibility. Test configurations include two and three types with distinct delays, as well as an equality case \(b_i e^{-\mu\tau_i}=1\). Run `python CHECKER.py` after installing the dependencies listed in `requirements.txt`.

These are finite numerical corroborations. The existence, uniqueness, and positive-root conclusions for all admissible parameters come from the analytical monotonicity and determinant arguments above.

## Relationship to prior work

Bardina, Cano and Cuadrado (2026), equations (2.1) and (5.3)–(5.8), derive the original arbitrary-delay model and obtain necessary coexistence conditions, but their sufficient existence and complete equilibrium classification concern the two-type **common-delay** specialization; they report coexistence instability numerically. The result here supplies an exact sufficient-and-necessary threshold, uniqueness, and rigorously positive real characteristic exponent for **unequal delays**, under the explicitly stronger hypothesis that all surviving burst multipliers are at most one. The paper's necessary high-dose condition remains credited rather than claimed as new.

Bardina, Cuadrado and Rovira (2019) analyze a one-phage coinfection model, including positive steady states and bacterial-free stability. That single-delay one-phage classification does not imply this multi-phage unequal-delay spectral conclusion. Published general delayed-infection literature supplies context, not an identical theorem in the particular model.

## Limitations

The nonproductive-surviving-burst condition is sufficient for this complete classification, not asserted necessary. No conclusion is claimed when any \(b_i e^{-\mu\tau_i}>1\); in particular, distinct-latency cocktails with effective types can have other equilibrium structures. A positive real characteristic exponent proves local instability but does not classify the number of unstable exponents, global solution behavior, or the geometry of attraction basins. No claim is made for finite populations, random disturbances, nonlinear saturation, or general time-dependent parameters. Priority outside the inspected literature cannot be ruled out absolutely.

## References

1. X. Bardina, M. Cano and S. Cuadrado, *Modelling and analysis of a cocktail phage therapy with coinfection*, arXiv:2611.08370v1 (first posted 2026-11-05), https://arxiv.org/html/2611.08370v1 .
2. X. Bardina, S. Cuadrado and C. Rovira, *Coinfection in a stochastic model for bacteriophage systems*, Discrete and Continuous Dynamical Systems B 24 (2019), 6607–6620, https://doi.org/10.3934/dcdsb.2019158 ; lawful author preprint https://mat.uab.cat/dpt/Publ/prep/p11_18.pdf .
3. E. E. Kyaw, H. Zheng and J. Wang, *Stability and Hopf Bifurcation Analysis for a Phage Therapy Model with and without Time Delay*, Axioms 12 (2023), article 772, https://doi.org/10.3390/axioms12080772 .
