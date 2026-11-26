# Exact one-crossing epidemic threshold under alternating directed contacts

## Finding

**Theorem (a sharp switching-interval classification).** Let \(p,q,\mu,\tau>0\). During alternating intervals of the common length \(\tau\), let the two-component infection perturbation \(z(t)\in\mathbb R^2\) obey

\[
\dot z=A_1z,\quad A_1=\begin{pmatrix}-\mu&p\\q&-\mu\end{pmatrix},\qquad
\dot z=A_2z,\quad A_2=\begin{pmatrix}-\mu&q\\p&-\mu\end{pmatrix}.
\]

The first generator acts on \([2n\tau,(2n+1)\tau)\), the second on \([(2n+1)\tau,(2n+2)\tau)\), for every integer \(n\ge0\). Write \(a=\sqrt{pq}\) and \(\kappa=(p+q)/(2\sqrt{pq})\ge1\). The exact dominant per-unit-time Floquet exponent is

\[
\boxed{\gamma(\tau)=-\mu+\frac{1}{\tau}\operatorname{arsinh}\!\left(\kappa\sinh(a\tau)\right).}
\]

If \(p\ne q\), this exponent is **strictly decreasing** for all \(\tau>0\), with endpoint limits

\[
\lim_{\tau\downarrow0}\gamma(\tau)=\frac{p+q}{2}-\mu,
\qquad
\lim_{\tau\to\infty}\gamma(\tau)=\sqrt{pq}-\mu.
\]

Thus a finite crossing \(\gamma(\tau_*)=0\) exists **if and only if**

\[
\boxed{\sqrt{pq}<\mu<\frac{p+q}{2},}
\]

and in this regime it is unique. Every \(0<\tau<\tau_*\) has a dominant multiplier greater than one (linear invasion); every \(\tau>\tau_*\) has a dominant multiplier less than one (linear decay). The crossing is uniquely specified by

\[
\operatorname{arsinh}\!\left(\kappa\sinh(a\tau_*)\right)=\mu\tau_*.
\]

Although both frozen generators are Hurwitz whenever \(\mu>a\), rapid reversal of **directed** cross-group transmission destabilizes their disease-free linearization whenever \(\mu<(p+q)/2\). Outside the crossing regime, \(\gamma(\tau)<0\) for all finite \(\tau>0\) if \(\mu\ge(p+q)/2\), and \(\gamma(\tau)>0\) for all finite \(\tau>0\) if \(\mu\le a\). Endpoint equalities in these two alternatives are strict at finite \(\tau\). When \(p=q\), the generators coincide and \(\gamma(\tau)=p-\mu\) for every \(\tau>0\), including the possibility of zero for all durations.

For fixed unequal \(p,q>0\), the unique critical duration has the sharp endpoint laws

\[
\tau_*\sim\sqrt{\frac{6((p+q)/2-\mu)}{\kappa(\kappa^2-1)a^3}}
\qquad\text{as }\mu\uparrow(p+q)/2,
\]

and

\[
\tau_*\sim\frac{\log\kappa}{\mu-a}
\qquad\text{as }\mu\downarrow a.
\]

Each asymptotic is taken through the nonempty crossing regime, holding \(p,q\) fixed. The assertions classify the Floquet linearization, not extinction probabilities in a finite stochastic epidemic.

## Assumptions and scope

The model is the linearization at the disease-free solution of the two-group mean-field susceptible-infected-susceptible system

\[
\dot x_i=-\mu x_i+(1-x_i)\sum_{j\ne i}b_{ij}(t)x_j,\qquad i=1,2,
\]

where the off-diagonal transmission rates are \((b_{12},b_{21})=(p,q)\) in the first half-period and \((q,p)\) in the second. Here \(0\le x_i\le1\) is an infection fraction and \(\mu\) is the common recovery rate. The directed transmission rates \(p,q\) need not coincide. Positive \(p,q,\mu,\tau\) are arbitrary. The fixed initial phase of the cycle does not change Floquet eigenvalues; reversing the two factors gives a similar monodromy. A strict negative exponent implies local exponential stability of the disease-free periodic solution of this mean-field system, and a strict positive exponent implies local instability. The theorem does not classify nonlinear behavior at zero exponent.

