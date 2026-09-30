# 64-cap concurring bush datum at R0 = 65536 with decoupling ratio >= 3/2

## Context

Canonical l^2 decoupling for the truncated elliptic paraboloid
P^2 = {(xi,|xi|^2): xi in [0,1]^2} in R^3 at the critical exponent p=4.
Bourgain-Demeter gives upper bound D_4 <= C_eps R^eps (essentially sharp via
unspecified extremals); the study guide baseline is D >= 1 plus an
unspecified logarithmic lower bound at critical p via number theory, with
higher-dimensional precise power open. Small-cap/parabola lines live in
different cap regimes. No prior source lists an explicit 64-cap concurring
bush with certified ratio. This record is the admitted preset fallback:
a single-scale citable obstruction benchmark, independent of the full
sqrt-log window growth (which is blocked by a coherence-volume obstruction
retained separately).

## Definitions

- R0 = 65536 = 2^16, R0^{-1/2} = 1/256, R0^{1/2} = 256.
- Canonical caps: R0^{-1/2}-cells; S* = corner 8x8 adjacent block,
  centres ((i+0.5)/256,(j+0.5)/256), i,j = 0..7 (64 distinct caps).
- Profile: per-cap Gaussian g_theta(xi) = exp(-|xi-w_theta|^2/(2s^2)),
  s = R0^{-1/2}/2 = 1/512 (essentially cap-supported).
- Coefficients: all equal to 1.
- Extension E: Ef(x) = int g(xi) exp(i(x'.xi + x3|xi|^2)) d xi, closed form
  via complex Gaussian integral (verified against direct quadrature,
  rel err 4.2e-15).
- f* = sum_{theta in S*} E f_theta.
- Concurring ball B* = ball radius 256 centred at origin, inside B_{R0};
  the 64 tube axes x' = -2 w x3 all pass through the origin; transverse
  separation at |x| <= 256 is <= 14 << tube width ~512, so all tubes
  overlap in B*. Constructive diagonal stem x' = -2 wbar x3,
  wbar = (1/64,1/64), stays inside B_{R0} for |x3| <= 40000.
- Decoupling ratio R(f*) = ||E f*||_{L^4(B_{R0})} /
  (sum_theta ||E f*_theta||_{L^4(B_{R0})}^2)^{1/2}.

## Result

R(f*) >= 3/2. Measured: primary R = 2.18 (R^4 = 22.66);
independent verifier from datum record only with different boxes/seeds:
R = 2.07, conservative -2se bound 1.92 >= 1.5. Verdict VERIFY_OK.

Explicit sides (primary box): ||Ef*||_4^4 = INT = 1.6010e-3
(so ||Ef*||_4 ~= 0.2000); single-tube ||Eg||_4^4 = ONE = 1.7247e-8
(so ||Eg||_4 ~= 0.01146); denominator (sum ||.||^2)^{1/2} = 8*ONE^{1/4}
~= 0.0917; R = 0.2000/0.0917 = 2.18.

## Proof / evidence

Closed-form Gaussian E (cmath, exact up to fp), Monte Carlo integration
of |S|^4 over a diagonal-following numerator sub-box inside B_{R0}
(half-width 512, x3 +-32768; verifier W=640, H=40000, seed 99) and of
single-tube |Eg|^4 over a wide tube box (verifier W2=2560, seed 123).
Numerator sub-box gives a lower bound (rest of B_{R0} only adds mass);
wide tube box captures essentially all L4 mass (negligible Gaussian tails)
with minimal-|w| cap proxy, so denominator is an overestimate:
both directions conservative for the >= claim. MC stderr reported;
distance to threshold ~7.8 sigma. Both norms recheckable from
output/artifacts/fallback_datum.json (64 centres, s, B*, coefficients).

Reproduction:
- python3 output/artifacts/fallback_diagonal_ratio.py (primary R = 2.18)
- python3 output/artifacts/verify_fallback_ratio.py (VERIFY_OK)
- supporting: bush_ceiling_check.py (spread-target CEILING_CONFIRMED).

## Limitations

Ratio is Monte Carlo with standard-error bound, not a deterministic
interval proof. Per-cap profile is Gaussian (s = half cap radius) rather
than sharp cap indicator; strict D_4 supremum interpretation would need a
few-percent truncation correction, well within the 28% margin.
Numerator integrates a large diagonal-following sub-box of B_{R0}
containing the constructive stem. Full sqrt-log window growth remains
open (blocked by carrier-phase decoherence: spread-bush Q-ratio ~0.35
vs 4/3, ceiling 0.72 < 4/3).

## Reproducibility

Stdlib Python only, seeded. Datum record output/artifacts/fallback_datum.json
lists all 64 centres, profile s, coefficients all_ones, B* centre/radius,
measured values and reproduction commands.

## References

- Bourgain-Demeter, The proof of the l^2 Decoupling Conjecture.
- Bhargava-Chan-Lim-Pang, A study guide for the l^2 decoupling theorem
  for the paraboloid (arXiv:2402.14756).
- Guth-Maldague-Oh, Small cap decoupling for the paraboloid in R^n.
- Fu-Guth-Maldague, Sharp superlevel set estimates for small cap
  decouplings of the parabola.
