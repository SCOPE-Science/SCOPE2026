# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified 71-point genus-4 double covers of the Serre-optimal elliptic curve over F_32 and elimination of the vertical-univariate subfamily for N_32(4)=72

## Abstract
We give a Magma-independent, license-free verification of the three
71-point genus-4 Artin–Schreier double covers recorded on
manYPoints `q=32,g=4` (Howe comment 2010-04-16), with substitution-checkable
68-point affine lists, exact pole/infinity accounting, and genus 4 via
Riemann–Hurwitz (conductor 6).  We prove the entire vertical-univariate
subfamily `D=x+b, N=a x^2+b_1 x+c` (1,048,576 models) contains no
72-point smooth genus-4 curve, by parity plus known `(32,3)=64` and
Hasse–Weil.  Time-boxed sampling of 600k general/genus-4-eligible models
found no 72-point genus-4 model; the only `UB>=72` candidates are proved
genus 5/6.  The interval `N_32(4) in {71,72}` is **not** closed here and the
residual real Weil polynomial `(x+11)^2(x^2+17x+71)` is **not** eliminated.
Verifier reruns `artifacts/verify_three.py` in <2s (stdlib only).

## 1. Primary source snapshot
manYPoints Details `q=32,g=4` fetched direct 2026-09-07 (proxy fails TLS;
`--noproxy "*"`, 14129 B, `artifacts/manypoints_q32_g4_snapshot.html`):
`Nmin=71` (Zieve 1999), `Nmax=72` (Howe–Lauter).  `E: y^2+x y=x^3+x`,
`r^5+r^2+1=0`.  Three covers (notation `x2=x^2`):
1. `(r27 x2+r13 x y+r14 x+r25)/(x+r30 y+r27)`, RWP `(x+7)(x+9)(x+11)^2`;
2. `(r26 x2+r29 x y+r16 x+r18)/(x+r28 y+r4)`, RWP `(x+11)(x^3+27x^2+239x+691)`;
3. `(r14 x2+r24 x+r18)/(x+r)`, RWP `(x+9)^3(x+11)`.
Upper comment: `>72` must be a double cover of `E` (IsogenyClasses.magma);
`32-4.magma` enumerates double covers, none `>71`; if 72 exists its RWP must be
`(x+11)^2(x^2+17x+71)`.  We did not access Magma scripts; the upper bound 72
is taken as reported.

## 2. Field, curve, method (proof)
`F32=F2[r]/(r^5+r^2+1)`, ints `0..31`, `r=2`, add XOR, mul mod `0b100101`.
`Tr(a)=sum_{i<5} a^{2^i}` in `{0,1}`; `z^2+z=f` has 2 solutions iff `Tr(f)=0`.
Brute force 1024 pairs: `E` affine 43 + infty =44, trace `-11`, Serre-optimal
(`|t|<=2 sqrt(32)=11.31`).  `x`-fibres: 21 x with 2 pts, `x=0` double `(0,0)`
1 pt, 10 x empty.

Lemmas (char-2 degree-2, Stichtenoth III.7.10 special): for `P in E(F32)`,
if `v_P(f)>=0` then 0/2 lifts by `Tr(f(P))`; if `v_P(f)<0` odd then totally
ramified, exactly 1 rational point above rational `P`; if even `<0` subtract
local `g^2+g`, `g=s t^{v/2}`, to reduce to prior cases.  Number above infty
max 2, above affine pole max 1, above regular max 2.  Hence
`UB=aff+kp*1+kb*2+2` is a rigorous upper bound (kb=both-zero removable).
If `f=g^2+g` globally (all poles even) the cover is reducible/geometrically
reducible; odd poles imply irreducible.  Different exponent for order-`m`
odd is `m+1`; `2g_C-2=sum(m_P+1)`.

## 3. Theorem 1 — three 71-point genus-4 models (proof, computed)
For each cover, `f=N/D` evaluated at 43 `E` points:
defined 42/42/41, `Tr0` 34 each -> **68 affine lifts** `(x,y,z)`, `z^2+z=f`,
listed in `cover*_affine68.txt` (sorted, substitution-checkable).
No `N=D=0` rationally.  Poles: covers1,2 one rational `(23,29)`; cover3 two
`(2,28),(2,30)`.  Transversality: `Fx=y+x^2+1,Fy=x`, `D` normal `(1,a)`,
tangent iff `Fy=Fx*a`; all four fail (cover3 vertical `a=0` needs `x0!=0`,
`x0=r`).  Hence simple poles `v=-1`, each +1.  Non-rational poles: `D` line
meets cubic in 3 (non-vertical, infty off line) or 2+infty (vertical); with
1 (resp. 2) distinct rational simples the rest are conjugate simples
(orbit-size argument; tangent would force `2+1+1=4>3`).  So 3 simples over
closure in all cases.

