# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Laplace needle certificate: Cheeger deficit does not control half-space asymmetry

## 1. Definitions

Let `nu(dx) = exp(-2|x|) dx` on `R` (total mass 1, variance 1/2, symmetric,
log-concave). For mass `t in (0,1)` the isoperimetric profile is
`I(t) = f(F^{-1}(t))` with `F` the CDF and `f` the density.
The Cheeger constant is the optimal `C` in `min(mu(A),1-mu(A)) <= C mu^+(A)`;
for mass-1/2 sets the deficit is `delta(A) = psi mu^+(A) - 1/2` with `psi`
that optimal constant. Half-space asymmetry `alpha(A)` is the `mu`-mass of
the symmetric difference with the closest affine half-space (in 1D: a ray).

## 2. Exact 1D profile and tent degeneracy (theorem, proved)

CDF: `F(t) = 0.5 exp(2t)` for `t <= 0`, `1 - 0.5 exp(-2t)` for `t >= 0`.
Inverting: for `t <= 1/2`, `F^{-1}(t) = (1/2) ln(2t) <= 0`, and
`f(F^{-1}(t)) = exp(2 x) = 2t`. By symmetry:

    I(t) = 2 min(t, 1-t),   0 < t < 1.

Hence the optimal Cheeger constant is `psi = 1/2`, and for `s in [0,1/2]`:

    phi(s) := I(s) + I(s+1/2) = 2s + (1-2s) = 1, identically.

Every interval of mass 1/2 has perimeter `I(s)+I(s+1/2) = 1 = I(1/2)`:
every mass-1/2 interval is a minimizer.

## 3. Extremal pair: deficit 0, asymmetry 1/2 (theorem, proved)

Take `c = (ln 2)/2`, `E = (-c, c)`. Then `F(-c) = 1/4`, `F(c) = 3/4`,
mass 1/2; perimeter `f(-c)+f(c) = 1/2+1/2 = 1`, so `delta(E) = 0`.
The mass-1/2 rays are `(-inf,0]`, `[0,inf)`; each disagrees with `E`
on mass `1/4 + 1/4 = 1/2`. Hence `alpha(E) = 1/2`.
No modulus `omega(delta) -> 0` can control 1D half-line asymmetry.

## 4. Isotropic transfer (lemma, proved)

Dilations preserve `(delta, alpha)`: if `Y = lam X`, perimeters scale by
`lam^{-1}` while the optimal Cheeger constant scales by `lam`, so
`delta` is invariant; `alpha` is a mass difference, hence invariant.
With `lam = sqrt(2)` the product laws below become isotropic with the
same numbers.

## 5. 2D consequences (theorem, proved)

Let `mu = nu x nu`. Half-plane `{x1 <= 0}`: mass 1/2, perimeter
`f(0)*1 = 1`. Strip `S = E x R`: mass 1/2, perimeter
`(f(-c)+f(c))*1 = 1` — exact tie. Symmetric square `Q` of side-mass
`m = 1/sqrt(2)`: mass `m^2 = 1/2`, perimeter `4(1-m)m = 2 sqrt(2)-2
≈ 0.8284 < 1`. So half-planes are NOT Cheeger minimizers, and with
`P* <= P(Q)` the optimal constant `psi = 0.5/P*` gives every half-plane
deficit `>= 0.5/P(Q) - 0.5 ≈ 0.1036 > 0.10`. (Minimality of `Q` itself
is NOT claimed.) Also `alpha(S) <= 1/4` via `H* = {x1 <= c}`.

## 6. Needle-averaged remark (interpretation with stated caveat)

For the strip `S` with the natural parallel-line disintegration, every
needle trace is the interval `E` with `delta_l = 0`, `alpha_l = 1/2`,
so averaged control fails for that disintegration. This is stated for
the exhibited disintegration only; quantification over all
KLS-localization disintegrations is open.

## 7. Verification

`output/artifacts/verify_laplace.py` checks every number above in closed
form: 11/12 lines PASS. The one FAIL line (profile grid, maxerr 7.5e-4)
is numerical-inversion resolution on a 4e-4 grid for a slope-2 profile;
Section 2 proves the identity exactly.

## 8. What remains open (not claimed)

A vanishing-deficit sequence `(n_k, mu_k, A_k)` in `n >= 2` (global
target half); square minimality; disintegration quantifiers; novelty
versus equality-case literature (no search permitted in recovery pass).
