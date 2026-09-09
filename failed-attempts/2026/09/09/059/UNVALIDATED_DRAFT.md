# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact helicity pair for the one-full-Lutz-twist Hopf contact pair on S^3

## 1. Objects (closed form)

`S^3 = {|z_1|^2+|z_2|^2 = 1}`, Hopf coordinates
`s in [0,pi/2]`, `phi_1, phi_2 in [0,2pi)`:
`z_1 = cos s e^{i phi_1}`, `z_2 = sin s e^{i phi_2}`.
Orientation: `Omega = ds ^ dphi_1 ^ dphi_2`; common volume
`mu_0 = Omega/(4pi^2)` (total mass 1). Helicity of a field
`X = A(s) d_1 + B(s) d_2` is `H(X) = \int X \cdot curl^{-1} X mu_0`-paired,
computed by the axisymmetric potentials of Section 3.

Standard tight form: `alpha_std = cos^2 s dphi_1 + sin^2 s dphi_2`.
`d(alpha_std) = -sin 2s ds^dphi_1 + sin 2s ds^dphi_2`.
Reeb field: **`R_std = d_{phi_1} + d_{phi_2}`** (i.e. `A=B=1`),
verified by `alpha_std(R)=1`, `i_R d(alpha_std)=0` (sympy).
Round-metric curl: `curl R_std = -2 R_std` in the `Omega` orientation
(`|lambda|=2`); divergence-free exactly by `S^1 x S^1` symmetry.

Lutz-twist form (fallback certificate model). Fix
`delta = 0.35`, `d_2 = 0.70`. On the twist layer `(0,delta)`:

> **`alpha_pi = cos(m_0 s) dphi_1 + sin(m_0 s) dphi_2`,
> `m_0 = 2pi/delta = 40pi/7`.**

Contact condition: `D := h_1 h_2' - h_2 h_1' = m_0 > 0` **exactly**
(constant). Winding: `psi(s) = m_0 s` runs `0 -> 2pi`: one full Lutz turn.
Reeb field on the twist layer: **`A(s) = cos(m_0 s)`, `B(s) = sin(m_0 s)`**
exactly (since `A = h_2'/D`, `B = -h_1'/D`).
Gluing: on `(delta,d_2)` a `C^0` matching layer
`rho in [1, rho_std(d_2)]` linear, `psi: 2pi -> 2pi+psi_std(d_2)` linear with
`psi' = m_1 = psi_std(d_2)/(d_2-delta) > 0` so `D = rho^2 m_1 > 0` exactly;
on `[d_2,pi/2)` the standard profile. Hence `alpha_pi ^ d(alpha_pi) != 0`
on every open piece (contact off the two knot circles and the core, where the
model is Lipschitz; all integrals below are knot-measure-zero independent).

Regularity statement (honest): the certificate twist layer is a Lipschitz
(`C^0`) Lutz profile — `h_2(s) ~ m_0 s` at the core rather than `s^2` — so it
is a *piecewise-smooth* contact model, not a smooth one. The smooth
(`C^1`-glued, `chi(t) = 3t^2-(2+eta)t^3+eta t^4`) model of
`output/artifacts/verify_target.py` carries the same winding with full
smoothness (CONTACT PASS there); its helicity is `-0.0219277665`. Both models
satisfy the fallback inequality with large margin.

## 2. Claim

For this explicitly named pair, normalized to the common volume `mu_0`:

- **`H_std = -1/(4pi^2) ~ -0.0253302959`** (exact closed form);
- **`H_pi = -0.0188237 +/- 1e-6`** (hybrid certificate model; twist-layer
  potentials exact in closed form with differentiation-checked antiderivatives;
  match/standard-layer potentials likewise elementary closed forms;
  final assembly two-grid converged, Richardson `4.1e-7`);
- **`H_pi != H_std`**: `H_pi - H_std ~ +0.00651` (relative `~26%`),
  margin `> 10^4 x` the discretization error (`4.1e-7` Richardson).

## 3. Proof

### 3a. `H_std` by exhibited antiderivative (differentiation-checkable)

With `w = sin 2s/(4pi^2)`, potentials
`F_1(s) = -cos^2 s/(4pi^2)`, `F_2(s) = (cos 2s-1)/(8pi^2)`, `A = B = 1`,
the helicity density is `J(s) = (2pi)^2(F_1 w + F_2 w) = -sin 2s/(4pi^2)`.
Antiderivative: **`F(s) = cos 2s/(8pi^2)`**, `F' - J = 0` (sympy exact).
`H_std = F(pi/2) - F(0) = -1/(4pi^2)`. QED.

