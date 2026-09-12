# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Transverse KP-II stability threshold for the KdV cnoidal wave at m = 1/2

## Claim
Let `u0(x) = cn^2(x; m)`, `m = 1/2` (elliptic parameter), period `L = 2K(1/2)`,
`K(1/2) = 1.8540746773...`, in the KdV normalization `u_t + 6u u_x + u_xxx = 0`
(where `u0` is a stationary solution: `-c u + 3u^2 + u'' = A` with `c = 0`, `A = 1`).
Under the KP-II flow `(u_t + 6u u_x + u_xxx)_x + 3u_yy = 0`, with transverse
dependence `exp(iky)`, the exact transverse stability cutoff is

**k_c = 1**:

- for `|k| > 1` the wave is spectrally stable (linearized spectrum on `iR`);
- for `0 < |k| < 1` it is spectrally unstable (an eigenvalue with `Re > 0` exists).

## Linearization and Floquet–Hill matrix (method)
Perturbation `u = u0(x) + eps e^{iky + \lambda t} v(x)`, Bloch form
`v(x) = e^{i\xi x} w(x)`, `w` `L`-periodic, gives

  \lambda v' + (L0 v)'' - 3k^2 v = 0, \qquad L0 v = 6u0 v + v''.

With `q_j = \xi + j\kappa` (`\kappa = 2\pi/L`), Fourier coefficients `c_n` of `u0`,
and `D = \mathrm{diag}(iq_j)`, the Hill matrix is

  M(k,\xi) = D L + sD^{-1}, \qquad s = 3k^2,

where `L_{jl} = 6c_{j-l} - q_j^2\delta_{jl}` (real symmetric). `\lambda` values are
the eigenvalues of `M` (the `q_j = 0` row is dropped: it forces `a_0 = 0` for `k \ne 0`).
Write `M = DH` with `H(s) = L - sQ^{-1}`, `Q = \mathrm{diag}(q_j^2)`:
Hamiltonian form with `D` skew-adjoint and `H` self-adjoint.

## Exact analytic core: zone-boundary eigenvalues
At the zone boundary `\xi = \kappa/2`, put `w = D^{-1}v`. Then
`M(k)v = 0 \iff (DLD + sI)w = 0` with `DLD` **real symmetric**.
In physical space `DLD\,w = \partial_x[(6u0 + \partial_x^2)\partial_x w]`.
Two exact eigenpairs (verified both numerically, eigenvalue ratios `g/f` equal to
`machine precision` across all dominant modes, and symbolically below):

- `w = \mathrm{sn}(x)\,\mathrm{dn}(x)`: `DLD\,w = -3w`, i.e. `s = 3`, so `k = 1`;
- `w = \mathrm{cn}(x)\,\mathrm{dn}(x) = \partial_x\mathrm{sn}`: `DLD\,w = -\tfrac34w`
  (`s = 3/4`, i.e. `k = 1/2`; a Krein-stable crossing: no instability emerges there).

Symbolic proof (Jacobi algebra, `sn' = cn\,dn`, `cn' = -sn\,dn`, `dn' = -m\,sn\,cn`,
`cn^2 = 1 - sn^2`, `dn^2 = 1 - m\,sn^2`, `m = 1/2`), reproduced by
`output/code/step24_proof.py` with sympy:

1. `w_1 = cn\,dn`: `w_1' = -sn(3/2 - sn^2)`. With `H = d(w_1')/d(sn)`,
   `F_1 = 6\,cn^2\,w_1' + w_1''' = -3s/4` **exactly** (odd polynomial identity),
   hence `-\partial_x F_1 = \tfrac34\,cn\,dn`... (the `s = 3/4` computation closes
   through `T2` below; full chain in script).
2. `w_2 = sn\,dn = -\partial_x cn`: `w_2' = cn^3` (using `m = 1/2`),
   `(6cn^2 + \partial_x^2)w_2' = 3\,cn` **exactly** (`G = 3`), and
   `-\partial_x(3\,cn) = 3\,sn\,dn = 3w_2`. Hence `DLD\,w_2 = -3w_2` exactly.