## Proof

Put

\[
B_1=A_1+\mu I=\begin{pmatrix}0&p\\q&0\end{pmatrix},
\qquad B_2=B_1^{\mathsf T}.
\]

Then \(B_1^2=B_2^2=a^2I\). With \(c=\cosh(a\tau)\) and \(s=\sinh(a\tau)/a\), the exact exponentials are \(e^{B_j\tau}=cI+sB_j\). The full-period fundamental matrix is

\[
\mathcal P(\tau)=e^{A_2\tau}e^{A_1\tau}
=e^{-2\mu\tau}(cI+sB_2)(cI+sB_1).
\]

The unattenuated product \(Q=e^{B_2\tau}e^{B_1\tau}\) is positive definite (indeed \(e^{B_2\tau}=(e^{B_1\tau})^{\mathsf T}\)), and \(\det Q=1\). Direct multiplication gives

\[
\operatorname{tr}Q=2c^2+\frac{p^2+q^2}{a^2}\sinh^2(a\tau)
=2+4\kappa^2\sinh^2(a\tau).
\]

For a determinant-one positive definite \(2\times2\) matrix, the eigenvalues are \(e^{\pm2h}\), where \(2\cosh(2h)=\operatorname{tr}Q\). Using \(\cosh(2h)=1+2\sinh^2h\), one obtains the **exact**, positive value

\[
h=\operatorname{arsinh}(\kappa\sinh(a\tau)).
\]

Consequently the two Floquet multipliers are \(e^{-2\mu\tau\pm2h}\), and the logarithm of the leading multiplier divided by the period \(2\tau\) gives the displayed formula for \(\gamma\).

For strict monotonicity suppose \(p\ne q\), so \(\kappa>1\), and define \(H(u)=\operatorname{arsinh}(\kappa\sinh u)\) for \(u\ge0\). A direct differentiation yields

\[
H(0)=0,\qquad
H''(u)=\frac{\kappa(1-\kappa^2)\sinh u}{\left(1+\kappa^2\sinh^2u\right)^{3/2}}<0
\quad(u>0).
\]

By strict concavity and \(H(0)=0\), the quotient \(H(u)/u\) decreases strictly for \(u>0\). Therefore \(\gamma(\tau)=-\mu+aH(a\tau)/(a\tau)\) decreases strictly. Taylor expansion at the origin gives \(H(u)/u\to\kappa\). The large-\(u\) expansion \(H(u)=u+\log\kappa+O(e^{-2u})\) gives \(H(u)/u\to1\). The endpoint limits and complete sign classification follow immediately by strict decrease and the intermediate value theorem. In particular, the frozen matrices have spectral abscissa \(a-\mu\), while the fast-switching average has spectral abscissa \((p+q)/2-\mu\).

For the near-upper-edge expansion, with fixed \(p\ne q\), write \(\Delta=(p+q)/2-\mu\downarrow0\). The odd Taylor series of \(H\) at zero is

\[
H(u)=\kappa u-\frac{\kappa(\kappa^2-1)}6u^3+O(u^5).
\]

At the unique crossing, division by \(\tau_*\) yields

\[
\Delta=\frac{\kappa(\kappa^2-1)a^3}{6}\tau_*^2+O(\tau_*^4).
\]

Strict monotonicity and continuity imply \(\tau_*\downarrow0\) as \(\Delta\downarrow0\), proving the first asymptotic. For the near-lower edge, put \(\varepsilon=\mu-a\downarrow0\). The crossing necessarily has \(\tau_*\to\infty\), and the large-argument expansion of \(H\) gives

\[
\varepsilon\tau_*=\log\kappa+O(e^{-2a\tau_*}),
\]

proving the second asymptotic. This completes all parameter and boundary cases. \(\square\)

## Verification

The executable file `verify.py` uses the Python standard library only and can be run with `python3 verify.py` after extracting it next to this document. It independently constructs the two exact core matrix exponentials, multiplies them, calculates the trace and determinant, computes the dominant eigenvalue from the quadratic formula, and compares it against the hyperbolic-function formula. Its fixed-seed tests cover 1,300 random matrix instances and 260 unequal-rate critical-duration and strict-monotonicity checks, as well as sample near-edge asymptotics. The test output was:

