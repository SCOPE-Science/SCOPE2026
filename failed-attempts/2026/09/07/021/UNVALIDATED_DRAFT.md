# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified bounded integral-point census with torsion and Hall extremum
## for sixth-power-free Mordell curves 10^7 < k <= 10^7+200 (partial result)

**Scope.** This is a *weakened, fully auditable* partial theorem toward the
lane target (Siegel-complete census via elliptic-log sieve). The full sieve,
rank upper bounds, saturated generators, Cremona canonical heights and
regulators are **not** claimed: no Sage/PARI was available (Python stdlib only)
and completeness for large x remains open. What is proved below is exact,
reproducible in seconds-to-minutes with pure Python integer arithmetic, and
clearly separates proof, computation, literature citation, and open remainder.

## 1. Objects

For integer k != 0 let

    E_k : y^2 = x^3 + k,   Delta = -432 k^2.

Put

    S = { k in Z : 10^7 < k <= 10^7+200, v_p(k) <= 5 for all primes p }.

E_k(Z) denotes affine integral points (x,y) in Z^2 satisfying the equation.
For P=(x,y) with x != 0 the Hall ratio is R(P)=sqrt(|x|)/|k|,
R(P)^2=|x|/k^2. Naive (logarithmic) heights used here are
h_x=log max(|x|,1), h_y=log max(|y|,1) (natural log, convenience floats;
exact integers |x|,|y| are the certified data).

## 2. Theorem (bounded census)

Let B=1_000_000, XMIN=-1000.

(a) **Stratum.** S has exactly 196 elements: all integers 10000001..10000200
    except 10000064, 10000128, 10000192 (divisible by 2^6=64) and 10000165
    (divisible by 7^6=117649). File `artifacts/S.csv`.

(b) **Torsion.** For every k in S, E_k(Q)_tors = {O}.
    - For 186 curves with v_2(k)<=3 and v_3(k)<=4 this is proved
      self-containedly via minimality + Nagell–Lutz (Section 3, zero
      candidates in `artifacts/lutz.csv`).
    - For all 196 (including the 10 valuation-exceptional curves listed in
      Section 3) it follows from the standard Mordell-curve torsion
      classification plus the exact verification that no k in S is a square
      or a cube. The classification itself is cited, not reproved.

(c) **Bounded completeness.** For each k in S let L_k(B) be the tabulated set
    in `artifacts/points.json` (pairs [x,y], y>=0; affine points are
    (x,±y), y=0 single). Then L_k(B) equals *exactly* the set of
    (x,y) in E_k(Z) with y>=0 and x<=B. Consequently any integral point not
    listed satisfies x>B. Every listed pair verifies y^2==x^3+k in integers.
    Counts: 23/196 curves nonempty; 29 x-values (y>=0); 58 affine points
    counting both signs. Full per-curve lists are in `points.json` /
    `bounded_summary.csv`; the 23 nonempty cases are:

    - 10000012: (93,3287)
    - 10000017: (-117,2898)
    - 10000020: (1141,38671)
    - 10000025: (10000,1000005)
    - 10000040: (-106,2968)
    - 10000044: (6333,503991)
    - 10000047: (14893,1817498)
    - 10000058: (1847,79441)
    - 10000060: (186,4054)
    - 10000068: (832,24206)
    - 10000079: (493,11394), (153793,60312156)
    - 10000097: (-212,687), (94,3291), (287,5800), (859,25374)
    - 10000098: (31,3167)
    - 10000105: (-204,1229)
    - 10000107: (14733,1788288)
    - 10000124: (50,3182), (301,6105), (1018,32634)
    - 10000133: (-173,2196)
    - 10000137: (58,3193)
    - 10000144: (680,18012)
    - 10000153: (-214,447)
    - 10000161: (240,4881)
    - 10000188: (42,3174)
    - 10000200: (121,3431)
    (each with ±y; y>=0 shown; e.g. (10000,1000005) since
    1000005^2=1000010000025=10000^3+10000025.)

