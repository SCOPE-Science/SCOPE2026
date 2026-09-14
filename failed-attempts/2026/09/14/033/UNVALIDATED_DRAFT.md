# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Transverse stability of a genuinely traveling finite-gap sine-Gordon stripe — disproof of the universal long-wave instability band

## 1. Problem and result

Consider the two-dimensional sine-Gordon equation

```
u_tt − u_xx − u_yy + sin(u) = 0,   u = u(t,x,y) real.
```

A *stripe* is a one-dimensional traveling wave `U(ξ)`, `ξ = x − c t`, with
subluminal speed `|c| < 1`, extended trivially in `y`. Linearizing
`u = U + w` gives

```
(1)   w_tt − 2c w_ξt + (c²−1) w_ξξ − w_yy + cos(U(ξ)) w = 0.
```

With transverse modes `w = e^{λt+iky} V(ξ)`, `γ² := 1 − c² > 0`, and

```
L₀ := −γ² d²/dξ² + cos(U(ξ)),
```

the spectral problem is the quadratic fiber pencil

```
(2)   P(λ,k) V := [λ² − 2cλ d/dξ + (L₀ + k²)] V = 0,
```

on `L²(ℝ)` (bounded stripe) or `L²_per` per Bloch fiber (periodic stripe).

**Target claim (admitted):** every genus-one/two stripe in the stated moduli
box has a threshold `k_c > 0` such that it is spectrally unstable for
`0 < |k| < k_c` with `Re λ ≥ Λ(k) > 0`, and stable for `|k| ≥ k_c`.

**Theorem (disproof of the universal band).** The universal statement is
**false**. There exists an explicit, genuinely traveling (`c = 1/2`),
genus-one rotational (kink-lattice) stripe

```
(3)   U(ξ) = π + 2 am(νξ | m),   m = 1/2,   ν = 1/(γ√m),   γ² = 3/4,
```

of period `L = 2K(m)γ√m ≈ 2.27077`, such that the full transverse spectrum
satisfies `Re λ = 0` for **every** transverse wavenumber `k ≠ 0` and every
longitudinal Bloch fiber. In fact this holds for **every** subluminal
rotational wave (`U′` nodeless) at **every** `|c| < 1`, including genuinely
traveling ones — not only the stationary case. Hence no universal threshold
`k_c > 0` with a long-wave transverse instability band `0 < |k| < k_c` can
hold over the stated class. The admitted target is resolved on its
**disproof branch**: an explicit stripe in the genus-one class that is
transversely stable for all `k ≠ 0`, with computed `(k,λ)` spectrum.

## 2. Preliminaries: the traveling-wave ODE

With `U(ξ)`, `ξ = x − ct`, the wave equation reduces to

```
(4)   −γ² U″ + sin(U) = 0,   γ² = 1 − c².
```

This is the pendulum equation with first integral

```
(5)   (1/2)(U′)² + γ⁻²cos(U) = E.
```

Two classical regimes:

- **Librational** (trapped): `U` oscillates about a multiple of `2π`; `U′`
  has zeros. Then `φ = U′` has nodes, and `φ` in the kernel of `L₀` is an
  *excited* eigenfunction, forcing `L₀` to have a negative eigenvalue; the
  stripe is already longitudinally (`k = 0`) unstable.
- **Rotational** (untrapped, kink lattice): `U` is strictly monotone,
  `U′` never vanishes (e.g. `U(ξ+Λ) = U(ξ) + 2π` or a periodic oscillation
  of `U` about a running mean with strictly positive velocity). Then
  `φ = U′` is a **nodeless** element of `ker L₀`, so `0` is the ground-state
  eigenvalue and **`L₀ ≥ 0`**.

The admitted box (genus one/two, `|c| < 1`) contains rotational waves; the
explicit wave (3) is one of them. The target's universal instability band
must therefore apply to it — and fails.

## 3. Proof of transverse stability for every rotational stripe

Let `U` be rotational, so `φ(ξ) := U′(ξ)` is bounded, periodic (or periodic
modulo the lattice), nodeless, and satisfies `L₀φ = 0` (differentiate (4)).
Write `q(ξ) := cos(U(ξ))` (periodic potential), and work on one period with
Bloch boundary conditions `V(ξ+L) = e^{iμL}V(ξ)`, or on the line with the
same fiber decomposition. On each fiber:

