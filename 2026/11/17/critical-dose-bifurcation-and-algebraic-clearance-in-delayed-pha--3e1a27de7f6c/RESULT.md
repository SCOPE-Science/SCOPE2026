# Critical-dose bifurcation and algebraic clearance in delayed phage cocktails

## Finding
For the coinfection-aware multiple-phage delay model of Bardina–Cano–Cuadrado, the equality excluded from its strict linear stability dichotomy has an explicit nonlinear threshold. With the notation below, if \(\kappa>0\), the bacteria-free state is locally asymptotically stable at exactly critical dosing and every sufficiently small compatible bacterial-positive history has the universal physical-time limits
\[
 tS(t)\longrightarrow\kappa^{-1},\quad tI(t)\longrightarrow J/\kappa,\quad t(Q_i(t)-q_i^*)\longrightarrow\sigma_i/\kappa.
\]
If \(\kappa<0\), the bacteria-free state is repelling toward positive bacteria at critical dosing. When the bacterial net growth parameter moves by \(\delta\) through the critical dose, the nonzero equilibrium branch satisfies \(S_*=\delta/\kappa+O(\delta^2)\), so the direction of the local exchange of stability is determined by the sign of \(\kappa\). No assertion is made at \(\kappa=0\).

## Assumptions and scope
Fix any integer \(n\ge1\). The susceptible bacterial count \(S\), infected bacterial count \(I\), and free-phage counts \(Q_i\) satisfy the retarded system
\[
\begin{aligned}
\dot S(t)&=\bigl(\alpha-\sum_{i=1}^n k_i Q_i(t)\bigr)S(t),\\
\dot I(t)&=\sum_{i=1}^n k_i[Q_i(t)S(t)-z_i Q_i(t-\tau_i)S(t-\tau_i)]-\mu I(t),\\
\dot Q_i(t)&=d_i-m_iQ_i(t)-k_iQ_i(t)S(t)-\ell_iQ_i(t)I(t)
 + k_i b_i z_iQ_i(t-\tau_i)S(t-\tau_i),
\end{aligned}
\]
where \(z_i=e^{-\mu\tau_i}\). All \(k_i,\ell_i,d_i,m_i,b_i,\tau_i,\mu,\alpha\) are strictly positive. Histories are continuous and nonnegative, and are biologically compatible in the sense
\[
 I(0)=\sum_i k_i\int_{-\tau_i}^{0}e^{\mu s}Q_i(s)S(s)\,ds.
\]
Take \(q_i^*=d_i/m_i\) and critical growth \(\alpha_c=\sum_i k_iq_i^*\). Introduce
\[
 J=\frac1\mu\sum_i k_iq_i^*(1-z_i),\qquad
 \sigma_i=\frac{q_i^*}{m_i}\bigl[k_i(b_iz_i-1)-\ell_i J\bigr],\qquad
 \kappa=\sum_i k_i\sigma_i.
\]
The precise conclusions hold in a sufficiently small neighborhood of the constant history \(E_0=(0,0,q_1^*,\ldots,q_n^*)\) in the continuous-history phase space, restricted to compatible physical histories and with \(S(0)>0\). In the statement with varying \(\delta=\alpha-\alpha_c\), all remaining parameters are fixed. Equilibrium stability is local in the compatible positive state space.

## Proof
**Step 1 (spectrum and center direction).** Writing \(S=u\), \(I=v\), \(Q_i=q_i^*+w_i\), the linearization is
\[
\begin{aligned}
\dot u&=\delta u,\\
\dot v&=\sum_i k_iq_i^*[u(t)-z_i u(t-\tau_i)]-\mu v,\\
\dot w_i&=-m_iw_i+k_iq_i^*[b_iz_i u(t-\tau_i)-u(t)]-\ell_iq_i^*v.
\end{aligned}
\]
This is a triangular retarded system: its characteristic roots are \(\delta,-\mu,-m_1,\ldots,-m_n\), counting multiplicity; all roots other than \(\delta\) lie in the open left half-plane. At \(\delta=0\), the zero root is simple. Substitution of a constant center eigenfunction \((u,v,w)=(1,J,\sigma_1,\ldots,\sigma_n)\) gives exactly \(\mu J=\sum_i k_iq_i^*(1-z_i)\) and \(m_i\sigma_i=k_iq_i^*(b_iz_i-1)-\ell_iq_i^*J\).