(d) **Rank lower bounds.** Each of the 23 curves in (c) has Mordell–Weil rank
    r_k >= 1 (any integral affine point is of infinite order once torsion is
    trivial). The remaining 173 curves have r_k >= 0 (no lower bound beyond
    trivial). No rank upper bounds are claimed.

(e) **Hall extremum among found points.** Among all tabulated points with
    x!=0, the unique maximizer of R (hence of R^2) by exact integer comparison
    is P*=(k*,x*,y*)=(10000079,153793,60312156), with
    R^2=153793/10000079^2≈1.5379057e-9, R≈3.9216141e-5.
    It is also the largest-|x| found point. Maximality is certified by
    cross-multiplication (Section 4). No global Hall-maximality beyond x<=B
    is claimed. Naive heights and Hall ranking for all 29 x-values are in
    `artifacts/heights.csv`, `artifacts/hall.csv`; witness in
    `artifacts/witness.json`.

## 3. Proofs and computational certificates

**S enumeration.** p^6<=10000200 forces p<=14 (17^6=24137569>max), so only
p=2,3,5,7,11,13 can violate sixth-power-freeness. Trial division of each of
the 200 integers by 2^6,3^6,5^6,7^6,11^6,13^6 is exact. Yields the 4 exclusions
above. Rerun: `enumerate.py`. No other prime power can divide any k in the
interval to the 6th power.

**No squares/cubes.** 3162^2=9998244<10^7<10000200<10004569=3163^2, so no
square lies in (10^7,10^7+200]; exact `math.isqrt` per k confirms.
215^3=9938375<10^7<10000200<10077696=216^3, so no cube; per-k exact binary
search confirms. Hence the torsion-classification premise holds.

**Torsion lemma (cited).** Standard: for E: y^2=x^3+k over Q with k>0
sixth-power-free, points of order 2 satisfy y=0 i.e. x^3=-k (k a cube) and
points of order 3 satisfy x=0 i.e. y^2=k (k a square); CM/Mazur theory excludes
other torsion (torsion is 1,2,3,6; both 2- and 3-torsion would force k a sixth
power, impossible here except k=1). See e.g. Silverman, *Arithmetic of
Elliptic Curves*, Chap. X / *Advanced Topics*; Knapp, *Elliptic Curves*;
Fueter classification; LMFDB Mordell-curve documentation. We use this as a
premise; our verified contribution is the square/cube check, not a new proof
of the classification.

**Self-contained Lutz check (186 curves).** Delta=-432k^2. For p>=5,
v_p(Delta)=2v_p(k)<=10<12. For p=2, v_2(Delta)=4+2v_2(k)<12 iff v_2(k)<=3;
for p=3, v_3(Delta)=3+2v_3(k)<12 iff v_3(k)<=4. Hence curves with v_2<=3 and
v_3<=4 have v_p(Delta)<12 at every p and the model y^2=x^3+k is globally
minimal. Nagell–Lutz then applies: torsion (x,y) is integral with y=0 or
y^2|Delta. Since Delta=-2^4·3^3·k^2, y^2|Delta iff y|12k. For each of the 186
minimal curves we enumerated all divisors y of D=12k and tested exactly whether
(y^2-k) is a nonnegative perfect cube (x^3). Result: zero candidates on all
186 (`lutz.py/csv`). The y=0 case is the cube condition already excluded.
Hence torsion trivial for those 186 with no literature black box.
The 10 valuation-exceptional curves are
10000016,10000032,10000048,10000080,10000096,10000112,10000144,10000160,
10000176 (v_2>=4) and 10000179 (v_3=5); for these torsion-triviality rests on
the cited classification (they also show zero y|12k candidates, recorded as
consistency only, since Lutz needs minimality).

**Bounded search (proof of (c)).** Fix k. If x^3+k<0 there is no y. Since
XMIN^3+max(S)=-1000^3+10000200=-989999800<0 and x^3 is increasing, every
x<XMIN has x^3+k<0 for every k in S. Thus {x : x^3+k>=0, x<=B} ⊆ [XMIN,B].
The program loops exactly over x=XMIN..B, computes v=x^3+k in integers,
y=isqrt(v), records iff y^2==v. By construction this finds *all* integral
points with x<=B (and no others). Each recorded pair re-verifies by integer
substitution. `verify.py` rechecks all substitutions in <2s; full search
reruns deterministically in ~37s (`search_bounded.py`, `rerun.sh`).