**Lemma 1 (ground-state factorization).** If `φ` is nodeless and
`L₀φ = 0`, then `⟨V, L₀V⟩ ≥ 0` for all `V` in the domain, with equality only
for multiples of `φ`. Indeed, with `a := φ′/φ` and
`D := γ(d/dξ − a)` (fiber-adjusted), integration by parts gives
`L₀ = D*D ≥ 0` (the boundary terms cancel by the Bloch condition since
`|e^{iμL}| = 1` and `a` is periodic).

*Proof.* Directly,
`D*D = −γ²(d/dξ + a)(d/dξ − a) = −γ²d²/dξ² + γ²(a′ + a²)`,
and `a′ + a² = φ″/φ = q/γ²` from `L₀φ = 0`. ∎

**Lemma 2 (energy identity).** For eigenpairs `P(λ,k)V = 0`, `V ≠ 0`, set
`S := ⟨V, L₀V⟩ ≥ 0`, `N := ‖V‖² > 0`, `J := ⟨V, V′⟩` (fiber derivative).
Pairing (2) with `V` gives

```
(6)   S − 2cλJ + (λ² + k²)N = 0.
```

Since `V′ = (d/dξ)V` is skew-adjoint on each Bloch fiber,
`J = −J̄` is purely imaginary; write `J = −ij` with `j ∈ ℝ`.

**Theorem.** Let `U` be any rotational stripe (`L₀ ≥ 0` by Lemma 1) with
`|c| < 1`. Then for every `k ≠ 0` and every Bloch fiber, every eigenvalue
satisfies `Re λ = 0`. In particular the explicit genus-one traveling stripe
(3) is transversely spectrally stable for all `k ≠ 0`.

*Proof.* Write `λ = σ + iτ`. Separating (6) into imaginary and real parts:

```
(7a)  2σ(τN − cj) = 0,
(7b)  S + 2cτj + (σ² − τ² + k²)N = 0.
```

Suppose `σ ≠ 0`. Then (7a) gives `τN = cj`, i.e. `τ = cj/N`. Substituting
in (7b):

```
(8)   S + c²j²/N + σ²N + k²N = 0.
```

Every term on the left is nonnegative (`S ≥ 0` by Lemma 1), and for
`k ≠ 0` the last two terms cannot both vanish: `k²N > 0` since `N > 0`.
This is a contradiction. Hence `σ = Re λ = 0`. The argument uses only
`L₀ ≥ 0` and `k ≠ 0`; it is uniform in `k ≠ 0`, in the Bloch parameter `μ`,
and in `c ∈ (−1,1)` — in particular it covers genuinely traveling stripes
such as (3) with `c = 1/2`. ∎

**Remarks.**
- (i) The boundary case `k = 0` is excluded: at `k = 0`, (8) admits the
  neutral translation eigenvalue `λ = 0`, `V = φ` (and Jordan chain from
  Lorentz/speed-invariance), consistently with the computed spectrum
  (`max|Re λ|` at `k = 0` is the discretization of the known Jordan block
  and converges to `0` under refinement: 2.6e−3 → 1.3e−3 → 6.6e−4).
- (ii) The proof shows more: no `Re λ ≠ 0` eigenvalue exists at all for
  `k ≠ 0` — neither a long-wave band nor short-wave instability. The
  target's "stable for `|k| ≥ k_c`" half holds vacuously here, but the
  "unstable band `0 < |k| < k_c`" half fails completely.
- (iii) Librational stripes *are* typically unstable (already at `k = 0`
  via the negative direction of `L₀`); this is consistent with the theorem
  and shows the class in the target is genuinely mixed — no universal band
  statement can hold without excluding the rotational subclass, which the
  admitted claim does not.

## 4. Explicit counterexample stripe (genus one, traveling)

Take `c = 1/2`, so `γ² = 3/4`, `γ = √3/2`. The rotational wave

```
U(ξ) = π + 2 am(νξ | m),  m = 1/2,  ν = 1/(γ√m) = 2√2/√3 ≈ 1.63299,
U(0) = π,  U′(0) = 2ν ≈ 3.266 > 0,
```

solves (4) (standard `sn/dn` identities: with `U = π + 2am(z|m)`,
`U′ = 2ν dn(z|m)`, `U″ = −2ν²m sn(z|m)cn(z|m)·2/... = −sin(U)·(2ν²m)` and
`2ν²m = 1/γ²`). It is strictly increasing with

