# Sign-reversal (decay) audit of the endpoint-uniform Mikado ratio law

## Context

The admitted target was a parametric transport-dominance barrier blocking
uniform `sup_q ||v_q||_{L^infty_t B^{1/3}_{3,infty}} <= M` Mikado closure toward
any strictly decreasing energy profile, with engine a growth law
`||R_trans||_1/(||R_osc||_1+lam^{-1}) >= c1 lam^{(4al-3)/3}` for fixed steady
shear `v0=(sin x3,0,0)`, intermittent Mikado family with `r=lam^{-al}`,
`al in (3/4,1]`, dyadic `lam>=2^12`.
The admitted preset fallback was the same inequality as a standalone obstruction
lemma with binary ALL-pairs success criterion.
Both are blocked in the standard scaling-model class: the ratio decays.

## Definitions

- Background: `v0(x)=(sin x3,0,0)` on `T^3`, steady Euler shear,
  `||grad v0||_inf=1`, hence `c1=10^{-2}||grad v0||_inf=0.01`.
- Tube: `W(x)=r^{-1} psi(x_perp/r) e^{i lam x3} e3`, Gaussian
  `psi(s)=exp(-|s|^2)`, `L^2`-normalized `psi_n=psi/||psi||_2`.
  Periodization error on `T^3` is `~exp(-(pi/r)^2)`, negligible for `r<<1`.
- Inverse divergence `R`: scalar order-`(-1)` Fourier-multiplier model
  `m(xi)=i xi/|xi|^2` (same frequency gain as symmetric Euler-Reynolds `R`).
- Transport source: `g=(v0.grad)W = sin(x3) d_1 W`.
- Oscillation: axial-oscillation model `||R_osc||_1=C_osc a^2`, `C_osc=2.0`;
  `C_osc=0` (pure-transverse, denominator `=lam^{-1}` floor) also audited.
- Fallback amplitude: `a^2=c_cap lam^{-2/3} r^{4/3}` (`M*=1`), nominal
  `c_cap=1`; robustness `c_cap in {0.1,1,10}`.
- Window: `al in {0.751,0.8,0.9,1.0}`, dyadic `lam=2^k`, `k=12..24` (52 pairs).

## Result (emergent finding)

For the objects above with the fallback's own cap-saturating amplitude:

1. `||(v0.grad)W||_1 = S = (2/pi)||d_1 psi_n||_1 = 1.800430 > 0`,
   `(lam,r)`-independent; `||W||_p=r^{2/p-1}C_p` with `C_2=1`,
   `C_1=2.506628`, `C_3=0.810245`, `||d_1 psi_n||_1=D_1=2.828109`.
2. `||R g||_1/||g||_1` gain is `(0.84--0.96)/lam` (FFT-verified, stable over
   `lam=16..256`, `al in {0.9,1.0}`); no hidden frequency enhancement.
3. The cap-saturating ratio obeys the decaying envelope
   `~lam^{-(1+2al)/3}` and violates the claimed lower bound
   `c1 lam^{(4al-3)/3}` at **all 52 audited (lam,al) pairs**
   (worst `ratio/bound=4.19e-08` at `al=1,k=24`), including the `R_osc=0`
   floor-only case. With the Besov-proxy amplitude the axial-oscillation ratio
   scales as `lam^{(al-2)/3}` (exponent in `[-0.42,-0.33]`), likewise decaying.

Floor-dominance mechanism: `||R_osc||_1/lam^{-1}=C_osc c_cap lam^{(1-4al)/3}`
with `(1-4al)/3 in [-1.0,-0.668]<0` on the window, so
`ratio ~= a S = S sqrt(c_cap) lam^{-(1+2al)/3}` with exponent in
`[-1.0,-0.83]<0`, opposite in sign to claimed `+(4al-3)/3 in (0,+1/3]`.

## Proof / evidence

- Analytic (Lemma 1): transverse `L^1` scaling `r^{-2} r^2` cancels; axial
  `|sin|` averages to `2/pi`. Constants by trapezoid rule (`N=801,L=6`),
  cross-checked to 6 digits across two scripts.
- Gain (computed): scalar order-`(-1)` antidivergence applied to `g` on
  resolved transverse/axial grid; `||Rg||_1/||g||_1 * lam = 0.84--0.96`.
- Falsification (computed): sweep 52 pairs at nominal constants gives 52/52
  violations; sample `lam=4096,al=1`: `a=2.441e-04`,
  `R_trans=1.073e-07`, `R_osc=1.192e-07`, floor `2.441e-04`,
  ratio `4.393e-04` vs bound `1.600e-01`. Robustness grid
  (`C_osc in {0,2}`, `c_cap in {0.1,1,10}`, 100x numerator inflation):
  52/52 fail nominal; 38--47/52 fail even at 100x inflation; gap widens
  monotonically in `lam` at every `al`, so no constant or sub-window repair.
- Exponent algebra `e(al)=(4al-3)/3>0` holds (`0.0013..0.3333`); failure is
  via the inequality branch, matching the binary FAIL condition exactly.

## Limitations

- Falsification lives in the standard scaling-model class above (Gaussian
  tube, order-`(-1)` multiplier model of `R`, stated oscillation models).
  Not a theorem about the exact tensor inverse-divergence `R` or all Mikado
  variants (e.g. temporal correctors, non-standard phase design).
- Gain FFT-verified to two digits over `lam=16..256`, extrapolated by scale
  invariance to the audit window.
- Sec. 2 identities are analytic; gain and sweep are machine-checked numerical
  evidence with logged replay.
- Consequence: any endpoint-uniform Mikado growth route must invoke mechanisms
  outside this standard class; the `lam^{(4al-3)/3}` law cannot be used as
  stated.

## Reproducibility

- `python3 output/artifacts/verify_emergent.py` -> `VERIFY_OK`
  (52/52 violations + sign table)
- `python3 output/artifacts/fallback_audit.py` (robustness grid)
- `python3 output/artifacts/fft_verify.py` (gain table)
- `python3 output/artifacts/scaling_check.py` (analytic constants + ratio table)

## References

- Buckmaster-De Lellis-Szekelyhidi-Vicol, Onsager's conjecture for admissible
  weak solutions, arXiv:1701.08678 (any `beta<1/3`, any smooth `e`; no
  endpoint cap, no ratio bound).
- Buckmaster-Vicol, Convex integration and phenomenologies in turbulence,
  arXiv:1901.09023 (survey; Reynolds Nash/transport/oscillation UPPER splits).
- Isett, Nonuniqueness and existence of continuous, globally dissipative Euler
  flows, arXiv:1710.11186 (subcritical dissipative non-uniqueness).
- Giri-Kwon-Novack, The L^3-based strong Onsager theorem,
  Annals 204(1):265-421 (every `beta<1/3`; isolates `beta=1/3` as open face).
- Cheskidov-Constantin-Friedlander-Shvydkoy, Energy conservation and Onsager's
  conjecture, arXiv:0704.0759 (`B^{1/3}_{3,c(N)}` little-o conservation, not a
  building-block ratio bound).