**Step 2 (quadratic drift).** For the smooth finite-delay semiflow, the local center manifold is one-dimensional and, using the physical bacterial coordinate as its parameter, has
\[
 I=JS+O(S^2),\qquad Q_i-q_i^*=\sigma_i S+O(S^2).
\]
The delayed coordinate satisfies \(S(t-\tau_i)=S(t)+O(S(t)^2)\) on this manifold at criticality because \(\dot S=O(S^2)\); the displayed linear coefficients already follow from the zero-eigenvalue equation without this approximation. Substituting in the *exact* susceptible equation gives
\[
 \dot S=-\kappa S^2+O(S^3)\qquad (\delta=0).
\]
For \(\delta\) small, smooth parameter-dependent center reduction gives \(\dot S=\delta S-\kappa S^2+O(|\delta|S^2+S^3)\). The implicit function theorem yields the branch \(S_*=\delta/\kappa+O(\delta^2)\) when \(\kappa\ne0\). Its center eigenvalue is \(-\delta+O(\delta^2)\), and all transverse roots remain strictly stable. Thus positive-branch stability and direction are determined by the signs of \(\delta\) and \(\kappa\).

**Step 3 (physical trajectories).** The stable foliation of the one-dimensional center manifold supplies exponential transverse tracking. The stable manifold of \(E_0\) is exactly the invariant bacterial-free slice \(S=0\) locally: this slice is invariant and its tangent space is precisely the stable spectral subspace, so uniqueness of the local stable manifold applies. Consequently a sufficiently small compatible trajectory with \(S(0)>0\) does not converge exponentially along the stable manifold. When \(\kappa>0\), it stays in a small positive neighborhood, approaches the center manifold, and has \(S(t)>0\) with \(\dot S=-\kappa S^2+O(S^3)\) up to exponentially small transverse errors. The ordinary parabolic asymptotic gives \(tS(t)\to1/\kappa\); the center graph and exponential tracking give the stated simultaneous limits for \(I\) and every \(Q_i\). For \(\kappa<0\), the positive center drift has the opposite sign, so the bacteria-free state is not Lyapunov stable in the physical positive state space and positive trajectories sufficiently near it eventually leave a fixed small neighborhood.

**Step 4 (both signs occur).** For a single phage with \(k_1=\ell_1=d_1=m_1=\mu=1\), \(\tau_1=\log2\), and \(\alpha_c=1\), one gets \(J=1/2\) and \(\kappa=b_1/2-3/2\). Thus \(b_1=4\) yields \(\kappa=1/2\), whereas \(b_1=2\) yields \(\kappa=-1/2\); both cases satisfy every positivity and latency assumption.

## Verification
The standalone `verify.py` checks the center-eigenvector identities for three symbolic phage types and the two exact opposite-sign scalar examples. Its output is `VERIFY_OK linear_infected=1 linear_phages=3 scalar_opposite_signs=2`. Those finite symbolic checks corroborate, but do not replace, the center-manifold and stable-foliation arguments.

## Relationship to prior work
Bardina, Cano and Cuadrado, arXiv:2611.08370v1 (first posted November 5, 2026), establish the delay model, well-posedness, and the strictly positive/negative *linear* dose criteria (their Proposition 5.1). Their discussion does not analyze the equality \(\alpha=\alpha_c\), give the center coefficient \(\kappa\), or derive the critical physical-time limits. Their earlier single-phage and stochastic references concern different restrictions or regimes. Standard retarded functional differential-equation center-manifold theory supplies the abstract reduction framework, not the model-specific coefficient or its mixed coinfection–latency sign.

## Limitations
This is a **local** result near the bacteria-free equilibrium, not a global eradication theorem. It requires compatible nonnegative histories and fixed positive finite delays. It makes no assertion for \(\kappa=0\), at large bacterial loads, for stochastic fluctuations, or for the existence of a distant attracting coexistence state on the backward side. Historical priority is provisional, particularly relative to earlier single-phage bifurcation analyses. Independent scientific audit has not been performed.

## References
1. X. Bardina, M. Cano, and S. Cuadrado, *Modelling and analysis of a cocktail phage therapy with coinfection*, arXiv:2611.08370v1 (first posted 2026-11-05), https://arxiv.org/html/2611.08370v1.
2. X. Bardina, S. Cuadrado, and C. Rovira, *Coinfection in a stochastic model for bacteriophage systems*, Discrete and Continuous Dynamical Systems B **24** (2019), 6607–6620, https://doi.org/10.3934/dcdsb.2019158.
3. J. K. Hale and S. M. Verduyn Lunel, *Introduction to Functional Differential Equations*, Springer, 1993 (standard center-manifold and spectral theory for smooth retarded equations).
