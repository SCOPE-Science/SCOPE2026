# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Irreducible degree-4 edge residue at (0,1,2,3,4): the target is FALSE

## Claim (disproof of the admitted target)

The admitted target states that with torus weights `lambda*=(0,1,2,3,4)`,
every quintic-twisted smooth-domain degree-4 edge contribution

  `Eij = (1/4) * eT(H0(C, f*O(5))) / eT(Nvir_ij)`

is regular at `lambda*` and that the 20-term sum satisfies
`Sirred(lambda*) = 17281/384`.

This conjunction is **false**: the pairs `(0,4)` and `(4,0)` are singular
at `lambda*` (genuine double poles), so the stated regular value
`17281/384` cannot hold as written. The corrected local ledger below
diagnoses the miscounted factor and gives the exact leading singularity.

## Set-up (standard Graber-Pandharipande edge weights)

Degree `d=4` cover of the coordinate line through fixed points `pi, pj`
with weights `li, lj`. Numerator Euler weights of `H0(C, f*O(5))` (rank 21):

  `n_a = ((20-a)*li + a*lj)/4`, `a = 0, ..., 20`.

Denominator: the 23 moving weights of `H0(C, f*T P4)` after removing the
two fixed weights `(i,0)` and `(j,d)`:

  `D1: ((4-m)*li + m*lj)/4 - lk`, `k != i,j`, `m = 0..4` (15 forms);
  `D2: ((4-m)*li + m*lj)/4 - li`, `m = 1..4`, and the same with `lj`,
      `m = 0..3` (8 forms).

Nonzero overall factors `1/4` and the automorphism weight
`W = (li-lj)(lj-li)/16` cannot create or remove zeros. This is the audit
plan's prescribed weight ledger.

## Singularity census at lambda* = (0,1,2,3,4)

Pair `(0,4)` (`li=0, lj=4`): numerator weights are exactly `n_a = a`:

- numerator zeros: only `a=0` (weight `5*lam0 = 0`), one simple zero;
- denominator zeros: exactly three, `(k,m) = (1,1),(2,2),(3,3)`, since
  `((4-m)*0 + m*4)/4 - k = m - k` vanishes exactly at `m=k=1,2,3`.

Pair `(4,0)` (`li=4, lj=0`): numerator weights are `n_a = 20-a`:

- numerator zeros: only `a=20`, one simple zero;
- denominator zeros: exactly three, `(k,m) = (1,3),(2,2),(3,1)`.

In both cases 3 denominator zeros against 1 numerator zero: net double
pole. The three vanishing linear forms have independent differentials
(`df = ((4-k)/4) dlam_i + (k/4) dlam_j - dlam_k`), so no cancellation path
can absorb them; moving only `lam0` already exhibits the pole.

Robustness: the three vanishing forms `m-k` lie in the `k != i,j` block,
so they are present whether that block runs over `m=0..4` or the interior
`m=1..3`. The pole is not a normalization artifact.

## Exact leading coefficient

Along the transverse line `lam(t) = (t,1,2,3,4)`, pair `(0,4)`:

- `N(t) = prod_{a=0..20}(a + (5-a/4) t) = 5t * R_N(t)`,
  `R_N(0) = 20! = 2432902008176640000`;
- `W(t) = -(4-t)^2/16`, `W(0) = -1`;
- `D(t) = t^3 * (3/4)(2/4)(1/4) * C0 * (1+O(t))`, slopes product `3/32`,
  where the nonzero remainder is `C0 = 144 * 576 = 82944`
  (per-`k` products `(-6)(4)(-6) = 144`; tangential `D2 = 24*24 = 576`).

Hence, for `0 < |t| < 1/2` (no other factor vanishes there),

  `E04(t) = K/t^2 * (1 + O(t))`,
  `K = (1/4)(5 * 20!)(-1)/((3/32) * 82944) = -391091500800000`.

Direct rational evaluation confirms `E04(1/1000)/10^6` and
`E04(1/10000)/10^8` agree with `K` to within 5% (see `verify.py`).
The twin pair `(4,0)` has the identical `K` by the evident `i <-> j`
swap symmetry of the ledger. Consequently the 20-term sum diverges like
`2K/t^2 -> -infinity` along this approach, rather than equaling
`17281/384 ~= 45.0026` at the limit point.

## What this establishes

- The literal target conjunction ("each `Eij` regular at `lambda*`" and
  "their sum equals `17281/384`") is rigorously disproved under the
  standard edge-weight convention named in the audit plan.
- Corrected fragment: pole order 2 on `(0,4)` and `(4,0)` with exact `K`;
  only 8 of the 20 pairs are regular at `lambda*` (6 are `0/0`, 6 polar).
- Error diagnosis: the target counted one quintic-numerator zero against
  three virtual-normal-bundle zeros on the extremal edges; `17281/384`
  can at best be repaired as a residue/regularized value under a stated
  subtraction scheme, which the current claim does not provide.

## Replay

`python3 output/artifacts/verify.py` prints `VERIFY_OK` (stdlib only).
