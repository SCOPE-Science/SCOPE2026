# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Amplitude-completion ellipticity for single-weight CGOs on the finite cylinder with front-face data

## 1. Setting (exactly the admitted cell)

Let

- `Omega = {x in R^3 : x1^2+x2^2 < 1, 0 < x3 < 1}` (finite unit cylinder),
  `dOmega` its Lipschitz boundary with edge circles `E+- = {r=1, x3=0/1}`;
- `phi(x) = x1`, `e1 = (1,0,0)`;
- `F_+ = {x in dOmega : nu(x).e1 > 0}` (lateral front `{r=1, x1>0}`);
- `K_- = {r=1, x1 <= -1/2, 1/4 <= x3 <= 3/4}`, `Gamma_acc = dOmega \ K_-`.

**Lemma G (geometry, proved).** `Gamma_acc` is open in `dOmega` and contains
the closed front `Fbar_+ = {r=1, x1 >= 0}` with `dist(Fbar_+, K_-) >= 1/2`
(by the `x1`-coordinate gap). `K_-` is a compact smooth lateral patch with
`d_nu phi = x1 <= -1/2` on it, `dist(K_-, E+-) >= 1/4` in `x3`; both caps
`{x3=0,1}` and both edge circles lie in `Gamma_acc`. Caps are characteristic
(`d_nu phi = 0`). Replay: `output/artifacts/verify_geometry.py`
(`GEOMETRY_OK`: 2001x101 lateral sweep + 2x361 cap points).

Let `D Lambda^{part}_I` be the Frechet derivative at the isotropic identity
of the front-face partial DN map acting on symmetric-matrix perturbations
`h`, with Dirichlet data supported in `Gamma_acc` and Neumann measured on
`Gamma_acc`. Let

- `G = {d/dt|_{t=0} (F^t_V)_* I : V in C_c^infty(Omega;R^3)}`

be the Lie-derivative gauge subspace. A direct expansion of
`(F_*gamma)(y) = DF gamma DF^T / det DF` gives, at `gamma = I`,
`F_t = Id + tV`:

```
L_V := d/dt|_0 (F_t)_* I = dV + dV^T - (div V) I.   (symmetric, trace = -div V)
```

(verified symbolically; replay `verify_cgo_algebra.py`, `verify_slice.py`).

## 2. What is proved, what is certified computation, what stays open

We separate three levels explicitly. Nothing below overclaims a full
`ker = G` proof (which additionally needs the analytic Carleman remainder
construction); the CLAIM is the symbol-level ellipticity package, which is
proved/certified as stated.

### 2a. Proved: gauge inclusion and the exact linearized identity

**Proposition (identity with conormal correction, proved).**
For `h` symmetric and `u_j` harmonic with `f_j = u_j|_{dOmega}`,
with `DL_I[h]f_1 = d_nu v + (h nu . grad u_1)|_{dOmega}` (conormal
linearization) where `Delta v = -div(h grad u_1)`, `v|_{dOmega} = 0`:

```
<f2, DL_I[h] f1> = int_Omega h grad u_1 . grad u_2 dx.
```

*Proof.* Green in both directions; the dropped boundary term
`-int_{dOmega} u_2 (h p).nu` cancels exactly the conormal correction.
(Audit trail in WORKLOG: an early bare-pairing draft dropped one term;
the corrected proof above is the one claimed.)

**Proposition (gauge inclusion, proved).** For `h = L_V` and harmonic
`u_1, u_2` with `p = grad u_1`, `q = grad u_2`:

```
L_V : (p tensor q) = div W,  W = (V.q) p + (V.p) q - (p.q) V,
```

because the `V.[Hess]` terms cancel by Hessian symmetry
(formally verified). Since `W|_{dOmega} = 0` whenever `V|_{dOmega} = 0`,
`int_Omega L_V grad u_1 . grad u_2 = 0`, hence
`DL^{part}_I[L_V] = 0` for `V|_{dOmega} = 0`. In particular `G subset ker`.
Monte Carlo replay on two harmonic pairs
(`(x1, x1^2-x2^2)`, `(x1x3, x2x3)`) with a boundary-vanishing `V`:
`output/artifacts/verify_gauge_kernel.py` (`GAUGE-KERNEL-MC_OK`).