```text
VERIFICATION_OK matrix_tests=1300 monotonic_cases=260
example_critical_half_period=0.8441526499425871
example_rho_tau_0.2=1.0902442189024490
example_rho_tau_1.0=0.9353925203135697
```

In particular, at \(p=4\), \(q=1\), \(\mu=9/4\), both static environments have principal growth \(-1/4\), yet the critical half-period is

\[
\tau_*=0.84415264994258796277\ldots.
\]

The complete-period dominant multiplier is approximately \(1.090244218902449\) at \(\tau=0.2\) and \(0.935392520313569\) at \(\tau=1\). Finite-precision tests do not replace the proof of strict concavity, uniqueness, or the global classification.

## Relationship to prior work

Valdano, Ferreri, Poletto and Colizza (2014/2015) establish general temporal-network epidemic threshold criteria using the spectral radius of an infection propagator, including treatment of directed/weighted cases. Speidel, Klemm, Eguíluz and Masuda (first public version 2016-02-02) develop a continuous-time temporal SIS linearization and monodromy approach, but their explicitly studied snapshot graphs are undirected; they do not derive this reversed-directed-rate family or its strict one-crossing dwell-time classification. Sejunti, Taylor and Masuda (2024) examine a reverse (individually supercritical but periodically subcritical) Parrondo effect, prominently for symmetric two-node contact matrices; their general Floquet machinery supplies context but not the exact mirrored-directed-contact result above. Gökçek (2004) gives general Floquet stability criteria and examples of switching-induced instability with signed off-diagonal entries; Lian and Liu (2013) provide sufficient dwell-time conditions for positive switched systems. These general facts neither fix the specific multiplier nor imply a unique stability crossing for every unequal pair of positive directed rates. A general matrix-product formula can of course be specialized to this pair, and the new assertion is expressly the **closed-form strict monotonicity, iff parameter regime, and sharp critical scaling**, not the already-known monodromy principle.

## Limitations

The model concerns exactly two groups, two alternating phases of equal duration, positive off-diagonal rates that swap between phases, and a common constant recovery rate; extension to other phase fractions, unequal diagonal rates, or three groups is not proved. It is a deterministic disease-free linearization. A principal Floquet multiplier greater than one entails local mean-field invasion, not guaranteed persistent infection in a finite stochastic epidemic; equality at the transition does not establish nonlinear stability or endemicity. The numerical checks sample finitely many parameters. Residual originality risk remains from a possible equivalent specialization in the wider theory of products of positive \(2\times2\) matrices and switched systems; no absolute priority claim is made.

## References

1. E. Valdano, L. Ferreri, C. Poletto, V. Colizza, “Analytical computation of the epidemic threshold on temporal networks,” *Physical Review X* **5** (2015), 021005; first preprint 2014-06-18, arXiv:1406.4815, https://arxiv.org/abs/1406.4815, DOI:10.1103/PhysRevX.5.021005.
2. L. Speidel, K. Klemm, V. M. Eguíluz, N. Masuda, “Temporal interactions facilitate endemicity in the susceptible-infected-susceptible epidemic model,” *New Journal of Physics* **18** (2016), 073013; first preprint 2016-02-02, arXiv:1602.00859, https://arxiv.org/abs/1602.00859, DOI:10.1088/1367-2630/18/7/073013.
3. T. Sejunti, D. Taylor, N. Masuda, “A Parrondo paradox in susceptible-infectious-susceptible dynamics over periodic temporal networks,” *Mathematical Biosciences* **378** (2024), 109336; arXiv:2406.16787, https://arxiv.org/abs/2406.16787.
4. C. Gökçek, “Stability analysis of periodically switched linear systems using Floquet theory,” *Mathematical Problems in Engineering* **2004** (2004), 1–10, https://doi.org/10.1155/S1024123X04401069.
5. J. Lian, J. Liu, “New results on stability of switched positive systems: an average dwell-time approach,” *IET Control Theory & Applications* (2013), https://doi.org/10.1049/iet-cta.2013.0280.