```
U(ξ + L) = U(ξ) + 2π,   L = 2K(m)γ√m ≈ 2.27077,
K(1/2) ≈ 1.85407   (AGM),
```

hence genus-one (one spectral gap pair open in the 1D Lax spectrum; a kink
lattice), subluminal, and inside the admitted genus ≤ 2, `|c| < 1` class.
`q(ξ) = cos(U(ξ))` is `L`-periodic, and `φ = U′ = 2ν dn(νξ|m)` is nodeless
(`dn ≥ √(1−m) > 0`), so Lemmas 1–2 apply verbatim.

## 5. Computed (k,λ) spectrum

Reproducible script: `output/artifacts/verify_stripe.py` (numpy only: RK4
integration of (4), second-order periodic finite differences, companion
linearization of the quadratic pencil, dense eigensolves).

- Period: RK4 gives `L_num ≈ 2.27077`, relative error `1.0e−4` vs the AGM
  prediction `2K(m)γ√m`; refined crossing `2.2707684522`.
- Nodelessness: `min U′ ≈ 2.309 > 0` over the period.
- Hill operator `L₀ = −γ²D₂ + diag(cos U)`: smallest periodic eigenvalue
  `≈ −4.5e−7` (≈ 0, the translation mode; `L₀U′` residual rms `≈ 1.2e−5`
  vs `|U′|` rms `≈ 2.79`), next eigenvalues `≈ 5.857 (×2), 23.06 (×2),
  51.77` — confirming `L₀ ≥ 0` with simple ground state `0`.
- Quadratic pencil `λ²V − 2cλV′ + (L₀ + k²)V = 0` (companion form,
  `N = 800` periodic grid), `max|Re λ|`:
  `k = 0.05, 0.1, 0.25, 0.5, 1.0, 2.0 → ≤ 5e−12` (roundoff level);
  antiperiodic fiber (`μ = π/L`): `k = 0.1, 0.5, 1.0 → ≤ 7e−12`.
  At `k = 0`: `6.6e−4`, converging to `0` linearly under refinement
  (`N = 200, 400, 800 → 2.6e−3, 1.3e−3, 6.6e−4`), the expected
  discretization of the `k = 0` Jordan block — not an instability.
- Refinement table and sampled eigenpair identity check:
  `output/artifacts/stripe_spectrum.json`,
  `output/artifacts/identity_check.json`
  (fiber residual `|S − 2cλJ + (λ²+k²)N|/(|S|+N) ≈ 2.5e−12` for the lowest
  mode at `k = 0.5`, `λ ≈ 0.495i`).

The computation therefore confirms the theorem: the `(k,λ)` spectrum of the
explicit stripe (3) is purely imaginary for all tested `k ≠ 0` across Bloch
fibers — transverse stability for all `k ≠ 0`, contradicting the claimed
universal band `0 < |k| < k_c`, `Re λ ≥ Λ(k) > 0`.

## 6. Scope and limitations

- The disproof targets exactly the *universal* reading of the admitted
  claim ("every stripe in the box has an unstable band"). It does not assert
  that *no* finite-gap SG stripe is transversely unstable — librational
  stripes carry a negative `L₀` direction and are unstable already at
  `k = 0`, with that instability typically persisting for small `k ≠ 0`.
- The analytic proof (§3) is self-contained and rigorous (Sturm–Liouville
  ground-state factorization + the skew-adjointness identity); it covers all
  rotational stripes at all `|c| < 1` and all Bloch fibers. The numerics (§5)
  are supporting evidence for the concrete stripe, with documented
  discretization behavior at `k = 0`.
- No external literature was needed; no `scope_literature_search` calls used.
- Finite-difference spectra are approximations; the *proof* of stability
  does not depend on them.

## 7. Conclusion

The stated transverse instability band — existence of `k_c > 0` and growth
curve `Λ(k) > 0` on `0 < |k| < k_c` for the finite-gap sine-Gordon stripes
in the admitted class — is **disproved as a universal claim** by the
explicit genus-one traveling kink-lattice stripe (3) at `c = 1/2`, which is
transversely spectrally stable (`Re λ = 0`) for every `k ≠ 0`. This is a
complete resolution of the admitted target on its disproof branch.