### 3b. Twist-layer exact antiderivatives (differentiation-checkable)

On `(0,delta)`, `wA = w cos(m_0 s)`, `wB = w sin(m_0 s)` admit the elementary
antiderivatives (artifact `fallback_cert.py`, `diff = 0` exactly in sympy):

- `P(s) = [140pi sin 2s sin(m_0 s) + 49 cos 2s cos(m_0 s)]/[(800pi^2-98)4pi^2]`,
- `Q(s) = [-140pi sin 2s cos(m_0 s) + 49 sin(m_0 s) cos 2s]/[(800pi^2-98)4pi^2]`.

Hence by FTC (exact closed forms):

- `int_0^delta wA = (-49+49cos(7/10))/(-392pi^2+3200pi^4) ~ -3.7431e-05`;
- `int_0^delta wB = 35 sin(7/10)/(-800pi^3+98pi) ~ -9.2042e-04`.

### 3c. `H_pi` assembly and inequality

Global potentials `F_1(s) = -int_s^{pi/2} wB`, `F_2(s) = -int_0^s wA` are
evaluated with the exact twist-layer pieces above; all six layer
potential-antiderivatives (twist/match/standard for `wA` and `wB`) exist as
elementary closed forms (twist pair `P, Q` displayed above; match/standard
analogues sympy-derived, `diff = 0`). The outer helicity assembly is
evaluated at `N = 6001` and `N = 24001`:
`-0.0188240604 -> -0.0188236538`, Richardson difference `4.1e-7`.
So `H_pi = -0.0188237 +/- 1e-6`, and
`|H_pi - H_std| >= 0.0064 >> 1e-5 >= error`. Therefore **`H_pi != H_std`**.
Replay: `python3 output/artifacts/fallback_cert.py`.

### 3d. Supporting orbit-link data (same Reeb field)

For the Reeb slope spectrum (smooth-model census, `verify_target.py`):
T(2,3) trefoil closed Reeb orbits bracketed at `s in [0.0873425, 0.08736]`
and `[0.2125025, 0.21252]`; meridian `(0,1)` zeros at `~0.17528-0.17530`,
`~0.32744-0.32746`; longitude `(1,0)` zeros at `~0.11415-0.11417`,
`~0.23630-0.23632`; overtwist radii `psi = pi/2, pi, 3pi/2` bracketed at
width `< 2e-6`. Linking integers: `|lk(T(2,3), Hopf fiber)| = 2`
(Gauss `-2.0000` at `n = 3200`), `|lk(T, core)| = 3` (`-3.0000`),
torus-framing self-link `pq = 6` (Gauss `-6.03 -> -6` converging;
sign = orientation convention).

## 4. Limits (what is NOT claimed)

- The full TARGET non-realization (`Phi_*R_pi = fB` impossible) is **not**
  proved: phase-1 analysis showed a bare `H_pi != H_std` comparison cannot
  obstruct realization because `H(cX) = c^2 H(X)` (rescaling absorbs nonzero
  values of matching sign) and volume-preserving pushforward preserves `H`
  while `f`-rescaling does not. This certificate is exactly the
  Arnold-helicity *input* the obstruction program needs, not the obstruction.
- The fallback certificate twist profile is Lipschitz at the core/knots;
  contactness holds on each open piece (`D > 0` exactly). The companion
  smooth model (same winding, `H_pi ~ -0.0219277665`) is in
  `output/artifacts/verify_target.py` (ALL PASS).
- Helicity sign follows the `Omega = ds^dphi_1^dphi_2` orientation; magnitudes
  and the inequality are convention-independent.

## 5. Replay inventory

- `output/artifacts/fallback_cert.py` — exact twist antiderivatives
  (`diff = 0`), FTC values, `H_pi` two-grid convergence. Run:
  `python3 output/artifacts/fallback_cert.py`.
- `output/artifacts/verify_target.py` — smooth-model contact proof
  (analytic twist + exact-quad match cert), `H_std` exact, `H_pi` 3-grid
  converged, orbit brackets. Run: `python3 output/artifacts/verify_target.py`.
- `output/artifacts/fallback_model.py`, `build_model.py` — model builders.
- `output/artifacts/link_cert.py` + `link_cert.json` — Gauss-link convergence
  (`n = 800/1600/3200`).
- `output/artifacts/target_verify.json`, `target_model.json`,
  `fallback_model.json` — logged numbers.
