# Separation-independent modal transition for harmonically confined diffusion under symmetric resetting

## Finding

Fix \(\kappa,D,r,a>0\). Between independent rate-\(r\) Poisson reset events, a particle evolves by the Ornstein--Uhlenbeck equation
\[
dX_t=-\kappa X_t\,dt+\sqrt{2D}\,dW_t.
\]
Every reset independently replaces the position with a draw from a fixed symmetric probability measure \(\mu\) satisfying \(\mu((-a,a))=0\). Let \(p\) be the stationary spatial probability density. Then, **throughout the reset-free gap** \((0,a)\),
\[
\begin{array}{c|c}
0<r<\kappa & p'(x)<0\\
r=\kappa &p'(x)=0\\
r>\kappa &p'(x)>0.
\end{array}
\]
In particular, the exact local-modal transition occurs at the reset rate equal to the trap relaxation rate, independent of the size of the gap, the diffusivity, or the reset distribution outside the gap.

For the physically natural equal-weight two-site reset law
\[
\mu=\tfrac12(\delta_{-a}+\delta_a),
\]
this is the **complete global modal phase diagram**: for \(0<r<\kappa\), \(p\) is strictly decreasing on \((0,\infty)\) and its sole maximum is at \(0\); for \(r>\kappa\), \(p\) is strictly increasing on \((0,a)\), strictly decreasing on \((a,\infty)\), and its only two maxima are \(\pm a\). For \(r=\kappa\), it is constant exactly on \([-a,a]\) and strictly decreases outside. The flat interval is an exact stationary plateau rather than a limiting approximation.

At the threshold \(r=\kappa\), an explicit normalized density is
\[
p(x)=\frac{\kappa}{2D}\exp\!\left(\frac{\kappa a^{2}}{2D}\right)
\int_{\max(|x|,a)}^{\infty}
\exp\!\left(-\frac{\kappa y^{2}}{2D}\right)dy.
\]

## Assumptions and scope

The process is on the entire real line; reset times form an independent homogeneous Poisson process; reset positions are independent, identically distributed and symmetric; the diffusion is overdamped with constant positive diffusivity and harmonic restoring drift. For the gap theorem, the reset law can have atoms, continuous parts, or unbounded support, but has no mass in \((-a,a)\). For the global classification it is exactly the equally weighted two-atom law at \(\pm a\), where \(a>0\). No classification of extrema *outside* the gap is asserted for arbitrary reset measures. All inequalities are exact for finite positive parameters.

## Proof

**1. Stationary existence, positivity, symmetry, and the gap equation.** If \(P_t(x\mid y)\) denotes the no-reset OU heat kernel, its Gaussian mean and variance are
\[
m_t(y)=ye^{-\kappa t},\qquad v_t=\frac{D}{\kappa}(1-e^{-2\kappa t}).
\]
Independent Poisson renewal gives a unique invariant density,
\[
p(x)=r\int_0^\infty e^{-rt}\int P_t(x\mid y)\,\mu(dy)\,dt.
\]
The integral is a probability density, strictly positive for every finite \(x\), and even when \(\mu\) is symmetric. On the source-free open interval \((-a,a)\), it is smooth and satisfies, by the stationary forward equation,
\[
D p''(x)+\kappa x p'(x)+(\kappa-r)p(x)=0,\qquad p'(0)=0.
\]
The density is smooth inside the gap by standard interior elliptic regularity (or the homogeneous second-order ODE).

**2. Universal strict sign in the gap.** Evaluating the ODE at \(x=0\) gives
\[
p''(0)=\frac{r-\kappa}{D}p(0).
\]
At any other interior zero of \(p'\), the same ODE gives \(p''=(r-\kappa)p/D\), whose sign is strictly the sign of \(r-\kappa\). When \(r>\kappa\), \(p'\) therefore starts positive to the right of zero and cannot have a first subsequent zero: at any such first zero its derivative would have to be nonpositive, whereas \(p''>0\). Likewise when \(r<\kappa\), \(p'\) starts negative and cannot have a first subsequent zero because \(p''<0\) at every zero. If \(r=\kappa\), the gap equation reduces to \(D p''+\kappa x p'=0\). Its general first derivative is \(C\exp[-\kappa x^2/(2D)]\); symmetry forces \(C=0\). This proves all three gap cases for every symmetric gapped reset distribution.

