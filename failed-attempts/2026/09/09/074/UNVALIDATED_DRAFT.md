# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# First high-precision R-symmetric halo-type periodic orbit of the spatial ERTBP at lunar eccentricity

## Claim

In the spatial elliptic restricted three-body problem (pulsating rotating frame,
Earth-Moon `mu = 0.012150585609624`, eccentricity exactly `e = 0.0549`), there
exists a numerically certified R-symmetric periodic orbit of primary period
(`2pi` in true anomaly `f`) continuing the circular L1 northern halo family,
with Fix(R) section crossings

- `a` at `f = 0`: `(x, z, vy) = (0.873491766672, 0.200416848519, 0.221727034018)`
  (with `y = vx = vz = 0`);
- `b` at `f = pi`: `(x, z, vy) = (0.993674921511, -0.030161618419, -0.881666894091)`
  (with `y = vx = vz = 0)`,

reproducing the two-point symmetric shooting residual
`‖(phi_{0->pi}(a) - b, phi_{pi->2pi}(b) - a)‖ = 1.47e-12` and full-period closure
`‖phi_{0->2pi}(a) - a‖ = 9.6e-11` under the archived replay script
(`output/artifacts/verify_orbit.py` → `VERIFY_OK`). A second, independent
integrator (`mpmath.odefun`, Taylor degree 12, 40-digit arithmetic) reproduces
both halves with residual components `<= 7e-11`. The e = 0 generating orbit is
the circular L1 northern-halo loop of period exactly `2pi/3` at
`(x0, z0, vy0) = (0.88278262, 0.19428077, 0.21872137)` (half-period `pi/3` to
`4e-13`), continued in `e` from 0 to 0.0549 with every step converged
(`output/artifacts/continue.log`). Finite-difference monodromy at `e = 0.0549`
gives eigenvalues approximately
`-6.147, 3.516 ± 0.781i, 0.271 ± 0.060i, -0.163` (det ≈ 1.00002), i.e. a
saddle × saddle-focus × stable linear type, distinct from the planar Lyapunov
orbit (which has `z ≡ 0`).

## Status of proof

This is a **high-precision numerical certificate, not an interval proof**: no
Taylor-model/Krawczyk inclusion is claimed. Residuals above are ordinary
floating-point defect norms, replayed by two independent codes, and are stated
as defect bounds of the computed pseudo-orbit, not as validated existence
enclosures. The target's validated existence-plus-stability-type claim and the
preset fallback's Krawczyk-box criterion are therefore **not** met; this report
is filed as an emergent finding (computational discovery + replayable
benchmark), not as the target or fallback.

## Method (replayable)

1. **Model.** Pulsating-frame spatial ERTBP, independent variable true anomaly
   `f`, `den = 1 + e cos f`, Earth-Moon `mu`, `e = 0.0549`.
2. **Symmetry reduction.** `R: (x, y, z, vx, vy, vz) -> (x, -y, z, -vx, vy, -vz)`;
   `Fix(R) = {y = vx = vz = 0}`. Reversibility lemma: if `a ∈ Fix(R)` at `f = 0`
   and `phi_{0->pi}(a) ∈ Fix(R)`, then the full `2pi` loop closes through
   `b = phi_{0->pi}(a)`; hence the square 3+3 two-point system
   `(phi_{0->pi}(a) - b, phi_{pi->2pi}(b) - a) = 0` in the
   `(a, b) ∈ Fix(R)²` unknowns (6 unknowns, 12 residuals solved by Gauss–Newton
   to `1.5e-12`).
3. **Seed.** Circular L1 northern-halo family (R-symmetric half-period shooting
   in `y = 0`) continued in amplitude to the period-tripling resonance
   `T = 2pi/3` (three halo loops per primary revolution), located by bisection
   at `z0 = 0.19428077025 ± 1e-11`.
4. **Continuation.** Parameter stepping `e = 0 → 0.0549` (steps `0.01`, then
   `0.002`) with Gauss–Newton (finite-difference Jacobian, least squares);
   every step converged; the log is archived.
5. **Integrators.** Discovery: adaptive Dormand–Prince RK45 (`tol = 1e-12`);
   independent check: `mpmath.odefun` Taylor integrator at 40 digits.
6. **Replay.** `python3 output/artifacts/verify_orbit.py` prints the residual
   norms and `VERIFY_OK` (thresholds: two-point `<= 5e-12`, closure `<= 1e-9`).

## Halo-type identification

- Out-of-plane amplitude `max|z| ≈ 0.20` (≈ 77 000 km), far from the planar
  (`z ≡ 0`) Lyapunov orbit at the same section (which the same 3-equation
  half-map independently locates at `(0.8267, 0, 0.0903)` and which the Newton
  solver demonstrably avoids from halo seeds).
- R-symmetric by construction (both section points in `Fix(R)` to `1e-12`).
- e = 0 limit is a genuine L1 northern-halo loop (R-symmetric, `T = 2pi/3`,
  northern, `Az ≈ 0.194`), not a Lyapunov orbit (Lyapunov orbits at this
  energy have `T ≈ 2.78/2` different signature and `z ≡ 0`).
- One primary revolution carries three halo loops (period-tripling resonance),
  consistent with the Leng–Lei multi-revolution elliptic-halo picture.

## Limitations and open steps

- No interval enclosure: wrapping, transversality, and Krawczyk inclusion are
  not addressed; a validated upgrade needs a Taylor-model Lohner code with QR
  plus the reversibility-lemma square system above (which reduces the rigorous
  problem to the 6-unknown two-point map already identified).
- Stability type is reported from finite differences (error ~1e-5 in
  eigenvalues, witnessed by `det M = 1.00002`); no validated monodromy box.
- Uniqueness within the section box and continuation in `e` beyond 0.0549 are
  not proved.

## Artifacts

- `output/artifacts/fast.py` — ERTBP RHS + adaptive RK45 batch integrator.
- `output/artifacts/verify_orbit.py` — replay script (`VERIFY_OK`).
- `output/artifacts/w_star.npy` — section vector `w*` (6 floats).
- `output/artifacts/continue.log` — e-continuation convergence table.