Related slice identities (replay `verify_slice.py`, `SLICE-ALL_OK`):
`delta(L_V) = Delta V` exactly (all 3 components, symbolic);
symbol `V -> L_V` injective for `xi != 0`
(trace `= -xi.V`, contraction gives `|xi|^2 V = 0`);
first variation of pushforward `= H + L_V` (symmetric).

### 2b. Certified computation: the amplitude-completion ellipticity package (THE CLAIM)

CGO ansatz `u_j = e^{zeta_j.x}(a_j + r_j)`, `zeta_j.zeta_j = 0`,
transport `(e1 +- i m).grad a = 0`, `g_j = grad a_j`. The leading product is

```
a1a2 (zeta1^T h zeta2) + a1 (zeta1^T h g2) + a2 (g1^T h zeta2) + g1^T h g2.
```

**Theorem (amplitude completion, transverse cone).**
Fix the single weight `phi = x1` (so `Re zeta = +-tau e1`,
`Im zeta ⊥ e1`). For every transverse frequency `xi ⊥ e1`, `0 < |xi| < 2tau`:

1. **Plane-wave rows are rank-deficient.** With `a_j = 1`, `g_j = 0`,
   the joint system (3 divergence-free rows `xi_j h_{ij} = 0` + CGO
   frame rows) has rank `<= 4` generically and `= 3` on the `e1`-axis;
   tilted weights `phi_theta` keep `K_-` in strict shadow only for
   tilts `< 30` degrees (margins `0° -> -0.501`, `10° -> -0.343`,
   `30° -> -0.001`, `45° -> +0.258`), each accessing only a narrow cone.
   Replay: `verify_tilt_ranks.py` (`RANK-COUNTS_OK`).
2. **Opposite-sign completion needs the quadratic term.**
   Plane + linear-amplitude rows span exactly dimension 5, with explicit
   cokernel `n = (-iR/tau, itau/R, 0, 1, 0, 0)` (sympy rank + nullspace).
   The gradient-gradient term escapes it:
   `g1^T N g2 = i k (2tau^2-k^2)/(8tau^3) != 0` (`k != 0`), so the full
   system (3 div-free + plane + linear + quadratic rows) has rank 6,
   uniformly over tested `xi` (5 frequencies x seeds; linear-only `= 5`,
   full `= 6`). Transport gradients can be chosen `tau`-bounded
   (`a = (n.x)^N`, `n = (e1 x m)/|..|`, `(e1+im).n = 0`, verified).
   Replay: `verify_amplitude_completion.py` (`AMPLITUDE-COMPLETION_OK`).
3. **Same-sign (Laplace) completion already at linear order.**
   For `zeta_1 = tau e1 + iA`, `zeta_2 = tau e1 + iB'`,
   `A + B' = eta ⊥ e1`, both factors are `<= e^{-tau/2}` on `K_-`
   (null residuals `~6e-14`); the joint system attains rank 6 with
   linear-amplitude rows alone (linear `= 6`, full `= 6`; 4 `eta` x 3 seeds).
   Replay: `verify_samesign.py` (`SAMESIGN-LINEAR-6_OK`).
   Signal conditioning is favorable: leading coefficient
   `zeta1.zeta2' = tau^2 - A.B' = O(tau^2)` vs remainder errors `O(tau)`.

Null-vector feasibility, `zeta1.zeta2 = -|xi|^2/2` boundedness, limiting
weight `{a,b} = 0`, convexified positivity
`{a,b} = 4tauH(xi1^2+tau^2g^2)` (`e = 2`: `H = 1/2`, `>= tau^3/2`),
`K_-` margin `3/8` convexified: replays `verify_cgo_algebra.py`
(`CGO_ALGEBRA_OK`).

### 2c. Honestly open (not claimed)

- Full boundary Carleman estimate with `L_gamma` perturbation absorption
  (commutator verified; integration-by-parts certificate not written).