**3. Complete classification for two reset atoms.** In the two-atom case the stationary equation has sources of mass \(r/2\) at \(\pm a\). Integrating through \(a\) yields continuity of \(p\) and the derivative jump
\[
p'(a+)-p'(a-)=-\frac{r}{2D}.
\]
For \(r<\kappa\), Step 2 gives \(p'(a-)<0\), hence \(p'(a+)<0\). At any zero of \(p'\) on \((a,\infty)\), the homogeneous equation gives \(p''=(r-\kappa)p/D<0\), so a derivative initially negative cannot cross zero there. Consequently \(p'<0\) everywhere to the right of \(a\).

For \(r>\kappa\), on \((a,\infty)\) a zero of \(p'\) would have \(p''>0\), so the derivative could only cross from negative to positive, never from positive to negative. Since \(p\) is positive and tends to zero at infinity (as follows directly from its OU Gaussian renewal integral with bounded reset positions), any nonnegative derivative at any point would force \(p\) to remain increasing eventually, impossible. Thus \(p'<0\) on \((a,\infty)\) also in this case. For \(r=\kappa\), the exterior homogeneous equation gives \(p'(x)=C\exp[-\kappa x^2/(2D)]\); the jump from the zero interior derivative makes \(C<0\). Symmetry supplies the negative half-line. No additional stationary extrema exist.

**4. Exact critical plateau and normalization.** At \(r=\kappa\), set \(p'\equiv0\) inside \((-a,a)\); the jump at \(a\) fixes the exterior derivative to
\[
p'(x)=-\frac{\kappa}{2D}\exp\!\left(\frac{\kappa(a^2-x^2)}{2D}\right),\qquad x>a.
\]
Integrating inward from \(p(\infty)=0\) gives the displayed formula, whose interior value is constant. It integrates to one because, writing \(c=\kappa/(2D)\) and \(C=ce^{ca^2}\int_a^\infty e^{-cy^2}dy\),
\[
2aC+2ce^{ca^2}\int_a^\infty(y-a)e^{-cy^2}dy=1.
\]
This is also the unique invariant density supplied by the renewal integral in Step 1.

## Verification

The standalone Python program `verify_modal.py` numerically evaluates the *independent renewal-age Gaussian mixture* using the change of variable \(t=s^2\), compares the exact plateau formula with direct integration, checks stationary shape on grids for multiple reset separations and rates on both sides of the threshold, checks its normalization, and independently confirms the second moment
\[
\mathbb E[X^2]=\frac{2D+ra^2}{2\kappa+r}
\]
for the two-point model. It passed 33 deterministic checks using SciPy. The global and gap-wide statements are proved above by the ODE sign argument, not inferred from a finite grid.

Reproduce with `python verify_modal.py` in a Python environment with SciPy installed.

## Relationship to prior work

Olsen, *Steady-state moments under resetting to a distribution* (2023), derives the general renewal representation and moment hierarchy for arbitrary resetting distributions in a harmonic potential. The result here treats a different observable: all stationary *spatial modes* and their exact threshold for a symmetric gapped reset source, which do not follow by directly reading a finite moment formula.

Trajanovski et al., *Ornstein-Uhlenbeck process and generalizations* (2023), investigate fixed-location OU resetting and comb constraints rather than equal-weight symmetric two-atom global modality. Pogorzelec and Dybiec, *Resetting induced multimodality* (2023), investigate reset-induced peaks for Levy-driven motion in non-harmonic potentials; they note that multiple resetting sites can produce multimodal states but do not give this Gaussian harmonic exact rate threshold or critical flat plateau. Julián-Salgado et al., *Diffusion with two resetting points* (2023), study the mean first passage to an absorbing target under free Brownian motion, not the stationary spatial modes in a harmonic trap. These general renewal, Fokker--Planck and multimodality frameworks remain essential antecedents.

## Limitations

The result is an exact model-specific stationary statement and does not characterize finite-time shape evolution, asymmetric reset weights, non-Poisson resetting, nonharmonic drift, or global mode counts for an arbitrary gapped symmetric measure. It does not establish publication priority: unlocated equivalent computations and straightforward extensions of published resolvent formulas remain risks. The independent scientific audit has not been performed.

## References

- K. Stølevik Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (first public version 2023-10-07), Phys. Rev. E 108, 044120 (2023). https://arxiv.org/abs/2310.04840
- P. Trajanovski et al., *Ornstein-Uhlenbeck process and generalizations: particle's dynamics under comb constraints and stochastic resetting*, arXiv:2301.12304 (2023). https://arxiv.org/abs/2301.12304
- P. Pogorzelec and B. Dybiec, *Resetting induced multimodality*, arXiv:2301.11427 (2023). https://arxiv.org/abs/2301.11427
- P. Julián-Salgado, L. Dagdug, D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897 (2023). https://arxiv.org/abs/2311.11897