Infinity (`t=x/y`, `(1+t)y+t^3y^2+t=0`, triangular `y_n+y_{n-1}=(t^3y^2)_n`,
pole branch `x=t^-2u^-1,y=t^-3u^-1`): all `v(f)=-2`, `Q0=c`, `s=sqrt(Q0)`,
`rem=Q1+s`.  Covers1,2 `rem=0`, regular `Q2` trace 0 -> split **+2**;
cover3 `rem=9!=0` -> ramified **+1**.  Stable trunc 12/16/20, residual 0.
Totals `68+1+2=71`, `68+1+2=71`, `68+2+1=71`.  Conductor `3*2+0=6` (covers1,2),
`2*2+2=6` (cover3) -> `2g-2=6`, `g=4`.  `verify_three.py` checks all.

## 4. Theorem 2 — vertical-univariate 1M contains no 72-pt genus-4 (proof)
Family `D=x+b`, `N=a x^2+b1 x+c` (1,048,576).  `b=0`: `D=x` tangent double at
`(0,0)` (`Fy=0`, normal `(1,0)` parallel), `v=2` even, after reduction affine
unramified, conductor from infty alone `<=4` -> `g<=2` or reducible
(`x+1/x`-type all-`Tr0` examples are `P`-equivalent to constants); Hasse–Weil
`g<=2` max `<=55<72`.  `b!=0`: transverse (as above), either `N(b)!=0`
(2 simples over closure, 0/2 rational) or `N(b)=0` (removable, no aff poles,
`g<=2`).  Genuine case `v_infty=-2` (`a!=0`; `a=0` gives `v=0` regular,
`g=3`).  If infty ramified, `g=4`, total `aff+kp+1` with `aff,kp` even
(`kp=0/2`) -> odd, never 72.  If infty regular, `g=3`, total even but
`N_32(3)=64` closed (Semirat tower + Lauter, per Details `q=32,g=3`) forbids
72.  Hence no smooth 72-pt genus-4 in the subfamily.  Exhaustive run (3.2s,
fast tables) corroborates: max `aff` among eligible `b!=0` is 68 -> max
genus-4 total 71.

## 5. Computed evidence — sampling (not proof)
`UB` filter above.  General `N(6)/D(3)` 300k random (seed 98765): best aff70,
29 `UB>=69`, 3 `UB>=72`; exact `v_infty=-3` ramified, `P` separable,
`gcd(P,Q)=1` -> 3 simples + order-3 infty = conductor 10 -> **genus 6**,
totals 72/71/71 genus-6, not genus-4.  Genus-4-eligible
`D=x+a y+b(a!=0),N=n0+n1x+n2y+n3x2+n4xy(n4!=0)` 300k (seed 20260907):
best aff82 tangent-double+removable (low genus); next aff70 with
`v=-2` ramified infty, `P` separable `gcd=1` -> 3 simples + simple infty =8
-> **genus 5**, totals 72/71/71 genus-5.  Fractions `~3e-7` and `~3e-4`;
seeds, `UB` definition, and top-candidate exact analyses in
`artifacts/search_summary.txt` and WORKLOG.  No 72-pt genus-4 observed.

## 6. Limitations, conjecture, uncertainty (do not overclaim)
- Interval **not** closed; residual RWP **not** eliminated; no 72-pt curve exhibited.
- `F1024` zeta moments not computed; RWP of the three models taken from Howe comment, not recomputed (would need `F1024` + point counts).
- Upper bound 72 and `(32,3)=64` taken from table/papers, not re-proved Magma-free.
- Sampling fractions tiny; negative sampling is evidence, not elimination.
- Originality: to our 2026-09-07 snapshot/arXiv/Crossref scan (per topic) no open-source recount exists; we claim only a Magma-independent check plus the 1M-subfamily proof, not a table change.  Any genus-5/6 72/71-pt models above are incidental higher-genus observations, not claimed as records (`N_32(5/6)` not checked).

## 7. Reproduce
`python3 artifacts/verify_three.py` (<2s) checks `E`, 68-lists by substitution,
poles, infty `Q`, totals, genus.  Lists use ints `0..31`, `r=2`,
`F2[r]/(r^5+r^2+1)`.
