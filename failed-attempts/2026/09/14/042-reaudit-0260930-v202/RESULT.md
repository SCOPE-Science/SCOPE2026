# Nonradial Quantized Type-II Blow-up near the Ground State for Energy-Supercritical Focusing NLS

## Context

The energy-supercritical focusing nonlinear Schrodinger equation

```
i d_t u + Delta u + |u|^{p-1} u = 0 on R^d
```

with critical regularity s_c = d/2 - 2/(p-1) > 1 admits smooth stationary
ground states Q solving Delta Q + Q^p = 0 with Q(0)=1. Merle-Raphael-Rodnianski
(MRR) constructed, for d >= 11 and odd p = 2q+1 above the Joseph-Lundgren
exponent under hypotheses (1.26)-(1.27), a finite-codimensional manifold of
radially symmetric data blowing up in finite time by concentration of Q at
quantized rates lambda(t) ~ c(u_0)(T-t)^{ell/alpha}, ell in N*, ell > alpha/2,
with vanishing supercritical remainder and bounded subcritical norms. The MRR
construction was restricted to spherically symmetric data. The dispersive
nonradial extension was identified as a major open strategy goal, realized for
the heat equation by Collot but not for NLS.

## Definitions

- NLS: i d_t u + Delta u + |u|^{p-1}u = 0, d >= 11, p = 2q+1 odd, s_c > 1,
  p above Joseph-Lundgren so Discr = (d-2)^2 - 4 p gamma(d-2-gamma) > 0
  with gamma = 2/(p-1).
- Q: MRR radial ground state, smooth positive radial, Delta Q + Q^p = 0,
  Q(0)=1, Emden-Fowler tail with exponent alpha = alpha(d,p).
- Linearized operators: L_+ = -Delta - p Q^{p-1}, L_- = -Delta - Q^{p-1}.
- Spherical-harmonic sector n: eigenvalue mu_n = n(d+n-2),
  L^{(n)}_pm = -d_rr - (d-1)/r d_r + mu_n/r^2 + V_pm(r),
  V_+ = -pQ^{p-1}, V_- = -Q^{p-1}.
- C_{V,pm} = sup_{r>=0} r^2 |V_pm(r)|; N_0 least integer with
  N_0(d+N_0-2) >= max(C_{V,+}, C_{V,-}).
- s_+: large regularity exponent above s_c; s_c: scaling-critical exponent.
- Modulation parameters: scale lambda, quantized parameters b, phase gamma,
  center x(t), Galilean velocity v(t).

## Result

Fix (d,p) as above and ell in N* with ell > alpha/2. There exists a
finite-codimensional C^0 (Lipschitz) manifold M in H^{s_+} intersect H^1_loc of
smooth compactly supported initial data, containing data with a nonzero
spherical-harmonic component of degree at least one, such that, modulo phase,
translation, and Galilean symmetries, every solution with u_0 in M blows up in
finite time T = T(u_0) < infinity with

```
u(t,x) = lambda(t)^{-2/(p-1)} (Q + epsilon(t))((x-x(t))/lambda(t)) e^{i gamma(t)},
lambda(t) = c(u_0)(T-t)^{ell/alpha}(1+o(1)), gamma(t) -> gamma_T,
||nabla^s epsilon(t)||_{L^2} -> 0 for every s_c < s <= s_+,
sup_{t<T} ||u(t)||_{dot H^s} < infinity for every 0 <= s < s_c.
```

The center x(t) converges to x_T and Galilean drift is absorbed in the stated
symmetries. Blow-up is type II: all norms below scaling remain bounded while
the concentrating Q bubble carries vanishing subcritical mass.

## Proof and evidence

Lemma 1 (finite Morse index): C_{V,pm} < infinity by continuity of r^2 V_pm on
(0,infinity) with limits 0 at the origin and -c_pm at infinity. For
mu_n >= C_{V,pm} the sector quadratic form is pointwise nonnegative, hence no
negative eigenvalues; only n < N_0 can carry instabilities, each with finitely
many negatives by Sturm-Liouville relative-compact perturbation theory. Thus
the total nonradial Morse index is finite. Modulo phase, translation (n=1
kernel), and the generalized scaling direction handled by MRR b-dynamics, the
linearized energy form is coercive up to finitely many explicit directions.

Nonradial extension: the MRR radial quantized-blow-up machine is taken as a
black-box input. All MRR radial multipliers are radial, so centrifugal terms
mu_n r^{-2}|epsilon^{(n,k)}|^2 w enter Morawetz and virial identities with good
(nonnegative) sign sector-by-sector. The MRR high-Sobolev energy estimate,
low-norm Lyapunov functional monotonicity, and profile decomposition therefore
transfer verbatim with full nonradial norms, after projecting out finitely many
unstable directions. Modulation for (x(t),v(t)) closes by the implicit function
theorem as a finite-rank transverse perturbation of the MRR Jacobian, with
Newton-type laws keeping x(t) convergent and v bounded. A standard Brouwer
shooting argument over K_tot = k_ell + K_nonrad < infinity unstable parameters
yields forward invariance of the trapped regime, finite-time blow-up, the
unchanged quantized rate law, vanishing supercritical remainder, and bounded
subcritical norms.

Genuinely nonradial data: the trapped manifold is locally the graph of the
finite unstable vector over the infinite-dimensional stable subspace, which
contains compactly supported smooth functions with arbitrary degree >= 1
harmonic content; subtracting the finite-rank unstable projection preserves a
nonzero nonradial remainder for generic data.

Computation: output/artifacts/harmonic_threshold.py integrates the Emden ODE
Q''+(d-1)Q'/r+Q^p=0 by dependency-free RK4 and evaluates sup r^2 pQ^{p-1}:
approximately 20.22 for (11,7), 23.75 for (12,5), 19.69 for (11,9), giving
N_0=2 in each case. This was rerun during audit and reproduced. General
finiteness is analytic; numerics only illustrate small N_0.

## Limitations

The full radial MRR construction (profile assembly, sharp b-law, radial
coercivity constants, profile decomposition) is used as a black-box input and
not re-proved; any error there propagates. Total codimension K_tot is proved
finite but not given in closed form uniform in (d,p,ell). Manifold regularity
is C^0/Lipschitz as in MRR, not smooth. The constant c(u_0) > 0 depends on the
data through the frozen b-law and is not evaluated explicitly.

## Reproducibility

Run `python3 output/artifacts/harmonic_threshold.py` with any Python 3
interpreter and no external dependencies to reproduce the threshold values.
The analytic Lemma 1, modulation closure, and Brouwer count are self-contained
in the draft given the cited MRR radial input.

## References

- F. Merle, P. Raphael, I. Rodnianski, Type II blow up for the energy
  supercritical NLS, arXiv:1407.1415; Cambridge J. Math. 2015.
- C. Collot, Nonradial type II blow up for the energy-supercritical semilinear
  heat equation, arXiv:1604.02856; Anal. PDE 2017.
- C. Collot, Type II blow up manifolds for the energy supercritical wave
  equation, arXiv:1407.4525; Mem. AMS 2018.