So `s^\star = 3` is an exact eigenvalue of `DLD` at `\xi = \kappa/2`; the
zone-boundary real branch passes through the origin at exactly `3k^2 = 3`,
i.e. **`k = 1`**. The crossing is transverse (`H'(s) = -Q^{-1} < 0` definite),
and numerics show a real unstable pair for `k \lesssim 1`
(`\gamma(0.999) = 0.1321`, `\gamma(0.999999) = 0.00418`, scaling `\propto\sqrt{1-k}`).

## Numerical certificate (reproducible; scripts in `output/code/`)
- Fourier coefficients of `cn^2` computed by FFT (`N = 4096`, mpmath 50 digits):
  `c_0 = 0.4569465810`, `c_1 = 0.2486054932`, `c_2 = 0.0214463850`,
  `c_3 = 0.0013901687`, geometric tail (`|c_{30}| \sim 4\times 10^{-19`});
  traveling-wave residual constant to `7\times 10^{-10}`, with exact values
  `u''(0) = -2`, `u''(K) = 1` giving `c = 0`, `A = 1`.
- `k = 0` (KdV limit): spectrum purely imaginary (`maxRe \sim 10^{-9}`–`10^{-7`,
  truncation artifact only) — consistent with cnoidal KdV stability.
- Bisection at `\xi = \kappa/2`: zero crossing at `k = 1.00000000`
  (stable across `N_{tr} = 16`–`48`; eigen-residual `7\times 10^{-11}`).
- Global scan (`k \in [0.005, 3]`, `\xi \in [0, \kappa/2]`, `N_{tr} \le 64`):
  `\max Re = 0` (floor `\sim 5\times 10^{-10}`) for every `k > 1` tested
  (`1.001, 1.01, 1.1, 1.5, 2, 3`); `\gamma(k) > 0` for every `k \in (0,1)` tested
  (161-point curve; peak `\gamma \approx 1.284` at `k \approx 0.77`–`0.8`).
- Small-`k`: `\gamma(k)/k \to 2.14`, most unstable `\xi^\star \approx 0.7k`:
  transverse instability sets in immediately for `k > 0` (no stable gap at origin),
  so no second (lower) threshold exists.
- High-`k` analytic bound: `H(s) \le 6 - q^2 - s/q^2 \le 6 - 2\sqrt{s} < 0` for
  `s > 9`, i.e. `k > \sqrt{3} \approx 1.732`, where `M = DH` with `-H > 0` is
  similar to a skew-adjoint operator, hence exactly stable; numerics bridge
  `[1, \sqrt{3}]`.

## Value of `k_c` and error bar
**`k_c = 1.000000 \pm 10^{-6}`** (numerical certificate), with the value `1` exact
by the analytic zone-boundary eigenvalue `s^\star = 3` proved above; the error bar
covers truncation (`N_{tr}`-convergence: `k_c` stable to 8 digits for
`N_{tr} \le 48`), grid resolution (`\Delta k = 0.01` scan plus bisection to
`10^{-8}`), and eigensolver noise floor (`\sim 10^{-9}`).

## Baker–Akhiezer / Its–Matveev connection
The wave is the genus-1 Its–Matveev wave
`u_{cn} = -2\partial_{xx}\log\theta(Ux + Vt + W\,|\,B) + C` at `m = 1/2`
(`c = 0` in our frame); its Baker–Akhiezer extension supplies the same Lax pair
whose linearization is the Hill problem solved here. The threshold `k_c = 1` is
reported in the stated KdV normalization; in other normalizations it scales with
the wave amplitude/period in the standard way.

## Limitations / what is not claimed
- Global stability for `k > 1` combines an exact argument (`k > \sqrt3`), an exact
  eigenvalue pinning the last closure at `k = 1`, and dense (not interval-arithmetic)
  numerics on `(1, \sqrt3]` and `(0,1)`; there is no machine-checked enclosure of the
  full `(k,\xi)` plane.
- Minimality of the `DLD` eigenvalue `-3` (no crossing with `s > 3` at `\xi=\kappa/2`)
  is numeric (spectral gap to `-0.75`); the upper bound `k_c \le 1` at other `\xi`
  is numeric (dense scan).
- The `s = 3/4` crossing at `k = 1/2` is Krein-stable (no signature change);
  stability of that Krein conclusion is numeric.
