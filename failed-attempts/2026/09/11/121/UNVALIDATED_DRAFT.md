# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Disproof of the claimed nonzero-winding Fisher–Hartwig ladder at κ=1

## 1. Claim under test

Let `f0(z) = |z+1|^{1/2} g_{-1,1/4}(z)` be the Fisher–Hartwig symbol with
`α = β = 1/4` at `z0 = -1`, `V = 0`, let `w(z) = z f0(z)` (winding number `κ = 1`)
and `D_n` the `n × n` Toeplitz determinant. The target asserts

    D_n(w) = (-1)^n W⋆ E0 n^{-1/2} (1 + O(n^{-1/2})),     (†)

with `E0 = 2^{-1/8}` and `W⋆ = 2^{-3/4} e^{iπ/8} Γ(3/4)/Γ(5/4) ≠ 0`.
In particular `|D_n(w)| ~ C n^{-1/2}` with `C = |W⋆|E0 ≈ 0.737 > 0`.

**Theorem (disproof).** Under the standard Fisher–Hartwig branch convention
(Ehrhardt; Deift–Its–Krasovsky), `D_n(w) = 0` for every `n ≥ 1`. Hence (†) is false.
The same holds for either global branch choice of the square root.

## 2. The base symbol is analytic

Parametrize `z = e^{iθ}`, `θ ∈ (-π, π)`. The standard jump factor at `θ0 = π`
with `β = 1/4` is `g(θ) = e^{iβθ} = e^{iθ/4}` on `(-π, π)` (equivalently one-sided
limits `e^{±iπβ}` at the cut). Since `|e^{iθ}+1| = 2cos(θ/2) ≥ 0` there,

    f0(e^{iθ}) = (2cos(θ/2))^{1/2} e^{iθ/4}.

Meanwhile, for the principal branch, `(1+e^{iθ})^{1/2} = (2cos(θ/2))^{1/2} e^{iθ/4}`
on the same interval, because `1+e^{iθ} = 2cos(θ/2)e^{iθ/2}` with `cos(θ/2) > 0`
a.e. Hence as `L¹(𝕋)` functions,

    f0(z) = (1+z)^{1/2} = Σ_{k≥0} c_k z^k,   c_k = binom(1/2, k),

with Taylor coefficients `c_0 = 1, c_1 = 1/2, c_2 = -1/8, c_3 = 1/16, …`
The negative Fourier coefficients of `f0` all vanish:

    (f0)_m = c_m (m ≥ 0),  (f0)_m = 0 (m < 0).

So the jump phase and the modulus *recombine* into an analytic function — the
`α = β` choice produces a square-root *zero* at `z = -1`, not a two-sided tail.
This is verified numerically to ~1e-38 in
`output/artifacts/fourier_support_table.py` (30-digit mpmath quadrature:
negative modes vanish; nonnegative modes equal `binom(1/2,k)`).

Integrability/series justification. `Σ|c_k| < ∞` since `|c_k| ~ 1/(2√π k^{3/2})`;
indeed one checks by hand that `|c_k| ≤ 1/(2k^{3/2})` for `k ≥ 1` (equality at
`k=1`; the induction step `|c_{k+1}|/|c_k| = (k-1/2)/(k+1)` reduces to
`(k-1/2)²(k+1) ≤ k³`, i.e. `k ≥ 1/3`), so the Taylor series converges absolutely
and uniformly on `𝕋` to the continuous representative of `f0`, and its coefficients
are the Fourier coefficients. Hence `T_n(f0)` is lower-triangular with unit
diagonal, so `D_n(f0) = 1` for all `n` — already contradicting the auxiliary
claim `E0 = 2^{-1/8}` as the base limit (the `α=β` cancellation zeroes the
usual FH power and the constant collapses to 1 in this normalization).

## 3. The winding shift kills every determinant

Fourier shift: `(w)_k = (f0)_{k-1}`. Therefore

    (w)_k = 0 for every k ≤ 0.

The first row of the Toeplitz section `T_n(w)` is `((w)_{-(j-1)})_{j=1..n} = 0`.
Hence

    D_n(w) = 0  for every n ≥ 1,

exactly. This is certified by exact rational arithmetic in
`output/artifacts/verify_disproof.py` (stdlib `Fraction` Gaussian elimination:
`D_n(w) = 0`, `D_n(f0) = 1` for `n = 1..8`; the first-row argument extends it
to all `n`). At `n = 1` alone: exact `D_1(w) = (f0)_{-1} = 0` versus claimed
`|D_1| ≈ 0.737` — a single-point falsification with gap ~0.74.

Branch robustness. Flipping the global branch sign sends `(1+z)^{1/2} → -(1+z)^{1/2}`,
scaling every `D_n(w)` by `(-1)^n` but preserving exact vanishing. The computation
uses the literature-standard convention shared by the cited base sources
(Ehrhardt one-singularity theorem; Deift–Its–Krasovsky), so the disproof is
stated in exactly the normalization under which `E0` was imported.

## 4. What the target's preflight got wrong

- `(f0)_{-1} ≠ 0` (claimed nonzero): exact value is `0`.
- `f0` has "infinitely many nonzero positive and negative coefficients":
  false — negative coefficients all vanish (analyticity shown above).
- Base limit `E0 = 2^{-1/8}`: exact `D_n(f0) = 1` for all `n`.
- "Generically nonzero one-dimensional section": the section is identically
  zero by triangularity, so no Wiener–Hopf/OPUC asymptotics can produce a
  nonzero `W⋆`.

## 5. Value of the negative resolution

This is the first certified *winding obstruction* for a Fisher–Hartwig base of
precisely the type the admission review declared independently valuable:
rather than a nonzero `n^{-1/2}` ladder, the `κ = 1` shift of this analytic-type
base annihilates the determinant identically. It pins down exactly where ladder
formulas break — when the base symbol's Fourier support is one-sided, a positive
winding shift pushes the section into triangular vanishing — and tells
practitioners the `α = β` diagonal is degenerate for winding ladders. Any future
ladder program must avoid the analytic/anti-analytic diagonals or shift in the
opposite direction.

## 6. Reproduction

- `python3 output/artifacts/verify_disproof.py` → `VERIFY_OK` (stdlib only).
- `python3 output/artifacts/fourier_support_table.py` → `SUPPORT_TABLE_OK`
  (requires `mpmath`; 30-digit quadrature).

## 7. Limitations

- The disproof assumes the standard FH branch convention used by the cited base
  literature; a nonstandard jump convention with the cut placed so that `f0`
  is anti-analytic would move the vanishing to a different shift direction,
  but the stated target (with `w = z f0` and the imported `E0`) is false as written.
- No replacement ladder constant is claimed; the general `κ`-ladder program for
  non-degenerate (`α ≠ ±β`) parameters remains open.