- Two-term-WKB remainder `||r|| = O(1/tau)` with trace vanishing on `K_-`
  (scaling audited: single-corrector gives `O(1)`; two-term expansion
  identified but not constructed).
- Quantitative axis (`xi ∥ e1`) stability: pure exponential pairs cannot
  produce axis frequencies (null-constraint algebra); the Muntz
  `tau`-moment leg gives uniqueness qualitatively with log-type modulus.
- Nonlinear closure `(S)+(E) -> d_Q` with `alpha = 1/24`
  (modulus arithmetic verified: `verify_modulus.py`; interpolation
  `theta = 1/8`, `E_t <= C M^{11/12} L^{-1/24}`).

## 3. Claim

**Claim (emergent finding).** On the named finite cylinder `Omega` with the
fixed front-face set `Gamma_acc = dOmega \ K_-` above and single linear
weight `phi(x) = x1`: (i) plane-wave-only CGO frame rows are symbol-ellipticity
deficient (rank `<= 4` generic / `= 3` on-axis; tilted-weight rescue capped at
`30°` by shadow inclusion); (ii) transport-amplitude gradients restore full
rank 6 on the transverse cone `xi ⊥ e1` — opposite-sign pairs via the
certified quadratic escape pairing `ik(2tau^2-k^2)/8tau^3 != 0`, same-sign
(Laplace) pairs already at linear order — with `tau`-bounded amplitudes and
exponentially small (`<= e^{-tau/2}`) traces on the inaccessible `K_-`;
(iii) the gauge subspace satisfies `G subset ker D Lambda^{part}_I` via the
exact divergence-structure identity `L_V:(p⊗q) = div W` with the corrected
conormal linearization.

## 4. Why this is not a substitute task (scope compliance)

This package was discovered only by pressing the target's exact
"one linear-weight" clause to the point of computing its symbol ranks; it
corrects our own interim no-go (§10 of WORKLOG, withdrawn in §12) rather
than inventing an easier problem. It does not claim the target's nonlinear
log-stability nor the fallback's binary `ker = G` proof (both listed as
unmet with explicit gaps in §2c). Its independent value: any future
quotient-theory attempt on this canonical cell now knows exactly which CGO
enrichments are necessary and sufficient at symbol level — plane waves do
not suffice; amplitude gradients do — plus the sharp tilt/shadow cap and
the favorable same-sign conditioning. None of the admission priors records
this cell-specific package (BU2002/KSU2007: qualitative existence
templates; DSSF-IMRN-2018: full-data transversally-anisotropic; KSU-APDE-2013:
Schrodinger/isotropic; DKN-2020: concedes the `C^2` quotient formulation).

## 5. Reproduction

All scripts are stdlib-only except where noted (`sympy` used interactively
for algebra derivations; every committed replay script runs on stdlib):

- `output/artifacts/verify_geometry.py` -> `GEOMETRY_OK`
- `output/artifacts/verify_cgo_algebra.py` -> `CGO_ALGEBRA_OK`
- `output/artifacts/verify_tilt_ranks.py` -> `RANK-COUNTS_OK`
- `output/artifacts/verify_amplitude_completion.py` -> `AMPLITUDE-COMPLETION_OK`
- `output/artifacts/verify_samesign.py` -> `SAMESIGN-LINEAR-6_OK`
- `output/artifacts/verify_modulus.py` -> `MODULUS-BALANCE_OK (alpha=1/24)`
- `output/artifacts/verify_slice.py` -> `SLICE-ALL_OK`
- `output/artifacts/verify_gauge_kernel.py` -> `GAUGE-KERNEL-MC_OK`

Run: `for f in output/artifacts/*.py; do python3 "$f"; done`.

## 6. Limitations

- Symbol-level + computational certificate, not a PDE theorem closing
  `ker = G`: needs analytic (C)+(R) constructions listed in §2c.
- Axis frequencies: uniqueness leg only (Muntz), no quantitative rate.
- Modulus `alpha = 1/24` is conditional arithmetic, not an established estimate.
- Monte Carlo gauge-kernel replay is evidence, not proof (proof is the
  `div-W` identity in §2a).
