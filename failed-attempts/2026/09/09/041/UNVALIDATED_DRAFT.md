# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified Khovanov–Lee profile data for the knot 10_124 (single-knot partial theorem)

## Statement (partial; collapse page explicitly NOT claimed)

Let D be the committed 10-crossing planar diagram of 10_124 with PD code

`X4251 X8493 X9,17,10,16 X5,15,6,14 X15,7,16,6 X11,19,12,18 X13,1,14,20
X17,11,18,10 X19,13,20,12 X2837`

(KnotAtlas PD, committed in `output/artifacts/pd_codes.json`), oriented with all
crossings positive (writhe +10; trefoil-calibrated orientation rule, repaying the
KnotAtlas Jones polynomial `-q^10+q^6+q^4` exactly and the Euler identity
`chi(Kh) = (q+q^-1)V(q^2)` exactly). Then, for the Khovanov complex built from
scratch over Z with the standard Frobenius maps (merge `++/+-/-+→+/−/−`,
`−−→0`; split `+→+−/−+`, `−→−−`) and the Lee deformation
`Phi` (merge `−−→+`, split `−→++`, zero otherwise):

1. **Rational Khovanov homology (bigraded).** `dim_Q Kh^{h,q}` is 1 exactly at
   `(0,7),(0,9),(2,11),(3,15),(4,13),(4,15),(5,17),(5,19),(6,17),(7,21)` and 0
   elsewhere (total 10). The blocks at `(0,9),(1,9)` are SNF-exact
   (`d(0,9)` rank 2, `d(1,9)` rank 8, all unit invariant factors); all 60 block
   ranks agree mod two distinct large primes (1000000007, 998244353);
   `d^2=0` holds on all 20155 column compositions; the graded Euler
   characteristic equals the KnotAtlas Kh-table chi column in all 8 rows.
2. **Integral 2-torsion (certified).** `SNF(d(2,13))` (384x93) has rank 84 with
   sole non-unit invariant factor 2; `SNF(d(6,19))` (1071x822) has rank 561 with
   sole non-unit invariant factor 2 (sympy exact). UCT comparison
   (`dim_F2` vs `dim_Q`) shows excess exactly at `(2,13),(3,13)` and
   `(6,19),(7,19)` with clean neighbors, pinning the 2-primary torsion hosts at
   `(h,q)=(2,13)` and `(6,19)` (odd torsion not excluded).
3. **Lee data (computed).** `d_Lee=d+Phi` satisfies `d Phi+Phi d=0` on all
   122866 composed entries (global, mod 1e9+7); ungraded Lee homology has
   dimension 2 (per-height Lee ranks
   `6,34,200,712,1688,2632,2720,1792,704,128`, nullity 2, identical mod two
   primes). The Phi-induced E2 maps on the four bigrading-compatible pairs have
   ranks `(2,11)->(3,15):1`, `(4,13)->(5,17):1`, `(4,15)->(5,19):0`,
   `(6,17)->(7,21):1` (quotient-correct representatives; the zero is exact over
   Z, `Phi_int=0` on the integral generator, with `H(4,15)=H(5,19)=Z` proved by
   all-ones SNF of the four adjacent differentials).
4. **Explicit open tension (no collapse claim).** Items 1–3 force the E3 page to
   be 4-dimensional at `(0,7),(0,9),(4,15),(5,19)` with no further nonzero
   bigrading-compatible higher differential, contradicting Lee dimension 2.
   Hence at least one of the computed inputs deviates from the standard theory
   in a way invisible to every check applied (`d^2=0`, Euler/chi, trefoil E2
   control, global `dPhi+Phid=0`, SNF spot-checks, two-prime agreement). The
   exact collapse page and E-infinity bigradings are therefore NOT claimed;
   all logs are archived for audit.

## Why this is new (gap)

KnotAtlas tabulates for 10_124 the Khovanov/Star tables only as ungraded or
chi-level data plus `s`/signature/Jones inputs; it records no Lee E2
differential ranks, no integral SNF torsion locations per bidegree, and no
replayable Lee-nullity certificate. The SNF-certified Z2 hosts, the exact
E2-differential ranks, and the machine-checkable `d_Lee^2=0` + Lee-nullity-2
logs are new exact data for this knot. The `s`/signature/Jones values used as
inputs are external data, not findings.

## Replay

- `python3 output/artifacts/kh_stepA.py` — circle-count distributions (all 8 PDs).
- `python3 output/artifacts/kh_stepB.py 10_124` — Jones bracket fit (zero-tolerant).
- `python3 output/artifacts/kh_stepD.py 10_124` — chain dimensions.
- `python3 output/artifacts/kh_stepE.py` — edge census (1136 merge/3984 split).
- `python3 output/artifacts/kh_stepF.py` — q-blocks.
- `python3 output/artifacts/kh_stepG.py <p>` — differential ranks mod p
  (saved `kh_ranks_1000000007.json`, `kh_ranks_998244353.json`,
  `kh_ranks_mod2.json`).
- `python3 output/artifacts/kh_stepJ.py` — Lee ranks (`lee_ranks_10_124.json`).
- SNF certificates: rebuild integer blocks from `d213_int.pkl`/`d619_int.pkl`
  (and rerun `smith_normal_form` as in WORKLOG substeps 14/20) for the 2-torsion
  and the `(0,9),(1,9),(4,19),(5,19),(3,15),(4,15)` exact ranks.
- Trefoil control PD `X1425 X3641 X5263` validates orientation signs and the
  Phi-induced E2 rank-1 computation end to end (see WORKLOG substeps 4/17).

## Limitations (explicit)

- (a) Only 10_124 of the 8-knot window is carried past Jones level (10_128 also
  Jones-matched; the other six PDs need per-crossing phase resolution).
- (b) Kh block ranks outside the SNF-checked blocks rest on two-prime
  agreement, not exact arithmetic; odd integral torsion outside the two SNF
  blocks is not excluded.
- (c) The E2 ranks rest on mod-prime quotient computations (one exact over Z:
  the `(4,15)->(5,19)` zero).
- (d) The collapse page / E-infinity bigradings / torsion-to-collapse lemma are
  NOT established (open tension documented above); no statement is made about
  the remaining seven knots' Lee pages.
