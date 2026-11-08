# Universal critical inverse-time extinction for monotone adaptive SIS contact feedback

## Finding

For the adaptive SIS prevalence/contact system below, every solution with initially positive infection has a universal, initial-condition-independent inverse-time decay at the exact reproduction threshold. The amplitude depends explicitly on the initial slopes of the link-breaking and link-creation responses. The contact density has a simultaneous signed inverse-time correction.

Let \(z_0=\xi c(0)/(\zeta b(0)+\xi c(0))\) and set \(\tau z_0=1\). Define
\[
\mathcal A=1+\frac{\zeta[c(0)b'(0)-b(0)c'(0)]}{c(0)[\zeta b(0)+\xi c(0)]}\ge1.
\]
Then for **every** \(y(0)\in(0,1]\) and \(z(0)\in[0,1]\),
\[
\lim_{t\to\infty}t y(t)=\frac{1}{\mathcal A},\qquad
\lim_{t\to\infty}t\,[z(t)-z_0]=\frac{h'(0)}{\mathcal A},
\]
where \(h(y)=\xi c(y)/(\zeta b(y)+\xi c(y))\), so \(h'(0)\le0\). Both limits include the boundary case \(b(0)=0\), for which \(z_0=1\). There is no positive-prevalence equilibrium at this threshold.

## Assumptions and scope

Work in recovery-normalized time and let \(\zeta,\xi>0\). Assume \(b,c\in C^2([0,1])\), \(b(y)\ge0\) is nondecreasing and \(c(y)>0\) is nonincreasing on \([0,1]\). The two-dimensional mean-field equations are
\[
\dot y=y[-1+\tau(1-y)z],\qquad
\dot z=-\zeta z b(y)+\xi(1-z)c(y).
\]
The variables \(y,z\in[0,1]\) are prevalence and normalized contact density. Here \(\tau>0\) is the infection-to-recovery ratio. Put \(H(y)=\zeta b(y)+\xi c(y)>0\) and \(h(y)=\xi c(y)/H(y)\); the reproduction ratio is \(\mathcal R_0=\tau h(0)\). The result concerns exactly \(\mathcal R_0=1\), finite strictly positive contact adjustment rates, and strictly positive initial prevalence; it makes no stochastic finite-network claim.

## Proof

**1. Invariance and positivity.** At \(y=1\), \(\dot y=-1\), and at \(y=0\), \(\dot y=0\). At \(z=0\), \(\dot z=\xi c(y)>0\), and at \(z=1\), \(\dot z=-\zeta b(y)\le0\). Thus the unit square is forward invariant. Uniqueness and \(\dot y=y q(t)\) with bounded \(q\) ensure \(y(t)>0\) for every finite \(t\) when \(y(0)>0\).

**2. A global critical extinction bound.** Monotonicity of \(b\) and \(c\) implies for all \(z\in[0,1]\)
\[
\dot z\le-\zeta b(0)z+\xi c(0)(1-z)=-H(0)(z-z_0).
\]
Comparison yields \(z(t)\le z_0+K e^{-H(0)t}\), where \(K=(z(0)-z_0)_+\). Set \(B=\max_{[0,1]}b\) and \(c_*=\min_{[0,1]}c>0\). Another comparison gives
\[
\dot z\ge-\zeta Bz+\xi c_*(1-z).
\]
Consequently there exists \(\eta>0\) with \(z(t)\ge\eta\) for \(t\ge1\), regardless of the initial contact density. Since \(\tau z_0=1\),
\[
\dot y\le \tau K e^{-H(0)t}y-\tau\eta y^2 \quad(t\ge1).
\]
For \(w=1/y\), this is \(\dot w\ge\tau\eta-\tau K e^{-H(0)t}w\). The integrating factor for the integrable nonnegative coefficient gives \(w(t)\ge C_1t-C_2\) for suitable positive constants at sufficiently large \(t\). Hence \(y(t)=O(t^{-1})\to0\).

**3. Contact relaxation.** The exact equation is \(\dot z=H(y)[h(y)-z]\). As \(y\to0\), \(H(y)\to H(0)>0\) and \(h(y)\to z_0\). Variation of constants, using the positive uniform lower bound for \(H\), proves \(z(t)\to z_0\). Hence \(\dot y/y=\tau(1-y)z-1\to0\).

**4. A first-order tracking identity.** Put \(v=z-h(y)\) and \(r=v/y\). Since \(y>0\), differentiation is legitimate, and
\[
\dot r=-\left(H(y)+\frac{\dot y}{y}\right)r-h'(y)\frac{\dot y}{y}.
\]
The coefficient multiplying \(-r\) tends to \(H(0)>0\), while the forcing tends to zero. The scalar stable-equation integrating factor therefore gives \(r(t)\to0\). Taylor expansion then yields
\[
 z=z_0+h'(0)y+o(y).
\]
This argument obtains a global tracking estimate rather than assuming a center manifold or extrapolating finite simulations.

**5. Exact coefficient and both limits.** Using \(\tau z_0=1\) and the tracking expansion,
\[
\frac{d}{dt}\frac1y=\frac{1-\tau(1-y)z}{y}=1-\tau h'(0)+o(1)=\mathcal A+o(1).
\]
Integration and division by \(t\) show \((t y(t))^{-1}\to\mathcal A\). Direct differentiation of \(h\) gives
\[
 h'(0)=\frac{\xi\zeta[c'(0)b(0)-c(0)b'(0)]}{[\zeta b(0)+\xi c(0)]^2}\le0,
\]
and \(\mathcal A=1-\tau h'(0)\), which is the stated formula. Multiplying the contact expansion by \(t\) proves the second limit. Finally a positive equilibrium would satisfy \(z=h(y)\) and \(1=\tau(1-y)h(y)<\tau h(0)=1\), a contradiction: \(h\) is nonincreasing and \(y>0\). This proves the claim.

## Verification

The standalone `verify.py` checks the symbolic derivative and amplitude identities with exact algebra and the fixed-contact Riccati solution exactly. It also integrates five admissible response pairs to large finite time and checks the predicted scaled prevalence and contact corrections numerically. In those finite tests, relative prevalence-amplitude discrepancies are below \(2.4\times10^{-5}\). To reproduce: run `python verify.py` with SymPy and SciPy installed. The proof above, rather than the numerical experiments, establishes the infinite-time limits for all admissible responses.

## Relationship to prior work

Achterberg and Sensi introduced the exact two-dimensional adaptive NIMFA system with general prevalence-dependent link-breaking and link-creation responses and determined its reproduction ratio and qualitative equilibria. Their work does not state the global, initial-condition-independent \(t^{-1}\) amplitude and contact correction at the **equality** threshold under monotone avoidance. Achterberg, Sensi and Sottile proved global disease-free stability for multigroup adaptive SIS under monotone responses when \(\mathcal R_0<1\); the strict inequality does not supply the critical equality or its rate. Earlier adaptive-network moment closures concern more general stochastic network models and different approximations. Prior critical rates in other epidemic systems do not imply this exact feedback-slope coefficient. The equilibrium and scalar linear-tracking tools used here are classical and are not claimed as novel in themselves.

## Limitations

The theorem is deterministic and uses recovery-normalized physical time. It requires strictly positive creation response \(c\) and both contact-adjustment rates strictly positive; zero rates, discontinuous responses, nonmonotone avoidance, cross-group couplings, and heterogeneous finite stochastic networks are outside the claim. The decay is asymptotic, not a uniform finite-time error bound across all responses or initial conditions. Formal publication priority cannot be established solely by indexed searching; an equivalent treatment under different terminology may exist.

## References

1. M. A. Achterberg and M. Sensi, *A minimal model for adaptive SIS epidemics*, arXiv:2209.01224 (first publicly posted 2022-09-02), https://arxiv.org/abs/2209.01224 ; *Nonlinear Dynamics* 111 (2023), 12657–12670, https://pmc.ncbi.nlm.nih.gov/articles/PMC10163586/ .
2. M. A. Achterberg, M. Sensi and S. Sottile, *A minimal model for multigroup adaptive SIS epidemics*, arXiv:2407.17639 (first posted 2024-07-24), https://arxiv.org/abs/2407.17639 .
3. M. A. Achterberg and P. Van Mieghem, *Moment closure approximations of susceptible-infected-susceptible epidemics on adaptive networks*, *Physical Review E* 106 (2022), 014308, https://doi.org/10.1103/PhysRevE.106.014308 .