**Rank >=1.** If torsion is trivial, any affine rational (in particular
integral) point != O has infinite order, so the free rank is >=1. Applies to
the 23 curves; for k=10000144 (valuation-exceptional) this uses the cited
torsion lemma, for the other 22 the self-contained Lutz torsion proof suffices.

## 4. Hall maximizer certificate

For x!=0, R1>R2 ⟺ sqrt(|x1|)/k1 > sqrt(|x2|)/k2 ⟺ |x1|k2^2>|x2|k1^2, pure
integers (k>0). `verify.py` recomputes the maximum over the 29 tabulated
nonzero-x entries by this exact comparison and checks equality with
`witness.json`. No floating point enters the maximality proof; the decimal
R values quoted are convenience evaluations. Largest |x| coincides with Hall
max here because k varies by <0.002%.

## 5. Limitations and open remainder (explicit non-claims)

- No Siegel completeness: points with x>B=1e6 are uncertified; 173/196 curves
  are empty up to B but may have larger points (expected: integral points of
  rank->0 curves can have x >> 1e6; cf. Pasten's |k|^{1/2+eps} log-bound, which
  for |k|~1e7 is astronomically larger than B).
- No rank intervals/generators/saturation, no 2-descent/Selmer, no analytic
  rank or BSD cross-check, no elliptic-log (David/LLL) height bounds or sieve
  logs. The lane audit plan Steps 2–3,5 (canonical heights/regulators) are not
  executed.
- Canonical (Cremona/PARI-normalized Neron–Tate) heights and regulators are
  not given; only exact integers (|x|,|y|) and convenience naive logs plus
  Hall ratios. Do not interpret naive logs as canonical heights.
- Torsion for 10/196 curves depends on the cited classification; all else is
  self-contained integer arithmetic.
- Local-modular emptiness search (m<500) found nothing; this is reported as a
  failed attempt, not a result.
- Relation to Bennett–Ghadermarzi (|k|<=1e7, Thue method): our block lies
  strictly above their range; method (bounded enumeration) and artifact
  (lower-bound lists + torsion + Hall table) differ. No priority claim over
  their completeness; no per-k lists are duplicated.

## 6. Reproducibility

All artifacts under `output/artifacts/` (verification-critical only):
`S.csv`, `points.json`, `bounded_summary.csv`, `torsion.csv`, `lutz.csv`,
`heights.csv`, `hall.csv`, `witness.json`, `verify.py`, `rerun.sh`,
`enumerate.py`, `torsion_check.py`, `search_bounded.py`, `build_tables.py`,
`lutz_check.py`. Rerun: `bash rerun.sh` (needs only CPython 3.12 stdlib;
~40s dominated by bounded search) then `python3 verify.py` (<2s) prints
ALL CHECKS PASSED. Python version used: 3.12.3. No seeds/randomness; all loops
deterministic. Complete code and logs are the certificate; no CAS required.

## References (motivation/background, not reproved)

- Bennett–Ghadermarzi, Mordell's equation: a classical approach (2015,
  arXiv:1311.7077): solves |k|<=1e7 via Thue equations; motivates
  beyond-threshold block.
- Gebel–Pethő–Zimmer–Herrmann, Computing all S-integral points (1997):
  Siegel–Baker–Coates/Lang–Zagier sieve background.
- Ghadermarzi, Multiples of integral points on Mordell curves (2022).
- Pasten (2026), Power-saving bounds for Mordell equations.
- D'Mello (2014), Hall's conjecture gaps.
- Silverman, *Arithmetic of Elliptic Curves* / *Advanced Topics*; Knapp,
  *Elliptic Curves*; Fueter torsion classification; Mazur torsion theorem —
  for torsion-premise provenance.
